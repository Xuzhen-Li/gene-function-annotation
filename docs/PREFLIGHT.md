# Preflight check before RUN=1 / 运行前检查

Open a terminal (Mac: Terminal app; Linux: a terminal window; cluster: your login shell) inside the `gene-function-annotation` folder to run `python3 pipeline/preflight.py`, which is the preflight check you must run before every `RUN=1` (a setting that makes a pipeline script actually run, while without it scripts and `print_qc_commands.py` only print commands); you can run `python3 pipeline/preflight.py --list` to list steps and `python3 pipeline/preflight.py --env config/local.env --step diamond` to check one step and run nothing, verifying that input files exist (files made by later steps are not required), no value is still a placeholder such as `/path/to` or `YOUR_*` (a temporary text you must replace with your real path or setting), output paths can be created, needed tools are installed or the container image is present (a packaged file with all needed software), and values with a fixed set of choices are valid.

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

Each output line starts with `[PASS]`, `[STOP]` or `[WARN]` and names the problem and the fix, and running `echo $?` shows the exit code (a number the program returns to show if it worked: 0 = PASS, 1 = STOP, 2 = usage error); only STOP lines block and print "Do not use RUN=1 yet." plus the command to re-run the check, while PASS prints "PASS. Next:" then `set -a && source config/local.env && set +a` and the `RUN=1` command; you must set `EGGNOG_PFAM_REALIGN` to `none`, `realign` or `denovo` in `config/local.env` because if it is unset you get a STOP since the script default `'realtime'` is not accepted by eggNOG-mapper (`emapper`, a tool that assigns gene functions), and `PROTEINS_FA` is the protein file made in `gene-structure-annotation` at `release/<TAG>/proteins.faa` (if it is not under a `release/` folder, a WARN asks you to record its source and `sha256`, which is a unique file fingerprint, in `METHODS`).

## 中文

请在 `gene-function-annotation` 文件夹中打开终端（Mac：Terminal 应用；Linux：终端窗口；集群：登录 shell）并在每次使用 `RUN=1`（让流程脚本真正运行的设置，不加时脚本和 `print_qc_commands.py` 只打印命令）前运行预检查 `python3 pipeline/preflight.py`；你可以运行 `python3 pipeline/preflight.py --list` 查看步骤，或运行 `python3 pipeline/preflight.py --env config/local.env --step diamond` 检查单个步骤而不实际运行程序，它会确认输入文件存在（后续步骤生成的文件不要求）、没有 `/path/to` 或 `YOUR_*` 这样的占位符（需要替换为你真实路径或设置的临时文本）、输出路径可创建、所需工具已安装或容器镜像存在（打包了所需软件的文件）且固定选项的值有效；每行输出以 `[PASS]`、`[STOP]` 或 `[WARN]` 开头并指出问题和修复方法，运行 `echo $?` 可查看退出码（程序返回的代表运行状态的数字：0 = PASS，1 = STOP，2 = 用法错误），只有 STOP 行会阻断运行并提示 "Do not use RUN=1 yet." 及重新检查的命令，PASS 则提示 "PASS. Next:" 以及 `set -a && source config/local.env && set +a` 和 `RUN=1` 命令；你必须在 `config/local.env` 中将 `EGGNOG_PFAM_REALIGN` 设为 `none`、`realign` 或 `denovo`，若未设置会触发 STOP，因为 eggNOG-mapper（`emapper`，一种基因功能注释工具）不接受脚本默认值 `'realtime'`，此外 `PROTEINS_FA` 是 `gene-structure-annotation` 生成的蛋白文件 `release/<TAG>/proteins.faa`，如果它不在 `release/` 文件夹下，WARN 会要求你在 `METHODS` 中记录其来源和 `sha256`（一种唯一的文件校验指纹）。
