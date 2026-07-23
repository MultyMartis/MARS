"""Tests for SIMPLE offline formatter."""

from __future__ import annotations

import unittest

from client_ops_reporting_bridge.pipeline import process_fixture_dir
from client_ops_reporting_bridge.simple_formatter import format_simple

from support import ExporterTestCase


class TestSimpleFormatter(ExporterTestCase):
    def test_ok_exact(self) -> None:
        r = process_fixture_dir(self.fixture("fixture-ok"))
        self.assertTrue(r.distributable)
        assert r.simple_text is not None
        expected = (self.fixture("fixture-ok") / "expected-simple.txt").read_text(
            encoding="utf-8"
        )
        self.assertEqual(r.simple_text, expected)
        self.assertIn("ЗПМ · OK", r.simple_text)
        self.assertIn("Action: none", r.simple_text)

    def test_attention_exact(self) -> None:
        r = process_fixture_dir(self.fixture("fixture-attention-onboarding"))
        assert r.simple_text is not None
        self.assertIn("ЗПМ · ATTENTION", r.simple_text)
        self.assertIn("Baseline: 1737", r.simple_text)
        self.assertIn("Current: 1817", r.simple_text)
        self.assertIn("Added: 80", r.simple_text)
        self.assertIn("Onboarding needed: 4", r.simple_text)
        self.assertIn("Action: проверить новые ветки каталога", r.simple_text)
        self.assertIn("Run: 2026-07-23 12:30", r.simple_text)

    def test_failed(self) -> None:
        r = process_fixture_dir(self.fixture("fixture-failed-execution"))
        assert r.simple_text is not None
        self.assertIn("ЗПМ · FAILED", r.simple_text)

    def test_blocked_conflict(self) -> None:
        r = process_fixture_dir(
            self.fixture("fixture-blocked-classification-conflict")
        )
        assert r.simple_text is not None
        self.assertIn("ЗПМ · BLOCKED", r.simple_text)
        self.assertNotIn(":\\", r.simple_text)
        self.assertNotIn("Traceback", r.simple_text)

    def test_timezone_conversion(self) -> None:
        r = process_fixture_dir(self.fixture("fixture-ok"))
        assert r.envelope is not None
        text = format_simple(r.envelope, tz_name="Europe/Moscow")
        self.assertIn("Run: 2026-07-20 18:05", text)


if __name__ == "__main__":
    unittest.main()
