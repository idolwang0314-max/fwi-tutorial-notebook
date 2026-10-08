"""Rebuild the public catalog from library.json. Python 3.10+ standard library only.

Run from any directory: python path/to/build.py
No network access, original research workspace, or scientific software is needed.
The catalog is the editable source; cards, indexes, CSV, BibTeX and HTML are derived.
"""
from pathlib import Path
import csv, json, re, collections

OUT = Path(__file__).resolve().parent
CUTOFF = '2026-10-08'
SCOPE = {'medical_fwi':'医学超声 FWI','ndt_fwi':'超声 NDT / 导波 FWI','geophysical_method':'地球物理及可迁移方法','adjacent_ultrasound':'相邻超声方法 / 硬件','unknown':'待分类'}
V = {'primary_fulltext':'一手全文/相关段落','primary_abstract':'一手摘要','primary_abstract_and_section_preview':'一手摘要/分节预览','metadata_only':'仅书目元数据','legacy_note':'历史笔记，尚未复核结论','unresolved':'待核验'}
def seq(x):
    return x if isinstance(x, list) else ([x] if x else [])
records = json.loads((OUT/'library.json').read_text(encoding='utf-8'))
ids = [r['id'] for r in records]
dois = [r['doi'].lower() for r in records if r.get('doi')]
assert len(ids) == len(set(ids)), 'Duplicate IDs'
assert all(re.fullmatch(r'UFWI-\d{3,}', x) for x in ids), 'Invalid ID'
assert len(dois) == len(set(dois)), 'Duplicate DOIs'
ranks = sorted(r['rank'] for r in records if r.get('rank'))
assert ranks == list(range(1, len(ranks)+1)), 'Noncontinuous ranks'
for r in records:
    assert r['note_path'] == 'papers/' + r['id'] + '.md', 'Unexpected card path'
    assert not (r.get('rank') and r['publication_status']=='withdrawn'), 'Withdrawn ranked record'
records.sort(key=lambda r: (r.get('rank') or 10000, r['priority'], -(r.get('year') or 0), r['title']))
(OUT/'papers').mkdir(exist_ok=True)
for r in records:
 lines=[f"# {r['id']} · {r['title']}",'',f"[总索引](../INDEX.md) · [可筛选网页](../index.html) · [阅读排序](../READING_RANKING.md)",'',f"- 作者：{'; '.join(r.get('authors',[])) or '待核验'}",f"- 年份 / 期刊：{r.get('year') or '待核验'} / {r.get('venue') or '待核验'}",f"- 发表类型 / 状态：{r.get('publication_type')} / {r['publication_status']}",f"- 研究类型：{SCOPE.get(r.get('scope'),r.get('scope'))}",f"- 主题：{'、'.join(r.get('categories',[]))}",f"- 核验程度：{V.get(r.get('verification'),r.get('verification'))}",f"- 优先级：{r['priority']}"+(f"；精读第 {r['rank']} 篇" if r['rank'] else ''),f"- DOI：[{r['doi']}](https://doi.org/{r['doi']})" if r['doi'] else '- DOI：未核验，不补猜。']
 if not r.get('authors_complete'):lines.append('- 作者列表：不完整，引用前请从出版社导出完整书目。')
 if r.get('epmc_publication_date'):lines.append('- Europe PMC日期（可能为卷期日；差异见备注）：'+r['epmc_publication_date'])
 if r.get('publisher_online_date'):lines.append('- 出版社在线日期：'+r['publisher_online_date'])
 for field,label in [('source_record_id','增补来源 ID'),('weekly_class','2026-10-08 分类'),('first_public_date','已记录首次公开日期'),('window_reference_date','本次日期窗判定日'),('date_basis','日期依据'),('event_date','会议活动日期（非首次发表日）'),('submission_timestamp_utc','arXiv 提交 UTC'),('submission_timestamp_beijing','arXiv 提交北京时间')]:
  if field=='source_record_id' and r.get(field)==r['id']:continue
  if field=='weekly_class' and r.get(field)=='existing_not_reviewed':continue
  if r.get(field):lines.append('- '+label+'：'+str(r[field]))
 if r.get('project_reading_rank_20261008'):lines.append('- 2026-10-08 专题阅读：第 '+str(r['project_reading_rank_20261008'])+' 篇，见 [专题顺序](../PROJECT_READING_20261008.md)；不改变历史主榜。')
 if r.get('date_resolution'):lines += ['', '日期冲突处理：', '', '```json', json.dumps(r['date_resolution'],ensure_ascii=False,indent=2), '```']
 if r.get('date_evidence'):lines += ['', '公开来源原始日期字段（冲突时采用上方处理说明）：', '', '```json', json.dumps(r['date_evidence'],ensure_ascii=False,indent=2), '```']
 for field,label in [('review_note_20261004','2026-10-04 复核备注'),('weekly_review_note','2026-10-08 复核备注'),('read_coverage','一手材料阅读范围'),('project_reading_reason_20261008','2026-10-08 专题阅读理由')]:
  if r.get(field):lines += ['',label+'：'+str(r[field])]

 for title,field in [('创新点 / 主要贡献','innovation'),('技术手段','methods'),('验证证据','evidence'),('局限与评估','limitations'),('研究相关性','relevance')]:lines += ['',f'## {title}','',str(r.get(field) or '尚未核验；不根据标题推断。')]
 if r['rank']:lines += ['','## 排序理由','',r['ranking_reason']]
 lines+=['','## 公开来源','']+[f'- [{u}]({u})' for u in r['source_urls']]
 lines+=['',r['notes'],'','核验程度表示本轮查阅证据，不代表已复现实验。局限和研究价值包含整理者评估；不把贡献概括等同于全球首创。']
 (OUT/r['note_path']).write_text('\n'.join(lines)+'\n',encoding='utf-8')
(OUT/'library.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
fields=['id','source_record_id','catalog_added_at','weekly_class','first_public_date','window_reference_date','date_basis','date_timezone','event_date','submission_timestamp_utc','submission_timestamp_beijing','date_resolution','date_evidence','project_reading_rank_20261008','project_reading_reason_20261008','reviewed_at','weekly_review_note','rank','priority','title','year','epmc_publication_date','publisher_online_date','authors','authors_complete','venue','doi','publication_type','publication_status','scope','categories','innovation','methods','evidence','limitations','relevance','verification','ranking_reason','source_urls','notes']
with (OUT/'library.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore',lineterminator='\n');w.writeheader()
 for r in records:w.writerow({k:('; '.join(r.get(k,[])) if isinstance(r.get(k),list) else json.dumps(r[k],ensure_ascii=False) if isinstance(r.get(k),dict) else r.get(k,'')) for k in fields})
def bibtex_escape(s):return str(s).replace('\\','\\textbackslash{}').replace('&','\\&').replace('%','\\%').replace('_','\\_').replace('#','\\#')
def bib_author(s):
 s=str(s).strip()
 if ',' not in s:
  m=re.fullmatch(r"([A-Z][A-Za-zÀ-ÿ'’\-]+(?: [A-Z][a-zÀ-ÿ'’\-]+)*) ([A-Z]{1,4})",s)
  if m:return m[1]+', '+m[2]
 return s
bib=[]
for r in records:
 if r['publication_status']=='withdrawn' or not r.get('year') or not r.get('authors') or r.get('verification')=='unresolved':continue
 typ='article' if r.get('publication_type') in ['journal','review'] else 'inproceedings' if r.get('publication_type')=='conference' else 'incollection' if r.get('publication_type')=='book_chapter' else 'misc'
 authors=[bib_author(a) for a in r['authors'] if not re.search(r'^et\s+al|^others$',a,re.I)]
 f={'title':'{'+r['title']+'}','author':' and '.join(authors)+(' and others' if not r.get('authors_complete') else ''),'year':r['year'],'doi':r['doi'],'url':r.get('url','')}
 if typ=='article':f['journal']=r.get('venue','')
 elif typ=='inproceedings':f['booktitle']=r.get('venue','')
 elif typ=='incollection':f['booktitle']=r.get('venue','').replace(' (book chapter)','')
 bibnotes=[]
 if r.get('publication_type')=='preprint':bibnotes.append('Preprint; peer review not verified')
 if r.get('publication_type')=='conference_presentation':bibnotes.append('Conference presentation; metadata only, slides and research-paper content not reviewed')
 if r.get('publication_status')=='conference_program_and_abstract':bibnotes.append('Official conference program and abstract; proceedings DOI and first-publication date unverified')
 if r.get('publication_status') in ('accepted_manuscript_online','in_press_journal_preproof'):bibnotes.append(r['publication_status'].replace('_',' '))
 if not r.get('authors_complete'):bibnotes.append('Author list incomplete; verify before citation')
 if r.get('verification')=='legacy_note':bibnotes.append('Bibliographic record inherited from earlier research notes; verify before citation')
 if bibnotes:f['note']='; '.join(bibnotes)
 bib.append('@'+typ+'{'+r['id'].replace('-','')+',\n'+',\n'.join('  '+k+' = {'+bibtex_escape(v)+'}' for k,v in f.items() if v)+'\n}')
(OUT/'references.bib').write_text('\n\n'.join(bib)+'\n',encoding='utf-8')
def table_record(r):
 t=r['title'].replace('|','/')
 return f"| {r['id']} | {r['rank'] or '—'} / {r['priority']} | {r.get('year') or '—'} | [{t}]({r['note_path']}) | {r.get('venue','')} | {SCOPE.get(r.get('scope'),r.get('scope'))} | {V.get(r.get('verification'),r.get('verification'))} |"
index=['# 超声 FWI 文献总索引','','[阅读排序](READING_RANKING.md) · [研究综述](REVIEW_CN.md) · [筛选网页](index.html) · [CSV](library.csv) · [BibTeX](references.bib) · [检索口径](SEARCH_METHOD.md) · [合并说明](MERGE_NOTES.md)','',f'截至 {CUTOFF}，去重 {len(records)} 条；包含直接FWI、地球物理方法及明确标记的相邻资料，不等同于同等数量的医学FWI期刊论文。','','| ID | 排序 / 优先级 | 年份 | 题名 / 单篇卡片 | 期刊或来源 | 类型 | 核验 |','|---|---|---|---|---|---|---|']+[table_record(r) for r in records]
(OUT/'INDEX.md').write_text('\n'.join(index)+'\n',encoding='utf-8')
ranked=[r for r in records if r['rank']]
ranklines=['# 最值得精读的论文：排序与阅读路线','','主榜保留 2026-09-26 的 26 篇次序。当前主题阅读另见 [2026-10-08 十二篇专题顺序](PROJECT_READING_20261008.md)，不是主榜重排。','','这是围绕环阵超声FWI、三维重建、AWI和声源校准的阅读优先级，不是影响因子/引用量榜。主榜按相关性、可辨识的技术贡献、实测验证、可复用方法综合人工判断；具体理由逐篇列出，避免给尚未深读的文章伪精确分数。2020年前奠基论文另列；新预印本单列前沿观察。','','| 顺序 | 论文 | 核心贡献 | 为什么排在这里 |','|---|---|---|---|']
for r in ranked:ranklines.append(f"| {r['rank']} | [{r['title']}]({r['note_path']})（{r['year']}，{r['venue']}） | {r['innovation'].replace('|','/')} | {r['ranking_reason']} |")
ranklines+=['','## 分主题阅读顺序','','- AWI / 缺低频：Warner & Guasch 2016 → Guasch 2019 → Pladys 2021 → Yong 2023两篇 → Ali 2025 FDWI → OT/SAWI新工作。','- 真三维与可复现基线：Lucka 2022 → Li 2023 elevation-focused → Ali 2024二维开源 → Ali 2025多行环阵 → Dantuma 2026在体。','- 换能器与实验误差：Cueto 2021/2022 SRI → Wu 2023指向性 → 2026分布式声源 → 在体工作流的联合标定。','- 骨与透颅：Guasch 2020 → Robins 2023 → Li 2023肌骨 → Mitcham 2025离体 → 2026 Rytov / 神经物理预印本。','- 计算与稀疏采样：Lucka 2022 → source encoding / vortex → Louboutin 2023波场压缩 → Mercier 2025联合设计 → Forte 2026 phase encoding。','','## 奠基论文与前沿观察','','奠基论文应先读其基本假设，再对照近期失效案例；前沿观察的预印本不能视为已经独立验证。','']
for r in records:
 if (r.get('year') and r['year']<2020 and r.get('priority_hint',4)<=2) or (r.get('publication_type')=='preprint' and r['publication_status']!='withdrawn'):
  ranklines.append(f"- [{r['title']}]({r['note_path']})（{r.get('year')}，{r.get('publication_type')}）：{r['relevance']}")
(OUT/'READING_RANKING.md').write_text('\n'.join(ranklines)+'\n',encoding='utf-8')
# Compact group indexes are derived from the same records.
by=['# 分类索引','','分类维度彼此独立：应用领域、技术标签、期刊、作者团队、验证证据。相邻成像和预印本不混同于实测FWI。','']
for field,label in [('scope','应用领域'),('venue','期刊 / 来源'),('group','作者 / 团队'),('categories','技术主题')]:
 by += ['## '+label,''];groups=collections.defaultdict(list)
 for r in records:
  for x in seq(r.get(field)):groups[x].append(r)
 for name,rr in sorted(groups.items()):
  by += ['### '+str(SCOPE.get(name,name)), '']+[f"- [{r['id']} · {r['title']}]({r['note_path']})（{r.get('year')}，{r['priority']}）" for r in rr]+['']
(OUT/'CLASSIFICATION.md').write_text('\n'.join(by).rstrip()+'\n',encoding='utf-8')
# Standalone search UI; all content is local and no external JS dependency is used.
data=json.dumps(records,ensure_ascii=False).replace('</','<\\/')
template=(OUT/'viewer_template.html').read_text(encoding='utf-8')
(OUT/'index.html').write_text(template.replace('__DATA__',data).replace('__SCOPE__',json.dumps(SCOPE,ensure_ascii=False)).replace('__VERIFY__',json.dumps(V,ensure_ascii=False)),encoding='utf-8')
stats={'cutoff':CUTOFF,'records':len(records),'ranked':len(ranked),'bibtex':len(bib),'doi_unique':len({r['doi'] for r in records if r['doi']}),'scope':dict(collections.Counter(r.get('scope') for r in records)),'verification':dict(collections.Counter(r.get('verification') for r in records)),'type':dict(collections.Counter(r.get('publication_type') for r in records)),'status':dict(collections.Counter(r['publication_status'] for r in records)),'venue':dict(collections.Counter(r.get('venue') for r in records))}
(OUT/'STATS.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(stats,ensure_ascii=False,indent=2))
