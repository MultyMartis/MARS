"""EAR Runtime remote listing models — pure data structures only.

Standard library only. No filesystem access. No network. No traversal.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class ListingEntry:
    """Single remote path entry in a listing result."""

    path: str
    entry_type: str
    size: int | None
    modified: str | None
    excluded: bool


@dataclass
class ListingResult:
    """Structured result of a remote path listing (mock or live)."""

    source: str
    entry_count: int
    excluded_count: int
    entries: list[ListingEntry] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """Serialize listing result to a plain dict."""
        return {
            "source": self.source,
            "entry_count": self.entry_count,
            "excluded_count": self.excluded_count,
            "entries": [
                {
                    "path": entry.path,
                    "entry_type": entry.entry_type,
                    "size": entry.size,
                    "modified": entry.modified,
                    "excluded": entry.excluded,
                }
                for entry in self.entries
            ],
        }
