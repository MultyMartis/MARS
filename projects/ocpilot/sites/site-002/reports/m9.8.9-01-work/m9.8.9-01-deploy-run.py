#!/usr/bin/env python3
"""M9.8.9-01 — wishlist/compare smart titles + tip dedup."""
from __future__ import annotations

import ftplib
import hashlib
import io
import json
import re
from datetime import datetime, timezone
from pathlib import Path

FTP_HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"
REMOTE_PATH = "assets/js/main.js"

ROOT = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002")
WORK_DIR = ROOT / "reports" / "m9.8.9-01-work"
CAPTURE_DIR = WORK_DIR / "live-capture"
CAPTURE_PATH = CAPTURE_DIR / "assets__js__main.js"
BACKUP_PATH = ROOT / "backups" / "main.js.pre-m9.8.9-01-wishlist-compare-tooltips.bak"
PATCHED_PATH = WORK_DIR / "assets__js__main.js.patched"

OLD_BLOCK = """(function () {
  const SHOW_TIME = 3000;

  function showTip(el, text, isRemove) {
    const body = el.querySelector('.zpm-tip__body');
    if (body) body.textContent = text;

    el.classList.remove('is-tip', 'is-remove');

    if (isRemove) {
      el.classList.add('is-remove');
    }

    // restart animation
    // eslint-disable-next-line no-unused-expressions
    el.offsetHeight;

    el.classList.add('is-tip');

    clearTimeout(el._tipTimer);
    el._tipTimer = setTimeout(() => {
      el.classList.remove('is-tip', 'is-remove');
    }, SHOW_TIME);
  }"""

NEW_BLOCK = """(function () {
  const SHOW_TIME = 3000;
  const TITLE_FAV_ADD = 'Добавить в избранное';
  const TITLE_FAV_REMOVE = 'Удалить из избранного';
  const TITLE_COMPARE_ADD = 'Добавить к сравнению';
  const TITLE_COMPARE_REMOVE = 'Удалить из сравнения';
  const ACTION_SELECTOR = '[data-fav-toggle], [data-compare-toggle]';

  function updateActionTitle(btn) {
    const isFav = btn.hasAttribute('data-fav-toggle');
    const isActive = btn.classList.contains('active');
    let title;

    if (isFav) {
      title = isActive ? TITLE_FAV_REMOVE : TITLE_FAV_ADD;
    } else {
      title = isActive ? TITLE_COMPARE_REMOVE : TITLE_COMPARE_ADD;
    }

    btn.setAttribute('title', title);
  }

  function initActionTitles() {
    document.querySelectorAll(ACTION_SELECTOR).forEach(updateActionTitle);
  }

  function hideAllActionTips(exceptEl) {
    document.querySelectorAll(ACTION_SELECTOR).forEach((node) => {
      if (node === exceptEl) return;
      node.classList.remove('is-tip', 'is-remove');
      clearTimeout(node._tipTimer);
    });
  }

  function showTip(el, text, isRemove) {
    hideAllActionTips(el);

    const body = el.querySelector('.zpm-tip__body');
    if (body) body.textContent = text;

    el.classList.remove('is-tip', 'is-remove');

    if (isRemove) {
      el.classList.add('is-remove');
    }

    // restart animation
    // eslint-disable-next-line no-unused-expressions
    el.offsetHeight;

    el.classList.add('is-tip');

    clearTimeout(el._tipTimer);
    el._tipTimer = setTimeout(() => {
      el.classList.remove('is-tip', 'is-remove');
    }, SHOW_TIME);
  }"""

OLD_TOGGLE_TAIL = """  const newState = btn.classList.toggle('active');
  showTip(btn, newState ? 'Добавлено' : 'Удалено', !newState);

  });
})();"""

NEW_TOGGLE_TAIL = """  const newState = btn.classList.toggle('active');
  updateActionTitle(btn);
  showTip(btn, newState ? 'Добавлено' : 'Удалено', !newState);

  });

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initActionTitles);
  } else {
    initActionTitles();
  }
})();"""


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
    if "TITLE_FAV_ADD" in content:
        raise RuntimeError("Patch already applied (TITLE_FAV_ADD present)")
    if OLD_BLOCK not in content:
        raise RuntimeError("Expected FAVORITES/COMPARE block not found")
    if OLD_TOGGLE_TAIL not in content:
        raise RuntimeError("Expected toggle tail not found")
    content = content.replace(OLD_BLOCK, NEW_BLOCK, 1)
    content = content.replace(OLD_TOGGLE_TAIL, NEW_TOGGLE_TAIL, 1)
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
        "task": "M9.8.9-01",
        "authority": "SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01",
        "stamp": stamp,
        "remote_path": REMOTE_PATH,
        "phase": "pre-deploy",
        "capture": str(CAPTURE_PATH),
        "backup": str(BACKUP_PATH),
        "sha256": live_sha,
        "size": len(live_raw),
        "patch": {
            "type": "js-wishlist-compare-smart-titles",
            "file": "main.js",
            "changes": [
                "native title on fav/compare buttons (add/remove states)",
                "init titles on DOMContentLoaded",
                "hide previous fav/compare popup before showing new one",
            ],
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
