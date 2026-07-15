#!/usr/bin/env python3
"""FP-0002 V9-06E29C — probe Excel + WP inventory (read-only)."""
from __future__ import annotations

import json
import re
from pathlib import Path

import openpyxl
import pymysql

EXCEL = Path(
    r"X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/02_CONTENT/Предварит структура и спрос.xlsx"
)
OUT = Path(
    r"X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06e29c-excel-structure-completion"
)
DB = "mars_wp_fp0002"
PREFIX = "fp02_"


def db():
    return pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database=DB,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )


def read_excel():
    wb = openpyxl.load_workbook(EXCEL, read_only=True, data_only=True)
    ws = wb["Структура"]
    rows = list(ws.iter_rows(values_only=True))
    header = rows[0] if rows else ()
    data_rows = rows[1:]
    return header, data_rows


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    header, data_rows = read_excel()
    conn = db()
    cur = conn.cursor()
    cur.execute(
        f"""
        SELECT ID, post_title, post_name, post_type, post_status, post_parent
        FROM {PREFIX}posts
        WHERE post_type IN ('page','service','post')
          AND post_status IN ('publish','draft','private','future')
        ORDER BY post_type, ID
        """
    )
    posts = cur.fetchall()
    cur.execute(
        f"""
        SELECT post_id, meta_value
        FROM {PREFIX}postmeta
        WHERE meta_key = '_wp_page_template'
        """
    )
    templates = {int(r["post_id"]): r["meta_value"] for r in cur.fetchall()}
    cur.execute(
        f"""
        SELECT post_id, meta_key, meta_value
        FROM {PREFIX}postmeta
        WHERE meta_key IN ('service_layout_variant','_service_layout_variant')
        """
    )
    service_meta = cur.fetchall()
    conn.close()

    payload = {
        "excel_header": list(header) if header else [],
        "excel_row_count": len(data_rows),
        "excel_sample_rows": [list(r) for r in data_rows[:20]],
        "posts": posts,
        "templates": templates,
        "service_meta": service_meta,
    }
    out = OUT / "probe-inventory.json"
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2, default=str) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    print("HEADER:", header)
    print("POSTS:", len(posts))
    for p in posts:
        tpl = templates.get(p["ID"], "")
        print(
            p["ID"],
            p["post_type"],
            p["post_name"],
            p["post_status"],
            f"parent={p['post_parent']}",
            tpl,
        )


if __name__ == "__main__":
    main()
