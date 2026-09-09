#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Resume leftover homepage + console + security snapshot after home selector timeout."""
from __future__ import annotations

import importlib.util
import json
from datetime import datetime, timezone
from pathlib import Path

_REG = Path(__file__).resolve().parent / "_form-ajax-endpoint-01-regression.py"
_spec = importlib.util.spec_from_file_location("form_ajax_reg", _REG)
_r = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_r)

OUT = _r.OUT
HOME = _r.HOME
SEO_HUB = _r.SEO_HUB
RESTAURANT = _r.RESTAURANT
WEBINAR = _r.WEBINAR


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    report = json.loads(OUT.read_text(encoding="utf-8"))
    report["resume_started"] = utc_now()
    sftp, transport = _r.sftp_connect()
    test_mode_touched = False
    try:
        report["events_before_resume"] = _r.tail_events(sftp, 40)
        report["cfg_before_resume"] = _r.cfg_snapshot(sftp)
        test_mode_touched = True
        report["resume_test_mode_on"] = _r.set_test_mode(sftp, True)
        stamp = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
        home = _r.submit_case(
            {
                "case": "valid_home",
                "url": HOME,
                "form_id": "page__FORM",
                "button_id": "page__FORM_send",
                "name": f"AJAX EP HM {stamp}",
                "phone": f"+7985{stamp[-7:]}",
                "consent": True,
                "honeypot": None,
            }
        )
        valids = list(report.get("valid_submits") or [])
        valids = [v for v in valids if v.get("case") != "valid_home"]
        valids.append(home)
        report["valid_submits"] = valids
        report["valid_home_resume"] = home
        report["shared_js_console"] = [
            _r.load_console(HOME),
            _r.load_console(SEO_HUB),
            _r.load_console(RESTAURANT),
            _r.load_console(WEBINAR),
        ]
        report["events_after_resume"] = _r.tail_events(sftp, 15)
        report["resume_test_mode_off"] = _r.set_test_mode(sftp, False)
        test_mode_touched = False
        report["cfg_final"] = _r.cfg_snapshot(sftp)
        report["resume_ended"] = utc_now()
        OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        print(
            json.dumps(
                {
                    "home": home,
                    "cfg_final": report["cfg_final"],
                    "valid_bodies": [v.get("body") for v in valids],
                    "valid_urls": [v.get("post_url") for v in valids],
                    "console_error_counts": [
                        len(c.get("console_errors") or []) for c in report["shared_js_console"]
                    ],
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0
    except Exception:
        if test_mode_touched:
            try:
                report["resume_test_mode_off_on_error"] = _r.set_test_mode(sftp, False)
            except Exception as restore_exc:  # noqa: BLE001
                report["resume_test_mode_restore_error"] = str(restore_exc)
        report["resume_ended"] = utc_now()
        OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        raise
    finally:
        sftp.close()
        transport.close()


if __name__ == "__main__":
    raise SystemExit(main())
