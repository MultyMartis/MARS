"""EAR Runtime listing validator — structural checks on ListingResult only.

Standard library only. No runtime execution. No remote access.
"""

from __future__ import annotations

from typing import Any

from shared.listing_models import ListingResult

ALLOWED_ENTRY_TYPES: frozenset[str] = frozenset({"file", "directory"})


def validate_listing_result(result: ListingResult) -> dict[str, Any]:
    """Validate a ListingResult object. Returns structured valid/errors result."""
    errors: list[str] = []

    if not isinstance(result.source, str) or not result.source.strip():
        errors.append("source must be a non-empty string")

    actual_count = len(result.entries)
    if result.entry_count != actual_count:
        errors.append(
            f"entry_count ({result.entry_count}) does not match "
            f"entries length ({actual_count})"
        )

    actual_excluded = sum(1 for entry in result.entries if entry.excluded)
    if result.excluded_count != actual_excluded:
        errors.append(
            f"excluded_count ({result.excluded_count}) does not match "
            f"excluded entries ({actual_excluded})"
        )

    for index, entry in enumerate(result.entries):
        prefix = f"entries[{index}]"

        if not isinstance(entry.path, str) or not entry.path.strip():
            errors.append(f"{prefix}.path must be a non-empty string")
            continue

        if entry.entry_type not in ALLOWED_ENTRY_TYPES:
            errors.append(
                f"{prefix}.entry_type must be one of "
                f"{sorted(ALLOWED_ENTRY_TYPES)!r} (got {entry.entry_type!r})"
            )

    return {
        "valid": len(errors) == 0,
        "errors": errors,
    }
