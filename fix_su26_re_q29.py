import json

path = r'C:\Users\Admin\.gemini\antigravity\scratch\osg202\data\OSG202_SU26_RE_HN.json'
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data:
    if q['order_num'] == 29:
        for opt in q['question_options']:
            if opt['label'] == 'B':
                opt['is_correct'] = True
            else:
                opt['is_correct'] = False
        print("Updated Q29:", [o['label'] for o in q['question_options'] if o['is_correct']])

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Saved updated SU26_RE_HN.json")
