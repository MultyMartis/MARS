import hashlib
import os
import shutil
import subprocess
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ws = Path(r"C:\MARS Phenix\AI MARS\workspaces\fp-0002-shpigovsky-v7")
repo = Path(r"C:\MARS Phenix\AI MARS")
out_dir = Path(
    r"C:\MARS Phenix\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v7\operator-checkpoints"
)
zip_path = out_dir / "FP-0002-V7-PG-004-SERVICE-LEAF-GROUP-2-BEFORE-SOURCE.zip"
staging = out_dir / "_staging-pg004-group2"
head = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=repo).decode().strip()
branch = subprocess.check_output(["git", "branch", "--show-current"], cwd=repo).decode().strip()
ts = datetime.now(timezone.utc).isoformat()

if staging.exists():
    shutil.rmtree(staging)
staging.mkdir(parents=True)

include_roots = [
    "src",
    "foundation/FP-0002-V7-OPERATIONAL-STATUS.md",
    "foundation/FP-0002-V7-PNG-GROUPED-PAGE-IMPLEMENTATION-PROTOCOL-v1.md",
    "plans/service-leaf-page",
    "package.json",
    "package-lock.json",
    "gulpfile.js",
]

for item in include_roots:
    src = ws / item
    dst = staging / item
    if src.is_dir():
        shutil.copytree(src, dst, ignore=shutil.ignore_patterns("node_modules", "dist"))
    elif src.is_file():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)

manifest = f"""# BACKUP-MANIFEST — FP-0002 PG-004 SERVICE LEAF GROUP 2

- repository: C:\\MARS Phenix\\AI MARS
- workspace: workspaces/fp-0002-shpigovsky-v7
- branch: {branch}
- HEAD: {head}
- group_1_commits: a1780ebf, 38ac867a
- task_scope: FP-0002-PG-004 SERVICE LEAF GROUP 2 (signs-heading-list through signs-editorial)
- timestamp_utc: {ts}
- fp0002_wip: package-lock.json drift only in working tree
- exclusions: node_modules, dist, reviews screenshots, Figma, INCOMING, operator PNG, temp, Git metadata, unrelated ORCA WIP

## Included paths

"""
for root, _, files in os.walk(staging):
    for f in sorted(files):
        rel = (Path(root) / f).relative_to(staging).as_posix()
        manifest += f"- {rel}\n"

(staging / "BACKUP-MANIFEST.md").write_text(manifest, encoding="utf-8")
(staging / "RESTORE-INSTRUCTIONS.md").write_text(
    """# Restore instructions

1. Unzip to a clean folder.
2. Copy `src/`, `package.json`, `package-lock.json`, `gulpfile.js`, `foundation/FP-0002-V7-OPERATIONAL-STATUS.md`, `foundation/FP-0002-V7-PNG-GROUPED-PAGE-IMPLEMENTATION-PROTOCOL-v1.md`, and `plans/service-leaf-page/` into `workspaces/fp-0002-shpigovsky-v7/`.
3. Run `npm install` and `npm run build` with portable Node.
4. GROUP 1 commits remain `a1780ebf` / `38ac867a`.
5. This backup is pre–Service Leaf GROUP 2 implementation.
""",
    encoding="utf-8",
)

if zip_path.exists():
    zip_path.unlink()

with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
    for root, _, files in os.walk(staging):
        for f in files:
            fp = Path(root) / f
            zf.write(fp, fp.relative_to(staging).as_posix())

checksums = []
with zipfile.ZipFile(zip_path, "r") as zf:
    for info in zf.infolist():
        if info.is_dir():
            continue
        data = zf.read(info.filename)
        checksums.append(f"{hashlib.sha256(data).hexdigest().upper()}  {info.filename}")

zip_hash = hashlib.sha256(zip_path.read_bytes()).hexdigest().upper()
checksum_text = "\n".join(checksums) + f"\n\nZIP_SHA256={zip_hash}\n"
(staging / "CHECKSUMS-SHA256.txt").write_text(checksum_text, encoding="utf-8")

with zipfile.ZipFile(zip_path, "a", zipfile.ZIP_DEFLATED) as zf:
    zf.write(staging / "CHECKSUMS-SHA256.txt", "CHECKSUMS-SHA256.txt")

shutil.rmtree(staging)
print("ZIP", zip_path)
print("ZIP_SHA256", zip_hash)
print("entries", len(checksums))
