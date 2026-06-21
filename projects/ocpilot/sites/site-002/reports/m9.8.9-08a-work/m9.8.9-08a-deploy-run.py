#!/usr/bin/env python3
"""M9.8.9-08A — filter group reset button: move to group body, always visible disabled/active."""
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
WORK_DIR = ROOT / "reports" / "m9.8.9-08a-work"
CAPTURE_DIR = WORK_DIR / "live-capture"

FILES = [
    {
        "remote": "catalog/view/theme/default/template/sections/filterssidebar.twig",
        "local": "catalog__view__theme__default__template__sections__filterssidebar.twig",
        "backup": ROOT / "backups" / "filterssidebar.twig.pre-m9.8.9-08a-group-reset-position.bak",
        "patched": "catalog__view__theme__default__template__sections__filterssidebar.twig.patched",
        "patch_fn": "patch_twig",
    },
    {
        "remote": "assets/js/main.js",
        "local": "assets__js__main.js",
        "backup": ROOT / "backups" / "main.js.pre-m9.8.9-08a-group-reset-position.bak",
        "patched": "assets__js__main.js.patched",
        "patch_fn": "patch_main_js",
    },
    {
        "remote": "assets/css/style.css",
        "local": "assets__css__style.css",
        "backup": ROOT / "backups" / "style.css.pre-m9.8.9-08a-group-reset-position.bak",
        "patched": "assets__css__style.css.patched",
        "patch_fn": "patch_style_css",
    },
]

GROUP_RESET_BTN = (
    '<button type="button" class="flt__group-reset" data-filter-group-reset disabled '
    'aria-label="Сбросить {{ group.name }}">Сбросить</button>'
)

JS_VISIBILITY_OLD = """  function updateGroupResetVisibility(root) {
    root.querySelectorAll("[data-filter-group-reset]").forEach((btn) => {
      const group = btn.closest("[data-acc].flt__group");
      if (!group) return;
      const panel = group.querySelector("[data-acc-panel]");
      if (!panel) return;
      const hasChecked = panel.querySelector(".flt__check-input:checked") !== null;
      btn.hidden = !hasChecked;
    });
  }"""

JS_VISIBILITY_NEW = """  function updateGroupResetVisibility(root) {
    root.querySelectorAll("[data-filter-group-reset]").forEach((btn) => {
      const group = btn.closest("[data-acc].flt__group");
      if (!group) return;
      const panel = group.querySelector("[data-acc-panel]");
      if (!panel) return;
      const hasChecked = panel.querySelector(".flt__check-input:checked") !== null;
      btn.disabled = !hasChecked;
      btn.classList.toggle("is-active", hasChecked);
    });
  }"""

JS_CLICK_GUARD_OLD = """      btn.addEventListener("click", (e) => {
        e.preventDefault();
        e.stopPropagation();

        const group = btn.closest("[data-acc].flt__group");"""

JS_CLICK_GUARD_NEW = """      btn.addEventListener("click", (e) => {
        e.preventDefault();
        e.stopPropagation();
        if (btn.disabled) return;

        const group = btn.closest("[data-acc].flt__group");"""

CSS_OLD = """/* M9.8.9-08 — attribute filter group reset headbar */
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
}"""

CSS_NEW = """/* M9.8.9-08A — attribute filter group reset (body placement) */
.flt__group-reset {
  display: block;
  margin: var(--pad-gap-mini, 8px) 0 0;
  padding: 0;
  border: 0;
  background: transparent;
  color: var(--text-muted, #9a9a9a);
  font: inherit;
  font-size: 12px;
  line-height: 1.2;
  cursor: not-allowed;
  white-space: nowrap;
  text-align: left;
}

.flt__group-reset:disabled {
  color: var(--text-muted, #9a9a9a);
  cursor: not-allowed;
  opacity: 0.65;
}

.flt__group-reset.is-active,
.flt__group-reset:not(:disabled) {
  color: var(--accent-color-02);
  cursor: pointer;
  opacity: 1;
}

.flt__group-reset.is-active:hover,
.flt__group-reset.is-active:focus-visible,
.flt__group-reset:not(:disabled):hover,
.flt__group-reset:not(:disabled):focus-visible {
  text-decoration: underline;
}"""


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
    if "M9.8.9-08A" in content or (
        "data-filter-group-reset" in content
        and "flt__group-headbar" not in content
        and re.search(r"data-acc-panel[^>]*>[\s\S]*?data-filter-group-reset", content)
    ):
        raise RuntimeError("Twig patch already applied (08A body placement)")

    if "data-filter-group-reset" not in content:
        raise RuntimeError("M9.8.9-08 not present — expected data-filter-group-reset in twig")

    headbar_reset_re = re.compile(
        r"\s*<button type=\"button\" class=\"flt__group-reset\" data-filter-group-reset hidden "
        r'aria-label="Сбросить \{\{ group\.name \}\}">Сбросить</button>',
        re.MULTILINE,
    )
    content, n_removed = headbar_reset_re.subn("", content)
    if n_removed < 1:
        raise RuntimeError("Could not remove headbar reset buttons from twig")

    headbar_open_re = re.compile(
        r"<div class=\"flt__group-headbar\">\s*\n(\s*)<button class=\"flt__group-head\"",
        re.MULTILINE,
    )

    def unwrap_headbar(match: re.Match[str]) -> str:
        indent = match.group(1)
        return f"{indent}<button class=\"flt__group-head\""

    content = headbar_open_re.sub(unwrap_headbar, content)

    content = content.replace(
        "        </button>\n      </div>\n\n      <div class=\"flt__group-body\"",
        "        </button>\n\n      <div class=\"flt__group-body\"",
    )
    content = content.replace(
        "            </button>\n          </div>\n\n          <div class=\"flt__group-body\"",
        "            </button>\n\n          <div class=\"flt__group-body\"",
    )
    content = content.replace(
        "  </button>\n  </div>\n\n  <div class=\"flt__group-body\"",
        "  </button>\n\n  <div class=\"flt__group-body\"",
    )

    panel_close_re = re.compile(
        r"(        {% endfor %}\n)(      </div>\n    </section>\n    {% endfor %}\n\n    {% if filter_secondary_groups %})",
        re.MULTILINE,
    )
    if not panel_close_re.search(content):
        raise RuntimeError("Primary filter_groups panel close anchor not found")
    content = panel_close_re.sub(
        r"\1        " + GROUP_RESET_BTN + "\n\\2",
        content,
        count=1,
    )

    nested_close_re = re.compile(
        r"(            {% endfor %}\n)(          </div>\n        </section>\n        {% endfor %})",
        re.MULTILINE,
    )
    if not nested_close_re.search(content):
        raise RuntimeError("Secondary nested groups panel close anchor not found")
    content = nested_close_re.sub(
        r"\1            " + GROUP_RESET_BTN + "\n\\2",
        content,
        count=1,
    )

    else_close_re = re.compile(
        r"(    {% endfor %}\n)(  </div>\n</section>\n{% endfor %})",
        re.MULTILINE,
    )
    if not else_close_re.search(content):
        raise RuntimeError("Non-profile filter_groups panel close anchor not found")
    content = else_close_re.sub(
        r"\1    " + GROUP_RESET_BTN + "\n\\2",
        content,
        count=1,
    )

    if content.count("data-filter-group-reset") != n_removed:
        raise RuntimeError(
            f"Reset button count mismatch: removed {n_removed}, "
            f"now {content.count('data-filter-group-reset')}"
        )

    return content


def patch_main_js(content: str) -> str:
    if "btn.classList.toggle(\"is-active\"" in content:
        raise RuntimeError("main.js patch already applied (08A visibility logic)")

    if JS_VISIBILITY_OLD not in content:
        raise RuntimeError("updateGroupResetVisibility block not found in main.js")

    content = content.replace(JS_VISIBILITY_OLD, JS_VISIBILITY_NEW, 1)

    if JS_CLICK_GUARD_OLD not in content:
        raise RuntimeError("initGroupReset click handler anchor not found in main.js")

    return content.replace(JS_CLICK_GUARD_OLD, JS_CLICK_GUARD_NEW, 1)


def patch_style_css(content: str) -> str:
    if "M9.8.9-08A" in content:
        raise RuntimeError("style.css patch already applied (08A)")

    if CSS_OLD not in content:
        raise RuntimeError("M9.8.9-08 CSS block not found in style.css")

    return content.replace(CSS_OLD, CSS_NEW, 1)


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
        "task": "M9.8.9-08A",
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
