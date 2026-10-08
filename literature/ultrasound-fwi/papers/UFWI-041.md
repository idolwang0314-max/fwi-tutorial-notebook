# UFWI-041 · Stride: A flexible software platform for high-performance ultrasound computed tomography

[总索引](../INDEX.md) · [可筛选网页](../index.html) · [阅读排序](../READING_RANKING.md)

- 作者：Carlos Cueto; Oscar Bates; George Strong; Javier Cudeiro; Fabio Luporini; Òscar Calderón Agudo; Gerard Gorman; Lluis Guasch; Meng-Xing Tang
- 年份 / 期刊：2022 / Computer Methods and Programs in Biomedicine
- 发表类型 / 状态：journal / published
- 研究类型：医学超声 FWI
- 主题：三维加速专题、D；2D/3D USCT software platform。、开源软件、高性能计算、三维
- 核验程度：一手摘要
- 优先级：P1
- DOI：[10.1016/j.cmpb.2022.106855](https://doi.org/10.1016/j.cmpb.2022.106855)
- Europe PMC日期（可能为卷期日；差异见备注）：2022-05-04

## 创新点 / 主要贡献

将超声优化问题高层接口、自动生成PDE求解器和集群并行统一成开源平台。

## 技术手段

Python接口；Devito波场求解；Mosaic分布式并行。

## 验证证据

解析解、颅骨模型对照；二维/三维数值及实验示例与并行扩展测试。

## 局限与评估

软件能力展示不等于临床有效性；默认物理模型范围要逐项检查。

## 研究相关性

最值得用于复现Imperial方法和检查forward/adjoint实现的入口。

## 公开来源

- [https://doi.org/10.1016/j.cmpb.2022.106855](https://doi.org/10.1016/j.cmpb.2022.106855)
- [https://arxiv.org/abs/2110.03345](https://arxiv.org/abs/2110.03345)
- [https://pubmed.ncbi.nlm.nih.gov/35588663/](https://pubmed.ncbi.nlm.nih.gov/35588663/)
- [https://github.com/trustimaging/stride](https://github.com/trustimaging/stride)

检索核验日期2026-09-26。正式2022-05-04，卷221。存在2023 corrigendum doi10.1016/j.cmpb.2023.107710，应与原文一起查阅。

核验程度表示本轮查阅证据，不代表已复现实验。局限和研究价值包含整理者评估；不把贡献概括等同于全球首创。
