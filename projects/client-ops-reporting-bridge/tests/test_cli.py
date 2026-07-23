"""CLI and mutation-boundary tests."""

from __future__ import annotations

import io
import json
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest import mock

from client_ops_reporting_bridge.artifact_loader import snapshot_source_hashes
from client_ops_reporting_bridge.cli import (
    assert_safe_output_path,
    main,
)
from client_ops_reporting_bridge.constants import (
    EXIT_SOURCE_BLOCKED,
    EXIT_SUCCESS,
    EXIT_UNSAFE_OUTPUT_PATH,
)
from client_ops_reporting_bridge.errors import UnsafeOutputPathError

from support import PROJECT_ROOT, ExporterTestCase


def _run_cli(argv: list[str]) -> int:
    buf_out = io.StringIO()
    buf_err = io.StringIO()
    with redirect_stdout(buf_out), redirect_stderr(buf_err):
        return main(argv)


class TestCLI(ExporterTestCase):
    def test_validate_only_success(self) -> None:
        code = _run_cli(
            [
                "validate-only",
                "--fixture",
                str(self.fixture("fixture-ok")),
            ]
        )
        self.assertEqual(code, EXIT_SUCCESS)

    def test_validate_only_blocked(self) -> None:
        code = _run_cli(
            [
                "validate-only",
                "--fixture",
                str(self.fixture("fixture-blocked-missing-artifact")),
            ]
        )
        self.assertEqual(code, EXIT_SOURCE_BLOCKED)

    def test_build_envelope_success(self) -> None:
        out_dir = PROJECT_ROOT / "test-output"
        out_dir.mkdir(exist_ok=True)
        out = out_dir / "envelope-ok.json"
        if out.exists():
            out.unlink()
        code = _run_cli(
            [
                "build-envelope",
                "--fixture",
                str(self.fixture("fixture-ok")),
                "--output",
                str(out),
            ]
        )
        self.assertEqual(code, EXIT_SUCCESS)
        self.assertTrue(out.is_file())
        data = json.loads(out.read_text(encoding="utf-8"))
        self.assertEqual(data["schema_name"], "mars.client_ops.report")
        out.unlink()

    def test_output_path_rejection(self) -> None:
        with self.assertRaises(UnsafeOutputPathError):
            assert_safe_output_path(Path(r"C:\Windows\Temp\not-allowed-elsewhere.json"))
        code = _run_cli(
            [
                "build-envelope",
                "--fixture",
                str(self.fixture("fixture-ok")),
                "--output",
                r"C:\AI MARS\forbidden-envelope.json",
            ]
        )
        self.assertEqual(code, EXIT_UNSAFE_OUTPUT_PATH)

    def test_no_external_access(self) -> None:
        with mock.patch("urllib.request.urlopen") as urlopen:
            code = _run_cli(
                [
                    "validate-only",
                    "--fixture",
                    str(self.fixture("fixture-ok")),
                ]
            )
            self.assertEqual(code, EXIT_SUCCESS)
            urlopen.assert_not_called()


class TestMutationBoundary(ExporterTestCase):
    def test_fixture_hashes_unchanged(self) -> None:
        path = self.fixture("fixture-ok")
        before = snapshot_source_hashes(path)
        code = _run_cli(
            [
                "validate-only",
                "--fixture",
                str(path),
            ]
        )
        self.assertEqual(code, EXIT_SUCCESS)
        after = snapshot_source_hashes(path)
        self.assertEqual(before, after)

    def test_build_does_not_mutate_sources(self) -> None:
        path = self.fixture("fixture-attention-onboarding")
        before = snapshot_source_hashes(path)
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "env.json"
            code = _run_cli(
                [
                    "build-envelope",
                    "--fixture",
                    str(path),
                    "--output",
                    str(out),
                ]
            )
            self.assertEqual(code, EXIT_SUCCESS)
            self.assertTrue(out.is_file())
        after = snapshot_source_hashes(path)
        self.assertEqual(before, after)

    def test_no_storage_path_writes(self) -> None:
        # Refuse Storage root paths
        with self.assertRaises(UnsafeOutputPathError):
            assert_safe_output_path(
                Path(r"X:\AI MARS STORAGE\ocpilot\forbidden.json")
            )


if __name__ == "__main__":
    unittest.main()
