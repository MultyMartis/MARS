"""Create stable reference source backup after final commit."""
import hashlib
import subprocess
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ws = Path(r"C:\MARS Phenix\AI MARS\workspaces\fp-0002-shpigovsky-v7")
repo = ws.parents[1]
storage = Path(r"C:\MARS Phenix\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v7\reference-baselines")
storage.mkdir(parents=True, exist_ok=True)
zip_path = storage / "FP-0002-V7-SERVICE-SUBDIVISION-INTERNAL-PAGE-REFERENCE-01-SOURCE.zip"

commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo, text=True).strip()
commit_short = commit[:8]
branch = subprocess.check_output(["git", "branch", "--show-current"], cwd=repo, text=True).strip()

fig = Path(r"C:\MARS Phenix\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\INCOMING\01_DESIGN\Spig_v1.2.fig")
desk = Path(r"C:\MARS Phenix\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\INCOMING\01_DESIGN\26.06.2026\Услуга подраздел - десктоп.png")
mob = Path(r"C:\MARS Phenix\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\INCOMING\01_DESIGN\26.06.2026\Услуга подраздел - мобильная.png")

def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest().upper()

rel_roots = ["src", "package.json", "package-lock.json", "gulpfile.js", "foundation/FP-0002-V7-OPERATIONAL-STATUS.md"]
ws_prefix = "workspaces/fp-0002-shpigovsky-v7"

def git_ls_tree(prefix: str):
    out = subprocess.check_output(["git", "ls-tree", "-r", "--name-only", f"HEAD:{prefix}"], cwd=repo, text=True)
    return [line.strip() for line in out.splitlines() if line.strip()]

files = []
for rel in rel_roots:
    git_path = f"{ws_prefix}/{rel}"
    if rel == "src":
        for f in git_ls_tree(git_path):
            files.append((f"{git_path}/{f}", f"{rel}/{f}"))
    else:
        files.append((git_path, rel))

manifest = f"""# REFERENCE-MANIFEST — FP-0002 SERVICE SUBDIVISION INTERNAL PAGE

- project: FP-0002
- page: FP-0002-PG-003
- page type: SERVICE_SUBDIVISION_INTERNAL_PAGE
- source page: src/pages/usluga-podrazdel-v1.html
- branch: {branch}
- final commit: {commit}
- parent reference: fp-0002-v7-services-v2-internal-page-reference-01
- Figma file: {fig}
- Figma SHA-256: {sha(fig)}
- desktop PNG: {desk}
- desktop PNG SHA-256: {sha(desk)}
- mobile PNG: {mob}
- mobile PNG SHA-256: {sha(mob)}
- build command: npm run build
- build exit code: 0
- regression result: PASS (Home/Services V1/V2/GROUP 1-4)
- known operator override: lifebuoy decor removed
- stable tag: fp-0002-v7-service-subdivision-internal-page-reference-01
- timestamp: {datetime.now(timezone.utc).isoformat()}
- exclusions: node_modules, dist, reviews screenshots, Figma, INCOMING, operator PNG, temp, git metadata
"""

restore = f"""# RESTORE-INSTRUCTIONS — SERVICE SUBDIVISION REFERENCE 01

1. Extract ZIP into `workspaces/fp-0002-shpigovsky-v7/`.
2. Verify commit `{commit}` matches intended reference.
3. Run `npm run build` with portable Node.
4. Preview `dist/usluga-podrazdel-v1.html`.
"""

with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
    for git_path, arc in files:
        data = subprocess.check_output(["git", "show", f"HEAD:{git_path}"], cwd=repo)
        zf.writestr(arc, data)
    zf.writestr("REFERENCE-MANIFEST.md", manifest.encode("utf-8"))
    zf.writestr("RESTORE-INSTRUCTIONS.md", restore.encode("utf-8"))

zip_sha = hashlib.sha256(zip_path.read_bytes()).hexdigest().upper()
(storage / "CHECKSUMS-SHA256.txt").write_text(f"{zip_sha}  {zip_path.name}\n", encoding="utf-8")
(storage / "REFERENCE-MANIFEST.md").write_text(manifest, encoding="utf-8")
(storage / "RESTORE-INSTRUCTIONS.md").write_text(restore, encoding="utf-8")

print("commit", commit)
print("zip", zip_path)
print("sha256", zip_sha)
print("ok", zip_path.exists(), zipfile.is_zipfile(zip_path))
