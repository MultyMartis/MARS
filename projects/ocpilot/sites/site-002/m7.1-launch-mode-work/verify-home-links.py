#!/usr/bin/env python3
import re
import ssl
import urllib.request

url = "https://zpm.new-site.space/"
h = urllib.request.urlopen(
    urllib.request.Request(url, headers={"User-Agent": "qa"}),
    context=ssl.create_default_context(),
    timeout=60,
).read().decode("utf-8", "replace")

mobile = re.findall(
    r'<li class="zpm-mmenu__item"><a class="zpm-mmenu__link" href="([^"]+)">Каталог</a></li>',
    h,
)
all_links = re.findall(r'class="btn zpm-catalog__all-link"[^>]*href="([^"]+)"', h)
if not all_links:
    all_links = re.findall(r'href="([^"]+)" class="btn zpm-catalog__all-link"', h)
roots = re.findall(r'data-cat-btn[^>]*data-cat="([^"]+)"', h)
print("mobile:", mobile)
print("all_link:", all_links)
print("roots:", roots)
