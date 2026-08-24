# -*- coding: utf-8 -*-
"""FP-0002: bounded production robots restore and post-write validation."""
from __future__ import annotations

import difflib
import hashlib
import io
import json
import re
import ssl
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen

import paramiko


HERE = Path(__file__).resolve().parent
PROJECT = Path(__file__).resolve().parents[4]
REPO = next(parent for parent in Path(__file__).resolve().parents if (parent / ".git").exists())
SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
ROBOTS_REMOTE = f"{DOCROOT}/robots.txt"
POLICY_REMOTE = f"{DOCROOT}/wp-content/plugins/shpigovsky-core/assets/robots-seo-policy.txt"
INDEXING_REMOTE = f"{DOCROOT}/wp-content/plugins/shpigovsky-core/src/Admin/IndexingControl.php"
WATCHDOG_REMOTE = f"{DOCROOT}/wp-content/plugins/shpigovsky-core/src/Admin/IndexingWatchdog.php"
CANONICAL_GIT_PATH = (
    "workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/"
    "WORDPRESS/plugins/shpigovsky-core/assets/robots-seo-policy.txt"
)
REVIEW_GIT_PATH = (
    "workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/"
    "WORDPRESS/seo/OLYA-ROBOTS-REVIEWED-CANDIDATE.txt"
)
UA = "FP-0002-OLYA-ROBOTS-CLOSEOUT-2026-08-24/1.0"


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_json(name: str, value: Any) -> None:
    (HERE / name).write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def git_bytes(path: str) -> bytes:
    return subprocess.check_output(
        ["git", "show", f"HEAD:{path}"],
        cwd=REPO,
    )


def parse_secrets(text: str) -> dict[str, str]:
    pairs: dict[str, str] = {}
    for line in text.splitlines():
        match = re.match(
            r"^[-*]?\s*`?([A-Za-z0-9_./-]+)`?\s*[:=]\s*(.*)$",
            line.strip(),
        )
        if match:
            pairs[match.group(1)] = (
                match.group(2).strip().strip("`").strip('"').strip("'")
            )
    return pairs


def getf(pairs: dict[str, str], *keys: str) -> str | None:
    for key in keys:
        value = pairs.get(key)
        if value and "<OPERATOR" not in value and value.strip():
            return value.strip()
    return None


def http_get(url: str) -> tuple[int, str, dict[str, str], bytes]:
    request = Request(url, headers={"User-Agent": UA})
    with urlopen(
        request,
        timeout=45,
        context=ssl.create_default_context(),
    ) as response:
        return (
            response.status,
            str(response.geturl()),
            {key.lower(): value for key, value in response.headers.items()},
            response.read(),
        )


def meta_robots(body: bytes) -> str | None:
    text = body.decode("utf-8", errors="replace")
    match = re.search(
        r"<meta\s+[^>]*name=['\"]robots['\"][^>]*content=['\"]([^'\"]+)",
        text,
        re.I,
    )
    if not match:
        match = re.search(
            r"<meta\s+[^>]*content=['\"]([^'\"]+)['\"][^>]*name=['\"]robots['\"]",
            text,
            re.I,
        )
    return match.group(1) if match else None


def has_global_close(body: bytes) -> bool:
    return bool(
        re.search(
            r"(?mi)^\s*Disallow:\s*/\s*$",
            body.decode("utf-8", errors="replace"),
        )
    )


def connect() -> tuple[paramiko.SSHClient, paramiko.SFTPClient]:
    pairs = parse_secrets(SECRETS.read_text(encoding="utf-8", errors="replace"))
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        hostname=getf(pairs, "ssh_host", "sftp_host", "ftp_host")
        or "shpigovsky.beget.tech",
        port=int(getf(pairs, "ssh_port", "sftp_port") or "22"),
        username=getf(pairs, "ssh_username", "ssh_user", "sftp_user", "ftp_user"),
        password=getf(
            pairs,
            "ssh_password_or_key_reference",
            "ssh_password",
            "sftp_password",
            "ftp_or_sftp_password",
            "ftp_password",
        ),
        timeout=60,
        allow_agent=False,
        look_for_keys=False,
    )
    return client, client.open_sftp()


def read_remote(sftp: paramiko.SFTPClient, path: str) -> bytes:
    stream = io.BytesIO()
    sftp.getfo(path, stream)
    return stream.getvalue()


def wp_state(client: paramiko.SSHClient) -> dict[str, Any]:
    php = r"""
$_SERVER['HTTP_HOST']='shpigovsky.ru';
$_SERVER['SERVER_NAME']='shpigovsky.ru';
$_SERVER['HTTPS']='on';
$_SERVER['REQUEST_URI']='/';
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
$snap = class_exists('Shpigovsky\\Core\\Admin\\IndexingState')
  ? Shpigovsky\Core\Admin\IndexingState::snapshot() : null;
$open_body = class_exists('Shpigovsky\\Core\\Admin\\IndexingControl')
  ? Shpigovsky\Core\Admin\IndexingControl::robots_body(true) : null;
$next_watch = wp_next_scheduled('fp02_indexing_watchdog_check');
echo wp_json_encode(array(
  'blog_public' => (int) get_option('blog_public'),
  'indexing_snapshot' => $snap,
  'human_authority' => get_option('fp02_indexing_human_authority'),
  'guard_active' => class_exists('Shpigovsky\\Core\\Admin\\IndexingControl'),
  'watchdog_active' => class_exists('Shpigovsky\\Core\\Admin\\IndexingWatchdog'),
  'watchdog_next_utc' => $next_watch ? gmdate('c', $next_watch) : null,
  'watchdog_last' => get_option('fp02_indexing_watchdog_last'),
  'watchdog_baseline' => get_option('fp02_indexing_watchdog_baseline'),
  'open_body_sha256' => is_string($open_body) ? hash('sha256', $open_body) : null,
  'open_body_has_global_disallow' => is_string($open_body)
    ? (bool) preg_match('/^\s*Disallow:\s*\/\s*$/mi', $open_body) : null,
), JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
echo "\n";
"""
    command = (
        "php8.2 -d display_errors=0 -r 'eval(stream_get_contents(STDIN));' "
        "2>/dev/null || php -d display_errors=0 "
        "-r 'eval(stream_get_contents(STDIN));'"
    )
    stdin, stdout, stderr = client.exec_command(command, timeout=180)
    stdin.write(php)
    stdin.channel.shutdown_write()
    raw = stdout.read().decode("utf-8", errors="replace")
    err = stderr.read().decode("utf-8", errors="replace")
    code = stdout.channel.recv_exit_status()
    line = next((item for item in raw.splitlines() if item.lstrip().startswith("{")), None)
    if code != 0 or not line:
        raise RuntimeError(f"WP state probe failed: code={code}; stderr={err[:500]!r}")
    return json.loads(line)


def public_probe(url: str) -> dict[str, Any]:
    status, final_url, headers, body = http_get(url)
    return {
        "url": url,
        "status": status,
        "final_url": final_url,
        "x_robots_tag": headers.get("x-robots-tag"),
        "meta_robots": meta_robots(body),
        "bytes": len(body),
    }


def robots_checks(
    live_status: int,
    live_headers: dict[str, str],
    live: bytes,
    physical: bytes,
    canonical: bytes,
) -> dict[str, Any]:
    text = live.decode("utf-8", errors="replace")
    expected_agents = (
        "User-agent: Yandex",
        "User-agent: GoogleBot",
        "User-agent: Bingbot",
        "User-agent: *",
        "User-Agent: Googlebot-Image",
    )
    return {
        "http_status": live_status,
        "content_type": live_headers.get("content-type"),
        "live_sha256": sha(live),
        "physical_sha256": sha(physical),
        "canonical_sha256": sha(canonical),
        "live_equals_physical": live == physical,
        "physical_equals_canonical": physical == canonical,
        "live_equals_canonical": live == canonical,
        "global_disallow_root": has_global_close(live),
        "production_sitemap": "Sitemap: https://shpigovsky.ru/wp-sitemap.xml" in text,
        "staging_host_present": bool(re.search(r"beget\.tech|staging", text, re.I)),
        "expected_agents": {
            agent: agent in text for agent in expected_agents
        },
        "bytes": len(live),
        "line_count": len(text.splitlines()),
    }


def main() -> None:
    canonical = git_bytes(CANONICAL_GIT_PATH)
    review = git_bytes(REVIEW_GIT_PATH)
    canonical_meta = {
        "captured_at": utcnow(),
        "source": f"HEAD:{CANONICAL_GIT_PATH}",
        "review_source": f"HEAD:{REVIEW_GIT_PATH}",
        "canonical_sha256": sha(canonical),
        "review_sha256": sha(review),
        "sources_equal": canonical == review,
        "bytes": len(canonical),
        "line_endings": "LF" if b"\r\n" not in canonical else "CRLF",
        "utf8_bom": canonical.startswith(b"\xef\xbb\xbf"),
    }
    write_json("00-canonical-meta.json", canonical_meta)
    (HERE / "00-canonical-robots.txt").write_bytes(canonical)
    if not canonical_meta["sources_equal"]:
        raise SystemExit("STOP: runtime canonical and review source differ")

    client, sftp = connect()
    try:
        physical_before = read_remote(sftp, ROBOTS_REMOTE)
        policy_before = read_remote(sftp, POLICY_REMOTE)
        indexing_before = read_remote(sftp, INDEXING_REMOTE)
        watchdog_before = read_remote(sftp, WATCHDOG_REMOTE)
        stat_before = sftp.stat(ROBOTS_REMOTE)
        live_status, live_url, live_headers, live_before = http_get(
            "https://shpigovsky.ru/robots.txt"
        )
        sitemap_status, sitemap_url, sitemap_headers, sitemap_before = http_get(
            "https://shpigovsky.ru/wp-sitemap.xml"
        )
        state_before = wp_state(client)

        snapshot = state_before.get("indexing_snapshot") or {}
        pre = {
            "captured_at": utcnow(),
            "mode": "PRE_MUTATION",
            "blog_public": state_before.get("blog_public"),
            "effective": snapshot.get("effective"),
            "human_decision": snapshot.get("human_decision"),
            "human_recorded_at": snapshot.get("human_recorded_at"),
            "human_source": snapshot.get("human_source"),
            "guard_active": state_before.get("guard_active"),
            "watchdog_active": state_before.get("watchdog_active"),
            "watchdog_next_utc": state_before.get("watchdog_next_utc"),
            "watchdog_last": state_before.get("watchdog_last"),
            "watchdog_baseline": state_before.get("watchdog_baseline"),
            "open_body_sha256": state_before.get("open_body_sha256"),
            "open_body_has_global_disallow": state_before.get(
                "open_body_has_global_disallow"
            ),
            "physical": {
                "path": ROBOTS_REMOTE,
                "sha256": sha(physical_before),
                "bytes": len(physical_before),
                "mtime_utc": datetime.fromtimestamp(
                    stat_before.st_mtime, timezone.utc
                ).isoformat(),
            },
            "live": {
                "status": live_status,
                "final_url": live_url,
                "content_type": live_headers.get("content-type"),
                "sha256": sha(live_before),
                "equals_physical": live_before == physical_before,
            },
            "canonical": canonical_meta,
            "production_owner": {
                "policy_asset_sha256": sha(policy_before),
                "policy_asset_equals_canonical": policy_before == canonical,
                "indexing_control_sha256": sha(indexing_before),
                "watchdog_sha256": sha(watchdog_before),
            },
            "sitemap": {
                "status": sitemap_status,
                "final_url": sitemap_url,
                "content_type": sitemap_headers.get("content-type"),
                "production_host_present": b"https://shpigovsky.ru/" in sitemap_before,
                "staging_host_present": bool(
                    re.search(rb"beget\.tech|staging", sitemap_before, re.I)
                ),
            },
        }
        write_json("01-pre-intake.json", pre)
        (HERE / "01-physical-robots-before.txt").write_bytes(physical_before)
        (HERE / "01-live-robots-before.txt").write_bytes(live_before)
        diff = "".join(
            difflib.unified_diff(
                physical_before.decode("utf-8", errors="replace").splitlines(True),
                canonical.decode("utf-8", errors="replace").splitlines(True),
                fromfile="CURRENT-PHYSICAL-ROBOTS",
                tofile="CURRENT-OLYA-CANONICAL-ROBOTS",
            )
        )
        (HERE / "02-physical-vs-canonical.diff").write_text(
            diff,
            encoding="utf-8",
            newline="\n",
        )

        open_ok = (
            pre["blog_public"] == 1
            and pre["effective"] == "OPEN"
            and pre["human_decision"] == "OPEN"
        )
        owner_ok = (
            pre["guard_active"] is True
            and pre["watchdog_active"] is True
            and pre["open_body_sha256"] == sha(canonical)
            and pre["open_body_has_global_disallow"] is False
            and pre["production_owner"]["policy_asset_equals_canonical"] is True
        )
        if not open_ok:
            raise SystemExit("STOP: indexing is not OPEN — HUMAN APPROVED")
        if not owner_ok:
            raise SystemExit("STOP: OPEN-state owner does not match canonical Olya policy")

        timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        backup_remote = f"{ROBOTS_REMOTE}.fp0002-pre-restore-{timestamp}.bak"
        sftp.putfo(io.BytesIO(physical_before), backup_remote)
        backup_bytes = read_remote(sftp, backup_remote)
        (HERE / f"03-rollback-robots-{timestamp}.txt").write_bytes(backup_bytes)
        backup_meta = {
            "captured_at": utcnow(),
            "remote_path": backup_remote,
            "evidence_copy": f"03-rollback-robots-{timestamp}.txt",
            "sha256": sha(backup_bytes),
            "bytes": len(backup_bytes),
            "matches_pre_restore_physical": backup_bytes == physical_before,
        }
        write_json("03-backup-meta.json", backup_meta)
        if backup_bytes != physical_before:
            raise SystemExit("STOP: backup verification failed")

        sftp.putfo(io.BytesIO(canonical), ROBOTS_REMOTE)
        sftp.chmod(ROBOTS_REMOTE, stat_before.st_mode & 0o777)
        physical_after = read_remote(sftp, ROBOTS_REMOTE)
        restore = {
            "applied_at": utcnow(),
            "path": ROBOTS_REMOTE,
            "before_sha256": sha(physical_before),
            "canonical_sha256": sha(canonical),
            "after_sha256": sha(physical_after),
            "exact_match": physical_after == canonical,
            "policy_content_changed_during_deploy": False,
            "backup_remote": backup_remote,
        }
        write_json("04-restore.json", restore)
        if physical_after != canonical:
            raise SystemExit("FAIL: physical robots write did not match canonical bytes")

        live_status, live_url, live_headers, live_after = http_get(
            "https://shpigovsky.ru/robots.txt"
        )
        sitemap_status, sitemap_url, sitemap_headers, sitemap_after = http_get(
            "https://shpigovsky.ru/wp-sitemap.xml"
        )
        state_after = wp_state(client)
        homepage = public_probe("https://shpigovsky.ru/")
        service = public_probe(
            "https://shpigovsky.ru/uslugi/zavisimosti/"
            "lechenie-alkogolnoy-zavisimosti/"
        )
        contacts = public_probe("https://shpigovsky.ru/kontakty/")
        robots = robots_checks(
            live_status,
            live_headers,
            live_after,
            physical_after,
            canonical,
        )
        snapshot_after = state_after.get("indexing_snapshot") or {}
        sitemap_text = sitemap_after.decode("utf-8", errors="replace")
        post = {
            "captured_at": utcnow(),
            "robots": robots,
            "robots_final_url": live_url,
            "indexing": {
                "blog_public": state_after.get("blog_public"),
                "effective": snapshot_after.get("effective"),
                "human_decision": snapshot_after.get("human_decision"),
                "guard_active": state_after.get("guard_active"),
                "watchdog_active": state_after.get("watchdog_active"),
                "watchdog_next_utc": state_after.get("watchdog_next_utc"),
                "watchdog_last": state_after.get("watchdog_last"),
                "watchdog_baseline": state_after.get("watchdog_baseline"),
                "open_body_sha256": state_after.get("open_body_sha256"),
            },
            "sitemap": {
                "status": sitemap_status,
                "final_url": sitemap_url,
                "content_type": sitemap_headers.get("content-type"),
                "xml_sitemap": "<sitemapindex" in sitemap_text
                or "<urlset" in sitemap_text,
                "production_host_present": "https://shpigovsky.ru/" in sitemap_text,
                "staging_host_present": bool(
                    re.search(r"beget\.tech|staging", sitemap_text, re.I)
                ),
                "referenced_by_robots": robots["production_sitemap"],
            },
            "public_regression": {
                "homepage": homepage,
                "service": service,
                "contacts": contacts,
            },
        }
        write_json("05-post-validation.json", post)
        (HERE / "05-live-robots-after.txt").write_bytes(live_after)
        (HERE / "05-physical-robots-after.txt").write_bytes(physical_after)

        robots_pass = (
            robots["http_status"] == 200
            and str(robots["content_type"] or "").lower().startswith("text/plain")
            and robots["live_equals_physical"]
            and robots["physical_equals_canonical"]
            and not robots["global_disallow_root"]
            and robots["production_sitemap"]
            and not robots["staging_host_present"]
            and all(robots["expected_agents"].values())
        )
        indexing_pass = (
            post["indexing"]["blog_public"] == 1
            and post["indexing"]["effective"] == "OPEN"
            and post["indexing"]["human_decision"] == "OPEN"
            and post["indexing"]["guard_active"] is True
            and post["indexing"]["watchdog_active"] is True
            and post["indexing"]["watchdog_next_utc"]
            and post["indexing"]["open_body_sha256"] == sha(canonical)
            and not any(
                "noindex" in str(page.get("meta_robots") or "").lower()
                or "noindex" in str(page.get("x_robots_tag") or "").lower()
                for page in (homepage, service)
            )
        )
        sitemap_pass = (
            post["sitemap"]["status"] == 200
            and post["sitemap"]["xml_sitemap"]
            and post["sitemap"]["production_host_present"]
            and not post["sitemap"]["staging_host_present"]
            and post["sitemap"]["referenced_by_robots"]
        )
        public_pass = all(
            page["status"] == 200 for page in (homepage, service, contacts)
        )
        summary = {
            "status": (
                "PASS"
                if robots_pass and indexing_pass and sitemap_pass and public_pass
                else "ATTENTION"
            ),
            "canonical_sha256": sha(canonical),
            "old_production_sha256": sha(physical_before),
            "live_sha256": sha(live_after),
            "physical_sha256": sha(physical_after),
            "backup": backup_meta,
            "robots_pass": robots_pass,
            "indexing_pass": indexing_pass,
            "sitemap_pass": sitemap_pass,
            "public_pass": public_pass,
            "open_state_owner_preserves_olya": owner_ok
            and post["indexing"]["open_body_sha256"] == sha(canonical),
            "olya_policy_intact": robots_pass,
            "indexing_open_human_approved": indexing_pass,
            "production_mutations": [
                backup_remote,
                ROBOTS_REMOTE,
            ],
            "synthetic_close_performed": False,
            "form_or_smtp_test_performed": False,
            "editorial_db_touched": False,
        }
        write_json("06-summary.json", summary)
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        if summary["status"] != "PASS":
            raise SystemExit(2)
    finally:
        sftp.close()
        client.close()


if __name__ == "__main__":
    main()
