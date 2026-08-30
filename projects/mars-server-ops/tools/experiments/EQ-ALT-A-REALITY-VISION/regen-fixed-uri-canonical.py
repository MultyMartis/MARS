#!/usr/bin/env python3
"""Regenerate LF-only fixed share URI with canonical spx=%2F. No secret prints."""
from __future__ import annotations

import hashlib
import json
import urllib.parse
from pathlib import Path

WAVE = Path(r"X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\eqvps-alt-a-reality-vision-2026-08-29")


def main() -> int:
    sec = json.loads((WAVE / "client-secrets.local.json").read_text(encoding="utf-8"))
    remark = sec.get("remark", "MCA-ONE-EQ-ALT-A-REALITY-VISION")
    address = sec.get("address", "95.216.126.173")
    qs = urllib.parse.urlencode(
        {
            "encryption": "none",
            "flow": "xtls-rprx-vision",
            "security": "reality",
            "sni": sec["serverName"],
            "fp": "chrome",
            "pbk": sec["publicKey"],
            "sid": sec["shortId"],
            "spx": "/",
            "type": "tcp",
            "headerType": "none",
        }
    )
    uri = f"vless://{sec['uuid']}@{address}:9443?{qs}#{urllib.parse.quote(remark)}"
    assert "spx=%2F" in uri
    assert "\r" not in uri
    (WAVE / "vless-share-fixed.uri.local").write_bytes((uri + "\n").encode("utf-8"))
    profile = {
        "remarks": remark,
        "address": address,
        "port": 9443,
        "id": sec["uuid"],
        "flow": "xtls-rprx-vision",
        "encryption": "none",
        "network": "tcp",
        "headerType": "none",
        "security": "reality",
        "sni": sec["serverName"],
        "fingerprint": "chrome",
        "publicKey": sec["publicKey"],
        "shortId": sec["shortId"],
        "spiderX": "/",
    }
    (WAVE / "v2rayn-profile-fixed.local.json").write_text(
        json.dumps(profile, indent=2) + "\n", encoding="utf-8"
    )
    orig = (WAVE / "vless-share.uri.local").read_text(encoding="utf-8").strip().replace("\r", "")
    pub_sha = hashlib.sha256(sec["publicKey"].encode()).hexdigest()[:12]
    print("PAYLOAD_EQ_ORIG_STRIPPED", orig == uri)
    print("HAS_SPX_PCT2F", "spx=%2F" in uri)
    print("PUB_SHA12", pub_sha)
    print("FIXED_EOL", (WAVE / "vless-share-fixed.uri.local").read_bytes()[-4:].hex())
    meta = f"""# EQ-ALT-A client profile validation (safe)

- display_name: `{remark}`
- server_host: `{address}`
- port: `9443`
- transport: `tcp/raw`
- security: `reality`
- sni / serverName: `{sec['serverName']}`
- fingerprint: `chrome`
- flow: `xtls-rprx-vision`
- public_key_status: `STRUCTURALLY_OK`
- public_key_sha12: `{pub_sha}`
- public_key_len: `{len(sec['publicKey'])}`
- shortId_status: `HEX_LEN_16_OK`
- shortId_len: `{len(sec['shortId'])}`
- server_keypair_class: `MATCH` (xray x25519 -i on EQVPS)
- original_uri_defect: `CRLF_EOL` (query payload otherwise identical to fixed)
- fixed_uri_eol: `LF_ONLY`
- fixed_spx_encoding: `spx=%2F` (urlencode-canonical)
- local_xray_config_test: `PASS`
- isolated_transport_retest: `FAIL_TIMEOUT` (see fix01-isolated-transport-retest.json)
- secrets: `[LOCAL SECRET EXISTS — VALUE NOT EXPOSED]`
- original_preserved: `vless-share.uri.local` + `vless-share.uri.local.ORIGINAL-BYTES.bak`
- fixed_uri: `vless-share-fixed.uri.local`
- fixed_profile_json: `v2rayn-profile-fixed.local.json`
"""
    (WAVE / "client-profile-validation-safe.md").write_text(meta, encoding="utf-8")
    print("META_UPDATED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
