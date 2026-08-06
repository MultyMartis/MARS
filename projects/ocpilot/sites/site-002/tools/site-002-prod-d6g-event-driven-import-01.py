#!/usr/bin/env python3
"""SITE-002 D6G deploy: wrapper+contract+admin module+menu snippet via FTP."""
from __future__ import annotations

import argparse
import ftplib
import hashlib
import io
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

OPERATION = "SITE-002-PROD-D6G-EVENT-DRIVEN-1C-IMPORT-01"
SECRETS = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOY_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-D6G-EVENT-DRIVEN-1C-IMPORT-01"
)
# Prefer worktree if present
WT = Path(r"X:\AI MARS STORAGE\git-sync-d6g-event-driven\repo")
MAIN = Path(r"X:\AI MARS")
REPO = WT if (WT / "projects/ocpilot/sites/site-002/tools/mars_1c_import_wrapper.php").is_file() else MAIN
TOOLS = REPO / "projects/ocpilot/sites/site-002/tools"
ADMIN = REPO / "projects/ocpilot/sites/site-002/opencart-admin/mars_1c_exchange"


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def load_ftp_fields() -> dict[str, str]:
    text = SECRETS.read_text(encoding="utf-8")
    # Prefer PRODUCTION section
    block = text
    pm = re.search(r"##\s*PRODUCTION[\s\S]*?(?=##\s|\Z)", text, re.I)
    if pm:
        block = pm.group(0)
    m = re.search(r"###\s*FTP\s*/\s*SFTP\s*([\s\S]*?)(?=^### |\Z)", block, re.M | re.I)
    if not m:
        m = re.search(r"###\s*FTP\s*/\s*SFTP\s*([\s\S]*?)(?=^### |\Z)", text, re.M | re.I)
    if not m:
        raise RuntimeError("FTP section not found")
    fields: dict[str, str] = {}
    for line in m.group(1).splitlines():
        lm = re.match(r"[-*]?\s*(host|port|username|user|login|password|pass)\s*[:=]\s*(.+)$", line.strip(), re.I)
        if not lm:
            continue
        key = lm.group(1).lower()
        val = lm.group(2).strip().strip("`").strip('"').strip("'")
        if key == "host":
            fields["host"] = val
        elif key == "port":
            fields["port"] = val
        elif key in ("username", "user", "login"):
            fields["username"] = val
        elif key in ("password", "pass"):
            fields["password"] = val
    fields.setdefault("port", "21")
    for req in ("host", "username", "password"):
        if not fields.get(req):
            raise RuntimeError(f"Missing FTP {req}")
    return fields


def ftp_connect(fields: dict[str, str]) -> ftplib.FTP:
    ftp = ftplib.FTP()
    ftp.connect(fields["host"], int(fields["port"]), timeout=180)
    ftp.login(fields["username"], fields["password"])
    return ftp


def list_names(ftp: ftplib.FTP, path: str) -> list[str]:
    names: list[str] = []
    try:
        for name, _ in ftp.mlsd(path):
            if name not in (".", ".."):
                names.append(name)
        return names
    except Exception:
        lines: list[str] = []
        try:
            ftp.retrlines("LIST " + path, lines.append)
        except Exception:
            return []
        for line in lines:
            parts = line.split()
            if parts:
                names.append(parts[-1])
        return names


def resolve_roots(ftp: ftplib.FTP) -> dict[str, str]:
    pwd = ftp.pwd() or "/"
    public = None
    storage = None
    for base in [pwd, "/"]:
        names = {n.lower(): n for n in list_names(ftp, base)}
        if "public_html" in names:
            public = base.rstrip("/") + "/" + names["public_html"]
        if "storage" in names:
            storage = base.rstrip("/") + "/" + names["storage"]
        if public and storage:
            break
    if not public or not storage:
        raise RuntimeError("Could not resolve public_html/storage")
    return {"public": public, "storage": storage}


def ftp_mkdirs(ftp: ftplib.FTP, remote_dir: str) -> None:
    parts = remote_dir.strip("/").split("/")
    cur = ""
    for p in parts:
        cur += "/" + p
        try:
            ftp.mkd(cur)
        except ftplib.error_perm:
            pass


def ftp_upload(ftp: ftplib.FTP, remote: str, data: bytes) -> None:
    ftp_mkdirs(ftp, "/".join(remote.split("/")[:-1]))
    ftp.storbinary("STOR " + remote, io.BytesIO(data))


def ftp_download(ftp: ftplib.FTP, remote: str) -> bytes | None:
    bio = io.BytesIO()
    try:
        ftp.retrbinary("RETR " + remote, bio.write)
    except ftplib.error_perm:
        return None
    return bio.getvalue()


UPLOADS = [
    ("tools/mars_1c_import_wrapper.php", "storage", "mars-tools/cron/mars_1c_import_wrapper.php"),
    ("tools/mars_1c_import_run_contract.php", "storage", "mars-tools/cron/mars_1c_import_run_contract.php"),
    (
        "opencart-admin/mars_1c_exchange/admin/controller/tool/mars_1c_exchange.php",
        "public",
        "admin/controller/tool/mars_1c_exchange.php",
    ),
    (
        "opencart-admin/mars_1c_exchange/admin/model/tool/mars_1c_exchange.php",
        "public",
        "admin/model/tool/mars_1c_exchange.php",
    ),
    (
        "opencart-admin/mars_1c_exchange/admin/view/template/tool/mars_1c_exchange.twig",
        "public",
        "admin/view/template/tool/mars_1c_exchange.twig",
    ),
    (
        "opencart-admin/mars_1c_exchange/admin/language/ru-ru/tool/mars_1c_exchange.php",
        "public",
        "admin/language/ru-ru/tool/mars_1c_exchange.php",
    ),
    (
        "opencart-admin/mars_1c_exchange/admin/language/en-gb/tool/mars_1c_exchange.php",
        "public",
        "admin/language/en-gb/tool/mars_1c_exchange.php",
    ),
]


def local_bytes(rel: str) -> bytes:
    if rel.startswith("tools/"):
        return (TOOLS / rel[len("tools/") :]).read_bytes()
    if rel.startswith("opencart-admin/"):
        return (REPO / "projects/ocpilot/sites/site-002" / rel).read_bytes()
    raise RuntimeError(rel)


def patch_column_left(src: str) -> tuple[str, bool]:
    marker = "tool/mars_1c_exchange"
    if marker in src:
        return src, False
    snippet = """
\t\t\tif ($this->user->hasPermission('access', 'tool/mars_1c_exchange')) {
\t\t\t\t$system[] = array(
\t\t\t\t\t'name'\t   => 'Обмен с 1С',
\t\t\t\t\t'href'\t   => $this->url->link('tool/mars_1c_exchange', 'user_token=' . $this->session->data['user_token'], true),
\t\t\t\t\t'children' => array()
\t\t\t\t);
\t\t\t}
"""
    # Insert before system menu is appended to $data['menus'] if possible, else before return
    idx = src.find("$data['menus'][] = array(")
    # Prefer insertion near other tool entries
    tool_idx = src.find("'route' => 'tool/")
    if tool_idx == -1:
        tool_idx = src.find("tool/backup")
    if tool_idx != -1:
        # find end of that system[] push block after tool_idx — fallback: before closing of system building
        anchor = src.find("$data['menus'][] = array(\n\t\t\t\t'id'", tool_idx)
        if anchor == -1:
            anchor = src.find("if ($system)", tool_idx)
        if anchor != -1:
            return src[:anchor] + snippet + "\n" + src[anchor:], True
    # fallback before final return $this->load->view
    anchor = src.rfind("return $this->load->view('common/column_left'")
    if anchor != -1:
        return src[:anchor] + snippet + "\n" + src[anchor:], True
    return src, False


def cmd_deploy(_: argparse.Namespace) -> int:
    DEPLOY_ROOT.mkdir(parents=True, exist_ok=True)
    fields = load_ftp_fields()
    ftp = ftp_connect(fields)
    roots = resolve_roots(ftp)
    results = []
    for local_rel, root_key, remote_rel in UPLOADS:
        data = local_bytes(local_rel)
        remote = roots[root_key].rstrip("/") + "/" + remote_rel
        before = ftp_download(ftp, remote)
        if before is not None:
            (DEPLOY_ROOT / "server-source-before" / Path(remote_rel).name).write_bytes(before)
        ftp_upload(ftp, remote, data)
        after = ftp_download(ftp, remote)
        ok = after is not None and sha256(after) == sha256(data)
        results.append({"remote": remote_rel, "ok": ok, "sha256": sha256(data)})
        (DEPLOY_ROOT / "server-source-after" / Path(remote_rel).name).write_bytes(after or b"")

    # column_left patch
    col_remote = roots["public"].rstrip("/") + "/admin/controller/common/column_left.php"
    col_before = ftp_download(ftp, col_remote)
    patched = False
    if col_before:
        (DEPLOY_ROOT / "server-source-before" / "column_left.php").write_bytes(col_before)
        new_src, changed = patch_column_left(col_before.decode("utf-8", errors="replace"))
        if changed:
            ftp_upload(ftp, col_remote, new_src.encode("utf-8"))
            patched = True
        (DEPLOY_ROOT / "server-source-after" / "column_left.php").write_bytes(
            (ftp_download(ftp, col_remote) or b"")
        )

    # clear modification cache files (not whole storage)
    mod_dir = roots["storage"].rstrip("/") + "/modification"
    cleared = []
    for name in list_names(ftp, mod_dir):
        if name.endswith(".php") or name == "index.html":
            # only clear admin common cache if present; avoid broad wipe — delete known admin cache tree lightly
            pass
    # Clear admin twig/modification for column_left if exists
    for rel in [
        "modification/admin/controller/common/column_left.php",
        "modification/admin/view/template/common/column_left.twig",
    ]:
        remote = roots["storage"].rstrip("/") + "/" + rel
        try:
            ftp.delete(remote)
            cleared.append(rel)
        except Exception:
            pass

    ftp.quit()
    summary = {
        "operation": OPERATION,
        "finished_at": utc_now(),
        "uploads": results,
        "column_left_patched": patched,
        "modification_cleared": cleared,
        "all_ok": all(r["ok"] for r in results),
    }
    write_json(DEPLOY_ROOT / "logs" / "deploy.json", summary)
    print(json.dumps({"ok": summary["all_ok"], "column_left_patched": patched, "uploads": len(results)}, ensure_ascii=False))
    return 0 if summary["all_ok"] else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("deploy")
    p.set_defaults(func=cmd_deploy)
    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
