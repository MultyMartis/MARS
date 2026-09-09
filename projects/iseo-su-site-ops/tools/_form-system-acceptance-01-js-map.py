#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parse common.js form send handlers: endpoint, preventDefault, button binding."""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

SRC = Path(r"X:\AI MARS\projects\iseo-su-site-ops\production-source\js\common.js")
OUT = Path(r"X:\AI MARS\projects\iseo-su-site-ops\evidence\form-system-acceptance-01\_js-handler-map.json")

CLICK_RE = re.compile(
    r"""(?:\$\((?:document)\)\.on\(\s*"click"\s*,\s*"([^"]+)"|\$\("([^"]+)"\)\.on\(\s*"click")\s*,\s*function\s*\(([^)]*)\)\s*\{""",
    re.M,
)


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    text = SRC.read_text(encoding="utf-8", errors="replace")
    handlers = []
    for m in CLICK_RE.finditer(text):
        selector = m.group(1) or m.group(2)
        args = m.group(3) or ""
        start = m.start()
        # take a window of the function body
        chunk = text[m.start() : m.start() + 900]
        urls = re.findall(r"url:\s*(?:root\s*\?\s*'([^']+)'\s*:\s*)?'([^']+)'", chunk)
        url_plain = re.findall(r"url:\s*'([^']+)'", chunk)
        prevent = "preventDefault" in chunk[:500]
        prevent_call = bool(re.search(r"preventDefault\s*\(", chunk[:500]))
        return_false = "return false" in chunk[:700]
        serialize = re.findall(r'\$\("([^"]+)"\)\.serialize', chunk)
        handlers.append(
            {
                "selector": selector,
                "event_arg": args.strip(),
                "preventDefault_token": prevent,
                "preventDefault_call": prevent_call,
                "return_false": return_false,
                "urls": url_plain,
                "root_ternary": urls,
                "serialize_targets": serialize,
                "offset": start,
                "type_submit_risk": selector.endswith("_send") or "FORM_send" in selector,
            }
        )
    calc = {
        "calc_submit_selector": ".calculator_stage__btns .submit",
        "preventDefault_bug": "e.preventDefault;" in text and "e.preventDefault()" not in text[text.find("calculator_stage__btns .submit") : text.find("calculator_stage__btns .submit") + 80]
        if "calculator_stage__btns .submit" in text
        else None,
    }
    # more precise calc snippet
    idx = text.find("$('.calculator_stage__btns .submit').click")
    calc_snip = text[idx : idx + 200] if idx >= 0 else ""
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        json.dumps(
            {
                "ts": utc_now(),
                "source": str(SRC),
                "handler_count": len(handlers),
                "relative_urls": [h for h in handlers if any(not u.startswith("/") for u in h["urls"])],
                "root_relative_urls": [h for h in handlers if any(u.startswith("/") for u in h["urls"])],
                "missing_preventDefault_call": [
                    h["selector"]
                    for h in handlers
                    if "FORM_send" in h["selector"] and not h["preventDefault_call"] and not h["return_false"]
                ],
                "calc": {"index": idx, "snippet": calc_snip, **calc},
                "handlers": handlers,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print("handlers", len(handlers))
    print("relative", [h["selector"] + " -> " + ",".join(h["urls"]) for h in handlers if any(not u.startswith("/") for u in h["urls"])])
    print("no preventDefault call and no return false", [h["selector"] for h in handlers if "FORM_send" in (h["selector"] or "") and not h["preventDefault_call"] and not h["return_false"]])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
