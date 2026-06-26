"""Create pre-final-corrections operator checkpoint ZIP from committed HEAD (7886629d)."""
import hashlib
import subprocess
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ws = Path(r"C:\MARS Phenix\AI MARS\workspaces\fp-0002-shpigovsky-v7")
repo = ws.parents[1]
storage = Path(r"C:\MARS Phenix\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v7\operator-checkpoints")
storage.mkdir(parents=True, exist_ok=True)
zip_path = storage / "FP-0002-V7-SERVICE-SUBDIVISION-BEFORE-FINAL-CORRECTIONS.zip"

head = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=repo, text=True).strip()
assert head == "7886629d", f"Expected 7886629d, got {head}"

rel_roots = [
    "src",
    "package.json",
    "package-lock.json",
    "gulpfile.js",
    "foundation/FP-0002-V7-OPERATIONAL-STATUS.md",
]

def git_ls_tree(prefix: str):
    out = subprocess.check_output(
        ["git", "ls-tree", "-r", "--name-only", f"HEAD:{prefix}"],
        cwd=repo,
        text=True,
    )
    return [line.strip() for line in out.splitlines() if line.strip()]

ws_prefix = f"workspaces/fp-0002-shpigovsky-v7"
files = []
for rel in rel_roots:
    git_path = f"{ws_prefix}/{rel}"
    p = ws / rel
    if rel == "src" or (p.exists() and p.is_dir()):
        for f in git_ls_tree(git_path):
            arc = f"{rel}/{f}" if not f.startswith(rel + "/") else f
            files.append((f"{git_path}/{f}" if not f.startswith(ws_prefix) else f, arc))
    else:
        files.append((git_path, rel))

manifest_lines = [
    "# BACKUP-MANIFEST — FP-0002 SERVICE SUBDIVISION BEFORE FINAL CORRECTIONS",
    "",
    f"- timestamp: {datetime.now(timezone.utc).isoformat()}",
    "- branch: mars/canonical-post-recovery",
    f"- HEAD: {head}",
    "- GROUP 1 commit: f3917bf6",
    "- GROUP 2 commit: 41777d4a",
    "- GROUP 3 commit: 57ac6d34",
    "- GROUP 4 commit: 7886629d",
    "- scope: three final corrections — approach→home-clinic-landscape; template garbage removal; dependencies border-bottom removal",
    "- exclusions: node_modules, dist, Figma, INCOMING, operator PNG, reviews screenshots, temp, git metadata, unrelated ORCA WIP",
    "",
    "## Included paths",
    "",
]
for _, arc in files:
    manifest_lines.append(f"- {arc}")

with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
    for git_path, arc in files:
        data = subprocess.check_output(["git", "show", f"HEAD:{git_path}"], cwd=repo)
        zf.writestr(arc, data)

restore = """# RESTORE-INSTRUCTIONS — FP-0002 BEFORE FINAL CORRECTIONS

1. Stop preview server if running.
2. Extract `FP-0002-V7-SERVICE-SUBDIVISION-BEFORE-FINAL-CORRECTIONS.zip` into `workspaces/fp-0002-shpigovsky-v7/` preserving relative paths.
3. Verify `src/pages/usluga-podrazdel-v1.html` still includes `service-subdivision-approach-v1.html`.
4. Run `npm run build` from workspace root using portable Node.
5. Confirm HEAD was `7886629d` at backup time (GROUP 4 baseline).
"""
(storage / "RESTORE-INSTRUCTIONS.md").write_text(restore, encoding="utf-8")
(storage / "BACKUP-MANIFEST.md").write_text("\n".join(manifest_lines) + "\n", encoding="utf-8")

sha = hashlib.sha256(zip_path.read_bytes()).hexdigest().upper()
(storage / "CHECKSUMS-SHA256.txt").write_text(f"{sha}  {zip_path.name}\n", encoding="utf-8")
print("zip", zip_path)
print("sha256", sha)
print("ok", zip_path.exists(), zipfile.is_zipfile(zip_path))
with zipfile.ZipFile(zip_path) as zf:
    names = zf.namelist()
    print("entries", len(names))
    print("has page", "src/pages/usluga-podrazdel-v1.html" in names)
