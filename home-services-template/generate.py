#!/usr/bin/env python3
"""Build <slug>/index.html pitch pages for home-services (electric/HVAC/plumbing) prospects.

Usage (from repo root):
  python3 home-services-template/generate.py home-services-template/prospects.csv
  python3 home-services-template/generate.py prospects.json --out . [--draft] [--only slug]

Never invents data: optional sections with no data are left out; reviews
missing quote/name/source_url are dropped. Missing REQUIRED fields skip the
prospect (or, with --draft, render a visible yellow FLAG so it can't ship by accident).
"""
import csv, json, sys, os, re, html, argparse

HERE = os.path.dirname(os.path.abspath(__file__))
REQUIRED = ["slug", "business_name", "greeting", "city", "trade"]
BANNED = [r"guarantee", r"24/7", r"automated dispatch", r"zero lost leads", r"certif",
          r"\bLLC\b", r"profit[- ]share", r"\$\s?\d", r"per month", r"/mo\b", r"pricing"]
TRADES = {
  "electric": {"work": "electrical", "urgent": "power problem", "maint": "electrical safety check"},
  "hvac": {"work": "heating and cooling", "urgent": "no-heat or no-AC call", "maint": "furnace and AC tune-up"},
  "plumbing": {"work": "plumbing", "urgent": "leak or backed-up drain", "maint": "water heater and drain check"},
  "plumbing-hvac": {"work": "plumbing and heating", "urgent": "no-heat call or leak", "maint": "boiler, furnace, and plumbing check"},
}
N_REVIEWS, N_STATS, N_HEARD, N_NOTICED = 6, 5, 3, 4

def e(s): return html.escape((s or "").strip(), quote=True)
def g(r, k): return (r.get(k) or "").strip()

def load(path):
    if path.endswith(".json"):
        return json.load(open(path))
    with open(path, newline="", encoding="utf-8-sig") as f:
        return [r for r in csv.DictReader(f) if not g(r, "slug").startswith("#")]

def stats(r):
    out = [(g(r, f"stat{i}_value"), g(r, f"stat{i}_label")) for i in range(1, N_STATS + 1)]
    out = [s for s in out if s[0] and s[1]]
    if not out: return ""
    return '<div class="stats">' + "".join(f'<div class="stat"><b>{e(v)}</b>{e(l)}</div>' for v, l in out) + "</div>"

def reviews(r, warn):
    cards = []
    for i in range(1, N_REVIEWS + 1):
        q, n, u = g(r, f"review{i}_quote"), g(r, f"review{i}_name"), g(r, f"review{i}_source_url")
        if not (q or n or u): continue
        if not (q and n and u):
            warn(f"review{i} dropped: needs quote + name + source_url"); continue
        lbl = g(r, f"review{i}_source_label") or u
        svc = g(r, f"review{i}_service")
        amp = f'<p style="margin:0"><b>What we\'d amplify:</b> {e(svc)}</p>' if svc else ""
        cards.append(f'<div class="card"><p style="font-size:18px;margin:0 0 6px">“{e(q.strip("“”\""))}”</p>'
                     f'<p class="note" style="margin:0 0 10px">{e(n)} · <a href="{e(u)}" target="_blank" rel="noopener">{e(lbl)}</a></p>{amp}</div>')
    return "\n".join(cards)

def items(r, pre, n, warn):
    out = []
    for i in range(1, n + 1):
        t, b = g(r, f"{pre}{i}_title"), g(r, f"{pre}{i}_body")
        if t and b: out.append(f'<div class="card"><h3>{e(t)}</h3><p>{e(b)}</p></div>')
        elif t or b: warn(f"{pre}{i} dropped: needs title + body")
    return "\n".join(out)

def section(tpl, name, keep):
    pat = re.compile(r"\{\{#" + name + r"\}\}(.*?)\{\{/" + name + r"\}\}", re.S)
    return pat.sub((lambda m: m.group(1)) if keep else "", tpl)

def build(r, tpl, out, draft):
    slug = g(r, "slug")
    warns = []; warn = lambda m: warns.append(m)
    missing = [k for k in REQUIRED if not g(r, k)]
    if missing and not draft:
        return slug, None, [f"SKIPPED: missing required {missing}"]
    if slug and not re.fullmatch(r"[a-z0-9-]+", slug):
        return slug, None, ["SKIPPED: slug must be lowercase letters, digits, hyphens"]
    def val(k):
        v = g(r, k)
        return e(v) if v else f'<span class="flag">MISSING {k.upper()}</span>'
    biz = val("business_name"); short = e(g(r, "short_name")) or biz
    rc, hs = reviews(r, warn), stats(r)
    heard, noticed = items(r, "heard", N_HEARD, warn), items(r, "noticed", N_NOTICED, warn)
    if not rc: warn("no verifiable reviews -> reputation section omitted")
    if not heard: warn("no 'what we heard' items -> section omitted")
    if not noticed: warn("no 'what we noticed' items -> section omitted")
    t = tpl
    t = section(t, "REVIEWS", bool(rc)); t = section(t, "HEARD", bool(heard)); t = section(t, "NOTICED", bool(noticed))
    city = val("city")
    intro = e(g(r, "hero_intro")) or (f"Your {city} customers clearly trust what you do. This page is just for you: "
            "what we noticed, and how a B-O-G front desk can carry the parts of the business that shouldn't all sit on your shoulders.")
    is_ex = g(r, "is_example").lower() in ("1", "true", "yes")
    rep = {
        "EXAMPLE_BANNER": '<div class="example">EXAMPLE PAGE · fictional business and sample data to demonstrate the template · not a real prospect</div>' if is_ex else "",
        "BUSINESS_NAME": biz, "SHORT_NAME": short, "CITY": city, "SLUG": e(slug),
        "HERO_INTRO": intro, "HERO_STATS": hs, "REPUTATION_STATS": hs, "REVIEW_CARDS": rc,
        "HEARD_HEADING": e(g(r, "heard_heading")) or "What's on your plate",
        "HEARD_ITEMS": heard, "NOTICED_ITEMS": noticed,
        "WEBSITE_LABEL": e(g(r, "website_label")) or "your website",
        "GIFT_CARD": e(g(r, "gift_card_name")) or f"{short} Gift Card",
        "GREETING": val("greeting"),
        "TRADE_WORK": e(TRADES.get(g(r,"trade"),{}).get("work","")) or val("trade"),
        "URGENT_EXAMPLE": e(TRADES.get(g(r,"trade"),{}).get("urgent","")) or val("trade"),
        "MAINT_EXAMPLE": e(TRADES.get(g(r,"trade"),{}).get("maint","")) or val("trade"),
    }
    for k, v in rep.items(): t = t.replace("{{" + k + "}}", v)
    left = re.findall(r"\{\{[^}]+\}\}", t)
    if left: warn(f"unfilled placeholders: {sorted(set(left))}")
    text = re.sub(r"<style>.*?</style>|href=\"[^\"]*\"", "", t, flags=re.S)
    for b in BANNED:
        if re.search(b, text, re.I): warn(f"BANNED phrase /{b}/ found - fix data before shipping")
    if missing: warn(f"DRAFT: missing required {missing} (flagged on page)")
    d = os.path.join(out, slug or "_missing-slug"); os.makedirs(d, exist_ok=True)
    p = os.path.join(d, "index.html"); open(p, "w").write(t)
    return slug, p, warns

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("data"); ap.add_argument("--out", default=os.path.dirname(HERE))
    ap.add_argument("--draft", action="store_true"); ap.add_argument("--only")
    a = ap.parse_args()
    tpl = open(os.path.join(HERE, "template.html")).read()
    rc = 0
    for r in load(a.data):
        if a.only and g(r, "slug") != a.only: continue
        if not any((v or "").strip() for v in r.values()): continue
        slug, p, w = build(r, tpl, a.out, a.draft)
        print(f"[{slug or '?'}] " + (p or "not built"))
        for m in w: print("   - " + m)
        if p is None or any("BANNED" in m for m in w): rc = 1
    sys.exit(rc)

if __name__ == "__main__": main()
