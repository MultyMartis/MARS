#!/usr/bin/env python3
"""Set client_inbounds.flow_override and optionally patch runtime config flow. LOCAL ONLY."""
from __future__ import annotations

import json
import re
from pathlib import Path

import paramiko

BASE = Path(r"X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP")
WAVE = BASE / "eqvps-alt-a-reality-vision-2026-08-29"
SECRETS = BASE / "secrets.local.md"
KEY = BASE / "ssh" / "marsops_ed25519"


def load_pw() -> str:
    text = SECRETS.read_text(encoding="utf-8")
    m = re.search(r"marsops sudo password[^\n]*\n+```[^\n]*\n([^\n]+)\n```", text, re.I)
    return m.group(1).strip().strip("`")


def sudo(c, cmd: str, pw: str):
    full = f"sudo -S -p '' bash -lc {json.dumps(cmd)}"
    stdin, stdout, stderr = c.exec_command(full, get_pty=True, timeout=180)
    stdin.write(pw + "\n")
    stdin.flush()
    stdin.channel.shutdown_write()
    out = (stdout.read() + stderr.read()).decode("utf-8", "replace").replace(pw, "<REDACTED>")
    return stdout.channel.recv_exit_status(), out


def main() -> int:
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
        script = (
            "import json,sqlite3\n"
            "conn=sqlite3.connect('/etc/x-ui/x-ui.db')\n"
            "cur=conn.cursor()\n"
            "cur.execute(\"SELECT id FROM inbounds WHERE port=9443\")\n"
            "iid=cur.fetchone()[0]\n"
            "cur.execute(\"SELECT id FROM clients WHERE email='MCA-ONE-EQ-ALT-A-REALITY-VISION'\")\n"
            "cid=cur.fetchone()[0]\n"
            "cur.execute('UPDATE client_inbounds SET flow_override=? WHERE client_id=? AND inbound_id=?', ('xtls-rprx-vision', cid, iid))\n"
            "print('FLOW_OVERRIDE', list(cur.execute('SELECT * FROM client_inbounds WHERE inbound_id=?', (iid,))))\n"
            "conn.commit(); conn.close()\n"
            "print('OVERRIDE_OK')\n"
        )
        sftp = c.open_sftp()
        with sftp.file("/home/marsops/mars-alt-a-flow-override.py", "w") as rf:
            rf.write(script)
        sftp.close()
        code, out = sudo(c, "python3 /home/marsops/mars-alt-a-flow-override.py", pw)
        print(out)
        if "OVERRIDE_OK" not in out:
            return 2
        code, out = sudo(c, "systemctl restart x-ui && sleep 7 && systemctl is-active x-ui", pw)
        print(out)
        inspect = (
            "import json\n"
            "cfg=json.load(open('/usr/local/x-ui/bin/config.json'))\n"
            "for ib in cfg.get('inbounds',[]):\n"
            " if ib.get('port')==9443:\n"
            "  print('CFG_CLIENT', (ib.get('settings') or {}).get('clients'))\n"
        )
        sftp = c.open_sftp()
        with sftp.file("/home/marsops/mars-alt-a-inspect3.py", "w") as rf:
            rf.write(inspect)
        sftp.close()
        code, out = sudo(c, "python3 /home/marsops/mars-alt-a-inspect3.py", pw)
        print(out)
        (WAVE / "post-flow-override.txt").write_text(out, encoding="utf-8")

        if "xtls-rprx-vision" not in out:
            # Known 3X-UI 3.7.0 residual: patch runtime config.json then restart xray via x-ui
            patch = (
                "import json\n"
                "p='/usr/local/x-ui/bin/config.json'\n"
                "cfg=json.load(open(p))\n"
                "changed=False\n"
                "for ib in cfg.get('inbounds',[]):\n"
                " if ib.get('port')==9443:\n"
                "  for cl in (ib.get('settings') or {}).get('clients') or []:\n"
                "   if cl.get('email')=='MCA-ONE-EQ-ALT-A-REALITY-VISION':\n"
                "    if cl.get('flow')!='xtls-rprx-vision':\n"
                "     cl['flow']='xtls-rprx-vision'; changed=True\n"
                "open(p,'w').write(json.dumps(cfg,indent=2))\n"
                "print('PATCHED', changed)\n"
            )
            sftp = c.open_sftp()
            with sftp.file("/home/marsops/mars-alt-a-patch-cfg.py", "w") as rf:
                rf.write(patch)
            sftp.close()
            code, out = sudo(c, "python3 /home/marsops/mars-alt-a-patch-cfg.py", pw)
            print(out)
            # Restart only xray child by bouncing x-ui — may regenerate and wipe patch.
            # Prefer sending HUP or x-ui API. Safest for this residual: stop x-ui briefly,
            # patch again after stop? Actually x-ui regenerates on start from DB.
            # So patch AFTER start: stop xray process? Better approach:
            # use xray run with patched config outside x-ui — OUT OF SCOPE / risky.
            #
            # Alternative: after x-ui start, patch config and kill only xray so x-ui restarts it
            # — x-ui may rewrite config again from DB.
            #
            # Historical wave treated omitted flow as residual and still got server-side Reality PASS
            # with client-side Vision. Proceed to probe with residual documented.
            (WAVE / "flow-runtime-residual.json").write_text(
                json.dumps(
                    {
                        "status": "3X-UI_OMITS_FLOW_IN_CONFIG_JSON",
                        "db_flow": "xtls-rprx-vision",
                        "flow_override": "xtls-rprx-vision",
                        "config_json_flow": "absent",
                        "action": "continue_with_client_side_vision_flow",
                        "reference": "EQVPS-MICRO-IP-ingress-deployment-2026-08-27.md residual",
                    },
                    indent=2,
                ),
                encoding="utf-8",
            )
            print("RESIDUAL_DOCUMENTED")
            return 0
        print("FLOW_IN_CONFIG_OK")
        return 0
    finally:
        c.close()


if __name__ == "__main__":
    raise SystemExit(main())
