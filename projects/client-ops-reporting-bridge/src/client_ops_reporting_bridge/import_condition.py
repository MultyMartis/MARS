"""Import / offers report classification contract (Phase 1B-D6F1A).

Factual classification only. Does not claim products were disabled solely
because offers files are absent. Does not invent price/stock updates without
authoritative offers input.
"""

from __future__ import annotations

from typing import Any, Final, Mapping, Optional, Sequence

# Exact report classes (operator contract).
FULL_SUCCESS: Final[str] = "FULL_SUCCESS"
CATALOG_SUCCESS_OFFERS_INPUT_MISSING: Final[str] = "CATALOG_SUCCESS_OFFERS_INPUT_MISSING"
CATALOG_AND_OFFERS_SUCCESS: Final[str] = "CATALOG_AND_OFFERS_SUCCESS"
COMPLETED_WITH_WARNINGS: Final[str] = "COMPLETED_WITH_WARNINGS"
IMPORT_ERROR: Final[str] = "IMPORT_ERROR"
NO_FRESH_IMPORT: Final[str] = "NO_FRESH_IMPORT"
MONITOR_COULD_NOT_CONFIRM_COMPLETION: Final[str] = "MONITOR_COULD_NOT_CONFIRM_COMPLETION"
CONFLICT_OR_INCOMPLETE_FILE_SET: Final[str] = "CONFLICT_OR_INCOMPLETE_FILE_SET"
RECOVERY_CONDITION_RESOLVED: Final[str] = "RECOVERY_CONDITION_RESOLVED"

SEVERITY_OK: Final[str] = "OK"
SEVERITY_ATTENTION: Final[str] = "ATTENTION"
SEVERITY_ERROR: Final[str] = "ERROR"

# Offers state classifications (operator contract).
OFFERS_INPUT_PRESENT_AND_PROCESSED: Final[str] = "OFFERS_INPUT_PRESENT_AND_PROCESSED"
OFFERS_INPUT_ABSENT: Final[str] = "OFFERS_INPUT_ABSENT"
OFFERS_INPUT_PRESENT_NOT_PROCESSED: Final[str] = "OFFERS_INPUT_PRESENT_NOT_PROCESSED"
OFFERS_INPUT_STATE_AMBIGUOUS: Final[str] = "OFFERS_INPUT_STATE_AMBIGUOUS"

CANONICAL_OFFERS_GLOB: Final[str] = "offers0_*.xml"
CANONICAL_CATALOG_GLOB: Final[str] = "import0_*.xml"


def _norm_names(names: Optional[Sequence[str]]) -> list[str]:
    out: list[str] = []
    for n in names or []:
        s = str(n or "").strip()
        if s:
            out.append(s)
    return out


def offers_files_present(names: Optional[Sequence[str]]) -> bool:
    """True when at least one canonical offers0_*.xml name is present."""
    for n in _norm_names(names):
        lower = n.lower()
        if lower.startswith("offers0_") and lower.endswith(".xml"):
            return True
    return False


def catalog_files_present(names: Optional[Sequence[str]]) -> bool:
    for n in _norm_names(names):
        lower = n.lower()
        if lower.startswith("import0_") and lower.endswith(".xml"):
            return True
    return False


def classify_offers_state(
    *,
    offers_input_files: Optional[Sequence[str]] = None,
    offers_phase_status: Optional[str] = None,
    offers_processed_count: Optional[int] = None,
) -> str:
    """Return one exact offers-state classification."""
    present = offers_files_present(offers_input_files)
    status = str(offers_phase_status or "").strip().upper()
    processed = offers_processed_count
    if present and (
        (isinstance(processed, int) and processed > 0)
        or status in {"PASS", "OK", "SUCCESS", "PROCESSED"}
    ):
        # Presence alone with formal PASS and zero listed inputs is NOT processed.
        if present and (processed is None or processed > 0):
            return OFFERS_INPUT_PRESENT_AND_PROCESSED
    if present and (processed == 0 or status in {"SKIP", "EMPTY", "NO_INPUT"}):
        return OFFERS_INPUT_PRESENT_NOT_PROCESSED
    if not present:
        return OFFERS_INPUT_ABSENT
    return OFFERS_INPUT_STATE_AMBIGUOUS


def classify_import_report(
    *,
    fresh_import_confirmed: bool,
    catalog_input_files: Optional[Sequence[str]] = None,
    offers_input_files: Optional[Sequence[str]] = None,
    catalog_phase_ok: Optional[bool] = None,
    offers_phase_ok: Optional[bool] = None,
    offers_processed_count: Optional[int] = None,
    import_error: bool = False,
    warnings_present: bool = False,
    monitor_completion_confirmed: bool = True,
    conflict_or_incomplete: bool = False,
    recovery_resolved: bool = False,
) -> dict[str, Any]:
    """Classify a daily import/report outcome.

    Returns dict with keys: report_class, severity, offers_state, summary_code,
    reason_codes, action_code, action_text, factual_claims.
    """
    offers_state = classify_offers_state(
        offers_input_files=offers_input_files,
        offers_phase_status="PASS" if offers_phase_ok else None,
        offers_processed_count=offers_processed_count,
    )
    # Formal offers PASS with no input files ⇒ absent, not processed.
    if (
        offers_phase_ok
        and not offers_files_present(offers_input_files)
        and (offers_processed_count is None or offers_processed_count == 0)
    ):
        offers_state = OFFERS_INPUT_ABSENT

    if not monitor_completion_confirmed:
        return {
            "report_class": MONITOR_COULD_NOT_CONFIRM_COMPLETION,
            "severity": SEVERITY_ATTENTION,
            "offers_state": offers_state,
            "summary_code": "MONITOR_COMPLETION_UNCONFIRMED",
            "reason_codes": ["MONITOR_COMPLETION_EVIDENCE_MISSING"],
            "action_code": "REVIEW_MONITOR_COMPLETION",
            "action_text": "Проверить завершение монитора: маркер/summary отсутствуют или противоречивы",
            "factual_claims": [
                "completion evidence missing or inconsistent",
            ],
        }

    if conflict_or_incomplete:
        return {
            "report_class": CONFLICT_OR_INCOMPLETE_FILE_SET,
            "severity": SEVERITY_ATTENTION,
            "offers_state": offers_state,
            "summary_code": "IMPORT_FILE_SET_INCOMPLETE_OR_CONFLICT",
            "reason_codes": ["IMPORT_SOURCE_SET_CONFLICT"],
            "action_code": "REVIEW_IMPORT_FILE_SET",
            "action_text": "Проверить комплект файлов обмена 1С (каталог/offers)",
            "factual_claims": [
                "conflicting or incomplete source file set",
            ],
        }

    if import_error:
        return {
            "report_class": IMPORT_ERROR,
            "severity": SEVERITY_ERROR,
            "offers_state": offers_state,
            "summary_code": "IMPORT_ERROR",
            "reason_codes": ["IMPORT_PHASE_ERROR"],
            "action_code": "REVIEW_IMPORT_ERROR",
            "action_text": "Разбрать ошибку импорта 1С по фазе и журналу",
            "factual_claims": [
                "import phase reported an error",
            ],
        }

    if not fresh_import_confirmed:
        return {
            "report_class": NO_FRESH_IMPORT,
            "severity": SEVERITY_ATTENTION,
            "offers_state": offers_state,
            "summary_code": "NO_FRESH_1C_IMPORT",
            "reason_codes": ["NO_FRESH_IMPORT_IN_EXPECTED_WINDOW"],
            "action_code": "REVIEW_MISSING_IMPORT",
            "action_text": "Подтвердить, почему не было свежего обмена с 1С в ожидаемом окне",
            "factual_claims": [
                "no fresh 1C import confirmed in expected window",
            ],
        }

    catalog_ok = bool(catalog_phase_ok) and catalog_files_present(catalog_input_files)
    offers_ok = offers_state == OFFERS_INPUT_PRESENT_AND_PROCESSED

    if catalog_ok and offers_state == OFFERS_INPUT_ABSENT:
        return {
            "report_class": CATALOG_SUCCESS_OFFERS_INPUT_MISSING,
            "severity": SEVERITY_ATTENTION,
            "offers_state": offers_state,
            "summary_code": "OFFERS_INPUT_MISSING",
            "reason_codes": [
                "CATALOG_IMPORT_COMPLETED",
                "OFFERS0_XML_ABSENT",
                "PRICES_STOCK_MAY_NOT_UPDATE",
            ],
            "action_code": "REVIEW_MISSING_OFFERS",
            "action_text": (
                "Каталог импортирован; файл offers0_*.xml не получен — "
                "цены и остатки могли не обновиться"
            ),
            "factual_claims": [
                "catalog import completed",
                "offers0_*.xml was not received/found",
                "prices and stock may not have been updated",
                "this is not a full successful 1C exchange",
            ],
            "forbidden_claims": [
                "products were disabled because offers were absent",
                "prices changed without offers evidence",
            ],
        }

    if catalog_ok and offers_ok and warnings_present:
        return {
            "report_class": COMPLETED_WITH_WARNINGS,
            "severity": SEVERITY_ATTENTION,
            "offers_state": offers_state,
            "summary_code": "IMPORT_COMPLETED_WITH_WARNINGS",
            "reason_codes": ["IMPORT_WARNINGS_PRESENT"],
            "action_code": "REVIEW_IMPORT_WARNINGS",
            "action_text": "Импорт завершён с предупреждениями — проверить журнал",
            "factual_claims": [
                "import completed with non-critical warnings",
            ],
        }

    if catalog_ok and offers_ok:
        report_class = (
            CATALOG_AND_OFFERS_SUCCESS
            if offers_processed_count and offers_processed_count > 0
            else FULL_SUCCESS
        )
        if recovery_resolved:
            report_class = RECOVERY_CONDITION_RESOLVED
        return {
            "report_class": report_class,
            "severity": SEVERITY_OK,
            "offers_state": offers_state,
            "summary_code": "FULL_IMPORT_SUCCESS"
            if report_class != RECOVERY_CONDITION_RESOLVED
            else "CONDITION_RESOLVED",
            "reason_codes": ["CATALOG_PROCESSED", "OFFERS_PROCESSED"],
            "action_code": "NONE",
            "action_text": "Полный обмен 1С завершён без критических ошибок",
            "factual_claims": [
                "catalog processed",
                "offers processed",
                "no critical import errors",
            ],
        }

    if catalog_ok and offers_state == OFFERS_INPUT_PRESENT_NOT_PROCESSED:
        return {
            "report_class": CATALOG_SUCCESS_OFFERS_INPUT_MISSING,
            "severity": SEVERITY_ATTENTION,
            "offers_state": offers_state,
            "summary_code": "OFFERS_PRESENT_NOT_PROCESSED",
            "reason_codes": ["OFFERS_INPUT_PRESENT_NOT_PROCESSED"],
            "action_code": "REVIEW_OFFERS_PROCESSING",
            "action_text": "Offers-файл найден, но обработка цен/остатков не подтверждена",
            "factual_claims": [
                "offers file present but not processed",
            ],
        }

    return {
        "report_class": CONFLICT_OR_INCOMPLETE_FILE_SET,
        "severity": SEVERITY_ATTENTION,
        "offers_state": offers_state,
        "summary_code": "IMPORT_CONDITION_INCOMPLETE",
        "reason_codes": ["IMPORT_CONDITION_UNCLASSIFIED_INCOMPLETE"],
        "action_code": "REVIEW_IMPORT_CONDITION",
        "action_text": "Проверить комплект и результаты фаз импорта 1С",
        "factual_claims": [
            "import condition incomplete or ambiguous",
        ],
    }


def apply_import_condition_to_status(
    *,
    current_status: str,
    import_result: Mapping[str, Any],
) -> dict[str, Any]:
    """Merge import classification into monitor-derived status.

    Import ATTENTION/ERROR wins over OK. Does not downgrade FAILED.
    """
    severity = str(import_result.get("severity") or SEVERITY_OK)
    status = current_status
    if current_status == "FAILED":
        status = "FAILED"
    elif severity == SEVERITY_ERROR:
        status = "FAILED"
    elif severity == SEVERITY_ATTENTION and current_status == "OK":
        status = "ATTENTION"
    elif severity == SEVERITY_ATTENTION:
        status = "ATTENTION"
    return {
        "normalized_status": status,
        "summary_code": import_result.get("summary_code"),
        "reason_codes": list(import_result.get("reason_codes") or []),
        "action_code": import_result.get("action_code"),
        "action_text": import_result.get("action_text"),
        "report_class": import_result.get("report_class"),
        "offers_state": import_result.get("offers_state"),
    }
