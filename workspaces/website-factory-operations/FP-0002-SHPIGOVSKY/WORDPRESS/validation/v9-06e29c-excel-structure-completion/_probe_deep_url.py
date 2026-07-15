import urllib.request

url = "http://shpigovsky.test/uslugi/zavisimosti/lechenie-narkoticheskoy-zavisimosti/soli/"
req = urllib.request.Request(url, headers={"User-Agent": "e29c"})
body = urllib.request.urlopen(req, timeout=20).read().decode("utf-8", "replace")
print("len", len(body))
print("has leaf main", "page-service-leaf-v1" in body)
print("has subdivision", "page-service-subdivision-v1" in body)
print("has 404", "404" in body[:2000])
print("title snippet", body[body.find("<title"):body.find("</title>")+8] if "<title" in body else "no title")
