#!/usr/bin/env python3
"""
Millstone & Co. — sync-partials.py

Refreshes the shared chrome in every page from docs/partials/. Pages stay plain
static HTML (no include system at runtime); this script only rewrites the
regions between marker comments, so you edit a partial once and re-sync.

Markers a page carries (the JSON is the page's own settings):

  <!-- @head {"title": "…", "description": "…", "file": "index.html"} -->
  <!-- @head:end -->
      add  "robots": "noindex"  for login, register, dashboard, 404, coming-soon:
      the canonical + social block is replaced by <meta name="robots" content="noindex,nofollow">.

  <!-- @header {"nav": "home1"} -->     public header.  nav = home1 home2 about products
  <!-- @header:end -->                  plans pricing blog contact dashboard none

  <!-- @footer -->  <!-- @footer:end -->       public footer
  <!-- @scripts --> <!-- @scripts:end -->      Bootstrap bundle + main.js
  <!-- @appnav {"active": "overview"} --> <!-- @appnav:end -->   dashboard sidebar
  <!-- @apptop --> <!-- @apptop:end -->                          dashboard top bar

Anything between a start and end marker is replaced; everything outside is left alone.
Usage (from the template root):   python docs/sync-partials.py [page.html ...]
"""
import html
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PARTIALS = ROOT / "docs" / "partials"

NAV_HREF = {
    "about": "about.html", "products": "products.html", "plans": "delivery-plans.html",
    "pricing": "pricing.html", "blog": "blog.html", "contact": "contact.html",
    "dashboard": "dashboard.html",
}
HOME_HREF = {"home1": "index.html", "home2": "home-2.html"}


def load(name):
    text = (PARTIALS / name).read_text(encoding="utf-8")
    return re.sub(r"^\s*<!--.*?-->\s*", "", text, count=1, flags=re.S).rstrip() + "\n"


def build_head(cfg):
    out = load("head.html")
    title = html.escape(cfg["title"], quote=True)
    desc = html.escape(cfg["description"], quote=True)
    if cfg.get("robots") == "noindex":
        out = re.sub(r"<!-- @SEO -->.*?<!-- @SEO:end -->", '<meta name="robots" content="noindex,nofollow">', out, flags=re.S)
    else:
        out = out.replace("<!-- @SEO -->\n", "").replace("<!-- @SEO:end -->\n", "")
    out = out.replace("{{PAGE_TITLE}}", title).replace("{{PAGE_DESCRIPTION}}", desc)
    out = out.replace("{{PAGE_FILE}}", "" if cfg["file"] == "index.html" else cfg["file"])
    return out


def mark(tag, current=False):
    """Add nav-active (and aria-current when it is the page itself) to an opening tag."""
    tag = re.sub(r'class="([^"]*)"', lambda m: 'class="%s nav-active"' % m.group(1), tag, count=1)
    if current:
        tag = tag.replace(">", ' aria-current="page">', 1)
    return tag


def build_header(cfg, page_file):
    out = load("header.html")
    nav = cfg.get("nav", "none")
    if nav in HOME_HREF:
        out = re.sub(r'<a class="nav-link dropdown-toggle"[^>]*>', lambda m: mark(m.group(0)), out, count=1)
        out = re.sub(r'<a class="dropdown-item" href="%s"[^>]*>' % re.escape(HOME_HREF[nav]),
                     lambda m: mark(m.group(0), HOME_HREF[nav] == page_file), out, count=1)
    elif nav in NAV_HREF:
        href = NAV_HREF[nav]
        out = re.sub(r'<a class="nav-link" href="%s"[^>]*>' % re.escape(href),
                     lambda m: mark(m.group(0), href == page_file), out, count=1)
    elif nav != "none":
        sys.exit("Unknown nav key %r in %s" % (nav, page_file))
    return out


def build_appnav(cfg, page_file):
    out = load("app-nav.html")
    key = cfg.get("active")
    if key:
        out, n = re.subn(r'<a href="([^"]+)" data-key="%s">' % re.escape(key),
                         lambda m: '<a href="%s" data-key="%s" class="nav-active" aria-current="page">' % (m.group(1), key), out, count=1)
        if not n:
            sys.exit("Unknown appnav key %r in %s" % (key, page_file))
    return out


def replace_region(text, name, builder):
    pattern = re.compile(r"(<!-- @%s(?P<cfg> \{.*?\})? -->\n)(.*?)(<!-- @%s:end -->)" % (name, name), re.S)

    def sub(m):
        cfg = json.loads(m.group("cfg")) if m.group("cfg") else {}
        return m.group(1) + builder(cfg) + m.group(4)

    return pattern.subn(sub, text)


def main():
    names = sys.argv[1:]
    pages = [ROOT / n for n in names] if names else sorted(ROOT.glob("*.html"))
    for page in pages:
        text = page.read_text(encoding="utf-8")
        counts = []
        for name, builder in (
            ("head", build_head),
            ("header", lambda c: build_header(c, page.name)),
            ("footer", lambda c: load("footer.html")),
            ("scripts", lambda c: load("scripts.html")),
            ("appnav", lambda c: build_appnav(c, page.name)),
            ("apptop", lambda c: load("app-top.html")),
        ):
            text, n = replace_region(text, name, builder)
            counts.append("%s:%d" % (name, n))
        page.write_text(text, encoding="utf-8", newline="\n")
        print("synced %-28s %s" % (page.name, " ".join(counts)))


if __name__ == "__main__":
    main()
