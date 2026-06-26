"""GROUP 3 operator checkpoint backup from committed GROUP 2 HEAD."""
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
zip_path = out_dir / "FP-0002-V7-PG-004-SERVICE-LEAF-GROUP-3-BEFORE-SOURCE.zip"
staging = out_dir / "_staging-pg004-group3"
head = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=repo).decode().strip()
branch = subprocess.check_output(["git", "branch", "--show-current"], cwd=repo).decode().strip()
ts = datetime.now(timezone.utc).isoformat()

if staging.exists():
    shutil.rmtree(staging)
staging.mkdir(parents=True)

archive_paths = [
    f"{prefix}src",
    f"{prefix}foundation/FP-0002-V7-OPERATIONAL-STATUS.md",
    f"{prefix}foundation/FP-0002-V7-PNG-GROUPED-PAGE-IMPLEMENTATION-PROTOCOL-v1.md",
    f"{prefix}plans/service-leaf-page",
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

manifest = f"""# BACKUP-MANIFEST — FP-0002 PG-004 SERVICE LEAF GROUP 3

- repository: C:\\MARS Phenix\\AI MARS
- workspace: workspaces/fp-0002-shpigovsky-v7
- branch: {branch}
- HEAD: {head}
- group_1_commits: a1780ebf, 38ac867a
- group_2_commits: 4a9fe6e9
- task_scope: FP-0002-PG-004 SERVICE LEAF GROUP 3 (approach + team + cards + landscape)
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
2. Copy contents into `workspaces/fp-0002-shpigovsky-v7/` preserving relative paths.
3. Run portable Node `npm install` and `npm run build`.
4. GROUP 1 commits: a1780ebf / 38ac867a; GROUP 2 commit: 4a9fe6e9.
5. This backup is pre–Service Leaf GROUP 3 implementation at HEAD `{head}`.
""".format(head=head),
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
