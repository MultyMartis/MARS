#!/usr/bin/env python3
"""TEMPORARY frontend probe — NOT FOR GIT."""
import re
import urllib.request

html = urllib.request.urlopen("http://shpigovsky.test/").read().decode("utf-8", "replace")
nav = re.findall(r'class="site-header__nav-link[^"]*"[^>]*href="([^"]+)"[^>]*>([^<]+)</a>', html)
footer = re.findall(r'aria-label="[^"]*информация[^"]*"[\s\S]*?</nav>', html, re.I)
footer_block = footer[0] if footer else ""
legal_links = re.findall(r'href="([^"]+)"[^>]*class="site-footer__nav-link"[^>]*>([^<]+)</a>', footer_block)
if not legal_links:
    legal_links = re.findall(r'class="site-footer__nav-link"[^>]*href="([^"]+)"[^>]*>([^<]+)</a>', html)
print("PRIMARY NAV:")
for u, t in nav:
    print(f"  {t.strip()} -> {u}")
print("LEGAL/INFO FOOTER:")
for u, t in legal_links:
    if any(k in u for k in ("policy", "agreement", "consent", "cookie", "pravovaya", "privacy", "user")):
        print(f"  {t.strip()} -> {u}")

pp = urllib.request.urlopen("http://shpigovsky.test/privacy-policy/").read().decode("utf-8", "replace")
if "legal-document__container" in pp:
    print("privacy has legal-document__container: YES")
if "max-width: 900px" in pp:
    print("inline 900px in HTML: YES")
# check computed - look for stylesheet rule mention
css_href = re.findall(r'href="([^"]*v9-style[^"]*)"', pp)
print("css:", css_href[:1])
