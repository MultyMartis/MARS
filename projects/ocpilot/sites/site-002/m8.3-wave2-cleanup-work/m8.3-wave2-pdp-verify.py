#!/usr/bin/env python3
"""Quick PDP verify after M8.3 Wave 2."""
import ssl
import urllib.request

PDP = (
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
    "stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/"
    "stol-tumba-spkb-18-7-vl5-1800h700h850"
)
ctx = ssl.create_default_context()
req = urllib.request.Request(PDP, headers={"User-Agent": "BZPM-M8.3-W2-PDP"})
resp = urllib.request.urlopen(req, timeout=60, context=ctx)
body = resp.read().decode("utf-8", "replace")
print("status", resp.status)
print("php_errors", any(x in body for x in ("Fatal error", "Parse error", "Uncaught")))
print("has_specs", "product-specs" in body or "specifications" in body.lower())
print("packaging_on_pdp_may_exist", "упаковк" in body.lower() or "Упаковка" in body)
