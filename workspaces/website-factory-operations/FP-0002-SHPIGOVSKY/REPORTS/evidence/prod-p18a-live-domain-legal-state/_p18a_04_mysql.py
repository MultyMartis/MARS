# -*- coding: utf-8 -*-
"""P18A: DB SELECT for home/siteurl/legal meta. No secrets in evidence."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import paramiko

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
EV = Path(r"X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\REPORTS\evidence\prod-p18a-live-domain-legal-state")
PREFIX = "fp02_"


def parse_secrets(text: str) -> dict:
    pairs = {}
    for line in text.splitlines():
        m = __import__("re").match(r"^[-*]?\s*`?([A-Za-z0-9_./-]+)`?\s*[:=]\s*(.*)$", line.strip())
        if m:
            pairs[m.group(1)] = m.group(2).strip().strip("`").strip('"').strip("'")
    return pairs


def getf(pairs, *keys):
    for k in keys:
        v = pairs.get(k)
        if v and "<OPERATOR" not in v and v.strip():
            return v.strip()
    return None


SQL = r"""
SELECT option_name, option_value
FROM {p}options
WHERE option_name IN ('home','siteurl','blog_public','wp_page_for_privacy_policy','permalink_structure','blogname','blogdescription');

SELECT '---LEGAL-PAGES---';
SELECT p.ID, p.post_title, p.post_name, p.post_status, p.post_modified_gmt, pm.meta_value AS template,
       CHAR_LENGTH(p.post_content) AS content_bytes,
       (p.post_content LIKE '%[ДЕМО%') AS has_demo_bracket,
       (p.post_content LIKE '%ДЕМО:%') AS has_demo_colon,
       (p.post_content LIKE '%Lorem ipsum%') AS has_lorem
FROM {p}posts p
INNER JOIN {p}postmeta pm ON pm.post_id=p.ID AND pm.meta_key='_wp_page_template'
WHERE pm.meta_value='page-templates/legal.php' AND p.post_status NOT IN ('trash')
ORDER BY p.ID;

SELECT '---LEGAL-META---';
SELECT pm.post_id, pm.meta_key, pm.meta_value
FROM {p}postmeta pm
INNER JOIN {p}posts p ON p.ID=pm.post_id
INNER JOIN {p}postmeta t ON t.post_id=p.ID AND t.meta_key='_wp_page_template' AND t.meta_value='page-templates/legal.php'
WHERE (pm.meta_key LIKE 'legal_%' OR pm.meta_key LIKE '_legal_%' OR pm.meta_key IN ('demo_marker','legal_demo'))
ORDER BY pm.post_id, pm.meta_key;

SELECT '---REVISIONS---';
SELECT r.ID, r.post_parent, r.post_name, r.post_status, r.post_modified_gmt
FROM {p}posts r
WHERE r.post_type='revision' AND r.post_parent IN (
  SELECT p.ID FROM {p}posts p
  INNER JOIN {p}postmeta pm ON pm.post_id=p.ID AND pm.meta_key='_wp_page_template' AND pm.meta_value='page-templates/legal.php'
)
ORDER BY r.post_parent, r.ID DESC;

SELECT '---PLACEHOLDER-POSTS---';
SELECT ID, post_title, post_name, post_status, post_type
FROM {p}posts
WHERE post_content LIKE '%[ДЕМО%' AND post_type IN ('page','post') AND post_status NOT IN ('trash','auto-draft')
ORDER BY ID;

SELECT '---PLACEHOLDER-META---';
SELECT post_id, meta_key
FROM {p}postmeta
WHERE meta_value LIKE '%[ДЕМО%' AND meta_key NOT LIKE '\\_%'
ORDER BY post_id, meta_key;
"""


def main() -> int:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    pairs = parse_secrets(SECRETS.read_text(encoding="utf-8"))
    db_name = getf(pairs, "db_name")
    db_user = getf(pairs, "db_user")
    db_pass = getf(pairs, "db_password")
    db_host = getf(pairs, "db_host", "mysql_host") or "localhost"
    sql = SQL.format(p=PREFIX)
    remote_sql = "/tmp/fp02_p18a_legal.sql"
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        hostname=getf(pairs, "ssh_host"),
        port=int(getf(pairs, "ssh_port") or "22"),
        username=getf(pairs, "ssh_username"),
        password=getf(pairs, "ssh_password_or_key_reference"),
        timeout=60,
        allow_agent=False,
        look_for_keys=False,
    )
    sftp = client.open_sftp()
    with sftp.file(remote_sql, "w") as fh:
        fh.write(sql)
    cmd = (
        f"MYSQL_PWD={db_pass} mysql --default-character-set=utf8mb4 "
        f"-h {db_host} -u {db_user} {db_name} < {remote_sql}"
    )
    stdin, stdout, stderr = client.exec_command(cmd, timeout=60)
    out = stdout.read().decode("utf-8", errors="replace")
    err = stderr.read().decode("utf-8", errors="replace")
    code = stdout.channel.recv_exit_status()
    try:
        sftp.remove(remote_sql)
    except OSError:
        pass
    # redact any accidental password echo
    err = err.replace(db_pass or "", "***")
    (EV / "DB-LEGAL-INTAKE.txt").write_text(out + (f"\n---stderr---\n{err}\nexit={code}\n" if err or code else ""), encoding="utf-8")
    print("mysql exit", code, "out_len", len(out))
    print(out[:4000])
    sftp.close()
    client.close()
    (EV / "DB-LEGAL-INTAKE.meta.json").write_text(
        json.dumps({"generated_at": now, "php_avoided": "wp-load CLI fatal; used mysql SELECT", "exit": code}, indent=2)
        + "\n",
        encoding="utf-8",
    )
    return 0 if code == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
