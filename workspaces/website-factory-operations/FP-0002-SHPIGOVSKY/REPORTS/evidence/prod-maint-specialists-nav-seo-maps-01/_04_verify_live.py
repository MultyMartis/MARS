# -*- coding: utf-8 -*-
import re
import urllib.request

BASE = "https://shpigovsky.ru"


def fetch(url):
    return urllib.request.urlopen(url, timeout=30).read().decode("utf-8", "replace")


contacts = fetch(f"{BASE}/kontakty/")
for src in re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', contacts, re.I):
    if "constructor" in src:
        print("MAP_SRC", src)

home = fetch(f"{BASE}/")
print("HOME_TITLE", re.search(r"<title>(.*?)</title>", home, re.I | re.S).group(1))
desc = re.findall(r'<meta name="description" content="([^"]+)"', home, re.I)
print("HOME_DESC", desc[0] if desc else "NONE")

spec = fetch(f"{BASE}/specialisty/")
print("SPEC_NAV", "internal-page-nav" in spec, "breadcrumbs" in spec)

service = fetch(f"{BASE}/uslugi/zavisimosti/lechenie-narkoticheskoy-zavisimosti/soli/")
print("SERVICE_STATUS_TITLE", re.search(r"<title>(.*?)</title>", service, re.I | re.S).group(1))
