"""Sequential dispatch guard — fail closed on concurrency > 1."""

from __future__ import annotations

import threading
from typing import Optional

from .producer_constants import DEFAULT_CONCURRENCY


class SequentialDispatchError(RuntimeError):
    """Raised when parallel/concurrent dispatch is requested or detected."""


class SequentialDispatchGuard:
    """Single-process sequential dispatch lock.

    Not a distributed lock. Enforces in-process concurrency=1 only.
    """

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._active = 0

    def assert_concurrency(self, concurrency: int) -> None:
        if concurrency != DEFAULT_CONCURRENCY:
            raise SequentialDispatchError(
                f"concurrency={concurrency} rejected; sequential only (concurrency=1)"
            )

    def acquire(self, *, concurrency: int = 1) -> None:
        self.assert_concurrency(concurrency)
        if not self._lock.acquire(blocking=False):
            raise SequentialDispatchError(
                "parallel dispatch rejected; another dispatch is in progress"
            )
        self._active += 1

    def release(self) -> None:
        if self._active > 0:
            self._active -= 1
        try:
            self._lock.release()
        except RuntimeError:
            pass

    @property
    def active(self) -> int:
        return self._active


# Process-wide default guard for the producer CLI / pipeline.
_DEFAULT_GUARD: Optional[SequentialDispatchGuard] = None


def get_default_guard() -> SequentialDispatchGuard:
    global _DEFAULT_GUARD
    if _DEFAULT_GUARD is None:
        _DEFAULT_GUARD = SequentialDispatchGuard()
    return _DEFAULT_GUARD


def reset_default_guard_for_tests() -> SequentialDispatchGuard:
    """Test helper — replace the process-wide guard."""
    global _DEFAULT_GUARD
    _DEFAULT_GUARD = SequentialDispatchGuard()
    return _DEFAULT_GUARD
