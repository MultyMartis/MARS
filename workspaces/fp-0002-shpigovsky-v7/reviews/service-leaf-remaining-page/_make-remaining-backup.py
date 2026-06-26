"""Pre–remaining-page operator checkpoint backup at GROUP 4 HEAD."""
import hashlib
import io
import os
import shutil
import subprocess
import tarfile
import zipfile
from datetime import datetime, timezone
from pathlib import Path

repo = Path(r"C:\MARS Phenix\AI MARS")
prefix = "workspaces/fp-0002-shpigovsky-v7/"
out_dir = Path(
    r"C:\MARS Phenix\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v7\operator-checkpoints"
)
zip_path = out_dir / "FP-0002-V7-PG-004-SERVICE-LEAF-BEFORE-REMAINING-PAGE-SOURCE.zip"
staging = out_dir / "_staging-pg004-remaining"
head = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=repo).decode().strip()
branch = subprocess.check_output(["git", "branch", "--show-current"], cwd=repo).decode().strip()
ts = datetime.now(timezone.utc).isoformat()

status = subprocess.check_output(["git", "status", "--short", prefix], cwd=repo).decode().strip()

if staging.exists():
    shutil.rmtree(staging)
staging.mkdir(parents=True)

archive_paths = [
    f"{prefix}src/pages/usluga-konechnaya-v1.html",
    f"{prefix}src/partials",
    f"{prefix}src/scss/style.scss",
    f"{prefix}src/js/main.js",
    f"{prefix}src/img/content",
    f"{prefix}foundation/FP-0002-V7-OPERATIONAL-STATUS.md",
    f"{prefix}package.json",
    f"{prefix}package-lock.json",
    f"{prefix}gulpfile.js",
]

tar_bytes = subprocess.check_output(
    ["git", "archive", "--format=tar", "HEAD", *archive_paths],
    cwd=repo,
)
with tarfile.open(fileobj=io.BytesIO(tar_bytes), mode="r:") as tar:
    for member in tar.getmembers():
        rel = member.name
        if not rel.startswith(prefix):
            continue
        target = staging / rel[len(prefix) :]
        if member.isdir():
            target.mkdir(parents=True, exist_ok=True)
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(tar.extractfile(member).read())

manifest = f"""# BACKUP-MANIFEST — FP-0002 PG-004 SERVICE LEAF BEFORE REMAINING PAGE

- repository: C:\\MARS Phenix\\AI MARS
- workspace: workspaces/fp-0002-shpigovsky-v7
- branch: {branch}
- HEAD: {head}
- group_1_commits: a1780ebf, 38ac867a
- group_2_commit: 4a9fe6e9
- group_3_commit: cde12e60
- group_4_commit: edd6a2c7
- service_leaf_status: GROUP_1-4_COMPLETE; GROUP_5-6_NOT_IMPLEMENTED
- task_scope: FP-0002-PG-004 SERVICE LEAF remaining page (GROUP 5-6 + full assembly)
- timestamp_utc: {ts}
- working_tree_service_leaf_scope:
```
{status or '(clean at HEAD for workspace prefix)'}
```
- exclusions: node_modules, dist, reviews/screenshots, Figma, INCOMING, approved PNG, temp, Git metadata, unrelated ORCA WIP

## Included paths

"""
for root, _, files in os.walk(staging):
    for f in sorted(files):
        rel = (Path(root) / f).relative_to(staging).as_posix()
        manifest += f"- {rel}\n"

(staging / "BACKUP-MANIFEST.md").write_text(manifest, encoding="utf-8")
(staging / "RESTORE-INSTRUCTIONS.md").write_text(
    f"""# Restore instructions

1. Unzip to a clean folder.
2. Copy contents into `workspaces/fp-0002-shpigovsky-v7/` preserving relative paths.
3. Run portable Node: `npm install` and `npm run build`.
4. Baseline HEAD: `{head}` (GROUP 4 complete).
5. This backup is pre–Service Leaf remaining page pass (GROUP 5-6 + shared lower blocks).
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

# Validate required entries
required = [
    "src/pages/usluga-konechnaya-v1.html",
    "src/scss/style.scss",
    "BACKUP-MANIFEST.md",
    "RESTORE-INSTRUCTIONS.md",
]
with zipfile.ZipFile(zip_path, "r") as zf:
    names = set(zf.namelist())
    missing = [r for r in required if r not in names]
    if missing:
        raise SystemExit(f"BACKUP FAILED missing: {missing}")

shutil.rmtree(staging)
print("ZIP", zip_path)
print("ZIP_SHA256", zip_hash)
