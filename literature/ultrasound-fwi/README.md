# 超声 FWI 文献库 · Ultrasound FWI literature library

**179 条文献记录，保留 26 篇历史精读排序，新增 12 篇专题阅读顺序；逐篇提供创新点、技术手段、验证证据、局限和公开来源。**

合并历史多智能体文献调研与截至 **2026-10-08** 的公开检索，重点为 **Ultrasonics、IEEE TUFFC/TUSON、Geophysics/GJI**，并追踪 **Imperial College** 和 **李玉冰（Yubing Li）** 等作者路线。主要覆盖 2020—2026 年，保留关键奠基论文。一条 2027 卷期记录已于 2026 在线公开，书目年与在线日期分别记录。

本次相对上一公开版新增 28 条：10 月 4 日补漏 4 条，10 月 8 日新增 24 条。已有 ID 和历史主榜保持稳定；会议活动日、期刊上线日与预印本提交日分别标记。原 68 项候选筛查保留为初版快照，新检索见 [本次日志](SEARCH_LOG_20261008.md)。

## 从这里开始

| 入口 | 内容 |
|---|---|
| **[研究综述](REVIEW_CN.md)** | 前沿技术路线、值得追踪的进展与评价边界 |
| **[26 篇历史主榜](READING_RANKING.md)** | 保留 2026-09-26 的阅读次序和理由 |
| **[本次 12 篇专题阅读](PROJECT_READING_20261008.md)** | 几何、源校准、Radon matching、AWI 和三维计算 |
| **[2026-10-08 周综述](WEEKLY_REVIEW_CN.md)** | 24 条本次新收录、9 条旧文复核与时间边界 |
| **[179 条总索引](INDEX.md)** | 每篇链接到独立卡片，便于在 GitHub 直接阅读 |
| [分类索引](CLASSIFICATION.md) | 按应用、技术、期刊和团队查找 |
| [作者路线](AUTHOR_MAP.md) | Imperial、李玉冰及其他相关团队 |
| [CSV](library.csv) · [BibTeX](references.bib) · [JSON](library.json) | 表格处理、引用管理和结构化数据 |
| [检索方法](SEARCH_METHOD.md) · [候选筛查](screening.csv) | 检索式、范围和 68 项数据库候选的处理结果 |
| [合并说明](MERGE_NOTES.md) · [本次增补](CHANGELOG_20261008.md) · [ID 映射](ID_MAP_20261008.json) | 去重、证据等级与稳定编号 |
| [数据维护](MAINTAINING.md) · [本次审核](REVIEW_20261008.md) | 构建方法与已采纳日期纠错 |
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
| 医学 FWI 相关 | 87 |
| NDT / 工业 / 导波 FWI | 19 |
| 地球物理及可迁移方法 | 39 |
| 相邻超声、学习与硬件 | 34 |

19 条核查了一手全文或相关段落，112 条核查了一手摘要，1 条核查摘要与分节预览，47 条仍基于历史笔记。状态分别保留 148 条 published、4 条 published_online、1 条 accepted manuscript、1 条 journal preproof、12 条当前预印本、12 条本周会议日程/摘要，以及 1 条作者撤回旧预印本。撤回版本只作版本追踪，并排除推荐与 BibTeX；BibTeX 共 177 条，缺少必要作者信息的记录不导出。

这些数字包含会议、书章和相邻方法，不能等同于 179 篇医学 FWI 期刊论文。本库不宣称穷尽全部数据库，也不把摘要核查视为全文精读或独立复现。具体限制见每篇卡片。

维护时编辑 `library.json`，执行 `python literature/ultrasound-fwi/build.py` 和 `python literature/ultrasound-fwi/validate.py`；详见[维护说明](MAINTAINING.md)。

[返回文献目录](../README.md) · [返回 FWI 教程](../../README.md)
