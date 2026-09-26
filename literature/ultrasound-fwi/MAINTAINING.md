# 数据维护与重建

`library.json` 是唯一文献数据源。`build.py` 使用 Python 3.10+ 标准库，不联网，也不依赖原始研究工作区、PDF、GPU 或科学计算包。

从仓库根目录运行：

```bash
python literature/ultrasound-fwi/build.py
python literature/ultrasound-fwi/validate.py
```

`validate.py` 用标准库检查数据与相对链接。如果系统有 Node.js，还会检查网页脚本语法，并用最小 DOM 接口验证检索、筛选和重置；未安装 Node.js 时明确记录跳过该项。它不运行 FWI 教程或科学实验。

## 文件职责

| 文件 | 维护方式 |
|---|---|
| `library.json` | 手工核验和编辑的主数据 |
| `viewer_template.html` | 离线浏览器样式和交互模板 |
| `REVIEW_CN.md`、`AUTHOR_MAP.md`、`SEARCH_METHOD.md`、`MERGE_NOTES.md`、`README.md` | 人工综合报告；更新数据后同步数字和结论 |
| `screening.json`、`screening.csv` | 初版数据库检索的候选审计快照 |
| `papers/`、`INDEX.md`、`READING_RANKING.md`、`CLASSIFICATION.md` | `build.py` 生成 |
| `library.csv`、`references.bib`、`index.html`、`STATS.json` | `build.py` 生成 |
| `validation.json`、`VALIDATION.md` | `validate.py` 生成 |

生成脚本更新文件，不自动删除旧卡片；移除文献应有明确理由，并自行处理相应卡片及报告链接。验证脚本会报告孤立卡片。

## 每条记录

必须保留稳定 `id`，并令 `note_path` 为 `papers/<id>.md`。新增 ID 使用现存最大数字加一，已有编号间隔不补占。不要因改名或阅读次序变化重编号。

主要字段：

| 字段 | 内容 |
|---|---|
| `title`、`authors`、`authors_complete`、`year`、`venue`、`doi`、`url` | 书目与原文地址；未知值不猜测 |
| `publication_type`、`publication_status` | 论文类型；已发表、预印本、撤回或未核验状态 |
| `scope`、`categories`、`group` | 应用领域、技术标签与作者路线 |
| `innovation`、`methods` | 主要贡献与技术手段 |
| `evidence`、`limitations`、`relevance` | 验证数据、局限和研究价值 |
| `verification`、`verified_at`、`source_urls`、`notes` | 内容核验程度、日期、公开证据与备注 |
| `rank`、`ranking_reason`、`priority` | 主榜顺序及理由；未入榜 `rank` 为 `null` |
| `epmc_publication_date`、`publisher_online_date` | 可选日期；与卷期年份分别记录 |

领域为 `medical_fwi`、`ndt_fwi`、`geophysical_method`、`adjacent_ultrasound`；内容证据等级见[合并说明](MERGE_NOTES.md)。日期使用 `YYYY-MM-DD`。

主榜保持从 1 开始连续编号，均应有一手证据和具体排序理由。P0 为主榜，P1 为重要参考，P2 为专题扩展，P3 为未核验/撤回历史。撤回版本不得进入主榜或 BibTeX。

## 更新流程

1. 根据 DOI 检查重复；无 DOI 时核对准确题名、作者及版本关系。
2. 查看公开一手来源，填入贡献、方法和验证层级；只读摘要就注明摘要，不推测全文参数。
3. 更新主数据、来源和核验日期，必要时调整人工排序及综合报告。
4. 运行构建与验证，检查 `git diff`，将主数据与派生文件一起提交。

初版检索截止日为 2026-09-26。扩大时间窗时同步 `build.py`、网页模板及报告中的截止日期；`screening.*` 保留其原始快照语义，新增检索另存有日期的筛查记录。
