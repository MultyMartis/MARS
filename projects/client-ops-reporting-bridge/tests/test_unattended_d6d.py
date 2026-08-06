"""Phase 1B-D6D — offline Python binding tests (language boundary)."""

from __future__ import annotations

import unittest

from client_ops_reporting_bridge.unattended_d6d import (
    D6D_AUTHORITATIVE_ARTIFACTS,
    D6D_COMPLETION_MARKER,
    D6D_LANGUAGE_BOUNDARY,
    D6D_UNATTENDED_PRODUCTION_ENABLED,
    assert_freshness_binding,
    map_monitor_classification_to_source_status,
    producer_input_contract_keys,
    producer_output_contract_keys,
)


class TestD6DLanguageBoundary(unittest.TestCase):
    def test_production_disabled(self) -> None:
        self.assertFalse(D6D_UNATTENDED_PRODUCTION_ENABLED)

    def test_status_mapping(self) -> None:
        self.assertEqual(map_monitor_classification_to_source_status("NO_ACTION_REQUIRED"), "OK")
        self.assertEqual(map_monitor_classification_to_source_status("ONBOARDING_REQUIRED"), "ATTENTION")
        self.assertEqual(map_monitor_classification_to_source_status("HYGIENE_REVIEW_REQUIRED"), "ATTENTION")
        self.assertEqual(map_monitor_classification_to_source_status("FAILURE_REVIEW_REQUIRED"), "FAILED")
        self.assertEqual(map_monitor_classification_to_source_status("NOPE"), "BLOCKED")

    def test_authoritative_artifacts(self) -> None:
        self.assertIn("run-summary.json", D6D_AUTHORITATIVE_ARTIFACTS)
        self.assertEqual(D6D_COMPLETION_MARKER, "run-complete.marker")

    def test_freshness_binding(self) -> None:
        info = assert_freshness_binding()
        self.assertEqual(info["stale_after_seconds"], 93600)

    def test_contracts(self) -> None:
        self.assertIn("kill_switch_mode", producer_input_contract_keys())
        self.assertIn("exit_class", producer_output_contract_keys())
        self.assertIn("Python", D6D_LANGUAGE_BOUNDARY)
        self.assertIn("Node", D6D_LANGUAGE_BOUNDARY)


if __name__ == "__main__":
    unittest.main()
