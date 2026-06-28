#!/usr/bin/env python3
"""Clear OpenCart cache and verify dealers seo_url on TEST."""
import ftplib
import io
import json
import ssl
import urllib.request

FTP_HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

PATCH = """<?php
require_once __DIR__ . '/config.php';
header('Content-Type: application/json; charset=utf-8');
$mysqli = new mysqli(DB_HOSTNAME, DB_USERNAME, DB_PASSWORD, DB_DATABASE);
$mysqli->set_charset('utf8');
$rows = [];
$r = $mysqli->query("SELECT seo_url_id, store_id, language_id, query, keyword FROM " . DB_PREFIX . "seo_url WHERE keyword='dealers' OR query LIKE '%dealers%' OR query='information_id=10'");
while ($row = $r->fetch_assoc()) { $rows[] = $row; }
$cleared = 0;
$cacheDir = DIR_STORAGE . 'cache/';
foreach (glob($cacheDir . '*') as $f) {
  if (is_file($f)) { @unlink($f); $cleared++; }
}
echo json_encode(['seo_rows'=>$rows,'cache_files_cleared'=>$cleared]);
"""


def ftp_upload(name: str, body: str) -> None:
    ftp = ftplib.FTP(FTP_HOST, timeout=120)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.storbinary("STOR " + name, io.BytesIO(body.encode()))
    ftp.quit()


def ftp_delete(name: str) -> None:
    ftp = ftplib.FTP(FTP_HOST, timeout=120)
    ftp.login(FTP_USER, FTP_PASS)
    try:
        ftp.delete(name)
    except ftplib.error_perm:
        pass
    ftp.quit()


ftp_upload("m916-dealers-cache-clear.php", PATCH)
ctx = ssl.create_default_context()
req = urllib.request.Request(
    "https://zpm.new-site.space/m916-dealers-cache-clear.php",
    headers={"Cookie": "beget=begetok", "User-Agent": "MARS-M9.16-cache"},
)
raw = urllib.request.urlopen(req, context=ctx, timeout=60).read().decode()
print(raw)
ftp_delete("m916-dealers-cache-clear.php")

req2 = urllib.request.Request(
    "https://zpm.new-site.space/dealers",
    headers={"Cookie": "beget=begetok", "User-Agent": "MARS-M9.16-retest"},
)
html = urllib.request.urlopen(req2, context=ctx, timeout=60).read().decode("utf-8", "replace")
print("zpm-dealers-page:", "zpm-dealers-page" in html)
print("zpm-seo:", "zpm-seo" in html)
