#!/usr/bin/env python3
"""M9.8.9-08 — attribute filter group reset: capture, backup, patch, deploy."""
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

ROOT = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002")
WORK_DIR = ROOT / "reports" / "m9.8.9-08-work"
CAPTURE_DIR = WORK_DIR / "live-capture"

FILES = [
    {
        "remote": "catalog/view/theme/default/template/sections/filterssidebar.twig",
        "local": "catalog__view__theme__default__template__sections__filterssidebar.twig",
        "backup": ROOT / "backups" / "filterssidebar.twig.pre-m9.8.9-08-filter-group-reset.bak",
        "patched": "catalog__view__theme__default__template__sections__filterssidebar.twig.patched",
        "patch_fn": "patch_twig",
    },
    {
        "remote": "assets/js/main.js",
        "local": "assets__js__main.js",
        "backup": ROOT / "backups" / "main.js.pre-m9.8.9-08-filter-group-reset.bak",
        "patched": "assets__js__main.js.patched",
        "patch_fn": "patch_main_js",
    },
    {
        "remote": "assets/css/style.css",
        "local": "assets__css__style.css",
        "backup": ROOT / "backups" / "style.css.pre-m9.8.9-08-filter-group-reset.bak",
        "patched": "assets__css__style.css.patched",
        "patch_fn": "patch_style_css",
    },
]

ATTR_HEADBAR = """      <div class="flt__group-headbar">
        <button class="flt__group-head" type="button" data-acc-btn aria-expanded="{% if group.expanded %}true{% else %}false{% endif %}">
          <span class="flt__group-title">{{ group.name }}</span>
          <span class="flt__chev" aria-hidden="true"></span>
        </button>
        <button type="button" class="flt__group-reset" data-filter-group-reset hidden aria-label="Сбросить {{ group.name }}">Сбросить</button>
      </div>"""

ATTR_HEADBAR_ELSE = """  <div class="flt__group-headbar">
    <button class="flt__group-head" type="button" data-acc-btn aria-expanded="{% if group.expanded %}true{% endif %}">
      <span class="flt__group-title">{{ group.name }}</span>
      <span class="flt__chev" aria-hidden="true"></span>
    </button>
    <button type="button" class="flt__group-reset" data-filter-group-reset hidden aria-label="Сбросить {{ group.name }}">Сбросить</button>
  </div>"""

ATTR_HEADBAR_NESTED = """          <div class="flt__group-headbar">
            <button class="flt__group-head" type="button" data-acc-btn aria-expanded="{% if group.expanded %}true{% else %}false{% endif %}">
              <span class="flt__group-title">{{ group.name }}</span>
              <span class="flt__chev" aria-hidden="true"></span>
            </button>
            <button type="button" class="flt__group-reset" data-filter-group-reset hidden aria-label="Сбросить {{ group.name }}">Сбросить</button>
          </div>"""

JS_VISIBILITY_FN = """
  function updateGroupResetVisibility(root) {
    root.querySelectorAll("[data-filter-group-reset]").forEach((btn) => {
      const group = btn.closest("[data-acc].flt__group");
      if (!group) return;
      const panel = group.querySelector("[data-acc-panel]");
      if (!panel) return;
      const hasChecked = panel.querySelector(".flt__check-input:checked") !== null;
      btn.hidden = !hasChecked;
    });
  }
"""

JS_GROUP_RESET_FN = """
  function initGroupReset(root) {
    const form = root.querySelector("[data-filters-form]");
    if (!form) return;

    root.querySelectorAll("[data-filter-group-reset]").forEach((btn) => {
      btn.addEventListener("click", (e) => {
        e.preventDefault();
        e.stopPropagation();

        const group = btn.closest("[data-acc].flt__group");
        if (!group) return;
        const panel = group.querySelector("[data-acc-panel]");
        if (!panel) return;

        panel.querySelectorAll(".flt__check-input").forEach((input) => {
          input.checked = false;
          const label = input.closest(".flt__check");
          if (label) label.classList.remove("active");
        });

        syncChoiceClasses(root);
        updateBrowserUrl(form);
      });
    });
  }
"""

CSS_HEADBAR = """
/* M9.8.9-08 — attribute filter group reset headbar */
.flt__group-headbar {
  display: flex;
  align-items: center;
  gap: var(--pad-gap-mini, 8px);
  width: 100%;
}

.flt__group-headbar .flt__group-head {
  flex: 1 1 auto;
  min-width: 0;
  width: auto;
}

.flt__group-reset {
  flex: 0 0 auto;
  margin: 0;
  padding: 0;
  border: 0;
  background: transparent;
  color: var(--accent-color-01);
  font: inherit;
  font-size: 12px;
  line-height: 1.2;
  cursor: pointer;
  white-space: nowrap;
}

.flt__group-reset:hover,
.flt__group-reset:focus-visible {
  text-decoration: underline;
}

.flt__group-reset[hidden] {
  display: none !important;
}
"""


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


def patch_twig(content: str) -> str:
    if "data-filter-group-reset" in content:
        raise RuntimeError("Twig patch already applied (data-filter-group-reset present)")

    primary_old = """    {% for group in filter_groups %}
    <section class="flt__group" data-acc>
      <button class="flt__group-head" type="button" data-acc-btn aria-expanded="{% if group.expanded %}true{% else %}false{% endif %}">
        <span class="flt__group-title">{{ group.name }}</span>
        <span class="flt__chev" aria-hidden="true"></span>
      </button>"""

    primary_new = """    {% for group in filter_groups %}
    <section class="flt__group" data-acc>
""" + ATTR_HEADBAR

    nested_old = """        {% for group in filter_secondary_groups %}
        <section class="flt__group" data-acc>
          <button class="flt__group-head" type="button" data-acc-btn aria-expanded="{% if group.expanded %}true{% else %}false{% endif %}">
            <span class="flt__group-title">{{ group.name }}</span>
            <span class="flt__chev" aria-hidden="true"></span>
          </button>"""

    nested_new = """        {% for group in filter_secondary_groups %}
        <section class="flt__group" data-acc>
""" + ATTR_HEADBAR_NESTED

    else_old = """    {% for group in filter_groups %}
<section class="flt__group" data-acc>
  <button class="flt__group-head" type="button" data-acc-btn aria-expanded="{% if group.expanded %}true{% endif %}">
    <span class="flt__group-title">{{ group.name }}</span>
    <span class="flt__chev" aria-hidden="true"></span>
  </button>"""

    else_new = """    {% for group in filter_groups %}
<section class="flt__group" data-acc>
""" + ATTR_HEADBAR_ELSE

    for old, new, label in [
        (primary_old, primary_new, "profile primary filter_groups"),
        (nested_old, nested_new, "profile secondary nested groups"),
        (else_old, else_new, "non-profile filter_groups"),
    ]:
        if old not in content:
            raise RuntimeError(f"Twig anchor not found: {label}")
        content = content.replace(old, new, 1)

    return content


def patch_main_js(content: str) -> str:
    if "initGroupReset" in content:
        raise RuntimeError("main.js patch already applied (initGroupReset present)")

    sync_old = """    root.querySelectorAll(".flt__switch").forEach((label) => {
      const input = label.querySelector(".flt__switch-input");
      label.classList.toggle("active", !!(input && input.checked));
    });
  }"""

    sync_new = """    root.querySelectorAll(".flt__switch").forEach((label) => {
      const input = label.querySelector(".flt__switch-input");
      label.classList.toggle("active", !!(input && input.checked));
    });

    updateGroupResetVisibility(root);
  }"""

    if sync_old not in content:
        raise RuntimeError("syncChoiceClasses block not found in main.js")

    content = content.replace(sync_old, sync_new, 1)

    insert_anchor = " function initReset(root) {"
    if insert_anchor not in content:
        raise RuntimeError("initReset anchor not found in main.js")

    content = content.replace(
        insert_anchor,
        JS_VISIBILITY_FN + JS_GROUP_RESET_FN + insert_anchor,
        1,
    )

    onready_old = """    initCopyLink(root);
    initReset(root);
    syncChoiceClasses(root);"""

    onready_new = """    initCopyLink(root);
    initReset(root);
    initGroupReset(root);
    syncChoiceClasses(root);"""

    if onready_old not in content:
        raise RuntimeError("onReady init chain not found in main.js")

    return content.replace(onready_old, onready_new, 1)


def patch_style_css(content: str) -> str:
    if ".flt__group-headbar" in content:
        raise RuntimeError("style.css patch already applied (.flt__group-headbar present)")

    anchor = ".flt__group-head {"
    idx = content.find(anchor)
    if idx == -1:
        raise RuntimeError(".flt__group-head { anchor not found in style.css")

    end = content.find("}", idx)
    if end == -1:
        raise RuntimeError(".flt__group-head block end not found")

    insert_at = end + 1
    return content[:insert_at] + CSS_HEADBAR + content[insert_at:]


PATCH_FNS = {
    "patch_twig": patch_twig,
    "patch_main_js": patch_main_js,
    "patch_style_css": patch_style_css,
}


def main() -> None:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    WORK_DIR.mkdir(parents=True, exist_ok=True)
    CAPTURE_DIR.mkdir(parents=True, exist_ok=True)
    ROOT.joinpath("backups").mkdir(parents=True, exist_ok=True)

    manifest_pre: dict = {
        "task": "M9.8.9-08",
        "authority": "SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01",
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
