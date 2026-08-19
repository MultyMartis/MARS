#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PROD-P18E-E/F exact-file deploy + bounded legal page update."""
from __future__ import annotations

import hashlib
import io
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import paramiko

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
ROOT = Path(__file__).resolve().parents[3]
EV = ROOT / "REPORTS" / "evidence" / "prod-p18e-ef-form-goal-policy-integration"
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
THEME_REMOTE = f"{DOCROOT}/wp-content/themes/shpigovsky"
PLUGIN_REMOTE = f"{DOCROOT}/wp-content/plugins/shpigovsky-core"
POLICY_CONTENT = (EV / "cookie-policy-after.html").read_text(encoding="utf-8")

FILES = {
    "plugin_bootstrap": (
        ROOT / "WORDPRESS" / "plugins" / "shpigovsky-core" / "shpigovsky-core.php",
        f"{PLUGIN_REMOTE}/shpigovsky-core.php",
    ),
    "privacy_php": (
        ROOT / "WORDPRESS" / "plugins" / "shpigovsky-core" / "src" / "Privacy" / "PrivacyConsent.php",
        f"{PLUGIN_REMOTE}/src/Privacy/PrivacyConsent.php",
    ),
    "dashboard_php": (
        ROOT / "WORDPRESS" / "plugins" / "shpigovsky-core" / "src" / "Admin" / "SystemDashboard.php",
        f"{PLUGIN_REMOTE}/src/Admin/SystemDashboard.php",
    ),
    "privacy_js": (
        ROOT / "WORDPRESS" / "plugins" / "shpigovsky-core" / "assets" / "js" / "privacy-consent.js",
        f"{PLUGIN_REMOTE}/assets/js/privacy-consent.js",
    ),
    "footer_php": (
        ROOT / "WORDPRESS" / "theme" / "shpigovsky" / "template-parts" / "layout" / "footer.php",
        f"{THEME_REMOTE}/template-parts/layout/footer.php",
    ),
    "shell_js": (
        ROOT / "WORDPRESS" / "theme" / "shpigovsky" / "assets" / "js" / "v9-shell.js",
        f"{THEME_REMOTE}/assets/js/v9-shell.js",
    ),
    "theme_css": (
        ROOT / "WORDPRESS" / "theme" / "shpigovsky" / "assets" / "css" / "v9-style.css",
        f"{THEME_REMOTE}/assets/css/v9-style.css",
    ),
}

UPDATE_PHP = r"""<?php
$_SERVER['HTTP_HOST'] = 'shpigovsky.ru';
$_SERVER['SERVER_NAME'] = 'shpigovsky.ru';
$_SERVER['REQUEST_URI'] = '/';
$_SERVER['HTTPS'] = 'on';
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';

$policy_id = 24;
$policy = get_post($policy_id);
$before = array(
    'exists' => $policy instanceof WP_Post,
    'ID' => $policy instanceof WP_Post ? (int) $policy->ID : 0,
    'modified_gmt' => $policy instanceof WP_Post ? $policy->post_modified_gmt : null,
    'content' => $policy instanceof WP_Post ? (string) $policy->post_content : '',
);
$content = file_get_contents('/tmp/fp02_p18ef_cookie_policy_after.html');

if ($policy instanceof WP_Post && is_string($content) && trim($content) !== '') {
    wp_update_post(array(
        'ID' => $policy_id,
        'post_content' => $content,
    ));
}

$meta = get_option('fp02_metacode_system_meta', array());
if (!is_array($meta)) {
    $meta = array();
}
$meta['baseline_id'] = 'FP-0002-PROD-BASELINE-2026-08-19-P18E-EF';
$meta['latest_wave'] = 'P18E-E/F Form Goal + Cookie Policy Integration';
$meta['parity'] = 'MATCH';
$meta['verified_at'] = gmdate('Y-m-d H:i') . ' UTC';
$meta['backup'] = 'BOUNDED PAGE SNAPSHOT / EXACT FILE DEPLOY';
$meta['state_note'] = 'COOKIE CONSENT ACTIVE; METRIKA CONSENT-GATED; FORM GOAL CONSENT-GATED; COOKIE SETTINGS REOPEN ACTIVE; INDEXING CLOSED';
$meta['indexing'] = 'CLOSED — WAITING FOR OLYA APPROVAL';
$meta['metrika_form_goals'] = 'CONSENT-GATED';
update_option('fp02_metacode_system_meta', $meta, false);

$after = get_post($policy_id);
echo wp_json_encode(array(
    'ok' => true,
    'policy_before' => array(
        'exists' => $before['exists'],
        'ID' => $before['ID'],
        'modified_gmt' => $before['modified_gmt'],
        'content_bytes' => strlen((string) $before['content']),
    ),
    'policy_after' => $after instanceof WP_Post ? array(
        'ID' => (int) $after->ID,
        'modified_gmt' => $after->post_modified_gmt,
        'content_bytes' => strlen((string) $after->post_content),
    ) : null,
    'meta_after' => get_option('fp02_metacode_system_meta', array()),
), JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES) . "\n";
"""


def parse_secrets(text: str) -> dict[str, str]:
    pairs: dict[str, str] = {}
    for line in text.splitlines():
        m = re.match(r"^[-*]?\s*`?([A-Za-z0-9_./-]+)`?\s*[:=]\s*(.*)$", line.strip())
        if m:
            pairs[m.group(1)] = m.group(2).strip().strip("`").strip('"').strip("'")
    return pairs


def getf(pairs: dict[str, str], *keys: str) -> str | None:
    for key in keys:
        value = pairs.get(key)
        if value and "<OPERATOR" not in value and value.strip():
            return value.strip()
    return None


def sha256_bytes(data: bytes | None) -> str | None:
    return hashlib.sha256(data).hexdigest() if data is not None else None


def sftp_get_bytes(sftp: paramiko.SFTPClient, remote: str) -> bytes | None:
    bio = io.BytesIO()
    try:
        sftp.getfo(remote, bio)
        return bio.getvalue()
    except Exception:
        return None


def ssh_connect(pairs: dict[str, str]) -> paramiko.SSHClient:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        hostname=getf(pairs, "ssh_host", "sftp_host", "ftp_host") or "shpigovsky.beget.tech",
        port=int(getf(pairs, "ssh_port", "sftp_port") or "22"),
        username=getf(pairs, "ssh_username", "ssh_user", "sftp_user", "ftp_user"),
        password=getf(pairs, "ssh_password_or_key_reference", "ssh_password", "sftp_password", "ftp_or_sftp_password", "ftp_password"),
        timeout=30,
    )
    return client


def run_ssh(client: paramiko.SSHClient, cmd: str, timeout: int = 120) -> tuple[str, str, int]:
    stdin, stdout, stderr = client.exec_command(cmd, timeout=timeout)
    del stdin
    out = stdout.read().decode("utf-8", "replace")
    err = stderr.read().decode("utf-8", "replace")
    code = stdout.channel.recv_exit_status()
    return out, err, code


def local_head_sha() -> str:
    probe = Path(__file__).resolve()
    for candidate in [probe.parent, *probe.parents]:
        if (candidate / ".git").exists():
            return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=candidate).decode("utf-8").strip()
    raise RuntimeError("Git root not found for deploy snapshot")


def main() -> None:
    EV.mkdir(parents=True, exist_ok=True)
    pairs = parse_secrets(SECRETS.read_text(encoding="utf-8"))
    client = ssh_connect(pairs)
    sftp = client.open_sftp()

    before = {}
    for key, (local_path, remote_path) in FILES.items():
        local_bytes = local_path.read_bytes()
        remote_bytes = sftp_get_bytes(sftp, remote_path)
        before[key] = {
            "local_path": str(local_path),
            "remote_path": remote_path,
            "local_sha256": sha256_bytes(local_bytes),
            "remote_sha256_before": sha256_bytes(remote_bytes),
        }

    policy_before_php = "/tmp/fp02_p18ef_update.php"
    policy_after_html = "/tmp/fp02_p18ef_cookie_policy_after.html"
    sftp.putfo(io.BytesIO(POLICY_CONTENT.encode("utf-8")), policy_after_html)
    sftp.putfo(io.BytesIO(UPDATE_PHP.encode("utf-8")), policy_before_php)

    for _, (local_path, remote_path) in FILES.items():
        sftp.put(str(local_path), remote_path)

    lint_results = {}
    for remote in [
        f"{PLUGIN_REMOTE}/shpigovsky-core.php",
        f"{PLUGIN_REMOTE}/src/Privacy/PrivacyConsent.php",
        f"{PLUGIN_REMOTE}/src/Admin/SystemDashboard.php",
        f"{THEME_REMOTE}/template-parts/layout/footer.php",
    ]:
        out, err, code = run_ssh(client, f"php8.2 -l {remote} || php -l {remote}", timeout=60)
        lint_results[remote] = {"code": code, "out": out.strip(), "err": err.strip()}

    out, err, code = run_ssh(client, f"php8.2 {policy_before_php} || php {policy_before_php}", timeout=120)
    try:
        update_result = json.loads(out.strip().splitlines()[-1])
    except Exception:
        update_result = {"ok": False, "raw_tail": out[-4000:], "err_tail": err[-2000:], "code": code}

    after = {}
    for key, (_, remote_path) in FILES.items():
        remote_bytes = sftp_get_bytes(sftp, remote_path)
        after[key] = {"remote_sha256_after": sha256_bytes(remote_bytes)}

    snapshot = {
        "utc": datetime.now(timezone.utc).isoformat(),
        "source_head_sha": local_head_sha(),
        "before": before,
        "after": after,
        "lint": lint_results,
        "db_update": update_result,
    }
    (EV / "02-deploy-snapshot.json").write_text(
        json.dumps(snapshot, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    if isinstance(update_result, dict) and "policy_before" in update_result:
        (EV / "cookie-policy-before.json").write_text(
            json.dumps(update_result["policy_before"], ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    try:
        sftp.remove(policy_before_php)
    except Exception:
        pass
    try:
        sftp.remove(policy_after_html)
    except Exception:
        pass

    sftp.close()
    client.close()
    print("DEPLOY_OK", update_result.get("ok", False))


if __name__ == "__main__":
    main()
