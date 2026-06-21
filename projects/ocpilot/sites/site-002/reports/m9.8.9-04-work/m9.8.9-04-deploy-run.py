#!/usr/bin/env python3
"""M9.8.9-04 — filter scroll offset fix: capture, backup, patch main.js, deploy."""
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
REMOTE_PATH = "assets/js/main.js"

ROOT = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002")
WORK_DIR = ROOT / "reports" / "m9.8.9-04-work"
CAPTURE_DIR = WORK_DIR / "live-capture"
CAPTURE_PATH = CAPTURE_DIR / "assets__js__main.js"
BACKUP_PATH = ROOT / "backups" / "main.js.pre-m9.8.9-04-filter-scroll-offset.bak"
PATCHED_PATH = WORK_DIR / "assets__js__main.js.patched"

OLD_SCROLL = "      grid.scrollIntoView({ behavior: 'smooth', block: 'start' });"

NEW_SCROLL = "      scrollToCategorySection();"

SCROLL_HELPERS = """  function getPageScrollOffset() {
    var isMobile = window.innerWidth <= 1024;
    var stickyEl = isMobile
      ? document.querySelector('[data-header-mobilebar]')
      : document.querySelector('[data-header-sticky]');

    if (stickyEl) {
      var measured = Math.ceil(stickyEl.getBoundingClientRect().height);
      if (measured > 0) {
        return measured;
      }
    }

    var cssVal = getComputedStyle(document.documentElement)
      .getPropertyValue('--header-posotopn-and-size')
      .trim();
    var parsed = parseInt(cssVal, 10);
    if (!isNaN(parsed) && parsed > 0) {
      return parsed;
    }

    return isMobile ? 100 : 140;
  }

  function getPageScrollTop() {
    if (document.body.classList.contains('is-scroll-locked')) {
      var top = parseInt(document.body.style.top || '0', 10) || 0;
      return Math.abs(top);
    }

    return (
      window.pageYOffset ||
      document.documentElement.scrollTop ||
      0
    );
  }

  function scrollToCategorySection() {
    var target =
      document.querySelector('.page--category section.category') ||
      document.querySelector('section.category');
    if (!target) return;

    if (document.documentElement.classList.contains('is-filter-open')) {
      var closeBtn = document.querySelector('[data-filter-close]');
      if (closeBtn) closeBtn.click();
    }

    var offset = getPageScrollOffset();
    var scrollTop = getPageScrollTop();
    var targetTop =
      target.getBoundingClientRect().top +
      scrollTop -
      offset;

    window.scrollTo({
      top: Math.max(0, targetTop),
      behavior: 'smooth'
    });
  }

"""

ANCHOR = "  /**\n * Основная функция обновления товаров\n */\nfunction updateProducts(root) {"


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


def apply_patch(content: str) -> str:
    if OLD_SCROLL not in content:
        raise RuntimeError("Expected grid.scrollIntoView anchor not found in live main.js")
    if "function scrollToCategorySection()" in content:
        raise RuntimeError("Patch already applied (scrollToCategorySection present)")
    if ANCHOR not in content:
        raise RuntimeError("Expected updateProducts anchor not found")
    content = content.replace(ANCHOR, SCROLL_HELPERS + ANCHOR, 1)
    content = content.replace(OLD_SCROLL, NEW_SCROLL, 1)
    return content


def main() -> None:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    WORK_DIR.mkdir(parents=True, exist_ok=True)
    CAPTURE_DIR.mkdir(parents=True, exist_ok=True)
    ROOT.joinpath("backups").mkdir(parents=True, exist_ok=True)

    live_raw = ftp_download(REMOTE_PATH)
    live_sha = sha256_hex(live_raw)
    CAPTURE_PATH.write_bytes(live_raw)
    BACKUP_PATH.write_bytes(live_raw)

    live_text = live_raw.decode("utf-8")
    patched_text = apply_patch(live_text)
    patched_raw = patched_text.encode("utf-8")
    patched_sha = sha256_hex(patched_raw)
    PATCHED_PATH.write_bytes(patched_raw)

    manifest_pre = {
        "task": "M9.8.9-04",
        "authority": "SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01",
        "stamp": stamp,
        "remote_path": REMOTE_PATH,
        "phase": "pre-deploy",
        "capture": str(CAPTURE_PATH),
        "backup": str(BACKUP_PATH),
        "sha256": live_sha,
        "size": len(live_raw),
        "patch": {
            "type": "js-scroll-offset",
            "file": "main.js",
            "change": "After filter AJAX: scroll section.category with header offset (not .category__grid scrollIntoView)",
        },
    }
    manifest_pre_path = WORK_DIR / f"manifest-pre-{stamp}.json"
    manifest_pre_path.write_text(
        json.dumps(manifest_pre, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    ftp_upload(REMOTE_PATH, patched_raw)

    verify_raw = ftp_download(REMOTE_PATH)
    verify_sha = sha256_hex(verify_raw)

    manifest_post = {
        **manifest_pre,
        "phase": "post-deploy",
        "patched_local": str(PATCHED_PATH),
        "patched_sha256": patched_sha,
        "verify_sha256": verify_sha,
        "deploy_ok": verify_sha == patched_sha,
    }
    manifest_post_path = WORK_DIR / f"manifest-post-{stamp}.json"
    manifest_post_path.write_text(
        json.dumps(manifest_post, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print(json.dumps(manifest_post, indent=2, ensure_ascii=False))
    if not manifest_post["deploy_ok"]:
        raise SystemExit("Deploy verification failed: live SHA != patched SHA")


if __name__ == "__main__":
    main()
