#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import importlib.util
from pathlib import Path

p = Path(r"X:\AI MARS\projects\iseo-su-site-ops\tools\_form-contract-regression-01-validate.py")
spec = importlib.util.spec_from_file_location("v", p)
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)
sftp, transport = v.sftp_connect()
try:
    tail = v.tail_events(sftp, 30)
    for line in tail:
        print(line)
finally:
    sftp.close()
    transport.close()
