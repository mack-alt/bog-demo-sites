import sys
def page(c):
    svc=''.join(f'<div class="card"><h3>{a}</h3><p>{b}</p></div>' for a,b in c['svc'])
    gal=''.join(f'<img src="img/{g}" alt="{c["name"]} work photo">' for g in c['gal'])
    faq=''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in c['faq'])
    proof=''.join(f'<div class="stat"><b>{a}</b><span>{b}</span></div>' for a,b in c['proof'])
    opts=''.join(f'<option>{a}</option>' for a,_ in c['svc'])
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{c["title"]}</title><meta name="description" content="{c["tag"]}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap" rel="stylesheet">
<style>
:root{{--p:{c["p"]};--a:{c["a"]};--d:#0f172a;--bg:{c["bg"]}}}
*{{box-sizing:border-box}}body{{margin:0;font-family:Inter,system-ui,sans-serif;color:var(--d);background:#fff;line-height:1.55}}
a{{color:inherit}}.w{{max-width:1120px;margin:auto;padding:0 20px}}
.demo{{background:#111;color:#fff;text-align:center;font-size:12px;padding:6px}}
header{{position:sticky;top:0;background:#fffffff2;backdrop-filter:blur(6px);z-index:9;border-bottom:1px solid #e5e7eb}}
header .w{{display:flex;justify-content:space-between;align-items:center;height:64px}}.logo{{font-weight:800;font-size:18px;color:var(--p)}}
.btn{{display:inline-block;background:var(--a);color:#fff;padding:13px 22px;border-radius:10px;font-weight:700;text-decoration:none;border:0;font-size:16px;cursor:pointer}}
.btn.o{{background:transparent;border:2px solid #fff}}
.hero{{background:linear-gradient(90deg,{c["p"]}ee,{c["p"]}99),url(img/{c["hero"]}) center/cover;color:#fff;padding:56px 0}}
.hero .w{{display:grid;gap:32px}}h1{{font-size:clamp(32px,6vw,54px);line-height:1.08;margin:0 0 14px}}
.promo{{display:inline-block;background:#ffffff26;padding:6px 12px;border-radius:99px;font-size:14px;margin-bottom:14px}}
.cta{{display:flex;gap:12px;flex-wrap:wrap;margin:22px 0}}
form{{background:#fff;color:var(--d);padding:24px;border-radius:16px;box-shadow:0 20px 50px #0004;display:grid;gap:10px}}
form h2{{margin:0;font-size:22px}}input,select,textarea{{font:inherit;padding:12px;border:1px solid #cbd5e1;border-radius:8px;width:100%}}
.note{{font-size:12px;color:#64748b}}section{{padding:64px 0}}section.alt{{background:var(--bg)}}
h2.t{{font-size:clamp(26px,4vw,38px);margin:0 0 8px}}.sub{{color:#475569;margin:0 0 28px}}
.grid{{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(240px,1fr))}}
.card{{background:#fff;border:1px solid #e5e7eb;border-radius:14px;padding:22px;border-top:4px solid var(--p)}}.card h3{{margin:0 0 6px}}
.gal{{display:grid;gap:10px;grid-template-columns:repeat(auto-fill,minmax(160px,1fr))}}.gal img{{width:100%;aspect-ratio:1;object-fit:cover;border-radius:12px}}
.stat{{background:#fff;border-radius:14px;padding:22px;text-align:center;border:1px solid #e5e7eb}}.stat b{{display:block;font-size:30px;color:var(--p)}}
.label{{display:inline-block;background:var(--a);color:#fff;font-size:12px;padding:4px 10px;border-radius:99px;margin-bottom:12px}}
.ref{{background:var(--p);color:#fff;border-radius:20px;padding:40px;text-align:center}}
details{{border-bottom:1px solid #e5e7eb;padding:16px 0}}summary{{font-weight:700;cursor:pointer}}
footer{{background:var(--d);color:#cbd5e1;padding:40px 0 90px;font-size:15px}}footer .w{{display:grid;gap:20px;grid-template-columns:repeat(auto-fit,minmax(220px,1fr))}}
.hcall{{white-space:nowrap;flex-shrink:0;padding:10px 16px}}.hcall .full{{display:none}}.logo{{line-height:1.2;margin-right:10px}}
.mcall{{position:fixed;bottom:12px;left:12px;right:12px;text-align:center;z-index:10;box-shadow:0 8px 24px #0005}}
@media(min-width:600px){{.hcall .full{{display:inline}}}}
@media(min-width:900px){{.hero .w{{grid-template-columns:1.2fr 1fr;align-items:center}}.hero{{padding:90px 0}}.hcall{{white-space:nowrap;flex-shrink:0;padding:10px 16px}}.hcall .full{{display:none}}.logo{{line-height:1.2;margin-right:10px}}
.mcall{{display:none}}footer{{padding-bottom:40px}}}}
</style></head><body>
<div class="demo">Demo preview by Blades of Grass Marketing</div>
<header><div class="w"><span class="logo">{c["name"]}</span><a class="btn hcall" href="tel:{c["tel"]}" aria-label="Call {c["phone"]}">&#128222; Call<span class="full"> {c["phone"]}</span></a></div></header>
<div class="hero"><div class="w"><div>{c["promo"]}<h1>{c["h1"]}</h1><p style="font-size:19px;opacity:.95">{c["tag"]}</p>
<div class="cta"><a class="btn" href="#quote">{c["ctaq"]}</a><a class="btn o" href="tel:{c["tel"]}">Call {c["phone"]}</a></div><p style="opacity:.9;font-size:14px">{c["herofoot"]}</p></div>
<form id="quote" onsubmit="event.preventDefault();this.innerHTML='<h2>Thanks!</h2><p>This is a demo form — on the live site your request would go straight to the team.</p>'">
<h2>{c["ctaq"]}</h2><input required placeholder="Full name"><input required type="tel" placeholder="Phone"><input type="email" placeholder="Email"><input placeholder="{c["addr_ph"]}">
<select><option>Service needed</option>{opts}</select><textarea rows="3" placeholder="Anything we should know?"></textarea>
<button class="btn">{c["ctaq"]}</button><span class="note">Demo form — no data is sent.</span></form></div></div>
{c.get("video","")}<section><div class="w"><h2 class="t">Services</h2><p class="sub">{c["svcsub"]}</p><div class="grid">{svc}</div></div></section>
<section class="alt"><div class="w"><h2 class="t">Gallery</h2><p class="sub">A look at the {c["name"]} experience.</p><div class="gal">{gal}</div></div></section>
<section><div class="w">{c["prooflabel"]}<h2 class="t">{c["prooft"]}</h2><p class="sub">{c["proofsub"]}</p><div class="grid">{proof}</div></div></section>
<section class="alt"><div class="w"><div class="ref"><h2 class="t">{c["refh"]}</h2><p style="font-size:18px">{c["refp"]}</p><a class="btn" href="tel:{c["tel"]}">Ask about referrals</a></div></div></section>
<section><div class="w" style="max-width:800px"><h2 class="t">FAQ</h2>{faq}</div></section>
<footer><div class="w"><div><b style="color:#fff;font-size:18px">{c["name"]}</b><p>{c["foot"]}</p></div><div><b style="color:#fff">Contact</b><p>{c["contact"]}</p></div>
<div><p class="note" style="color:#94a3b8">Demo preview by Blades of Grass Marketing. Not the official site.</p></div></div></footer>
<a class="btn mcall" href="tel:{c["tel"]}">Call {c["phone"]}</a></body></html>'''
aloha=dict(name="Aloha Window & Exterior Wash",title="Aloha Window & Exterior Wash | Seattle Window Cleaning & Pressure Washing",p="#0b6e8a",a="#f59e0b",bg="#eef8fb",hero="a15.jpg",tel="+12063070760",phone="(206) 307-0760",
promo='<span class="promo">$50 off your first cleaning</span>',h1="Sparkling windows. A fresh exterior. The Aloha touch.",tag="Professional window cleaning, pressure washing, soft washing and roof surface care for Seattle homes and businesses.",
ctaq="Get a free quote",herofoot="Fully insured · Mon–Fri 8–7 · Sat 9–3",addr_ph="Street address & ZIP",svcsub="Residential and commercial exterior cleaning, done with honesty and care.",
svc=[("Window Cleaning","Interior and exterior glass cleaning that removes haze, fingerprints and buildup."),("Pressure Washing","Driveways, patios, walkways and hard surfaces brought back to life."),("House Soft Washing","Low-pressure washing for siding, trim and delicate exterior materials."),("Roof Surface Cleaning","Removes moss, streaks and seasonal debris safely."),("Solar Panel Cleaning","Residue-free cleaning to support better light absorption."),("Commercial Exterior","Storefront windows, building washing, parking lots and sidewalks.")],
gal=[f"a{i}.webp" for i in range(7,15)],prooflabel='<span class="label">From our family\'s THA House Cleaning customers</span>',
prooft="Trusted by Seattle families",proofsub="Aloha is new, and it comes from the same family as THA House Cleaning. These ratings belong to THA House Cleaning, not to Aloha.",
proof=[("4.9 ★","THA House Cleaning on Google (120+ reviews)"),("5.0 ★","THA House Cleaning on Yelp (176+ reviews)"),("15+ yrs","THA serving the Seattle area")],
refh="Inside & out, one family",refp="Our sister company THA House Cleaning takes care of the inside. Ask us about bundling interior and exterior care.",
faq=[("What areas do you serve?","We're based at 3400 Harbor Ave SW in Seattle and serve Seattle-area homes and businesses."),("Are you insured?","Yes, Aloha is fully insured."),("Will soft washing damage my siding?","Soft washing uses low pressure made for siding, trim and delicate materials."),("Do you offer bundle savings?","Yes. Pairing services like window cleaning plus pressure washing saves 5%, and new customers get $50 off their first cleaning."),("What are your hours?","Mon–Fri 8 AM–7 PM, Saturday 9 AM–3 PM, closed Sunday.")],
video='<section class="alt" style="padding:40px 0"><div class="w" style="max-width:900px"><h2 class="t">Pressure Wash Partner</h2><video controls playsinline preload="metadata" poster="video-poster.jpg" style="width:100%;border-radius:16px;background:#000"><source src="Pressure_Wash_Partner.mp4" type="video/mp4"></video></div></section>',foot="Window cleaning, pressure washing and exterior care in Seattle.",contact="3400 Harbor Ave SW, Seattle WA 98126<br>(206) 307-0760<br>smile@alohawashpro.com<br>Mon–Fri 8–7 · Sat 9–3 · Sun closed")
tha=dict(name="THA House Cleaning",title="THA House Cleaning | Seattle House Cleaning Services",p="#1f3d36",a="#c2410c",bg="#f6f3ee",hero="t8.webp",tel="+14252899310",phone="425-289-9310",
promo='<span class="promo">$25 off your first cleaning with code CLEAN25</span>',h1="We clean homes that make you feel good.",tag="Professional Seattle home cleaning with safe products, proven methods and spotless results.",
ctaq="Book my cleaning",herofoot="Google 4.9 ★ (120+) · Yelp 5.0 ★ (176+) · 2026 Nextdoor Neighborhood Fave",addr_ph="Address or ZIP",svcsub="From routine upkeep to a full reset. Pick what fits your home.",
svc=[("Regular Cleaning","Weekly, bi-weekly or monthly upkeep to keep your home consistently clean."),("Deep Cleaning","Extra attention to built-up grime and the details."),("Move In / Move Out","Full detailing to get units ready quickly."),("Airbnb Turnovers","Fast, detailed turnovers that keep guests happy."),("Office & Commercial","Professional cleaning with flexible schedules."),("Party & Open House","Before and after party cleaning and open house prep.")],
gal=[f"t{i}.webp" for i in (1,2,3,4,5,6,9)],prooflabel="",prooft="Numbers that build trust",proofsub="Thank you to the neighbors who trust us with their homes.",
proof=[("4.9 ★","Google (120+ reviews)"),("5.0 ★","Yelp (176+ reviews)"),("900+","Homes cleaned this year"),("15+","Years serving the Seattle area"),("2026","Nextdoor Neighborhood Fave")],
refh="Refer a friend, you both get a THA Gift Card",refp="Love your clean home? Share THA with a friend. When they book, you both get a THA Gift Card.",
faq=[("What's the difference between regular and deep cleaning?","Regular cleaning covers routine dust, dirt and surfaces. Deep cleaning targets built-up grime and detailed work. It's a good fit for an occasional reset."),("What products do you use?","We use safe products and proven methods."),("How do I get my first-clean discount?","Use code CLEAN25 for $25 off your first cleaning."),("Do you clean for Airbnb hosts and property managers?","Yes. We do turnovers and move-in/move-out cleans."),("Do you clean exteriors too?","Our sister company Aloha Window & Exterior Wash handles windows and exteriors.")],
foot="Seattle house cleaning for homeowners, hosts, businesses and property managers.",contact="425-289-9310<br>thacleaning.com")
open('aloha/index.html','w').write(page(aloha));open('tha/index.html','w').write(page(tha))
