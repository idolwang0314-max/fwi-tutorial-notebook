# 检索口径与覆盖边界

检索日：2026-09-26。目标是尽可能广覆盖、可追溯的研究型文献库，**不是已满足PRISMA的系统综述，也不宣称收全全球全部文章**。

## 范围

主时间窗2020-01-01至2026-09-26公开的研究；旧文献和关键奠基工作不因早于2020而删除。发表年份优先正式卷期年，最早在线和预印本日期分开；2027卷期108280已于2026-08-20在线公开，因此入窗且明确标2027。

重点期刊Ultrasonics、TUFFC/TUSON、Geophysics；拓展OJUFFC、TMI、UMB、JASA、PMB、Inverse Problems、Chinese Physics B、GJI、Medical Physics等。作者按Imperial及李玉冰官方机构资料、共同作者和引文追踪。

## 实际检索渠道

1. 公开Web搜索：论文精确标题、期刊+FWI、作者+ultrasound，查出版社、作者机构、作者稿与arXiv。
2. 公开Europe PMC API，题名/摘要查询，resultType=core，pageSize=1000；一次获得68项（未超过页大小）。检索式列于下方，全部候选及去向保存在[筛查表](screening.csv)。
3. Crossref官方公开API核对部分DOI、题名、作者、日期和出版社登记摘要；DOI存在不等于方法已验证。
4. 历史清单/笔记与82份论文PDF前1–2页核查，以及三维加速、创新审计报告的引用索引。

数据库检索式：

```text
((TITLE_ABS:"full waveform inversion") OR (TITLE_ABS:"full-waveform inversion"))
AND ((TITLE_ABS:ultrasound) OR (TITLE_ABS:ultrasonic) OR (JOURNAL_NAME:Ultrasonics))
AND FIRST_PDATE:[2020-01-01 TO 2026-09-26]
```

补充关键词：full-waveform / full waveform / full wave inversion；USCT / UST / breast / brain / bone / musculoskeletal / guided wave / NDT；adaptive / localized / optimal transport / frequency difference / source encoding / directivity / spatial response / attenuation / 3D / neural operator；Yubing Li / Yu-Bing Li / 李玉冰；Guasch / Warner / Cueto / Robins / Bates。

## 去重与筛查

- DOI转小写并去doi.org前缀；无DOI只对规范化相同题名合并，禁止按相似技术词混并。
- 相同DOI保留新的一手核验内容，并合并公开来源；原始材料定位信息仅用于整理过程。不同DOI的会议/期刊建立版本关系，不当作重复实验的独立证据。
- 68项公共查询结果全部在[筛查表](screening.csv)：{'included': 64, 'version_link': 2, 'excluded_scope': 2}。包括GraphNN预印本→正式期刊、Learned2023预印本→TCI2024两个版本关联；两条范围外结果也保留筛除记录。
- 未公开材料和非论文资产不进入正式发表论文排名；候选引用在完成书目及内容核验前不计入151条正式记录。

## 证据与排序

本轮一手全文/相关段落16条，一手摘要88条，旧笔记47条。摘要数据和作者结论均以“作者报告”理解，未做数值复现。局限、相关性与阅读优先级是整理者综合评估。

主榜26篇采用人工可解释顺序：与环阵FWI、三维、AWI及校准研究的相关性、技术贡献可辨识性、验证强度、实现/数据可复用性共同决定；不使用无法校准的影响分数。P0是主榜；P1重要补读；P2专题扩展；P3未核验状态或已撤回历史。

## 未覆盖与限制

未登录Web of Science、Scopus或付费IEEE/Elsevier全文账户；不含完整订阅数据库引文导出，不批量下载PDF。部分出版社页面403/访问失败，改用作者机构、PMC全文或出版社提供的原始摘要。书目不全或只读摘要均在单篇中标明。公开检索可能漏掉未收录、非英文、仅录用未公开和标题未出现FWI的工作，因此“搜索所有”只能作为覆盖目标而非已达成的穷尽结论。

公开版合并与证据说明见 [MERGE_NOTES.md](MERGE_NOTES.md)。
