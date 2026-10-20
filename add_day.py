#!/usr/bin/env python3
"""Usage: python3 add_day.py new.json [YYYY-MM-DD]
Theme: workplace + global supply chain vendors (inquiries, quotes, lead times, MOQ, shipping delays, ETA, invoices, reading emails). Include ~3 type:"phrase" items (workplace situation -> most natural sentence; word="phrase:<key>").
new.json = {"questions":[...10 items same schema as questions/2026-10-21.json...]}
Validates: 10 questions, 4 options, answer 0-3, no word reused from earlier days. Writes questions/DATE.json and updates manifest.json.
`python3 add_day.py --used` prints all used words."""
import json,sys,os,datetime
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),'questions')
m=json.load(open(f'{D}/manifest.json'))
used={q['word'].lower() for d in m['days'] for q in json.load(open(f'{D}/{d}.json'))['questions']}
if sys.argv[1]=='--used': print('\n'.join(sorted(used))); sys.exit()
date=sys.argv[2] if len(sys.argv)>2 else datetime.date.today().isoformat()
qs=json.load(open(sys.argv[1]))['questions']
assert len(qs)==10,'need 10'
for q in qs:
    assert len(q['options'])==4 and 0<=q['answer']<=3, q
    assert q['word'].lower() not in used, 'repeat: '+q['word']
    q.setdefault('id',q['word'])
json.dump({'date':date,'questions':qs},open(f'{D}/{date}.json','w'),ensure_ascii=False,indent=1)
if date not in m['days']: m['days'].append(date); m['days'].sort()
json.dump(m,open(f'{D}/manifest.json','w'))
print('added',date)
