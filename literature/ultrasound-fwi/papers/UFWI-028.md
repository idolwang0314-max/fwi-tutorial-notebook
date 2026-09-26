# UFWI-028 · 3-D Nonlinear Acoustic Inverse Scattering: Algorithm and Quantitative Results

[总索引](../INDEX.md) · [可筛选网页](../index.html) · [阅读排序](../READING_RANKING.md)

- 作者：J. W. Wiskin; D. T. Borup; E. Iuanow; J. Klock; Mark W. Lenox
- 年份 / 期刊：2017 / IEEE Transactions on Ultrasonics, Ferroelectrics, and Frequency Control (TUFFC)
- 发表类型 / 状态：journal / published
- 研究类型：医学超声 FWI
- 主题：三维加速专题、A
- 核验程度：历史笔记，尚未复核结论
- 优先级：P1
- DOI：[10.1109/tuffc.2017.2706189](https://doi.org/10.1109/tuffc.2017.2706189)

## 创新点 / 主要贡献

旧专题归纳：8×192 接收阵列，360° 旋转、约 1° 间隔，垂直步距约 2 mm；使用 3D phase-screen/Fourier split-step 的 paraxial forward/adjoint，nonlinear CG 和 0.3–1.3 MHz frequency continuation，TOF 初模。

## 技术手段

8×192 接收阵列，360° 旋转、约 1° 间隔，垂直步距约 2 mm；使用 3D phase-screen/Fourier split-step 的 paraxial forward/adjoint，nonlinear CG 和 0.3–1.3 MHz frequency continuation，TOF 初模。

## 验证证据

六个圆柱体平均相对声速误差的绝对值约 0.22%；实验估计 intrinsic resolution 约 1.414 mm。论文没有给出可核验的实测重建运行时间。

## 局限与评估

paraxial approximation 对大角度散射和 backscatter 不准确；这一路线属于成熟 prior art，不能把 split-step/Green propagation 本身当新颖点。

## 研究相关性

说明“近似 3D forward + 频率递进”可在真实大体积数据上形成定量结果；如果目标是先改善 z 连续性，可以把 paraxial/phase-screen 作为低成本 3D baseline，而不是一开始就全带宽精确 FDTD。

## 公开来源

- [https://doi.org/10.1109/TUFFC.2017.2706189](https://doi.org/10.1109/TUFFC.2017.2706189)
- [https://pmc.ncbi.nlm.nih.gov/articles/PMC6214813/](https://pmc.ncbi.nlm.nih.gov/articles/PMC6214813/)
- [https://doi.org/10.1109/tuffc.2017.2706189](https://doi.org/10.1109/tuffc.2017.2706189)

沿用2026-08-29专题笔记；本轮未逐条重新打开外部来源，旧primary级别不继承。；本地PDF前1–2页的首页题名/DOI已核对，未据此上调外部证据等级。；旧专题将E. Iuanow扩写为Eric，首页不足以支持，现保留E. Iuanow。

核验程度表示本轮查阅证据，不代表已复现实验。局限和研究价值包含整理者评估；不把贡献概括等同于全球首创。
