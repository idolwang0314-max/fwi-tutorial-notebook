"""Validate the public catalog; no network or scientific computation required."""
from pathlib import Path
import collections
import csv
import json
import re
import shutil
import subprocess
import tempfile
from urllib.parse import unquote, urlparse

OUT = Path(__file__).resolve().parent
rows = json.loads((OUT / 'library.json').read_text(encoding='utf-8'))
errors, warnings = [], []


def check(condition, message):
    if not condition:
        errors.append(message)


ids = {r['id'] for r in rows}
dois = [r['doi'].lower() for r in rows if r.get('doi')]
check(len(ids) == len(rows), 'Duplicate IDs')
check(len(dois) == len(set(dois)), 'Duplicate DOIs')
required = ('id title authors authors_complete year venue doi scope publication_type '
            'publication_status innovation methods evidence limitations relevance '
            'verification source_urls priority rank ranking_reason note_path').split()
for r in rows:
    for key in required:
        check(key in r, f'{r["id"]}: missing {key}')
    for key in ['title', 'innovation', 'methods', 'evidence', 'limitations', 'relevance']:
        check(bool(r.get(key)), f'{r["id"]}: empty {key}')
    check(re.fullmatch(r'UFWI-\d{3,}', r['id']), f'{r["id"]}: invalid ID')
    check(r['note_path'] == 'papers/' + r['id'] + '.md', f'{r["id"]}: invalid card path')
    check((OUT / r['note_path']).exists(), f'{r["id"]}: missing card')
    check(r['priority'] in ['P0', 'P1', 'P2', 'P3'], f'{r["id"]}: invalid priority')
    check(bool(r.get('rank')) == (r['priority'] == 'P0'), f'{r["id"]}: rank/P0 mismatch')
    if r.get('doi'):
        check(re.fullmatch(r'10\.\d{4,9}/\S+', r['doi']), f'{r["id"]}: invalid DOI')
    for url in [r.get('url', '')] + r.get('source_urls', []):
        if url:
            parsed = urlparse(url)
            check(parsed.scheme in ['https', 'http'] and bool(parsed.netloc),
                  f'{r["id"]}: nonpublic source URL')
    if r.get('rank'):
        check(r['verification'].startswith('primary_'), f'{r["id"]}: ranked without primary evidence')
        check(bool(r['ranking_reason']), f'{r["id"]}: missing ranking reason')
        check(r['publication_status'] != 'withdrawn', f'{r["id"]}: withdrawn ranked entry')

rank = sorted(r['rank'] for r in rows if r.get('rank'))
check(rank == list(range(1, len(rank) + 1)), 'Noncontinuous ranks')
with (OUT / 'library.csv').open(encoding='utf-8-sig', newline='') as f:
    csv_rows = list(csv.DictReader(f))
check(len(csv_rows) == len(rows), 'CSV row count')
check([r['id'] for r in csv_rows] == [r['id'] for r in rows], 'CSV ID order')
index = (OUT / 'INDEX.md').read_text(encoding='utf-8')
for r in rows:
    check(r['note_path'] in index, f'{r["id"]}: not in total index')
cards = {p.stem for p in (OUT / 'papers').glob('*.md')}
check(cards == ids, 'Missing or orphan paper cards')

# Check repository-relative links, never fetch external URLs during validation.
for p in OUT.rglob('*.md'):
    for link in re.findall(r'\]\(([^\n]+?)\)', p.read_text(encoding='utf-8')):
        if link.startswith(('https:', 'http:', '#', 'mailto:')):
            continue
        link = unquote(link.strip('<>').split('#')[0])
        check(not Path(link).is_absolute(), f'{p.name}: absolute file link')
        target = p.parent / link
        # This report is created at the end of this command, including on first run.
        pending_report = target.resolve() == (OUT / 'VALIDATION.md').resolve()
        check(target.exists() or pending_report, f'{p.name}: broken link {link}')

private_keys = {'local_paths', 'origin_roles', 'provenance_records'}
for r in rows:
    check(not (private_keys & r.keys()), f'{r["id"]}: internal provenance field')
private_path = re.compile(r'/(?:cpfs\d*|home|root)/|(?:\.plans|codex_handoffs)/|file://')
for p in OUT.rglob('*'):
    if p.is_file() and p.suffix in ['.md', '.json', '.csv', '.html', '.bib']:
        check(not private_path.search(p.read_text(encoding='utf-8-sig')),
              f'{p.relative_to(OUT)}: internal path')

bib = (OUT / 'references.bib').read_text(encoding='utf-8')
keys = re.findall(r'@\w+\{([^,]+),', bib)
check(len(keys) == len(set(keys)), 'Duplicate BibTeX keys')
check(bib.count('{') == bib.count('}'), 'Unbalanced BibTeX braces')
for r in rows:
    key = r['id'].replace('-', '')
    eligible = (r['publication_status'] != 'withdrawn' and r.get('year')
                and r.get('authors') and r['verification'] != 'unresolved')
    check((key in keys) == bool(eligible), f'{r["id"]}: BibTeX inclusion mismatch')
    if key in keys and not r['authors_complete']:
        entry = re.search(r'@\w+\{' + key + r',([\s\S]*?)(?=\n@|\Z)', bib).group(1)
        check('and others' in entry and 'Author list incomplete' in entry,
              f'{r["id"]}: partial authors not marked')
    if key in keys and r['publication_type'] == 'book_chapter':
        check('@incollection{' + key in bib, f'{r["id"]}: incorrect chapter type')

screen = json.loads((OUT / 'screening.json').read_text(encoding='utf-8'))
check(len(screen) == 68, 'Initial screening snapshot count differs from 68')
for record in screen:
    if record.get('library_id'):
        check(record['library_id'] in ids, 'Screening refers to missing catalog record')

page = (OUT / 'index.html').read_text(encoding='utf-8')
script = re.findall(r'<script>([\s\S]*?)</script>', page)[0]
embedded = re.search(r'const records=(.*?), scopes=', script).group(1)
check(json.loads(embedded) == rows, 'HTML embedded data differs from catalog')
for href in re.findall(r'href="([^"]+)"', page):
    if not href.startswith(('https:', 'http:', '#')):
        check((OUT / href).exists(), f'HTML broken link: {href}')
stats = json.loads((OUT / 'STATS.json').read_text(encoding='utf-8'))
for key, expected in [('records', len(rows)), ('ranked', len(rank)), ('bibtex', len(keys))]:
    check(stats[key] == expected, f'STATS mismatch: {key}')
for key, field in [('scope', 'scope'), ('verification', 'verification'), ('status', 'publication_status')]:
    check(stats[key] == dict(collections.Counter(r[field] for r in rows)), f'STATS mismatch: {key}')

js_smoke = None
if shutil.which('node'):
    harness = r'''
const fs=require('fs'),vm=require('vm');
class Elem{constructor(tag){this.tag=tag;this.children=[];this.value='';this.textContent=''}append(...a){for(const x of a){if(x.tag==='fragment')this.children.push(...x.children);else this.children.push(x)}}replaceChildren(...a){this.children=[];this.append(...a)}addEventListener(){}}
let ids={};for(const k of ['q','scope','venue','year','verify','sort','reset','cards','count'])ids[k]=new Elem(k);ids.sort.value='priority';
let ctx={document:{getElementById:x=>ids[x],createElement:x=>new Elem(x),createDocumentFragment:()=>new Elem('fragment')}};vm.createContext(ctx);vm.runInContext(fs.readFileSync(process.argv[2],'utf8'),ctx);
const expected=vm.runInContext('records.length',ctx);if(ids.cards.children.length!==expected)throw Error('Initial render count');
ids.q.value='adaptive';vm.runInContext('render()',ctx);if(ids.cards.children.length<1||ids.cards.children.length>=expected)throw Error('Search filter');
ids.q.value='';ids.scope.value='geophysical_method';vm.runInContext('render()',ctx);let n=vm.runInContext('records.filter(x=>x.scope==="geophysical_method").length',ctx);if(ids.cards.children.length!==n)throw Error('Scope filter');
ids.reset.onclick();if(ids.cards.children.length!==expected)throw Error('Reset');
ids.q.value='2312.15575';vm.runInContext('render()',ctx);let linked=vm.runInContext('records.filter(r=>JSON.stringify(r).toLowerCase().includes("2312.15575")).length',ctx);if(ids.cards.children.length!==linked||linked<1)throw Error('Withdrawn/version search');
console.log(JSON.stringify({initial:expected,geophysical:n,search:true,reset:true,withdrawn:true}));
'''
    with tempfile.TemporaryDirectory(prefix='public_fwi_check_') as td:
        js = Path(td) / 'viewer.js'
        js.write_text(script, encoding='utf-8')
        result = subprocess.run(['node', '--check', str(js)], capture_output=True, text=True)
        check(result.returncode == 0, 'JavaScript syntax: ' + result.stderr)
        test = Path(td) / 'smoke.js'
        test.write_text(harness, encoding='utf-8')
        result = subprocess.run(['node', str(test), str(js)], capture_output=True, text=True)
        check(result.returncode == 0, 'JavaScript smoke: ' + result.stderr)
        if result.returncode == 0:
            js_smoke = json.loads(result.stdout)
else:
    warnings.append('Node.js unavailable; JavaScript syntax and DOM smoke checks skipped.')

result = dict(records=len(rows), csv_rows=len(csv_rows), unique_doi=len(dois),
              ranked=len(rank), bibtex_entries=len(keys), screened=len(screen),
              checks_passed=not errors, errors=errors, warnings=warnings, js_smoke=js_smoke)
(OUT / 'validation.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
report = ['# 公开文献库验证结果', '', f'结果：{"PASS" if not errors else "FAIL"}。', '',
          f'- 文献 {len(rows)} 条；唯一非空 DOI {len(dois)}；主榜 {len(rank)}；BibTeX {len(keys)} 条。',
          '- JSON/CSV/HTML 数据一致，必填字段、ID/DOI、排名和优先级、单篇卡片和索引通过检查。',
          '- 生成 Markdown 与 HTML 相对链接、公开来源 URL 格式及内部路径检查。',
          '- BibTeX 键、基础括号、部分作者提示、书章类型与撤回排除规则检查。',
          '- 68 项初版筛查快照及统计文件检查。',
          '- 本检查不联网核验 URL 存活，不等于重新核验文献结论；未使用 TeX 编译器或完整 BibTeX 解析器。', '',
          '## 网页检查', '',
          'Node.js 语法与最小 DOM 接口检查通过：检索、领域筛选、重置及撤回版本检索。' if js_smoke else 'JavaScript 检查未通过或未执行，详见下方结果。',
          '此项不等于真实浏览器视觉验收。', '', '```json', json.dumps(result, ensure_ascii=False, indent=2), '```', '',
          '没有运行 PDE/GPU 实验，没有安装依赖。']
(OUT / 'VALIDATION.md').write_text('\n'.join(report) + '\n', encoding='utf-8')
print(json.dumps(result, ensure_ascii=False, indent=2))
raise SystemExit(bool(errors))
