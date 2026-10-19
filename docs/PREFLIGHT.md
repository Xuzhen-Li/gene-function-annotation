# Preflight check before RUN=1 / 运行前检查

<!-- Prose on this page is a placeholder. Replace each [[TODO-TEXT]] with reviewed text. -->

[[TODO-TEXT: what preflight is, and that it is the check before every RUN=1 (print_qc_commands.py only prints commands).]]

```bash
python3 pipeline/preflight.py --list
python3 pipeline/preflight.py --env config/local.env --step diamond
echo $?    # 0 = PASS, 1 = STOP, 2 = usage error
```

| Step | Script it checks |
|---|---|
| `diamond` | `pipeline/F1_diamond.sh` |
| `eggnog` | `pipeline/F2_eggnog.sh` |
| `interproscan` | `pipeline/F3_interproscan.sh` |
| `kofam` | `pipeline/F1b_kofam.sh` |
| `merge` | `pipeline/F_merge_tables.py` |
| `nlr` | `pipeline/F8_run.sh` |
| `orthofinder` | `pipeline/F7_orthofinder.sh` |
| `itak` | `pipeline/F9_itak.sh` |
| `release` | `pipeline/F_release.sh` |

[[TODO-TEXT: how to read [PASS] / [STOP] / [WARN] lines and the next-step hint; why EGGNOG_PFAM_REALIGN must be set; that PROTEINS_FA comes from the structure release.]]

## 中文

[[TODO-TEXT: 中文说明，内容与英文部分对应。]]
