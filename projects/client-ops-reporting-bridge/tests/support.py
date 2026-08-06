"""Shared helpers for Phase 1A offline exporter tests (absolute imports)."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parents[1]
_SRC = _PROJECT_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

PROJECT_ROOT = _PROJECT_ROOT
FIXTURES = PROJECT_ROOT / "fixtures"


def fixture_path(name: str) -> Path:
    return FIXTURES / name


class ExporterTestCase(unittest.TestCase):
    """Base test case with fixture helpers."""

    def fixture(self, name: str) -> Path:
        path = fixture_path(name)
        self.assertTrue(path.is_dir(), f"missing fixture {name}")
        return path
