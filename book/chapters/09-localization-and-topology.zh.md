# 第 9 章 定位与拓扑

*本章收录[主页第 8 节](../../README.zh.md#section-8)：该节说明、含论文、实验室、权威度和评价的完整工具表，以及评测要点。链接指回仓库。*

信号肽、跨膜拓扑结构与亚细胞定位预测（F1+ 附加项）。

**需要：** 通常只需蛋白序列（用于 SignalP、TargetP 等工具）。结果应作为 F1+ 的附加列并入总表，不要另建第二张主表。[按场景列出的数据需求](../../README.zh.md#data-needs)

**分组：**
- *信号肽与拓扑*（互补）：SignalP 6.0、DeepTMHMM 或 TMbed 或 TMHMM 2.0 或 Phobius。信号肽用 SignalP 6.0，再加一个跨膜拓扑工具：默认用 DeepTMHMM 或 TMbed，TMHMM 2.0 只用于复现旧表。Phobius 和 TMbed 也能判定信号肽。
- *细胞器定位*（可替代）：TargetP 2.0、LOCALIZER、DeepLoc 2.1、WoLF PSORT。质体与线粒体定位用 TargetP 2.0；多亚细胞区室判定用 DeepLoc 2.1。
- *植物分泌组*（按顺序）：SignalP 6.0、ApoplastP。在 SignalP 之后用 ApoplastP 区分质外体蛋白。


| 工具 | 角色 | 用途 / 何时用 | 原始论文 | 实验室（通讯作者，机构） | 权威度（档位 · 被引） | 评价（出处） |
|---|---|---|---|---|---|---|
| [SignalP 6.0](https://services.healthtech.dtu.dk/services/SignalP-6.0/) | 默认（信号肽） | 基于蛋白语言模型预测全部五类信号肽的工具。 | [Nature Biotechnology 2022](https://doi.org/10.1038/s41587-021-01156-3) | Henrik Nielsen (Technical University of Denmark) | 标准 · 3441 次 | 论文摘要：“We introduce SignalP 6.0, a machine learning model that detects all five SP types and is applicable to metagenomic data.” |
| [TMHMM 2.0](https://services.healthtech.dtu.dk/services/TMHMM-2.0/) | 备选 | 基于 HMM 预测跨膜螺旋的工具。 | [Journal of Molecular Biology 2001](https://doi.org/10.1006/jmbi.2000.4315) | Anders Krogh (Technical University of Denmark) | 标准 · 14533 次 | 无摘要或仓库说明可引；见原文 |
| [Phobius](https://phobius.sbc.su.se/) | 备选 | 联合预测跨膜拓扑结构与信号肽的工具。 | [Journal of Molecular Biology 2004](https://doi.org/10.1016/j.jmb.2004.03.016) | Erik L. L. Sonnhammer (Karolinska Institutet) | 标准 · 2783 次 | 无摘要或仓库说明可引；见原文 |
| [WoLF PSORT](https://wolfpsort.hgc.jp/) | 备选 | 内置植物模型的亚细胞定位预测工具。 | [Nucleic Acids Research 2007](https://doi.org/10.1093/nar/gkm259) | Kenta Nakai (Korea Center for Disease Control and Prevention) | 标准 · 4718 次 | 无摘要或仓库说明可引；见原文 |
| [LOCALIZER](https://localizer.csiro.au/) | 备选 | 预测植物蛋白与病原效应蛋白在叶绿体、线粒体及细胞核定位的工具。 | [Scientific Reports 2017](https://doi.org/10.1038/srep44598) | Jana Sperschneider (Commonwealth Scientific and Industrial Research Organisation) | 标准 · 521 次 | 作者摘要原句：“LOCALIZER shows greater prediction accuracy for chloroplast and mitochondrial targeting compared to other methods for 652 plant proteins.” |
| [DeepLoc 2.1](https://services.healthtech.dtu.dk/services/DeepLoc-2.1/) | 备选 | 基于蛋白语言模型预测亚细胞定位与膜蛋白类型的工具。 | [Nucleic Acids Research 2024](https://doi.org/10.1093/nar/gkae237) | Henrik Nielsen (Technical University of Denmark) | 成熟 · 290 次 | 作者摘要原句：“Notably, DeepLoc 2.1 outperforms existing models, with the larger ProtT5 model exhibiting a marginal advantage over the ESM-1B model.” |
| [TargetP 2.0](https://services.healthtech.dtu.dk/services/TargetP-2.0/) | 备选 | 预测 N 端靶向肽（信号肽、线粒体、叶绿体与类囊体转运肽）的工具。 | [Life Science Alliance 2019](https://doi.org/10.26508/lsa.201900429) | Arne Elofsson (Stockholm University) +1 | 标准 · 1263 次 | 论文摘要：“Here, we demonstrate this by presenting TargetP 2.0, a novel state-of-the-art method to identify N-terminal sorting signals, which direct proteins to the secretory pathway, mitochondria, and chloroplasts or other plastids.” |
| [DeepTMHMM](https://dtu.biolib.com/DeepTMHMM) | 默认拓扑（DeepTMHMM 或 TMbed） | 跨膜拓扑结构预测工具（预印本）。 | [bioRxiv (Cold Spring Harbor Laboratory) 2022](https://doi.org/10.1101/2022.04.08.487609) | Ole Winther (University of Copenhagen) | 标准 · 1984 次 | 作者摘要原句：“We introduce DeepTMHMM, a deep learning protein language model-based algorithm that can detect and predict the topology of both alpha helical and beta barrels proteins with unprecedented accuracy.” |
| [TMbed](https://github.com/BernhoferM/TMbed) | 默认拓扑（DeepTMHMM 或 TMbed） | 基于 ProtT5 嵌入预测跨膜螺旋、β-桶和信号肽；在全蛋白组规模下运行很快。 | [BMC Bioinformatics 2022](https://doi.org/10.1186/s12859-022-04873-x) | Michael Bernhofer (Technical University of Munich) | 成熟 · 122 次 | 作者摘要原句：“TMbed completes predictions for entire proteomes within hours on a single consumer-grade desktop machine at performance levels similar or better than methods, which are using evolutionary information from multiple sequence alignments (MSAs) of protein …”；GitHub 最后提交 2026-02 |
| [ApoplastP](https://apoplastp.csiro.au/) | 备选 | 预测植物蛋白或效应蛋白是否定位于质外体；构建分泌组时可与 SignalP 互补。 | [New Phytologist 2017](https://doi.org/10.1111/nph.14946) | Jana Sperschneider (Commonwealth Scientific and Industrial Research Organisation) | 成熟 · 225 次 | 作者摘要原句：“ApoplastP predicts apoplastic localization in effectors with a sensitivity of 75% and a false positive rate of 5%, improving the accuracy of cysteine-rich classifiers by > 13%.” |
| [SUBA3](https://suba.live/) | 备选 | 整合实验与预测的拟南芥亚细胞定位数据库；用于核对植物定位预测。 | [Nucleic Acids Research 2012](https://doi.org/10.1093/nar/gks1151) | A. Harvey Millar (The University of Western Australia) | 成熟 · 318 次 | 无摘要或仓库说明可引；见原文 |
