# UFWI-096 · Lossy checkpoint compression in full waveform inversion: a case study with ZFPv0.5.5 and the overthrust model

[总索引](../INDEX.md) · [可筛选网页](../index.html) · [阅读排序](../READING_RANKING.md)

- 作者：Navjot Kukreja; Jan Hückelheim; Mathias Louboutin; John Washbourne; Paul H. J. Kelly; Gerard J. Gorman
- 年份 / 期刊：2022 / Geoscientific Model Development
- 发表类型 / 状态：journal / published
- 研究类型：地球物理及可迁移方法
- 主题：计算加速、三维、波场压缩、开源
- 核验程度：一手摘要
- 优先级：P1
- DOI：[10.5194/gmd-15-3815-2022](https://doi.org/10.5194/gmd-15-3815-2022)

## 创新点 / 主要贡献

将checkpoint重计算与受控有损压缩结合，联合权衡显存、误差及运行时间。

## 技术手段

ZFP压缩+checkpointing；量化梯度/模型误差与重计算成本。

## 验证证据

Overthrust地震FWI数值案例；论文及代码入口公开。

## 局限与评估

压缩容差依赖波场动态范围；不能以压缩比替代成像质量验证。

## 研究相关性

为三维超声保存波场提供可复现工程路线，需对含骨/衰减波场重新设容差。

## 公开来源

- [https://gmd.copernicus.org/articles/15/3815/2022/gmd-15-3815-2022.html](https://gmd.copernicus.org/articles/15/3815/2022/gmd-15-3815-2022.html)
- [https://doi.org/10.5194/gmd-15-3815-2022](https://doi.org/10.5194/gmd-15-3815-2022)

本轮核验；创新为文献贡献概括，迁移价值/局限含本库评估，不是全球首创证明。

核验程度表示本轮查阅证据，不代表已复现实验。局限和研究价值包含整理者评估；不把贡献概括等同于全球首创。
