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
            go_terms="GO:0004672", go_evidence="IEA", go_source="GO:0004672=interproscan,eggnog")


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

    def test_name_source_rule(self):
        trembl = {**FULL, "diamond_db": "trembl"}
        rows = [row("g1", **FULL),
                row("g2", **{**trembl, "final_name": "similar to kinase", "final_name_source": "eggnog"}),
                row("g3", **{**trembl, "eggnog_name": "", "final_name_source": "interproscan_domain"}),
                row("g4", final_name="uncharacterized protein", final_name_source="none"),
                row("g5", **{**trembl, "final_name_source": "swissprot"})]
        s, _ = run(rows)
        self.assertEqual(float(s["share_name_source_consistent"]["value"]), 0.8)
        self.assertEqual(s["share_name_source_consistent"]["status"], "warn")
        self.assertEqual(float(s["share_name_source_interproscan_domain"]["value"]), 0.2)

    def _expected(self, **kw):
        p = {k: v[1] for k, v in qc.load_thresholds(qc.DEFAULT_THRESHOLDS).items() if v[0] == "param"}
        return qc.expected_name_sources(row("g", **{**FULL, **kw}), p)

    def test_name_source_uninformative_swissprot_falls_through(self):
        self.assertEqual(self._expected(diamond_name="Uncharacterized protein At1g01010"), {"eggnog"})
        self.assertEqual(self._expected(diamond_name="Uncharacterized protein At1g01010",
                                        eggnog_name=""), {"interproscan_domain"})

    def test_name_source_non_domain_ips_rows_do_not_name(self):
        nd = dict(eggnog_name="", diamond_db="trembl", ips_ipr="",
                  ips_domains="MobiDBLite:mobidb-lite;PANTHER:PTHR11695;Coils:Coil",
                  ips_domain_desc="consensus disorder prediction;ALCOHOL DEHYDROGENASE;-")
        self.assertEqual(self._expected(**nd), {"none"})
        # IPR ID without an informative domain signature: both outcomes accepted
        self.assertEqual(self._expected(**{**nd, "ips_ipr": "IPR002085"}), {"interproscan_domain", "none"})

    def test_name_source_count_mismatch_lenient(self):
        self.assertEqual(self._expected(diamond_db="trembl", eggnog_name="", ips_ipr="",
                                        ips_domains="Pfam:PF1;Pfam:PF2", ips_domain_desc="A; B; C"),
                         {"interproscan_domain", "none"})

    def test_name_source_lenient_cases_pass(self):
        g2 = dict(diamond_db="trembl", eggnog_name="", ips_domains="PANTHER:PTHR11695",
                  ips_domain_desc="-", ips_ipr="IPR002085")
        g3 = dict(diamond_name="Uncharacterized protein", final_name="similar to kinase",
                  final_name_source="eggnog")
        rows = [row("g1", **FULL),
                row("g2", **{**FULL, **g2, "final_name": "uncharacterized protein", "final_name_source": "none"}),
                row("g2b", **{**FULL, **g2, "final_name": "Alcohol dehydrogenase domain-containing protein",
                              "final_name_source": "interproscan_domain"}),
                row("g3", **{**FULL, **g3})]
        s, _ = run(rows)
        self.assertEqual(float(s["share_name_source_consistent"]["value"]), 1.0)
        self.assertEqual(s["share_name_source_consistent"]["status"], "pass")
        # g3 is not accepted as swissprot
        s, _ = run([row("g3", **{**FULL, **g3, "final_name_source": "swissprot"})])
        self.assertEqual(s["share_name_source_consistent"]["status"], "warn")

    def test_status_compares_raw_value(self):
        thr = {"share_go_evidence_iea": ("min", 1.0, "rule_of_thumb")}
        self.assertEqual(qc.status("share_go_evidence_iea", 0.99995, thr)[0], "warn")
        self.assertEqual(qc.fmt(qc.Share(19999, 20000)), "1")  # prints as 1 ...
        self.assertEqual(qc.status("share_go_evidence_iea", qc.Share(19999, 20000), thr)[0], "warn")  # ... fails
        self.assertEqual(qc.status("share_go_evidence_iea", qc.Share(20000, 20000), thr)[0], "pass")

    def test_report_has_k_n(self):
        s, _ = run([row("g1", **FULL), row("g2", **{**FULL, "go_source": ""}), row("g3")])
        self.assertEqual(s["share_go_with_source"]["k_n"], "1/2")
        self.assertEqual(s["n_genes"]["k_n"], "")

    def _dc(self, **kw):
        p = {k: v[1] for k, v in qc.load_thresholds(qc.DEFAULT_THRESHOLDS).items() if v[0] == "param"}
        return qc.diamond_check(row("g", **{**FULL, **kw}), p)

    def test_diamond_edge_qcov(self):
        self.assertEqual(self._dc(diamond_qcov="50.0"), "edge")   # raw could be 49.96 or 50.04
        self.assertEqual(self._dc(diamond_qcov="49.95"), "fail")  # 2 decimals: +-0.005, clearly below
        self.assertEqual(self._dc(diamond_qcov="50"), "edge")     # integer display: +-0.5
        self.assertEqual(self._dc(diamond_qcov="49.5"), "fail")   # 1 decimal: +-0.05, clearly below
        self.assertEqual(self._dc(diamond_qcov="50.1"), "pass")

    def test_diamond_edge_evalue(self):
        self.assertEqual(self._dc(diamond_evalue="1e-05"), "edge")   # 1e-05 printed with 1 sig digit
        self.assertEqual(self._dc(diamond_evalue="1.0e-05"), "edge")
        self.assertEqual(self._dc(diamond_evalue="1.2e-05"), "fail")  # clearly above 1e-5
        self.assertEqual(self._dc(diamond_evalue="9e-06"), "pass")

    def test_diamond_edge_name_source_and_clear_miss(self):
        p = {k: v[1] for k, v in qc.load_thresholds(qc.DEFAULT_THRESHOLDS).items() if v[0] == "param"}
        edge = row("g", **{**FULL, "diamond_scov": "50.0"})
        self.assertEqual(qc.expected_name_sources(edge, p), {"swissprot", "eggnog"})
        miss = row("g", **{**FULL, "diamond_scov": "49.0"})
        self.assertEqual(qc.expected_name_sources(miss, p), {"eggnog"})
        s, _ = run([row("g1", **{**FULL, "diamond_qcov": "50.0", "final_name_source": "eggnog"}),
                    row("g2", **{**FULL, "diamond_qcov": "50.0"}),
                    row("g3", **{**FULL, "diamond_qcov": "45.0"})])  # clear miss named swissprot
        self.assertEqual(s["share_name_source_consistent"]["k_n"], "2/3")
        self.assertEqual(s["share_name_source_consistent"]["status"], "warn")

    def test_name_source_hypothetical_eggnog_name_skipped(self):
        for name in ("hypothetical protein", "-", "Uncharacterized protein"):
            self.assertEqual(self._expected(diamond_db="trembl", eggnog_name=name), {"interproscan_domain"}, name)

    def test_example_name_sources_consistent(self):
        ex = ROOT / "testdata" / "function_qc"
        p = {k: v[1] for k, v in qc.load_thresholds(qc.DEFAULT_THRESHOLDS).items() if v[0] == "param"}
        for f in ("merged.sim.tsv", "relative.sim.tsv"):
            for r in qc.read_tsv(ex / f):
                self.assertIn(r["final_name_source"], qc.NAME_SOURCES)
                self.assertIn(r["final_name_source"], qc.expected_name_sources(r, p), r["gene_id"])

    def test_go_source(self):
        s, _ = run([row("g1", **FULL), row("g2", **{**FULL, "go_source": ""}), row("g3")])
        self.assertEqual(float(s["share_go_with_source"]["value"]), 0.5)
        self.assertEqual(s["share_go_with_source"]["status"], "warn")

    def test_schema_has_go_source(self):
        self.assertEqual(len(COLS), 24)
        self.assertEqual(COLS[COLS.index("go_evidence") + 1], "go_source")

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
