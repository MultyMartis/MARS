"""FP-0002 V6 — pre-modals operator-stable backup, checksums, restore test."""
from __future__ import annotations

import hashlib
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RELEASE_ID = "FP-0002-V6-PRE-MODALS-OPERATOR-STABLE-01"
RELEASE_DIR = ROOT / "releases" / RELEASE_ID
STORAGE_DIR = Path(r"C:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v6\releases")
ZIP_PATH = STORAGE_DIR / f"{RELEASE_ID}-SOURCE.zip"

INCLUDE_TOP = (
    "gulpfile.js",
    "package.json",
    "package-lock.json",
)
INCLUDE_DOCS = (
    "BACKUP-MANIFEST.md",
    "CHECKSUMS-SHA256.txt",
    "RESTORE-INSTRUCTIONS.md",
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def collect_files() -> list[Path]:
    files: list[Path] = []
    src_root = ROOT / "src"
    for path in sorted(src_root.rglob("*")):
        if path.is_file():
            files.append(path)
    for name in INCLUDE_TOP:
        files.append(ROOT / name)
    for name in INCLUDE_DOCS:
        files.append(RELEASE_DIR / name)
    return files


def write_checksums(files: list[Path]) -> str:
    lines: list[str] = []
    for path in files:
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path.name
        lines.append(f"{sha256_file(path)}  {rel.as_posix()}")
    content = "\n".join(lines) + "\n"
    checksum_path = RELEASE_DIR / "CHECKSUMS-SHA256.txt"
    checksum_path.write_text(content, encoding="utf-8")
    return sha256_file(checksum_path)


def create_zip(files: list[Path]) -> str:
    STORAGE_DIR.mkdir(parents=True, exist_ok=True)
    if ZIP_PATH.exists():
        ZIP_PATH.unlink()

    with zipfile.ZipFile(ZIP_PATH, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            if not path.is_file():
                continue
            if path.is_relative_to(ROOT):
                arcname = path.relative_to(ROOT).as_posix()
            else:
                arcname = path.name
            archive.write(path, arcname)

    return sha256_file(ZIP_PATH)


def restore_test() -> tuple[bool, str]:
    # Must mirror workspaces/fp-0002-shpigovsky-v6 depth so gulpfile ../../shared -> MARS/shared.
    temp_root = ROOT.parent / "fp-0002-pre-modals-restore-test"
    if temp_root.exists():
        shutil.rmtree(temp_root, ignore_errors=True)
    temp_root.mkdir(parents=True, exist_ok=True)
    try:
        with zipfile.ZipFile(ZIP_PATH, "r") as archive:
            archive.extractall(temp_root)

        subprocess.check_call(["npm", "ci"], cwd=temp_root, shell=True)
        subprocess.check_call(["npm", "run", "build"], cwd=temp_root, shell=True)

        dist_index = temp_root / "dist" / "index.html"
        if not dist_index.is_file():
            return False, "dist/index.html missing"

        html = dist_index.read_text(encoding="utf-8")
        checks = [
            ("home-final-form" in html, "final form"),
            ("swiper-bundle.min.js" in html, "swiper vendor"),
            ("fancybox.umd.js" in html, "fancybox vendor"),
            ("data-modal" not in html, "modal markup absent"),
            ("data-modal-open" not in html, "modal triggers absent"),
        ]
        failed = [name for ok, name in checks if not ok]
        if failed:
            return False, "restore checks failed: " + ", ".join(failed)

        main_js = (temp_root / "src" / "js" / "main.js").read_text(encoding="utf-8")
        if "data-modal" in main_js or "data-modal-open" in main_js:
            return False, "modal initializers present in main.js"

        return True, "PASS"
    finally:
        if temp_root.exists():
            shutil.rmtree(temp_root, ignore_errors=True)


def main() -> int:
    if not RELEASE_DIR.is_dir():
        print(f"MISSING_RELEASE_DIR: {RELEASE_DIR}")
        return 2

    files = collect_files()
    checksum_file_hash = write_checksums(files)
    zip_hash = create_zip(files)
    ok, message = restore_test()

    print(f"RELEASE_ID={RELEASE_ID}")
    print(f"ZIP_PATH={ZIP_PATH}")
    print(f"ZIP_SHA256={zip_hash}")
    print(f"CHECKSUMS_SHA256={checksum_file_hash}")
    print(f"RESTORE_TEST={message}")
    return 0 if ok else 3


if __name__ == "__main__":
    raise SystemExit(main())
