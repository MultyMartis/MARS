"""Create GROUP 4 operator checkpoint ZIP."""
import hashlib
import subprocess
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ws = Path(__file__).resolve().parents[2]
repo = ws.parents[1]
storage = Path(r"C:\MARS Phenix\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v7\operator-checkpoints")
storage.mkdir(parents=True, exist_ok=True)
zip_path = storage / "FP-0002-V7-SERVICE-SUBDIVISION-PNG-GROUP-4-BEFORE-SOURCE.zip"

head = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=repo, text=True).strip()

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
    "# BACKUP-MANIFEST — FP-0002 GROUP 4",
    "",
    f"- timestamp: {datetime.now(timezone.utc).isoformat()}",
    "- branch: mars/canonical-post-recovery",
    f"- HEAD: {head}",
    "- GROUP 1 commit: f3917bf6",
    "- GROUP 2 commit: 41777d4a",
    "- GROUP 3 commit: 57ac6d34",
    "- scope: GROUP 4 corridor / approach intro / team photo / approach service cards",
    "- exclusions: node_modules, dist, Figma, INCOMING, operator PNG, temp, git metadata, ORCA WIP",
    "",
    "## Included paths",
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

restore = """# RESTORE-INSTRUCTIONS — FP-0002 GROUP 4

1. Stop preview server if running.
2. Extract `FP-0002-V7-SERVICE-SUBDIVISION-PNG-GROUP-4-BEFORE-SOURCE.zip` into `workspaces/fp-0002-shpigovsky-v7/` preserving relative paths.
3. Verify `src/pages/usluga-podrazdel-v1.html` matches pre-GROUP-4 state.
4. Run `npm run build` from workspace root.
5. Confirm HEAD was `57ac6d34` at backup time (GROUP 3 baseline).
"""
(storage / "RESTORE-INSTRUCTIONS.md").write_text(restore, encoding="utf-8")
(storage / "BACKUP-MANIFEST.md").write_text("\n".join(manifest_lines) + "\n", encoding="utf-8")

sha = hashlib.sha256(zip_path.read_bytes()).hexdigest().upper()
(storage / "CHECKSUMS-SHA256.txt").write_text(f"{sha}  {zip_path.name}\n", encoding="utf-8")
print("zip", zip_path)
print("sha256", sha)
print("ok", zip_path.exists(), zipfile.is_zipfile(zip_path))
