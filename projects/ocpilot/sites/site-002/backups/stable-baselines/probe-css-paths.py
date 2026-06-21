#!/usr/bin/env python3
import ftplib, io, re, ssl, urllib.request, json

BASE = 'https://zpm.new-site.space'
HOST = 'polygonws.beget.tech'
FTP_USER = 'polygonws_zpm'
FTP_PASS = 'RT4uK7VKr&c'

req = urllib.request.Request(BASE+'/', headers={'User-Agent':'css-probe'})
html = urllib.request.urlopen(req, timeout=60).read().decode('utf-8','replace')
css = sorted(set(re.findall(r'href="([^"]+\.css[^"]*)"', html)))
print('CSS on home:')
for c in css:
    print(' ', c)

ftp = ftplib.FTP(HOST, timeout=120)
ftp.login(FTP_USER, FTP_PASS)
# try list stylesheet dir
try:
    ftp.cwd('catalog/view/theme/default/stylesheet')
    print('FTP stylesheet dir:', ftp.nlst())
except Exception as e:
    print('list error', e)
ftp.quit()
