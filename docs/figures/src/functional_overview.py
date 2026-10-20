#!/usr/bin/env python3
"""Build docs/figures/functional_overview.svg (editable, units = mm) and its PNG.

Edit the BOXES / layout below, then run:
    python3 docs/figures/src/functional_overview.py
PNG export needs `rsvg-convert` (librsvg). Text-fit checks use Pillow + an Arial
TTF when available (set FONT_DIR); otherwise they are skipped.
"""
import os, shutil, subprocess, sys
from xml.sax.saxutils import escape

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_SVG = os.path.join(HERE, '..', 'functional_overview.svg')
OUT_PNG = os.path.join(HERE, '..', 'functional_overview.png')
DPI = 200

PT = 25.4 / 72            # mm per pt
SW = 0.5 * PT             # 0.5 pt stroke
FONT = 'Arial, Helvetica, sans-serif'
W, H = 183, 86            # mm (double column)

# restrained palette
INK, GREY, LIGHT, PAPER = '#333333', '#6B6B6B', '#F0F0F0', '#F7F7F7'
BLUE, BLUE_BG = '#1F72AE', '#DEE4F0'
ORANGE, ORANGE_BG = '#F77E12', '#FBD6A0'
GREEN = '#119B76'
VIOLET = '#595594'

items, boxes_txt = [], []   # boxes_txt: (bbox, label, container) for checks

def rect(x, y, w, h, stroke=INK, fill='#FFFFFF', dash=False, rx=1.2):
    d = f' stroke-dasharray="{4*SW:.3f} {3*SW:.3f}"' if dash else ''
    items.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{rx}" '
                 f'fill="{fill}" stroke="{stroke}" stroke-width="{SW:.3f}"{d}/>')
    return (x, y, w, h)

def text(x, y, s, size=7, bold=False, color=INK, anchor='middle', inside=None):
    wt = ' font-weight="bold"' if bold else ''
    items.append(f'<text x="{x:.2f}" y="{y:.2f}" font-family="{FONT}" font-size="{size*PT:.3f}"'
                 f'{wt} fill="{color}" text-anchor="{anchor}">{escape(s)}</text>')
    boxes_txt.append((x, y, s, size, bold, anchor, inside))

def arrow(pts, color=GREY, dash=False):
    d = f' stroke-dasharray="{4*SW:.3f} {3*SW:.3f}"' if dash else ''
    p = ' '.join(f'{a:.2f},{b:.2f}' for a, b in pts)
    items.append(f'<polyline points="{p}" fill="none" stroke="{color}" stroke-width="{SW:.3f}"{d} '
                 f'marker-end="url(#arr)"/>')

def labelled_box(x, y, w, h, title, lines, stroke=INK, fill='#FFFFFF', dash=False, tcolor=None):
    b = rect(x, y, w, h, stroke, fill, dash)
    n = 1 + len(lines)
    lh = 3.3
    y0 = y + h/2 - (n - 1) * lh / 2 + 1.0
    text(x + w/2, y0, title, 8, True, tcolor or stroke, inside=b)
    for i, s in enumerate(lines):
        text(x + w/2, y0 + (i + 1) * lh, s, 7, False, INK, inside=b)
    return b

# ---------------------------------------------------------------- layout
M = 3
text(M, 6.5, 'gene-function-annotation - functional overview', 8, True, INK, 'start')

top, hgt = 12, 38                      # main row
mid = top + hgt / 2
cols = [20, 18, 31, 35, 28, 25]        # widths; gaps fill the rest
gap = (W - 2*M - sum(cols)) / (len(cols) - 1)
xs = []
x = M
for w in cols:
    xs.append(x); x += w + gap

b_in = labelled_box(xs[0], top, cols[0], hgt, 'Input',
                    ['proteins.faa', 'structure', 'release'], GREY, PAPER, dash=True, tcolor=GREY)
b_f0 = labelled_box(xs[1], top, cols[1], hgt, 'F0 QC', ['protein', 'BUSCO'], ORANGE, '#FFFFFF')

# F1 framework container with stacked tools
fx, fw = xs[2], cols[2]
b_f1 = rect(fx, top, fw, hgt, BLUE, BLUE_BG)
text(fx + fw/2, top + 4.2, 'F1 framework', 8, True, BLUE, inside=b_f1)
tools = [('DIAMOND', False), ('eggNOG-mapper', False), ('InterProScan', False), ('KofamScan (opt.)', True)]
ty, th, tg = top + 6.6, 6.2, 1.4
for name, dash in tools:
    tb = rect(fx + 2, ty, fw - 4, th, BLUE, '#FFFFFF', dash)
    text(fx + fw/2, ty + th/2 + 0.9, name, 7, False, INK, inside=tb)
    ty += th + tg

b_int = labelled_box(xs[3], top, cols[3], hgt, 'Integrate',
                     ['→ gene-level table', 'merged_function_table.tsv'], GREEN, '#FFFFFF')
b_qa = labelled_box(xs[4], top, cols[4], hgt, 'Quality check',
                    ['coverage', 'agreement rate', '→ QC table'], ORANGE, '#FFFFFF')
b_rel = labelled_box(xs[5], top, cols[5], hgt, 'Release',
                     ['F_release.sh', 'release/<TAG>/', 'METHODS'], INK, LIGHT)

for i in range(len(xs) - 1):
    arrow([(xs[i] + cols[i], mid), (xs[i+1] - 0.3, mid)])

# bottom row
bt, bh = top + hgt + 8, 24
# flow tool under Input + F0
fl_w = xs[1] + cols[1] - xs[0]
b_flow = labelled_box(xs[0], bt, fl_w, bh, 'Plan the frame',
                      ['flow.py → my_fa_plan.md', 'F1 default', 'F2 · F3 · F5'], GREY, '#FFFFFF', dash=False, tcolor=GREY)
arrow([(xs[0] + fl_w, bt + bh/2), (fx + fw/2, bt + bh/2), (fx + fw/2, top + hgt + 0.3)], GREY, dash=True)

# add-ons under Integrate + Quality check
ax, aw = xs[3], xs[4] + cols[4] - xs[3]
b_add = rect(ax, bt, aw, bh, VIOLET, '#FFFFFF', dash=True)
text(ax + aw/2, bt + 4.2, 'Add-ons (optional)', 8, True, VIOLET, inside=b_add)
addons = ['F4 AHRD names', 'F4b PANNZER', 'F6 Mercator BINs', 'F8 NLR families']
iw = (aw - 6) / 2
for k, name in enumerate(addons):
    cx = ax + 2 + (k % 2) * (iw + 2)
    cy = bt + 7.2 + (k // 2) * 8
    ib = rect(cx, cy, iw, 6.2, VIOLET, '#FFFFFF')
    text(cx + iw/2, cy + 3.1 + 0.9, name, 7, False, INK, inside=ib)
# master -> add-ons -> QC
icx = xs[3] + cols[3]/2
qcx = xs[4] + cols[4]/2
arrow([(icx, top + hgt), (icx, bt - 0.3)], VIOLET)
arrow([(qcx, bt), (qcx, top + hgt + 0.3)], VIOLET)

# release gates under Release
b_gate = labelled_box(xs[5], bt, cols[5], bh, 'Release gates',
                      ['Gate-F1 to F7', 'provenance', 'BUSCO · versions'], INK, '#FFFFFF')
arrow([(xs[5] + cols[5]/2, bt), (xs[5] + cols[5]/2, top + hgt + 0.3)], INK)

# ---------------------------------------------------------------- write
svg = [f'<?xml version="1.0" encoding="UTF-8"?>',
       f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}mm" height="{H}mm" viewBox="0 0 {W} {H}">',
       '<defs><marker id="arr" viewBox="0 0 6 6" refX="5.5" refY="3" markerWidth="6" markerHeight="6" '
       'markerUnits="userSpaceOnUse" orient="auto"><path d="M0,0.6 L5.5,3 L0,5.4 Z" fill="context-stroke"/></marker></defs>',
       f'<rect width="{W}" height="{H}" fill="#FFFFFF"/>'] + items + ['</svg>']
# marker size in user units (mm): 6 → scale down
svg[2] = svg[2].replace('markerWidth="6" markerHeight="6"', 'markerWidth="1.8" markerHeight="1.8"')
open(OUT_SVG, 'w').write('\n'.join(svg) + '\n')

# ---------------------------------------------------------------- checks
def checks():
    try:
        from PIL import ImageFont
    except ImportError:
        return ['(skipped: Pillow not installed)']
    fd = os.environ.get('FONT_DIR', os.path.expanduser('~/.local/share/fonts'))
    try:
        reg = ImageFont.truetype(os.path.join(fd, 'Arial.TTF'), 1000)
        bld = ImageFont.truetype(os.path.join(fd, 'Arialbd.TTF'), 1000)
    except OSError:
        return ['(skipped: Arial TTF not found)']
    errs, bbs = [], []
    for x, y, s, size, bold, anchor, inside in boxes_txt:
        tw = (bld if bold else reg).getlength(s) / 1000 * size * PT
        em = size * PT
        x0 = {'start': x, 'middle': x - tw/2, 'end': x - tw}[anchor]
        bb = (x0, y - 0.74*em, x0 + tw, y + 0.21*em)
        bbs.append((bb, s))
        if bb[0] < 0 or bb[2] > W or bb[1] < 0 or bb[3] > H:
            errs.append(f'outside canvas: {s}')
        if inside:
            bx, by, bw, bh_ = inside
            if bb[0] < bx + 0.8 or bb[2] > bx + bw - 0.8 or bb[1] < by + 0.5 or bb[3] > by + bh_ - 0.5:
                errs.append(f'outside box: {s}')
    for i in range(len(bbs)):
        for j in range(i + 1, len(bbs)):
            a, b = bbs[i][0], bbs[j][0]
            if a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]:
                errs.append(f'overlap: {bbs[i][1]} x {bbs[j][1]}')
    return errs

errs = checks()
for e in errs:
    print(e)
if shutil.which('rsvg-convert'):
    subprocess.run(['rsvg-convert', '-d', str(DPI), '-p', str(DPI), OUT_SVG, '-o', OUT_PNG], check=True)
else:
    print('rsvg-convert not found: PNG not updated', file=sys.stderr)
sys.exit(1 if [e for e in errs if not e.startswith('(')] else 0)
