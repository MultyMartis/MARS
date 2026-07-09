#!/usr/bin/env python3
"""Patch seo_pro getPathByCategory to use category_path table."""
from __future__ import annotations

import io
import re
from pathlib import Path

import ftplib

SECRETS = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
OUT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    r"\SITE-002-PROD-CATEGORY-LARI-REPARENT-IMPLEMENTATION-01\verification\seo_pro.php.patched"
)

OLD = """\t\tif (!isset($path[$category_id])) {
\t\t\t$max_level = 10;

\t\t\t$sql = \"SELECT CONCAT_WS('_'\";
\t\t\tfor ($i = $max_level-1; $i >= 0; --$i) {
\t\t\t\t$sql .= \",t$i.category_id\";
\t\t\t}
\t\t\t$sql .= \") AS path FROM \" . DB_PREFIX . \"category t0\";
\t\t\tfor ($i = 1; $i < $max_level; ++$i) {
\t\t\t\t$sql .= \" LEFT JOIN \" . DB_PREFIX . \"category t$i ON (t$i.category_id = t\" . ($i-1) . \".parent_id)\";
\t\t\t}
\t\t\t$sql .= \" WHERE t0.category_id = '\" . $category_id . \"'\";

\t\t\t$query = $this->db->query($sql);

\t\t\tif (!is_array($path)) $path=array();

\t\t\t$path[$category_id] = 
\t\t\t$query->num_rows ? 
\t\t\t$query->row['path'] : 
\t\t\tfalse;

\t\t\t$this->cache->set('category.seopath', $path);
\t\t}"""

NEW = """\t\tif (!isset($path[$category_id])) {
\t\t\t// SITE-002: use category_path (authoritative after reparent)
\t\t\t$query = $this->db->query(\"SELECT path_id FROM \" . DB_PREFIX . \"category_path WHERE category_id = '\" . (int)$category_id . \"' ORDER BY level ASC\");
\t\t\tif (!is_array($path)) {
\t\t\t\t$path = array();
\t\t\t}
\t\t\tif ($query->num_rows) {
\t\t\t\t$parts = array();
\t\t\t\tforeach ($query->rows as $row) {
\t\t\t\t\t$parts[] = (int)$row['path_id'];
\t\t\t\t}
\t\t\t\t$path[$category_id] = implode('_', $parts);
\t\t\t} else {
\t\t\t\t$path[$category_id] = false;
\t\t\t}
\t\t\t$this->cache->set('category.seopath', $path);
\t\t}"""


def parse(sub: str) -> dict[str, str]:
    text = SECRETS.read_text(encoding="utf-8")
    block = re.search(r"^## PRODUCTION\s*$([\s\S]*?)(?=^## |\Z)", text, re.M).group(1)
    part = re.search(rf"^### {re.escape(sub)}\s*$([\s\S]*?)(?=^### |\Z)", block, re.M).group(1)
    out: dict[str, str] = {}
    key = None
    for line in part.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.endswith(":"):
            key = s[:-1].strip().lower().replace(" ", "_")
            out.setdefault(key, "")
        elif key:
            out[key] = s
    return out


def main() -> None:
    f = parse("FTP / SFTP")
    ftp = ftplib.FTP()
    ftp.connect(f["host"], int(f.get("port") or 21), timeout=120)
    ftp.login(f["username"], f["password"])
    buf = io.BytesIO()
    ftp.retrbinary("RETR /public_html/catalog/controller/startup/seo_pro.php", buf.write)
    content = buf.getvalue().decode("utf-8", "replace")
    if OLD not in content:
        raise RuntimeError("getPathByCategory anchor not found")
    content = content.replace(OLD, NEW, 1)
    OUT.write_text(content, encoding="utf-8")
    ftp.storbinary("STOR /public_html/catalog/controller/startup/seo_pro.php", io.BytesIO(content.encode("utf-8")))
    ftp.quit()
    print("seo_pro.php patched and uploaded")


if __name__ == "__main__":
    main()
