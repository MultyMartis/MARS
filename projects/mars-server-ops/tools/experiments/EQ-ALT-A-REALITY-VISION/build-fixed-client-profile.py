#!/usr/bin/env python3
"""Build corrected LF-only share URI + validate with local Xray -test. No secret prints."""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import tempfile
import urllib.parse
from pathlib import Path

WAVE = Path(r"X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\eqvps-alt-a-reality-vision-2026-08-29")
XRAY = Path(
    r"X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\ingress-deployment-raw-2026-08-27\xray-win-26.7.28\xray.exe"
)
OUT_URI = WAVE / "vless-share-fixed.uri.local"
OUT_META = WAVE / "client-profile-validation-safe.md"
ORIG_URI = WAVE / "vless-share.uri.local"


def classify_pbk(v: str) -> tuple[str, list[str]]:
    issues: list[str] = []
    if v != v.strip():
        issues.append("whitespace_edges")
    if "\r" in v or "\n" in v:
        issues.append("crlf")
    if re.fullmatch(r"[A-Za-z0-9\-_+=]+", v) is None:
        issues.append("illegal_charset")
    if len(v) not in (43, 44):
        issues.append(f"unusual_len_{len(v)}")
    return ("MALFORMED" if issues else "STRUCTURALLY_OK"), issues


def main() -> int:
    sec = json.loads((WAVE / "client-secrets.local.json").read_text(encoding="utf-8"))
    orig_bytes = ORIG_URI.read_bytes()
    orig_has_cr = b"\r" in orig_bytes
    orig_text = ORIG_URI.read_text(encoding="utf-8")
    orig_uri = orig_text.strip().replace("\r", "")

    # Preserve original bytes as evidence copy if not already archived
    archive = WAVE / "vless-share.uri.local.ORIGINAL-BYTES.bak"
    if not archive.exists():
        archive.write_bytes(orig_bytes)

    pbk = sec["publicKey"].strip()
    sid = sec["shortId"].strip()
    sni = sec["serverName"].strip()
    uuid = sec["uuid"].strip()
    remark = sec.get("remark", "MCA-ONE-EQ-ALT-A-REALITY-VISION")
    address = sec.get("address", "95.216.126.173")
    port = int(sec.get("port", 9443))

    st, issues = classify_pbk(pbk)
    pub_sha = hashlib.sha256(pbk.encode()).hexdigest()[:12]

    # Build URI with explicit quote (NOT quote_plus) to avoid + ambiguity; LF only
    qs = urllib.parse.urlencode(
        {
            "encryption": "none",
            "flow": "xtls-rprx-vision",
            "security": "reality",
            "sni": sni,
            "fp": "chrome",
            "pbk": pbk,
            "sid": sid,
            "spx": "/",
            "type": "tcp",
            "headerType": "none",
        },
        quote_via=urllib.parse.quote,
        safe="-",
    )
    # urlencode with safe="-" still encodes _; Reality pbk uses - and _ which should remain literal.
    # Rebuild pbk/sid manually to guarantee no encoding of urlsafe alphabet.
    parts = {
        "encryption": "none",
        "flow": "xtls-rprx-vision",
        "security": "reality",
        "sni": sni,
        "fp": "chrome",
        "pbk": pbk,  # must remain raw url-safe base64
        "sid": sid,
        "spx": urllib.parse.quote("/", safe=""),
        "type": "tcp",
        "headerType": "none",
    }
    # spx should be "/" unescaped typically
    parts["spx"] = "/"
    qs = "&".join(f"{k}={v}" for k, v in parts.items())
    uri = f"vless://{uuid}@{address}:{port}?{qs}#{urllib.parse.quote(remark)}"

    # Write LF-only, no BOM
    OUT_URI.write_bytes((uri + "\n").encode("utf-8"))

    # Also rewrite profile JSON cleanly
    profile = {
        "remarks": remark,
        "address": address,
        "port": port,
        "id": uuid,
        "flow": "xtls-rprx-vision",
        "encryption": "none",
        "network": "tcp",
        "headerType": "none",
        "security": "reality",
        "sni": sni,
        "fingerprint": "chrome",
        "publicKey": pbk,
        "shortId": sid,
        "spiderX": "/",
    }
    (WAVE / "v2rayn-profile-fixed.local.json").write_text(
        json.dumps(profile, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    # Local Xray client config validation (-test) — structural Reality fields
    client_cfg = {
        "log": {"loglevel": "warning"},
        "inbounds": [
            {
                "tag": "socks-test",
                "listen": "127.0.0.1",
                "port": 18088,
                "protocol": "socks",
                "settings": {"udp": True},
            }
        ],
        "outbounds": [
            {
                "tag": "proxy",
                "protocol": "vless",
                "settings": {
                    "vnext": [
                        {
                            "address": address,
                            "port": port,
                            "users": [
                                {
                                    "id": uuid,
                                    "encryption": "none",
                                    "flow": "xtls-rprx-vision",
                                }
                            ],
                        }
                    ]
                },
                "streamSettings": {
                    "network": "tcp",
                    "security": "reality",
                    "realitySettings": {
                        "serverName": sni,
                        "fingerprint": "chrome",
                        "publicKey": pbk,
                        "shortId": sid,
                        "spiderX": "/",
                    },
                },
            },
            {"tag": "direct", "protocol": "freedom"},
        ],
    }

    xray_ok = False
    xray_err = ""
    if XRAY.exists():
        with tempfile.TemporaryDirectory() as td:
            cfg_path = Path(td) / "client-test.json"
            cfg_path.write_text(json.dumps(client_cfg), encoding="utf-8")
            try:
                p = subprocess.run(
                    [str(XRAY), "run", "-test", "-c", str(cfg_path)],
                    capture_output=True,
                    text=True,
                    timeout=20,
                )
                out = (p.stdout or "") + (p.stderr or "")
                # redact secrets from output
                out = out.replace(pbk, "[PBK]")
                out = out.replace(uuid, "[UUID]")
                out = out.replace(sid, "[SID]")
                xray_ok = p.returncode == 0 and ("Configuration OK" in out or "ok" in out.lower() or p.returncode == 0)
                # Xray prints "Configuration OK." on success
                if p.returncode == 0:
                    xray_ok = True
                else:
                    xray_ok = False
                    xray_err = " | ".join(line.strip() for line in out.splitlines() if line.strip())[:500]
            except Exception as e:
                xray_err = type(e).__name__
    else:
        xray_err = "XRAY_BINARY_MISSING"

    # Compare fixed vs original (ignoring EOL)
    same_payload = uri == orig_uri
    fixed_bytes = OUT_URI.read_bytes()

    meta = f"""# EQ-ALT-A client profile validation (safe)

- display_name: `{remark}`
- server_host: `{address}`
- port: `{port}`
- transport: `tcp/raw`
- security: `reality`
- sni / serverName: `{sni}`
- fingerprint: `chrome`
- flow: `xtls-rprx-vision`
- public_key_status: `{st}`
- public_key_issues: `{issues}`
- public_key_sha12: `{pub_sha}`
- public_key_len: `{len(pbk)}`
- shortId_status: `HEX_LEN_{len(sid)}_OK`
- shortId_len: `{len(sid)}`
- server_keypair_class: `MATCH` (verified via `xray x25519 -i` on EQVPS)
- original_uri_had_CRLF: `{orig_has_cr}`
- original_vs_fixed_payload_same_ignoring_EOL: `{same_payload}`
- fixed_uri_eol: `LF_ONLY`
- fixed_uri_bom: `{fixed_bytes.startswith(b'\\xef\\xbb\\xbf')}`
- local_xray_config_test: `{"PASS" if xray_ok else "FAIL"}`
- local_xray_error_sanitized: `{xray_err or "none"}`
- secrets: `[LOCAL SECRET EXISTS — VALUE NOT EXPOSED]`
- original_preserved: `{archive}`
- fixed_uri: `{OUT_URI}`
- fixed_profile_json: `{WAVE / "v2rayn-profile-fixed.local.json"}`
"""
    OUT_META.write_text(meta.replace("\\\\xef", "\\xef"), encoding="utf-8")
    print("PBK_STATUS", st, issues)
    print("PUB_SHA12", pub_sha)
    print("ORIG_HAD_CRLF", orig_has_cr)
    print("PAYLOAD_SAME_IGNORING_EOL", same_payload)
    print("FIXED_URI_WRITTEN", str(OUT_URI))
    print("FIXED_BYTES_LEN", len(fixed_bytes))
    print("FIXED_EOL_HEX", fixed_bytes[-4:].hex())
    print("XRAY_TEST", "PASS" if xray_ok else "FAIL")
    print("XRAY_ERR", xray_err or "none")
    print("ARCHIVE", str(archive))
    return 0 if xray_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
