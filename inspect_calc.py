import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r'C:\Users\Admin\.gemini\antigravity\scratch\osg202\data'

def inspect_q(filename, q_num):
    with open(f'{base_dir}\\{filename}', 'r', encoding='utf-8') as f:
        data = json.load(f)
    for q in data:
        if q['order_num'] == q_num:
            print(f"=== {filename} Q{q_num} ===")
            print(q.get('content'))
            print("Options:")
            for opt in q.get('question_options', []):
                corr = " [CORRECT]" if opt.get('is_correct') else ""
                print(f"  {opt['label']}: {opt.get('content')}{corr}")
            if q.get('explanation'):
                print("Explanation:", q['explanation'])
            print()

inspect_q('OSG202_SU26_RE_HN.json', 17)
inspect_q('OSG202_SU26_RE_HN.json', 29)
inspect_q('OSG202_SU26_RE_HN.json', 33)
inspect_q('OSG202_SU26_RE_HN.json', 48)
inspect_q('OSG202_SU26_FE_HN.json', 5)
inspect_q('OSG202_SU26_FE_HN.json', 14)
inspect_q('OSG202_SU26_FE_HN.json', 16)
