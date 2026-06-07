"""EAR Runtime manifest models — pure data structures only.



Standard library only. No filesystem access. No network. No hashing.

"""



from __future__ import annotations



from dataclasses import dataclass, field

from typing import Any





@dataclass(frozen=True)

class ManifestEntry:

    """Single path entry in a manifest."""



    path: str

    entry_type: str

    excluded: bool





@dataclass

class Manifest:

    """Structured manifest derived from a listing result."""



    source: str

    entry_count: int

    excluded_count: int

    entries: list[ManifestEntry] = field(default_factory=list)



    def to_dict(self) -> dict[str, Any]:

        """Serialize manifest to a plain dict."""

        return {

            "source": self.source,

            "entry_count": self.entry_count,

            "excluded_count": self.excluded_count,

            "entries": [

                {

                    "path": entry.path,

                    "entry_type": entry.entry_type,

                    "excluded": entry.excluded,

                }

                for entry in self.entries

            ],

        }

