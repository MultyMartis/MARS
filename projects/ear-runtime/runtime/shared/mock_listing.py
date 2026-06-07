"""EAR Runtime mock listing builder — synthetic listing data only.

Standard library only. No filesystem reads. No SITE-001 data. No network.
"""

from __future__ import annotations

from shared.listing_models import ListingEntry, ListingResult

_MOCK_SOURCE = "mock"
_MOCK_TIMESTAMP = "2026-06-04T12:00:00Z"


def build_mock_listing() -> ListingResult:
    """Return a synthetic ListingResult with representative path entries."""
    entries: list[ListingEntry] = [
        ListingEntry(
            path="catalog/",
            entry_type="directory",
            size=None,
            modified=_MOCK_TIMESTAMP,
            excluded=False,
        ),
        ListingEntry(
            path="catalog/controller/",
            entry_type="directory",
            size=None,
            modified=_MOCK_TIMESTAMP,
            excluded=False,
        ),
        ListingEntry(
            path="catalog/controller/startup/",
            entry_type="directory",
            size=None,
            modified=_MOCK_TIMESTAMP,
            excluded=False,
        ),
        ListingEntry(
            path="catalog/controller/startup/seo_url.php",
            entry_type="file",
            size=2048,
            modified=_MOCK_TIMESTAMP,
            excluded=False,
        ),
        ListingEntry(
            path="catalog/model/",
            entry_type="directory",
            size=None,
            modified=_MOCK_TIMESTAMP,
            excluded=False,
        ),
        ListingEntry(
            path="image/",
            entry_type="directory",
            size=None,
            modified=_MOCK_TIMESTAMP,
            excluded=False,
        ),
        ListingEntry(
            path="image/cache/",
            entry_type="directory",
            size=None,
            modified=_MOCK_TIMESTAMP,
            excluded=True,
        ),
        ListingEntry(
            path="system/",
            entry_type="directory",
            size=None,
            modified=_MOCK_TIMESTAMP,
            excluded=False,
        ),
        ListingEntry(
            path="system/storage/cache/",
            entry_type="directory",
            size=None,
            modified=_MOCK_TIMESTAMP,
            excluded=True,
        ),
        ListingEntry(
            path="system/config/",
            entry_type="directory",
            size=None,
            modified=_MOCK_TIMESTAMP,
            excluded=False,
        ),
        ListingEntry(
            path="admin/",
            entry_type="directory",
            size=None,
            modified=_MOCK_TIMESTAMP,
            excluded=False,
        ),
        ListingEntry(
            path="index.php",
            entry_type="file",
            size=512,
            modified=_MOCK_TIMESTAMP,
            excluded=False,
        ),
    ]

    excluded_count = sum(1 for entry in entries if entry.excluded)

    return ListingResult(
        source=_MOCK_SOURCE,
        entry_count=len(entries),
        excluded_count=excluded_count,
        entries=entries,
    )
