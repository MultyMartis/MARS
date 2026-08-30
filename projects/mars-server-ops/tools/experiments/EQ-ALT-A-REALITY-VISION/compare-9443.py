#!/usr/bin/env python3
"""Compare 9443 inbound structure to working standalone shape. No secret values."""
from __future__ import annotations

import json
import re
from pathlib import Path

import paramiko

BASE = Path(r"X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP")
WAVE = BASE / "eqvps-alt-a-reality-vision-2026-08-29"
SECRETS = BASE / "secrets.local.md"
KEY = BASE / "ssh" / "marsops_ed25519"

REMOTE = r'''#!/usr/bin/env python3
import json
cfg=json.load(open("/usr/local/x-ui/bin/config.json"))
for ib in cfg.get("inbounds",[]):
  if ib.get("port")!=9443: continue
  def walk(obj, prefix=""):
    if isinstance(obj, dict):
      for k,v in obj.items():
        if k.lower() in ("privatekey","publickey","id","password","email"):
          print(f"{prefix}{k}: <redacted_type={type(v).__name__}_len={len(str(v))}>")
        else:
          walk(v, prefix+k+".")
    elif isinstance(obj, list):
      print(f"{prefix}list_len={len(obj)}")
      for i,v in enumerate(obj[:5]):
        walk(v, prefix+f"[{i}].")
    else:
      print(f"{prefix}{obj!r}")
  walk(ib)
  print("TOP_KEYS", sorted(ib.keys()))
  print("SETTINGS_KEYS", sorted((ib.get("settings") or {}).keys()))
  print("STREAM_KEYS", sorted((ib.get("streamSettings") or {}).keys()))
  print("REALITY_KEYS", sorted(((ib.get("streamSettings") or {}).get("realitySettings") or {}).keys()))
'''


def load_pw() -> str:
    text = SECRETS.read_text(encoding="utf-8")
    m = re.search(r"marsops sudo password[^\n]*\n+```[^\n]*\n([^\n]+)\n```", text, re.I)
    return m.group(1).strip().strip("`")


def sudo(c, cmd, pw, timeout=60):
    full = f"sudo -S -p '' bash -lc {json.dumps(cmd)}"
    i, o, e = c.exec_command(full, get_pty=True, timeout=timeout)
    i.write(pw + "\n")
    i.flush()
    i.channel.shutdown_write()
    out = (o.read() + e.read()).decode("utf-8", "replace").replace(pw, "<REDACTED>")
    return o.channel.recv_exit_status(), out


def main():
    pw = load_pw()
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(
        "95.216.126.173",
        22,
        username="marsops",
        key_filename=str(KEY),
        timeout=30,
        allow_agent=False,
        look_for_keys=False,
    )
    try:
        sftp = c.open_sftp()
        body = REMOTE.replace("\r\n", "\n")
        sftp.file("/home/marsops/mars-compare-9443.py", "w").write(body)
        sftp.close()
        code, out = sudo(c, "python3 /home/marsops/mars-compare-9443.py", pw)
        print(code)
        print(out)
        (WAVE / "compare-9443-structure.txt").write_text(out, encoding="utf-8")
    finally:
        c.close()


if __name__ == "__main__":
    main()
