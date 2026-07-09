#!/usr/bin/env python3
"""SITE-002 lari reparent final SEO/url fix — upload patches + cache clear + htaccess."""
from __future__ import annotations

import hashlib
import io
import json
import re
import shlex
import time
from datetime import datetime, timezone
from pathlib import Path

import ftplib
import paramiko

SECRETS = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOY = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    r"\SITE-002-PROD-CATEGORY-LARI-REPARENT-IMPLEMENTATION-01"
)
SEO_LOCAL = DEPLOY / "verification" / "seo_url.php.patched"
CV_LOCAL = DEPLOY / "verification" / "category_visibility.php.patched"
CAT_LOCAL = DEPLOY / "verification" / "category.php.patched"
HTACCESS_LOCAL = DEPLOY / "verification" / "htaccess.patched"

OLD_SITE002_START = "\t\t\t// SITE-002 category_path canonical"
OLD_SITE002_END = "\t\t// Redirect 301   \n\t\t} elseif (isset($this->request->get['route'])"

HELPER_METHODS = """
\tprivate function site002CanonicalCategoryPath($path_value) {
\t\t$path_parts = explode('_', (string)$path_value);
\t\t$leaf_id = (int)array_pop($path_parts);
\t\tif ($leaf_id <= 0) {
\t\t\treturn array();
\t\t}
\t\t$query = $this->db->query("SELECT path_id FROM " . DB_PREFIX . "category_path WHERE category_id = '" . (int)$leaf_id . "' ORDER BY level ASC");
\t\t$canonical_ids = array();
\t\tforeach ($query->rows as $row) {
\t\t\t$canonical_ids[] = (int)$row['path_id'];
\t\t}
\t\treturn $canonical_ids;
\t}

\tprivate function site002CategorySlugTrail(array $category_ids) {
\t\t$slug_parts = array();
\t\tforeach ($category_ids as $category_id) {
\t\t\t$keyword_query = $this->db->query("SELECT keyword FROM " . DB_PREFIX . "seo_url WHERE query = 'category_id=" . (int)$category_id . "' AND store_id = '" . (int)$this->config->get('config_store_id') . "' AND language_id = '" . (int)$this->config->get('config_language_id') . "'");
\t\t\tif ($keyword_query->num_rows && $keyword_query->row['keyword']) {
\t\t\t\t$slug_parts[] = $keyword_query->row['keyword'];
\t\t\t} else {
\t\t\t\treturn array();
\t\t\t}
\t\t}
\t\treturn $slug_parts;
\t}
"""

SITE002_BLOCK = """\t\t\t// SITE-002 category_path canonical v2 (SITE-002-PROD-CATEGORY-LARI-REPARENT-IMPLEMENTATION-01)
\t\t\tif (!empty($this->request->get['path'])) {
\t\t\t\t$canonical_ids = $this->site002CanonicalCategoryPath($this->request->get['path']);
\t\t\t\tif ($canonical_ids) {
\t\t\t\t\t$this->request->get['path'] = implode('_', $canonical_ids);
\t\t\t\t}
\t\t\t\tif (isset($this->request->get['_route_']) && $canonical_ids) {
\t\t\t\t\t$slug_parts = $this->site002CategorySlugTrail($canonical_ids);
\t\t\t\t\tif ($slug_parts) {
\t\t\t\t\t\t$expected_route = 'katalog/' . implode('/', $slug_parts);
\t\t\t\t\t\t$actual_route = trim($this->request->get['_route_'], '/');
\t\t\t\t\t\tif ($expected_route !== $actual_route && substr_count($expected_route, '/') > substr_count($actual_route, '/')) {
\t\t\t\t\t\t\t$this->response->redirect($expected_route, 301);
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t}
\t\t\t\tif (!empty($this->request->get['path']) && isset($this->request->get['route']) && $this->request->get['route'] == 'product/katalog') {
\t\t\t\t\t$this->request->get['route'] = 'product/category';
\t\t\t\t}
\t\t\t}
"""

REDIRECT_BLOCK = """# SITE-002 lari reparent redirects (SITE-002-PROD-CATEGORY-LARI-REPARENT-IMPLEMENTATION-01)
RewriteRule ^katalog/nejtralnoe-oborudovanie/lari/(.+)$ /katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari/$1 [R=301,L]
RewriteRule ^katalog/nejtralnoe-oborudovanie/lari/?$ /katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari [R=301,L]
"""


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


def ftp_download(remote: str) -> str:
    f = parse("FTP / SFTP")
    ftp = ftplib.FTP()
    ftp.connect(f["host"], int(f.get("port") or 21), timeout=180)
    ftp.login(f["username"], f["password"])
    buf = io.BytesIO()
    ftp.retrbinary(f"RETR {remote}", buf.write)
    ftp.quit()
    return buf.getvalue().decode("utf-8", "replace")


def ftp_upload(remote: str, data: bytes) -> str:
    f = parse("FTP / SFTP")
    ftp = ftplib.FTP()
    ftp.connect(f["host"], int(f.get("port") or 21), timeout=180)
    ftp.login(f["username"], f["password"])
    ftp.storbinary(f"STOR {remote}", io.BytesIO(data))
    ftp.quit()
    return hashlib.sha256(data).hexdigest()


def patch_seo_url(content: str) -> str:
    start = content.find(OLD_SITE002_START)
    if start == -1:
        raise RuntimeError("SITE-002 block start not found in seo_url.php")
    end = content.find(OLD_SITE002_END, start)
    if end == -1:
        raise RuntimeError("SITE-002 block end anchor not found")
    content = content[:start] + SITE002_BLOCK + content[end:]

  # Fix elseif product/category branch
    old_branch = """\t\t\t} elseif ($this->request->get['route'] == 'product/category' && isset($this->request->get['path'])) {
\t\t\t\t$categorys_id = explode('_', $this->request->get['path']);
\t\t\t\t$cat_path = '';
\t\t\t\tforeach ($categorys_id as $category_id) {"""
    new_branch = """\t\t\t} elseif ($this->request->get['route'] == 'product/category' && isset($this->request->get['path'])) {
\t\t\t\t$canonical_ids = $this->site002CanonicalCategoryPath($this->request->get['path']);
\t\t\t\tif ($canonical_ids) {
\t\t\t\t\t$this->request->get['path'] = implode('_', $canonical_ids);
\t\t\t\t}
\t\t\t\t$categorys_id = $canonical_ids ? $canonical_ids : explode('_', (string)$this->request->get['path']);
\t\t\t\t$cat_path = '';
\t\t\t\tforeach ($categorys_id as $category_id) {"""
    if old_branch not in content:
        raise RuntimeError("seo_url elseif branch anchor not found")
    content = content.replace(old_branch, new_branch, 1)

    content = content.replace(
        "\t\t\t} elseif ($cat_path) {\n\t\t\t\t$this->response->redirect($arg, 301);",
        "\t\t\t} elseif ($cat_path) {\n\t\t\t\t$this->response->redirect('katalog/' . $arg, 301);",
        1,
    )

    old_rewrite_path = """\t\t\t\t} elseif ($key == 'path') {
\t\t\t\t\t$categories = explode('_', $value);

\t\t\t\t\tforeach ($categories as $category) {"""
    new_rewrite_path = """\t\t\t\t} elseif ($key == 'path') {
\t\t\t\t\t$canonical_ids = $this->site002CanonicalCategoryPath($value);
\t\t\t\t\t$categories = $canonical_ids ? $canonical_ids : explode('_', $value);

\t\t\t\t\tforeach ($categories as $category) {"""
    if old_rewrite_path not in content:
        raise RuntimeError("seo_url rewrite path anchor not found")
    content = content.replace(old_rewrite_path, new_rewrite_path, 1)

    if "function site002CanonicalCategoryPath" not in content:
        content = content.replace("\n}\n", HELPER_METHODS + "\n}\n", 1)
    return content


def patch_category_links(content: str) -> str:
    replacements = [
        (
            "$this->url->link('product/category', 'path=' . $visibility->buildCategoryPathParam($this, (int)$category_info['category_id']))",
            "$this->url->link('product/katalog', 'path=' . $visibility->buildCategoryPathParam($this, (int)$category_info['category_id']))",
        ),
        (
            "$this->url->link('product/category', 'path=' . $visibility->buildCategoryPathParam($this, $branch_id))",
            "$this->url->link('product/katalog', 'path=' . $visibility->buildCategoryPathParam($this, $branch_id))",
        ),
    ]
    for old, new in replacements:
        if old not in content:
            raise RuntimeError(f"category.php anchor missing: {old[:60]}")
        content = content.replace(old, new)
    return content


def patch_visibility(content: str) -> str:
    old = "$controller->url->link('product/category', 'path=' . $this->buildCategoryPathParam($controller, $branch_id))"
    new = "$controller->url->link('product/katalog', 'path=' . $this->buildCategoryPathParam($controller, $branch_id))"
    if old not in content:
        raise RuntimeError("category_visibility homepage href anchor missing")
    return content.replace(old, new, 1)


def patch_htaccess(content: str) -> str:
    marker = "# SITE-002 lari reparent redirects"
    if marker in content:
        lines = content.splitlines()
        out = []
        skip = False
        for ln in lines:
            if marker in ln:
                skip = True
                continue
            if skip and ln.startswith("RewriteRule ^katalog/nejtralnoe-oborudovanie/lari"):
                continue
            if skip and ln.strip() == "":
                skip = False
                continue
            if skip:
                continue
            out.append(ln)
        content = "\n".join(out) + "\n"
    insert_at = content.find("RewriteEngine On")
    line_end = content.find("\n", insert_at)
    return content[: line_end + 1] + "\n" + REDIRECT_BLOCK + content[line_end + 1 :]


def ssh_exec(cmd: str) -> str:
    ssh = parse("SSH")
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(
        ssh["host"],
        port=int(ssh.get("port") or 22),
        username=ssh["username"],
        password=ssh["password"],
        timeout=60,
        allow_agent=False,
        look_for_keys=False,
    )
    _i, o, e = c.exec_command(cmd, timeout=180)
    out = o.read().decode() + e.read().decode()
    c.close()
    return out


def clear_cache() -> str:
    # Scoped cache clear: cat-list-header + general cache folder
    cmds = [
        "cd /home/*/bzpm.ru/storage/cache 2>/dev/null || cd /bzpm.ru/storage/cache 2>/dev/null || cd /storage/cache 2>/dev/null; pwd; ls cache.cat-list-header 2>/dev/null; rm -f cache.cat-list-header 2>/dev/null; find . -maxdepth 1 -type f -name 'cache.*' -delete 2>/dev/null; echo CACHE_CLEARED",
    ]
    return ssh_exec("bash -lc " + shlex.quote("; ".join(cmds)))


def http_probe(url: str) -> dict:
    import subprocess

    r = subprocess.run(
        ["curl", "-sI", "-H", "Cache-Control: no-cache", url],
        capture_output=True,
        text=True,
        timeout=60,
    )
    status = ""
    location = ""
    for ln in r.stdout.splitlines():
        if ln.startswith("HTTP/"):
            status = ln.strip()
        if ln.lower().startswith("location:"):
            location = ln.split(":", 1)[1].strip()
    return {"url": url, "status": status, "location": location}


def main() -> None:
    DEPLOY.mkdir(parents=True, exist_ok=True)
    (DEPLOY / "verification").mkdir(parents=True, exist_ok=True)

    seo = ftp_download("/public_html/catalog/controller/startup/seo_url.php")
    cv = ftp_download("/public_html/system/library/zpm/category_visibility.php")
    cat = ftp_download("/public_html/catalog/controller/product/category.php")
    ht = ftp_download("/public_html/.htaccess")

    seo_p = patch_seo_url(seo)
    cv_p = patch_visibility(cv)
    cat_p = patch_category_links(cat)
    ht_p = patch_htaccess(ht)

    SEO_LOCAL.write_text(seo_p, encoding="utf-8")
    CV_LOCAL.write_text(cv_p, encoding="utf-8")
    CAT_LOCAL.write_text(cat_p, encoding="utf-8")
    HTACCESS_LOCAL.write_text(ht_p, encoding="utf-8")

    manifest = []
    for remote, local in [
        ("/public_html/catalog/controller/startup/seo_url.php", SEO_LOCAL),
        ("/public_html/system/library/zpm/category_visibility.php", CV_LOCAL),
        ("/public_html/catalog/controller/product/category.php", CAT_LOCAL),
        ("/public_html/.htaccess", HTACCESS_LOCAL),
    ]:
        sha = ftp_upload(remote, local.read_bytes())
        manifest.append({"remote": remote, "sha256": sha})
        time.sleep(0.5)

    cache_log = clear_cache()

    probes = [
        http_probe("https://bzpm.ru/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari"),
        http_probe("https://bzpm.ru/katalog/nejtralnoe-oborudovanie/lari"),
        http_probe("https://bzpm.ru/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari/skladskie-lari"),
        http_probe("https://bzpm.ru/katalog/nejtralnoe-oborudovanie/lari/skladskie-lari"),
        http_probe("https://bzpm.ru/"),
    ]

    out = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "uploads": manifest,
        "cache_clear": cache_log.strip(),
        "http_probes": probes,
    }
    (DEPLOY / "verification" / "final-fix-result.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
