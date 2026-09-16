# Plant simulation trio — function side

Paired with [gene-structure-annotation `examples/plant_sim/`](https://github.com/Xuzhen-Li/gene-structure-annotation/tree/main/examples/plant_sim) (same folder IDs).
Paths in `env.snippet` are placeholders — do not commit real cluster paths.

| ID | Species | Function stress |
|----|---------|-----------------|
| `01_vitis_s1_s7` | Grape | F1 + `want_nlr` (F8) |
| `02_oryza_s1` | Rice | Plain F1; Add-ons (none) |
| `03_solanum_s11` | Tomato | F1 + Mercator (F6) |

## Run (function)

```bash
cd gene-function-annotation
for d in examples/plant_sim/01_vitis_s1_s7 examples/plant_sim/02_oryza_s1 examples/plant_sim/03_solanum_s11; do
  python3 pipeline/flow_tool/flow.py --answers "$d/answers.sim.yaml" --emit-commands -o "$d/plan.md"
done
# Optional: merge this folder's env.snippet into config/local.env, then
# python3 pipeline/print_qc_commands.py
```

**Classroom minimum ≠ finish IPS tonight** — see [`docs/START_HERE.md`](../../docs/START_HERE.md).
These sims do **not** download DBs or run DIAMOND/eggNOG/IPS.
