import hashlib
import os
import shutil
import subprocess
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ws = Path(r"C:\MARS Phenix\AI MARS\workspaces\fp-0002-shpigovsky-v7")
out_dir = Path(
    r"C:\MARS Phenix\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v7\operator-checkpoints"
)
zip_path = out_dir / "FP-0002-V7-PG-004-SERVICE-LEAF-PASS-OPENING-BEFORE-SOURCE.zip"
staging = out_dir / "_staging-pg004-pass-opening"
head = (
    subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=ws.parent.parent)
    .decode()
    .strip()
)
branch = (
    subprocess.check_output(["git", "branch", "--show-current"], cwd=ws.parent.parent)
    .decode()
    .strip()
)
ts = datetime.now(timezone.utc).isoformat()

if staging.exists():
    shutil.rmtree(staging)
staging.mkdir(parents=True)

include_roots = [
    "src",
    "foundation/FP-0002-V7-OPERATIONAL-STATUS.md",
    "foundation/FP-0002-V7-PNG-GROUPED-PAGE-IMPLEMENTATION-PROTOCOL-v1.md",
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

manifest = f"""# BACKUP-MANIFEST — FP-0002 PG-004 SERVICE LEAF PASS OPENING

- repository: C:\\MARS Phenix\\AI MARS
- workspace: workspaces/fp-0002-shpigovsky-v7
- branch: {branch}
- HEAD: {head}
- service_subdivision_reference_commit: eb10c71b
- service_subdivision_stable_tag: fp-0002-v7-service-subdivision-internal-page-reference-01
- task_scope: FP-0002-PG-004 SERVICE LEAF INTERNAL PAGE — PASS OPENING (planning only)
- timestamp_utc: {ts}
- fp0002_wip: untracked service-subdivision-procedure-v1.html partial (not in backup scope change)
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
2. Copy `src/`, `package.json`, `package-lock.json`, `gulpfile.js`, and `foundation/FP-0002-V7-OPERATIONAL-STATUS.md`, `foundation/FP-0002-V7-PNG-GROUPED-PAGE-IMPLEMENTATION-PROTOCOL-v1.md` into `workspaces/fp-0002-shpigovsky-v7/`.
3. Run `npm install` and `npm run build` with portable Node.
4. Baseline authority remains commit `eb10c71b` / tag `fp-0002-v7-service-subdivision-internal-page-reference-01` for Service Subdivision reference.
5. This backup is pre–Service Leaf Pass Opening planning; do not treat planning artifacts inside the ZIP as implementation authority.
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

receipt = f"""# Backup receipt — FP-0002 PG-004 Pass Opening

- ZIP: `{zip_path}`
- ZIP_SHA256: `{zip_hash}`
- entries: {len(checksums)}
- timestamp_utc: {ts}
- HEAD: {head}
- verdict: COMPLETE
"""
receipt_path = ws / "reviews/service-leaf-pass-opening/BACKUP-RECEIPT-v1.md"
receipt_path.write_text(receipt, encoding="utf-8")

shutil.rmtree(staging)
print("ZIP", zip_path)
print("ZIP_SHA256", zip_hash)
print("entries", len(checksums))
