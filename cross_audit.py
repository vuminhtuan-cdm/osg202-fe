import json
import glob
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r'C:\Users\Admin\.gemini\antigravity\scratch\osg202\data'

# Load all exams
exams = {}
for f in glob.glob(f'{base_dir}\\*.json'):
    fname = f.split('\\')[-1]
    with open(f, 'r', encoding='utf-8') as fp:
        exams[fname] = json.load(fp)

print("Loaded exams:", list(exams.keys()))

# Check text questions across SU26_RE_HN, SU26_FE_HN, FA25_RE
text_exams = ['OSG202_SU26_RE_HN.json', 'OSG202_SU26_FE_HN.json', 'OSG202_FA25_RE.json']

# Find similar/overlapping questions
all_text_qs = []
for ex_name in text_exams:
    for q in exams[ex_name]:
        content = q.get('content') or ''
        # normalize
        norm = re.sub(r'\(choose\s+\d+\s+answers?\)', '', content, flags=re.IGNORECASE)
        norm = re.sub(r'[^a-zA-Z0-9]', '', norm).lower()[:60]
        if norm:
            all_text_qs.append((ex_name, q['order_num'], norm, q))

from collections import defaultdict
grouped = defaultdict(list)
for ex_name, qnum, norm, q in all_text_qs:
    grouped[norm].append((ex_name, qnum, q))

print(f"\nTotal unique question signatures: {len(grouped)}")
overlap_count = 0
for norm, occurrences in grouped.items():
    if len(occurrences) > 1:
        overlap_count += 1
        print(f"\n--- Overlapping Question ({len(occurrences)} exams) ---")
        for ex_name, qnum, q in occurrences:
            corr = [o['label'] for o in q.get('question_options', []) if o.get('is_correct')]
            corr_text = [o.get('content') for o in q.get('question_options', []) if o.get('is_correct')]
            print(f"  [{ex_name}] Q{qnum}: ans={corr} -> {corr_text}")
