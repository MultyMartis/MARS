"""Tests for source validation helpers."""

from __future__ import annotations

import unittest

from client_ops_reporting_bridge.source_validation import (
    parse_timestamp,
    require_non_negative_int,
)


class TestSourceValidation(unittest.TestCase):
    def test_integer_ok(self) -> None:
        value, issues = require_non_negative_int(
            4, field="x", artifact="a.json"
        )
        self.assertEqual(value, 4)
        self.assertEqual(issues, [])

    def test_explicit_zero_ok(self) -> None:
        value, issues = require_non_negative_int(
            0, field="x", artifact="a.json"
        )
        self.assertEqual(value, 0)
        self.assertEqual(issues, [])

    def test_bool_rejected(self) -> None:
        value, issues = require_non_negative_int(
            True, field="x", artifact="a.json"
        )
        self.assertIsNone(value)
        self.assertTrue(issues)

    def test_negative_rejected(self) -> None:
        value, issues = require_non_negative_int(
            -1, field="x", artifact="a.json"
        )
        self.assertIsNone(value)
        self.assertEqual(issues[0].code, "SOURCE_METRIC_NEGATIVE")

    def test_timestamp_parse_z(self) -> None:
        dt, issue = parse_timestamp("2026-07-23T09:30:00Z")
        self.assertIsNone(issue)
        assert dt is not None
        self.assertEqual(dt.tzinfo is not None, True)
        self.assertEqual(dt.hour, 9)

    def test_timestamp_invalid(self) -> None:
        dt, issue = parse_timestamp("not-a-time")
        self.assertIsNone(dt)
        assert issue is not None
        self.assertEqual(issue.code, "OBSERVED_AT_UNPARSEABLE")


if __name__ == "__main__":
    unittest.main()
