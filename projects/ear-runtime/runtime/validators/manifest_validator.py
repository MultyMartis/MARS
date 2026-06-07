"""EAR Runtime manifest validator — structural checks on Manifest only.



Standard library only. No runtime execution. No remote access.

"""



from __future__ import annotations



from typing import Any



from shared.manifest_models import Manifest



ALLOWED_ENTRY_TYPES: frozenset[str] = frozenset({"file", "directory"})





def validate_manifest(manifest: Manifest) -> dict[str, Any]:

    """Validate a Manifest object. Returns structured valid/errors result."""

    errors: list[str] = []



    if manifest.entries is None:

        errors.append("entries list must exist")

        return {

            "valid": False,

            "errors": errors,

        }



    if not isinstance(manifest.source, str) or not manifest.source.strip():

        errors.append("source must be a non-empty string")



    actual_count = len(manifest.entries)

    if manifest.entry_count != actual_count:

        errors.append(

            f"entry_count ({manifest.entry_count}) does not match "

            f"entries length ({actual_count})"

        )



    actual_excluded = sum(1 for entry in manifest.entries if entry.excluded)

    if manifest.excluded_count != actual_excluded:

        errors.append(

            f"excluded_count ({manifest.excluded_count}) does not match "

            f"excluded entries ({actual_excluded})"

        )



    for index, entry in enumerate(manifest.entries):

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

