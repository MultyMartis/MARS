import re, ssl, urllib.request
for path in [
    "/katalog/nejtralnoe-oborudovanie/stoly/",
    "/katalog/nejtralnoe-oborudovanie/moechnye-vanny/",
]:
    u = "https://zpm.new-site.space" + path
    h = urllib.request.urlopen(u, context=ssl.create_default_context(), timeout=60).read().decode("utf-8", "replace")
    print("===", path, "===")
    print("len", len(h))
    for pat in ["flt__group", "flt__", "data-filter", "filters-form", "name=\"attr[", "price_from", "only_with_price"]:
        print(pat, h.count(pat))
    m = re.search(r'(<form[^>]*filter[^>]*>.*?</form>)', h, re.S | re.I)
    if not m:
        m = re.search(r'(<aside[^>]*>.*?</aside>)', h, re.S)
    if m:
        snippet = m.group(1)[:4000]
        print("SNIPPET:\n", snippet)
    print()
