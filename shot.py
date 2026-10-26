from playwright.sync_api import sync_playwright
with sync_playwright() as p:
  b=p.chromium.launch(executable_path="/usr/bin/google-chrome")
  for s in ["aloha","tha"]:
    for n,vp in [("desktop",dict(width=1440,height=900)),("mobile",dict(width=390,height=844))]:
      pg=b.new_page(viewport=vp,device_scale_factor=1);pg.goto(f"file:///workspace/bog/demo-sites/{s}/index.html");pg.wait_for_timeout(1500)
      pg.screenshot(path=f"/workspace/bog/demo-sites/{s}/screenshot-{n}.png",full_page=True)
