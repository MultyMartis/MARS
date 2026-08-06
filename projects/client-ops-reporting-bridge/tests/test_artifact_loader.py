"""Tests for artifact loading."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from support import ExporterTestCase, FIXTURES

from client_ops_reporting_bridge.artifact_loader import (
    load_artifacts,
    snapshot_source_hashes,
)


class TestArtifactLoader(ExporterTestCase):
    def test_required_files_ok(self) -> None:
        arts = load_artifacts(self.fixture("fixture-ok"))
        self.assertEqual(arts.missing, [])
        self.assertEqual(arts.malformed, [])
        self.assertIsInstance(arts.monitor_classification, dict)
        self.assertIsInstance(arts.changed_summary, dict)
        self.assertIsInstance(arts.run_summary, dict)

    def test_missing_file(self) -> None:
        arts = load_artifacts(self.fixture("fixture-blocked-missing-artifact"))
        self.assertIn("changed-summary.json", arts.missing)

    def test_malformed_json(self) -> None:
        arts = load_artifacts(self.fixture("fixture-blocked-malformed-json"))
        self.assertIn("monitor-classification.json", arts.malformed)

    def test_utf8_handling(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "monitor-classification.json").write_text(
                json.dumps(
                    {
                        "classification": "NO_ACTION_REQUIRED",
                        "onboarding_needs_count": 0,
                        "note": "ЗПМ · проверка",
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            (root / "changed-summary.json").write_text(
                json.dumps(
                    {
                        "baseline_url_count": 1,
                        "current_url_count": 1,
                        "added_count": 0,
                        "removed_count": 0,
                        "onboarding_needs_count": 0,
                    }
                ),
                encoding="utf-8",
            )
            (root / "run-summary.json").write_text(
                json.dumps(
                    {
                        "run_id": "utf8-run",
                        "classification": "NO_ACTION_REQUIRED",
                        "finished_at": "2026-07-23T09:30:00Z",
                        "exit_code": 0,
                    }
                ),
                encoding="utf-8",
            )
            arts = load_artifacts(root)
            self.assertEqual(arts.missing, [])
            self.assertEqual(arts.malformed, [])
            self.assertIn("ЗПМ", arts.monitor_classification["note"])

    def test_snapshot_hashes_stable(self) -> None:
        path = self.fixture("fixture-ok")
        h1 = snapshot_source_hashes(path)
        h2 = snapshot_source_hashes(path)
        self.assertEqual(h1, h2)
        self.assertIn("monitor-classification.json", h1)


if __name__ == "__main__":
    unittest.main()
