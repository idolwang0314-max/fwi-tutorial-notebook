# UFWI-124 · Full-waveform inversion imaging of the human brain

[总索引](../INDEX.md) · [可筛选网页](../index.html) · [阅读排序](../READING_RANKING.md)

- 作者：Lluís Guasch; Oscar Calderón Agudo; Meng-Xing Tang; Parashkev Nachev; Michael Warner
- 年份 / 期刊：2020 / npj Digital Medicine
- 发表类型 / 状态：journal / published
- 研究类型：医学超声 FWI
- 主题：脑成像、AWI、三维、奠基
- 核验程度：一手全文/相关段落
- 优先级：P0；精读第 7 篇
- DOI：[10.1038/s41746-020-0240-8](https://doi.org/10.1038/s41746-020-0240-8)
- Europe PMC日期（可能为卷期日；差异见备注）：2020-03-06
- 2026-10-08 分类：existing_fulltext_reverification

2026-10-08 复核备注：全文边界复核：本轮重新核 Nature 主文 Fig.1(a)、Fig.3/4/5 及其 Results，Methods In silico modelling / FWI iteration；与旧2026-09-27笔记交叉核对。

一手材料阅读范围：本轮重新核 Nature 主文 Fig.1(a)、Fig.3/4/5 及其 Results，Methods In silico modelling / FWI iteration；与旧2026-09-27笔记交叉核对。

## 创新点 / 主要贡献

展示脑部超声定量 FWI 潜力：二维无颅骨先验 AWI→FWI，与已有真实颅骨初模的三维高分辨 FWI 分别验证。

## 技术手段

变密度声学有限差分。二维水初模以中心100 kHz单频带 AWI初始化，平滑后320 kHz至约850 kHz的L2-FWI；三维示例初模含真实颅骨、软组织均匀。

## 验证证据

Fig.4无骨先验 AWI→FWI为二维合成；Fig.3三维重建依赖真实颅骨初模。另有真人/离体颅骨透射波形实验验证穿透与SNR，不是实测脑FWI图像。

## 局限与评估

不能把二维无骨先验结果表述成已完成水初模三维AWI脑重建；没有活体脑FWI图像。3D数据用2D反演的失效提示离面物理问题；弹性/吸收/标定及计算规模仍是限制，原Fullwave3D为商业代码。

## 研究相关性

AWI在医学超声中最重要的动机论文之一，必须按证据层级阅读。

## 排序理由

Imperial超声FWI跨领域里程碑，值得读其数值验证和颅骨建模条件，避免把题名误解为临床已实现。

## 公开来源

- [https://www.nature.com/articles/s41746-020-0240-8](https://www.nature.com/articles/s41746-020-0240-8)
- [https://pmc.ncbi.nlm.nih.gov/articles/PMC7060331/](https://pmc.ncbi.nlm.nih.gov/articles/PMC7060331/)

保留原书目与2020-03-06出版日期；本轮修正二维AWI流程与三维骨先验示例被串接的证据边界。

核验程度表示本轮查阅证据，不代表已复现实验。局限和研究价值包含整理者评估；不把贡献概括等同于全球首创。
