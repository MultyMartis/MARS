"""EAR Runtime snapshot package models — pure data structures only.

Standard library only. No filesystem access. No network. No hashing.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class SnapshotPackage:
    """In-memory snapshot package derived from an evidence package."""

    snapshot_id: str
    site_id: str
    source: str
    connector: str
    quality_level: str
    entry_count: int
    excluded_count: int
    created_from: str
    safe_unknown: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """Serialize snapshot package to a plain dict."""
        return {
            "snapshot_id": self.snapshot_id,
            "site_id": self.site_id,
            "source": self.source,
            "connector": self.connector,
            "quality_level": self.quality_level,
            "entry_count": self.entry_count,
            "excluded_count": self.excluded_count,
            "created_from": self.created_from,
            "safe_unknown": list(self.safe_unknown),
            "notes": list(self.notes),
        }
