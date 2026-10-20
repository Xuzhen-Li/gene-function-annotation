"""Tests for the F0 stop clean-up, F8 NLR classes, the F_merge_tables wrapper,
missing-input errors and the F1/F2/F3/F_release command defaults. Stdlib only."""
import io
import os
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "pipeline"))
import F0_clean_proteins as f0  # noqa: E402
import F8_list_nlr_from_ips as f8  # noqa: E402
import F_aggregate as agg  # noqa: E402
import F_merge_tables as fmt  # noqa: E402

TOY = ROOT / "testdata" / "function"
EXPECTED = TOY / "expected" / "merged_function_table.tsv"


def quiet(fn, *args):
    out, err = io.StringIO(), io.StringIO()
    with redirect_stdout(out), redirect_stderr(err):
        rc = fn(*args)
    return rc, out.getvalue(), err.getvalue()


def ips_line(pid, analysis, acc, desc="-", ipr="-"):
    return "\t".join([pid, "md5", "900", analysis, acc, desc, "1", "100", "1e-20", "T",
                      "19-10-2026", ipr, "-", "-"]) + "\n"


class TestNLR(unittest.TestCase):
    def run_f8(self, lines):
        with tempfile.TemporaryDirectory() as d:
            ips, out = Path(d, "ips.tsv"), Path(d, "nlr.tsv")
            ips.write_text("".join(lines))
            rc, _, _ = quiet(f8.main, ["--ips", str(ips), "--out", str(out)])
            self.assertEqual(rc, 0)
            rows = [r.split("\t") for r in out.read_text().splitlines()]
        self.assertEqual(rows[0], f8.COLUMNS)
        return {r[0]: r for r in rows[1:]}

    def test_classes(self):
        got = self.run_f8([
            # CNL: coiled coil (Coils) + NB-ARC + LRR
            ips_line("cnl", "Coils", "Coil"), ips_line("cnl", "Pfam", "PF00931", "NB-ARC", "IPR002182"),
            ips_line("cnl", "Pfam", "PF13855", "LRR_8", "IPR001611"),
            # CNL via Rx_N
            ips_line("rx", "Pfam", "PF18052", "Rx_N", "IPR041118"), ips_line("rx", "Pfam", "PF00931"),
            ips_line("rx", "Pfam", "PF00560"),
            # TNL
            ips_line("tnl", "Pfam", "PF01582", "TIR", "IPR000157"), ips_line("tnl", "Pfam", "PF00931"),
            ips_line("tnl", "Pfam", "PF00560", "LRR_1", "IPR001611"),
            # RNL
            ips_line("rnl", "Pfam", "PF05659", "RPW8", "IPR008808"), ips_line("rnl", "Pfam", "PF00931"),
            ips_line("rnl", "Pfam", "PF13516"),
            # TN (no LRR), NL (no N-terminal domain), N (NB-ARC only, via InterPro entry only)
            ips_line("tn", "Pfam", "PF01582"), ips_line("tn", "Pfam", "PF00931"),
            ips_line("nl", "Pfam", "PF00931"), ips_line("nl", "SMART", "SM00369"),
            ips_line("n", "PANTHER", "PTHR23155", "-", "IPR002182"),
        ])
        want = {"cnl": "CNL", "rx": "CNL", "tnl": "TNL", "rnl": "RNL", "tn": "TN", "nl": "NL", "n": "N"}
        self.assertEqual({k: v[1] for k, v in got.items()}, want)
        self.assertEqual(got["tnl"][2:4], ["TIR", "yes"])
        self.assertEqual(got["n"][2:4], ["-", "no"])

    def test_requires_nbarc(self):
        got = self.run_f8([
            # LRR receptor kinase: LRR + kinase, no NB-ARC -> not an NLR
            ips_line("rlk", "Pfam", "PF00560", "LRR_1", "IPR001611"),
            ips_line("rlk", "Pfam", "PF00069", "Pkinase", "IPR000719"),
            # receptor-like protein: LRR only
            ips_line("rlp", "Pfam", "PF13855", "LRR_8", "IPR001611"),
            # TIR-only and RPW8-only proteins
            ips_line("tir", "Pfam", "PF01582", "TIR", "IPR000157"),
            ips_line("rpw8", "Pfam", "PF05659", "RPW8", "IPR008808"),
            # keyword in a description must not be enough
            ips_line("kw", "PANTHER", "PTHR0001", "disease resistance protein"),
        ])
        self.assertEqual(got, {})

    def test_missing_ips_is_clean_error(self):
        rc, _, err = quiet(f8.main, ["--ips", "/nonexistent/ips.tsv", "--out", "/tmp/x.tsv"])
        self.assertEqual(rc, 1)
        self.assertIn("[ERR]", err)


class TestStopStrip(unittest.TestCase):
    def test_clean(self):
        self.assertEqual(f0.clean("MKV*"), ("MKV", 1, []))
        self.assertEqual(f0.clean("MKV."), ("MKV", 1, []))
        self.assertEqual(f0.clean("MKV.*"), ("MKV", 2, []))
        self.assertEqual(f0.clean("MKVL"), ("MKVL", 0, []))
        self.assertEqual(f0.clean("MK*V.L*"), ("MK*V.L", 1, [3, 5]))

    def run_f0(self, fasta, *extra):
        d = tempfile.mkdtemp()
        inp, out, rep = Path(d, "in.faa"), Path(d, "out.faa"), Path(d, "stops.tsv")
        inp.write_text(fasta)
        rc, _, err = quiet(f0.main, ["--in", str(inp), "--out", str(out), "--report", str(rep), *extra])
        return rc, out, rep, err

    def test_file(self):
        fa = ">g1 desc\nMKVL\nAA*\n>g2\nMKV.\n>g3\nMK*VL\nQ.\n"
        rc, out, rep, err = self.run_f0(fa)
        self.assertEqual(rc, 0)
        self.assertEqual(out.read_text(), ">g1 desc\nMKVLAA\n>g2\nMKV\n>g3\nMK*VLQ\n")
        lines = rep.read_text().splitlines()
        self.assertEqual(lines[1:], ["g3\t6\t1\t3\tkept"])
        self.assertIn("internal_stop=1", err)
        self.assertIn("[WARN]", err)

    def test_drop_internal(self):
        rc, out, rep, _ = self.run_f0(">g1\nMKV*\n>g3\nMK*VL*\n", "--drop-internal")
        self.assertEqual(rc, 0)
        self.assertEqual(out.read_text(), ">g1\nMKV\n")
        self.assertTrue(rep.read_text().splitlines()[1].endswith("dropped"))

    def test_errors(self):
        rc, _, err = quiet(f0.main, ["--in", "/nonexistent.faa", "--out", "/tmp/o.faa", "--report", "/tmp/r.tsv"])
        self.assertEqual((rc, "[ERR]" in err), (1, True))
        with tempfile.TemporaryDirectory() as d:
            p = Path(d, "a.faa")
            p.write_text(">g\nMK*\n")
            rc, _, err = quiet(f0.main, ["--in", str(p), "--out", str(p), "--report", str(Path(d, "r"))])
            self.assertEqual(rc, 1)
            self.assertEqual(p.read_text(), ">g\nMK*\n")


TOY_LEGACY = ["--proteins", str(TOY / "toy.faa"), "--emapper", str(TOY / "toy.emapper.annotations"),
              "--ips", str(TOY / "toy.ips.tsv"), "--diamond", str(TOY / "toy.diamond.tsv")]


class TestWrapperAndToy(unittest.TestCase):
    def test_argv_mapping(self):
        new, errs = fmt.build_argv(TOY_LEGACY + ["--out", "o.tsv", "--db-version", "x=1@2026-01-01"])
        self.assertEqual(errs, [])
        self.assertIn("--diamond-swissprot", new)
        self.assertNotIn("--diamond", new)
        self.assertEqual(new[-2:], ["--db-version", "x=1@2026-01-01"])

    def test_toy_expected_via_wrapper_and_aggregate(self):
        with tempfile.TemporaryDirectory() as d:
            o1, o2 = Path(d, "w", "merged_function_table.tsv"), Path(d, "a", "merged_function_table.tsv")
            rc, _, err = quiet(fmt.main, TOY_LEGACY + ["--out", str(o1)])
            self.assertEqual(rc, 0)
            self.assertIn("[DEPRECATED]", err)
            args = [x if x != "--diamond" else "--diamond-swissprot" for x in TOY_LEGACY]
            rc, _, _ = quiet(agg.main, args + ["--out", str(o2)])
            self.assertEqual(rc, 0)
            self.assertEqual(o1.read_text(), EXPECTED.read_text())
            self.assertEqual(o2.read_text(), EXPECTED.read_text())

    def test_optional_inputs_can_be_left_out(self):
        with tempfile.TemporaryDirectory() as d:
            o = Path(d, "merged_function_table.tsv")
            rc, _, _ = quiet(fmt.main, ["--proteins", str(TOY / "toy.faa"),
                                        "--diamond", str(TOY / "toy.diamond.tsv"), "--out", str(o)])
            self.assertEqual(rc, 0)
            self.assertEqual(len(o.read_text().splitlines()), 3)


class TestMissingInput(unittest.TestCase):
    def check_cli(self, script, args):
        r = subprocess.run([sys.executable, str(ROOT / "pipeline" / script), *args],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 1, r.stderr)
        self.assertNotIn("Traceback", r.stderr)
        return r.stderr

    def test_wrapper_missing_ips(self):
        with tempfile.TemporaryDirectory() as d:
            err = self.check_cli("F_merge_tables.py", [
                "--proteins", str(TOY / "toy.faa"), "--ips", str(Path(d, "nope_ips.tsv")),
                "--out", str(Path(d, "o.tsv"))])
            self.assertIn("--ips file not found", err)
            self.assertIn("leave out --ips", err)
            self.assertFalse(Path(d, "o.tsv").exists())

    def test_aggregate_missing_inputs(self):
        with tempfile.TemporaryDirectory() as d:
            err = self.check_cli("F_aggregate.py", [
                "--proteins", str(Path(d, "nope.faa")), "--emapper", str(Path(d, "nope.emapper")),
                "--out", str(Path(d, "o.tsv"))])
            self.assertIn("--proteins file not found", err)
            self.assertIn("--emapper file not found", err)


class TestScriptDefaults(unittest.TestCase):
    def dry(self, script, **env):
        base = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "WORK_DIR": "/tmp/gfa_test_work",
                "PROTEINS_FA": "/tmp/gfa_test.faa"}
        base.update(env)
        return subprocess.run(["bash", str(ROOT / "pipeline" / script)], env=base,
                              capture_output=True, text=True)

    def test_f1_diamond(self):
        r = self.dry("F1_diamond.sh", DIAMOND_DB="/tmp/sp.dmnd")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("--more-sensitive", r.stdout)
        self.assertIn("stitle qlen slen qcovhsp scovhsp", r.stdout)
        self.assertIn("RUN=1 bash pipeline/F1_diamond.sh", r.stdout)
        self.assertNotIn("export RUN=1", r.stdout)

    def test_f2_eggnog(self):
        r = self.dry("F2_eggnog.sh")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("--pfam_realign none", r.stdout)
        self.assertIn("--tax_scope Viridiplantae", r.stdout)
        self.assertIn("RUN=1 bash pipeline/F2_eggnog.sh", r.stdout)
        bad = self.dry("F2_eggnog.sh", EGGNOG_PFAM_REALIGN="realtime")
        self.assertEqual(bad.returncode, 1)
        self.assertIn("none, realign or denovo", bad.stderr)

    def test_f3_interproscan(self):
        r = self.dry("F3_interproscan.sh", INTERPROSCAN_HOME="/tmp/ips")
        self.assertEqual(r.returncode, 0, r.stderr)
        for flag in ("-goterms", "-iprlookup", "-pa"):
            self.assertIn(f" {flag} ", r.stdout)

    def test_release_rejects_placeholder(self):
        r = self.dry("F_release.sh", WORK_DIR="/path/to/work", RELEASE_TAG="t1")
        self.assertEqual(r.returncode, 1)
        self.assertIn("still /path/to", r.stderr)
        self.assertNotIn("Permission denied", r.stderr)

    def test_release_uses_merged_function_table(self):
        with tempfile.TemporaryDirectory() as d:
            fun = Path(d, "function")
            (fun / "merge").mkdir(parents=True)
            (fun / "merge" / "merged_function_table.tsv").write_text(EXPECTED.read_text())
            prot = Path(d, "p.faa")
            prot.write_text(">geneA\nMK\n")
            r = self.dry("F_release.sh", WORK_DIR=d, PROTEINS_FA=str(prot), RELEASE_TAG="t1")
            self.assertEqual(r.returncode, 0, r.stderr)
            rel = fun / "release" / "t1"
            self.assertEqual((rel / "merged_function_table.tsv").read_text(), EXPECTED.read_text())


if __name__ == "__main__":
    unittest.main()
