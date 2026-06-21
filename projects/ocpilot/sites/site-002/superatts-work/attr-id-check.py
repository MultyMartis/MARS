#!/usr/bin/env python3
import re, ssl, urllib.parse, urllib.request, http.cookiejar
from html import unescape

PMA='https://bruma.beget.com/phpMyAdmin'; DB='polygonws_zpm'; DU='polygonws_zpm'; DP='VBCDry2bJ5P'
IDS=[12,13,14,15,21,25,26,28,29,30,33,115]

ctx=ssl.create_default_context(); cj=http.cookiejar.CookieJar()
op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj),urllib.request.HTTPSHandler(context=ctx))
lp=op.open(PMA+'/',timeout=60).read().decode('utf-8','replace')
token=re.search(r'name="token"\s+value="([^"]+)"',lp).group(1)
op.open(urllib.request.Request(PMA+'/index.php',data=urllib.parse.urlencode({'pma_username':DU,'pma_password':DP,'server':'1','target':'index.php','token':token}).encode(),method='POST'),timeout=60)
html=op.open(urllib.request.Request(PMA+'/sql.php',data=urllib.parse.urlencode({'db':DB,'sql_query':'SELECT a.attribute_id,ad.name FROM oc_attribute a JOIN oc_attribute_description ad ON ad.attribute_id=a.attribute_id AND ad.language_id=1 WHERE a.attribute_id IN ('+','.join(map(str,IDS))+') ORDER BY a.attribute_id','token':token,'sql_delimiter':';'}).encode(),method='POST'),timeout=180).read().decode('utf-8','replace')
for m in re.finditer(r'<td[^>]*>(\d+)</td>\s*<td[^>]*>([^<]+)</td>', html):
    print(m.group(1), unescape(m.group(2).strip()))
print('--- bath product attrs ---')
html2=op.open(urllib.request.Request(PMA+'/sql.php',data=urllib.parse.urlencode({'db':DB,'sql_query':"""SELECT a.attribute_id,ad.name,IFNULL(pa.text,'') val FROM oc_attribute a JOIN oc_attribute_description ad ON ad.attribute_id=a.attribute_id AND ad.language_id=1 LEFT JOIN oc_product_attribute pa ON pa.attribute_id=a.attribute_id AND pa.product_id=2448 AND pa.language_id=1 WHERE a.attribute_id IN ("""+','.join(map(str,IDS))+""") ORDER BY a.attribute_id""",'token':token,'sql_delimiter':';'}).encode(),method='POST'),timeout=180).read().decode('utf-8','replace')
for m in re.finditer(r'<td[^>]*>(\d+)</td>\s*<td[^>]*>([^<]+)</td>\s*<td[^>]*>([^<]*)</td>', html2):
    print(m.group(1), unescape(m.group(2).strip()), '|', unescape(m.group(3).strip()))
