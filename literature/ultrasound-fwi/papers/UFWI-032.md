# UFWI-032 · Implementation and Validation of the Multi-scale Gradient Smoothing Strategy for Breast Full Waveform Inversion

[总索引](../INDEX.md) · [可筛选网页](../index.html) · [阅读排序](../READING_RANKING.md)

- 作者：Yun Wu; Qiude Zhang; Weicheng Yan; Zhaohui Liu; Xiaolu Zeng; Mingyue Ding; Wu Qiu; Ming Yuchi
- 年份 / 期刊：2026 / Ultrasound in Medicine & Biology
- 发表类型 / 状态：journal / published
- 研究类型：医学超声 FWI
- 主题：三维加速专题、C
- 核验程度：历史笔记，尚未复核结论
- 优先级：P1
- DOI：[10.1016/j.ultrasmedbio.2026.02.020](https://doi.org/10.1016/j.ultrasmedbio.2026.02.020)
- Europe PMC日期（可能为卷期日；差异见备注）：2026-03-23

## 创新点 / 主要贡献

旧专题归纳：对每步 gradient 做 Gaussian low-pass，并随迭代逐渐减小 smoothing scale，先恢复大结构再恢复细节。

## 技术手段

对每步 gradient 做 Gaussian low-pass，并随迭代逐渐减小 smoothing scale，先恢复大结构再恢复细节。

## 验证证据

摘要明确报告相对 baselines 有更低 RMSE、更高 SSIM，且 in-vivo CNR 最高；摘要未列具体数值、schedule、网格或运行时间，因此这里不补写数字。

## 局限与评估

缺少真 3D 证据；过强 smoothing 会牺牲骨管壁与小血管边界。

## 研究相关性

这是比“直接将 mask 外全置水”更柔和、风险较低的 early-iteration 先验；可用于缓解密网格的高频伪影。

## 公开来源

- [https://doi.org/10.1016/j.ultrasmedbio.2026.02.020](https://doi.org/10.1016/j.ultrasmedbio.2026.02.020)
- [https://pubmed.ncbi.nlm.nih.gov/41876345/](https://pubmed.ncbi.nlm.nih.gov/41876345/)

沿用2026-08-29专题笔记；本轮未逐条重新打开外部来源，旧primary级别不继承。

核验程度表示本轮查阅证据，不代表已复现实验。局限和研究价值包含整理者评估；不把贡献概括等同于全球首创。
