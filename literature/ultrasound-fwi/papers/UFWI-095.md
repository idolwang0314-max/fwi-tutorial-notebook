# UFWI-095 · Wave-based inversion at scale on GPUs with randomized trace estimation

[总索引](../INDEX.md) · [可筛选网页](../index.html) · [阅读排序](../READING_RANKING.md)

- 作者：Mathias Louboutin; Felix J. Herrmann
- 年份 / 期刊：2023 / Geophysical Prospecting
- 发表类型 / 状态：journal / published
- 研究类型：地球物理及可迁移方法
- 主题：计算加速、随机梯度、三维、开源
- 核验程度：一手摘要
- 优先级：P1
- DOI：[10.1111/1365-2478.13405](https://doi.org/10.1111/1365-2478.13405)

## 创新点 / 主要贡献

用随机迹估计压缩伴随成像条件所需的正向波场时间历史。

## 技术手段

随机探针累计、近似梯度、GPU实现；与源编码减少炮数是不同层面。

## 验证证据

声学二维/三维FWI与TTI成像；作者提供TimeProbeSeismic.jl实现。

## 局限与评估

近似梯度有方差；须比较同精度总成本和收敛，不是无损替代。

## 研究相关性

三维超声显存受限时可研究，先量化随机误差及含衰减条件。

## 公开来源

- [https://slim.gatech.edu/node/7269](https://slim.gatech.edu/node/7269)
- [https://slim.gatech.edu/Publications/Public/Journals/GeophysicalProspecting/2023/louboutin2023rte/paper.html](https://slim.gatech.edu/Publications/Public/Journals/GeophysicalProspecting/2023/louboutin2023rte/paper.html)
- [https://doi.org/10.1111/1365-2478.13405](https://doi.org/10.1111/1365-2478.13405)

本轮核验；创新为文献贡献概括，迁移价值/局限含本库评估，不是全球首创证明。

核验程度表示本轮查阅证据，不代表已复现实验。局限和研究价值包含整理者评估；不把贡献概括等同于全球首创。
