import sys, os, csv
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svgkit_v2 import SVG, PAL, tint, tw, wrap, INK, MUTED, ink_on

OUT, REPO = sys.argv[1], sys.argv[2]
B, O, G, R, P, S, GR = PAL["blue"], PAL["orange"], PAL["green"], PAL["red"], PAL["purple"], PAL["sky"], PAL["grey"]
BR = PAL["brown"]; MG = PAL["magenta"]

def badge(s, x, y, n, color):
    s.raw("<circle cx=\"%.1f\" cy=\"%.1f\" r=\"11\" fill=\"%s\"/>" % (x, y, color))
    s.text(x, y + 4.6, str(n), 12.5, True, ink_on(color, 12.5), "middle")

def route_map():
    W, H = 1320, 650
    s = SVG(W, H, "Functional annotation route in gene-function-annotation")
    # input
    s.node(20, 70, 170, "proteins.faa", ["One representative protein per gene, from the structure release (A6)"], "#333333", tsize=15, bsize=12, align="start", min_h=150)
    st = [("F0  Protein QC", ["BUSCO in protein mode", "Catastrophic result: fix gene models upstream, not here"], O)]
    x = 216
    h = s.node(x, 70, 170, st[0][0], st[0][1], O, tsize=15, bsize=12, align="start", min_h=150)
    badge(s, x + 154, 68, 1, O)
    s.line([(190, 140), (213, 140)], "#333333", 2)
    # F1 frame block with three lanes
    fx = 412; fw = 330
    s.rect(fx, 52, fw, 190, B, rx=10)
    badge(s, fx + fw - 16, 50, 2, B)
    s.text(fx + 12, 76, "Frame F1 (default)", 15, True, INK)
    s.text(fx + 12, 94, "three independent lines of evidence", 12, False, MUTED)
    lanes = [("DIAMOND vs Swiss-Prot", "similarity to curated proteins", B), ("eggNOG-mapper", "orthology-based transfer: name, GO, KO", G), ("InterProScan", "signatures: domains, families, InterPro2GO", P)]
    for i, (t, d, c) in enumerate(lanes):
        yy = 106 + i * 44
        s.rect(fx + 12, yy, fw - 24, 38, c, rx=6, fill="#FFFFFF", shadow=False)
        s.text(fx + 22, yy + 16, t, 13, True, INK)
        s.text(fx + 22, yy + 31, d, 11.5, False, INK)
    s.line([(386, 140), (409, 140)], "#333333", 2)
    # merge
    mx = 768
    s.node(mx, 70, 170, "Merge", ["F_merge_tables.py", "merged_function_table.tsv", "GO from each source kept; evidence IEA"], G, tsize=15, bsize=12, align="start", min_h=150)
    badge(s, mx + 154, 68, 3, G)
    s.line([(742, 140), (765, 140)], "#333333", 2)
    qx = 964
    s.node(qx, 70, 160, "Function QC", ["Coverage and agreement between sources", "QC table; F-L0 / F-L1 in EVALUATION.md"], R, tsize=15, bsize=12, align="start", min_h=150)
    badge(s, qx + 144, 68, 4, R)
    s.line([(938, 140), (961, 140)], "#333333", 2)
    rx = 1150
    s.node(rx, 70, 150, "Release", ["F_release.sh to release/<TAG>/", "METHODS with DB versions", "Gate-F1 to Gate-F7"], "#1D7CBB", tsize=15, bsize=12, align="start", min_h=150)
    badge(s, rx + 134, 68, 5, "#1D7CBB")
    s.line([(1124, 140), (1147, 140)], "#333333", 2)
    s.text(20, 36, "Always: F0, frame F1, merge, release. Default if unsure: F1 only (docs/ROADMAP.md).", 14, True, INK)
    # add-ons
    ay = 290
    s.rect(412, ay, 888, 130, MG, rx=10, fill=tint(MG, 0.96), shadow=False, dash="5 4")
    s.text(426, ay + 24, "Optional add-ons after F1, only if that figure or species needs them", 14, True, INK)
    adds = [("F4  Readable names", "AHRD (\u00b1 PANNZER)", MG), ("F6  MapMan bins", "Mercator4; see MERCATOR_WHEN.md", G), ("F8  NLR screen", "InterProScan filter \u00b1 HRP; not a curated NLR set", R), ("F9  TF and kinase", "iTAK", BR)]
    cw = (888 - 28 - 3 * 12) / 4
    for i, (t, d, c) in enumerate(adds):
        s.node(426 + i * (cw + 12), ay + 38, cw, t, [d], c, tsize=13, bsize=11.5, align="start", min_h=78)
    s.line([(577, 244), (577, ay - 3)], MG, 1.6, dash="4 3")
    s.line([(853, ay), (853, 224)], MG, 1.6, dash="4 3")
    s.text(589, 270, "after F1", 11.5, False, INK)
    s.text(865, 270, "joined at merge", 11.5, False, INK)
    # alternate frames and F7
    s.rect(20, 260, 366, 360, "#6B6B6B", rx=10, fill="#F7F7F7", shadow=False, dash="5 4")
    s.text(34, 284, "Other frames (all rejoin at merge)", 14, True, INK)
    alts = [("F2  Fast", "eggNOG-mapper (\u00b1 KofamScan); InterProScan later", O), ("F3  EnTAP", "lab standardised on EnTAP", S), ("F5  Trinotate", "transcriptome peptides, no genome GFF", P), ("F7  Genome panel", "before F1: OrthoFinder representatives", B)]
    for i, (t, d, c) in enumerate(alts):
        s.node(34, 296 + i * 78, 338, t, [d], c, tsize=12.5, bsize=11.5, align="start", min_h=66)
    s.text(W - 20, H - 12, "Stage IDs and runners from docs/ROADMAP.md and README; tool roles from catalog/SOFTWARE_AUTHORITY.tsv.", 11, False, MUTED, "end")
    return s

def decision():
    W, H = 1320, 610
    s = SVG(W, H, "Which functional annotation frame to use")
    def q(x, y, w, t):
        return s.node(x, y, w, t, [], "#333333", tsize=14)
    def leaf(x, y, w, t, lines, c):
        return s.node(x, y, w, t, lines, c, tsize=14.5, bsize=12, align="start")
    def lab(x, y, t, c="#000000"):
        s.text(x, y, t, 12.5, True, INK, "middle")
    s.node(440, 16, 440, "Structure release passed F0 protein BUSCO", [], "#333333", tsize=14)
    s.line([(660, 50), (660, 74)], "#333333", 1.8)
    h = q(420, 76, 480, "Several genomes in one panel?")
    s.line([(900, 76 + h / 2), (968, 76 + h / 2)], B, 1.8); lab(934, 76 + h / 2 - 7, "yes", B)
    leaf(970, 52, 330, "F7  Orthogroups first", ["OrthoFinder, then F1 on representatives", "Check: labels apply to representatives, not every gene"], B)
    s.line([(660, 76 + h), (660, 150)], "#333333", 1.8); lab(680, 76 + h + 20, "no")
    h2 = q(380, 152, 560, "Only transcriptome peptides (Trinity), no genome GFF?")
    s.line([(940, 152 + h2 / 2), (968, 152 + h2 / 2)], P, 1.8); lab(954, 152 + h2 / 2 - 7, "", P)
    leaf(970, 140, 330, "F5 Trinotate  or  F3 EnTAP", ["EnTAP was designed for de novo transcriptomes of non-model eukaryotes", "Check: state the frame in METHODS"], P)
    lab(955, 152 + h2 / 2 - 8, "yes", P)
    s.line([(660, 152 + h2), (660, 230)], "#333333", 1.8); lab(680, 152 + h2 + 20, "no")
    h3 = q(400, 232, 520, "Need answers today and InterProScan is too slow?")
    s.line([(400, 232 + h3 / 2), (330, 232 + h3 / 2), (330, 300)], O, 1.8); lab(365, 232 + h3 / 2 - 7, "yes", O)
    s.line([(920, 232 + h3 / 2), (990, 232 + h3 / 2), (990, 300)], B, 1.8); lab(955, 232 + h3 / 2 - 7, "no", B)
    leaf(140, 302, 380, "F2  Fast first pass", ["eggNOG-mapper, optional KofamScan; run InterProScan later into merge", "Check: do not ship F2 as if InterProScan had been run"], O)
    leaf(800, 302, 380, "F1  Default paper release", ["DIAMOND vs Swiss-Prot, eggNOG-mapper, InterProScan", "Check: merged row count close to the protein count"], B)
    yb = 430
    s.rect(20, yb, W - 40, 160, MG, rx=10, fill=tint(MG, 0.96), shadow=False, dash="5 4")
    s.text(34, yb + 22, "Then add only what the paper needs (add-ons do not raise the grade by themselves)", 13.5, True, INK)
    side = [("Readable names wanted", "F4  AHRD", MG), ("MapMan figure planned", "F6  Mercator4", G), ("Disease or NLR story", "F8  InterProScan filter, NLR-Annotator, NLRtracker", R), ("TFs or kinases", "F9  iTAK", BR)]
    cw = (W - 40 - 28 - 3 * 12) / 4
    for i, (t, l, c) in enumerate(side):
        s.node(34 + i * (cw + 12), yb + 36, cw, t, [l], c, tsize=13, bsize=12, align="start", min_h=88)
    s.text(W - 20, H - 4, "", 1)
    return s

def evidence():
    rows = list(csv.DictReader(open(os.path.join(REPO, "testdata/function_aggregate/expected/merged_function_table.tsv"), encoding="utf-8"), delimiter="\t"))
    r = rows[0]
    W, H = 1320, 530
    s = SVG(W, H, "Three F1 evidence lines merged into one gene row")
    s.node(20, 200, 180, r["gene_id"], ["one protein from proteins.faa (simulated test record)"], "#333333", tsize=15, bsize=12, align="start", min_h=90)
    lanes = [
        ("DIAMOND vs Swiss-Prot", B, ["best hit " + r["diamond_hit"], "name: " + r["diamond_name"], "identity %s%%, query cover %s%%, E = %s" % (r["diamond_pident"], r["diamond_qcov"], r["diamond_evalue"])]),
        ("eggNOG-mapper", G, ["orthogroup " + r["eggnog_og"], "name %s; KO %s" % (r["eggnog_name"], r["eggnog_ko"]), "GO terms: " + r["eggnog_go"].replace(";", ", ")]),
        ("InterProScan", P, [r["ips_domains"].replace(";", ", "), "InterPro entries: " + r["ips_ipr"].replace(";", ", "), "GO terms: " + r["ips_go"].replace(";", ", ")]),
    ]
    y = 30
    for t, c, ls in lanes:
        hh = s.node(260, y, 470, t, ls, c, tsize=14, bsize=12, align="start", min_h=128)
        s.line([(200, 245), (230, 245), (230, y + 64), (257, y + 64)], c, 1.6)
        s.line([(730, y + 64), (770, y + 64), (770, 245), (796, 245)], c, 1.6, arrow=(t == "InterProScan"))
        y += 172
    # merged row card
    gs = dict(x.split("=") for x in r["go_source"].split(";"))
    s.rect(800, 60, 500, 380, "#333333", rx=10, fill="#FFFFFF")
    s.text(816, 88, "merged_function_table.tsv (one row)", 14, True, INK)
    items = [("gene_id", r["gene_id"], "#000000"), ("final_name", "%s  (source: %s)" % (r["final_name"], r["final_name_source"]), B),
             ("eggnog_ko / kofam_ko", "%s / %s" % (r["eggnog_ko"], r["kofam_ko"]), G), ("ips_ipr", r["ips_ipr"].replace(";", ", "), P),
             ("go_evidence", r["go_evidence"] + "  (machine predictions stay IEA)", R)]
    yy = 118
    for k, v, c in items:
        s.raw("<text x=\"816\" y=\"%.1f\" font-family=\"Liberation Mono, DejaVu Sans Mono, monospace\" font-size=\"12\" fill=\"#6B6B6B\">%s</text>" % (yy, k))
        s.text(990, yy, v, 12.5, False, INK, maxw=300); yy += 26
    s.text(816, yy + 8, "go_terms with go_source", 12.5, True, INK); yy += 30
    col = {"interproscan": P, "eggnog": G}
    for term, src in gs.items():
        s.raw("<text x=\"826\" y=\"%.1f\" font-family=\"Liberation Mono, DejaVu Sans Mono, monospace\" font-size=\"12\" fill=\"#000000\">%s</text>" % (yy, term))
        xx = 960
        for sname in src.split(","):
            w = tw(sname, 11.5) + 14
            s.rect(xx, yy - 13, w, 18, col.get(sname, GR), rx=9, fill=tint(col.get(sname, GR), 0.85), shadow=False)
            s.text(xx + w / 2, yy, sname, 11.5, False, "#000000", "middle"); xx += w + 6
        yy += 24
    s.text(816, yy + 10, "db_versions records every database release used (METHODS).", 11.5, False, MUTED)
    s.text(W - 20, H - 12, "Values from the simulated test row in testdata/function_aggregate/expected/merged_function_table.tsv (not a real gene).", 11, False, MUTED, "end")
    return s

figs = {"function_route_map_v2": route_map, "function_frame_decision_v2": decision, "function_evidence_merge_v2": evidence}
for name, fn in figs.items():
    s = fn()
    ov = s.save(os.path.join(OUT, name + ".svg"))
    print(name, s.w, s.h, "overflow:", ov)
