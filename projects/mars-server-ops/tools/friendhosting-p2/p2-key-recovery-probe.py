"""Local-only: try unlock encrypted marsops key and reconnect. No secrets printed."""
from __future__ import annotations
import re
from pathlib import Path
import paramiko

BASE = Path(r"X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY")
ENC = BASE / "ssh" / "marsops_ed25519.encrypted.bak"
NEW = BASE / "ssh" / "marsops_ed25519"
SUDO = BASE / "ssh" / "marsops_sudo.secret"
SECRETS = BASE / "secrets.local.md"
HOST = "92.42.99.126"
PORT = 3333

def load_ssh_password() -> str:
    text = SECRETS.read_text(encoding="utf-8", errors="replace")
    in_ssh = False
    for line in text.splitlines():
        if re.match(r"^##\s*SSH\b", line, re.I):
            in_ssh = True
            continue
        if in_ssh and re.match(r"^##\s+", line):
            in_ssh = False
        if in_ssh:
            m = re.match(r"^-?\s*password:\s*`?([^`]+?)`?\s*$", line, re.I)
            if m:
                return m.group(1).strip()
    return ""

def try_connect(user: str, pkey: paramiko.PKey) -> bool:
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        c.connect(HOST, port=PORT, username=user, pkey=pkey, timeout=25, allow_agent=False, look_for_keys=False)
        stdin, stdout, stderr = c.exec_command(
            "whoami; ls /etc/ssh/sshd_config.d/ 2>/dev/null; "
            "sshd -T 2>/dev/null | egrep -i 'passwordauthentication|permitrootlogin|pubkeyauthentication|port '; "
            "wc -l /root/.ssh/authorized_keys /home/marsops/.ssh/authorized_keys 2>/dev/null",
            timeout=30,
        )
        out = stdout.read().decode("utf-8", "replace")
        print(f"LOGIN_OK user={user}")
        print(out[:1200])
        c.close()
        return True
    except Exception as e:
        print(f"LOGIN_FAIL user={user} err={type(e).__name__}")
        return False

def main() -> int:
    print("enc_exists", ENC.exists(), "size", ENC.stat().st_size if ENC.exists() else None)
    candidates = [None, "", '""', "''"]
    if SUDO.exists():
        candidates.append(SUDO.read_text(encoding="utf-8").strip())
    ssh_pw = load_ssh_password()
    if ssh_pw:
        candidates.append(ssh_pw)
    unlocked = None
    for i, p in enumerate(candidates):
        try:
            unlocked = paramiko.Ed25519Key.from_private_key_file(str(ENC), password=p if p else None)
            print("UNLOCKED_INDEX", i, "pw_len", 0 if p is None else len(p))
            break
        except Exception as e:
            print("unlock_fail", i, type(e).__name__)
    if unlocked is None:
        print("NO_PASSPHRASE_WORKED")
    else:
        for user in ("root", "marsops"):
            try_connect(user, unlocked)
    print("TRY_NEW_KEY")
    newk = paramiko.Ed25519Key.from_private_key_file(str(NEW))
    for user in ("root", "marsops"):
        try_connect(user, newk)
    if ssh_pw:
        c = paramiko.SSHClient()
        c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            c.connect(HOST, port=PORT, username="root", password=ssh_pw, timeout=20, allow_agent=False, look_for_keys=False)
            print("PASSWORD_STILL_WORKS")
            c.close()
        except Exception as e:
            print("PASSWORD_STATUS", type(e).__name__)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
