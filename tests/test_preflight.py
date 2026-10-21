"""Tests for pipeline/preflight.py (standard library only).

Run:  python3 -m unittest discover -s tests -v
Tools are faked with small executables in a temporary PATH folder.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PREFLIGHT = REPO / "pipeline" / "preflight.py"
sys.path.insert(0, str(REPO / "pipeline"))
import preflight  # noqa: E402


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="pf_"))
        self.bin = self.tmp / "bin"
        self.bin.mkdir()

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def fake_tool(self, *names):
        for n in names:
            p = self.bin / n
            p.write_text("#!/bin/sh\nexit 0\n")
            p.chmod(0o755)

    def touch(self, rel, text="x\n"):
        p = self.tmp / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
        return p

    def env_file(self, body):
        p = self.tmp / "local.env"
        p.write_text(textwrap.dedent(body).replace("@T", str(self.tmp)))
        return p

    def run_pf(self, *args):
        env = {"PATH": str(self.bin), "HOME": str(self.tmp)}
        return subprocess.run([sys.executable, str(PREFLIGHT), *args], env=env,
                              capture_output=True, text=True, cwd=self.tmp)


class EnvParsingTests(Base):
    def test_expansion_quotes_comments(self):
        p = self.env_file("""
            WORK_DIR="@T/work"   # comment
            export DRAFT_GFF="$WORK_DIR/draft/a.gff3"
            OUT="${MISSING:-@T/default}"
            LIT='$WORK_DIR/x'
            HASH="a#b"
        """)
        env = preflight.load_env(p, base={})
        self.assertEqual(env["WORK_DIR"], f"{self.tmp}/work")
        self.assertEqual(env["DRAFT_GFF"], f"{self.tmp}/work/draft/a.gff3")
        self.assertEqual(env["OUT"], f"{self.tmp}/default")
        self.assertEqual(env["LIT"], "$WORK_DIR/x")
        self.assertEqual(env["HASH"], "a#b")

    def test_placeholders(self):
        pr = preflight.placeholder_reason
        self.assertIn("/path/to", pr("/path/to/work"))
        self.assertIn("YOUR_", pr("YOUR_BUSCO_LINEAGE_odb12"))
        self.assertIn("$(...)", pr("$(pwd)/x"))
        self.assertIn("unset", pr("$NOPE/x"))
        self.assertEqual(pr(""), "empty")
        self.assertIsNone(pr("/data/genome.fa"))

    def test_env_file_read_without_export(self):
        # values only in the file (not exported in the shell) are still seen
        p = self.env_file("WORK_DIR=@T/work\n")
        res = self.run_pf("--env", str(p), "--step", next(iter(preflight.STEPS)))
        self.assertIn(f"WORK_DIR can be written: {self.tmp}/work", res.stdout)


class CliTests(Base):
    def test_list(self):
        res = self.run_pf("--list")
        self.assertEqual(res.returncode, 0)
        for name in preflight.STEPS:
            self.assertIn(name, res.stdout)

    def test_no_step_is_usage_error(self):
        self.assertEqual(self.run_pf().returncode, 2)

    def test_missing_env_file(self):
        res = self.run_pf("--env", str(self.tmp / "nope.env"), "--step", next(iter(preflight.STEPS)))
        self.assertEqual(res.returncode, 1)
        self.assertIn("env file not found", res.stdout)

    def test_example_env_stops(self):
        res = self.run_pf("--env", str(REPO / "config" / "example.env"), "--step",
                          next(iter(preflight.STEPS)))
        self.assertEqual(res.returncode, 1)
        self.assertIn("[STOP]", res.stdout)
        self.assertIn("Do not use RUN=1 yet", res.stdout)

    def test_command_substitution_stops(self):
        p = self.env_file('WORK_DIR="$(pwd)/work"\n')
        res = self.run_pf("--env", str(p), "--step", next(iter(preflight.STEPS)))
        self.assertEqual(res.returncode, 1)
        self.assertIn("not evaluated", res.stdout)


class PrintQcWordingTests(unittest.TestCase):
    def test_print_qc_points_to_preflight(self):
        text = (REPO / "pipeline" / "print_qc_commands.py").read_text(encoding="utf-8")
        self.assertIn("preflight.py", text)
        self.assertNotIn("not a RUN=1 plan", text)
        self.assertNotIn("RUN=1 yet", text)


class FunctionStepTests(Base):
    def base_env(self, extra=""):
        self.touch("struct/release/sp.v1/proteins.faa", ">p1\nMK\n")
        return self.env_file("""
            WORK_DIR="@T/work"
            FUNCTION_DIR="$WORK_DIR/function"
            PROTEINS_FA="@T/struct/release/sp.v1/proteins.faa"
            FUN_PREFIX="ann"
            RELEASE_TAG="sp_fun.v1"
        """ + textwrap.dedent(extra))

    def test_diamond_pass(self):
        self.touch("db/swissprot.dmnd")
        self.fake_tool("diamond")
        p = self.base_env('DIAMOND_DB="@T/db/swissprot.dmnd"\n')
        res = self.run_pf("--env", str(p), "--step", "diamond")
        self.assertEqual(res.returncode, 0, res.stdout)
        self.assertIn("RUN=1 bash pipeline/F1_diamond.sh", res.stdout)

    def test_diamond_db_missing_and_tool_missing(self):
        p = self.base_env('DIAMOND_DB="@T/db/none.dmnd"\n')
        res = self.run_pf("--env", str(p), "--step", "diamond")
        self.assertEqual(res.returncode, 1)
        self.assertIn("DIAMOND_DB not found", res.stdout)
        self.assertIn("tool DIAMOND not found", res.stdout)

    def test_proteins_missing_names_structure_repo(self):
        p = self.env_file('WORK_DIR="@T/work"\nPROTEINS_FA="@T/none.faa"\nDIAMOND_DB="@T/x"\n')
        res = self.run_pf("--env", str(p), "--step", "diamond")
        self.assertIn("gene-structure-annotation", res.stdout)

    def test_proteins_not_from_release_warns(self):
        self.touch("db/swissprot.dmnd")
        self.touch("loose.faa")
        self.fake_tool("diamond")
        p = self.base_env('DIAMOND_DB="@T/db/swissprot.dmnd"\nPROTEINS_FA="@T/loose.faa"\n')
        res = self.run_pf("--env", str(p), "--step", "diamond")
        self.assertEqual(res.returncode, 0, res.stdout)
        self.assertIn("Gate-F1", res.stdout)

    def test_eggnog_pfam_realign(self):
        self.fake_tool("emapper.py")
        p = self.base_env()
        res = self.run_pf("--env", str(p), "--step", "eggnog")
        self.assertEqual(res.returncode, 1)
        self.assertIn("realtime", res.stdout)
        for val, code in (("realtime", 1), ("none", 0), ("denovo", 0)):
            p = self.base_env(f'EGGNOG_PFAM_REALIGN="{val}"\n')
            self.assertEqual(self.run_pf("--env", str(p), "--step", "eggnog").returncode, code, val)

    def test_eggnog_container_route(self):
        self.touch("emapper.sif")
        self.fake_tool("singularity")
        p = self.base_env('EGGNOG_SIF="@T/emapper.sif"\nEGGNOG_PFAM_REALIGN="none"\n')
        res = self.run_pf("--env", str(p), "--step", "eggnog")
        self.assertEqual(res.returncode, 0, res.stdout)
        self.assertIn("container", res.stdout)

    def test_eggnog_data_dir_set_but_missing(self):
        self.fake_tool("emapper.py")
        p = self.base_env('EGGNOG_PFAM_REALIGN="none"\nEGGNOG_DATA_DIR="@T/nodata"\n')
        res = self.run_pf("--env", str(p), "--step", "eggnog")
        self.assertEqual(res.returncode, 1)
        self.assertIn("EGGNOG_DATA_DIR is set but not found", res.stdout)

    def test_interproscan_home(self):
        self.fake_tool("java")
        home = self.tmp / "ips"
        home.mkdir()
        p = self.base_env('INTERPROSCAN_HOME="@T/ips"\n')
        self.assertEqual(self.run_pf("--env", str(p), "--step", "interproscan").returncode, 1)
        sh = home / "interproscan.sh"
        sh.write_text("#!/bin/sh\n")
        sh.chmod(0o755)
        res = self.run_pf("--env", str(p), "--step", "interproscan")
        self.assertEqual(res.returncode, 0, res.stdout)

    def test_kofam_keys(self):
        self.fake_tool("exec_annotation")
        p = self.base_env()
        res = self.run_pf("--env", str(p), "--step", "kofam")
        self.assertEqual(res.returncode, 1)
        self.assertIn("KOFAM_KO_LIST", res.stdout)
        self.touch("kofam/ko_list")
        (self.tmp / "kofam" / "profiles").mkdir()
        p = self.base_env('KOFAM_KO_LIST="@T/kofam/ko_list"\nKOFAM_PROFILE_DIR="@T/kofam/profiles"\n')
        self.assertEqual(self.run_pf("--env", str(p), "--step", "kofam").returncode, 0)

    def test_merge_needs_one_result(self):
        p = self.base_env()
        res = self.run_pf("--env", str(p), "--step", "merge")
        self.assertEqual(res.returncode, 1)
        self.touch("work/function/diamond/swissprot.tsv")
        res = self.run_pf("--env", str(p), "--step", "merge")
        self.assertEqual(res.returncode, 0, res.stdout)
        self.assertIn("[WARN] eggNOG result not found", res.stdout)
        self.assertIn("F_merge_tables.py", res.stdout)

    def test_release_needs_master(self):
        p = self.base_env()
        self.assertEqual(self.run_pf("--env", str(p), "--step", "release").returncode, 1)
        self.touch("work/function/merge/merged_function_table.tsv")
        res = self.run_pf("--env", str(p), "--step", "release")
        self.assertEqual(res.returncode, 0, res.stdout)
        self.assertIn("F_release.sh", res.stdout)

    def test_function_dir_defaults_to_work(self):
        self.touch("struct/release/sp.v1/proteins.faa")
        p = self.env_file('WORK_DIR="@T/work"\nPROTEINS_FA="@T/struct/release/sp.v1/proteins.faa"\n'
                          'RELEASE_TAG="t"\n')
        self.touch("work/function/merge/merged_function_table.tsv")
        self.assertEqual(self.run_pf("--env", str(p), "--step", "release").returncode, 0)

    def test_orthofinder_needs_two_proteomes(self):
        self.fake_tool("orthofinder")
        p = self.base_env()
        self.touch("work/function/orthofinder/input/a.faa")
        self.assertEqual(self.run_pf("--env", str(p), "--step", "orthofinder").returncode, 1)
        self.touch("work/function/orthofinder/input/b.faa")
        self.assertEqual(self.run_pf("--env", str(p), "--step", "orthofinder").returncode, 0)

    def test_two_steps_one_stop(self):
        self.fake_tool("diamond")
        self.touch("db/swissprot.dmnd")
        p = self.base_env('DIAMOND_DB="@T/db/swissprot.dmnd"\n')
        res = self.run_pf("--env", str(p), "--step", "diamond", "--step", "itak")
        self.assertEqual(res.returncode, 1)
        self.assertIn("RESULT diamond: PASS", res.stdout)
        self.assertIn("RESULT itak: STOP", res.stdout)


if __name__ == "__main__":
    unittest.main()
