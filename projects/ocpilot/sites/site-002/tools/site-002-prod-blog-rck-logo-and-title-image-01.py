#!/usr/bin/env python3
"""SITE-002 Run 4.271 — attach RCK logo + hero image to blog post 13."""
from __future__ import annotations

import hashlib
import io
import json
import re
import shlex
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import ftplib
import paramiko
from PIL import Image

OPERATION_ID = "SITE-002-PROD-BLOG-RCK-LOGO-AND-TITLE-IMAGE-01"
OCPILOT_RUN = "4.271"
POST_ID = 13
SECRETS = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    rf"\{OPERATION_ID}"
)
INCOMING_LOGO = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\incoming"
    r"\SITE-002-PROD-BLOG-SCHEDULED-NEWS-RCK-PRODUCTIVITY-01\logo-rck.png"
)
COMPOSER_HERO = Path(
    r"C:\Users\MetaCODE ONE\.cursor\projects\x-AI-MARS\assets"
    r"\rck-productivity-hero-zpm-2026.png"
)
DATE_ADDED_MUST = "2026-07-16 03:00:00"
SEO_KEYWORD_MUST = "blog/news/proizvoditelnost-truda-rck-altayskiy-kray-2026"
HERO_REMOTE_NAME = "rck-productivity-hero-zpm-2026.jpg"
LOGO_REMOTE_NAME = "rck-logo-altay-2026.png"
HERO_DB = f"catalog/blog/{HERO_REMOTE_NAME}"
LOGO_PUBLIC = f"/image/catalog/blog/{LOGO_REMOTE_NAME}"
REMOTE_BLOG_DIR = "/public_html/image/catalog/blog/"
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"
CAPTION = (
    "Работа по проекту ведётся при участии экспертов Регионального центра компетенций "
    "Алтайского края."
)
BODY_PARAS = [
    (
        "Барнаульский завод пищевого машиностроения принимает участие в федеральном проекте "
        "«Производительность труда», который реализуется в рамках национального проекта "
        "«Эффективная и конкурентная экономика»."
    ),
    (
        "Участие в программе направлено на повышение эффективности производственных процессов, "
        "внедрение современных подходов к организации работы и развитие инструментов бережливого "
        "производства. В рамках проекта на предприятии проводится анализ текущих процессов, "
        "выявляются зоны для улучшения и формируются решения, которые помогут сократить потери, "
        "повысить производительность и укрепить конкурентные позиции завода."
    ),
    (
        "Работа ведётся совместно с экспертами Регионального центра компетенций в сфере "
        "производительности труда Алтайского края (РЦК). Специалисты центра сопровождают "
        "предприятия-участники проекта, помогают выстраивать системный подход к оптимизации "
        "процессов и внедрению практик бережливого производства."
    ),
    (
        "Для Барнаульского завода пищевого машиностроения участие в проекте — это важный этап "
        "развития. Предприятие выпускает оборудование из нержавеющей стали для предприятий "
        "общественного питания, торговли и пищевых производств: столы, стеллажи, полки, "
        "моечные ванны, подставки, вытяжные зонты и другую продукцию. Повышение внутренней "
        "эффективности позволит и дальше развивать производственные возможности, улучшать "
        "организацию работы и повышать устойчивость бизнеса."
    ),
    (
        "В настоящее время на предприятии продолжается работа в рамках первого этапа проекта. "
        "В ближайшее время планируется подведение промежуточных итогов и подготовка информации "
        "о достигнутых результатах и показателях."
    ),
    (
        "Мы рассматриваем участие в проекте как возможность для последовательного развития "
        "производства, повышения качества внутренних процессов и дальнейшего роста эффективности "
        "предприятия."
    ),
]


def build_body_with_logo() -> str:
    # Exact approved text from Run 4.270; only change is inserting the RCK logo
    # into the existing caption block (replacing caption-only placeholder).
    parts = [
        f"<p><strong>{BODY_PARAS[0]}</strong></p>",
        f"<p>{BODY_PARAS[1]}</p>",
        f"<p>{BODY_PARAS[2]}</p>",
        "<p>"
        f'<img src="{LOGO_PUBLIC}" '
        'alt="Логотип Регионального центра компетенций Алтайского края" '
        'style="max-width:280px;height:auto;" />'
        f"<br /><em>{CAPTION}</em>"
        "</p>",
        f"<p>{BODY_PARAS[3]}</p>",
        f"<p>{BODY_PARAS[4]}</p>",
        f"<p>{BODY_PARAS[5]}</p>",
    ]
    return "\n".join(parts)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def parse_section(name: str) -> dict[str, str]:
    text = SECRETS.read_text(encoding="utf-8")
    m = re.search(r"^## PRODUCTION\s*$([\s\S]*?)(?=^## |\Z)", text, re.M)
    if not m:
        raise RuntimeError("PRODUCTION section missing")
    block = m.group(1)
    sm = re.search(rf"^### {re.escape(name)}\s*$([\s\S]*?)(?=^### |\Z)", block, re.M)
    if not sm:
        raise RuntimeError(f"Missing subsection {name}")
    fields: dict[str, str] = {}
    key = None
    for line in sm.group(1).splitlines():
        s = line.strip()
        if not s:
            continue
        if s.endswith(":"):
            key = s[:-1].strip().lower().replace(" ", "_")
            fields.setdefault(key, "")
            continue
        if key:
            fields[key] = s
    return fields


def mysql(sql: str, write: bool = False) -> str:
    ssh_c = parse_section("SSH")
    db = parse_section("Database")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        ssh_c["host"],
        port=int(ssh_c.get("port") or 22),
        username=ssh_c["username"],
        password=ssh_c["password"],
        timeout=60,
        allow_agent=False,
        look_for_keys=False,
    )
    cmd = (
        f"MYSQL_PWD={shlex.quote(db['password'])} mysql -N -B "
        f"-u {shlex.quote(db['username'])} {shlex.quote(db['database'])}"
    )
    stdin, stdout, stderr = client.exec_command(cmd, timeout=180)
    payload = sql if sql.rstrip().endswith(";") else sql + ";"
    stdin.write(payload)
    stdin.channel.shutdown_write()
    out = stdout.read().decode("utf-8", "replace")
    err = stderr.read().decode("utf-8", "replace")
    client.close()
    combined = out + err
    if write and ("ERROR" in combined.upper() or "Access denied" in combined):
        raise RuntimeError(combined[:800])
    return combined


def sql_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace("'", "''")


def ftp_connect() -> ftplib.FTP:
    f = parse_section("FTP / SFTP")
    ftp = ftplib.FTP()
    ftp.connect(f["host"], int(f.get("port") or 21), timeout=180)
    ftp.login(f["username"], f["password"])
    ftp.set_pasv(True)
    return ftp


def http_get(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            body = resp.read()
            return {
                "url": url,
                "status": resp.status,
                "final_url": resp.geturl(),
                "bytes": len(body),
                "body_text": body.decode("utf-8", "replace") if len(body) < 2_500_000 else "",
                "sha256": sha256_bytes(body),
            }
    except urllib.error.HTTPError as exc:
        body = exc.read() if exc.fp else b""
        return {
            "url": url,
            "status": exc.code,
            "final_url": url,
            "bytes": len(body),
            "body_text": body.decode("utf-8", "replace"),
            "sha256": sha256_bytes(body) if body else "",
        }
    except Exception as exc:  # noqa: BLE001
        return {"url": url, "status": 0, "error": str(exc), "bytes": 0, "body_text": ""}


def prepare_images() -> dict:
    if not INCOMING_LOGO.is_file():
        raise RuntimeError(f"Logo missing: {INCOMING_LOGO}")
    if not COMPOSER_HERO.is_file():
        raise RuntimeError(f"Composer hero missing: {COMPOSER_HERO}")

    image_input = ROOT / "image-input"
    image_processed = ROOT / "image-processed"
    image_input.mkdir(parents=True, exist_ok=True)
    image_processed.mkdir(parents=True, exist_ok=True)

    logo_raw = INCOMING_LOGO.read_bytes()
    (image_input / INCOMING_LOGO.name).write_bytes(logo_raw)
    logo_out = image_processed / LOGO_REMOTE_NAME
    # Keep uploaded bytes (PNG with brand black background) — no redesign.
    logo_out.write_bytes(logo_raw)
    with Image.open(io.BytesIO(logo_raw)) as im:
        logo_meta = {"format": im.format, "mode": im.mode, "size": list(im.size)}

    hero_raw = COMPOSER_HERO.read_bytes()
    (image_input / COMPOSER_HERO.name).write_bytes(hero_raw)
    hero_out = image_processed / HERO_REMOTE_NAME
    with Image.open(io.BytesIO(hero_raw)) as im:
        rgb = im.convert("RGB")
        # Target landscape suited to blog resizeCrop 1400x700 / list 600x400.
        w, h = rgb.size
        target_ratio = 1400 / 700
        cur_ratio = w / h if h else target_ratio
        if abs(cur_ratio - target_ratio) > 0.02:
            if cur_ratio > target_ratio:
                new_w = int(h * target_ratio)
                left = (w - new_w) // 2
                rgb = rgb.crop((left, 0, left + new_w, h))
            else:
                new_h = int(w / target_ratio)
                top = (h - new_h) // 2
                rgb = rgb.crop((0, top, w, top + new_h))
        if rgb.size[0] != 1400 or rgb.size[1] != 700:
            rgb = rgb.resize((1400, 700), Image.Resampling.LANCZOS)
        buf = io.BytesIO()
        rgb.save(buf, format="JPEG", quality=90, optimize=True)
        hero_bytes = buf.getvalue()
        hero_meta = {"format": "JPEG", "mode": "RGB", "size": [1400, 700]}
    hero_out.write_bytes(hero_bytes)

    summary = {
        "at": utc_now(),
        "logo": {
            "incoming": str(INCOMING_LOGO),
            "incoming_name": INCOMING_LOGO.name,
            "processed": str(logo_out),
            "remote_name": LOGO_REMOTE_NAME,
            "db_or_body_path": LOGO_PUBLIC,
            "sha256": sha256_bytes(logo_raw),
            "bytes": len(logo_raw),
            "meta": logo_meta,
        },
        "hero": {
            "composer_source": str(COMPOSER_HERO),
            "processed": str(hero_out),
            "remote_name": HERO_REMOTE_NAME,
            "db_path": HERO_DB,
            "sha256": sha256_bytes(hero_bytes),
            "bytes": len(hero_bytes),
            "meta": hero_meta,
            "generation_mode": "COMPOSER_ONLY_NO_API",
        },
    }
    write_json(image_processed / "image-processing-summary.json", summary)
    write_text(
        image_processed / "image-processing-summary.md",
        "# Image processing\n\n"
        f"**Operation:** `{OPERATION_ID}`\n"
        f"**Run:** {OCPILOT_RUN}\n\n"
        "## Logo\n\n"
        f"- Incoming: `{INCOMING_LOGO.name}`\n"
        f"- Remote: `{REMOTE_BLOG_DIR}{LOGO_REMOTE_NAME}`\n"
        f"- Body src: `{LOGO_PUBLIC}`\n"
        f"- Bytes: {len(logo_raw)}\n"
        f"- SHA256: `{sha256_bytes(logo_raw)}`\n\n"
        "## Hero / title image\n\n"
        f"- Source: Composer GenerateImage `{COMPOSER_HERO.name}`\n"
        f"- Mode: COMPOSER_ONLY_NO_API\n"
        f"- Remote: `{REMOTE_BLOG_DIR}{HERO_REMOTE_NAME}`\n"
        f"- DB `image`: `{HERO_DB}`\n"
        f"- Normalized: 1400×700 JPEG q90\n"
        f"- Bytes: {len(hero_bytes)}\n"
        f"- SHA256: `{sha256_bytes(hero_bytes)}`\n",
    )
    return summary


def ftp_upload(local: Path, remote: str, ftp: ftplib.FTP) -> dict:
    data = local.read_bytes()
    before = sha256_bytes(data)
    ftp.storbinary("STOR " + remote, io.BytesIO(data))
    bio = io.BytesIO()
    ftp.retrbinary("RETR " + remote, bio.write)
    after = sha256_bytes(bio.getvalue())
    return {
        "local": str(local),
        "remote": remote,
        "bytes": len(data),
        "sha256_local": before,
        "sha256_remote": after,
        "match": before == after,
    }


def backup_post() -> str:
    dump = mysql(
        "SELECT id, category_id, active, date_added, IFNULL(image,''), title, "
        "short_description, content, meta_title, meta_description, meta_keyword, views "
        f"FROM oc_blog_posts WHERE id={POST_ID}"
    )
    write_text(ROOT / "db-backup" / "post13-before.sqlish.tsv", dump)
    return dump


def apply_db_update(content: str) -> dict:
    escaped = sql_escape(content)
    sql = (
        f"UPDATE oc_blog_posts SET image='{sql_escape(HERO_DB)}', "
        f"content='{escaped}' WHERE id={POST_ID} "
        f"AND date_added='{DATE_ADDED_MUST}' AND active=1 "
        f"AND (image IS NULL OR image='' OR image='{sql_escape(HERO_DB)}');"
    )
    result = mysql(sql, write=True)
    after = mysql(
        "SELECT id, category_id, active, date_added, IFNULL(image,''), "
        "CHAR_LENGTH(title), CHAR_LENGTH(short_description), CHAR_LENGTH(content), "
        "LEFT(title,80), "
        "(content LIKE '%БЗПМ%') AS has_bzpm, "
        f"(content LIKE '%{LOGO_REMOTE_NAME}%') AS has_logo, "
        f"(image='{sql_escape(HERO_DB)}') AS has_hero "
        f"FROM oc_blog_posts WHERE id={POST_ID}"
    )
    seo = mysql(
        f"SELECT seo_url_id, query, keyword FROM oc_seo_url WHERE query='blog_post_id={POST_ID}'"
    )
    date_ok = mysql(
        f"SELECT date_added FROM oc_blog_posts WHERE id={POST_ID}"
    ).strip()
    write_text(ROOT / "article-apply" / "post13-after.tsv", after)
    write_text(ROOT / "article-apply" / "seo-after.tsv", seo)
    return {
        "update_result": result.strip(),
        "after": after.strip(),
        "seo": seo.strip(),
        "date_added": date_ok,
        "date_unchanged": date_ok == DATE_ADDED_MUST,
        "seo_unchanged": SEO_KEYWORD_MUST in seo,
    }


def verify_http() -> dict:
    slug = "proizvoditelnost-truda-rck-altayskiy-kray-2026"
    checks = []
    urls = [
        ("home", "https://bzpm.ru/"),
        ("blog", "https://bzpm.ru/blog"),
        ("blog_news", "https://bzpm.ru/blog/news"),
        ("article_seo", f"https://bzpm.ru/blog/news/{slug}"),
        ("article_route", f"https://bzpm.ru/index.php?route=blog/post&blog_post_id={POST_ID}"),
        ("contact", "https://bzpm.ru/contact"),
        ("sitemap", "https://bzpm.ru/sitemap.xml"),
        ("hero_asset", f"https://bzpm.ru/image/catalog/blog/{HERO_REMOTE_NAME}"),
        ("logo_asset", f"https://bzpm.ru/image/catalog/blog/{LOGO_REMOTE_NAME}"),
    ]
    for name, url in urls:
        res = http_get(url)
        text = res.get("body_text") or ""
        item = {
            "name": name,
            "url": url,
            "status": res.get("status"),
            "bytes": res.get("bytes"),
            "sha256": res.get("sha256", ""),
            "contains_slug": slug in text,
            "contains_title_fragment": "Производительность труда" in text
            or "производительность труда" in text.lower(),
            "contains_bzpm": "БЗПМ" in text,
            "error": res.get("error"),
        }
        checks.append(item)
    gate = mysql(
        f"SELECT id, (date_added <= NOW()) AS due, NOW(), date_added "
        f"FROM oc_blog_posts WHERE id={POST_ID}"
    ).strip()
    gate_legacy = mysql(
        "SELECT id, (date_added <= NOW()) AS due FROM oc_blog_posts WHERE id=8"
    ).strip()
    write_json(ROOT / "verification" / "http-verify.json", {"at": utc_now(), "checks": checks})
    write_text(
        ROOT / "verification" / "prepublish-gate.md",
        "# Pre-publish gate\n\n"
        f"```\npost13:\n{gate}\n\nlegacy8:\n{gate_legacy}\n```\n",
    )
    return {"checks": checks, "gate": gate, "gate_legacy": gate_legacy}


def main() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    prepared = prepare_images()
    backup_post()

    before_meta = mysql(
        "SELECT id, active, date_added, IFNULL(image,''), CHAR_LENGTH(content) "
        f"FROM oc_blog_posts WHERE id={POST_ID}"
    ).strip()
    # Rebuild approved body with logo insert only (avoid mysql -B newline mangling).
    content_probe = mysql(
        f"SELECT "
        f"(content LIKE '%{sql_escape(CAPTION)}%') AS has_caption, "
        f"(content LIKE '%БЗПМ%') AS has_bzpm "
        f"FROM oc_blog_posts WHERE id={POST_ID}"
    ).strip().splitlines()[0]
    write_text(ROOT / "article-apply" / "content-probe.txt", content_probe + "\n")
    parts = content_probe.split("\t")
    if len(parts) < 2 or parts[0] != "1" or parts[1] != "0":
        raise RuntimeError(f"Content probe failed (need caption=1 bzpm=0): {content_probe!r}")
    new_content = build_body_with_logo()
    if "БЗПМ" in new_content:
        raise RuntimeError("Built content unexpectedly contains БЗПМ")
    write_text(ROOT / "article-apply" / "content-after.html", new_content)

    ftp = ftp_connect()
    try:
        # ensure blog dir exists
        try:
            ftp.cwd(REMOTE_BLOG_DIR)
        except ftplib.error_perm:
            # create nested path if needed
            parts = REMOTE_BLOG_DIR.strip("/").split("/")
            path = ""
            for p in parts:
                path += "/" + p
                try:
                    ftp.mkd(path)
                except ftplib.error_perm:
                    pass
        uploads = []
        for local_name, remote_name in (
            (HERO_REMOTE_NAME, HERO_REMOTE_NAME),
            (LOGO_REMOTE_NAME, LOGO_REMOTE_NAME),
        ):
            local = ROOT / "image-processed" / local_name
            remote = REMOTE_BLOG_DIR + remote_name
            uploads.append(ftp_upload(local, remote, ftp))
    finally:
        ftp.quit()

    write_json(ROOT / "ftp-upload" / "image-upload-result.json", {"at": utc_now(), "uploads": uploads})
    write_text(
        ROOT / "ftp-upload" / "image-upload-result.txt",
        "\n".join(
            f"{u['remote']} match={u['match']} bytes={u['bytes']} sha256={u['sha256_remote']}"
            for u in uploads
        )
        + "\n",
    )

    db_result = apply_db_update(new_content)
    http_result = verify_http()

    summary = {
        "operation_id": OPERATION_ID,
        "ocpilot_run": OCPILOT_RUN,
        "at": utc_now(),
        "before_meta": before_meta,
        "prepared": prepared,
        "ftp_uploads": uploads,
        "db": db_result,
        "http": {
            "checks": [
                {
                    "name": c["name"],
                    "status": c["status"],
                    "contains_slug": c["contains_slug"],
                    "contains_bzpm": c["contains_bzpm"],
                }
                for c in http_result["checks"]
            ],
            "gate": http_result["gate"],
        },
        "invariants": {
            "date_added_unchanged": db_result["date_unchanged"],
            "seo_unchanged": db_result["seo_unchanged"],
            "post_id": POST_ID,
            "no_new_article": True,
        },
    }
    write_json(ROOT / "logs" / "apply-summary.json", summary)
    write_text(
        ROOT / "article-apply" / "apply-method.md",
        "# Apply method\n\n"
        "1. Composer-only hero JPEG normalized to 1400×700.\n"
        "2. Operator logo PNG copied from intake without redesign.\n"
        "3. FTP upload both files into `/public_html/image/catalog/blog/`.\n"
        f"4. Scoped `UPDATE oc_blog_posts` for id={POST_ID} only: set `image` + insert logo "
        "into existing caption block; guard on `date_added` + empty image.\n"
        "5. No change to slug, date_added, title, teaser, SEO, autopublish model.\n",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
