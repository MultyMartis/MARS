#!/usr/bin/env python3
"""Corrective hero seed: move alcohol hero from wrong ID 77 to 74."""
import json
import subprocess
from pathlib import Path

import pymysql

PHP = Path(r"X:/MARS-Localhost/laragon/bin/php/php-8.3.30-Win32-vs16-x64/php.exe")
EVIDENCE = Path(
    r"X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06e7b-hero-system-finalization-scope-reconciliation"
)

conn = pymysql.connect(host="127.0.0.1", user="root", password="", database="mars_wp_fp0002", charset="utf8mb4")
cur = conn.cursor()
# Reuse attachment 305 on correct alcohol service (74); clear mis-assigned 77
cur.execute("SELECT meta_value FROM fp02_postmeta WHERE post_id=77 AND meta_key='hero_media'")
wrong = cur.fetchone()
att_id = wrong[0] if wrong else None
actions = []
if att_id:
    cur.execute("DELETE FROM fp02_postmeta WHERE post_id=77 AND meta_key IN ('hero_media','_hero_media')")
    actions.append({"action": "cleared_wrong_77", "attachment_was": att_id})
conn.commit()
conn.close()

# PHP update_field for 74
fix_php = r"""<?php
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
$att = 305;
$r = update_field('hero_media', (int)$att, 74);
echo json_encode(['update_74' => (bool)$r, 'get' => get_field('hero_media', 74)], JSON_UNESCAPED_UNICODE);
"""
fix_path = EVIDENCE / "_fix_alcohol_seed.php"
fix_path.write_text(fix_php, encoding="utf-8")
proc = subprocess.run([str(PHP), str(fix_path)], capture_output=True, text=True)
result = {"actions": actions, "php_stdout": proc.stdout.strip(), "php_exit": proc.returncode}

conn = pymysql.connect(host="127.0.0.1", user="root", password="", database="mars_wp_fp0002", charset="utf8mb4")
cur = conn.cursor()
for oid in [74, 77]:
    cur.execute("SELECT meta_value FROM fp02_postmeta WHERE post_id=%s AND meta_key='hero_media'", (oid,))
    row = cur.fetchone()
    result[f"hero_media_{oid}"] = row[0] if row else None
conn.close()

out = EVIDENCE / "hero-alcohol-id-correction.json"
out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, ensure_ascii=False, indent=2))
