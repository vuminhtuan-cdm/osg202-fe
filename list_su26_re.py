import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Admin\.gemini\antigravity\scratch\osg202\data\OSG202_SU26_RE_HN.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data:
    num = q['order_num']
    content = (q.get('content') or '').strip()
    corr = [o['label'] for o in q.get('question_options', []) if o.get('is_correct')]
    corr_text = [o.get('content') for o in q.get('question_options', []) if o.get('is_correct')]
    print(f"Q{num}: {content[:60]}... -> {corr}: {corr_text}")
