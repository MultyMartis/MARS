"""Create GROUP 2 operator checkpoint ZIP."""
import hashlib
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ws = Path(__file__).resolve().parents[2]
storage = Path(r"C:\MARS Phenix\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v7\operator-checkpoints")
storage.mkdir(parents=True, exist_ok=True)
zip_path = storage / "FP-0002-V7-SERVICE-SUBDIVISION-PNG-GROUP-2-BEFORE-SOURCE.zip"

include_paths = [
    ws / "src",
    ws / "package.json",
    ws / "package-lock.json",
    ws / "gulpfile.js",
    ws / "foundation" / "FP-0002-V7-OPERATIONAL-STATUS.md",
]

exclude_dirs = {"node_modules", "dist", ".git"}
exclude_names = {".DS_Store"}

manifest_lines = [
    "# BACKUP-MANIFEST — FP-0002 GROUP 2",
    "",
    f"- timestamp: {datetime.now(timezone.utc).isoformat()}",
    "- branch: mars/canonical-post-recovery",
    "- GROUP 1 commit: f3917bf6",
    "- scope: GROUP 2 CTA-01 + Program + CTA-02 transition",
    "- exclusions: node_modules, dist, Figma, INCOMING, operator PNG, temp, git metadata, ORCA WIP",
    "",
]

with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
    for base in include_paths:
        if base.is_file():
            arc = base.relative_to(ws).as_posix()
            zf.write(base, arc)
            manifest_lines.append(f"- {arc}")
            continue
        for path in base.rglob("*"):
            if not path.is_file():
                continue
            rel = path.relative_to(ws)
            if any(part in exclude_dirs for part in rel.parts):
                continue
            if path.name in exclude_names:
                continue
            zf.write(path, rel.as_posix())

restore = storage / "RESTORE-INSTRUCTIONS-GROUP-2.txt"
restore.write_text(
    "Restore: extract ZIP into workspaces/fp-0002-shpigovsky-v7/ preserving paths.\n",
    encoding="utf-8",
)
manifest_path = storage / "BACKUP-MANIFEST-GROUP-2.md"
manifest_path.write_text("\n".join(manifest_lines) + "\n", encoding="utf-8")

sha = hashlib.sha256(zip_path.read_bytes()).hexdigest().upper()
(storage / "CHECKSUMS-SHA256-GROUP-2.txt").write_text(f"{sha}  {zip_path.name}\n", encoding="utf-8")
print("zip", zip_path)
print("sha256", sha)
print("ok", zip_path.exists(), zipfile.is_zipfile(zip_path))
