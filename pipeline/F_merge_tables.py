#!/usr/bin/env python3
"""Merge eggNOG / InterProScan / DIAMOND into one gene-centric TSV (best-effort parsers)."""
from __future__ import annotations
import argparse, csv, re
from pathlib import Path
from collections import defaultdict

def fasta_ids(path: str) -> list[str]:
    ids = []
    for line in open(path):
        if line.startswith(">"):
            ids.append(line[1:].split()[0])
    return ids

def parse_emapper(path: Path) -> dict[str, dict]:
    out = {}
    with open(path) as f:
        header = None
        for line in f:
            if line.startswith("#"):
                if line.startswith("#query") or "query" in line.lower() and "seed" in line.lower():
                    header = line.lstrip("#").strip().split("\t")
                continue
            if not line.strip():
                continue
            cols = line.rstrip("\n").split("\t")
            if header and len(cols) >= len(header):
                row = dict(zip(header, cols))
                q = row.get("query") or row.get("#query") or cols[0]
            else:
                q = cols[0]
                row = {"raw": line.rstrip()}
            # common emapper columns (v2 names; v3 may differ — keep raw too)
            out[q] = {
                "emapper_COG": row.get("COG_category") or row.get("cog_category") or "",
                "emapper_Description": row.get("Description") or row.get("description") or "",
                "emapper_GOs": row.get("GOs") or row.get("go") or "",
                "emapper_KEGG_ko": row.get("KEGG_ko") or row.get("kegg_ko") or "",
                "emapper_KEGG_Pathway": row.get("KEGG_Pathway") or row.get("kegg_pathway") or "",
                "emapper_PFAMs": row.get("PFAMs") or row.get("pfam") or "",
                "emapper_Preferred_name": row.get("Preferred_name") or row.get("preferred_name") or "",
            }
    return out

def parse_ips_tsv(path: Path) -> dict[str, dict]:
    # InterProScan TSV: protein_id ... signature ... go ...
    go = defaultdict(set)
    sig = defaultdict(set)
    ipr = defaultdict(set)
    for line in open(path):
        if not line.strip() or line.startswith("#"):
            continue
        c = line.rstrip("\n").split("\t")
        if len(c) < 12:
            continue
        pid, analysis, sigacc, sigdesc = c[0], c[3], c[4], c[5]
        sig[pid].add(f"{analysis}:{sigacc}")
        if len(c) > 11 and c[11].startswith("IPR"):
            ipr[pid].add(c[11])
        if len(c) > 13 and c[13]:
            for g in re.split(r"[|,]", c[13]):
                if g.startswith("GO:"):
                    go[pid].add(g)
    return {
        k: {
            "ips_signatures": ";".join(sorted(sig[k]))[:2000],
            "ips_InterPro": ";".join(sorted(ipr[k])),
            "ips_GOs": ";".join(sorted(go[k])),
        }
        for k in set(sig) | set(ipr) | set(go)
    }

def parse_diamond(path: Path) -> dict[str, dict]:
    best = {}
    for line in open(path):
        c = line.rstrip("\n").split("\t")
        if len(c) < 12:
            continue
        q, s, pident, evalue, bits = c[0], c[1], c[2], c[10], float(c[11])
        title = c[12] if len(c) > 12 else ""
        if q not in best or bits > best[q]["_bits"]:
            best[q] = {
                "diamond_sseqid": s,
                "diamond_pident": pident,
                "diamond_evalue": evalue,
                "diamond_stitle": title,
                "_bits": bits,
            }
    for v in best.values():
        v.pop("_bits", None)
    return best

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--proteins", required=True)
    ap.add_argument("--emapper", action="append", default=[])
    ap.add_argument("--ips", action="append", default=[])
    ap.add_argument("--diamond", action="append", default=[])
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    ids = fasta_ids(args.proteins)
    em, ip, di = {}, {}, {}
    for p in args.emapper:
        em.update(parse_emapper(Path(p)))
    for p in args.ips:
        ip.update(parse_ips_tsv(Path(p)))
    for p in args.diamond:
        di.update(parse_diamond(Path(p)))

    fields = [
        "gene_id",
        "emapper_Preferred_name", "emapper_Description", "emapper_GOs",
        "emapper_KEGG_ko", "emapper_KEGG_Pathway", "emapper_COG", "emapper_PFAMs",
        "ips_InterPro", "ips_signatures", "ips_GOs",
        "diamond_sseqid", "diamond_pident", "diamond_evalue", "diamond_stitle",
    ]
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "w", newline="") as fo:
        w = csv.DictWriter(fo, fieldnames=fields, delimiter="\t", extrasaction="ignore")
        w.writeheader()
        for gid in ids:
            row = {"gene_id": gid}
            row.update(em.get(gid, {}))
            row.update(ip.get(gid, {}))
            row.update(di.get(gid, {}))
            w.writerow(row)
    print(f"[OK] {len(ids)} genes → {args.out}")
    _warn_empty_master(Path(args.out), len(ids))

def _warn_empty_master(out: Path, n_proteins: int) -> None:
    try:
        lines = out.read_text().splitlines()
    except OSError:
        return
    if len(lines) < 2:
        print("[WARN] master missing or header-only")
        return
    body = lines[1:]
    nonempty = sum(1 for L in body if ("GO:" in L) or ("\tPF" in L) or ("IPR" in L) or ("K0" in L))
    print(f"[merge] rows={len(body)} proteins_in={n_proteins} rows_with_GO/PF/IPR/K_signal≈{nonempty}")
    if body and nonempty == 0:
        print("[WARN] all rows look annotation-empty — check emapper/IPS paths and DB↔binary versions")


if __name__ == "__main__":
    main()
