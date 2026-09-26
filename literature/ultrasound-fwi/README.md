# 超声 FWI 文献库 · Ultrasound FWI literature library

**151 条文献记录，26 篇精读排序；逐篇提供创新点、技术手段、验证证据、局限和公开来源。**

合并历史多智能体文献调研与截至 **2026-09-26** 的公开检索，重点为 **Ultrasonics、IEEE TUFFC/TUSON、Geophysics/GJI**，并追踪 **Imperial College** 和 **李玉冰（Yubing Li）** 等作者路线。主要覆盖 2020—2026 年，保留关键奠基论文。一条 2027 卷期记录已于 2026 在线公开，书目年与在线日期分别记录。

## 从这里开始

| 入口 | 内容 |
|---|---|
| **[研究综述](REVIEW_CN.md)** | 前沿技术路线、值得追踪的进展与评价边界 |
| **[26 篇精读排序](READING_RANKING.md)** | 阅读次序、逐篇理由、AWI/三维/标定等专题路线 |
| **[151 条总索引](INDEX.md)** | 每篇链接到独立卡片，便于在 GitHub 直接阅读 |
| [分类索引](CLASSIFICATION.md) | 按应用、技术、期刊和团队查找 |
| [作者路线](AUTHOR_MAP.md) | Imperial、李玉冰及其他相关团队 |
| [CSV](library.csv) · [BibTeX](references.bib) · [JSON](library.json) | 表格处理、引用管理和结构化数据 |
| [检索方法](SEARCH_METHOD.md) · [候选筛查](screening.csv) | 检索式、范围和 68 项数据库候选的处理结果 |
| [合并说明](MERGE_NOTES.md) · [数据维护](MAINTAINING.md) | 去重规则、证据等级、后续增补方法 |
| [验证结果](VALIDATION.md) | 数据、链接、导出和离线检索检查 |

## 最值得先读的五篇

1. [Ali 等，TMI 2024](papers/UFWI-013.md)：二维环阵声速/衰减的开源基线，有数值、体模与人体示例。
2. [Cueto 等，TUFFC 2022](papers/UFWI-035.md)：Spatial Response Identification，理解仪器校准如何影响反演。
3. [Lucka 等，Inverse Problems 2022](papers/UFWI-025.md)：真三维时域 FWI 的计算、存储与优化设计。
4. [Wu、Li 等，Ultrasonics 2025](papers/UFWI-104.md)：OT 辅助声速/阻抗反演与离体证据。
5. [Ali 等，JASA Express Letters 2025](papers/UFWI-097.md)：frequency differencing，为缺低频数据构造初始化信息。

排序侧重环阵 FWI、三维、AWI 和声源校准中的研究价值；完整理由见[精读排序](READING_RANKING.md)。

## 离线筛选

[下载整个仓库 ZIP](https://github.com/idolwang0314-max/fwi-tutorial-notebook/archive/refs/heads/main.zip)，解压后用浏览器打开 `literature/ultrasound-fwi/index.html`，即可搜索标题、作者、DOI、创新点与技术，按领域、年份、期刊和核验程度筛选。页面自带全部文献数据，不需要安装软件或启动服务。外部论文来源链接需要联网。

GitHub 的 [index.html 文件页](index.html) 显示源码；在线阅读请使用上方 Markdown 索引。离线网页中的详细内容也可直接展开查看。

## 收录与证据

| 范围 | 记录数 |
|---|---:|
| 医学 FWI 相关 | 76 |
| NDT / 工业 / 导波 FWI | 18 |
| 地球物理及可迁移方法 | 27 |
| 相邻超声、学习与硬件 | 30 |

16 条核查了一手全文或相关段落，88 条核查了一手摘要，47 条仍基于历史笔记。143 条为已发表记录，7 条为当前预印本，1 条作者撤回旧预印本仅用于版本追踪，并排除在推荐和 BibTeX 之外。BibTeX 共 149 条，缺少必要作者信息的记录不导出。

这些数字包含会议、书章和相邻方法，不能等同于 151 篇医学 FWI 期刊论文。本库不宣称穷尽全部数据库，也不把摘要核查视为全文精读或独立复现。具体限制见每篇卡片。

维护时编辑 `library.json`，执行 `python literature/ultrasound-fwi/build.py` 和 `python literature/ultrasound-fwi/validate.py`；详见[维护说明](MAINTAINING.md)。

[返回文献目录](../README.md) · [返回 FWI 教程](../../README.md)
