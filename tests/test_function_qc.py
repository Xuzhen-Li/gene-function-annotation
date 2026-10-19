"""Tests for pipeline/F10_function_qc.py using mocked merged-table outputs."""
import csv
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "pipeline"))
import F10_function_qc as qc  # noqa: E402

COLS = [r["column"] for r in qc.read_tsv(qc.DEFAULT_SCHEMA)]
VER = "interproscan=5.72@2026-09-01;eggnog=5.0.2@2026-08-15;diamond=2.1.10@2026-09-01;kofam=2026-07@2026-07-20"


def row(gid, **kw):
    r = {c: "" for c in COLS}
    r.update(gene_id=gid, db_versions=VER)
    r.update(kw)
    return r


FULL = dict(ips_domains="Pfam:PF00069", ips_domain_desc="Protein kinase domain", ips_go="GO:0004672",
            eggnog_og="KOG1", eggnog_name="kinase", eggnog_description="Protein kinase",
            eggnog_go="GO:0004672", eggnog_ko="K04733", kofam_ko="K04733", diamond_db="swissprot",
            diamond_hit="sp|P1|X", diamond_name="Serine/threonine-protein kinase", diamond_evalue="1e-50",
            diamond_pident="80", diamond_qcov="90", diamond_scov="90",
            final_name="Serine/threonine-protein kinase", final_name_source="swissprot",
            go_terms="GO:0004672", go_evidence="IEA")


def write(path, rows):
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, COLS, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def run(rows, relative=None):
    d = Path(tempfile.mkdtemp())
    write(d / "m.tsv", rows)
    args = ["--merged", str(d / "m.tsv"), "--out", str(d / "qc.tsv")]
    if relative is not None:
        write(d / "r.tsv", relative)
        args += ["--relative", str(d / "r.tsv")]
    assert qc.main(args) == 0
    summ = {r["metric"]: r for r in qc.read_tsv(d / "qc.tsv")}
    conf = qc.read_tsv(d / "qc.conflicts.tsv")
    return summ, conf


class TestFunctionQC(unittest.TestCase):
    def test_coverage_and_hypothetical(self):
        rows = [row("g1", **FULL), row("g2", final_name="uncharacterized protein"),
                row("g3", **{**FULL, "kofam_ko": ""}), row("g4", final_name="hypothetical protein")]
        s, _ = run(rows)
        self.assertEqual(float(s["coverage_interproscan"]["value"]), 0.5)
        self.assertEqual(float(s["coverage_kofam"]["value"]), 0.25)
        self.assertEqual(float(s["share_hypothetical"]["value"]), 0.5)
        self.assertEqual(s["share_hypothetical"]["status"], "warn")
        self.assertEqual(s["coverage_any"]["threshold_label"], "rule_of_thumb")

    def test_agreement_and_conflict(self):
        bad = {**FULL, "eggnog_name": "Histone H3", "eggnog_description": "Core histone",
               "eggnog_ko": "K11253", "diamond_name": "Histone H3.2", "eggnog_go": "GO:0000786"}
        s, conf = run([row("g1", **FULL), row("g2", **bad)])
        self.assertEqual(float(s["agree_ko_eggnog_vs_kofam"]["value"]), 0.5)
        self.assertEqual(float(s["share_ge2_tools_agree"]["value"]), 1.0)
        kinds = {(c["gene_id"], c["conflict"]) for c in conf}
        self.assertIn(("g2", "eggnog_name_vs_pfam_domain"), kinds)
        self.assertIn(("g2", "eggnog_ko_vs_kofam_ko"), kinds)
        self.assertEqual(float(s["share_conflict"]["value"]), 0.5)

    def test_diamond_filters_and_distribution(self):
        weak = {**FULL, "diamond_evalue": "1e-3", "diamond_qcov": "30"}
        s, _ = run([row("g1", **FULL), row("g2", **weak)])
        self.assertEqual(float(s["share_diamond_hits_pass_filters"]["value"]), 0.5)
        self.assertAlmostEqual(float(s["diamond_neglog10_evalue_median"]["value"]), 26.5)

    def test_go_iea_and_db_versions(self):
        s, _ = run([row("g1", **FULL), row("g2", **{**FULL, "go_evidence": "ISS", "db_versions": "eggnog=5.0.2"})])
        self.assertEqual(float(s["share_go_evidence_iea"]["value"]), 0.5)
        self.assertEqual(s["share_go_evidence_iea"]["status"], "warn")
        self.assertEqual(float(s["share_genes_db_versions_complete"]["value"]), 0.5)

    def test_relative(self):
        rel = [row("r1", **FULL), row("r2", final_name="uncharacterized protein")]
        s, _ = run([row("g1", **FULL), row("g2", **FULL)], relative=rel)
        self.assertAlmostEqual(float(s["delta_coverage_any_vs_relative"]["value"]), 0.5)
        self.assertEqual(s["delta_coverage_any_vs_relative"]["status"], "warn")
        self.assertEqual(float(s["ko_jaccard_vs_relative"]["value"]), 1.0)

    def test_missing_column_exits(self):
        d = Path(tempfile.mkdtemp())
        (d / "m.tsv").write_text("gene_id\tfinal_name\ng1\tx\n")
        with self.assertRaises(SystemExit):
            qc.main(["--merged", str(d / "m.tsv"), "--out", str(d / "o.tsv")])

    def test_example_runs(self):
        d = Path(tempfile.mkdtemp())
        ex = ROOT / "testdata" / "function_qc"
        qc.main(["--merged", str(ex / "merged.sim.tsv"), "--relative", str(ex / "relative.sim.tsv"),
                 "--out", str(d / "qc.tsv")])
        s = {r["metric"]: r["status"] for r in qc.read_tsv(d / "qc.tsv")}
        self.assertTrue(set(s.values()) <= {"pass", "warn", "na", "info"})


if __name__ == "__main__":
    unittest.main()
