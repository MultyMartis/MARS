#!/usr/bin/env python3
"""Safe structural audit of EQ-ALT-A client REALITY profile. No secret dumps."""
from __future__ import annotations

import hashlib
import json
import re
import urllib.parse
from pathlib import Path

WAVE = Path(r"X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\eqvps-alt-a-reality-vision-2026-08-29")


def classify_pbk(v: object) -> tuple[str, list[str]]:
    issues: list[str] = []
    if v is None:
        return "MISSING", ["missing"]
    if not isinstance(v, str):
        return "MALFORMED", ["not_string"]
    if v != v.strip():
        issues.append("whitespace_edges")
    if "\r" in v or "\n" in v:
        issues.append("crlf")
    if '"' in v or "'" in v:
        issues.append("quotes")
    if "%" in v:
        issues.append("url_escape_chars")
    if " " in v:
        issues.append("internal_space")
    if re.fullmatch(r"[A-Za-z0-9\-_/+=]+", v) is None:
        issues.append("illegal_charset")
    if len(v) not in (43, 44):
        issues.append(f"unusual_len_{len(v)}")
    if re.fullmatch(r"[0-9a-fA-F]{64}", v):
        issues.append("looks_like_hex_priv")
    # URL-safe base64 without padding is typical for Xray Reality pbk
    if "+" in v or "/" in v:
        issues.append("standard_base64_chars_plus_slash")
    return ("MALFORMED" if issues else "STRUCTURALLY_OK"), issues


def main() -> int:
    uri_raw = (WAVE / "vless-share.uri.local").read_text(encoding="utf-8")
    sec = json.loads((WAVE / "client-secrets.local.json").read_text(encoding="utf-8"))
    prof = json.loads((WAVE / "v2rayn-profile.local.json").read_text(encoding="utf-8"))

    uri = uri_raw.strip()
    print("URI_LINE_COUNT", len(uri_raw.splitlines()))
    print("URI_HAS_CR", "\r" in uri_raw)
    print("URI_TRAILING_NEWLINE", uri_raw.endswith("\n"))
    print("URI_PREFIX", uri[:8] if uri else "EMPTY")

    m = re.match(r"^vless://([^@]+)@([^:]+):(\d+)\?([^#]*)(?:#(.*))?$", uri)
    print("URI_REGEX_MATCH", bool(m))
    if not m:
        print("URI_PARSE_FAIL")
        return 2

    uuid_s, host, port, qs, frag = m.groups()
    params = urllib.parse.parse_qs(qs, keep_blank_values=True)
    flat = {k: (v[0] if len(v) == 1 else v) for k, v in params.items()}
    print("HOST", host)
    print("PORT", port)
    print("FRAG_DECODED", urllib.parse.unquote(frag or ""))
    print("PARAM_KEYS", sorted(flat.keys()))
    for req in ["encryption", "flow", "security", "sni", "fp", "pbk", "sid", "type", "headerType", "spx"]:
        print(f"HAS_{req}", req in flat)

    pbk = flat.get("pbk", "")
    sid = flat.get("sid", "")
    sni = flat.get("sni", "")
    flow = flat.get("flow", "")
    fp = flat.get("fp", "")
    typ = flat.get("type", "")
    sec_p = flat.get("security", "")

    st, issues = classify_pbk(pbk)
    print("PBK_STATUS", st)
    print("PBK_ISSUES", issues)
    print("PBK_LEN", len(pbk) if isinstance(pbk, str) else None)
    print("PBK_SHA12", hashlib.sha256(pbk.encode()).hexdigest()[:12] if isinstance(pbk, str) else None)
    print("SID_LEN", len(sid) if isinstance(sid, str) else None)
    print("SID_HEX", bool(re.fullmatch(r"[0-9a-fA-F]*", sid or "")))
    print("SID_HAS_WS", bool(re.search(r"\s", sid or "")))
    print("SID_LEN_OK", len(sid or "") in (0, 2, 4, 6, 8, 10, 12, 14, 16))
    print("SNI", sni)
    print("FLOW", flow)
    print("FP", fp)
    print("TYPE", typ)
    print("SECURITY", sec_p)
    print("UUID_LEN", len(uuid_s))
    print("UUID_SHAPE", bool(re.fullmatch(r"[0-9a-fA-F-]{36}", uuid_s)))
    print("MULTI_VALUE_PARAMS", [k for k, v in params.items() if len(v) > 1])

    print("SEC_PBK_SHA12", hashlib.sha256(sec["publicKey"].encode()).hexdigest()[:12])
    print("URI_PBK_EQ_SEC", pbk == sec.get("publicKey"))
    print("URI_SID_EQ_SEC", sid == sec.get("shortId"))
    print("URI_SNI_EQ_SEC", sni == sec.get("serverName"))
    print("URI_UUID_EQ_SEC", uuid_s == sec.get("uuid"))
    print("PROF_PBK_EQ_SEC", prof.get("publicKey") == sec.get("publicKey"))
    print("SEC_SNI", sec.get("serverName"))
    print("SEC_DEST", sec.get("dest"))
    print("SEC_PBK_LEN", len(sec.get("publicKey", "")))
    print("SEC_SID_LEN", len(sec.get("shortId", "")))
    st2, iss2 = classify_pbk(sec.get("publicKey"))
    print("SEC_PBK_STATUS", st2, iss2)
    # Check whether pbk was double-encoded in URI query
    raw_qs_pbk = None
    for part in qs.split("&"):
        if part.startswith("pbk="):
            raw_qs_pbk = part[4:]
            break
    print("PBK_RAW_QS_EQ_DECODED", raw_qs_pbk == pbk if raw_qs_pbk is not None else None)
    print("PBK_PCT_IN_RAW_QS", ("%" in raw_qs_pbk) if raw_qs_pbk is not None else None)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
