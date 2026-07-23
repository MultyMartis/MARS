"""Tests for envelope security validation."""

from __future__ import annotations

import copy
import unittest

from client_ops_reporting_bridge.pipeline import process_fixture_dir
from client_ops_reporting_bridge.security_validator import (
    redact_for_diagnostics,
    validate_envelope_security,
)

from support import ExporterTestCase


def _base_envelope() -> dict:
    r = process_fixture_dir(
        ExporterTestCase().fixture("fixture-ok")  # type: ignore[misc]
    )
    assert r.envelope is not None
    return copy.deepcopy(r.envelope)


class TestSecurityValidator(ExporterTestCase):
    def setUp(self) -> None:
        r = process_fixture_dir(self.fixture("fixture-ok"))
        assert r.envelope is not None
        self.base = copy.deepcopy(r.envelope)

    def test_contains_secrets_true(self) -> None:
        env = copy.deepcopy(self.base)
        env["security"]["contains_secrets"] = True
        issues = validate_envelope_security(env)
        self.assertTrue(any("SECRET" in i.code or "contains" in i.message for i in issues) or issues)

    def test_redacted_false(self) -> None:
        env = copy.deepcopy(self.base)
        env["security"]["redacted"] = False
        issues = validate_envelope_security(env)
        self.assertTrue(any(i.code == "ENVELOPE_NOT_REDACTED" for i in issues))

    def test_windows_path(self) -> None:
        env = copy.deepcopy(self.base)
        env["action"]["text"] = r"see X:\Synthetic\path"
        issues = validate_envelope_security(env)
        self.assertTrue(any(i.code == "ENVELOPE_PATH_DETECTED" for i in issues))

    def test_unc_path(self) -> None:
        env = copy.deepcopy(self.base)
        env["action"]["text"] = r"see \\fileserver\share\report"
        issues = validate_envelope_security(env)
        self.assertTrue(any(i.code == "ENVELOPE_PATH_DETECTED" for i in issues))

    def test_embedded_credentials_uri(self) -> None:
        env = copy.deepcopy(self.base)
        env["action"]["text"] = "https://user:pass@example.invalid/x"
        issues = validate_envelope_security(env)
        self.assertTrue(
            any(i.code == "ENVELOPE_SECRET_MARKER_DETECTED" for i in issues)
        )

    def test_token_like_marker(self) -> None:
        env = copy.deepcopy(self.base)
        env["action"]["text"] = "api_key=SYNTHETIC_TEST_MARKER_NOT_REAL"
        issues = validate_envelope_security(env)
        self.assertTrue(
            any(i.code == "ENVELOPE_SECRET_MARKER_DETECTED" for i in issues)
        )

    def test_stack_trace(self) -> None:
        env = copy.deepcopy(self.base)
        env["action"]["text"] = (
            "Traceback (most recent call last):\n"
            '  File "x.py", line 1, in <module>\n'
        )
        issues = validate_envelope_security(env)
        self.assertTrue(any(i.code == "RAW_LOG_DETECTED" for i in issues))

    def test_suspicious_top_level_key(self) -> None:
        env = copy.deepcopy(self.base)
        env["telegram"] = {"chat_id": "synthetic"}
        issues = validate_envelope_security(env)
        self.assertTrue(issues)

    def test_diagnostics_redaction(self) -> None:
        raw = r"leak X:\Secrets\token and api_key=ABC"
        red = redact_for_diagnostics(raw)
        self.assertNotIn("X:\\Secrets", red)
        self.assertIn("REDACTED", red)

    def test_fixture_security_rejected(self) -> None:
        r = process_fixture_dir(self.fixture("fixture-security-secret-detected"))
        self.assertTrue(r.security_rejected)
        self.assertEqual(r.summary_code, "ENVELOPE_SECURITY_REJECTED")
        self.assertFalse(r.distributable)
        self.assertIsNone(r.envelope)


if __name__ == "__main__":
    unittest.main()
