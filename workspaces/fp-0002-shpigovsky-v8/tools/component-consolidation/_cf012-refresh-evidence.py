#!/usr/bin/env python3
"""Re-capture CF-011 before + CF-012 after evidence in one run."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / "tools" / "component-consolidation"


def run_old_before(port: int = 4198) -> None:
    subprocess.check_call([sys.executable, str(TOOL / "_cf012-old-ref-compare.py")])
    # old-ref compare restores new state; run dedicated before capture on CF-011 next
    subprocess.check_call(
        [sys.executable, str(TOOL / "_cf012-capture-phase.py"), "before", str(port)],
    )


def run_after(port: int = 4199) -> None:
    subprocess.check_call([sys.executable, str(TOOL / "_cf012-browser-qa.py"), "after", str(port)])


if __name__ == "__main__":
    run_old_before()
    run_after()
