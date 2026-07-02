#!/usr/bin/env python3
"""FP-0002 WPilot DEV-runtime reconciliation — read-only inventory and comparison."""
from __future__ import annotations

import hashlib
import json
import ssl
import sys
import urllib.error
import urllib.request
import zipfile
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(r"X:\AI MARS")
STORAGE = Path(r"X:\AI MARS STORAGE")
LOCALHOST = Path(r"X:\MARS-Localhost")
OUT_DIR = REPO / "projects" / "wpilot" / "manifests"
EVIDENCE_DIR = STORAGE / "wpilot" / "evidence" / "dev.gktriumph.ru" / "dev-runtime-reconciliation-2026-07-02"

BRAIN = REPO / "projects" / "wpilot" / "plugin" / "metacode-wpilot"
LOCAL = (
    LOCALHOST
    / "sites"
    / "wordpress"
    / "projects"
    / "shpigovsky"
    / "wp-content"
    / "plugins"
    / "metacode-wpilot"
)
OLD_ZIP = STORAGE / "wpilot" / "deploy-packages" / "metacode-wpilot-v0.3.0.zip"
RC5_ZIP = STORAGE / "wpilot" / "deploy-packages" / "metacode-wpilot-v0.3.0-rc5.zip"

DEV_BASE = "https://dev.gktriumph.ru/wp-content/plugins/metacode-wpilot"
DEV_FINGERPRINT_FILES = [
    "languages/metacode-wpilot-ru_RU.mo",
    "languages/metacode-wpilot-ru_RU.po",
    "admin/class-wpilot-admin-ui-model.php",
    "admin/class-wpilot-admin-page.php",
    "includes/class-wpilot-connection-tracker.php",
    "includes/class-wpilot-auth.php",
    "metacode-wpilot.php",
]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def dir_manifest(root: Path) -> dict:
    files: dict[str, dict] = {}
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(root).as_posix()
        data = path.read_bytes()
        files[rel] = {"size": len(data), "sha256": sha256_bytes(data)}
    aggregate = sha256_bytes(
        "\n".join(f"{k}|{files[k]['sha256']}" for k in sorted(files)).encode("utf-8")
    )
    dirs = len({p.parent for p in root.rglob("*") if p.is_dir()})
    return {
        "files": files,
        "file_count": len(files),
        "directory_count": dirs,
        "aggregate_sha256": aggregate,
    }


def zip_manifest(zpath: Path) -> dict:
    files: dict[str, dict] = {}
    with zipfile.ZipFile(zpath) as zf:
        for name in sorted(zf.namelist()):
            if name.endswith("/"):
                continue
            rel = name.split("/", 1)[1] if "/" in name else name
            data = zf.read(name)
            files[rel] = {"size": len(data), "sha256": sha256_bytes(data)}
    aggregate = sha256_bytes(
        "\n".join(f"{k}|{files[k]['sha256']}" for k in sorted(files)).encode("utf-8")
    )
    return {
        "files": files,
        "file_count": len(files),
        "directory_count": len({str(Path(k).parent) for k in files if "/" in k}),
        "aggregate_sha256": aggregate,
        "package_sha256": sha256_bytes(zpath.read_bytes()),
    }


def fetch_dev_file(rel: str) -> dict:
    url = f"{DEV_BASE}/{rel}"
    req = urllib.request.Request(url, method="GET", headers={"User-Agent": "MARS-WPilot-Reconcile/1.0"})
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
            data = resp.read()
            return {
                "relative_path": rel,
                "url": url,
                "http_status": resp.status,
                "size": len(data),
                "sha256": sha256_bytes(data) if data else "",
                "accessible": len(data) > 0,
            }
    except urllib.error.HTTPError as exc:
        return {
            "relative_path": rel,
            "url": url,
            "http_status": exc.code,
            "size": 0,
            "sha256": "",
            "accessible": False,
            "error": str(exc),
        }
    except Exception as exc:  # noqa: BLE001
        return {
            "relative_path": rel,
            "url": url,
            "http_status": 0,
            "size": 0,
            "sha256": "",
            "accessible": False,
            "error": str(exc),
        }


def classify_file(rel: str, surfaces: dict[str, dict]) -> str:
    present = {name: rel in data["files"] for name, data in surfaces.items()}
    hashes = {
        name: data["files"][rel]["sha256"]
        for name, data in surfaces.items()
        if rel in data["files"]
    }

    if present.get("dev_remote") and all(
        hashes.get("dev_remote") == hashes.get(n)
        for n in ("brain", "rc5_zip")
        if present.get(n)
    ):
        if present.get("old_zip") and rel not in surfaces["old_zip"]["files"]:
            return "MISSING_FROM_OLD_PACKAGE"
        if present.get("local") and rel not in surfaces["local"]["files"]:
            return "OLDER_THAN_DEV"
        return "IDENTICAL_TO_DEV"

    if present.get("brain") and present.get("rc5_zip"):
        if hashes.get("brain") == hashes.get("rc5_zip"):
            if not present.get("dev_remote"):
                return "SAFE_UNKNOWN"
            if hashes.get("dev_remote") == hashes.get("brain"):
                return "IDENTICAL_TO_DEV"

    if present.get("brain") and not present.get("dev_remote"):
        if present.get("local") and rel in surfaces["local"]["files"]:
            if hashes.get("brain") != hashes.get("local"):
                return "POST_DEV_BRAIN_DELTA" if present.get("rc5_zip") else "SAFE_UNKNOWN"
        return "SAFE_UNKNOWN"

    if present.get("dev_remote") and not present.get("brain"):
        return "DEV_ONLY_UNTRACKED"

    if present.get("local") and not present.get("brain") and not present.get("dev_remote"):
        return "LOCAL_ONLY"

    if present.get("old_zip") and not present.get("brain"):
        return "OLDER_THAN_DEV"

    if rel.endswith(".mo") or rel.endswith(".po"):
        return "SAFE_UNKNOWN"

    return "SAFE_UNKNOWN"


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)

    surfaces = {
        "brain": dir_manifest(BRAIN),
        "local": dir_manifest(LOCAL),
        "old_zip": zip_manifest(OLD_ZIP),
        "rc5_zip": zip_manifest(RC5_ZIP),
    }

    dev_remote_files: dict[str, dict] = {}
    dev_fetch_log = []
    for rel in DEV_FINGERPRINT_FILES:
        entry = fetch_dev_file(rel)
        dev_fetch_log.append(entry)
        if entry.get("accessible") and entry.get("sha256"):
            dev_remote_files[rel] = {
                "size": entry["size"],
                "sha256": entry["sha256"],
            }

    all_dev_paths = set()
    for rel in surfaces["brain"]["files"]:
        fetched = fetch_dev_file(rel)
        if fetched.get("accessible") and fetched.get("sha256"):
            all_dev_paths.add(rel)
            dev_remote_files[rel] = {
                "size": fetched["size"],
                "sha256": fetched["sha256"],
            }

    surfaces["dev_remote"] = {
        "files": dev_remote_files,
        "file_count": len(dev_remote_files),
        "directory_count": len({str(Path(k).parent) for k in dev_remote_files if "/" in k}),
        "aggregate_sha256": sha256_bytes(
            "\n".join(
                f"{k}|{dev_remote_files[k]['sha256']}" for k in sorted(dev_remote_files)
            ).encode("utf-8")
        )
        if dev_remote_files
        else "",
    }

    all_rels = sorted(
        set().union(*(set(s["files"]) for s in surfaces.values()))
    )

    matrix = []
    counts: dict[str, int] = {}
    for rel in all_rels:
        cls = classify_file(rel, surfaces)
        counts[cls] = counts.get(cls, 0) + 1
        row = {
            "relative_file": rel,
            "dev": rel in surfaces["dev_remote"]["files"],
            "brain": rel in surfaces["brain"]["files"],
            "old_zip": rel in surfaces["old_zip"]["files"],
            "shpigovsky": rel in surfaces["local"]["files"],
            "classification": cls,
        }
        if rel in surfaces["dev_remote"]["files"] and rel in surfaces["brain"]["files"]:
            row["dev_brain_match"] = (
                surfaces["dev_remote"]["files"][rel]["sha256"]
                == surfaces["brain"]["files"][rel]["sha256"]
            )
        matrix.append(row)

    dev_brain_matches = sum(
        1
        for rel in surfaces["brain"]["files"]
        if rel in surfaces["dev_remote"]["files"]
        and surfaces["dev_remote"]["files"][rel]["sha256"]
        == surfaces["brain"]["files"][rel]["sha256"]
    )
    dev_brain_total = len(surfaces["brain"]["files"])
    dev_full_coverage = dev_brain_matches == dev_brain_total and dev_brain_total > 0

    report = {
        "generated_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "task": "FP-0002-WPILOT-DEV-RUNTIME-RECONCILIATION",
        "surfaces": {
            name: {
                "path": str(
                    {
                        "brain": BRAIN,
                        "local": LOCAL,
                        "old_zip": OLD_ZIP,
                        "rc5_zip": RC5_ZIP,
                        "dev_remote": DEV_BASE,
                    }[name]
                ),
                "file_count": data["file_count"],
                "directory_count": data["directory_count"],
                "aggregate_sha256": data["aggregate_sha256"],
                **(
                    {"package_sha256": data["package_sha256"]}
                    if "package_sha256" in data
                    else {}
                ),
            }
            for name, data in surfaces.items()
        },
        "comparisons": {
            "brain_equals_rc5_zip": surfaces["brain"]["aggregate_sha256"]
            == surfaces["rc5_zip"]["aggregate_sha256"],
            "local_equals_old_zip": surfaces["local"]["aggregate_sha256"]
            == surfaces["old_zip"]["aggregate_sha256"],
            "brain_equals_local": surfaces["brain"]["aggregate_sha256"]
            == surfaces["local"]["aggregate_sha256"],
            "dev_remote_brain_file_matches": dev_brain_matches,
            "dev_remote_brain_file_total": dev_brain_total,
            "dev_remote_full_brain_coverage": dev_full_coverage,
        },
        "classification_counts": counts,
        "dev_fetch_probe": dev_fetch_log,
        "file_matrix": matrix,
        "version_identity": {
            "advertised_version_all_surfaces": "0.3.0",
            "materially_different_builds": surfaces["brain"]["aggregate_sha256"]
            != surfaces["old_zip"]["aggregate_sha256"],
            "collision": "VERSION_IDENTITY_COLLISION",
        },
    }

    manifest_path = OUT_DIR / "wpilot-dev-runtime-reconciliation-2026-07-02.json"
    remote_manifest_path = EVIDENCE_DIR / "dev-remote-manifest-redacted.json"
    matrix_path = OUT_DIR / "wpilot-four-surface-matrix-2026-07-02.json"

    manifest_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    remote_manifest_path.write_text(
        json.dumps(
            {
                "site": "https://dev.gktriumph.ru",
                "inventory_method": "read-only HTTPS GET wp-content/plugins/metacode-wpilot/*",
                "exact_file_authority_available": dev_full_coverage,
                "partial_file_count": surfaces["dev_remote"]["file_count"],
                "aggregate_sha256_partial": surfaces["dev_remote"]["aggregate_sha256"],
                "files": {
                    k: {"size": v["size"], "sha256": v["sha256"]}
                    for k, v in dev_remote_files.items()
                },
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    matrix_path.write_text(json.dumps(matrix, indent=2), encoding="utf-8")

    print(json.dumps(report["comparisons"], indent=2))
    print("classification_counts", json.dumps(counts))
    print("dev_remote_files", surfaces["dev_remote"]["file_count"])
    print("manifest", manifest_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
