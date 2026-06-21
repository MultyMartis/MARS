#!/usr/bin/env python3
import ftplib
import hashlib
import io
import json
import os
import re
import urllib.request

HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"
BASELINE_CSS_SHA = "0a6e8d4e2035ba12a2095966213a6d5669260203a806efd62ab00c876c405ef6"
SPKB_URL = (
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
    "stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/"
    "stol-tumba-spkb-18-7-vl5-1800h700h850"
)

def ftp_download(remote_path):
    ftp = ftplib.FTP(HOST, timeout=120)
    ftp.login(FTP_USER, FTP_PASS)
    bio = io.BytesIO()
    ftp.retrbinary("RETR " + remote_path, bio.write)
    try:
        ftp.quit()
    except EOFError:
        pass
    return bio.getvalue()

req = urllib.request.Request(SPKB_URL, headers={"Cookie": "beget=begetok"})
html = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")
primary = re.search(
    r'<dl class="product-hero__props product-hero__props--primary">(.*?)</dl>',
    html,
    re.S,
)
primary_html = primary.group(1) if primary else ""
css = ftp_download("assets/css/style.css")
twig = ftp_download("catalog/view/theme/default/template/product/producthero.twig")

checks = {}
for label, icon in [
    ("Длина", "fal fa-ruler-horizontal"),
    ("Ширина", "fal fa-arrows-alt-h"),
    ("Высота", "fal fa-arrows-alt-v"),
    ("Масса", "fas fa-weight-hanging"),
]:
    m = re.search(
        rf'product-hero__prop--primary.*?<i class="([^"]+)".*?<dt>[^<]*{label}',
        primary_html,
        re.S | re.I,
    )
    checks[label] = {"expected": icon, "actual": m.group(1) if m else None, "ok": bool(m and m.group(1) == icon)}

out = {
    "php_ok": "Fatal error" not in html and "Parse error" not in html,
    "icon_checks": checks,
    "all_icons_ok": all(v["ok"] for v in checks.values()),
    "style_css_sha256": hashlib.sha256(css).hexdigest(),
    "style_css_unchanged": hashlib.sha256(css).hexdigest() == BASELINE_CSS_SHA,
    "twig_has_conditional": b"prop_name = a.name|lower" in twig,
    "twig_no_fad_primary": b"fad fa-weight-hanging" not in twig,
    "cart_intact": "data-cart-add" in html,
    "qty_intact": "data-cart-qty" in html,
    "wishlist_intact": "data-fav-toggle" in html,
    "compare_intact": "data-compare-toggle" in html,
    "fancybox_intact": "data-fancybox" in html,
    "gallery_intact": "js-product-gallery" in html,
    "primary_sample": primary_html[:1200],
}
print(json.dumps(out, ensure_ascii=False, indent=2))
