#!/usr/bin/env python3
import importlib.util
import re
from pathlib import Path

p = Path(r"X:\AI MARS\projects\iseo-su-site-ops\tools\_form-contract-regression-01-validate.py")
spec = importlib.util.spec_from_file_location("v", p)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
sftp, t = m.sftp_connect()
try:
    text = m.read_remote_bytes(sftp, m.CFG_REMOTE).decode("utf-8", "replace")
    red = re.sub(r'("hmac_secret"\s*=>\s*)([^,\n]+)', r"\1REDACTED", text)
    keys = ("hmac", "test_mode", "honeypot", "min_fill", "rate_limit", "duplicate", "nikel", "im.work", "consent")
    for line in red.splitlines():
        low = line.lower()
        if any(k in low for k in keys):
            print(line.strip()[:140])
    print("SNAPSHOT", m.cfg_snapshot(sftp))
finally:
    sftp.close()
    t.close()
