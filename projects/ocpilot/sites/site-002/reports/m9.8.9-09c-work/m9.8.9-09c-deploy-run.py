#!/usr/bin/env python3
"""M9.8.9-09C — limit toolbar AJAX refresh hotfix: capture, backup, patch, deploy."""
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
WORK_DIR = ROOT / "reports" / "m9.8.9-09c-work"
CAPTURE_DIR = WORK_DIR / "live-capture"

REMOTE = "assets/js/main.js"
LOCAL = "assets__js__main.js"
BACKUP = ROOT / "backups" / "main.js.pre-m9.8.9-09c-limit-ajax-refresh.bak"
PATCHED = "assets__js__main.js.patched"

UPDATE_PRODUCTS_OLD = """      } else {
        // Если в новом HTML пагинации нет (товаров мало)
        if (oldPagination) {
          oldPagination.remove(); // Удаляем старую, если она была
        }
      }


      grid.style.opacity = "1";"""

UPDATE_PRODUCTS_NEW = """      } else {
        // Если в новом HTML пагинации нет (товаров мало)
        if (oldPagination) {
          oldPagination.remove(); // Удаляем старую, если она была
        }
      }

      // 3. Обновляем limit control (актуальные href с filters из AJAX-ответа)
      const oldLimit = document.querySelector(".category__limit");
      const newLimit = doc.querySelector(".category__limit");
      if (newLimit && oldLimit) {
        oldLimit.outerHTML = newLimit.outerHTML;
        initCategoryLimitMenu();
      }

      grid.style.opacity = "1";"""

INIT_PAGINATION_ANCHOR = """/**
 * Перехват кликов по пагинации
 */
function initPaginationAJAX(root) {"""

INIT_LIMIT_MENU_FN = """/**
 * Dropdown «Показывать по» — init/re-init после AJAX limit refresh
 */
function initCategoryLimitMenu() {
  const limitContainer = document.querySelector(".category__limit");
  if (!limitContainer) return;

  let toggleBtn = limitContainer.querySelector("[data-limit-open]");
  const menu = limitContainer.querySelector("[data-limit-menu]");
  const sortContainer = document.querySelector(".category__sort");
  const sortToggleBtn = sortContainer ? sortContainer.querySelector("[data-sort-open]") : null;
  const sortMenu = sortContainer ? sortContainer.querySelector("[data-sort-menu]") : null;
  if (!toggleBtn || !menu) return;

  const freshToggle = toggleBtn.cloneNode(true);
  toggleBtn.replaceWith(freshToggle);
  toggleBtn = freshToggle;

  toggleBtn.addEventListener("click", (e) => {
    const isExpanded = toggleBtn.getAttribute("aria-expanded") === "true";
    toggleBtn.setAttribute("aria-expanded", String(!isExpanded));
    menu.hidden = isExpanded;

    if (!isExpanded && sortToggleBtn && sortMenu) {
      sortToggleBtn.setAttribute("aria-expanded", "false");
      sortMenu.hidden = true;
    }

    e.stopPropagation();
  });
}

/**
 * Перехват кликов по пагинации
 */
function initPaginationAJAX(root) {"""

ONREADY_OLD = """    initPaginationAJAX(root);
  });
})();"""

ONREADY_NEW = """    initPaginationAJAX(root);
    initCategoryLimitMenu();
  });
})();"""

LIMIT_IIFE_OLD = """/* ЛИМИТ товаров на странице */
(function () {
  const limitContainer = document.querySelector('.category__limit');
  if (!limitContainer) return;

  const toggleBtn = limitContainer.querySelector('[data-limit-open]');
  const menu = limitContainer.querySelector('[data-limit-menu]');
  const sortContainer = document.querySelector('.category__sort');
  const sortToggleBtn = sortContainer ? sortContainer.querySelector('[data-sort-open]') : null;
  const sortMenu = sortContainer ? sortContainer.querySelector('[data-sort-menu]') : null;

  function closeMenu() {
    toggleBtn.setAttribute('aria-expanded', 'false');
    menu.hidden = true;
  }

  toggleBtn.addEventListener('click', (e) => {
    const isExpanded = toggleBtn.getAttribute('aria-expanded') === 'true';
    toggleBtn.setAttribute('aria-expanded', !isExpanded);
    menu.hidden = isExpanded;

    if (!isExpanded && sortToggleBtn && sortMenu) {
      sortToggleBtn.setAttribute('aria-expanded', 'false');
      sortMenu.hidden = true;
    }

    e.stopPropagation();
  });

  document.addEventListener('click', (e) => {
    if (!limitContainer.contains(e.target)) {
      closeMenu();
    }
  });
})();"""

LIMIT_DOC_CLICK = """/* ЛИМИТ товаров на странице — close-on-outside (delegated, survives limit DOM refresh) */
(function () {
  document.addEventListener("click", (e) => {
    const limitContainer = document.querySelector(".category__limit");
    if (!limitContainer || limitContainer.contains(e.target)) return;

    const toggleBtn = limitContainer.querySelector("[data-limit-open]");
    const menu = limitContainer.querySelector("[data-limit-menu]");
    if (!toggleBtn || !menu) return;

    toggleBtn.setAttribute("aria-expanded", "false");
    menu.hidden = true;
  });
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
    if "initCategoryLimitMenu()" in content and "oldLimit.outerHTML = newLimit.outerHTML" in content:
        raise RuntimeError("main.js patch already applied (limit AJAX refresh present)")

    if UPDATE_PRODUCTS_OLD not in content:
        raise RuntimeError("updateProducts pagination anchor not found in main.js")
    content = content.replace(UPDATE_PRODUCTS_OLD, UPDATE_PRODUCTS_NEW, 1)

    if INIT_PAGINATION_ANCHOR not in content:
        raise RuntimeError("initPaginationAJAX anchor not found in main.js")
    content = content.replace(INIT_PAGINATION_ANCHOR, INIT_LIMIT_MENU_FN, 1)

    if ONREADY_OLD not in content:
        raise RuntimeError("filters onReady anchor not found in main.js")
    content = content.replace(ONREADY_OLD, ONREADY_NEW, 1)

    if LIMIT_IIFE_OLD not in content:
        raise RuntimeError("limit IIFE block not found in main.js")
    content = content.replace(LIMIT_IIFE_OLD, LIMIT_DOC_CLICK, 1)

    return content


def main() -> None:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    WORK_DIR.mkdir(parents=True, exist_ok=True)
    CAPTURE_DIR.mkdir(parents=True, exist_ok=True)
    ROOT.joinpath("backups").mkdir(parents=True, exist_ok=True)

    capture_path = CAPTURE_DIR / LOCAL
    patched_path = WORK_DIR / PATCHED

    live_raw = ftp_download(REMOTE)
    live_sha = sha256_hex(live_raw)
    capture_path.write_bytes(live_raw)
    BACKUP.write_bytes(live_raw)

    live_text = live_raw.decode("utf-8")
    patched_text = patch_main_js(live_text)
    patched_raw = patched_text.encode("utf-8")
    patched_sha = sha256_hex(patched_raw)
    patched_path.write_bytes(patched_raw)

    file_entry = {
        "remote_path": REMOTE,
        "capture": str(capture_path),
        "backup": str(BACKUP),
        "patched_local": str(patched_path),
        "sha256_pre": live_sha,
        "sha256_patched": patched_sha,
        "size_pre": len(live_raw),
        "size_patched": len(patched_raw),
    }

    manifest_pre = {
        "task": "M9.8.9-09C",
        "authority": "SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01",
        "stamp": stamp,
        "phase": "pre-deploy",
        "files": [file_entry],
    }

    ftp_upload(REMOTE, patched_raw)

    verify_raw = ftp_download(REMOTE)
    verify_sha = sha256_hex(verify_raw)
    file_entry["verify_sha256"] = verify_sha
    file_entry["deploy_ok"] = verify_sha == patched_sha

    cache_cleared = clear_twig_cache()

    manifest_post = {
        **manifest_pre,
        "phase": "post-deploy",
        "twig_cache_cleared": cache_cleared,
        "all_deploy_ok": file_entry["deploy_ok"],
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
        raise SystemExit("Deploy verification failed")


if __name__ == "__main__":
    main()
