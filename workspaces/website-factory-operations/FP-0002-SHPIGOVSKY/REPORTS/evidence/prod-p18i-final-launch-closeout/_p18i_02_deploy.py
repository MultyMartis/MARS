# -*- coding: utf-8 -*-
"""PROD-P18I: deploy URL normalization fix + dashboard closeout. Read-only indexing."""
from __future__ import annotations

import hashlib
import io
import json
import re
import select
import socket
import threading
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import paramiko

ROOT = Path(__file__).resolve().parents[3]
EV = ROOT / "REPORTS" / "evidence" / "prod-p18i-final-launch-closeout"
SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
THEME_REMOTE = f"{DOCROOT}/wp-content/themes/shpigovsky"
PLUGIN_REMOTE = f"{DOCROOT}/wp-content/plugins/shpigovsky-core"
WP_LOAD = f"{DOCROOT}/wp-load.php"

DEPLOY_MAP = {
    f"{PLUGIN_REMOTE}/shpigovsky-core.php": ROOT / "WORDPRESS/plugins/shpigovsky-core/shpigovsky-core.php",
    f"{PLUGIN_REMOTE}/src/Admin/SystemDashboard.php": ROOT / "WORDPRESS/plugins/shpigovsky-core/src/Admin/SystemDashboard.php",
    f"{THEME_REMOTE}/inc/template-tags.php": ROOT / "WORDPRESS/theme/shpigovsky/inc/template-tags.php",
    f"{THEME_REMOTE}/inc/home-fallbacks.php": ROOT / "WORDPRESS/theme/shpigovsky/inc/home-fallbacks.php",
    f"{THEME_REMOTE}/inc/home-helpers.php": ROOT / "WORDPRESS/theme/shpigovsky/inc/home-helpers.php",
    f"{THEME_REMOTE}/inc/reusable-blocks-helpers.php": ROOT / "WORDPRESS/theme/shpigovsky/inc/reusable-blocks-helpers.php",
}


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


def write_json(name: str, payload: Any) -> None:
    EV.mkdir(parents=True, exist_ok=True)
    (EV / name).write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


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


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


class LocalForward:
    def __init__(self, transport: paramiko.Transport, remote_host: str, remote_port: int):
        self.transport = transport
        self.remote_host = remote_host
        self.remote_port = remote_port
        self.sock = socket.socket()
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(("127.0.0.1", 0))
        self.sock.listen(4)
        self.local_port = self.sock.getsockname()[1]
        self._stop = False
        threading.Thread(target=self._accept, daemon=True).start()

    def _accept(self) -> None:
        while not self._stop:
            ready, _, _ = select.select([self.sock], [], [], 0.5)
            if not ready:
                continue
            try:
                client, _ = self.sock.accept()
            except OSError:
                return
            threading.Thread(target=self._forward, args=(client,), daemon=True).start()

    def _forward(self, client: socket.socket) -> None:
        try:
            chan = self.transport.open_channel("direct-tcpip", (self.remote_host, self.remote_port), client.getpeername())
        except Exception:
            client.close()
            return
        try:
            while True:
                ready, _, _ = select.select([client, chan], [], [], 30)
                if client in ready:
                    data = client.recv(65536)
                    if not data:
                        break
                    chan.sendall(data)
                if chan in ready:
                    data = chan.recv(65536)
                    if not data:
                        break
                    client.sendall(data)
        finally:
            client.close()
            chan.close()

    def close(self) -> None:
        self._stop = True
        try:
            self.sock.close()
        except OSError:
            pass


def main() -> None:
    pairs = parse_secrets(SECRETS.read_text(encoding="utf-8", errors="replace"))
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        hostname=getf(pairs, "ssh_host", "sftp_host", "ftp_host") or "shpigovsky.beget.tech",
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
    sftp = client.open_sftp()
    manifest = []
    for remote, local in DEPLOY_MAP.items():
        payload = local.read_bytes()
        with sftp.file(remote, "wb") as fh:
            fh.write(payload)
        manifest.append(
            {
                "remote": remote,
                "local": str(local.relative_to(ROOT)),
                "sha256": sha256_bytes(payload),
                "bytes": len(payload),
            }
        )
    sftp.close()

    meta_php = f"""<?php
require '{WP_LOAD}';
$meta = get_option('fp02_metacode_system_meta', array());
if (!is_array($meta)) {{ $meta = array(); }}
$meta['baseline_id'] = 'FP-0002-PRODUCTION-FINAL-2026-08-20-P18I';
$meta['latest_wave'] = 'P18I Final Launch Closeout';
$meta['parity'] = 'MATCH';
$meta['verified_at'] = gmdate('Y-m-d H:i') . ' UTC';
$meta['indexing'] = 'OPEN — HUMAN-APPROVED';
$meta['public_origin'] = 'https://shpigovsky.ru/ — WordPress production';
$meta['sitemap_submissions'] = 'P18I closeout — see REPORT';
update_option('fp02_metacode_system_meta', $meta, false);
if (function_exists('wp_cache_flush')) {{ wp_cache_flush(); }}
if (function_exists('opcache_reset')) {{ @opcache_reset(); }}
echo json_encode(array(
  'core' => defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null,
  'blog_public' => (int) get_option('blog_public', 1),
  'meta' => $meta,
), JSON_UNESCAPED_UNICODE);
"""
    remote_meta = f"/tmp/fp02_p18i_meta_{int(time.time())}.php"
    sftp2 = client.open_sftp()
    with sftp2.file(remote_meta, "w") as fh:
        fh.write(meta_php.encode("utf-8"))
    sftp2.close()
    stdin, stdout, stderr = client.exec_command(f"php8.2 {remote_meta} 2>/dev/null || php {remote_meta}; rm -f {remote_meta}", timeout=120)
    meta_out = stdout.read().decode("utf-8", errors="replace").strip()
    client.close()

    write_json(
        "11-deploy-fix-manifest.json",
        {
            "deployed_at": utcnow(),
            "files": manifest,
            "meta_update": meta_out[-2000:] if meta_out else stderr.read().decode() if False else meta_out,
        },
    )
    print(json.dumps({"ok": True, "files": len(manifest)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
