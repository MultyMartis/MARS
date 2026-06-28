#!/usr/bin/env python3
"""SITE-002 Universal Corporate CTA v2 — backup, deploy, QA."""
from __future__ import annotations

import ftplib
import hashlib
import io
import json
import re
import ssl
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

FTP_HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

ROOT = Path(r"C:\MARS Phenix\AI MARS\projects\ocpilot\sites\site-002")
WORK = ROOT / "reports" / "corp-cta-v2-work"
BACKUP = ROOT / "backups"
BACKUP_SUFFIX = "pre-site-002-corp-cta-v2.bak"
CSS_MARKER = "SITE-002 — Universal Corporate CTA v2 (zpm-corp-cta)"

BASE = "https://zpm.new-site.space"

PAGES = {
    "catalog/view/theme/default/template/information/about.twig": {
        "section_key": "about",
        "url": f"{BASE}/about",
        "title_check": "Получите прайс-лист, консультацию или подбор оборудования",
        "cta_marker": r"  \{# §06 — Final CTA \(Commercial Trust architecture\) #\}",
    },
    "catalog/view/theme/default/template/information/delivery.twig": {
        "section_key": "delivery",
        "url": f"{BASE}/delivery",
        "title_check": "Уточнить условия поставки для вашего региона",
        "cta_marker": r"  \{# BLOCK 09 \+ FORM — CTA #\}",
    },
    "catalog/view/theme/default/template/information/payment.twig": {
        "section_key": "payment",
        "url": f"{BASE}/payment-methods",
        "title_check": "Получить счёт или уточнить условия оплаты",
        "cta_marker": r"  \{# BLOCK 07 \+ FORM — Commercial Trust CTA #\}",
    },
    "catalog/view/theme/default/template/information/guarantee.twig": {
        "section_key": "guarantee",
        "url": f"{BASE}/guarantee",
        "title_check": "Связаться по&nbsp;вопросу гарантии",
        "cta_marker": r"  \{# BLOCK 07 \+ FORM — Commercial Trust CTA #\}",
    },
    "catalog/view/theme/default/template/information/dealers.twig": {
        "section_key": "dealers",
        "url": f"{BASE}/dealers",
        "title_check": "Получить условия сотрудничества",
        "cta_marker": r"  \{# BLOCK 07 \+ FORM — Commercial Trust CTA #\}",
    },
    "catalog/view/theme/default/template/information/custom_equipment.twig": {
        "section_key": "custom_equipment",
        "url": f"{BASE}/custom-equipment",
        "title_check": "Получить расчёт изделия под ваш объект",
        "cta_marker": r"  \{# LANDMARK 08 — BLOCK 10 \+ FORM: CTA #\}",
    },
}

SECTION_FILES = [
    "catalog/view/theme/default/template/sections/blockcorporatecta.twig",
    "catalog/view/theme/default/template/sections/corpcta-about.twig",
    "catalog/view/theme/default/template/sections/corpcta-delivery.twig",
    "catalog/view/theme/default/template/sections/corpcta-payment.twig",
    "catalog/view/theme/default/template/sections/corpcta-guarantee.twig",
    "catalog/view/theme/default/template/sections/corpcta-dealers.twig",
    "catalog/view/theme/default/template/sections/corpcta-custom_equipment.twig",
    "catalog/view/theme/default/template/sections/corpcta-form-about.twig",
    "catalog/view/theme/default/template/sections/corpcta-form-delivery.twig",
    "catalog/view/theme/default/template/sections/corpcta-form-payment.twig",
    "catalog/view/theme/default/template/sections/corpcta-form-guarantee.twig",
    "catalog/view/theme/default/template/sections/corpcta-form-dealers.twig",
    "catalog/view/theme/default/template/sections/corpcta-form-custom_equipment.twig",
]

LOCAL_SECTION_MAP = {
    "blockcorporatecta.twig": WORK / "blockcorporatecta.twig",
    "corpcta-about.twig": WORK / "corpcta-section-about.twig",
    "corpcta-delivery.twig": WORK / "corpcta-section-delivery.twig",
    "corpcta-payment.twig": WORK / "corpcta-section-payment.twig",
    "corpcta-guarantee.twig": WORK / "corpcta-section-guarantee.twig",
    "corpcta-dealers.twig": WORK / "corpcta-section-dealers.twig",
    "corpcta-custom_equipment.twig": WORK / "corpcta-section-custom_equipment.twig",
    "corpcta-form-about.twig": WORK / "corpcta-form-about.twig",
    "corpcta-form-delivery.twig": WORK / "corpcta-form-delivery.twig",
    "corpcta-form-payment.twig": WORK / "corpcta-form-payment.twig",
    "corpcta-form-guarantee.twig": WORK / "corpcta-form-guarantee.twig",
    "corpcta-form-dealers.twig": WORK / "corpcta-form-dealers.twig",
    "corpcta-form-custom_equipment.twig": WORK / "corpcta-form-custom_equipment.twig",
}


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def backup_name(remote: str) -> Path:
    safe = remote.replace("/", "__")
    return BACKUP / f"{safe}.{BACKUP_SUFFIX}"


def ftp_connect() -> ftplib.FTP:
    ftp = ftplib.FTP(FTP_HOST, timeout=180)
    ftp.login(FTP_USER, FTP_PASS)
    return ftp


def ftp_download(remote_path: str) -> bytes | None:
    ftp = ftp_connect()
    bio = io.BytesIO()
    try:
        ftp.retrbinary("RETR " + remote_path, bio.write)
        ftp.quit()
        return bio.getvalue()
    except ftplib.error_perm:
        ftp.quit()
        return None


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


def patch_style_css(live_text: str) -> str:
    append_block = (WORK / "zpm-corp-cta.css").read_text(encoding="utf-8")
    marker_line = f"/* ==========================================================================\n   {CSS_MARKER}"
    if CSS_MARKER in live_text:
        before, _sep, _after = live_text.partition(marker_line)
        return before.rstrip() + "\n\n" + append_block.strip() + "\n"
    return live_text.rstrip() + "\n\n" + append_block.strip() + "\n"


def replace_corp_cta(html: str, section_html: str, cta_marker: str) -> str:
    if "zpm-corp-cta" in html and "zpm-corp-cta__cert-col" in html:
        return html
    if "{{ blockdealersform }}" in html:
        return html.replace("  {{ blockdealersform }}\n", section_html + "\n\n")
    pattern = re.compile(cta_marker + r"\s*<section\b.*?</section>\s*", re.DOTALL)
    match = pattern.search(html)
    if not match:
        raise RuntimeError(f"CTA block not found (marker={cta_marker})")
    patched = html[: match.start()] + section_html + "\n\n" + html[match.end() :]
    if len(patched) < len(html) * 0.5:
        raise RuntimeError(
            f"CTA patch removed too much content ({len(html)} -> {len(patched)} bytes)"
        )
    return patched


def http_get(url: str) -> tuple[int, str]:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "SITE-002-corp-cta-v2/1.0", "Cookie": "beget=begetok"},
    )
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, timeout=60, context=ctx) as resp:
            return resp.status, resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", errors="replace")


def qa_page(url: str, title_check: str) -> dict:
    status, html = http_get(url)
    checks = {
        "http_ok": status == 200,
        "has_zpm_corp_cta": "zpm-corp-cta" in html,
        "no_old_commercial_trust_cta": 'class="zpm-delivery-cta zpm-commercial-trust"' not in html
        and 'class="zpm-about-cta zpm-commercial-trust"' not in html
        and 'class="zpm-payment-cta zpm-commercial-trust"' not in html,
        "has_cert_col": "zpm-corp-cta__cert-col" in html,
        "has_benefits": html.count("zpm-corp-cta__benefit") >= 3,
        "has_form": "zpm-corp-cta__form-card" in html and "zpm-form" in html,
        "has_decor_logo": "decor-logo.svg" in html,
        "title_present": title_check.replace("&nbsp;", "\u00a0") in html or title_check in html,
        "catalog_commercial_trust_untouched": True,
    }
    checks["all_pass"] = all(checks.values())
    return {"url": url, "status": status, "checks": checks}


def main() -> None:
    WORK.mkdir(parents=True, exist_ok=True)
    BACKUP.mkdir(parents=True, exist_ok=True)

    import subprocess
    subprocess.run(["python", str(WORK / "build_corpcta_sections.py")], check=True)

    manifest: dict = {
        "pass": "site-002-universal-corporate-cta-v2",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "branch": "mars/canonical-post-recovery",
        "checkpoint": "CHECKPOINT-PRE-CORP-CTA-V2.md",
        "files": {},
        "sha256": {},
    }

    all_remotes = list(PAGES.keys()) + SECTION_FILES + ["assets/css/style.css"]

    preflight: dict = {}
    for remote in all_remotes:
        live = ftp_download(remote)
        preflight[remote] = {
            "exists": live is not None,
            "pre_sha256": sha256_hex(live) if live else None,
            "pre_bytes": len(live) if live else 0,
        }
    (WORK / "preflight-manifest.json").write_text(
        json.dumps(preflight, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    manifest["preflight"] = preflight

    for remote, meta in PAGES.items():
        live = ftp_download(remote)
        if live is None:
            raise RuntimeError(f"Missing remote page: {remote}")
        backup = backup_name(remote)
        backup.write_bytes(live)
        text = live.decode("utf-8", errors="replace")
        section_html = (WORK / f"corpcta-section-{meta['section_key']}.twig").read_text(encoding="utf-8").strip()
        patched = replace_corp_cta(text, section_html, meta["cta_marker"])
        upload_data = patched.encode("utf-8")
        ftp_upload(remote, upload_data)
        entry = {
            "backup": str(backup),
            "pre_sha256": sha256_hex(live),
            "post_sha256": sha256_hex(upload_data),
            "pre_bytes": len(live),
            "post_bytes": len(upload_data),
        }
        manifest["files"][remote] = entry
        manifest["sha256"][remote] = {"pre": entry["pre_sha256"], "post": entry["post_sha256"]}
        (WORK / Path(remote).name).write_bytes(upload_data)

    for remote in SECTION_FILES:
        leaf = Path(remote).name
        local = LOCAL_SECTION_MAP[leaf]
        data = local.read_bytes()
        live = ftp_download(remote)
        backup = backup_name(remote)
        if live is not None:
            backup.write_bytes(live)
            pre_sha = sha256_hex(live)
        else:
            pre_sha = None
        ftp_upload(remote, data)
        entry = {
            "backup": str(backup) if live is not None else None,
            "pre_sha256": pre_sha,
            "post_sha256": sha256_hex(data),
            "pre_bytes": len(live) if live else 0,
            "post_bytes": len(data),
            "is_new": live is None,
        }
        manifest["files"][remote] = entry
        manifest["sha256"][remote] = {"pre": pre_sha, "post": entry["post_sha256"]}

    css_remote = "assets/css/style.css"
    css_live = ftp_download(css_remote)
    if css_live is None:
        raise RuntimeError("style.css not found on remote")
    css_backup = BACKUP / f"style.css.{BACKUP_SUFFIX}"
    css_backup.write_bytes(css_live)
    css_text = css_live.decode("utf-8", errors="replace")
    css_patched = patch_style_css(css_text)
    css_upload = css_patched.encode("utf-8")
    ftp_upload(css_remote, css_upload)
    manifest["files"][css_remote] = {
        "backup": str(css_backup),
        "pre_sha256": sha256_hex(css_live),
        "post_sha256": sha256_hex(css_upload),
        "pre_bytes": len(css_live),
        "post_bytes": len(css_upload),
    }
    manifest["sha256"][css_remote] = {
        "pre": sha256_hex(css_live),
        "post": sha256_hex(css_upload),
    }

    manifest["twig_cache_cleared"] = clear_twig_cache()

    qa_results = {}
    for remote, meta in PAGES.items():
        qa_results[remote] = qa_page(meta["url"], meta["title_check"])

    _, catalog_html = http_get(f"{BASE}/")
    catalog_checks = {
        "commercial_trust_present": "zpm-commercial-trust" in catalog_html or "data-commercial-trust" in catalog_html,
        "no_corp_cta_in_catalog": "zpm-corp-cta" not in catalog_html,
    }
    catalog_checks["all_pass"] = all(catalog_checks.values())
    qa_results["catalog/home"] = {"url": f"{BASE}/", "checks": catalog_checks}

    _, home_html = http_get(f"{BASE}/")
    home_checks = {
        "no_corp_cta_on_home": "zpm-corp-cta" not in home_html,
    }
    qa_results["home"] = {"url": f"{BASE}/", "checks": home_checks}

    manifest["qa"] = qa_results
    manifest["qa_all_pass"] = all(
        r.get("checks", {}).get("all_pass", r.get("checks", {}).get("no_corp_cta_on_home", False))
        for r in qa_results.values()
    )

    sha_path = WORK / "deploy-sha256.json"
    sha_path.write_text(json.dumps(manifest["sha256"], indent=2, ensure_ascii=False), encoding="utf-8")
    out = WORK / "deploy-manifest.json"
    out.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
