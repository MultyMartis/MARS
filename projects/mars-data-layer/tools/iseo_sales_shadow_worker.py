#!/usr/bin/env python3
"""ISEO Sales Sheets → PG shadow worker (VEESP host). No secrets/PII in stdout."""
from __future__ import annotations

import base64
import hashlib
import json
import os
import re
import sqlite3
import subprocess
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

MODE = os.environ.get("ISEO_MODE", "inventory")
RAW_ID = os.environ.get("ISEO_RAW_ID", "1Ba1iveHphZqHSTjkHdih0Aqekk5gmonELEX5dKXZ2NU")
CLEAN_ID = os.environ.get("ISEO_CLEAN_ID", "1aeIWHeaqHwgJSKLCFZP8M4qG5y9qmOcPt6rvSWsltRU")
CRED_ID = os.environ.get("ISEO_CRED_ID", "nRfNJVn6SEziII8k")
PG_USER = os.environ.get("POSTGRES_USER", "mars_admin")
PG_DB = os.environ.get("POSTGRES_DB", "mars")
PG_CT = os.environ.get("ISEO_PG_CONTAINER", "mars-postgres")
N8N_DB = "/opt/n8n/n8n_data/database.sqlite"
N8N_CFG = "/opt/n8n/n8n_data/config"
SNAP = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
WORK = Path(f"/tmp/mars-iseo-shadow-{SNAP}")
WORK.mkdir(parents=True, exist_ok=True)

ALLOWED_STATUS = {
    "new", "pending", "reviewing", "contacted", "waiting_client",
    "qualified", "not_target", "processed", "spam", "closed", "error", "reopened",
}
STATUS_MAP = {
    "done": "processed", "completed": "processed", "complete": "processed",
    "in_progress": "reviewing", "in-progress": "reviewing", "working": "reviewing",
    "wait": "waiting_client", "waiting": "waiting_client",
    "reject": "not_target", "rejected": "not_target", "not target": "not_target",
    "duplicate": "processed", "dup": "processed",
}
SECRET_CFG = re.compile(r"(token|secret|password|oauth|refresh|client_secret|api[_-]?key|bot[_-]?token)", re.I)
PII_EMAIL = re.compile(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", re.I)
PII_PHONE = re.compile(r"\+?\d[\d\s\-()]{7,}\d")


def jdump(path: Path, obj: Any) -> None:
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2, default=str), encoding="utf-8")


def sha8(s: str) -> str:
    return hashlib.sha256((s or "").encode("utf-8", "replace")).hexdigest()[:8]


def redact(v: Any) -> Any:
    if v is None:
        return None
    s = str(v)
    # Do not treat ISO timestamps / UUIDs as phone numbers
    if re.match(r"^\d{4}-\d{2}-\d{2}[T ]", s) or re.match(r"^[0-9a-f-]{16,}$", s, re.I):
        return s
    s = PII_EMAIL.sub(lambda m: f"email_h:{sha8(m.group(0).lower())}", s)
    s = PII_PHONE.sub(lambda m: f"phone_h:{sha8(re.sub(r'\D', '', m.group(0)))}", s)
    return s


def sql_lit(v: Any) -> str:
    if v is None:
        return "NULL"
    if isinstance(v, bool):
        return "TRUE" if v else "FALSE"
    if isinstance(v, (int, float)) and not isinstance(v, bool):
        return str(v)
    if isinstance(v, (dict, list)):
        s = json.dumps(v, ensure_ascii=False, default=str)
        return "'" + s.replace("'", "''") + "'::jsonb"
    return "'" + str(v).replace("'", "''") + "'"


def parse_ts(v: Any) -> str | None:
    if v is None or str(v).strip() == "":
        return None
    s = str(v).strip()
    if s.endswith("Z") or "+00:00" in s or re.search(r"[+-]\d{2}:\d{2}$", s):
        ss = s.replace("Z", "+00:00")
        try:
            return datetime.fromisoformat(ss).isoformat()
        except ValueError:
            pass
    for fmt in (
        "%Y-%m-%dT%H:%M:%S.%f", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S",
        "%d.%m.%Y %H:%M:%S", "%d.%m.%Y %H:%M", "%Y-%m-%d",
    ):
        try:
            # Naive Sheets timestamps treated as Europe/Moscow (+03:00 fixed offset for import)
            return datetime.strptime(s, fmt).isoformat() + "+03:00"
        except ValueError:
            continue
    return None


def map_status(v: Any) -> tuple[str, str]:
    raw = (str(v).strip().lower() if v is not None else "")
    if not raw:
        return "new", "defaulted_empty"
    if raw in ALLOWED_STATUS:
        return raw, "exact"
    if raw in STATUS_MAP:
        return STATUS_MAP[raw], f"mapped_from:{raw}"
    return "error", f"unmapped:{raw}"


def decrypt_n8n(blob_b64: str, key: str) -> bytes:
    raw = base64.b64decode(blob_b64)
    if not raw.startswith(b"Salted__"):
        raise RuntimeError("cipher_not_salted")
    with tempfile.NamedTemporaryFile(delete=False) as tf:
        tf.write(raw)
        enc_path = tf.name
    try:
        p = subprocess.run(
            ["openssl", "enc", "-d", "-aes-256-cbc", "-md", "md5", "-pass", f"pass:{key}", "-in", enc_path],
            capture_output=True,
        )
        if p.returncode == 0 and p.stdout:
            return p.stdout
        # pure python fallback
        salt = raw[8:16]
        data = raw[16:]
        keyb = key.encode("utf-8")
        d = b""
        prev = b""
        while len(d) < 48:
            prev = hashlib.md5(prev + keyb + salt).digest()
            d += prev
        aes_key, iv = d[:32], d[32:48]
        from Crypto.Cipher import AES  # type: ignore
        from Crypto.Util.Padding import unpad  # type: ignore
        return unpad(AES.new(aes_key, AES.MODE_CBC, iv).decrypt(data), 16)
    finally:
        try:
            os.unlink(enc_path)
        except OSError:
            pass


def load_google_token() -> str:
    cfg = json.loads(Path(N8N_CFG).read_text(encoding="utf-8"))
    enc_key = cfg["encryptionKey"]
    con = sqlite3.connect(N8N_DB)
    row = con.execute("SELECT data FROM credentials_entity WHERE id=?", (CRED_ID,)).fetchone()
    con.close()
    if not row:
        raise RuntimeError("cred_missing")
    data = json.loads(decrypt_n8n(row[0], enc_key).decode("utf-8"))
    tok = data.get("oauthTokenData") or data
    access = tok.get("access_token")
    refresh = tok.get("refresh_token")
    client_id = data.get("clientId") or data.get("client_id")
    client_secret = data.get("clientSecret") or data.get("client_secret")
    if refresh and client_id and client_secret:
        body = urllib.parse.urlencode({
            "client_id": client_id,
            "client_secret": client_secret,
            "refresh_token": refresh,
            "grant_type": "refresh_token",
        }).encode()
        req = urllib.request.Request("https://oauth2.googleapis.com/token", data=body, method="POST")
        with urllib.request.urlopen(req, timeout=60) as resp:
            access = json.loads(resp.read().decode()).get("access_token", access)
    if not access:
        raise RuntimeError("no_access_token")
    return access


def sheets_get(token: str, path: str, params: dict[str, str] | None = None) -> Any:
    q = ("?" + urllib.parse.urlencode(params)) if params else ""
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{path}{q}"
    last_err: Exception | None = None
    for attempt in range(8):
        req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
        try:
            with urllib.request.urlopen(req, timeout=180) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            last_err = e
            if e.code in (429, 500, 502, 503, 504):
                ra = e.headers.get("Retry-After") if e.headers else None
                wait = float(ra) if ra and str(ra).isdigit() else min(60.0, (2 ** attempt) + 0.5)
                time.sleep(wait)
                continue
            raise
    raise RuntimeError(f"sheets_get_failed:{path}:{last_err}")


def fetch_spreadsheet(token: str, sid: str) -> dict[str, Any]:
    meta = sheets_get(token, sid, {"fields": "spreadsheetId,properties.title,sheets.properties"})
    data: dict[str, Any] = {
        "spreadsheetId": sid,
        "title": meta.get("properties", {}).get("title"),
        "tabs": {},
    }
    titles: list[str] = []
    props_by_title: dict[str, Any] = {}
    for sh in meta.get("sheets", []):
        p = sh.get("properties", {})
        title = p.get("title") or ""
        if not title:
            continue
        titles.append(title)
        props_by_title[title] = p

    # Batch-read to reduce quota pressure (Sheets 429 under per-tab GETs)
    for i in range(0, len(titles), 8):
        chunk = titles[i : i + 8]
        qparts = [
            "valueRenderOption=UNFORMATTED_VALUE",
            "dateTimeRenderOption=FORMATTED_STRING",
        ] + [f"ranges={urllib.parse.quote(t, safe='')}" for t in chunk]
        batch = sheets_get(token, f"{sid}/values:batchGet?{'&'.join(qparts)}")
        time.sleep(0.4)
        by_range: dict[str, list] = {}
        for vr in batch.get("valueRanges") or []:
            rng = vr.get("range") or ""
            tab_name = rng.split("!")[0].strip("'")
            by_range[tab_name] = vr.get("values") or []
        for title in chunk:
            p = props_by_title[title]
            rows = by_range.get(title) or []
            headers = [str(h) for h in (rows[0] if rows else [])]
            body = rows[1:] if len(rows) > 1 else []
            records = []
            for ri, r in enumerate(body, start=2):
                rec = {"_sheet_row": ri}
                for j, h in enumerate(headers):
                    rec[h] = r[j] if j < len(r) else ""
                records.append(rec)
            nonempty = sum(1 for r in body if any(str(c).strip() for c in r))
            data["tabs"][title] = {
                "meta": {"title": title, "sheetId": p.get("sheetId"), "index": p.get("index")},
                "headers": headers,
                "row_count_body": len(body),
                "nonempty_rows": nonempty,
                "records": records,
            }
            if title not in by_range:
                data["tabs"][title]["warn"] = "missing_from_batch"
    return data


def classify_row(tab: str, rec: dict[str, Any]) -> str:
    """Classify using stable identity fields — avoid whole-row substring false positives."""
    lid = str(rec.get("lead_id") or "").lower()
    src = str(rec.get("source") or "").lower()
    msgid = str(rec.get("gmail_message_id") or rec.get("source_message_id") or "").lower()
    subj = str(rec.get("email_subject") or rec.get("subject") or "").lower()
    markers = " ".join([lid, src, msgid, subj, str(rec.get("workflow") or "").lower()])
    if (
        src == "synthetic"
        or "synth" in lid
        or msgid.startswith("msg_synth")
        or "synthetic_test" in subj
        or "fixture" in markers
        or str(tab).upper().startswith("TEST_")
    ):
        return "TEST/SYNTHETIC"
    if str(tab).upper().startswith("ARCHIVE"):
        return "ARCHIVE"
    if tab in ("lead-base", "lead-base-processed"):
        return "LEGACY/OBSOLETE"
    if tab == "lead_raw_v2" and not str(rec.get("gmail_message_id") or "").strip():
        return "MALFORMED"
    if tab == "lead_clean_v2" and not str(rec.get("lead_id") or "").strip():
        return "MALFORMED"
    st = str(rec.get("manager_status") or rec.get("lifecycle_status") or rec.get("status") or "").lower()
    if st in ("processed", "closed", "spam", "not_target", "done"):
        return "TERMINAL/HISTORICAL BUSINESS DATA"
    return "ACTIVE BUSINESS DATA"


def g(rec: dict[str, Any], *keys: str) -> Any:
    for k in keys:
        if k in rec and str(rec.get(k) or "").strip() != "":
            return rec.get(k)
    lower = {str(a).lower(): a for a in rec}
    for k in keys:
        kk = lower.get(k.lower())
        if kk is not None and str(rec.get(kk) or "").strip() != "":
            return rec.get(kk)
    return None


def inventory_summary(bundle: dict[str, Any]) -> dict[str, Any]:
    out: dict[str, Any] = {"snapshot_id": SNAP, "cutoff_utc": datetime.now(timezone.utc).isoformat(), "spreadsheets": {}}
    for label, sid in (("RAW", RAW_ID), ("CLEAN", CLEAN_ID)):
        sp = bundle[label]
        tabs_out: dict[str, Any] = {}
        for title, tab in sp["tabs"].items():
            if "error" in tab:
                tabs_out[title] = tab
                continue
            classes = Counter(classify_row(title, r) for r in tab["records"])
            sample = [{k: redact(v) for k, v in list(r.items())[:14]} for r in tab["records"][:3]]
            key_field = None
            for cand in (
                "gmail_message_id", "lead_id", "dedup_key", "event_id",
                "delivery_id", "principal_key", "telegram_user_id", "key",
            ):
                if cand in tab["headers"]:
                    key_field = cand
                    break
            dups = 0
            if key_field:
                c = Counter(
                    str(r.get(key_field) or "").strip()
                    for r in tab["records"]
                    if str(r.get(key_field) or "").strip()
                )
                dups = sum(1 for _, n in c.items() if n > 1)
            tabs_out[title] = {
                "headers": tab["headers"],
                "row_count_body": tab["row_count_body"],
                "nonempty_rows": tab["nonempty_rows"],
                "classification": dict(classes),
                "duplicate_candidate_keys": dups,
                "key_field": key_field,
                "sample_redacted": sample,
            }
        out["spreadsheets"][label] = {"spreadsheetId": sid, "title": sp.get("title"), "tabs": tabs_out}
    return out




def build_transforms(bundle: dict[str, Any]) -> dict[str, Any]:
    raw_tab = bundle["RAW"]["tabs"].get("lead_raw_v2", {})
    clean_tab = bundle["CLEAN"]["tabs"].get("lead_clean_v2", {})
    dedup_tab = bundle["CLEAN"]["tabs"].get("DEDUP_INDEX", {})
    events_tab = bundle["CLEAN"]["tabs"].get("LEAD_EVENTS", {})
    access_tab = bundle["CLEAN"]["tabs"].get("ACCESS_CONTROL") or bundle["CLEAN"]["tabs"].get("ACCESS", {})
    lead_del = bundle["CLEAN"]["tabs"].get("LEAD_DELIVERIES", {})
    rem_del = bundle["CLEAN"]["tabs"].get("REMINDER_DELIVERIES", {})
    cfg_tab = bundle["CLEAN"]["tabs"].get("CONFIG", {})
    err_tab = bundle["CLEAN"]["tabs"].get("ERRORS", {})

    counters: Counter = Counter()
    excluded: list[dict] = []
    unknowns: list[dict] = []
    sql: list[str] = ["BEGIN;", "SET LOCAL search_path TO app_iseo_sales, public;"]

    inbound_by_source: dict[str, dict] = {}
    raw_id_counter: Counter = Counter()
    for rec in raw_tab.get("records", []):
        rid = str(rec.get("gmail_message_id") or "").strip()
        if rid:
            raw_id_counter[rid] += 1
        cls = classify_row("lead_raw_v2", rec)
        counters[f"raw_class_{cls}"] += 1
        if cls in ("TEST/SYNTHETIC", "LEGACY/OBSOLETE"):
            excluded.append({"domain": "inbound", "class": cls, "row": rec.get("_sheet_row")})
            continue
        if cls == "MALFORMED":
            unknowns.append({"domain": "inbound", "reason": "missing_source_id", "row": rec.get("_sheet_row")})
            continue
        src = str(g(rec, "gmail_message_id") or "").strip()
        if not src:
            unknowns.append({"domain": "inbound", "reason": "empty_source", "row": rec.get("_sheet_row")})
            continue
        # Keep latest sheet row for identical source_id (append-history collapse)
        prev = inbound_by_source.get(src)
        if prev is None or int(rec.get("_sheet_row") or 0) >= int(prev.get("_sheet_row") or 0):
            inbound_by_source[src] = rec
    counters["inbound_unique"] = len(inbound_by_source)
    counters["raw_gmail_message_id_unique_all"] = len(raw_id_counter)
    counters["raw_gmail_message_id_dup_keys"] = sum(1 for _, n in raw_id_counter.items() if n > 1)
    counters["raw_rows_total"] = len(raw_tab.get("records", []))

    for src, rec in inbound_by_source.items():
        recv = parse_ts(g(rec, "received_at", "received_ts", "created_at", "timestamp"))
        lead = g(rec, "lead_id")
        raw_text = g(rec, "raw_text", "body", "message_body", "raw")
        subject = g(rec, "subject")
        from_email = g(rec, "from_email", "from", "email_from")
        thread = g(rec, "gmail_thread_id", "thread_id")
        payload = {k: redact(v) for k, v in rec.items() if k != "_sheet_row"}
        pst = str(g(rec, "processing_status", "status") or "processed").lower()
        if pst not in ("received", "processing", "processed", "failed", "deferred", "skipped"):
            pst = "processed"
        sql.append(
            "INSERT INTO app_iseo_sales.inbound_events "
            "(source_system, source_id, gmail_thread_id, received_at, processing_status, lead_id, "
            "raw_payload, raw_text, subject, from_email, workflow_version) VALUES ("
            f"'gmail', {sql_lit(src)}, {sql_lit(thread)}, {sql_lit(recv)}, {sql_lit(pst)}, {sql_lit(lead)}, "
            f"{sql_lit(payload)}, {sql_lit(redact(raw_text) if raw_text else None)}, "
            f"{sql_lit(redact(subject) if subject else None)}, "
            f"{sql_lit(redact(str(from_email)) if from_email else None)}, 'sheets-shadow-import-v1'"
            ") ON CONFLICT (source_system, source_id) DO UPDATE SET "
            "last_seen_at = now(), updated_at = now(), "
            "lead_id = COALESCE(EXCLUDED.lead_id, app_iseo_sales.inbound_events.lead_id), "
            "raw_payload = EXCLUDED.raw_payload, "
            "raw_text = COALESCE(EXCLUDED.raw_text, app_iseo_sales.inbound_events.raw_text);"
        )

    by_lead: dict[str, dict] = {}
    for rec in clean_tab.get("records", []):
        cls = classify_row("lead_clean_v2", rec)
        counters[f"clean_class_{cls}"] += 1
        if cls in ("TEST/SYNTHETIC",):
            excluded.append({"domain": "leads", "class": cls, "row": rec.get("_sheet_row")})
            continue
        lid = str(g(rec, "lead_id") or "").strip()
        if not lid:
            unknowns.append({"domain": "leads", "reason": "missing_lead_id", "row": rec.get("_sheet_row")})
            continue
        prev = by_lead.get(lid)
        if prev is None or int(rec.get("_sheet_row") or 0) >= int(prev.get("_sheet_row") or 0):
            by_lead[lid] = rec
    counters["leads_unique"] = len(by_lead)
    counters["clean_rows"] = len(clean_tab.get("records", []))

    # Partial UNIQUE on source_message_id — keep first lead only per message id
    seen_src_msg: set[str] = set()
    status_hist_src: Counter = Counter()
    status_hist_pg: Counter = Counter()
    for lid, rec in by_lead.items():
        st, how = map_status(g(rec, "manager_status", "status"))
        status_hist_src[str(g(rec, "manager_status", "status") or "").strip() or "<empty>"] += 1
        status_hist_pg[st] += 1
        if how.startswith("unmapped"):
            unknowns.append({"domain": "leads", "reason": how, "lead_id_h": sha8(lid)})
        src_msg = str(g(rec, "source_message_id", "gmail_message_id", "message_id") or "").strip() or None
        if src_msg:
            if src_msg in seen_src_msg:
                counters["leads_source_message_id_dup_nulled"] += 1
                src_msg = None
            else:
                seen_src_msg.add(src_msg)
        created = parse_ts(g(rec, "created_at", "first_seen_at"))
        updated = parse_ts(g(rec, "updated_at", "processed_at"))
        contact_type = g(rec, "contact_type")
        if contact_type and str(contact_type).lower() not in ("phone", "email", "messenger", "mixed", "unknown"):
            contact_type = "unknown"
        dup_status = g(rec, "duplicate_status")
        if dup_status and str(dup_status).lower() not in ("new", "reprocessed", "repeat", "possible"):
            dup_status = None
        form_meta = {
            k: redact(v)
            for k, v in rec.items()
            if str(k).startswith("utm_") or k in ("form_metadata",)
        }
        sql.append(
            "INSERT INTO app_iseo_sales.leads ("
            "lead_id, source_message_id, client_name, primary_contact, contact_type, phone, email, messenger, "
            "site, service, summary, source, request_page, utm_source, utm_medium, utm_campaign, "
            "manager_status, assigned_to, manager_notes, telegram_action_token, form_metadata, "
            "data_contract_version, workflow_version, created_at, updated_at, processed_at, "
            "quality_status, priority, duplicate_status"
            ") VALUES ("
            f"{sql_lit(lid)}, {sql_lit(src_msg)}, {sql_lit(redact(g(rec, 'client_name', 'name')))}, "
            f"{sql_lit(redact(g(rec, 'primary_contact', 'contact')))}, {sql_lit(contact_type)}, "
            f"{sql_lit(redact(g(rec, 'phone')))}, {sql_lit(redact(g(rec, 'email')))}, "
            f"{sql_lit(redact(g(rec, 'messenger')))}, {sql_lit(redact(g(rec, 'site', 'domain')))}, "
            f"{sql_lit(g(rec, 'service', 'category'))}, {sql_lit(redact(g(rec, 'summary', 'request')))}, "
            f"{sql_lit(g(rec, 'source'))}, {sql_lit(g(rec, 'request_page'))}, {sql_lit(g(rec, 'utm_source'))}, "
            f"{sql_lit(g(rec, 'utm_medium'))}, {sql_lit(g(rec, 'utm_campaign'))}, {sql_lit(st)}, "
            f"{sql_lit(g(rec, 'assigned_to', 'owner', 'moderator'))}, "
            f"{sql_lit(redact(g(rec, 'manager_notes', 'notes')))}, {sql_lit(None)}, {sql_lit(form_meta)}, "
            f"'sheets-shadow-v1', 'sheets-shadow-import-v1', COALESCE({sql_lit(created)}, now()), "
            f"COALESCE({sql_lit(updated)}, now()), {sql_lit(parse_ts(g(rec, 'processed_at')))}, "
            f"{sql_lit(g(rec, 'quality_status'))}, {sql_lit(g(rec, 'priority'))}, {sql_lit(dup_status)}"
            ") ON CONFLICT (lead_id) DO UPDATE SET "
            "source_message_id = COALESCE(EXCLUDED.source_message_id, app_iseo_sales.leads.source_message_id), "
            "manager_status = EXCLUDED.manager_status, assigned_to = EXCLUDED.assigned_to, "
            "updated_at = EXCLUDED.updated_at, form_metadata = EXCLUDED.form_metadata, "
            "version = app_iseo_sales.leads.version + 1;"
        )
        sql.append(
            "INSERT INTO app_iseo_sales.lead_events "
            "(event_id, lead_id, event_type, occurred_at, actor_type, actor_id, payload) VALUES ("
            f"{sql_lit('mig_' + sha8(lid))}, {sql_lit(lid)}, 'lead.migrated_from_sheets', now(), "
            f"'system', 'sheets-shadow-import', {sql_lit({'snapshot_id': SNAP, 'source_status_map': how})}"
            ") ON CONFLICT (event_id) DO NOTHING;"
        )

    sql.append(
        "UPDATE app_iseo_sales.leads l SET inbound_event_id = ie.id "
        "FROM app_iseo_sales.inbound_events ie "
        "WHERE l.source_message_id IS NOT NULL AND ie.source_system='gmail' "
        "AND ie.source_id = l.source_message_id "
        "AND (l.inbound_event_id IS DISTINCT FROM ie.id);"
    )

    dedup_stats: Counter = Counter()
    dedup_keys_written: set[str] = set()

    def emit_dedup(key: str, kt: str, lid: str, origin: str) -> None:
        if not key or not lid or lid not in by_lead:
            return
        if kt not in ("gmail_message_id", "phone", "email", "messenger", "site"):
            dedup_stats["bad_type"] += 1
            return
        if key in dedup_keys_written:
            dedup_stats["dup_key_skipped"] += 1
            return
        dedup_keys_written.add(key)
        dedup_stats[f"from_{origin}"] += 1
        sql.append(
            "INSERT INTO app_iseo_sales.lead_dedup_keys (dedup_key, key_type, lead_id) VALUES ("
            f"{sql_lit(key)}, {sql_lit(kt)}, {sql_lit(lid)}"
            ") ON CONFLICT (dedup_key) DO UPDATE SET lead_id = EXCLUDED.lead_id;"
        )

    for rec in dedup_tab.get("records", []):
        lid = str(g(rec, "lead_id") or "").strip()
        mid = str(g(rec, "gmail_message_id") or "").strip()
        key = str(g(rec, "dedup_key") or "").strip()
        kt = str(g(rec, "key_type") or "").strip()
        norm = str(g(rec, "normalized_value") or "").strip()
        if classify_row(
            "DEDUP_INDEX",
            {"lead_id": lid, "gmail_message_id": mid or norm, "source": ""},
        ) == "TEST/SYNTHETIC":
            dedup_stats["test_excluded"] += 1
            continue
        if not key and kt and norm:
            key = f"{kt}:{norm}"
            dedup_stats["composed_from_parts"] += 1
        if not key and mid:
            key = f"gmail_message_id:{mid}"
            kt = "gmail_message_id"
            dedup_stats["composed_from_gmail_message_id"] += 1
        if not key:
            dedup_stats["empty"] += 1
            continue
        if ":" in key and not kt:
            kt = key.split(":", 1)[0]
        if not kt:
            kt = "gmail_message_id"
        if not lid or lid not in by_lead:
            dedup_stats["orphan_or_stale"] += 1
            continue
        emit_dedup(key, kt, lid, "sheet")

    # Reconstruct intended protection from authoritative cleaned leads when sheet keys sparse
    for lid, rec in by_lead.items():
        mid = str(g(rec, "source_message_id", "gmail_message_id") or "").strip()
        if mid:
            emit_dedup(f"gmail_message_id:{mid}", "gmail_message_id", lid, "lead_synth")
        phone = str(g(rec, "phone") or "").strip()
        if phone:
            emit_dedup(f"phone:{re.sub(r'\D', '', phone) or phone}", "phone", lid, "lead_synth")
        email = str(g(rec, "email") or "").strip().lower()
        if email and "@" in email:
            emit_dedup(f"email:{email}", "email", lid, "lead_synth")
        site = str(g(rec, "site", "domain") or "").strip().lower()
        if site:
            emit_dedup(f"site:{site}", "site", lid, "lead_synth")
        messenger = str(g(rec, "messenger") or "").strip().lower()
        if messenger:
            emit_dedup(f"messenger:{messenger}", "messenger", lid, "lead_synth")

    counters.update({f"dedup_{k}": v for k, v in dedup_stats.items()})
    counters["dedup_entries"] = len(dedup_tab.get("records", []))
    counters["dedup_keys_written"] = len(dedup_keys_written)

    for rec in events_tab.get("records", []):
        cls = classify_row("LEAD_EVENTS", rec)
        if cls == "TEST/SYNTHETIC":
            counters["events_test_excluded"] += 1
            continue
        lid = str(g(rec, "lead_id") or "").strip()
        if not lid or lid not in by_lead:
            counters["events_orphan"] += 1
            continue
        eid = str(g(rec, "event_id", "id") or "").strip() or (
            f"sheet_evt_{sha8(str(lid) + str(rec.get('_sheet_row')))}"
        )
        et = str(g(rec, "event_type", "type", "action") or "lead.sheet_event").strip()
        occurred = parse_ts(g(rec, "ts", "occurred_at", "created_at", "timestamp")) or (
            datetime.now(timezone.utc).isoformat()
        )
        actor_raw = str(g(rec, "actor", "actor_id", "actor_type") or "unknown")
        actor_type = "system"
        if actor_raw.lower() in ("system", "moderator", "admin", "workflow", "unknown"):
            actor_type = actor_raw.lower()
        elif actor_raw:
            actor_type = "moderator"
        sql.append(
            "INSERT INTO app_iseo_sales.lead_events "
            "(event_id, lead_id, event_type, occurred_at, actor_type, actor_id, payload) VALUES ("
            f"{sql_lit(eid)}, {sql_lit(lid)}, {sql_lit(et)}, {sql_lit(occurred)}, {sql_lit(actor_type)}, "
            f"{sql_lit(actor_raw)}, "
            f"{sql_lit({k: redact(v) for k, v in rec.items() if k != '_sheet_row'})}"
            ") ON CONFLICT (event_id) DO NOTHING;"
        )
        counters["events_migrated"] += 1

    for rec in access_tab.get("records", []):
        tg = str(g(rec, "telegram_user_id", "principal_key", "profile_key", "access_key", "id") or "").strip()
        if not tg:
            counters["access_skip"] += 1
            continue
        pk = f"tg:{tg}"
        role = str(g(rec, "role") or "moderator").lower()
        if role not in ("admin", "moderator", "viewer"):
            role = "moderator"
        status = str(g(rec, "status") or "active").lower()
        is_active = status in ("1", "true", "yes", "active", "approved")
        if status in ("revoked", "false", "0", "denied", "blocked"):
            is_active = False
        sql.append(
            "INSERT INTO app_iseo_sales.access_rules ("
            "principal_key, telegram_user_id, display_name, username, role, is_active, "
            "receives_cards, receives_reminders, reply_profile_number, notes, revoked_at"
            ") VALUES ("
            f"{sql_lit(pk)}, {sql_lit(tg)}, "
            f"{sql_lit(redact(g(rec, 'display_name', 'name')))}, {sql_lit(redact(g(rec, 'telegram_username', 'username')))}, "
            f"{sql_lit(role)}, {sql_lit(is_active)}, "
            f"TRUE, TRUE, "
            f"{sql_lit(g(rec, 'reply_profile_number'))}, {sql_lit('shadow-import')}, "
            f"{sql_lit(parse_ts(g(rec, 'revoked_at')) if not is_active else None)}"
            ") ON CONFLICT (principal_key) DO UPDATE SET "
            "is_active = EXCLUDED.is_active, role = EXCLUDED.role, updated_at = now(), "
            "telegram_user_id = COALESCE(EXCLUDED.telegram_user_id, app_iseo_sales.access_rules.telegram_user_id), "
            "username = COALESCE(EXCLUDED.username, app_iseo_sales.access_rules.username), "
            "display_name = COALESCE(EXCLUDED.display_name, app_iseo_sales.access_rules.display_name);"
        )
        counters["access_migrated"] += 1
        counters[f"access_status_{status}"] += 1
        counters[f"access_role_{role}"] += 1

    def map_delivery(rec: dict, dtype: str) -> None:
        did = str(
            g(rec, "delivery_key", "delivery_id", "id", "claim_id", "reminder_key") or ""
        ).strip() or (
            f"{dtype}_{sha8(str(rec.get('_sheet_row')) + str(g(rec, 'stable_lead_ref', 'lead_id') or ''))}"
        )
        lid = str(g(rec, "stable_lead_ref", "lead_id") or "").strip() or None
        # Detect clearly malformed delivery rows (webhook debug dumps in first columns)
        ts0 = str(g(rec, "delivery_timestamp") or "")
        if ts0.startswith("{") or "x-forwarded-for" in ts0.lower():
            counters[f"delivery_{dtype}_malformed"] += 1
            unknowns.append({"domain": "deliveries", "reason": "malformed_row", "type": dtype, "row": rec.get("_sheet_row")})
            return
        if lid and lid not in by_lead:
            counters[f"delivery_{dtype}_orphan_lead"] += 1
            # keep delivery with null lead_id rather than inventing FK break
            lid = None
        st = str(g(rec, "delivery_status", "status") or "").lower()
        if st in ("ok", "success", "delivered", "production", "sent"):
            st = "sent"
        if st not in ("pending", "processing", "sent", "retry", "dead", "cancelled"):
            st = "sent" if g(rec, "sent_at", "delivered_at", "telegram_message_ref", "telegram_message_id") else "cancelled"
        if st in ("pending", "processing", "retry"):
            if g(rec, "sent_at", "delivered_at", "telegram_message_ref", "telegram_message_id"):
                st = "sent"
            else:
                st = "cancelled"
                counters["delivery_forced_cancelled_pending"] += 1
        recipient = g(rec, "recipient_ref", "recipient_principal_key", "principal_key", "recipient")
        sent_at = parse_ts(g(rec, "delivered_at", "sent_at", "delivery_timestamp", "last_attempt_at"))
        sql.append(
            "INSERT INTO app_iseo_sales.deliveries ("
            "delivery_id, lead_id, channel, recipient_principal_key, delivery_type, payload, status, "
            "sent_at, external_message_id, telegram_chat_id, idempotency_key"
            ") VALUES ("
            f"{sql_lit(did)}, {sql_lit(lid)}, 'telegram', "
            f"{sql_lit(str(recipient) if recipient is not None else None)}, "
            f"{sql_lit(dtype)}, {sql_lit({k: redact(v) for k, v in rec.items() if k != '_sheet_row'})}, "
            f"{sql_lit(st)}, {sql_lit(sent_at)}, "
            f"{sql_lit(g(rec, 'telegram_message_ref', 'telegram_message_ref_safe', 'telegram_message_id', 'external_message_id'))}, "
            f"{sql_lit(g(rec, 'telegram_delivery_chat_id'))}, "
            f"{sql_lit('shadow:' + did)}"
            ") ON CONFLICT (delivery_id) DO UPDATE SET status = EXCLUDED.status, updated_at = now();"
        )
        counters[f"delivery_{dtype}"] += 1

    for rec in lead_del.get("records", []):
        map_delivery(rec, "lead_card")
    for rec in rem_del.get("records", []):
        map_delivery(rec, "reminder")
        counters["reminder_as_delivery"] += 1

    for rec in cfg_tab.get("records", []):
        key = str(g(rec, "key", "config_key", "name") or "").strip()
        if not key:
            continue
        val = g(rec, "value", "config_value")
        if SECRET_CFG.search(key) or SECRET_CFG.search(str(val or "")):
            counters["config_secret_skipped"] += 1
            excluded.append({"domain": "config", "class": "SECRET — DO NOT MIGRATE", "key": key})
            continue
        secretish = bool(re.search(r"(chat_id|user_id|admin)", key, re.I))
        sql.append(
            "INSERT INTO app_iseo_sales.config "
            "(key, value, value_type, description, is_secretish, updated_by) VALUES ("
            f"{sql_lit(key)}, {sql_lit(str(val) if val is not None else None)}, 'string', "
            f"'shadow-import', {sql_lit(secretish)}, 'sheets-shadow'"
            ") ON CONFLICT (key) DO UPDATE SET value = EXCLUDED.value, updated_at = now();"
        )
        counters["config_migrated"] += 1

    # Idempotent shadow error reload (errors table has no natural unique key)
    sql.append("DELETE FROM app_iseo_sales.errors WHERE app_component = 'shadow-import';")
    # Neutralize known schema-seed synthetic fixtures so they cannot look like live retry queue
    sql.append(
        "UPDATE app_iseo_sales.errors SET retryable = FALSE, resolved = TRUE "
        "WHERE coalesce(message_sanitized,'') ILIKE '%Synthetic Sheets quota%' "
        "OR coalesce(error_class,'') = 'sheets_quota_exceeded';"
    )

    for rec in err_tab.get("records", []):
        cls = classify_row(
            "ERRORS",
            {
                "lead_id": g(rec, "lead_id"),
                "source": "",
                "gmail_message_id": "",
                "email_subject": g(rec, "message"),
                "workflow": g(rec, "workflow"),
            },
        )
        if cls == "TEST/SYNTHETIC" or "SYNTHETIC_TEST" in str(g(rec, "message") or ""):
            counters["errors_test_excluded"] += 1
            continue
        msg = redact(g(rec, "message", "error", "error_message"))
        corr = "shadow-err-" + sha8(
            str(rec.get("_sheet_row")) + "|" + str(g(rec, "ts", "occurred_at", "created_at") or "") + "|" + str(msg or "")
        )
        sql.append(
            "INSERT INTO app_iseo_sales.errors ("
            "occurred_at, app_component, workflow_version, correlation_id, entity_type, entity_id, "
            "error_class, provider, code, stage, retryable, message_sanitized, context, resolved"
            ") VALUES ("
            f"COALESCE({sql_lit(parse_ts(g(rec, 'ts', 'occurred_at', 'created_at', 'timestamp')))}, now()), "
            f"'shadow-import', 'sheets-shadow-import-v1', {sql_lit(corr)}, "
            f"{sql_lit(g(rec, 'entity_type') or 'lead')}, {sql_lit(g(rec, 'entity_id', 'lead_id'))}, "
            f"{sql_lit(g(rec, 'error_class', 'class', 'error_code') or 'historical_sheets_error')}, "
            f"{sql_lit(g(rec, 'provider') or 'sheets')}, {sql_lit(g(rec, 'error_code', 'code'))}, {sql_lit(g(rec, 'stage'))}, "
            f"FALSE, {sql_lit(msg)}, "
            f"{sql_lit({k: redact(v) for k, v in rec.items() if k != '_sheet_row'})}, TRUE);"
        )
        counters["errors_historical"] += 1

    sql.append("COMMIT;")
    return {
        "sql": "\n".join(sql),
        "counters": dict(counters),
        "excluded": excluded[:500],
        "unknowns": unknowns[:500],
        "status_hist_src": dict(status_hist_src),
        "status_hist_pg": dict(status_hist_pg),
        "leads_count": len(by_lead),
        "inbound_count": len(inbound_by_source),
    }


def pg(sql: str) -> tuple[int, str, str]:
    p = subprocess.run(
        ["docker", "exec", "-i", PG_CT, "psql", "-v", "ON_ERROR_STOP=1", "-U", PG_USER, "-d", PG_DB],
        input=sql.encode(),
        capture_output=True,
    )
    return p.returncode, p.stdout.decode("utf-8", "replace"), p.stderr.decode("utf-8", "replace")


def pg_dump(tag: str) -> dict[str, Any]:
    path = f"/root/mars-backups/postgres/mars-{tag}-{SNAP}.sql.gz"
    Path("/root/mars-backups/postgres").mkdir(parents=True, exist_ok=True)
    cmd = (
        f"docker exec {PG_CT} pg_dump -U {PG_USER} -d {PG_DB} --no-owner --no-acl "
        f"| gzip -c > {path}"
    )
    p = subprocess.run(["bash", "-lc", cmd], capture_output=True)
    size = Path(path).stat().st_size if Path(path).exists() else 0
    return {"path": path, "size": size, "rc": p.returncode, "stderr": p.stderr.decode()[:400]}


def reconcile() -> dict[str, Any]:
    q = """
SELECT json_build_object(
  'inbound', (SELECT count(*) FROM app_iseo_sales.inbound_events),
  'leads', (SELECT count(*) FROM app_iseo_sales.leads),
  'dedup', (SELECT count(*) FROM app_iseo_sales.lead_dedup_keys),
  'events', (SELECT count(*) FROM app_iseo_sales.lead_events),
  'access', (SELECT count(*) FROM app_iseo_sales.access_rules),
  'deliveries', (SELECT count(*) FROM app_iseo_sales.deliveries),
  'config', (SELECT count(*) FROM app_iseo_sales.config),
  'errors', (SELECT count(*) FROM app_iseo_sales.errors),
  'pending_deliveries', (SELECT count(*) FROM app_iseo_sales.deliveries WHERE status='pending'),
  'orphan_events', (
    SELECT count(*) FROM app_iseo_sales.lead_events e
    LEFT JOIN app_iseo_sales.leads l ON l.lead_id=e.lead_id WHERE l.lead_id IS NULL
  ),
  'orphan_dedup', (
    SELECT count(*) FROM app_iseo_sales.lead_dedup_keys d
    LEFT JOIN app_iseo_sales.leads l ON l.lead_id=d.lead_id WHERE l.lead_id IS NULL
  ),
  'status_dist', (
    SELECT coalesce(json_object_agg(manager_status, c), '{}'::json)
    FROM (SELECT manager_status, count(*) c FROM app_iseo_sales.leads GROUP BY 1) s
  )
);
"""
    rc, out, err = pg(q)
    if rc != 0:
        return {"ok": False, "stderr": err}
    line = [x for x in out.splitlines() if x.strip().startswith("{")]
    return {"ok": True, "counts": json.loads(line[0]) if line else {}, "raw": out[:2000]}


def prove_live() -> dict[str, Any]:
    con = sqlite3.connect(N8N_DB)
    creds = con.execute(
        "SELECT id,name,type FROM credentials_entity WHERE type LIKE '%postgres%'"
    ).fetchall()
    wfs = con.execute("SELECT id,name,active,nodes FROM workflow_entity").fetchall()
    con.close()
    pg_bound: list[dict[str, Any]] = []
    active_sample: list[dict[str, str]] = []
    for wid, name, active, nodes in wfs:
        if active in (1, True, "true"):
            active_sample.append({"id": wid, "name": name})
        try:
            node_list = json.loads(nodes) if isinstance(nodes, str) else (nodes or [])
        except Exception:  # noqa: BLE001
            node_list = []
        for n in node_list if isinstance(node_list, list) else []:
            ntype = str((n or {}).get("type") or "")
            if "postgres" in ntype.lower():
                pg_bound.append({"workflow_id": wid, "workflow_name": name, "node_type": ntype})
    return {
        "postgres_type_credentials": [{"id": a, "name": b, "type": c} for a, b, c in creds],
        "workflows_with_postgres_nodes": pg_bound[:50],
        "postgres_credential_count": len(creds),
        "postgres_node_binding_count": len(pg_bound),
        "workflow_count": len(wfs),
        "active_workflows_sample": active_sample[:40],
        "iseo_active_present": any("i-SEO Sales Manager" in x["name"] for x in active_sample),
        "note": "Shadow import uses docker exec only; Sheets remains authority; no n8n PG cutover",
    }


def main() -> None:
    result: dict[str, Any] = {"mode": MODE, "snapshot_id": SNAP, "work": str(WORK)}
    if MODE == "prove-live":
        result["prove_live"] = prove_live()
        jdump(WORK / "result.json", result)
        print(json.dumps({"ok": True, "work": str(WORK), "result": result, "snapshot_id": SNAP, "mode": MODE}, default=str))
        return

    tok = load_google_token()
    bundle = {"RAW": fetch_spreadsheet(tok, RAW_ID), "CLEAN": fetch_spreadsheet(tok, CLEAN_ID)}
    inv = inventory_summary(bundle)
    jdump(WORK / "inventory_sanitized.json", inv)
    for label in ("RAW", "CLEAN"):
        slim = {
            "spreadsheetId": bundle[label]["spreadsheetId"],
            "title": bundle[label].get("title"),
            "tabs": {},
        }
        for t, tab in bundle[label]["tabs"].items():
            if "error" in tab:
                slim["tabs"][t] = tab
            else:
                slim["tabs"][t] = {
                    k: tab[k] for k in ("headers", "row_count_body", "nonempty_rows") if k in tab
                }
        jdump(WORK / f"sheet_{label.lower()}_headers.json", slim)

    tf = build_transforms(bundle)
    jdump(
        WORK / "transform_counters.json",
        {
            "counters": tf["counters"],
            "excluded": tf["excluded"],
            "unknowns": tf["unknowns"],
            "status_hist_src": tf["status_hist_src"],
            "status_hist_pg": tf["status_hist_pg"],
        },
    )
    (WORK / "apply.sql").write_text(tf["sql"], encoding="utf-8")
    result["inventory"] = inv
    result["counters"] = tf["counters"]
    result["status_hist_src"] = tf["status_hist_src"]
    result["status_hist_pg"] = tf["status_hist_pg"]
    result["unknown_count"] = len(tf["unknowns"])
    result["excluded_count"] = len(tf["excluded"])

    if MODE in ("inventory", "dry-run"):
        result["dry_run"] = True
        result["sql_bytes"] = len(tf["sql"].encode())
        jdump(WORK / "result.json", result)
        print(
            json.dumps(
                {
                    "ok": True,
                    "work": str(WORK),
                    "result": {
                        "mode": MODE,
                        "snapshot_id": SNAP,
                        "counters": tf["counters"],
                        "tabs": {l: list(bundle[l]["tabs"]) for l in bundle},
                        "unknown_count": len(tf["unknowns"]),
                        "sql_bytes": result["sql_bytes"],
                    },
                    "snapshot_id": SNAP,
                    "mode": MODE,
                },
                default=str,
            )
        )
        return

    if MODE == "reconcile":
        result["reconcile"] = reconcile()
        jdump(WORK / "result.json", result)
        print(json.dumps({"ok": True, "work": str(WORK), "result": result, "snapshot_id": SNAP, "mode": MODE}, default=str))
        return

    if MODE == "apply":
        pre = pg_dump("pre-shadow")
        result["pre_dump"] = pre
        runs = []
        for i in range(2):
            rc, out, err = pg(tf["sql"])
            runs.append({"run": i + 1, "rc": rc, "stdout_tail": out[-1500:], "stderr_tail": err[-1500:]})
            if rc != 0:
                result["apply_runs"] = runs
                result["ok"] = False
                jdump(WORK / "result.json", result)
                print(json.dumps({"ok": False, "work": str(WORK), "result": result, "snapshot_id": SNAP, "mode": MODE}, default=str))
                return
        post = pg_dump("post-shadow")
        result["post_dump"] = post
        result["apply_runs"] = runs
        result["reconcile"] = reconcile()
        result["ok"] = True
        jdump(WORK / "result.json", result)
        print(
            json.dumps(
                {
                    "ok": True,
                    "work": str(WORK),
                    "result": {
                        "mode": MODE,
                        "snapshot_id": SNAP,
                        "counters": tf["counters"],
                        "reconcile": result["reconcile"],
                        "pre_dump": pre,
                        "post_dump": post,
                        "apply_runs": [{"run": r["run"], "rc": r["rc"]} for r in runs],
                    },
                    "snapshot_id": SNAP,
                    "mode": MODE,
                },
                default=str,
            )
        )
        return

    raise SystemExit(f"unknown_mode:{MODE}")


if __name__ == "__main__":
    main()

