# UFWI-134 · Automatic Skull-Template Alignment Without a Guidance Image

[总索引](../INDEX.md) · [可筛选网页](../index.html) · [阅读排序](../READING_RANKING.md)

- 作者：Oscar Bates; Carlos Cueto; Ciaran Coleman; Cameron A B Smith; Lluis Guasch; Oscar Calderon Agudo
- 年份 / 期刊：2026 / Ultrasound in Medicine & Biology
- 发表类型 / 状态：journal / published
- 研究类型：医学超声 FWI
- 主题：旋转平移、几何校准、脑成像、流形优化
- 核验程度：一手全文/相关段落
- 优先级：P0；精读第 22 篇
- DOI：[10.1016/j.ultrasmedbio.2026.05.003](https://doi.org/10.1016/j.ultrasmedbio.2026.05.003)
- Europe PMC日期（可能为卷期日；差异见备注）：2026-06-06
- 出版社在线日期：2026-06-05

## 创新点 / 主要贡献

MOFI直接通过超声RF数据配准颅骨模板，去掉同步MRI指导配准需求。

## 技术手段

manifold optimisation for full-waveform inversion；将模型变换参数（旋转/平移）经自动微分连接到FWI梯度，以RF波形失配优化姿态。

## 验证证据

in silico与in vitro；图4演示错误模板位置导致FWI失败，而MOFI配准后重建成功。

## 局限与评估

仍需已有颅骨模板；本文实验为简化声学/常密度/零衰减模型，且模板声速和形状也不完全准确；配准不等于从零重建颅骨。

## 研究相关性

与当前旋转平移研究最直接的新Imperial论文。

## 排序理由

MOFI以RF波形直接优化模板旋转平移，与几何参数反演高度相关；仍需已有模板。

## 公开来源

- [https://doi.org/10.1016/j.ultrasmedbio.2026.05.003](https://doi.org/10.1016/j.ultrasmedbio.2026.05.003)
- [https://www.umbjournal.org/article/S0301-5629%2826%2900188-2/fulltext](https://www.umbjournal.org/article/S0301-5629%2826%2900188-2/fulltext)
- [https://arxiv.org/abs/2601.14533](https://arxiv.org/abs/2601.14533)

检索核验日期2026-09-26。预印本2026-01-20；出版社目录online2026-06-05，EuropePMC记2026-06-06，正式卷52(9):1854–1861。已读原文In vitro、方法及图4说明。

核验程度表示本轮查阅证据，不代表已复现实验。局限和研究价值包含整理者评估；不把贡献概括等同于全球首创。
