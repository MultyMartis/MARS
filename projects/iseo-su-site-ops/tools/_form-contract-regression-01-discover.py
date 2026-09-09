#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Discover live /page__FORM.php authorities with visible tel name=pf_contact and no pf_phone."""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

import paramiko

SECRETS = Path(r"X:\AI MARS\local\sites\iseo-su-production\secrets.local.md")
DOC = "/home/n/nikel0rv/i-seo.su/public_html"
OUT = Path(
    r"X:\AI MARS\projects\iseo-su-site-ops\evidence\form-contract-regression-01\live-authorities.json"
)
TEL_BAD = re.compile(
    r'<input\s+type="tel"[^>]*name="pf_contact"',
    re.I,
)
OLD_CORE = (
    '<input type="tel" id="pf_contact" name="pf_contact" placeholder="WhatsApp / Telegram" required>'
)


def parse_secrets(path: Path) -> dict:
    out = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^([a-z0-9_]+):\s*(.*)$", line.strip())
        if m:
            out[m.group(1)] = m.group(2).strip()
    return out


def listdir_names(sftp, path: str) -> list[str]:
    try:
        return sftp.listdir(path)
    except OSError:
        return []


def read_text(sftp, path: str) -> str:
    with sftp.open(path, "r") as f:
        return f.read().decode("utf-8", "replace")


def classify(text: str) -> dict:
    tel_bad = TEL_BAD.search(text) is not None
    pf_phone = 'name="pf_phone"' in text
    hidden = bool(
        re.search(
            r'<input[^>]*type="hidden"[^>]*name="pf_contact"',
            text,
            re.I,
        )
    ) or ('name="pf_contact" value="' in text)
    select = bool(re.search(r"<select[^>]*name=\"pf_contact\"", text, re.I))
    consent = 'name="personal_data_consent"' in text
    return {
        "tel_named_pf_contact": tel_bad,
        "pf_phone_present": pf_phone,
        "hidden_pf_contact": hidden,
        "select_pf_contact": select,
        "consent_checkbox": consent,
        "old_core_exact": OLD_CORE in text,
        "proven_defect": tel_bad and (not pf_phone),
    }


def main() -> int:
    secrets = parse_secrets(SECRETS)
    transport = paramiko.Transport(
        (secrets["ftp_or_sftp_host"], int(secrets.get("ftp_or_sftp_port") or 22))
    )
    transport.connect(
        username=secrets["ftp_or_sftp_username"],
        password=secrets["ftp_or_sftp_password"],
    )
    sftp = paramiko.SFTPClient.from_transport(transport)
    findings = []
    try:
        tp = f"{DOC}/wp-content/themes/iseoblog/template-parts"
        names = sorted(listdir_names(sftp, tp))
        formish = [
            n
            for n in names
            if n.startswith("content-form") or "form" in n.lower()
        ]
        for name in names:
            if not name.endswith(".php"):
                continue
            if "form" not in name.lower() and name not in (
                "content-footer.php",
                "content.php",
                "content-page.php",
            ):
                continue
            remote = f"{tp}/{name}"
            text = read_text(sftp, remote)
            info = classify(text)
            if info["tel_named_pf_contact"] or info["proven_defect"] or "pf_contact" in text:
                findings.append(
                    {
                        "kind": "theme-template-part",
                        "remote": remote,
                        "name": name,
                        **info,
                    }
                )

        extra_paths = [
            f"{DOC}/blog.html",
            f"{DOC}/blog-article.html",
            f"{DOC}/services/audit.html",
            f"{DOC}/services/adv.html",
            f"{DOC}/services/development.html",
            f"{DOC}/services/serm.html",
            f"{DOC}/services/ai-optimization.html",
            f"{DOC}/contacts.html",
            f"{DOC}/reviews.html",
            f"{DOC}/cases.html",
            f"{DOC}/services.html",
            f"{DOC}/webinar-seo-podryadchik.html",
            f"{DOC}/wp-content/themes/iseoblog/footer.php",
            f"{DOC}/wp-content/themes/iseoblog/page-home.php",
            f"{DOC}/wp-content/themes/iseoblog/page-blog.php",
        ]
        for remote in extra_paths:
            try:
                text = read_text(sftp, remote)
            except OSError:
                findings.append({"kind": "missing", "remote": remote})
                continue
            info = classify(text)
            findings.append({"kind": "file", "remote": remote, **info})

        # Sample live service pages that are not in MARS snapshot
        sample_pages = [
            f"{DOC}/services/seo/prodvizhenie-sajta-restorana.html",
            f"{DOC}/services/seo/prodvizhenie-sajta-otele.html",
            f"{DOC}/services/audit/tehnicheskij-audit.html",
            f"{DOC}/services/adv/kontekstnaya-reklama.html",
            f"{DOC}/services/development/sozdanie-sajtov.html",
            f"{DOC}/services/serm/smm.html",
        ]
        for remote in sample_pages:
            try:
                text = read_text(sftp, remote)
            except OSError:
                findings.append({"kind": "missing-page", "remote": remote})
                continue
            includes = re.findall(r"content-form[\w.-]+\.php", text)
            info = classify(text)
            findings.append(
                {
                    "kind": "page-sample",
                    "remote": remote,
                    "includes": includes,
                    "inline_old_core": info["old_core_exact"],
                    **info,
                }
            )
    finally:
        sftp.close()
        transport.close()

    OUT.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "task": "ISEO-SU-SITE-OPS-FORM-CONTRACT-REGRESSION-01",
        "scanned_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "formish_template_parts": formish,
        "all_template_part_names": names,
        "findings": findings,
        "proven_authorities": [
            f for f in findings if f.get("proven_defect")
        ],
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(
        json.dumps(
            {
                "out": str(OUT),
                "template_parts": names,
                "formish": formish,
                "proven_count": len(payload["proven_authorities"]),
                "proven": [
                    {"remote": f["remote"], "old_core": f.get("old_core_exact")}
                    for f in payload["proven_authorities"]
                ],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
