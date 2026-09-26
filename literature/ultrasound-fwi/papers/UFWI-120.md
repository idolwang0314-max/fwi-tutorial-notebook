# UFWI-120 · Graph neural networks for full waveform inversion

[总索引](../INDEX.md) · [可筛选网页](../index.html) · [阅读排序](../READING_RANKING.md)

- 作者：Divya Shyam Singh; Leon Herrmann; Tim Bürchner; Felix Dietrich; Stefan Kollmannsberger
- 年份 / 期刊：2026 / Computational Mechanics
- 发表类型 / 状态：journal / published
- 研究类型：超声 NDT / 导波 FWI
- 主题：图网络、参数化、迁移学习、三维弹性
- 核验程度：一手全文/相关段落
- 优先级：P1
- DOI：[10.1007/s00466-026-02796-5](https://doi.org/10.1007/s00466-026-02796-5)

## 创新点 / 主要贡献

以GCN参数化把神经FWI从规则网格扩展到任意几何，并从2D声学预训练迁移到3D弹性。

## 技术手段

首迭代伴随梯度到密度损伤场预训练；GCN；Salvus正演；PDE约束优化。

## 验证证据

不同几何、阵列分布及材料的数值实验。

## 局限与评估

主要数值验证；依赖预训练和商业Salvus；2D到3D迁移不保证任意损伤分布均泛化。

## 研究相关性

相比直接逆网络保留物理拟合与残差，适合研究学习参数化如何改善病态性。

## 公开来源

- [https://link.springer.com/article/10.1007/s00466-026-02796-5](https://link.springer.com/article/10.1007/s00466-026-02796-5)
- [https://doi.org/10.1007/s00466-026-02796-5](https://doi.org/10.1007/s00466-026-02796-5)

2026-06-04；核读摘要、方法和参数化部分，非全文逐段精读。

核验程度表示本轮查阅证据，不代表已复现实验。局限和研究价值包含整理者评估；不把贡献概括等同于全球首创。
