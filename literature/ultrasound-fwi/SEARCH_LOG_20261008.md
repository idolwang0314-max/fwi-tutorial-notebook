# 检索日志

日期：2026-10-08。周窗：北京时间10/2—10/8；期刊只有日期而无时刻时保留出版商源日期，不凭空转换。本次采用有界公开检索，没有批量下载论文。

## 基库和去重

基库为截至 2026-10-04 整理的 155 条记录。按 DOI 去前缀/小写比对，再核对题名变体、arXiv 编号和 conference paper_id。Radon 2019、PACS 2026、ggag376、OpenBreastUS 均未匹配既有条目。原始来源 ID 与公开 ID 的对应见 [ID_MAP_20261008.json](ID_MAP_20261008.json)。

## 可复核检索路径

1. 网页检索：ultrasound/full waveform inversion + October/Oct2026；Yubing Li/Guasch/Meng-Xing Tang + 2026；Radon matching；shot-dependent model extension。后按出版社/作者机构原始摘要核验，二手命中只作线索。
2. EuropePMC REST core：`(TITLE_ABS:"full waveform inversion" OR TITLE_ABS:"full-waveform inversion" OR TITLE_ABS:"ultrasound computed tomography") AND FIRST_PDATE:[2026-10-02 TO 2026-10-08]`，0条；同query的FIRST_IDATE窗返回3条，DOA-UCT实际电子10/1，另两条临床多模态词组误匹配已排除。PMID42825011 core元数据确认DOI/作者/摘要/日期。
3. Crossref works：filter=`from-online-pub-date:2026-10-02,until-online-pub-date:2026-10-08`，query=`full waveform inversion`，rows100（总匹配171，并非171篇FWI）；标题/作者摘要筛选到3条直接相关（eDWI/Q-FWI/upper-mantle），后者方法迁移关联低排除。另query=`ultrasound tomography`宽检索噪声多；重试遇429，不反复高频抓取，不声称完成全库分页。GJI ggag418/406通过出版商网页补出，说明关键词题名检索不能独立穷尽。
4. Crossref逐刊相同online-date窗，ISSN0041-624X、3066-9464、0885-3010、0926-9851均返回0（Ultrasonics/TUSON/TUFFC/JAG）。不把online字段缺失或索引迟到当作无新文章证明。
5. arXiv API：`(all:"full waveform inversion" OR all:"full-waveform inversion" OR all:"ultrasound tomography") AND lastUpdatedDate:[202610010000 TO 202610082359]`；额外扩一天供北京时间边界判别，max_results100，共5条：REG、Forte3D、C2Fhash、PG-VAE、GeoFWI3D。已全部给去向；精确版本史也核查Li团队3个已有arXiv编号和OpenBreastUS。
6. IUS2026官网session141/146/159/110/65/68/69/32/87及session_index；官方paper_details读作者摘要；官方search_paper.php只读POST检索Title contains waveform inversion/inversion及ID，分别返回9/13命中。没有登录或保存个人schedule。author/session缓存发生变化，7143采用当前7作者；7164当前目录缺失，隔离。初次公开时间未知，仅记录10/5—10/7program日期。
7. 全文有界深核：PACS经EuropePMC fullTextXML阅读方法Eq13、Fig2及实验；Forte3D arXiv HTML阅读频率/网格/计算时长/实验；GJI综述读相关model/source/receiver extension部分。其余按作者摘要级，不冒称全文精读。

## 来源和失败说明

主要源：ScienceDirect/Elsevier、OUP、Crossref出版商提交元数据、EuropePMC作者摘要、arXiv及API、IEEE IUS官方epapers2、KAUST/Dundee作者机构。PubMed网页偶有简化空响应，改用EuropePMC；OUP/DOI部分访问错误，使用同出版商可访问URL或Crossref原始abstract。未以ResearchGate、JoVE、新闻、搜索抓取日期支持技术或发表日期。会议列表可能更新，检索日状态单独记录。

Crossref/EuropePMC/arXiv结构化查询URL、返回数和命名候选去向保存在[SEARCH_EVENTS_20261008.json](SEARCH_EVENTS_20261008.json)；未保存全文大段拷贝、会议登录信息或任何凭据。

## 历史机制定向补漏

沿Marty/Fichtner作者主页、ETH机构库、SPIE/IEEE DOI元数据、作者上传全文，查核2021声弹FWI、2022弹性FWI+OT、2024离体骨表征、2025OT会议报告、2026颅骨物理消融。另以arXiv原文核Symes2024理论稿及其2025不同数值论文关系；将SAWI/MDWI/Guasch旧全文笔记重新对照primary段落。结果6条历史新增、3条已有更正；证据类型逐卡保留，未全库重审。
