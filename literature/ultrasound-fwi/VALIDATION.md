# 公开文献库验证结果

结果：PASS。

- 文献 179 条；唯一非空 DOI 166；主榜 26；BibTeX 177 条。
- JSON/CSV/HTML 数据一致，必填字段、ID/DOI、排名和优先级、单篇卡片和索引通过检查。
- 生成 Markdown 与 HTML 相对链接、公开来源 URL 格式及内部路径检查。
- BibTeX 键、基础括号、部分作者提示、书章类型与撤回排除规则检查。
- 68 项初版筛查快照、179 条来源 ID 映射、12 篇专题顺序及统计文件检查。
- 本检查不联网核验 URL 存活，不等于重新核验文献结论；未使用 TeX 编译器或完整 BibTeX 解析器。

## 网页检查

Node.js 语法与最小 DOM 接口检查通过：检索、领域筛选、重置及撤回版本检索。
此项不等于真实浏览器视觉验收。

```json
{
  "records": 179,
  "csv_rows": 179,
  "unique_doi": 166,
  "ranked": 26,
  "bibtex_entries": 177,
  "screened": 68,
  "source_ids": 179,
  "project_ranked": 12,
  "checks_passed": true,
  "errors": [],
  "warnings": [],
  "js_smoke": {
    "initial": 179,
    "geophysical": 39,
    "search": true,
    "reset": true,
    "withdrawn": true
  }
}
```

没有运行 PDE/GPU 实验，没有安装依赖。
