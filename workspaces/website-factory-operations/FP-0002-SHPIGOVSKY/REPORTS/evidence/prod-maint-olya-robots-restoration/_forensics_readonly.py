# -*- coding: utf-8 -*-
"""PROD-MAINT Olya robots: live forensics (read-only). Never mutates robots."""
from __future__ import annotations

import hashlib
import io
import json
import re
from datetime import datetime, timezone
from pathlib import Path

import paramiko
import requests

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
EV = Path(__file__).resolve().parent
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
UA = "FP-0002-PROD-MAINT-OLYA-ROBOTS/1.0"


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


def main() -> None:
    EV.mkdir(parents=True, exist_ok=True)
    pairs = parse_secrets(SECRETS.read_text(encoding="utf-8", errors="replace"))

    response = requests.get(
        "https://shpigovsky.ru/robots.txt",
        headers={"User-Agent": UA},
        timeout=30,
    )
    body = response.content
    http = {
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "status": response.status_code,
        "final_url": str(response.url),
        "content_type": response.headers.get("Content-Type"),
        "headers": {
            key: value
            for key, value in response.headers.items()
            if key.lower()
            in (
                "content-type",
                "server",
                "x-robots-tag",
                "cache-control",
                "last-modified",
                "etag",
                "content-length",
            )
        },
        "sha256": hashlib.sha256(body).hexdigest(),
        "bytes": len(body),
        "body_text": body.decode("utf-8", errors="replace"),
    }
    (EV / "01-live-robots-http.json").write_text(
        json.dumps(http, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (EV / "01-live-robots-before.txt").write_bytes(body)

    sitemap_response = requests.get(
        "https://shpigovsky.ru/wp-sitemap.xml",
        headers={"User-Agent": UA},
        timeout=30,
        allow_redirects=True,
    )
    sitemap_text = sitemap_response.text
    sitemap = {
        "status": sitemap_response.status_code,
        "final_url": str(sitemap_response.url),
        "content_type": sitemap_response.headers.get("Content-Type"),
        "bytes": len(sitemap_response.content),
        "sha256": hashlib.sha256(sitemap_response.content).hexdigest(),
        "head": sitemap_text[:500],
        "has_staging": any(
            token in sitemap_text
            for token in ("beget.tech", "localhost", "shpigovsky.test")
        ),
    }
    (EV / "01-sitemap-http.json").write_text(
        json.dumps(sitemap, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

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

    def run(cmd: str, timeout: int = 90) -> tuple[str, str, int]:
        _stdin, stdout, stderr = client.exec_command(cmd, timeout=timeout)
        out = stdout.read().decode("utf-8", errors="replace")
        err = stderr.read().decode("utf-8", errors="replace")
        code = stdout.channel.recv_exit_status()
        return out, err, code

    phys: dict = {"path": f"{DOCROOT}/robots.txt"}
    try:
        st = sftp.stat(f"{DOCROOT}/robots.txt")
        phys["exists"] = True
        phys["size"] = st.st_size
        phys["mtime"] = st.st_mtime
        bio = io.BytesIO()
        sftp.getfo(f"{DOCROOT}/robots.txt", bio)
        data = bio.getvalue()
        phys["sha256"] = hashlib.sha256(data).hexdigest()
        phys["body"] = data.decode("utf-8", errors="replace")
        (EV / "01-physical-robots-before.txt").write_bytes(data)
    except OSError as exc:
        phys["exists"] = False
        phys["error"] = str(exc)

    out, _err, _code = run(
        f"ls -la {DOCROOT}/robots.txt* 2>&1; "
        f"stat -c '%U:%G %a %y %n' {DOCROOT}/robots.txt 2>&1; "
        f"ls -la {DOCROOT}/wp-content/plugins/shpigovsky-core/src/Admin/Indexing*.php 2>&1"
    )
    phys["ls"] = out
    (EV / "01-physical-robots-meta.json").write_text(
        json.dumps(phys, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    php = r"""<?php
$_SERVER['HTTP_HOST']='shpigovsky.ru';
$_SERVER['SERVER_NAME']='shpigovsky.ru';
$_SERVER['HTTPS']='on';
$_SERVER['REQUEST_URI']='/';
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
$path = ABSPATH . 'robots.txt';
$exists = is_file($path);
$body = $exists ? file_get_contents($path) : null;
$snap = class_exists('Shpigovsky\\Core\\Admin\\IndexingState') ? Shpigovsky\\Core\\Admin\\IndexingState::snapshot() : null;
$ic_open = class_exists('Shpigovsky\\Core\\Admin\\IndexingControl') ? Shpigovsky\\Core\\Admin\\IndexingControl::robots_body(true) : null;
$ic_closed = class_exists('Shpigovsky\\Core\\Admin\\IndexingControl') ? Shpigovsky\\Core\\Admin\\IndexingControl::robots_body(false) : null;
$filters = $GLOBALS['wp_filter']['robots_txt'] ?? null;
$cb = array();
if ($filters) {
  foreach ($filters->callbacks as $prio => $list) {
    foreach ($list as $id => $f) {
      $fn = $f['function'];
      if (is_string($fn)) $cb[] = array('prio'=>$prio,'fn'=>$fn);
      elseif (is_array($fn)) $cb[] = array('prio'=>$prio,'fn'=>(is_object($fn[0])?get_class($fn[0]):(string)$fn[0]).'::'.(string)$fn[1]);
      else $cb[] = array('prio'=>$prio,'fn'=>'closure_or_other');
    }
  }
}
echo wp_json_encode(array(
  'ok'=>true,
  'core'=> defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null,
  'blog_public'=>(int)get_option('blog_public'),
  'home'=>get_option('home'),
  'siteurl'=>get_option('siteurl'),
  'abspath'=>ABSPATH,
  'robots_physical_exists'=>$exists,
  'robots_physical_bytes'=>$exists?strlen($body):0,
  'robots_physical_sha'=>$exists?hash('sha256',$body):null,
  'robots_physical_head'=>$exists?substr($body,0,200):null,
  'indexing_snapshot'=>$snap,
  'indexing_control_open_body'=>$ic_open,
  'indexing_control_closed_body'=>$ic_closed,
  'robots_txt_filters'=>$cb,
  'human_authority'=>get_option('fp02_indexing_human_authority'),
  'watchdog_baseline'=>get_option('fp02_indexing_watchdog_baseline'),
), JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES);
echo "\n";
"""
    remote = f"{DOCROOT}/wp-content/uploads/.fp02-olya-robots-forensics.php"
    sftp.putfo(io.BytesIO(php.encode("utf-8")), remote)
    out, err, code = run(f"php8.2 {remote} 2>/dev/null || php {remote}")
    try:
        sftp.remove(remote)
    except OSError:
        pass

    payload: dict
    try:
        payload = json.loads(out.strip().splitlines()[0])
    except Exception:
        payload = {"raw": out, "err": err, "code": code}
    (EV / "01-wp-forensics.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    home = requests.get("https://shpigovsky.ru/", headers={"User-Agent": UA}, timeout=30)
    meta_match = re.search(
        r"meta\s+name=['\"]robots['\"]\s+content=['\"]([^'\"]+)",
        home.text,
        re.I,
    )
    assets = {
        "status": home.status_code,
        "css": re.findall(r'href=["\']([^"\']+\.css[^"\']*)["\']', home.text, re.I)[:10],
        "js": re.findall(r'src=["\']([^"\']+\.js[^"\']*)["\']', home.text, re.I)[:10],
        "img": re.findall(
            r'src=["\']([^"\']+\.(?:png|jpe?g|gif|webp)[^"\']*)["\']', home.text, re.I
        )[:10],
        "x_robots": home.headers.get("X-Robots-Tag"),
        "meta_robots": meta_match.group(1) if meta_match else None,
    }
    (EV / "01-homepage-assets.json").write_text(
        json.dumps(assets, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    print("http_robots_sha", http["sha256"], "bytes", http["bytes"])
    print("sitemap", sitemap["status"], "staging", sitemap["has_staging"])
    print("phys", phys.get("exists"), phys.get("sha256"))
    if isinstance(payload, dict) and payload.get("ok"):
        print("blog_public", payload.get("blog_public"))
        print("core", payload.get("core"))
        print("phys_exists", payload.get("robots_physical_exists"))
        snap = payload.get("indexing_snapshot") or {}
        print("effective", snap.get("effective"))
        print("owner", (snap.get("robots") or {}).get("owner"))
        print(
            "ic_open_head",
            (payload.get("indexing_control_open_body") or "")[:90].replace("\n", "|"),
        )
    else:
        print("wp_forensics_failed", payload)

    sftp.close()
    client.close()
    print("DONE")


if __name__ == "__main__":
    main()
