"""Dependency-free checks for this distribution, not a scholarly evaluator."""
from pathlib import Path
import hashlib, json, re

ROOT=Path(__file__).resolve().parents[1]
SKILL=ROOT/'jmps-conclusion'
errors=[]
def check(condition,message):
    if not condition:errors.append(message)

text=(SKILL/'SKILL.md').read_text(encoding='utf8')
parts=text.split('---',2)
check(len(parts)==3 and not parts[0].strip(),'frontmatter delimiters')
# The entrypoint uses a deliberately small YAML subset: scalar fields plus metadata.
# This is a restricted validator for these files, not a general YAML implementation.
fm=parts[1] if len(parts)==3 else ''
check(re.search(r'^name: jmps-conclusion$',fm,re.M),'skill name')
description=re.search(r'^description: (.+)$',fm,re.M)
check(description is not None and len(description.group(1))<=1024,'description')
check(all(not line or re.match(r'^(?:name|description|metadata):|^  short-description:',line) for line in fm.splitlines()),'unsupported frontmatter field')
for p in SKILL.rglob('*.md'):
    s=p.read_text(encoding='utf8')
    for target in re.findall(r'\]\(([^)]+)\)',s):
        if not re.match(r'https?://',target):check((p.parent/target.split('#')[0]).is_file(),f'broken link {p.name}: {target}')
    check('[TODO:' not in s,f'unfinished scaffold {p.name}')
for p in ROOT.rglob('*'):
    if not p.is_file() or '.git' in p.parts:continue
    check(p.suffix.lower() not in {'.pdf','.docx','.xml','.tex','.sqlite','.env','.pem','.key'},f'undistributable file {p.relative_to(ROOT)}')
    if p.suffix in {'.md','.json','.jsonl','.py','.yaml','.yml','.txt'}:
        s=p.read_text(encoding='utf8')
        check(not re.search(r'(?<![A-Za-z])[A-Za-z]:[\\/](?!/)',s),f'absolute Windows path {p.relative_to(ROOT)}')
        check(not re.search(r'(?:gh[pousr]_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{24,})',s),f'credential pattern {p.relative_to(ROOT)}')
corpora={}
for name in ['jmps','nature','other']:
    p=ROOT/'evidence'/f'{name}.jsonl'
    check(p.is_file(),f'missing corpus {name}')
    if p.is_file():
        rows=[json.loads(line) for line in p.read_text(encoding='utf8').splitlines() if line.strip()]
        corpora[name]=rows
        check(len(rows)==60,f'{name} must have 60 distinct records')
        check(len({r['doi'].lower() for r in rows})==60,f'{name} duplicate DOI')
        check(sum(r['split']=='learn' for r in rows)==48,f'{name} original frozen split')
all_dois=[r['doi'].lower() for rows in corpora.values() for r in rows]
supplement=ROOT/'evidence/jmps_highcite_supplement.jsonl'
supplement_count=0
extra=[]
check(supplement.is_file(),'missing JMPS high-citation supplement')
if supplement.exists():
    extra=[json.loads(line) for line in supplement.read_text(encoding='utf8').splitlines() if line.strip()]
    supplement_count=len(extra)
    check(len(extra)==25,'high-citation supplement must contain25 records')
    check(sum(r['split']=='learn' for r in extra)==20,'supplement frozen split20/5')
    check(all(r['citation_count']>=100 for r in extra),'supplement citation threshold')
    check(sum(r['citation_count']>=100 for r in corpora['jmps'])+sum(r['citation_count']>=100 for r in extra)==60,'JMPS high-citation subset must contain60 records')
    all_dois += [r['doi'].lower() for r in extra]
check(len(set(all_dois))==len(all_dois),'duplicate DOI across strata')
language_counts={}
for group in ['jmps','nature','other']:
    p=ROOT/'evidence'/f'sentence_language_{group}.jsonl'
    check(p.is_file(),f'missing sentence language evidence: {group}')
    if not p.is_file():continue
    rows=[json.loads(line) for line in p.read_text(encoding='utf8').splitlines() if line.strip()]
    language_counts[group]=len(rows)
    allowed={r['sample_id']:r['doi'].lower() for r in corpora[group] if r['split']=='learn'}
    if group=='jmps':allowed.update({r['sample_id']:r['doi'].lower() for r in extra if r['split']=='learn'})
    ids=[r.get('sample_id',r.get('id')) for r in rows]
    check(len(ids)==len(set(ids))==len(allowed),f'{group} language ID coverage and uniqueness')
    check(all(i in allowed and r['doi'].lower()==allowed[i] for i,r in zip(ids,rows)),f'{group} language DOI/learning split')
    if group=='nature':check(next(r for r in rows if r['id']=='N19')['aggregation_role'].startswith('context_only'),'N19 must remain context only')
    if group=='other':check(next(r for r in rows if r['id']=='O25')['aggregation_role']=='review_comparator_only','O25 must remain review comparator')
inventory={str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts and p.name not in {'MANIFEST.json','STRUCTURE_CHECK.json'}}
official_path=ROOT/'evidence/SKILL_CREATOR_CHECK.json'
official=json.loads(official_path.read_text(encoding='utf8')) if official_path.exists() else {'passed':False,'message':'not recorded'}
result={'passed':not errors,'errors':errors,'corpus_records':{k:len(v) for k,v in corpora.items()},'additional_jmps_high_citation_records':supplement_count,'total_unique_records':len(set(all_dois)),'language_window_records':language_counts,'scope':'restricted frontmatter, links, corpus uniqueness, language IDs/splits and distribution scan; no proof of scholarly correctness','bundled_quick_validate':official,'files':inventory}
(ROOT/'evidence/STRUCTURE_CHECK.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
print(json.dumps({k:v for k,v in result.items() if k!='files'},ensure_ascii=False,indent=2))
raise SystemExit(0 if not errors else 1)
