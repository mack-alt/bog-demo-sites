# Residential-cleaning pitch-page template (Blades of Grass Marketing)

This is the THA page turned into a template you can reuse for every prospect. It builds one page per prospect at `https://mack-alt.github.io/bog-demo-sites/<slug>/`.

## Files
- `template.html`: the page layout with `{{PLACEHOLDERS}}`. The order matches THA: hero film, *Two plays built for X* (Reviews and Referral videos), reputation and review cards, what we heard, what we noticed, the 9 ways we'd grow, front desk vs. hiring table, FAQ, and the Text Kenny CTA.
- `generate.py`: reads a CSV or JSON file of prospects and writes `<slug>/index.html` in the repo root.
- `prospects.csv`: a starter file with one row, `example-cleaning`, which is clearly labeled EXAMPLE data. `prospects-blank.csv` has the headers only.
- `RESEARCH-CHECKLIST.md`: what to collect for each prospect, and where to find it.
- Videos are shared from `../assets/cleaning/` (copied from tha/: hero, reviews, referral, plus their posters). Every page points to these copies.

## Run
```
cd bog-demo-sites
python3 cleaning-template/generate.py cleaning-template/prospects.csv          # build all
python3 cleaning-template/generate.py my.csv --only acme-cleaning               # one prospect
python3 cleaning-template/generate.py my.csv --draft                            # build even with missing required fields (shows yellow MISSING flags, so do not push)
git add <slug> && git commit -m "Add <slug> pitch" && git pull --rebase && git push
```
The script exits with a non-zero code when it skips a prospect or finds a banned phrase. Fix the data and run it again.

## Columns (CSV header = JSON keys)
| Column | Req? | Notes |
|---|---|---|
| slug | YES | URL folder name, using lowercase letters, digits, and hyphens (`acme-cleaning`) |
| business_name | YES | The legal or display name, as it appears on their site or Google |
| owner_name | YES | First name only. It appears in the H1, the reputation intro, and the CTA |
| city | YES | Main city they serve |
| short_name | no | Short name for headings ("THA"). Falls back to business_name |
| website_label | no | e.g. `acme-clean.com`, used in "What we noticed on ___" |
| gift_card_name | no | e.g. `Acme Gift Card`. Falls back to `<short_name> Gift Card`. Never give a $ amount |
| hero_intro | no | Custom hero paragraph. A generic, flattering default is used when it's blank |
| is_example | no | `yes` shows the EXAMPLE banner. Leave it blank for real prospects |
| review1..6_quote | no | **Copy the quote word-for-word** (an excerpt is fine, but do not change any words) |
| review1..6_name | no | Reviewer name exactly as shown (e.g. "John H.") |
| review1..6_source_label | no | e.g. "Google review" or "Google review featured on acme.com" |
| review1..6_source_url | no | Link where the quote can be checked |
| review1..6_service | no | "What we'd amplify": the paired B-O-G service, phrased benefit first ("The Referral Engine, so ...") |
| stat1..5_value / _label | no | e.g. `4.9★` / `Google, 120+ reviews`. Only use facts you've checked |
| heard_heading | no | Default heading is "What's on your plate" |
| heard1..3_title / _body | no | What the owner told Kenny (pain points). Leave blank if you haven't talked to them |
| noticed1..4_title / _body | no | What you saw on their site or Google listing. Facts only |

A review card is dropped unless it has a quote, a name, and a source_url. A section with no data (reputation, heard, noticed) is left out entirely. The page never shows a placeholder or made-up content.

## Rules baked in (check them again whenever you edit data)
- The only CTA is **Text Kenny**: `sms:+12067436296`, written as 206-743-6296. Kenny is faceless.
- No pricing and no profit share. Never use the words "guarantee", "24/7", "automated dispatch", "zero lost leads", or any certifications. The generator scans each page for these and warns you.
- Don't promise texting up front, and don't name other shops. The brand is "Blades of Grass Marketing" (never LLC).
- Phrasing is benefit first, then the why: "We answer every call, so you get all the business you deserve."
- Light scheme: white with a green accent. Built on C.L.O.S.E.R.: **C**larify (what we heard), **L**abel (what we noticed), **O**verview past pain (hiring table), **S**ell the vacation, meaning outcomes (plays and growth cards), **E**xplain concerns (FAQ), **R**einforce (Text Kenny).
- The videos carry a small "DRAFT" corner mark from the THA cut. That's the same as on THA.
