# UFWI-115 · Simulation-to-Real First-Break Segmentation for Efficient Inversion in Musculoskeletal Ultrasound Tomography

[总索引](../INDEX.md) · [可筛选网页](../index.html) · [阅读排序](../READING_RANKING.md)

- 作者：Yifei Sun; Yubing Li; Yannick Benezeth; Stéphanie Bricq; Yunrong Zhang; Lekang Jiang; Chang Su; Ligang Cui; Weijun Lin
- 年份 / 期刊：2026 / arXiv
- 发表类型 / 状态：preprint / preprint
- 研究类型：医学超声 FWI
- 主题：首波拾取、域迁移、肌骨、混合反演
- 核验程度：一手摘要
- 优先级：P1
- DOI：[10.48550/arxiv.2608.19828](https://doi.org/10.48550/arxiv.2608.19828)

## 创新点 / 主要贡献

把多道首至轨迹作为二维分割目标，并以真实噪声和少量弱标注缩小仿真到实验差距。

## 技术手段

轻量2D U-Net；分阶段训练；decoder-only微调；首至+Rytov HFWI。

## 验证证据

仿体、离体牛肢、人在体大腿；全FMC秒级拾取；含局部估计SNR<3dB案例。

## 局限与评估

预印本；需要真实噪声和少量实验标签，不是零标注泛化。

## 研究相关性

关注真实系统弱信号及初模构建，属于算法链条而非单一损失函数创新。

## 公开来源

- [https://arxiv.org/abs/2608.19828](https://arxiv.org/abs/2608.19828)
- [https://doi.org/10.48550/arXiv.2608.19828](https://doi.org/10.48550/arXiv.2608.19828)

2026-08-20 v1；未见正式刊载链接。

核验程度表示本轮查阅证据，不代表已复现实验。局限和研究价值包含整理者评估；不把贡献概括等同于全球首创。
