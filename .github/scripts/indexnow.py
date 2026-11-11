"""Envoie à IndexNow les URL publiées ou mises à jour.

Usage : python3 .github/scripts/indexnow.py <commit_avant> <commit_après>
        python3 .github/scripts/indexnow.py --all   (toutes les URL du sitemap)
"""
import json, re, subprocess, sys, urllib.request

site = open("site.yml", encoding="utf-8").read()
base = re.search(r"^url:\s*(\S+)", site, re.M).group(1).rstrip("/")
key = re.search(r"^indexnow_key:\s*(\S+)", site, re.M).group(1)
host = base.split("//", 1)[1]

if sys.argv[1] == "--all":
    sm = open("docs/sitemap.xml", encoding="utf-8").read()
    urls = re.findall(r"<loc>([^<]+)</loc>", sm)
else:
    before, after = sys.argv[1], sys.argv[2]
    if set(before) == {"0"}:  # premier push d'une branche
        before = after + "~1"
    changed = subprocess.run(["git", "diff", "--name-only", before, after],
                             capture_output=True, text=True, check=True).stdout.split()
    urls = []
    for f in changed:
        m = re.match(r"content/(articles|pages)/([^/]+)\.md$", f)
        if m:
            urls.append(f"{base}/{m.group(2)}/")
    if any(f.startswith("content/articles/") for f in changed):
        urls += [f"{base}/", f"{base}/calendrier/"]

urls = sorted(set(urls))
if not urls:
    print("Aucune URL à envoyer.")
    sys.exit(0)

body = json.dumps({"host": host, "key": key,
                   "keyLocation": f"{base}/{key}.txt", "urlList": urls}).encode()
req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body,
                             headers={"Content-Type": "application/json; charset=utf-8"})
try:
    with urllib.request.urlopen(req, timeout=30) as r:
        print("IndexNow :", r.status)
except urllib.error.HTTPError as e:
    print("IndexNow : erreur", e.code, e.read()[:300])
    sys.exit(1)
for u in urls:
    print(" -", u)
