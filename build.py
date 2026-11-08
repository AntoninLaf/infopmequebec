#!/usr/bin/env python3
"""Générateur statique d'InfoPME Québec.

Usage : python3 build.py
Lit content/ et écrit le site complet dans docs/ (servi par GitHub Pages).
Échoue (code 1) si un lien interne est brisé ou si un article est incomplet.
"""
import html
import json
import re
import shutil
import sys
from datetime import date, datetime
from email.utils import format_datetime
from pathlib import Path

import markdown
import yaml

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "content"
OUT = ROOT / "docs"
CONFIG = yaml.safe_load((ROOT / "site.yml").read_text(encoding="utf-8"))
BASE = CONFIG["url"].rstrip("/")

REQUIRED = ["title", "description", "date", "category", "sources", "verified"]
MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août",
        "septembre", "octobre", "novembre", "décembre"]


def fr_date(d):
    d = to_date(d)
    return f"{d.day}{'er' if d.day == 1 else ''} {MOIS[d.month - 1]} {d.year}"


def to_date(v):
    if isinstance(v, datetime):
        return v.date()
    if isinstance(v, date):
        return v
    return date.fromisoformat(str(v))


def slugify(s):
    import unicodedata
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def read_md(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        sys.exit(f"ERREUR : front matter manquant dans {path}")
    meta = yaml.safe_load(m.group(1)) or {}
    body = markdown.markdown(m.group(2), extensions=["tables", "attr_list", "sane_lists"])
    return meta, body


def esc(s):
    return html.escape(str(s), quote=True)


CSS = """
:root{--ink:#14171c;--muted:#5d6672;--line:#e2e5ea;--navy:#0f2a4a;--navy-2:#1d3d66;--gold:#b8892b;--gold-bg:#faf5ea;--paper:#fff}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;font:17px/1.65 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color:var(--ink);background:var(--paper)}
a{color:var(--navy-2)}a:hover{color:var(--gold)}
.serif,h1,h2,h3,.brand{font-family:Georgia,"Times New Roman",serif}
.wrap{max-width:780px;margin:0 auto;padding:0 20px}
.topbar{background:var(--navy);color:#cfd8e3;font-size:13px}.topbar .wrap{padding-top:6px;padding-bottom:6px;display:flex;justify-content:space-between;gap:12px}
header.site{border-bottom:3px double var(--navy)}
header.site .wrap{text-align:center;padding-top:22px;padding-bottom:0}
.brand{display:inline-block;font-weight:700;font-size:38px;line-height:1;color:var(--navy);text-decoration:none;letter-spacing:-.02em}.brand span{color:var(--gold)}
.tag{margin:6px 0 14px;color:var(--muted);font-size:14px;font-style:italic;font-family:Georgia,serif}
nav.main{display:flex;justify-content:center;flex-wrap:wrap;gap:4px 26px;border-top:1px solid var(--line);padding:10px 0}
nav.main a{color:var(--ink);text-decoration:none;font-size:13px;font-weight:700;text-transform:uppercase;letter-spacing:.06em;white-space:nowrap}nav.main a:hover{color:var(--gold)}
main{padding:30px 0 48px}
h1{font-size:34px;line-height:1.18;letter-spacing:-.01em;margin:.15em 0 .45em;color:var(--navy)}
h2{font-size:24px;line-height:1.3;margin:1.8em 0 .5em;color:var(--navy)}h3{font-size:20px;margin:1.5em 0 .4em}
.meta{color:var(--muted);font-size:14px}
.kicker{display:inline-block;font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--gold);text-decoration:none}
.section-title{font-family:system-ui,sans-serif;font-size:13px;font-weight:800;text-transform:uppercase;letter-spacing:.1em;color:var(--navy);border-bottom:2px solid var(--navy);padding-bottom:6px;margin:0 0 4px}
.retenir{background:var(--gold-bg);border-left:4px solid var(--gold);padding:14px 18px;margin:22px 0;border-radius:2px}
.retenir h2{margin:0 0 6px;font-size:17px}.retenir ul{margin:0;padding-left:20px}
.deadline{display:inline-block;background:var(--navy);color:#fff;font-weight:700;font-size:13px;padding:2px 10px;border-radius:2px}
table{border-collapse:collapse;width:100%;margin:16px 0;font-size:15px}th,td{border:1px solid var(--line);padding:8px 10px;text-align:left;vertical-align:top}th{background:#f4f6f9;color:var(--navy)}
.sources{border-top:1px solid var(--line);margin-top:36px;padding-top:16px;font-size:15px}
.disclaimer{font-size:14px;color:var(--muted);background:#f4f6f9;padding:12px 16px;border-radius:2px}
ul.list{list-style:none;padding:0;margin:0}ul.list li{padding:18px 0;border-bottom:1px solid var(--line)}
ul.list h2,ul.list h3{margin:4px 0 6px;font-size:21px;line-height:1.3}ul.list h2 a,ul.list h3 a{color:var(--ink);text-decoration:none}ul.list h2 a:hover,ul.list h3 a:hover{color:var(--navy-2)}
ul.list p{margin:0;color:var(--muted);font-size:15px}
.dl{list-style:none;padding:0;margin:0 0 8px}
.dl li{display:grid;grid-template-columns:74px 1fr;gap:16px;align-items:center;padding:14px 0;border-bottom:1px solid var(--line)}
.dl .day{text-align:center;border:2px solid var(--navy);border-radius:2px;line-height:1.1;padding:6px 0}
.dl .day b{display:block;font-family:Georgia,serif;font-size:28px;color:var(--navy)}.dl .day small{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.06em;color:var(--muted)}
.dl a.t{font-family:Georgia,serif;font-size:19px;font-weight:700;color:var(--ink);text-decoration:none;line-height:1.3}.dl a.t:hover{color:var(--navy-2)}
.left{display:inline-block;margin-top:4px;font-size:13px;font-weight:700;color:var(--gold)}.left.soon{color:#b42318}
.more{font-size:14px;font-weight:700;text-decoration:none}
.lead{font-size:18px;color:#333}
.cal td:first-child{white-space:nowrap;font-weight:600}
footer.site{border-top:3px double var(--navy);color:var(--muted);font-size:14px;padding:24px 0 40px}
footer.site a{color:var(--muted)}
@media(max-width:560px){.topbar span:last-child{display:none}.lead{font-size:16px}.tag{display:none}body{font-size:16px}h1{font-size:27px}.brand{font-size:30px}.dl li{grid-template-columns:60px 1fr;gap:12px}.dl .day b{font-size:22px}}
"""


def layout(title, description, path, body, *, schema=None, og_type="website", noindex=False):
    url = BASE + path
    cats = "".join(
        f'<a href="/categorie/{c["slug"]}/">{esc(c.get("short", c["name"]))}</a>' for c in CONFIG["categories"] if c.get("nav")
    )
    full_title = title if path == "/" else f"{title} | {CONFIG['name']}"
    schema_tag = (
        f'<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>' if schema else ""
    )
    return f"""<!doctype html>
<html lang="fr-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{url}">
{'<meta name="robots" content="noindex">' if noindex else '<meta name="robots" content="index,follow,max-image-preview:large">'}
<meta property="og:site_name" content="{esc(CONFIG['name'])}">
<meta property="og:locale" content="fr_CA">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary">
<link rel="alternate" type="application/rss+xml" title="{esc(CONFIG['name'])}" href="/feed.xml">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 32 32%22><rect width=%2232%22 height=%2232%22 rx=%226%22 fill=%22%230b5cad%22/><text x=%2216%22 y=%2222%22 font-size=%2216%22 text-anchor=%22middle%22 fill=%22white%22 font-family=%22sans-serif%22 font-weight=%22bold%22>i</text></svg>">
<style>{CSS}</style>
{schema_tag}
</head>
<body>
<div class="topbar"><div class="wrap"><span>Subventions · Programmes d'aide · Dates limites</span><span>Sources officielles vérifiées</span></div></div>
<header class="site"><div class="wrap">
<a class="brand" href="/">InfoPME<span> Québec</span></a>
<p class="tag">{esc(CONFIG['tagline'])}</p>
<nav class="main"><a href="/calendrier/">Dates limites</a>{cats}</nav>
</div></header>
<main><div class="wrap">
{body}
</div></main>
<footer class="site"><div class="wrap">
<p><strong>{esc(CONFIG['name'])}</strong> — {esc(CONFIG['tagline'])}</p>
<p><a href="/a-propos/">À propos</a> · <a href="/politique-editoriale/">Politique éditoriale</a> · <a href="/corrections/">Corrections et contact</a> · <a href="/feed.xml">RSS</a></p>
<p>Information générale seulement. Vérifiez toujours les conditions auprès de l'organisme responsable avant de déposer une demande.</p>
</div></footer>
</body>
</html>
"""


def write(path, content):
    target = OUT / path.lstrip("/")
    if path.endswith("/"):
        target = target / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")


def org_schema():
    return {
        "@type": "NewsMediaOrganization",
        "name": CONFIG["name"],
        "url": BASE + "/",
        "publishingPrinciples": BASE + "/politique-editoriale/",
        "correctionsPolicy": BASE + "/corrections/",
        "parentOrganization": {"@type": "Organization", "name": CONFIG["publisher"]},
    }


def load_articles():
    arts = []
    cat_slugs = {c["slug"] for c in CONFIG["categories"]}
    for p in sorted((CONTENT / "articles").glob("*.md")):
        meta, body = read_md(p)
        missing = [k for k in REQUIRED if not meta.get(k)]
        if missing:
            sys.exit(f"ERREUR : {p.name} — champs manquants : {missing}")
        if meta["category"] not in cat_slugs:
            sys.exit(f"ERREUR : {p.name} — catégorie inconnue {meta['category']}")
        if meta.get("draft"):
            continue
        meta["slug"] = meta.get("slug") or p.stem
        meta["date"] = to_date(meta["date"])
        meta["updated"] = to_date(meta.get("updated") or meta["date"])
        meta["verified"] = to_date(meta["verified"])
        if meta.get("deadline"):
            meta["deadline"] = to_date(meta["deadline"])
        meta["path"] = f"/{meta['slug']}/"
        meta["body"] = body
        arts.append(meta)
    slugs = [a["slug"] for a in arts]
    dupes = {s for s in slugs if slugs.count(s) > 1}
    if dupes:
        sys.exit(f"ERREUR : slugs en double : {dupes}")
    return sorted(arts, key=lambda a: (a["date"], a["updated"]), reverse=True)


def cat(slug):
    return next(c for c in CONFIG["categories"] if c["slug"] == slug)


def article_page(a, arts):
    c = cat(a["category"])
    retenir = ""
    if a.get("retenir"):
        items = "".join(f"<li>{markdown.markdown(x)[3:-4]}</li>" for x in a["retenir"])
        retenir = f'<aside class="retenir"><h2>Ce qu\'il faut retenir</h2><ul>{items}</ul></aside>'
    dl = (
        f' · <span class="deadline">Date limite : {fr_date(a["deadline"])}</span>'
        if a.get("deadline") else ""
    )
    upd = f" · Mis à jour le {fr_date(a['updated'])}" if a["updated"] != a["date"] else ""
    srcs = "".join(
        f'<li><a href="{esc(s["url"])}" rel="noopener">{esc(s["name"])}</a></li>' for s in a["sources"]
    )
    related = [x for x in arts if x["slug"] != a["slug"] and x["category"] == a["category"]][:4]
    if len(related) < 3:
        related += [x for x in arts if x["slug"] != a["slug"] and x not in related][: 3 - len(related)]
    rel_html = ""
    if related:
        rel_html = "<h2>À lire aussi</h2><ul>" + "".join(
            f'<li><a href="{x["path"]}">{esc(x["title"])}</a></li>' for x in related
        ) + "</ul>"
    body = f"""<article>
<a class="kicker" href="/categorie/{c['slug']}/">{esc(c['name'])}</a>
<h1>{esc(a['title'])}</h1>
<p class="meta">Par <a href="/a-propos/">La rédaction</a> · Publié le <time datetime="{a['date']}">{fr_date(a['date'])}</time>{upd}{dl}</p>
{retenir}
{a['body']}
<div class="sources">
<p><strong>Sources officielles</strong> (vérifiées le {fr_date(a['verified'])}) :</p>
<ul>{srcs}</ul>
<p class="disclaimer">Information à titre indicatif. Vérifiez les conditions auprès de l'organisme responsable avant de déposer une demande. Une erreur? <a href="/corrections/">Signalez-la</a>.</p>
</div>
{rel_html}
</article>"""
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "NewsArticle",
                "headline": a["title"][:110],
                "description": a["description"],
                "datePublished": f"{a['date']}T08:00:00-05:00",
                "dateModified": f"{a['updated']}T08:00:00-05:00",
                "inLanguage": "fr-CA",
                "mainEntityOfPage": BASE + a["path"],
                "articleSection": c["name"],
                "author": {"@type": "Organization", "name": "La rédaction d'InfoPME Québec", "url": BASE + "/a-propos/"},
                "publisher": org_schema(),
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Accueil", "item": BASE + "/"},
                    {"@type": "ListItem", "position": 2, "name": c["name"], "item": f"{BASE}/categorie/{c['slug']}/"},
                    {"@type": "ListItem", "position": 3, "name": a["title"], "item": BASE + a["path"]},
                ],
            },
        ],
    }
    write(a["path"], layout(a["title"], a["description"], a["path"], body, schema=schema, og_type="article"))


def list_html(arts, h="h2"):
    out = []
    for a in arts:
        c = cat(a["category"])
        dl = f' · <span class="deadline">Date limite : {fr_date(a["deadline"])}</span>' if a.get("deadline") else ""
        out.append(
            f'<li><a class="kicker" href="/categorie/{c["slug"]}/">{esc(c["name"])}</a>'
            f'<{h}><a href="{a["path"]}">{esc(a["title"])}</a></{h}>'
            f'<p>{fr_date(a["date"])}{dl} — {esc(a["description"])}</p></li>'
        )
    return '<ul class="list">' + "".join(out) + "</ul>"


def build():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    arts = load_articles()
    today = date.today()

    for a in arts:
        article_page(a, arts)

    # Accueil : dates limites d'abord
    MOIS_C = ["janv.", "févr.", "mars", "avr.", "mai", "juin", "juil.", "août", "sept.", "oct.", "nov.", "déc."]
    upcoming = sorted([a for a in arts if a.get("deadline") and a["deadline"] >= today], key=lambda a: a["deadline"])[:6]
    if upcoming:
        up_html = '<h2 class="section-title">Prochaines dates limites</h2><ul class="dl">' + "".join(
            f'<li><div class="day"><b>{a["deadline"].day}</b><small>{MOIS_C[a["deadline"].month-1]}</small></div>'
            f'<div><a class="t" href="{a["path"]}">{esc(a["title"])}</a><br>'
            f'<span class="left" data-deadline="{a["deadline"]}"></span></div></li>' for a in upcoming
        ) + '</ul><p><a class="more" href="/calendrier/">Voir tout le calendrier →</a></p>'
    else:
        up_html = '<p>Aucune date limite à venir pour le moment.</p>'
    countdown = """<script>document.querySelectorAll('[data-deadline]').forEach(function(e){var d=new Date(e.dataset.deadline+'T23:59:00'),n=Math.ceil((d-new Date())/864e5);if(n<0){e.textContent='Terminé';return}e.textContent=n===0?'Dernier jour':n===1?'Il reste 1 jour':'Il reste '+n+' jours';if(n<=7)e.classList.add('soon')})</script>"""
    home = f"""<h1 class="serif" style="font-size:26px;margin-top:0">Les subventions et programmes d'aide pour les PME du Québec, avant la date limite</h1>
<p class="lead">{esc(CONFIG['intro'])}</p>
{up_html}
<h2 class="section-title" style="margin-top:40px">Dernières nouvelles</h2>
{list_html(arts[:30], "h3")}
{countdown}"""
    home_schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebSite", "name": CONFIG["name"], "url": BASE + "/", "inLanguage": "fr-CA"}, org_schema()]}
    write("/", layout(CONFIG["name"] + " — " + CONFIG["tagline"], CONFIG["description"], "/", home, schema=home_schema))

    # Catégories
    for c in CONFIG["categories"]:
        items = [a for a in arts if a["category"] == c["slug"]]
        body = f"<h1>{esc(c['name'])}</h1><p>{esc(c['description'])}</p>" + (
            list_html(items) if items else "<p>Aucun article pour le moment.</p>")
        write(f"/categorie/{c['slug']}/", layout(c["name"], c["description"], f"/categorie/{c['slug']}/", body,
                                                 noindex=not items))

    # Calendrier des dates limites
    future = sorted([a for a in arts if a.get("deadline") and a["deadline"] >= today], key=lambda a: a["deadline"])
    past = sorted([a for a in arts if a.get("deadline") and a["deadline"] < today], key=lambda a: a["deadline"], reverse=True)
    rows = lambda L: "".join(
        f'<tr><td>{fr_date(a["deadline"])}</td><td><a href="{a["path"]}">{esc(a["title"])}</a></td></tr>' for a in L)
    cal = (f"<h1>Calendrier des dates limites pour les PME du Québec</h1>"
           f"<p>Les prochaines dates limites des subventions, programmes d'aide et appels de projets couverts par InfoPME Québec, "
           f"de la plus proche à la plus lointaine. Mis à jour le {fr_date(today)}.</p>"
           + (f'<table class="cal"><thead><tr><th>Date limite</th><th>Programme</th></tr></thead><tbody>{rows(future)}</tbody></table>'
              if future else "<p>Aucune date limite à venir pour le moment.</p>")
           + (f'<h2>Dates limites passées</h2><table class="cal"><tbody>{rows(past)}</tbody></table>' if past else ""))
    write("/calendrier/", layout("Calendrier des dates limites — subventions PME Québec",
                                 "Toutes les prochaines dates limites des subventions et programmes d'aide pour les PME du Québec, en un seul calendrier.",
                                 "/calendrier/", cal))

    # Pages fixes
    pages = []
    for p in sorted((CONTENT / "pages").glob("*.md")):
        meta, body = read_md(p)
        path = f"/{p.stem}/"
        write(path, layout(meta["title"], meta["description"], path, f"<h1>{esc(meta['title'])}</h1>{body}"))
        pages.append(path)

    write("/404.html", layout("Page introuvable", "Page introuvable.", "/404.html",
                              '<h1>Page introuvable</h1><p><a href="/">Retour à l\'accueil</a></p>', noindex=True))

    # Sitemaps
    urls = [("/", today)] + [(a["path"], a["updated"]) for a in arts] + [("/calendrier/", today)] + \
           [(f"/categorie/{c['slug']}/", today) for c in CONFIG["categories"] if any(a["category"] == c["slug"] for a in arts)] + \
           [(p, today) for p in pages]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
        f"<url><loc>{BASE}{u}</loc><lastmod>{d}</lastmod></url>\n" for u, d in urls) + "</urlset>\n"
    (OUT / "sitemap.xml").write_text(sm, encoding="utf-8")

    recent = [a for a in arts if (today - a["date"]).days <= 2]
    news = ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:news="http://www.google.com/schemas/sitemap-news/0.9">\n' + "".join(
                f"<url><loc>{BASE}{a['path']}</loc><news:news><news:publication><news:name>{esc(CONFIG['name'])}</news:name>"
                f"<news:language>fr</news:language></news:publication><news:publication_date>{a['date']}T08:00:00-05:00</news:publication_date>"
                f"<news:title>{esc(a['title'])}</news:title></news:news></url>\n" for a in recent) + "</urlset>\n")
    (OUT / "news-sitemap.xml").write_text(news, encoding="utf-8")

    # RSS
    items = "".join(
        f"<item><title>{esc(a['title'])}</title><link>{BASE}{a['path']}</link><guid>{BASE}{a['path']}</guid>"
        f"<pubDate>{format_datetime(datetime(a['date'].year, a['date'].month, a['date'].day, 8))}</pubDate>"
        f"<description>{esc(a['description'])}</description></item>" for a in arts[:30])
    rss = (f'<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel><title>{esc(CONFIG["name"])}</title>'
           f"<link>{BASE}/</link><description>{esc(CONFIG['description'])}</description><language>fr-ca</language>{items}</channel></rss>\n")
    (OUT / "feed.xml").write_text(rss, encoding="utf-8")

    (OUT / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\nSitemap: {BASE}/news-sitemap.xml\n", encoding="utf-8")
    (OUT / "CNAME").write_text(CONFIG["domain"] + "\n", encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")

    check_links()
    print(f"OK — {len(arts)} articles, {len(pages)} pages. Site écrit dans docs/.")


def check_links():
    bad = []
    for f in OUT.rglob("*.html"):
        for href in re.findall(r'href="(/[^"#?]*)', f.read_text(encoding="utf-8")):
            t = OUT / href.lstrip("/")
            if href.endswith("/"):
                t = t / "index.html"
            if not t.exists():
                bad.append(f"{f.relative_to(OUT)} → {href}")
    if bad:
        print("ERREUR : liens internes brisés :\n  " + "\n  ".join(sorted(set(bad))))
        sys.exit(1)


if __name__ == "__main__":
    build()
