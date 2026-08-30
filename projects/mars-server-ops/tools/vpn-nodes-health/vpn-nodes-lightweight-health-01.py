#!/usr/bin/env python3
"""MARS Server Ops — lightweight VPN-node health / soak checker (read-only).

Supports FRIENDHOSTING-DE and MCA-VPN-001 (VEESP) via nodes.json.
No secrets in Git. Does not mutate servers, VPN, clients, firewall, or packages.
"""
from __future__ import annotations

import argparse
import json
import re
import socket
import ssl
from datetime import datetime, timezone
from pathlib import Path

import paramiko

HERE = Path(__file__).resolve().parent
DEFAULT_NODES = HERE / "nodes.json"
DEFAULT_EVIDENCE_ROOT = Path(
    r"X:\AI MARS\projects\mars-server-ops\evidence\DUAL-NODE-SOAK-MONITORING-T0-01"
)
REMOTE_PROBE = r"""
set +e
echo "HOSTNAME=$(hostname)"
echo "UPTIME_SEC=$(awk '{print int($1)}' /proc/uptime)"
echo "LOAD=$(cut -d' ' -f1-3 /proc/loadavg)"
free -b | awk '/^Mem:/{printf "MEM_TOTAL=%s\nMEM_USED=%s\nMEM_AVAIL=%s\n",$2,$3,$7} /^Swap:/{printf "SWAP_TOTAL=%s\nSWAP_USED=%s\nSWAP_FREE=%s\n",$2,$3,$4}'
df -B1 / | awk 'NR==2{printf "ROOT_SIZE=%s\nROOT_USED=%s\nROOT_AVAIL=%s\nROOT_USEPCT=%s\n",$2,$3,$4,$5}'
df -i / | awk 'NR==2{printf "INODE_USEPCT=%s\n",$5}'
systemctl is-active ssh 2>/dev/null || systemctl is-active sshd 2>/dev/null; echo "SSH_ACTIVE_EXIT=$?"
systemctl is-active x-ui >/dev/null 2>&1; echo "XUI_ACTIVE=$?"
systemctl is-enabled x-ui >/dev/null 2>&1; echo "XUI_ENABLED=$?"
pgrep -x xray >/dev/null 2>&1 || pgrep -f '/usr/local/x-ui/bin/xray-linux' >/dev/null 2>&1; echo "XRAY_PROC=$?"
systemctl is-active fail2ban >/dev/null 2>&1; echo "F2B_ACTIVE=$?"
ufw status 2>/dev/null | head -n 1 | sed 's/^/UFW_STATUS=/'
ufw status 2>/dev/null | awk '/DENY/{print}' | sed 's/^/UFW_DENY=/' | head -n 40
fail2ban-client status 2>/dev/null | head -n 5 | sed 's/^/F2B_LINE=/'
ss -lntH 2>/dev/null | awk '{print $4}' | sed 's/^/LISTEN=/'
systemctl is-active nginx >/dev/null 2>&1; echo "NGINX_ACTIVE=$?"
if command -v certbot >/dev/null 2>&1; then
  echo "CERTBOT=present"
  systemctl list-timers --all 2>/dev/null | grep -i certbot | head -n 3 | sed 's/^/CERTBOT_TIMER=/'
  ls /etc/letsencrypt/renewal 2>/dev/null | sed 's/^/CERTBOT_RENEWAL=/'
else
  echo "CERTBOT=absent"
fi
ls -1 /root/mars-backups 2>/dev/null | sed 's/^/REMOTE_BAK=/' | tail -n 20
x-ui setting -show true 2>/dev/null | egrep -i 'version|panelPort|webBasePath|webPort' | sed 's/^/XUI_SETTING=/' | head -n 20
"""


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def redact(t: str) -> str:
    t = re.sub(
        r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        "<UUID>",
        t,
    )
    t = re.sub(
        r"(?i)(password|passwd|secret|token|api[_-]?key|panel_password|panel_url)\s*[:=]\s*\S+",
        r"\1=<REDACTED>",
        t,
    )
    t = re.sub(r"vless://[^\s]+", "vless://<REDACTED>", t)
    t = re.sub(r"https?://[^\s]+/\S{8,}/?", "https://<REDACTED_PANEL_PATH>/", t)
    return t


def tcp(host: str, port: int, timeout: float = 6) -> bool:
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


def dns_a(name: str) -> list[str]:
    try:
        return sorted({ai[4][0] for ai in socket.getaddrinfo(name, None, socket.AF_INET)})
    except OSError:
        return []


def tls_probe(host: str, port: int, sni: str) -> dict:
    out: dict = {"ok": False}
    try:
        ctx = ssl.create_default_context()
        with socket.create_connection((host, port), timeout=15) as sock:
            with ctx.wrap_socket(sock, server_hostname=sni) as ssock:
                cert = ssock.getpeercert()
                subject = {}
                for rdn in cert.get("subject", ()):
                    for k, v in rdn:
                        subject[k] = v
                not_after = cert.get("notAfter")
                out = {
                    "ok": True,
                    "subject_cn": subject.get("commonName"),
                    "not_after": not_after,
                    "version": ssock.version(),
                }
                if not_after:
                    exp = datetime.strptime(not_after, "%b %d %H:%M:%S %Y %Z").replace(
                        tzinfo=timezone.utc
                    )
                    days = (exp - utc_now()).total_seconds() / 86400.0
                    out["expires_utc"] = exp.isoformat()
                    out["days_remaining"] = round(days, 2)
    except Exception as e:
        out["error"] = type(e).__name__
    return out


def load_key(path: Path):
    try:
        return paramiko.Ed25519Key.from_private_key_file(str(path))
    except paramiko.PasswordRequiredException:
        return paramiko.Ed25519Key.from_private_key_file(str(path), password='""')


def ssh_connect(host: str, port: int, user: str, key_path: Path) -> paramiko.SSHClient:
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(
        host,
        port=port,
        username=user,
        pkey=load_key(key_path),
        timeout=30,
        allow_agent=False,
        look_for_keys=False,
    )
    t = c.get_transport()
    if t:
        t.set_keepalive(20)
    return c


def ssh_run(c: paramiko.SSHClient, cmd: str, timeout: int = 90) -> tuple[int, str, str]:
    try:
        _, stdout, stderr = c.exec_command(cmd, timeout=timeout)
        stdout.channel.settimeout(timeout)
        stderr.channel.settimeout(timeout)
        out = stdout.read().decode("utf-8", "replace")
        err = stderr.read().decode("utf-8", "replace")
        code = stdout.channel.recv_exit_status()
        return code, out, err
    except Exception as e:
        return 124, "", f"ERR:{type(e).__name__}:{e}"


def parse_remote(text: str) -> dict:
    d: dict = {
        "raw_kv": {},
        "listen": [],
        "remote_bak": [],
        "f2b_lines": [],
        "xui_settings": [],
        "ufw_deny": [],
    }
    for line in text.splitlines():
        if line.startswith("LISTEN="):
            d["listen"].append(line.split("=", 1)[1])
            continue
        if "=" not in line:
            continue
        k, _, v = line.partition("=")
        if k == "F2B_LINE":
            d["f2b_lines"].append(v)
        elif k == "REMOTE_BAK":
            d["remote_bak"].append(v)
        elif k == "XUI_SETTING":
            d["xui_settings"].append(v)
        elif k == "UFW_DENY":
            d["ufw_deny"].append(v)
        elif k.startswith("CERTBOT"):
            d.setdefault("certbot", []).append(line)
        else:
            d["raw_kv"][k] = v
    return d


def listen_binds_for_port(listen_addrs: list[str], port: int) -> list[str]:
    hits = []
    suffix = f":{port}"
    for addr in listen_addrs:
        if addr.endswith(suffix) or addr.endswith(f"]:{port}"):
            hits.append(addr)
    return hits


def is_localhost_only(binds: list[str]) -> bool:
    if not binds:
        return True
    for b in binds:
        if b.startswith("127.") or b.startswith("[::1]") or b.startswith("::1"):
            continue
        # wildcard / public
        return False
    return True


def ufw_denies_port(ufw_deny_lines: list[str], port: int) -> bool:
    token = str(port)
    for line in ufw_deny_lines:
        # examples: "2096/tcp                   DENY IN     Anywhere"
        if re.search(rf"(^|\s){re.escape(token)}(/tcp|/udp)?(\s|$)", line, re.I) and re.search(
            r"DENY(\s+IN)?", line, re.I
        ):
            return True
    return False


def classify_not_public(
    port: int,
    listen_addrs: list[str],
    ufw_deny_lines: list[str],
    local_tcp_open: bool,
) -> dict:
    """Operator-local TCP is unreliable while on the node VPN (hairpin).

    Prefer remote listen binding + UFW DENY as authority for expected-not-public.
    """
    binds = listen_binds_for_port(listen_addrs, port)
    localhost_only = is_localhost_only(binds)
    denied = ufw_denies_port(ufw_deny_lines, port)
    if localhost_only and not any(
        b.startswith("0.0.0.0") or b.startswith("*") or b.startswith("[::]")
        for b in binds
    ):
        return {
            "publicly_exposed": False,
            "reason": "localhost_bind_only_or_absent",
            "binds": binds,
            "ufw_deny": denied,
            "local_tcp_open": local_tcp_open,
            "local_tcp_note": "ignored_for_not_public_when_localhost_only",
        }
    if denied:
        return {
            "publicly_exposed": False,
            "reason": "ufw_deny",
            "binds": binds,
            "ufw_deny": True,
            "local_tcp_open": local_tcp_open,
            "local_tcp_note": (
                "local_open_may_be_vpn_hairpin_artifact"
                if local_tcp_open
                else "local_closed"
            ),
        }
    if local_tcp_open:
        return {
            "publicly_exposed": True,
            "reason": "public_bind_and_local_tcp_open_without_ufw_deny",
            "binds": binds,
            "ufw_deny": False,
            "local_tcp_open": True,
        }
    return {
        "publicly_exposed": False,
        "reason": "local_tcp_closed",
        "binds": binds,
        "ufw_deny": denied,
        "local_tcp_open": False,
    }


def pct_from_str(s: str | None) -> float | None:
    if not s:
        return None
    m = re.search(r"(\d+(?:\.\d+)?)", str(s).replace("%", ""))
    return float(m.group(1)) if m else None


def classify_backup_age(days: float | None, thr: dict) -> str:
    if days is None:
        return "UNKNOWN"
    if days <= thr["backup_fresh_days"]:
        return "FRESH"
    if days <= thr["backup_aging_days"]:
        return "AGING"
    return "STALE"


def stamp_from_name(name: str) -> datetime | None:
    m = re.search(r"(20\d{6}T\d{6}Z)", name)
    if not m:
        return None
    return datetime.strptime(m.group(1), "%Y%m%dT%H%M%SZ").replace(tzinfo=timezone.utc)


def local_backup_state(node: dict, thr: dict) -> dict:
    bak_dir = Path(node["local_backup_dir"])
    preferred_stamp = node.get("preferred_backup_stamp")
    glob_pat = node.get("preferred_backup_glob", "*.tgz")
    result = {
        "dir_exists": bak_dir.is_dir(),
        "preferred_stamp": preferred_stamp,
        "selected": None,
        "age_days": None,
        "freshness": "UNKNOWN",
        "size_bytes": None,
        "sha_sidecar_present": False,
    }
    if not bak_dir.is_dir():
        return result
    candidates = sorted(bak_dir.glob(glob_pat), key=lambda p: p.name, reverse=True)
    chosen = None
    if preferred_stamp:
        for p in candidates:
            if preferred_stamp in p.name:
                chosen = p
                break
    if chosen is None and candidates:
        chosen = candidates[0]
    if chosen is None:
        return result
    result["selected"] = chosen.name
    result["size_bytes"] = chosen.stat().st_size
    sha = Path(str(chosen) + ".sha256")
    result["sha_sidecar_present"] = sha.is_file()
    ts = stamp_from_name(chosen.name)
    if ts:
        days = (utc_now() - ts).total_seconds() / 86400.0
        result["age_days"] = round(days, 2)
        result["backup_timestamp_utc"] = ts.isoformat()
        result["freshness"] = classify_backup_age(days, thr)
    return result


def classify_tls(days: float | None, thr: dict) -> str:
    if days is None:
        return "UNKNOWN"
    if days < thr["tls_fail_days"]:
        return "FAIL"
    if days < thr["tls_warn_days"]:
        return "WARN"
    return "PASS"


def check_node(node: dict, thr: dict, evidence_dir: Path) -> dict:
    nid = node["id"]
    host = node["ipv4"]
    domain = node["domain"]
    ssh_port = int(node["ssh_port"])
    vpn_port = int(node["vpn_port"])
    sni = node.get("tls_sni") or domain

    report: dict = {
        "node_id": nid,
        "inventory_ref": node.get("inventory_ref"),
        "label": node.get("label"),
        "checked_utc": utc_now().isoformat(),
        "soak_checkpoint": "T0",
        "network": {},
        "server": {},
        "services": {},
        "ports": {},
        "backup": {},
        "residuals": [],
        "issues": [],
        "warnings": [],
        "verdict": "FAIL",
        "real_workload_documented": node.get("real_workload_documented", {}),
        "mutations": {
            "server": 0,
            "vpn": 0,
            "client": 0,
            "reboot": 0,
        },
    }

    dns = dns_a(domain)
    report["network"]["dns_a"] = dns
    report["network"]["dns_ok"] = host in dns if dns else False
    if dns and host not in dns:
        report["warnings"].append(f"DNS A for {domain} does not include {host}: {dns}")

    ssh_tcp = tcp(host, ssh_port)
    vpn_tcp = tcp(host, vpn_port)
    report["network"]["ssh_tcp"] = {"port": ssh_port, "open": ssh_tcp}
    report["network"]["vpn_tcp"] = {"port": vpn_port, "open": vpn_tcp}
    tls = tls_probe(host, vpn_port, sni)
    report["network"]["tls_8443"] = tls
    report["network"]["tls_class"] = classify_tls(tls.get("days_remaining"), thr)
    if not ssh_tcp:
        report["issues"].append(f"SSH TCP :{ssh_port} closed/unreachable")
    if not vpn_tcp:
        report["issues"].append(f"VPN TCP :{vpn_port} closed/unreachable")
    if not tls.get("ok"):
        report["issues"].append("TLS handshake :8443 failed")
    elif report["network"]["tls_class"] == "FAIL":
        report["issues"].append("TLS certificate expires within fail threshold")
    elif report["network"]["tls_class"] == "WARN":
        report["warnings"].append("TLS certificate within warn window")

    port_map = {}
    for p in node.get("expected_public_tcp", []):
        open_ = tcp(host, int(p))
        port_map[str(p)] = {"expected": "public", "open": open_, "method": "local_tcp"}
        if not open_:
            report["issues"].append(f"Expected public TCP :{p} not reachable")
    # expected_not_public evaluated after remote probe (UFW/listen authority)
    not_public_local = {
        int(p): tcp(host, int(p)) for p in node.get("expected_not_public_tcp", [])
    }
    for p in node.get("known_residual_public_tcp", []):
        open_ = tcp(host, int(p))
        port_map[str(p)] = {
            "expected": "known_residual_public",
            "open": open_,
            "method": "local_tcp",
        }
        report["residuals"].append(
            {
                "port": int(p),
                "class": "KNOWN_RESIDUAL_PUBLIC",
                "open": open_,
                "note": "Documented residual — does not auto-fail",
            }
        )
    report["ports"] = port_map

    key_path = Path(node["ssh_key_local"])
    report["network"]["ssh_key_present"] = key_path.is_file()
    remote_text = ""
    parsed_listen: list[str] = []
    parsed_ufw_deny: list[str] = []
    if ssh_tcp and key_path.is_file():
        try:
            c = ssh_connect(host, ssh_port, node["ssh_user"], key_path)
            code, out, err = ssh_run(c, REMOTE_PROBE, timeout=90)
            c.close()
            remote_text = redact(out + ("\n" + err if err else ""))
            (evidence_dir / f"{nid}-remote.txt").write_text(remote_text, encoding="utf-8")
            parsed = parse_remote(out)
            parsed_listen = parsed.get("listen", [])
            parsed_ufw_deny = parsed.get("ufw_deny", [])
            kv = parsed["raw_kv"]
            report["server"] = {
                "hostname": kv.get("HOSTNAME"),
                "uptime_sec": int(kv["UPTIME_SEC"]) if kv.get("UPTIME_SEC", "").isdigit() else None,
                "load": kv.get("LOAD"),
                "mem_total": int(kv["MEM_TOTAL"]) if kv.get("MEM_TOTAL", "").isdigit() else None,
                "mem_used": int(kv["MEM_USED"]) if kv.get("MEM_USED", "").isdigit() else None,
                "mem_avail": int(kv["MEM_AVAIL"]) if kv.get("MEM_AVAIL", "").isdigit() else None,
                "swap_total": int(kv["SWAP_TOTAL"]) if kv.get("SWAP_TOTAL", "").isdigit() else None,
                "swap_used": int(kv["SWAP_USED"]) if kv.get("SWAP_USED", "").isdigit() else None,
                "root_usepct": pct_from_str(kv.get("ROOT_USEPCT")),
                "inode_usepct": pct_from_str(kv.get("INODE_USEPCT")),
                "ufw_status": kv.get("UFW_STATUS"),
                "listen_sample": parsed_listen,
            }
            mt = report["server"].get("mem_total") or 0
            ma = report["server"].get("mem_avail") or 0
            if mt > 0:
                avail_pct = 100.0 * ma / mt
                report["server"]["mem_avail_pct"] = round(avail_pct, 2)
                if avail_pct < thr["ram_available_warn_pct"]:
                    report["warnings"].append(
                        f"RAM available {avail_pct:.1f}% below warn threshold"
                    )
            st = report["server"].get("swap_total") or 0
            su = report["server"].get("swap_used") or 0
            if st > 0:
                swap_pct = 100.0 * su / st
                report["server"]["swap_used_pct"] = round(swap_pct, 2)
                if swap_pct >= thr["swap_used_warn_pct"]:
                    report["warnings"].append(f"Swap used {swap_pct:.1f}%")
            elif st == 0:
                report["warnings"].append("Swap total is 0")
            disk_pct = report["server"].get("root_usepct")
            if disk_pct is not None:
                if disk_pct >= thr["disk_fail_pct"]:
                    report["issues"].append(f"Root disk {disk_pct}% >= fail threshold")
                elif disk_pct >= thr["disk_warn_pct"]:
                    report["warnings"].append(f"Root disk {disk_pct}% >= warn threshold")

            ssh_ok = kv.get("SSH_ACTIVE_EXIT") == "0"
            xui_ok = kv.get("XUI_ACTIVE") == "0"
            xray_ok = kv.get("XRAY_PROC") == "0"
            f2b_ok = kv.get("F2B_ACTIVE") == "0"
            ufw_active = "active" in (kv.get("UFW_STATUS") or "").lower()
            report["services"] = {
                "ssh_active": ssh_ok,
                "x_ui_active": xui_ok,
                "x_ui_enabled": kv.get("XUI_ENABLED") == "0",
                "xray_process": xray_ok,
                "fail2ban_active": f2b_ok,
                "ufw_active": ufw_active,
                "nginx_active": kv.get("NGINX_ACTIVE") == "0",
                "certbot": parsed.get("certbot", []),
                "xui_settings_sanitized": parsed.get("xui_settings", []),
                "remote_exit": code,
            }
            if not ssh_ok:
                report["issues"].append("sshd/ssh service not active")
            if not xui_ok:
                report["issues"].append("x-ui service not active")
            if not xray_ok:
                report["issues"].append("xray process not detected")
            if not f2b_ok:
                report["warnings"].append("fail2ban not active")
            if not ufw_active:
                report["warnings"].append("UFW not active")
            if "nginx" in node.get("checks_extra", []):
                if not report["services"]["nginx_active"]:
                    report["issues"].append("nginx expected but not active")
            if "certbot" in node.get("checks_extra", []):
                if not any("CERTBOT=present" in x for x in parsed.get("certbot", [])):
                    report["warnings"].append("certbot not present")
            report["server"]["remote_backups_sample"] = parsed.get("remote_bak", [])[-5:]
        except Exception as e:
            report["issues"].append(f"SSH remote probe failed: {type(e).__name__}")
            (evidence_dir / f"{nid}-remote-error.txt").write_text(
                redact(f"{type(e).__name__}: {e}\n"), encoding="utf-8"
            )
    else:
        if not key_path.is_file():
            report["issues"].append("SSH private key missing in local contour")

    for p, local_open in not_public_local.items():
        cls = classify_not_public(p, parsed_listen, parsed_ufw_deny, local_open)
        port_map[str(p)] = {
            "expected": "not_public",
            "publicly_exposed": cls["publicly_exposed"],
            "method": "remote_listen_ufw_plus_local_tcp_hint",
            **cls,
        }
        if cls["publicly_exposed"]:
            report["issues"].append(f"Expected not-public TCP :{p} appears exposed")
        elif local_open and not cls["publicly_exposed"]:
            report["residuals"].append(
                {
                    "port": p,
                    "class": "LOCAL_TCP_OPEN_WHILE_FIREWALLED_OR_LOCALHOST",
                    "note": "Operator-local TCP open may be VPN hairpin; remote UFW/listen says not public",
                }
            )
    report["ports"] = port_map

    bak = local_backup_state(node, thr)
    report["backup"] = bak
    if bak["freshness"] == "STALE":
        report["warnings"].append("Preferred local backup STALE")
    elif bak["freshness"] == "AGING":
        report["warnings"].append("Preferred local backup AGING")
    elif bak["freshness"] == "UNKNOWN":
        report["warnings"].append("Local backup freshness UNKNOWN")
    if not bak.get("sha_sidecar_present"):
        report["warnings"].append("SHA sidecar missing for selected backup (existence-only check)")

    residuals_open = [r for r in report["residuals"] if r.get("open")]
    has_residuals = bool(report["residuals"])
    if report["issues"]:
        report["verdict"] = "FAIL"
    elif has_residuals or report["warnings"]:
        report["verdict"] = "PASS_WITH_RESIDUALS"
    else:
        report["verdict"] = "PASS"

    # Known public residuals (open=true) are informational only; hairpin notes also
    # keep PASS_WITH_RESIDUALS without failing the node.
    _ = residuals_open  # retained for evidence readers / future strict mode

    (evidence_dir / f"{nid}-result.json").write_text(
        redact(json.dumps(report, indent=2) + "\n"), encoding="utf-8"
    )
    return report


def main() -> int:
    ap = argparse.ArgumentParser(description="MARS VPN nodes lightweight health checker")
    ap.add_argument("--nodes", default=str(DEFAULT_NODES), help="Path to nodes.json")
    ap.add_argument(
        "--node",
        action="append",
        dest="only",
        help="Limit to node id (repeatable). Default: all",
    )
    ap.add_argument(
        "--evidence-dir",
        default=str(DEFAULT_EVIDENCE_ROOT),
        help="Evidence output directory",
    )
    ap.add_argument(
        "--checkpoint",
        default="T0",
        help="Soak checkpoint label (T0 / T+24h / T+72h / T+7d)",
    )
    args = ap.parse_args()

    cfg = json.loads(Path(args.nodes).read_text(encoding="utf-8"))
    thr = cfg["thresholds"]
    evidence_dir = Path(args.evidence_dir)
    evidence_dir.mkdir(parents=True, exist_ok=True)

    nodes = cfg["nodes"]
    if args.only:
        want = set(args.only)
        nodes = [n for n in nodes if n["id"] in want]

    summary = {
        "wave": "VPN-NODES-LIGHTWEIGHT-HEALTH",
        "checkpoint": args.checkpoint,
        "checked_utc": utc_now().isoformat(),
        "nodes": [],
        "combined_verdict": "FAIL",
        "soak_long_term": "NOT_YET_PROVEN",
        "acceptance_tokens": {
            "SOAK_T0_PASS": False,
            "SOAK_24H_PASS": False,
            "SOAK_72H_PASS": False,
            "SOAK_7D_PASS": False,
        },
    }

    verdicts = []
    for node in nodes:
        print(f"Checking {node['id']} ...", flush=True)
        r = check_node(node, thr, evidence_dir)
        r["soak_checkpoint"] = args.checkpoint
        summary["nodes"].append(
            {
                "id": r["node_id"],
                "verdict": r["verdict"],
                "uptime_sec": r.get("server", {}).get("uptime_sec"),
                "disk_usepct": r.get("server", {}).get("root_usepct"),
                "mem_avail_pct": r.get("server", {}).get("mem_avail_pct"),
                "swap_used_pct": r.get("server", {}).get("swap_used_pct"),
                "tls_days": r.get("network", {}).get("tls_8443", {}).get("days_remaining"),
                "tls_not_after": r.get("network", {}).get("tls_8443", {}).get("not_after"),
                "backup_freshness": r.get("backup", {}).get("freshness"),
                "backup_selected": r.get("backup", {}).get("selected"),
                "residuals": r.get("residuals", []),
                "issues": r.get("issues", []),
                "warnings": r.get("warnings", []),
            }
        )
        verdicts.append(r["verdict"])
        print(f"  -> {r['verdict']}", flush=True)

    if any(v == "FAIL" for v in verdicts):
        summary["combined_verdict"] = "FAIL"
    elif any(v == "PASS_WITH_RESIDUALS" for v in verdicts):
        summary["combined_verdict"] = "PASS_WITH_RESIDUALS"
    elif verdicts and all(v == "PASS" for v in verdicts):
        summary["combined_verdict"] = "PASS"

    if args.checkpoint == "T0" and summary["combined_verdict"] != "FAIL":
        summary["acceptance_tokens"]["SOAK_T0_PASS"] = True

    (evidence_dir / "Z-summary.json").write_text(
        redact(json.dumps(summary, indent=2) + "\n"), encoding="utf-8"
    )
    print(json.dumps(summary, indent=2))
    return 0 if summary["combined_verdict"] != "FAIL" else 2


if __name__ == "__main__":
    raise SystemExit(main())
