#!/usr/bin/env python3
"""Build docs/figures/functional_spine.svg (editable, units = mm) and its PNG.

Same style as functional_overview.py (Arial, 0.5 pt lines, same palette).
    python3 docs/figures/src/functional_spine.py
PNG export needs `rsvg-convert`; text-fit checks use Pillow + Arial TTF (FONT_DIR) when available.
"""
import os, shutil, subprocess, sys
from xml.sax.saxutils import escape

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_SVG = os.path.join(HERE, '..', 'functional_spine.svg')
OUT_PNG = os.path.join(HERE, '..', 'functional_spine.png')
DPI = 200

PT = 25.4 / 72
SW = 0.5 * PT
FONT = 'Arial, Helvetica, sans-serif'
W, H = 183, 62

INK, GREY, LIGHT, PAPER = '#333333', '#6B6B6B', '#F0F0F0', '#F7F7F7'
BLUE, BLUE_BG = '#1F72AE', '#DEE4F0'
ORANGE = '#F77E12'
GREEN = '#119B76'
VIOLET = '#595594'

items, texts = [], []

def rect(x, y, w, h, stroke=INK, fill='#FFFFFF', dash=False, rx=1.2):
    d = f' stroke-dasharray="{4*SW:.3f} {3*SW:.3f}"' if dash else ''
    items.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{rx}" '
                 f'fill="{fill}" stroke="{stroke}" stroke-width="{SW:.3f}"{d}/>')
    return (x, y, w, h)

def text(x, y, s, size=7, bold=False, color=INK, anchor='middle', inside=None):
    wt = ' font-weight="bold"' if bold else ''
    items.append(f'<text x="{x:.2f}" y="{y:.2f}" font-family="{FONT}" font-size="{size*PT:.3f}"'
                 f'{wt} fill="{color}" text-anchor="{anchor}">{escape(s)}</text>')
    texts.append((x, y, s, size, bold, anchor, inside))

def arrow(x1, y1, x2, y2, color=GREY):
    items.append(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{color}" '
                 f'stroke-width="{SW:.3f}" marker-end="url(#arr)"/>')

def box(x, y, w, h, title, lines, stroke, fill='#FFFFFF', dash=False, tcolor=None):
    b = rect(x, y, w, h, stroke, fill, dash)
    lh = 3.3
    y0 = y + h/2 - len(lines) * lh / 2 + 1.0
    text(x + w/2, y0, title, 8, True, tcolor or stroke, inside=b)
    for i, s in enumerate(lines):
        text(x + w/2, y0 + (i + 1) * lh, s, 7, False, INK, inside=b)

# ---------------------------------------------------------------- layout
M = 3
text(M, 6.5, 'gene-function-annotation - beginner spine', 8, True, '#000000', 'start')
text(M, 10.8, 'Labels on proteins. Not gene finding. Add-ons come after Integrate, before Quality check.',
     7, False, GREY, 'start')

top, bh = 15, 20
spec = [  # width, title, lines, stroke, fill, dash, title colour
    (21.5, 'proteins.faa', ['structure release'], GREY, PAPER, True, GREY),
    (20, 'F0 QC', ['protein BUSCO'], ORANGE, '#FFFFFF', False, None),
    (22, 'Framework F1', ['DIAMOND', 'eggNOG · IPS'], BLUE, BLUE_BG, False, None),
    (35, 'Integrate', ['IPS · eggNOG', 'DIAMOND · Kofam', '→ merged_function_table.tsv'], GREEN, '#FFFFFF', False, None),
    (20.5, 'add-ons', ['F4/F6/F8 ingest'], VIOLET, '#FFFFFF', True, None),
    (21.5, 'Quality check', ['coverage', 'agreement', '→ QC table'], ORANGE, '#FFFFFF', False, None),
    (18, 'release', ['+ METHODS', 'F-L1'], INK, LIGHT, False, None),
]
gap = (W - 2*M - sum(s[0] for s in spec)) / (len(spec) - 1)
x = M
prev = None
for w, t, lines, st, fill, dash, tc in spec:
    box(x, top, w, bh, t, lines, st, fill, dash, tc)
    if prev is not None:
        arrow(prev, top + bh/2, x - 0.3, top + bh/2)
    prev = x + w
    x += w + gap

cy, ch = top + bh + 5, 18
card = rect(M, cy, W - 2*M, ch, '#BFBFBF', PAPER)
text(M + 3, cy + 4.6, 'Remember', 8, True, '#000000', 'start', inside=card)
text(M + 3, cy + 8.6, '• Mercator (F6) / AHRD (F4) / NLR (F8): ingest after Integrate, before Quality check '
     '(web Mercator may submit in parallel with F1).', 7, False, '#000000', 'start', inside=card)
text(M + 3, cy + 12.0, '• Script F2_eggnog.sh = eggNOG step inside framework F1 (not fast-frame F2). '
     'See README “F numbering”.', 7, False, '#000000', 'start', inside=card)
text(M + 3, cy + 15.4, 'Advanced playbook figure: functional_overview.png (optional after the spine).',
     7, False, GREY, 'start', inside=card)

# ---------------------------------------------------------------- write
svg = ['<?xml version="1.0" encoding="UTF-8"?>',
       f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}mm" height="{H}mm" viewBox="0 0 {W} {H}">',
       '<defs><marker id="arr" viewBox="0 0 6 6" refX="5.5" refY="3" markerWidth="1.8" markerHeight="1.8" '
       'markerUnits="userSpaceOnUse" orient="auto"><path d="M0,0.6 L5.5,3 L0,5.4 Z" fill="context-stroke"/></marker></defs>',
       f'<rect width="{W}" height="{H}" fill="#FFFFFF"/>'] + items + ['</svg>']
open(OUT_SVG, 'w').write('\n'.join(svg) + '\n')

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
    for x, y, s, size, bold, anchor, inside in texts:
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
