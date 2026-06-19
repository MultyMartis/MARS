import hashlib
import json
import zipfile
from datetime import datetime, timezone
from pathlib import Path

SOURCE = Path(r"C:\AI MARS\projects\wpilot\plugin\metacode-wpilot")
OUT_DIR = Path(r"C:\AI MARS STORAGE\wpilot\deploy-packages")
ZIP_NAME = "metacode-wpilot-v0.3.0-rc3.zip"
ROOT = "metacode-wpilot/"

EXCLUDE_DIRS = {".git", "__pycache__"}
EXCLUDE_SUFFIXES = {".bak", ".tmp"}


def should_include(path: Path) -> bool:
    parts = set(path.parts)
    if parts & EXCLUDE_DIRS:
        return False
    if path.suffix.lower() in EXCLUDE_SUFFIXES:
        return False
    name = path.name.lower()
    if "token" in name and name.endswith((".txt", ".json", ".env")):
        return False
    return True


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    zip_path = OUT_DIR / ZIP_NAME

    files = []
    for path in sorted(SOURCE.rglob("*")):
        if not path.is_file() or not should_include(path.relative_to(SOURCE)):
            continue
        rel = path.relative_to(SOURCE).as_posix()
        files.append((path, ROOT + rel))

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for src, arc in files:
            zf.write(src, arc)

    digest = hashlib.sha256(zip_path.read_bytes()).hexdigest()
    inventory = {
        "package": ZIP_NAME,
        "built_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
        "baseline": "Variant B (checkpoint 8c67478 + UX-01 + UX-02)",
        "source": str(SOURCE),
        "zip_path": str(zip_path),
        "sha256": digest,
        "size_bytes": zip_path.stat().st_size,
        "root_folder": ROOT,
        "file_count": len(files),
        "bootstrap_present": any(a.endswith("metacode-wpilot.php") for _, a in files),
        "root_folder_correct": all(a.startswith(ROOT) and a.count("/") >= 1 for _, a in files),
        "mo_included": any(a.endswith(".mo") for _, a in files),
        "files": [arc for _, arc in sorted(files, key=lambda x: x[1])],
    }

    inv_path = OUT_DIR / "metacode-wpilot-v0.3.0-rc3.inventory.json"
    inv_path.write_text(json.dumps(inventory, indent=2), encoding="utf-8")

    print(json.dumps(inventory, indent=2))


if __name__ == "__main__":
    main()
