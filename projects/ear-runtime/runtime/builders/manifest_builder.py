"""EAR Runtime manifest builder — ListingResult to Manifest mapping only.



Standard library only. No filesystem access. No network. No hashing.

"""



from __future__ import annotations



from shared.listing_models import ListingResult

from shared.manifest_models import Manifest, ManifestEntry





def build_manifest(listing_result: ListingResult) -> Manifest:

    """Map a ListingResult to a Manifest without enrichment or IO."""

    entries = [

        ManifestEntry(

            path=entry.path,

            entry_type=entry.entry_type,

            excluded=entry.excluded,

        )

        for entry in listing_result.entries

    ]

    return Manifest(

        source=listing_result.source,

        entry_count=listing_result.entry_count,

        excluded_count=listing_result.excluded_count,

        entries=entries,

    )

