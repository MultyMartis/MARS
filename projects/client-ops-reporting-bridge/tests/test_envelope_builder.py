"""Tests for envelope builder."""

from __future__ import annotations

import unittest

from client_ops_reporting_bridge.pipeline import process_fixture_dir

from support import ExporterTestCase


class TestEnvelopeBuilder(ExporterTestCase):
    def test_required_shape_ok(self) -> None:
        r = process_fixture_dir(self.fixture("fixture-attention-onboarding"))
        self.assertTrue(r.distributable)
        env = r.envelope
        assert env is not None
        for key in (
            "schema_name",
            "schema_version",
            "event_id",
            "event_type",
            "generated_at",
            "observed_at",
            "environment",
            "site",
            "producer",
            "run",
            "action",
            "metrics",
            "freshness",
            "security",
        ):
            self.assertIn(key, env)
        self.assertEqual(env["schema_name"], "mars.client_ops.report")
        self.assertEqual(env["schema_version"], "1.0")

    def test_no_routing_delivery_ai(self) -> None:
        r = process_fixture_dir(self.fixture("fixture-ok"))
        env = r.envelope
        assert env is not None
        for banned in (
            "delivery",
            "ai",
            "routing",
            "telegram",
            "chat_id",
            "bot_token",
            "webhook",
        ):
            self.assertNotIn(banned, env)

    def test_no_paths_or_secrets_in_action(self) -> None:
        r = process_fixture_dir(self.fixture("fixture-attention-onboarding"))
        env = r.envelope
        assert env is not None
        text = env["action"]["text"]
        self.assertNotIn(":\\", text)
        self.assertNotIn("\\\\", text)
        self.assertNotIn("token", text.lower())

    def test_security_flags(self) -> None:
        r = process_fixture_dir(self.fixture("fixture-ok"))
        env = r.envelope
        assert env is not None
        self.assertIs(env["security"]["contains_secrets"], False)
        self.assertIs(env["security"]["redacted"], True)

    def test_blocked_conflict_envelope(self) -> None:
        r = process_fixture_dir(
            self.fixture("fixture-blocked-classification-conflict")
        )
        self.assertTrue(r.distributable)
        assert r.envelope is not None
        self.assertEqual(r.envelope["run"]["normalized_status"], "BLOCKED")
        self.assertEqual(r.envelope["metrics"]["added_urls"], 80)
        self.assertEqual(r.envelope["metrics"]["onboarding_needed_count"], 4)

    def test_missing_baseline_no_distributable(self) -> None:
        r = process_fixture_dir(
            self.fixture("fixture-blocked-missing-baseline")
        )
        self.assertFalse(r.distributable)
        self.assertIsNone(r.envelope)


if __name__ == "__main__":
    unittest.main()
