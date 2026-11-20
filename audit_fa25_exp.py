import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Admin\.gemini\antigravity\scratch\osg202\data\OSG202_FA25_RE.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data:
    num = q['order_num']
    opts = q.get('question_options', [])
    correct = [o['label'] for o in opts if o.get('is_correct')]
    exp = q.get('explanation') or ''
    
    # Check if explanation mentions "Do đó, phương án X" or "Đáp án X"
    m = re.findall(r'(?:phương án|đáp án)\s+([A-E])\b', exp, re.IGNORECASE)
    if m:
        # last mention often concludes the answer
        last_mention = m[-1].upper()
        if last_mention not in correct:
            print(f"Q{num}: Marked={correct}, but Explanation says: {m} (last={last_mention})")
            print("  Snippet:", exp[-200:])
