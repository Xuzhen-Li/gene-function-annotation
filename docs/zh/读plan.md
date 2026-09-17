# 读 plan 时看什么（英文 plan 指针）

`flow.py` 写出的 `my_fa_plan.md` 正文是**英文**。中文不必整篇翻译。

读的时候盯这几行即可：

1. **Frame** — 默认 **F1**（DIAMOND+eggNOG+IPS）；F2/F3/F5 是替代框，不是脚本文件名  
2. 每阶段 **Input → Software & purpose → Process → Output**  
3. **`F2_eggnog.sh`** 出现在 F1 骨架里 = F1 **内步**，不是框架 F2（见 [FAQ](FAQ_入门.md)）  
4. Add-ons（F4/F6/F8…）仅在对应 `want_*` 为 true 时出现  
5. 文末 **After this plan** — DB 路径 + 验收；术语 → [`99_术语表.md`](99_术语表.md)；起步 → [`03_怎么开始跑.md`](03_怎么开始跑.md)

今晚交卷：读懂 plan + DB 清单，不是跑完 IPS。离线勾选：[`../CLASSROOM_TONIGHT.md`](../CLASSROOM_TONIGHT.md)。
