import re
import urllib.request

url = "https://zpm.new-site.space/stoly-serii-premium/stoly/"
html = urllib.request.urlopen(
    urllib.request.Request(url, headers={"User-Agent": "MARS"}), timeout=60
).read().decode("utf-8")

benefits = len(re.findall(r'<li class="zpm-commercial-trust__benefit"', html))
services = len(re.findall(r'<div class="zpm-commercial-trust__service"', html))
title = re.search(r'zpm-commercial-trust__title[^>]*>([^<]+)', html).group(1)
print({"benefits": benefits, "services": services, "title": title})
