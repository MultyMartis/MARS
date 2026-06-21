#!/usr/bin/env python3
"""M9.8.9-09A — filter/limit/sort/pagination persistence hotfix: capture, backup, patch, deploy."""
from __future__ import annotations

import ftplib
import hashlib
import io
import json
from datetime import datetime, timezone
from pathlib import Path

FTP_HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

ROOT = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002")
WORK_DIR = ROOT / "reports" / "m9.8.9-09a-work"
CAPTURE_DIR = WORK_DIR / "live-capture"

FILES = [
    {
        "remote": "assets/js/main.js",
        "local": "assets__js__main.js",
        "backup": ROOT / "backups" / "main.js.pre-m9.8.9-09a-filter-limit-persistence.bak",
        "patched": "assets__js__main.js.patched",
        "patch_fn": "patch_main_js",
    },
    {
        "remote": "catalog/controller/product/category.php",
        "local": "catalog__controller__product__category.php",
        "backup": ROOT / "backups" / "category.php.pre-m9.8.9-09a-filter-limit-persistence.bak",
        "patched": "catalog__controller__product__category.php.patched",
        "patch_fn": "patch_category_php",
    },
]

JS_OLD = """function updateBrowserUrl(form) {
  const stateText = getReadableState(form);
  const newUrl = stateText
    ? window.location.pathname + "?filters=" + stateText
    : window.location.pathname;

  window.history.replaceState(null, "", newUrl);
  // Вызываем обновление товаров
  const root = form.closest("[data-filters]");
  debouncedUpdate(root);
}"""

JS_NEW = """function updateBrowserUrl(form) {
  const stateText = getReadableState(form);
  const params = new URLSearchParams(window.location.search);

  if (stateText) {
    params.set("filters", stateText);
  } else {
    params.delete("filters");
  }

  const query = params.toString();
  const newUrl = query
    ? window.location.pathname + "?" + query
    : window.location.pathname;

  window.history.replaceState(null, "", newUrl);
  // Вызываем обновление товаров
  const root = form.closest("[data-filters]");
  debouncedUpdate(root);
}"""

PHP_FILTERS_SNIPPET = """
\t\t\tif (isset($this->request->get['filters'])) {
\t\t\t\t$url .= '&filters=' . $this->request->get['filters'];
\t\t\t}
"""

PHP_SORTS_ANCHOR = """\t\t\tif (isset($this->request->get['limit'])) {
\t\t\t\t$url .= '&limit=' . $this->request->get['limit'];
\t\t\t}

\t\t\t$data['sorts'] = array();"""

PHP_SORTS_REPLACEMENT = """\t\t\tif (isset($this->request->get['limit'])) {
\t\t\t\t$url .= '&limit=' . $this->request->get['limit'];
\t\t\t}

\t\t\tif (isset($this->request->get['filters'])) {
\t\t\t\t$url .= '&filters=' . $this->request->get['filters'];
\t\t\t}

\t\t\t$data['sorts'] = array();"""

PHP_LIMITS_ANCHOR = """\t\t\tif (isset($this->request->get['order'])) {
\t\t\t\t$url .= '&order=' . $this->request->get['order'];
\t\t\t}

\t\t\t$data['limits'] = array();"""

PHP_LIMITS_REPLACEMENT = """\t\t\tif (isset($this->request->get['order'])) {
\t\t\t\t$url .= '&order=' . $this->request->get['order'];
\t\t\t}

\t\t\tif (isset($this->request->get['filters'])) {
\t\t\t\t$url .= '&filters=' . $this->request->get['filters'];
\t\t\t}

\t\t\t$data['limits'] = array();"""

PHP_PAGINATION_ANCHOR = """\t\t\tif (isset($this->request->get['limit'])) {
\t\t\t\t$url .= '&limit=' . $this->request->get['limit'];
\t\t\t}

\t\t\t$pagination = new Pagination();"""

PHP_PAGINATION_REPLACEMENT = """\t\t\tif (isset($this->request->get['limit'])) {
\t\t\t\t$url .= '&limit=' . $this->request->get['limit'];
\t\t\t}

\t\t\tif (isset($this->request->get['filters'])) {
\t\t\t\t$url .= '&filters=' . $this->request->get['filters'];
\t\t\t}

\t\t\t$pagination = new Pagination();"""


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def ftp_connect() -> ftplib.FTP:
    ftp = ftplib.FTP(FTP_HOST, timeout=180)
    ftp.login(FTP_USER, FTP_PASS)
    return ftp


def ftp_download(remote_path: str) -> bytes:
    ftp = ftp_connect()
    bio = io.BytesIO()
    ftp.retrbinary("RETR " + remote_path, bio.write)
    ftp.quit()
    return bio.getvalue()


def ftp_upload(remote_path: str, data: bytes) -> None:
    ftp = ftp_connect()
    bio = io.BytesIO(data)
    ftp.storbinary("STOR " + remote_path, bio)
    ftp.quit()


def clear_twig_cache() -> list[str]:
    cleared: list[str] = []
    try:
        ftp = ftp_connect()
        try:
            ftp.cwd("system/storage/cache/template")
            for name in ftp.nlst():
                if name in (".", ".."):
                    continue
                try:
                    ftp.delete(name)
                    cleared.append(name)
                except ftplib.error_perm:
                    pass
        except ftplib.error_perm:
            pass
        ftp.quit()
    except Exception:
        pass
    return cleared


def patch_main_js(content: str) -> str:
    if "new URLSearchParams(window.location.search)" in content and "params.delete(\"filters\")" in content:
        raise RuntimeError("main.js patch already applied (URLSearchParams filters persistence present)")

    if JS_OLD not in content:
        raise RuntimeError("updateBrowserUrl block not found in main.js")

    return content.replace(JS_OLD, JS_NEW, 1)


def patch_category_php(content: str) -> str:
    if content.count("$url .= '&filters=' . $this->request->get['filters'];") >= 3:
        raise RuntimeError("category.php patch already applied (filters in URL blocks present)")

    for anchor, replacement, label in [
        (PHP_SORTS_ANCHOR, PHP_SORTS_REPLACEMENT, "sorts URL block"),
        (PHP_LIMITS_ANCHOR, PHP_LIMITS_REPLACEMENT, "limits URL block"),
        (PHP_PAGINATION_ANCHOR, PHP_PAGINATION_REPLACEMENT, "pagination URL block"),
    ]:
        if anchor not in content:
            raise RuntimeError(f"category.php anchor not found: {label}")
        content = content.replace(anchor, replacement, 1)

    return content


PATCH_FNS = {
    "patch_main_js": patch_main_js,
    "patch_category_php": patch_category_php,
}


def main() -> None:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    WORK_DIR.mkdir(parents=True, exist_ok=True)
    CAPTURE_DIR.mkdir(parents=True, exist_ok=True)
    ROOT.joinpath("backups").mkdir(parents=True, exist_ok=True)

    manifest_pre: dict = {
        "task": "M9.8.9-09A",
        "authority": "SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01",
        "stamp": stamp,
        "phase": "pre-deploy",
        "files": [],
    }

    deploy_results: list[dict] = []

    for spec in FILES:
        remote = spec["remote"]
        capture_path = CAPTURE_DIR / spec["local"]
        patched_path = WORK_DIR / spec["patched"]
        patch_fn = PATCH_FNS[spec["patch_fn"]]

        live_raw = ftp_download(remote)
        live_sha = sha256_hex(live_raw)
        capture_path.write_bytes(live_raw)
        spec["backup"].write_bytes(live_raw)

        live_text = live_raw.decode("utf-8")
        patched_text = patch_fn(live_text)
        patched_raw = patched_text.encode("utf-8")
        patched_sha = sha256_hex(patched_raw)
        patched_path.write_bytes(patched_raw)

        file_entry = {
            "remote_path": remote,
            "capture": str(capture_path),
            "backup": str(spec["backup"]),
            "patched_local": str(patched_path),
            "sha256_pre": live_sha,
            "sha256_patched": patched_sha,
            "size_pre": len(live_raw),
            "size_patched": len(patched_raw),
        }
        manifest_pre["files"].append(file_entry)

        ftp_upload(remote, patched_raw)

        verify_raw = ftp_download(remote)
        verify_sha = sha256_hex(verify_raw)
        file_entry["verify_sha256"] = verify_sha
        file_entry["deploy_ok"] = verify_sha == patched_sha
        deploy_results.append(file_entry)

    cache_cleared = clear_twig_cache()

    manifest_post = {
        **manifest_pre,
        "phase": "post-deploy",
        "twig_cache_cleared": cache_cleared,
        "all_deploy_ok": all(f["deploy_ok"] for f in deploy_results),
    }

    manifest_pre_path = WORK_DIR / f"manifest-pre-{stamp}.json"
    manifest_post_path = WORK_DIR / f"manifest-post-{stamp}.json"
    manifest_pre_path.write_text(
        json.dumps(manifest_pre, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    manifest_post_path.write_text(
        json.dumps(manifest_post, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print(json.dumps(manifest_post, indent=2, ensure_ascii=False))
    if not manifest_post["all_deploy_ok"]:
        raise SystemExit("Deploy verification failed for one or more files")


if __name__ == "__main__":
    main()
