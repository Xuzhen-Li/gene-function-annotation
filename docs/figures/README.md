# Figures

| File | Role |
|------|------|
| `functional_spine.svg` / `.png` | **Beginner** one-glance spine (zh + root README) |
| `functional_overview.*` | Advanced playbook (keep; fold on zh entry) |
| `plant_sim_three_lines.*` | Copy of structure classroom crop lines |

Do not edit the `.svg` or `.png` image files by hand (`plant_sim_three_lines.*` is copied from the structure repo and has no script here). Edit the Python script that holds the layout and box lists. Open a terminal (Mac: Terminal app; Linux: a terminal window; cluster: your login shell) inside the `gene-function-annotation` folder (the repo root). Run `python3 docs/figures/src/functional_spine.py` or `python3 docs/figures/src/functional_overview.py`. Each script writes the `.svg` and uses `rsvg-convert` (librsvg) to export the `.png` at 200 dpi (dots per inch). Without `rsvg-convert`, it prints `"rsvg-convert not found: PNG not updated"`. Text-fit checks use Pillow and an Arial font via `FONT_DIR`, and are skipped when either is missing.
