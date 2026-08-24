# -*- coding: utf-8 -*-
"""Post-deploy live QA for Specialists Hub layout polish 01."""
from __future__ import annotations

import hashlib
import io
import json
import re
from pathlib import Path

import paramiko

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
OUT = Path(__file__).resolve().parent
WT = Path(
    r"X:\AI MARS\worktrees\fp0002-specialists-hub-layout-polish-01\workspaces"
    r"\website-factory-operations\FP-0002-SHPIGOVSKY\WORDPRESS"
)

REMOTE_FILES = [
    f"{DOCROOT}/wp-content/themes/shpigovsky/page-templates/specialists-hub.php",
    f"{DOCROOT}/wp-content/themes/shpigovsky/template-parts/specialist/hub-content.php",
    f"{DOCROOT}/wp-content/themes/shpigovsky/template-parts/home/rehabilitation-requirements.php",
    f"{DOCROOT}/wp-content/themes/shpigovsky/assets/css/v9-style.css",
]

LOCAL_FILES = [
    WT / "theme/shpigovsky/page-templates/specialists-hub.php",
    WT / "theme/shpigovsky/template-parts/specialist/hub-content.php",
    WT / "theme/shpigovsky/template-parts/home/rehabilitation-requirements.php",
    WT / "theme/shpigovsky/assets/css/v9-style.css",
]


def parse_secrets(text: str) -> dict[str, str]:
    pairs: dict[str, str] = {}
    for line in text.splitlines():
        match = re.match(r"^[-*]?\s*`?([A-Za-z0-9_./-]+)`?\s*[:=]\s*(.*)$", line.strip())
        if match:
            pairs[match.group(1)] = match.group(2).strip().strip("`").strip('"').strip("'")
    return pairs


def getf(pairs: dict[str, str], *keys: str) -> str | None:
    for key in keys:
        value = pairs.get(key)
        if value and "<OPERATOR" not in value and value.strip():
            return value.strip()
    return None


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fetch_html(client, url: str) -> str:
    cmd = (
        "python3 - <<'PY'\n"
        "import urllib.request\n"
        f"req=urllib.request.Request({url!r}, headers={{'User-Agent':'MARS-qa'}})\n"
        "html=urllib.request.urlopen(req, timeout=60).read().decode('utf-8','replace')\n"
        "print(html)\n"
        "PY"
    )
    _i, o, e = client.exec_command(cmd, timeout=90)
    return o.read().decode("utf-8", "replace")


def headers(client, url: str) -> str:
    _i, o, e = client.exec_command(f"curl -sI -A MARS-qa '{url}'", timeout=30)
    return o.read().decode("utf-8", "replace")


def main() -> None:
    pairs = parse_secrets(SECRETS.read_text(encoding="utf-8", errors="replace"))
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        hostname=getf(pairs, "ssh_host") or "shpigovsky.beget.tech",
        port=int(getf(pairs, "ssh_port") or "22"),
        username=getf(pairs, "ssh_username"),
        password=getf(pairs, "ssh_password_or_key_reference"),
        timeout=60,
        allow_agent=False,
        look_for_keys=False,
    )
    sftp = client.open_sftp()

    hub = fetch_html(client, "https://shpigovsky.ru/specyalisty/")
    OUT.joinpath("05-hub-html-post.txt").write_text(hub[:250000], encoding="utf-8")

    rehab_m = re.search(
        r"<section[^>]*home-rehabilitation-requirements[^>]*>[\s\S]{0,600}", hub
    )
    rehab_snippet = rehab_m.group(0) if rehab_m else ""
    # Inner container belonging to rehab block = first container immediately inside section
    rehab_inner_container = bool(
        re.search(
            r"<section[^>]*home-rehabilitation-requirements[^>]*>\s*<div class=\"container\">",
            hub,
        )
    )

    hub_qa = {
        "status_hint_len": len(hub),
        "has_internal_page_nav": "internal-page-nav" in hub,
        "has_breadcrumbs": "breadcrumbs" in hub or "Хлебные" in hub,
        "has_h1": bool(re.search(r"<h1[^>]*>\s*Специалисты", hub)),
        "has_specialists_hub": "specialists-hub" in hub,
        "has_feature_grid": "home-feature-grid" in hub,
        "card_hits": hub.count("home-feature-grid__card"),
        "has_plain_body": "plain-page-content__body" in hub,
        "has_rehab": "home-rehabilitation-requirements" in hub,
        "rehab_has_is_revealed_class_attr": "home-rehabilitation-requirements is-revealed"
        in hub
        or 'home-rehabilitation-requirements is-revealed"' in hub,
        "rehab_open_has_is_revealed": bool(
            re.search(
                r'class="[^"]*home-rehabilitation-requirements[^"]*is-revealed', hub
            )
            or re.search(
                r'class="[^"]*is-revealed[^"]*home-rehabilitation-requirements', hub
            )
        ),
        "rehab_inner_container_present": rehab_inner_container,
        "rehab_snippet": rehab_snippet[:500],
        "php_fatal": "Fatal error" in hub or "critical error" in hub.lower(),
        "has_site_header": "site-header" in hub,
        "has_site_footer": "site-footer" in hub,
        "editorial_lead_present": "12123123123" in hub,
        "editorial_body_present": "3123123123123" in hub,
        "about_home_present": "specialists-hub-about-home" in hub or "Комфорт" in hub,
    }
    OUT.joinpath("05-hub-qa.json").write_text(
        json.dumps(hub_qa, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("HUB_QA", json.dumps(hub_qa, ensure_ascii=False, indent=2))

    # CSS live rule from remote file
    with sftp.open(
        f"{DOCROOT}/wp-content/themes/shpigovsky/assets/css/v9-style.css", "rb"
    ) as rf:
        css = rf.read().decode("utf-8", "replace")
    m = re.search(r"\.plain-page-content__body\s*\{([^}]*)\}", css)
    body = m.group(1) if m else ""
    css_qa = {
        "rule": m.group(0) if m else None,
        "has_color": "color: var(--color-text-secondary, #475371);" in body,
        "has_margin_bottom": "margin-bottom: var(--pad-gap);" in body,
        "no_max_width": "max-width: 820px;" not in body,
        "no_font_size": "font-size: 18px;" not in body,
        "no_line_height": "line-height: 24px;" not in body,
    }
    OUT.joinpath("05-css-qa.json").write_text(
        json.dumps(css_qa, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("CSS_QA", css_qa)

    # Regression: page that should still have internal-page-nav (legal or generic)
    # Use /o-centre/ or a service page. Also homepage rehab block should keep container.
    home = fetch_html(client, "https://shpigovsky.ru/")
    home_rehab_inner = bool(
        re.search(
            r"<section[^>]*home-rehabilitation-requirements[^>]*>\s*<div class=\"container\">",
            home,
        )
    )
    # services hub or o-centre for internal-page-nav
    ocentre = fetch_html(client, "https://shpigovsky.ru/o-centre/")
    uslugi = fetch_html(client, "https://shpigovsky.ru/uslugi/")

    regression = {
        "home_has_rehab": "home-rehabilitation-requirements" in home,
        "home_rehab_keeps_inner_container": home_rehab_inner,
        "o_centre_has_internal_page_nav": "internal-page-nav" in ocentre,
        "uslugi_has_internal_page_nav": "internal-page-nav" in uslugi,
        "home_status_len": len(home),
        "o_centre_len": len(ocentre),
        "uslugi_len": len(uslugi),
    }
    OUT.joinpath("05-regression-qa.json").write_text(
        json.dumps(regression, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("REGRESSION", json.dumps(regression, ensure_ascii=False, indent=2))

    # SEO / robots / specialisty
    seo = {
        "specyalisty_headers": headers(client, "https://shpigovsky.ru/specyalisty/"),
        "specialisty_headers": headers(client, "https://shpigovsky.ru/specialisty/"),
        "robots_headers": headers(client, "https://shpigovsky.ru/robots.txt"),
    }
    # robots body hash
    robots_body = fetch_html(client, "https://shpigovsky.ru/robots.txt")
    seo["robots_sha256"] = sha256_bytes(robots_body.encode("utf-8"))
    seo["robots_len"] = len(robots_body)
    seo["blog_public"] = None

    probe = f"{DOCROOT}/wp-content/uploads/.fp02-layout-seo-qa.php"
    php = """<?php
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
header('Content-Type: application/json; charset=utf-8');
echo wp_json_encode(array(
  'blog_public' => (int) get_option('blog_public'),
  'home' => get_option('home'),
  'siteurl' => get_option('siteurl'),
  'page_1030_permalink' => get_permalink(1030),
), JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
"""
    sftp.putfo(io.BytesIO(php.encode("utf-8")), probe)
    _i, o, e = client.exec_command(
        f"/usr/local/bin/php8.2 -d display_errors=0 {probe}", timeout=60
    )
    raw = o.read().decode("utf-8", "replace")
    try:
        sftp.remove(probe)
    except OSError:
        pass
    start, end = raw.find("{"), raw.rfind("}")
    if start >= 0 and end > start:
        seo["wp_options"] = json.loads(raw[start : end + 1])
        seo["blog_public"] = seo["wp_options"].get("blog_public")
    OUT.joinpath("05-seo-qa.json").write_text(
        json.dumps(seo, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("SEO blog_public=", seo.get("blog_public"))
    print("specialisty first line:", seo["specialisty_headers"].splitlines()[:1])
    print("specyalisty first line:", seo["specyalisty_headers"].splitlines()[:1])

    # Parity local vs remote (semantic: normalize CRLF for compare)
    parity = []
    for local, remote in zip(LOCAL_FILES, REMOTE_FILES):
        local_raw = local.read_bytes()
        with sftp.open(remote, "rb") as rf:
            remote_raw = rf.read()
        local_n = local_raw.replace(b"\r\n", b"\n")
        remote_n = remote_raw.replace(b"\r\n", b"\n")
        parity.append(
            {
                "file": local.name,
                "exact_sha_match": sha256_bytes(local_raw) == sha256_bytes(remote_raw),
                "lf_semantic_match": sha256_bytes(local_n) == sha256_bytes(remote_n),
                "local_sha256": sha256_bytes(local_raw),
                "remote_sha256": sha256_bytes(remote_raw),
            }
        )
    OUT.joinpath("05-parity.json").write_text(
        json.dumps(parity, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("PARITY", json.dumps(parity, ensure_ascii=False, indent=2))

    sftp.close()
    client.close()

    # Acceptance gates
    fails = []
    if hub_qa["has_internal_page_nav"]:
        fails.append("hub still has internal-page-nav")
    if not hub_qa["has_h1"] or not hub_qa["has_specialists_hub"]:
        fails.append("hub listing/h1 broken")
    if hub_qa["php_fatal"]:
        fails.append("php fatal")
    if hub_qa["rehab_inner_container_present"]:
        fails.append("rehab still has inner container on hub")
    if not hub_qa["has_rehab"]:
        fails.append("rehab missing on hub")
    if not css_qa["has_color"] or not css_qa["has_margin_bottom"]:
        fails.append("css declarations missing")
    if not (
        css_qa["no_max_width"] and css_qa["no_font_size"] and css_qa["no_line_height"]
    ):
        fails.append("css old decls remain")
    if not regression["home_rehab_keeps_inner_container"]:
        fails.append("home rehab container regression")
    if not (
        regression["o_centre_has_internal_page_nav"]
        or regression["uslugi_has_internal_page_nav"]
    ):
        fails.append("internal-page-nav missing on regression surfaces")
    if seo.get("blog_public") != 1:
        fails.append("blog_public not 1")
    if not all(p["lf_semantic_match"] for p in parity):
        fails.append("parity fail")
    if not hub_qa["editorial_lead_present"] or not hub_qa["editorial_body_present"]:
        fails.append("editorial state not preserved")

    result = {"pass": not fails, "fails": fails}
    OUT.joinpath("05-acceptance.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("ACCEPTANCE", result)
    if fails:
        raise SystemExit("QA_FAIL")
    print("QA_PASS")


if __name__ == "__main__":
    main()
