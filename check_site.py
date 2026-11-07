"""Dependency-free static checks; does not contact Google or any private service."""
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
ROOT = Path(__file__).resolve().parent
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.ids=set(); self.tags=[]; self.meta=[]
    def handle_starttag(self, tag, attrs):
        a=dict(attrs); self.tags.append(tag)
        if "href" in a: self.links.append(a["href"])
        if "id" in a: self.ids.add(a["id"])
        if tag=="meta": self.meta.append(a)
pages={}
for route, filename in [("/", "index.html"),("/privacy", "privacy.html"),("/terms", "terms.html")]:
    text=(ROOT/filename).read_text(encoding="utf-8")
    page=Page(); page.feed(text); pages[route]=page
    assert "AgentFlow AI Backup" in text and "INSERT" not in text and "REPLACE_" not in text
    assert page.tags.count("h1")==1 and "title" in page.tags
    assert all(x not in page.tags for x in ("script","iframe","form"))
    assert any(m.get("name")=="viewport" for m in page.meta)
    assert any(m.get("name")=="description" and m.get("content") for m in page.meta)
    assert "/privacy" in page.links and "/terms" in page.links
    print("PASS", filename, "metadata, navigation, no active collection")
for route, page in pages.items():
    for link in page.links:
        u=urlsplit(link)
        if u.scheme:
            assert u.scheme=="https"; continue
        if u.path=="/style.css": assert (ROOT/"style.css").is_file(); continue
        target=u.path or route
        assert target in pages, link
        if u.fragment: assert u.fragment in pages[target].ids, link
assert json.loads((ROOT/"vercel.json").read_text())["cleanUrls"] is True
css=(ROOT/"style.css").read_text()
assert "@media(max-width:700px)" in css and "grid-template-columns:1fr" in css
assert "overflow-wrap:anywhere" in css
assert pages["/privacy"].tags.count("h2")==20
print("PASS all internal links/fragments, clean route mapping, responsive CSS and 20 policy sections")
