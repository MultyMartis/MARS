"""Offline pipeline: load → validate → normalize → envelope → security."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Optional

from .artifact_loader import load_artifacts, load_fixture_meta
from .envelope_builder import attach_envelope_with_security
from .errors import ProcessResult
from .models import FixtureMeta
from .normalizer import normalize
from .simple_formatter import format_simple


def process_fixture_dir(
    fixture_dir: Path,
    *,
    now_utc: Optional[datetime] = None,
    build_envelope: bool = True,
    meta: Optional[FixtureMeta] = None,
) -> ProcessResult:
    """Run the offline exporter core against a local fixture/run directory."""
    fixture_dir = Path(fixture_dir)
    loaded_meta = meta or load_fixture_meta(fixture_dir)
    artifacts = load_artifacts(fixture_dir)
    result = normalize(
        artifacts,
        now_utc=now_utc,
        meta=loaded_meta,
    )

    if not build_envelope:
        return result

    result = attach_envelope_with_security(result, meta=loaded_meta)

    # Stale / conflict / failed with trusted metrics: still try envelope
    # when attach did not already run — attach always attempted above.
    # For FAILED we want distributable envelope when metrics trusted.
    if (
        result.envelope is None
        and not result.security_rejected
        and result.metrics_trusted
        and result.normalized_status in {"FAILED", "BLOCKED", "OK", "ATTENTION"}
        and result.summary_code != "ENVELOPE_SECURITY_REJECTED"
    ):
        # attach_envelope already attempted; remaining None means contract gap
        pass

    if result.envelope is not None and result.distributable:
        tz = loaded_meta.display_timezone
        result.simple_text = format_simple(
            result.envelope, tz_name=tz
        )
    else:
        # Stale / blocked / not fresh-eligible: no customer-facing message.
        result.simple_text = None

    return result
