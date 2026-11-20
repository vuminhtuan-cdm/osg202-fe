import urllib.request

urls = [
    'https://vuminhtuan-cdm.github.io/osg202-fe/style.css',
    'https://vuminhtuan-cdm.github.io/osg202-fe/exams.js',
    'https://vuminhtuan-cdm.github.io/osg202-fe/app.js',
    'https://vuminhtuan-cdm.github.io/osg202-fe/images/sp26_re_q01.jpg',
    'https://vuminhtuan-cdm.github.io/osg202-fe/images/fa25_fe_q01.webp'
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            fname = u.split('/')[-1]
            print(f"{resp.status} OK: {fname} ({len(resp.read())} bytes)")
    except Exception as e:
        print(f"FAIL: {u} - {e}")
