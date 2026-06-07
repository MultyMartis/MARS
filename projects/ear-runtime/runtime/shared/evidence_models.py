"""EAR Runtime evidence package models — pure data structures only.

Standard library only. No filesystem access. No network. No hashing.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class EvidencePackage:
    """In-memory evidence package derived from a manifest and config."""

    source: str
    site_id: str
    connector: str
    manifest_entry_count: int
    manifest_excluded_count: int
    quality_level: str
    safe_unknown: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """Serialize evidence package to a plain dict."""
        return {
            "source": self.source,
            "site_id": self.site_id,
            "connector": self.connector,
            "manifest_entry_count": self.manifest_entry_count,
            "manifest_excluded_count": self.manifest_excluded_count,
            "quality_level": self.quality_level,
            "safe_unknown": list(self.safe_unknown),
            "notes": list(self.notes),
        }
