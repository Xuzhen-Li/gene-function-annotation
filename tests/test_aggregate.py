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
    "go_terms", "go_evidence", "db_versions",
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
        self.assertEqual(cols, EXPECTED_HEADER)

    def test_matches_expected_output(self):
        out = Path(tempfile.mkdtemp()) / "m.tsv"
        with redirect_stderr(io.StringIO()), redirect_stdout(io.StringIO()):
            agg.main(FULL_ARGS + ["--out", str(out)])
        self.assertEqual(out.read_text(), (D / "expected" / "merged_function_table.tsv").read_text())


class TestNamePriority(unittest.TestCase):
    def setUp(self):
        _, self.rows = run([])

    def test_swissprot_wins(self):
        r = self.rows["FAKE_g0001"]
        self.assertEqual((r["final_name"], r["final_name_source"]), ("Alcohol dehydrogenase 1", "swissprot"))
        self.assertEqual(r["diamond_db"], "swissprot")

    def test_interpro_before_eggnog_and_trembl_when_swissprot_fails(self):
        r = self.rows["FAKE_g0002"]  # SP hit pident 25 < 30
        self.assertEqual(r["final_name"], "similar to WRKY domain")
        self.assertEqual(r["final_name_source"], "interproscan")
        self.assertEqual(r["diamond_db"], "trembl")  # passing TrEMBL shown over failing SP

    def test_eggnog_before_trembl(self):
        r = self.rows["FAKE_g0003"]
        self.assertEqual((r["final_name"], r["final_name_source"]),
                         ("similar to Methyltransferase domain", "eggnog"))

    def test_trembl_last(self):
        r = self.rows["FAKE_g0004"]
        self.assertEqual(r["final_name_source"], "trembl")
        self.assertTrue(r["final_name"].startswith("similar to Pentatricopeptide"))

    def test_uninformative_trembl_gives_uncharacterized(self):
        r = self.rows["FAKE_g0005"]
        self.assertEqual((r["final_name"], r["final_name_source"]), ("uncharacterized protein", "none"))

    def test_without_interpro_eggnog_takes_over(self):
        base = [a for a in FULL_ARGS]
        i = base.index("--ips")
        del base[i:i + 2]
        _, rows = run([], base=base)
        self.assertEqual(rows["FAKE_g0002"]["final_name"], "similar to WRKY transcription factor")
        self.assertEqual(rows["FAKE_g0002"]["final_name_source"], "eggnog")


class TestDiamondFilters(unittest.TestCase):
    def test_scov_filter_blocks_name_but_hit_kept_for_qc(self):
        _, rows = run([])
        r = rows["FAKE_g0007"]  # scov 40 < 50
        self.assertEqual(r["diamond_hit"], "sp|Q9FAK4|PK1_FAKE")
        self.assertEqual(r["diamond_scov"], "40.0")
        self.assertEqual(r["final_name"], "uncharacterized protein")

    def test_cli_override_relaxes_filters(self):
        _, rows = run(["--min-scov", "30", "--min-pident", "20"])
        self.assertEqual(rows["FAKE_g0007"]["final_name"], "Serine/threonine-protein kinase 1")
        self.assertEqual(rows["FAKE_g0002"]["final_name"], "WRKY transcription factor 1")
        self.assertEqual(rows["FAKE_g0002"]["diamond_db"], "swissprot")

    def test_cli_override_tightens_filters(self):
        _, rows = run(["--max-evalue", "1e-130"])
        self.assertEqual(rows["FAKE_g0001"]["final_name_source"], "interproscan")

    def test_thresholds_file(self):
        with tempfile.TemporaryDirectory() as t:
            thr = write(t, "thr.tsv", "key\tdirection\tvalue\tlabel\n"
                                      "param_min_qcov\tparam\t95\trule_of_thumb\n")
            _, rows = run(["--thresholds", thr])
        self.assertEqual(rows["FAKE_g0001"]["final_name_source"], "swissprot")  # qcov 96.7
        self.assertEqual(rows["FAKE_g0004"]["final_name_source"], "none")       # qcov 90.9

    def test_qcov_from_fasta_when_no_qlen(self):
        with tempfile.TemporaryDirectory() as t:
            dm = write(t, "sp.tsv", "FAKE_g0006\tsp|Q0|X_FAKE\t80\t100\t0\t0\t1\t100\t1\t100\t1e-50\t200\t"
                                    "sp|Q0|X_FAKE Test protein OS=Fakeus OX=1 GN=TP PE=1 SV=1\n")
            cols = "qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore stitle"
            _, rows = run(["--diamond-swissprot", dm, "--diamond-columns", cols])
        r = rows["FAKE_g0006"]  # qlen 120 from FASTA, no slen -> scov unknown -> fails
        self.assertEqual(r["diamond_qcov"], "83.3")
        self.assertEqual(r["diamond_scov"], "")
        self.assertEqual(r["final_name"], "uncharacterized protein")


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
    def test_union_dedup_sorted_iea(self):
        _, rows = run([])
        r = rows["FAKE_g0001"]
        self.assertEqual(r["go_terms"], "GO:0004022;GO:0016491;GO:0055114")
        self.assertEqual(r["ips_go"], "GO:0016491;GO:0055114")
        self.assertEqual(r["eggnog_go"], "GO:0004022;GO:0016491")
        self.assertEqual(r["go_evidence"], "IEA")

    def test_all_go_rows_iea_and_empty_without_go(self):
        _, rows = run([])
        for r in rows.values():
            self.assertEqual(r["go_evidence"], "IEA" if r["go_terms"] else "")
        self.assertEqual(rows["FAKE_g0006"]["go_terms"], "")


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
