> **Template: Owner Pitch Page** · B-O-G Template Library (see /templates/). Folder name kept so live URLs keep working.

# Home-services pitch-page template (electric / HVAC / plumbing) · Blades of Grass Marketing

Adapted from `../cleaning-template/`. Same rules, same C.L.O.S.E.R. order, same light scheme. Differences:
- `trade` column (required): `electric`, `hvac`, `plumbing`, or `plumbing-hvac`. It fills trade wording (urgent-call example, maintenance-plan example).
- `greeting` column (required) replaces `owner_name`: an owner first name when confirmed from a source, otherwise a neutral greeting like `Team Wellco`.
- No videos. The cleaning films (and the Reviews/Referral cuts, which say "after every great clean" and show a THA gift card) are not used. The plays section is text cards.
- Growth cards: urgent calls, after-hours/weekend calls answered and booked, more jobs on the board, reviews, referrals, win-backs, maintenance plans, estimate follow-up, crew stays in the field.
- Banned-phrase scan skips href URLs (a source URL may contain "llc").

Run: `python3 home-services-template/generate.py home-services-template/prospects.json`
