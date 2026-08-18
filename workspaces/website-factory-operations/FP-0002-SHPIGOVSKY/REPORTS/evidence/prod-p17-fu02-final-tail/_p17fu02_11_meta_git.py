# -*- coding: utf-8 -*-
"""Record git SHA in dashboard meta + followup commit of GIT-CHECKPOINT.json."""
from __future__ import annotations

import json
import re
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import paramiko

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
SRC = Path(r"X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY")
EV = SRC / "REPORTS/evidence/prod-p17-fu02-final-tail"
REPO = Path(r"X:\AI MARS STORAGE\git-sync-fp0002-p14-20260816-173714\repo")
REL_ROOT = "workspaces/website-factory-operations/FP-0002-SHPIGOVSKY"
SHA = "16706398f03825b054ce75c56e8af48ec4349329"
REMOTE_PHP = "/tmp/fp02_p17fu02_meta_git.php"

PHP = f"""<?php
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
$before = get_option('fp02_metacode_system_meta', array());
if (!is_array($before)) $before = array();
$after = $before;
$after['git_sha'] = '{SHA}';
$after['latest_wave'] = 'P17-FU02 Final Pre-Cutover Tail Closure';
$after['precutover'] = 'READY FOR MANUAL NS SWITCH';
$after['parity'] = 'MATCH';
$after['verified_at'] = gmdate('Y-m-d H:i') . ' UTC';
update_option('fp02_metacode_system_meta', $after, false);
echo json_encode(array('after'=>get_option('fp02_metacode_system_meta')), JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES);
echo "\\n";
"""


def parse_secrets(text: str) -> dict:
    pairs = {}
    for line in text.splitlines():
        m = re.match(r"^[-*]?\s*`?([A-Za-z0-9_./-]+)`?\s*[:=]\s*(.*)$", line.strip())
        if m:
            pairs[m.group(1)] = m.group(2).strip().strip("`").strip('"').strip("'")
    return pairs


def getf(pairs, *keys):
    for k in keys:
        v = pairs.get(k)
        if v and "<OPERATOR" not in v and v.strip():
            return v.strip()
    return None


def run(cmd, cwd=None, check=True):
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if check and p.returncode != 0:
        raise RuntimeError(p.stderr[-2000:] + p.stdout[-2000:])
    return p


def main() -> int:
    pairs = parse_secrets(SECRETS.read_text(encoding="utf-8"))
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        hostname=getf(pairs, "ssh_host"),
        port=int(getf(pairs, "ssh_port") or "22"),
        username=getf(pairs, "ssh_username"),
        password=getf(pairs, "ssh_password_or_key_reference"),
        timeout=60,
        allow_agent=False,
        look_for_keys=False,
    )
    sftp = client.open_sftp()
    with sftp.file(REMOTE_PHP, "wb") as fh:
        fh.write(PHP.encode("utf-8"))
    stdin, stdout, stderr = client.exec_command(f"php8.2 {REMOTE_PHP} 2>/dev/null || php {REMOTE_PHP}", timeout=60)
    out = stdout.read().decode("utf-8", errors="replace")
    try:
        sftp.remove(REMOTE_PHP)
    except OSError:
        pass
    sftp.close()
    client.close()
    meta = None
    for ln in out.splitlines():
        if ln.startswith("{"):
            meta = json.loads(ln)
            break
    (EV / "METACODE-META-AFTER-GIT.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("META", json.dumps(meta, ensure_ascii=False)[:500])

    base = SRC / "REPORTS/BASELINE-FP-0002-PRODUCTION-POST-P13.md"
    text = base.read_text(encoding="utf-8")
    text = text.replace("*(this wave — see GIT-CHECKPOINT.json)*", f"`{SHA}`")
    base.write_text(text, encoding="utf-8")

    dest_root = REPO / REL_ROOT
    follow = [
        "REPORTS/BASELINE-FP-0002-PRODUCTION-POST-P13.md",
        "REPORTS/evidence/prod-p17-fu02-final-tail/GIT-CHECKPOINT.json",
        "REPORTS/evidence/prod-p17-fu02-final-tail/METACODE-META-AFTER-GIT.json",
        "REPORTS/evidence/prod-p17-fu02-final-tail/_p17fu02_11_meta_git.py",
    ]
    here = Path(__file__).resolve()
    dest_self = (EV / "_p17fu02_11_meta_git.py").resolve()
    if here != dest_self:
        shutil.copy2(here, dest_self)
    for rel in follow:
        src = SRC / Path(*rel.split("/"))
        if not src.exists():
            print("skip", rel)
            continue
        dest = dest_root / Path(*rel.split("/"))
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        run(["git", "add", "--", f"{REL_ROOT}/{rel}"], cwd=str(REPO))

    run(["git", "commit", "-m", "docs(fp-0002): record P17-FU02 git checkpoint"], cwd=str(REPO))
    sha = run(["git", "rev-parse", "HEAD"], cwd=str(REPO)).stdout.strip()
    run(["git", "push", "origin", "HEAD:mars/canonical-post-recovery"], cwd=str(REPO))
    remote = run(["git", "rev-parse", "origin/mars/canonical-post-recovery"], cwd=str(REPO)).stdout.strip()
    follow_ev = {"commit": sha, "remote": remote, "utc": datetime.now(timezone.utc).isoformat()}
    (EV / "GIT-CHECKPOINT-FOLLOWUP.json").write_text(json.dumps(follow_ev, indent=2) + "\n", encoding="utf-8")
    print("FOLLOWUP", sha, remote)
    return 0 if sha == remote else 2


if __name__ == "__main__":
    raise SystemExit(main())
