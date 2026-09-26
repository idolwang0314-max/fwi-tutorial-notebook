# UFWI-025 · High resolution 3D ultrasonic breast imaging by time-domain full waveform inversion

[总索引](../INDEX.md) · [可筛选网页](../index.html) · [阅读排序](../READING_RANKING.md)

- 作者：Felix Lucka; Mailyn Pérez-Liva; Bradley E Treeby; Ben T Cox
- 年份 / 期刊：2022 / Inverse Problems
- 发表类型 / 状态：journal / published
- 研究类型：医学超声 FWI
- 主题：三维加速专题、A、三维、随机源编码、内存优化、乳腺
- 核验程度：一手全文/相关段落
- 优先级：P0；精读第 3 篇
- DOI：[10.1088/1361-6420/ac3b64](https://doi.org/10.1088/1361-6420/ac3b64)

## 创新点 / 主要贡献

整合时间反演梯度、随机源编码和多尺度策略，使高分辨率三维乳腺FWI在适度GPU资源上可计算。

## 技术手段

time reversal梯度；延迟源编码；随机优化/迭代平均；粗细网格。

## 验证证据

逼真数值乳腺模型与多计算平台验证，论文目标预算为一天。

## 局限与评估

全部为数值proof-of-concept；不可称实测乳腺或临床系统；速度依赖资源/网格。

## 研究相关性

三维时域FWI工程实现与源编码应优先阅读的主文。

## 排序理由

真三维时域FWI计算路线的系统参考：源编码、梯度存储与多尺度；虽仅仿真，方法价值很高。

## 公开来源

- [https://doi.org/10.1088/1361-6420/ac3b64](https://doi.org/10.1088/1361-6420/ac3b64)
- [https://discovery.ucl.ac.uk/id/eprint/10139532/](https://discovery.ucl.ac.uk/id/eprint/10139532/)
- [https://arxiv.org/abs/2102.00755](https://arxiv.org/abs/2102.00755)
- [https://ir.cwi.nl/pub/31413/31413.pdf](https://ir.cwi.nl/pub/31413/31413.pdf)

检索核验日期2026-09-26。预印本2021-02-01；在线发表于2021，正式卷38(2022)025008；本库用卷期2022。

核验程度表示本轮查阅证据，不代表已复现实验。局限和研究价值包含整理者评估；不把贡献概括等同于全球首创。
