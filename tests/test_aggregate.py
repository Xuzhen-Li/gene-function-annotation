"""Tests for pipeline/F_aggregate.py using the simulated inputs in testdata/function_aggregate/."""
import csv
import io
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "pipeline"))
import F_aggregate as agg  # noqa: E402

D = ROOT / "testdata" / "function_aggregate"
EXPECTED_HEADER = [
    "gene_id", "ips_domains", "ips_domain_desc", "ips_ipr", "ips_go",
    "eggnog_og", "eggnog_name", "eggnog_description", "eggnog_go", "eggnog_ko",
    "diamond_db", "diamond_hit", "diamond_name", "diamond_evalue", "diamond_pident",
    "diamond_qcov", "diamond_scov", "kofam_ko", "final_name", "final_name_source",
    "go_terms", "go_evidence", "go_source", "db_versions",
]
FULL_ARGS = [
    "--proteins", str(D / "sim.faa"),
    "--ips", str(D / "sim.ips.tsv"),
    "--emapper", str(D / "sim.emapper.annotations"),
    "--diamond-swissprot", str(D / "sim.diamond.swissprot.tsv"),
    "--diamond-trembl", str(D / "sim.diamond.trembl.tsv"),
    "--kofam", str(D / "sim.kofam.detail.txt"),
    "--db-versions-file", str(D / "sim.db_versions.tsv"),
]


def run(extra, base=FULL_ARGS):
    out = Path(tempfile.mkdtemp()) / "merged.tsv"
    with redirect_stderr(io.StringIO()), redirect_stdout(io.StringIO()):
        rc = agg.main(list(base) + list(extra) + ["--out", str(out)])
    assert rc == 0, rc
    with open(out, newline="") as f:
        header = f.readline().rstrip("\n").split("\t")
        f.seek(0)
        rows = {r["gene_id"]: r for r in csv.DictReader(f, delimiter="\t")}
    return header, rows


def write(tmp, name, text):
    p = Path(tmp) / name
    p.write_text(text)
    return str(p)


class TestHeaderAndExample(unittest.TestCase):
    def test_exact_header(self):
        header, _ = run([])
        self.assertEqual(header, EXPECTED_HEADER)
        self.assertEqual(agg.COLUMNS, EXPECTED_HEADER)

    def test_header_matches_schema_if_present(self):
        if not agg.DEFAULT_SCHEMA.is_file():
            self.skipTest("pipeline/schema/merged_function_table.tsv not on this branch")
        with open(agg.DEFAULT_SCHEMA, newline="") as f:
            cols = [r["column"] for r in csv.DictReader(f, delimiter="\t")]
        if "go_source" not in cols:  # PR #1 schema without go_source: script adds it
            cols.insert(cols.index("go_evidence") + 1, "go_source")
        self.assertEqual(cols, EXPECTED_HEADER)

    def test_schema_check_strict(self):
        with tempfile.TemporaryDirectory() as t:
            base = [c for c in EXPECTED_HEADER if c != "go_source"]
            ok = write(t, "ok.tsv", "column\trequired\n" + "".join(f"{c}\tyes\n" for c in base))
            agg.check_schema(Path(ok))  # schema without go_source is accepted
            bad = write(t, "bad.tsv", "column\trequired\n" + "".join(f"{c}\tyes\n" for c in base[:-1]))
            with self.assertRaises(SystemExit):
                agg.check_schema(Path(bad))

    def test_matches_expected_output(self):
        out = Path(tempfile.mkdtemp()) / "m.tsv"
        with redirect_stderr(io.StringIO()), redirect_stdout(io.StringIO()):
            agg.main(FULL_ARGS + ["--out", str(out)])
        self.assertEqual(out.read_text(), (D / "expected" / "merged_function_table.tsv").read_text())


class TestNamePriority(unittest.TestCase):
    """Order: passing Swiss-Prot > eggNOG preferred name > InterProScan domain > uncharacterized."""

    def setUp(self):
        _, self.rows = run([])

    def test_1_swissprot_wins(self):
        r = self.rows["FAKE_g0001"]  # also has eggNOG ADH1 and Pfam domains
        self.assertEqual((r["final_name"], r["final_name_source"]), ("Alcohol dehydrogenase 1", "swissprot"))
        self.assertEqual(r["diamond_db"], "swissprot")

    def test_2_eggnog_preferred_name_when_swissprot_fails(self):
        r = self.rows["FAKE_g0002"]  # SP pident 25 < 30; eggNOG WRKY33; Pfam WRKY; passing TrEMBL
        self.assertEqual((r["final_name"], r["final_name_source"]), ("similar to WRKY33", "eggnog"))
        self.assertEqual(r["diamond_db"], "trembl")  # TrEMBL shown in diamond_* but does not name

    def test_3_domain_only_when_no_swissprot_or_eggnog_name(self):
        r = self.rows["FAKE_g0007"]  # SP scov 40 < 50; no eggNOG; Pfam protein kinase
        self.assertEqual((r["final_name"], r["final_name_source"]),
                         ("Protein kinase domain-containing protein", "interproscan_domain"))

    def test_3b_eggnog_without_preferred_name_falls_through_to_domain(self):
        base = list(FULL_ARGS)
        i = base.index("--emapper")
        with tempfile.TemporaryDirectory() as t:
            em = write(t, "e.annotations",
                       "#query\teggNOG_OGs\tmax_annot_lvl\tDescription\tPreferred_name\tGOs\tKEGG_ko\n"
                       "FAKE_g0002\tKOG1@2759|Eukaryota\t2759|Eukaryota\tWRKY transcription factor\t-\t-\t-\n")
            base[i + 1] = em
            _, rows = run([], base=base)
        self.assertEqual((rows["FAKE_g0002"]["final_name"], rows["FAKE_g0002"]["final_name_source"]),
                         ("WRKY domain-containing protein", "interproscan_domain"))

    def test_4_eggnog_description_only_is_uncharacterized(self):
        r = self.rows["FAKE_g0003"]  # eggNOG Preferred_name '-'
        self.assertEqual((r["final_name"], r["final_name_source"]), ("uncharacterized protein", "none"))
        self.assertEqual(r["eggnog_description"], "Methyltransferase domain")

    def test_4_trembl_only_never_names(self):
        for g in ("FAKE_g0004", "FAKE_g0005"):  # passing TrEMBL hits, informative and not
            r = self.rows[g]
            self.assertEqual(r["diamond_db"], "trembl")
            self.assertEqual((r["final_name"], r["final_name_source"]), ("uncharacterized protein", "none"))
        for r in self.rows.values():
            self.assertNotEqual(r["final_name_source"], "trembl")

    def test_4_no_source_is_uncharacterized(self):
        r = self.rows["FAKE_g0006"]
        self.assertEqual((r["final_name"], r["final_name_source"]), ("uncharacterized protein", "none"))

    def test_domain_label_prefers_pfam_and_drops_trailing_domain(self):
        ips = {"domains": {"PANTHER:PTHR1": ("SOME FAMILY", 1e-100),
                           "Pfam:PF2": ("Zinc finger domain", 1e-5),
                           "Pfam:PF1": ("Kinase domain", 1e-20),
                           "MobiDBLite:mobidb-lite": ("consensus disorder prediction", float("inf"))},
               "ipr": {"IPR1": ("Protein kinase-like", 1e-30)}, "go": set()}
        self.assertEqual(agg.ips_domain_label(ips), "Kinase")
        ips2 = {"domains": {"MobiDBLite:m": ("disorder", 1.0)}, "ipr": {"IPR9": ("NB-ARC", 1e-9)}, "go": set()}
        self.assertEqual(agg.ips_domain_label(ips2), "NB-ARC")


class TestDiamondFilters(unittest.TestCase):
    def test_scov_filter_blocks_name_but_hit_kept_for_qc(self):
        _, rows = run([])
        r = rows["FAKE_g0007"]  # scov 40 < 50
        self.assertEqual(r["diamond_hit"], "sp|Q9FAK4|PK1_FAKE")
        self.assertEqual(r["diamond_scov"], "40.0")
        self.assertNotEqual(r["final_name_source"], "swissprot")

    def test_cli_override_relaxes_filters(self):
        _, rows = run(["--min-scov", "30", "--min-pident", "20"])
        self.assertEqual(rows["FAKE_g0007"]["final_name"], "Serine/threonine-protein kinase 1")
        self.assertEqual(rows["FAKE_g0002"]["final_name"], "WRKY transcription factor 1")
        self.assertEqual(rows["FAKE_g0002"]["final_name_source"], "swissprot")
        self.assertEqual(rows["FAKE_g0002"]["diamond_db"], "swissprot")

    def test_cli_override_tightens_filters(self):
        _, rows = run(["--max-evalue", "1e-130"])
        self.assertEqual(rows["FAKE_g0001"]["final_name"], "similar to ADH1")
        self.assertEqual(rows["FAKE_g0001"]["final_name_source"], "eggnog")

    def test_thresholds_file(self):
        with tempfile.TemporaryDirectory() as t:
            thr = write(t, "thr.tsv", "key\tdirection\tvalue\tlabel\n"
                                      "param_min_qcov\tparam\t95\trule_of_thumb\n")
            _, rows = run(["--thresholds", thr])
        self.assertEqual(rows["FAKE_g0001"]["final_name_source"], "swissprot")  # qcov 96.7
        self.assertEqual(rows["FAKE_g0002"]["diamond_db"], "swissprot")         # nothing passes -> best failing

    def test_qcov_from_fasta_when_no_qlen(self):
        with tempfile.TemporaryDirectory() as t:
            dm = write(t, "sp.tsv", "FAKE_g0006\tsp|Q0|X_FAKE\t80\t100\t0\t0\t1\t100\t1\t100\t1e-50\t200\t"
                                    "sp|Q0|X_FAKE Test protein OS=Fakeus OX=1 GN=TP PE=1 SV=1\t110\n")
            cols = "qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore stitle slen"
            _, rows = run(["--diamond-swissprot", dm, "--diamond-columns", cols])
        r = rows["FAKE_g0006"]  # qlen 120 from FASTA
        self.assertEqual((r["diamond_qcov"], r["diamond_scov"]), ("83.3", "90.9"))
        self.assertEqual(r["final_name"], "Test protein")

    def _err(self, args):
        buf = io.StringIO()
        with self.assertRaises(SystemExit) as cm, redirect_stderr(buf), redirect_stdout(io.StringIO()):
            agg.main(args)
        return str(cm.exception.code)

    def test_missing_slen_is_friendly_error(self):
        line = ("g1\tsp|Q0|X\t80\t100\t0\t0\t1\t100\t1\t100\t1e-50\t200\t"
                "sp|Q0|X Test protein OS=F OX=1\n")
        with tempfile.TemporaryDirectory() as t:
            dm = write(t, "sp.tsv", line)
            fa = write(t, "p.faa", ">g1\n" + "M" * 100 + "\n")
            msg = self._err(["--proteins", fa, "--diamond-swissprot", dm, "--out", str(Path(t) / "o.tsv")])
        self.assertIn("missing slen", msg)
        self.assertNotIn("qlen", msg.split("missing", 1)[1].split(".", 1)[0])
        self.assertIn("F1_diamond.sh", msg)
        self.assertIn("--diamond-columns", msg)

    def test_missing_qlen_and_slen_without_fasta(self):
        line = ("g1\tsp|Q0|X\t80\t100\t0\t0\t1\t100\t1\t100\t1e-50\t200\t"
                "sp|Q0|X Test protein OS=F OX=1\n")
        with tempfile.TemporaryDirectory() as t:
            dm = write(t, "sp.tsv", line)
            msg = self._err(["--diamond-trembl", dm, "--out", str(Path(t) / "o.tsv")])
        self.assertIn("qlen (or --proteins FASTA), slen", msg)
        self.assertIn("--proteins", msg)


class TestKofam(unittest.TestCase):
    def test_threshold_filtering_detail(self):
        _, rows = run([])
        self.assertEqual(rows["FAKE_g0001"]["kofam_ko"], "K00001")   # K13951 below threshold dropped
        self.assertEqual(rows["FAKE_g0002"]["kofam_ko"], "")         # below threshold, no '*'
        self.assertEqual(rows["FAKE_g0003"]["kofam_ko"], "")         # threshold '-', no '*'
        self.assertEqual(rows["FAKE_g0003"]["eggnog_ko"], "K00599")  # eggNOG KO reported, not promoted

    def test_score_above_threshold_without_star_and_tsv(self):
        with tempfile.TemporaryDirectory() as t:
            p = write(t, "k.tsv", "#\tgene name\tKO\tthrshld\tscore\tE-value\tKO definition\n"
                                  "\tg1\tK00002\t100.0\t150.0\t1e-40\tx\n"
                                  "\tg1\tK00003\t100.0\t50.0\t1e-10\ty\n"
                                  "*\tg2\tK00004\t-\t10.0\t1e-3\tz\n")
            k = agg.parse_kofam(Path(p))
        self.assertEqual([x for x, _ in k["g1"]], ["K00002"])
        self.assertEqual([x for x, _ in k["g2"]], ["K00004"])

    def test_mapper_format(self):
        with tempfile.TemporaryDirectory() as t:
            p = write(t, "m.txt", "g1\tK00010\ng2\ng3\tK00020\n")
            k = agg.parse_kofam(Path(p))
        self.assertEqual(sorted(k), ["g1", "g3"])


class TestGo(unittest.TestCase):
    def test_union_dedup_sorted_iea_source(self):
        _, rows = run([])
        r = rows["FAKE_g0001"]
        self.assertEqual(r["ips_go"], "GO:0008270;GO:0016491;GO:0055114")
        self.assertEqual(r["eggnog_go"], "GO:0004022;GO:0016491")
        self.assertEqual(r["go_terms"], "GO:0004022;GO:0008270;GO:0016491;GO:0055114")
        self.assertEqual(r["go_evidence"], "IEA")
        self.assertEqual(r["go_source"], "GO:0004022=eggnog;GO:0008270=interproscan;"
                                         "GO:0016491=interproscan,eggnog;GO:0055114=interproscan")

    def test_ips_go_suffixes_stripped_and_deduplicated(self):
        rows = [
            "p1\tm\t9\tPfam\tPF1\tA domain\t1\t9\t1e-9\tT\td\tIPR1\tA\tGO:0005524(InterPro)|GO:0016887(PANTHER)\n",
            "p1\tm\t9\tPANTHER\tPTHR1\tFAM\t1\t9\t1e-9\tT\td\t-\t-\tGO:0005524(PANTHER)|GO:0005524(InterPro),GO:0016887\n",
            "p1\tm\t9\tSMART\tSM1\tB\t1\t9\t1e-9\tT\td\tIPR1\tA\tGO:0005524\n",
        ]
        with tempfile.TemporaryDirectory() as t:
            p = write(t, "i.tsv", "".join(rows))
            g = agg.parse_interproscan(Path(p))["p1"]["go"]
        self.assertEqual(sorted(g), ["GO:0005524", "GO:0016887"])

    def test_go_columns_aligned_and_empty_without_go(self):
        _, rows = run([])
        for r in rows.values():
            terms = r["go_terms"].split(";") if r["go_terms"] else []
            self.assertEqual(r["go_evidence"], "IEA" if terms else "")
            self.assertEqual([x.split("=")[0] for x in r["go_source"].split(";")] if terms else [], terms)
        self.assertEqual(rows["FAKE_g0006"]["go_source"], "")
        self.assertEqual(rows["FAKE_g0007"]["go_source"],
                         "GO:0004672=interproscan;GO:0005524=interproscan;GO:0006468=interproscan")


class TestMissingSources(unittest.TestCase):
    def test_gene_in_no_source_still_has_row(self):
        _, rows = run([])
        self.assertEqual(list(rows), [f"FAKE_g000{i}" for i in range(1, 8)])
        r = rows["FAKE_g0006"]
        self.assertEqual((r["final_name"], r["final_name_source"]), ("uncharacterized protein", "none"))
        for c in EXPECTED_HEADER:
            if c not in ("gene_id", "final_name", "final_name_source", "db_versions"):
                self.assertEqual(r[c], "", c)

    def test_partial_sources(self):
        _, rows = run([])
        r = rows["FAKE_g0003"]  # eggNOG only
        self.assertEqual(r["ips_domains"], "")
        self.assertEqual(r["diamond_hit"], "")
        self.assertNotEqual(r["eggnog_og"], "")

    def test_no_fasta_uses_union_of_ids(self):
        base = FULL_ARGS[2:]
        _, rows = run([], base=base)
        self.assertNotIn("FAKE_g0006", rows)
        self.assertEqual(sorted(rows), list(rows))

    def test_duplicate_ids_fail(self):
        with tempfile.TemporaryDirectory() as t:
            fa = write(t, "d.faa", ">g1\nMA\n>g1\nMA\n")
            with redirect_stderr(io.StringIO()):
                rc = agg.main(["--proteins", fa, "--out", str(Path(t) / "o.tsv")])
        self.assertEqual(rc, 1)


class TestDbVersions(unittest.TestCase):
    def test_versions_on_every_row(self):
        _, rows = run([])
        want = ("interproscan=5.72-103.0@2026-09-01;eggnog=5.0.2@2026-08-15;diamond=2.1.10@2026-09-01;"
                "swissprot=2026_03@2026-06-18;trembl=2026_03@2026-06-18;kofam=2026-07@2026-07-20")
        for r in rows.values():
            self.assertEqual(r["db_versions"], want)

    def test_cli_version_overrides_file_entry(self):
        _, rows = run(["--db-version", "kofam=2026-10@2026-10-01"])
        self.assertIn("kofam=2026-10@2026-10-01", rows["FAKE_g0001"]["db_versions"])
        self.assertNotIn("kofam=2026-07", rows["FAKE_g0001"]["db_versions"])

    def test_malformed_version_rejected(self):
        with self.assertRaises(SystemExit):
            agg.parse_db_versions(["swissprot=2026_03"], [])
        with self.assertRaises(SystemExit):
            agg.parse_db_versions(["swissprot=2026_03@19-10-2026"], [])


if __name__ == "__main__":
    unittest.main()
