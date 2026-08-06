"""Phase 1B-D6F1B — SITE-002 Telegram operator message formatter (Python twin).

Authoritative visible Russian operator UX. Plain text. UTC+07 local time.
Does not invent counts. Preserves factual underscores in filenames.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any, Final, Mapping, Optional, Sequence

from .import_condition import (
    CATALOG_AND_OFFERS_SUCCESS,
    CATALOG_SUCCESS_OFFERS_INPUT_MISSING,
    COMPLETED_WITH_WARNINGS,
    CONFLICT_OR_INCOMPLETE_FILE_SET,
    FULL_SUCCESS,
    IMPORT_ERROR,
    MONITOR_COULD_NOT_CONFIRM_COMPLETION,
    NO_FRESH_IMPORT,
    RECOVERY_CONDITION_RESOLVED,
)

SITE002_TZ: Final = timezone(timedelta(hours=7), name="UTC+07")
OPERATOR_MESSAGE_VERSION: Final[str] = "1b-d6f1b.1"

TITLE: Final[dict[str, str]] = {
    "SUCCESS": "✅ Импорт 1С завершён успешно",
    "PARTIAL_OFFERS_MISSING": "⚠️ Импорт 1С выполнен не полностью",
    "NO_FRESH": "⚠️ Свежий импорт 1С не обнаружен",
    "ERROR": "❌ Импорт 1С завершился с ошибкой",
    "WARNINGS": "⚠️ Импорт 1С завершён с предупреждениями",
    "MONITOR_UNCONFIRMED": "⚠️ Завершение обмена не подтверждено",
    "CONFLICT": "⚠️ Набор файлов обмена неполный или конфликтный",
    "RECOVERY": "✅ Обмен с 1С восстановлен",
    "ATTENTION_GENERIC": "⚠️ Требует внимания",
}

SCENARIO_NAME_RU: Final[dict[str, str]] = {
    "T1": "Успешный импорт",
    "T2": "Каталог загружен, цены и остатки не получены",
    "T3": "Свежий импорт не обнаружен",
    "T4": "Ошибка импорта",
}


def format_site002_local_time(iso: str) -> str:
    """Format authoritative ISO timestamp as DD.MM.YYYY, HH:mm in UTC+07."""
    text = str(iso or "").strip()
    if not text:
        return ""
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(text)
    except ValueError:
        return ""
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    local = dt.astimezone(SITE002_TZ)
    return local.strftime("%d.%m.%Y, %H:%M")


def is_full_operator_message(text: str) -> bool:
    t = str(text or "")
    return (
        t.startswith("🧪 ТЕСТОВОЕ СООБЩЕНИЕ")
        or t.startswith("✅ ")
        or t.startswith("⚠️ ")
        or t.startswith("❌ ")
    )


def _resolve_variant(data: Mapping[str, Any]) -> str:
    report_class = str(data.get("report_class") or "")
    summary = str(data.get("summary_code") or "")
    status = str(data.get("normalized_status") or "").upper()
    reasons = [str(r or "") for r in (data.get("reason_codes") or [])]

    if report_class == RECOVERY_CONDITION_RESOLVED or summary == "CONDITION_RESOLVED":
        return "RECOVERY"
    if report_class in {FULL_SUCCESS, CATALOG_AND_OFFERS_SUCCESS} or summary == "FULL_IMPORT_SUCCESS":
        return "SUCCESS"
    if (
        report_class == CATALOG_SUCCESS_OFFERS_INPUT_MISSING
        or summary in {"OFFERS_INPUT_MISSING", "OFFERS_PRESENT_NOT_PROCESSED"}
        or "OFFERS0_XML_ABSENT" in reasons
    ):
        return "PARTIAL_OFFERS_MISSING"
    if (
        report_class == NO_FRESH_IMPORT
        or summary == "NO_FRESH_1C_IMPORT"
        or "NO_FRESH_IMPORT_IN_EXPECTED_WINDOW" in reasons
    ):
        return "NO_FRESH"
    if report_class == IMPORT_ERROR or summary == "IMPORT_ERROR" or status in {"FAILED", "ERROR"}:
        return "ERROR"
    if report_class == COMPLETED_WITH_WARNINGS or summary == "IMPORT_COMPLETED_WITH_WARNINGS":
        return "WARNINGS"
    if (
        report_class == MONITOR_COULD_NOT_CONFIRM_COMPLETION
        or summary == "MONITOR_COMPLETION_UNCONFIRMED"
    ):
        return "MONITOR_UNCONFIRMED"
    if report_class == CONFLICT_OR_INCOMPLETE_FILE_SET or summary in {
        "IMPORT_FILE_SET_INCOMPLETE_OR_CONFLICT",
        "IMPORT_CONDITION_INCOMPLETE",
    }:
        return "CONFLICT"
    if status == "OK":
        return "SUCCESS"
    return "ATTENTION_GENERIC"


def _sanitize_error_summary(summary: Optional[str]) -> str:
    s = " ".join(str(summary or "").split()).strip()
    if not s:
        return ""
    if any(tok in s.lower() for tok in ("\\", "/", "stack", "traceback", "event_id", "run_id")):
        return s[:160].split("\\")[0].split("/")[0].strip()
    return s[:200]


def format_operator_telegram_message(data: Mapping[str, Any]) -> str:
    """Build production-visible Telegram body (no test wrapper)."""
    variant = _resolve_variant(data)
    domain = str(data.get("domain") or "bzpm.ru")
    observed = format_site002_local_time(
        str(data.get("observed_at") or data.get("generated_at") or "")
    )
    time_label = "Время проверки" if variant == "NO_FRESH" else "Время"
    lines: list[str] = [TITLE.get(variant, TITLE["ATTENTION_GENERIC"]), "", f"Сайт: {domain}"]
    if observed:
        lines.append(f"{time_label}: {observed}")
    lines.append("")

    if variant == "SUCCESS":
        lines.extend(
            [
                "Каталог обновлён.",
                "Цены и остатки обработаны.",
                "Критических ошибок не обнаружено.",
            ]
        )
        counts = data.get("factual_counts") or {}
        if isinstance(counts, Mapping) and counts.get("authoritative") is True:
            add = counts.get("added_urls")
            rem = counts.get("removed_urls")
            if isinstance(add, int) and isinstance(rem, int) and (add > 0 or rem > 0):
                lines.append(f"Изменения каталога: добавлено {add}, удалено {rem}.")
    elif variant == "PARTIAL_OFFERS_MISSING":
        lines.extend(
            [
                "Каталог обработан успешно.",
                "Файл с ценами и остатками от 1С не получен.",
                "",
                "Цены и остатки товаров могли не обновиться.",
                "",
                "Что проверить:",
                "выгрузку предложений из 1С и наличие файла <code>offers0_*.xml</code>.",
            ]
        )
    elif variant == "NO_FRESH":
        lines.extend(
            [
                "В ожидаемое время новый обмен с 1С не подтверждён.",
                "",
                "Каталог, цены и остатки могли остаться без обновления.",
                "",
                "Что проверить:",
                "расписание обмена и журнал выгрузки 1С.",
            ]
        )
    elif variant == "ERROR":
        lines.extend(
            [
                "Обмен не был завершён корректно.",
                "Актуальность каталога, цен и остатков не подтверждена.",
            ]
        )
        err = _sanitize_error_summary(data.get("error_summary"))  # type: ignore[arg-type]
        if err:
            lines.extend(["", f"Ошибка: {err}"])
        lines.extend(
            [
                "",
                "Что сделать:",
                "проверить журнал импорта и устранить указанную ошибку.",
            ]
        )
    elif variant == "WARNINGS":
        lines.extend(
            [
                "Импорт завершён, но есть некритические предупреждения.",
                "Каталог, цены и остатки обработаны.",
                "",
                "Что проверить:",
                "предупреждения в журнале импорта.",
            ]
        )
    elif variant == "MONITOR_UNCONFIRMED":
        lines.extend(
            [
                "Монитор не подтвердил корректное завершение цикла обмена.",
                "Достоверность отчёта требует проверки.",
                "",
                "Что проверить:",
                "завершение монитора и повторный запуск при необходимости.",
            ]
        )
    elif variant == "CONFLICT":
        lines.extend(
            [
                "Обнаружен неполный или конфликтный набор файлов обмена.",
                "",
                "Что проверить:",
                "состав файлов каталога и цен/остатков перед повторным импортом.",
            ]
        )
    elif variant == "RECOVERY":
        lines.extend(
            [
                "Предыдущая проблема больше не обнаружена.",
                "Каталог, цены и остатки обработаны успешно.",
            ]
        )
    else:
        lines.extend(
            [
                "Состояние обмена с 1С требует внимания оператора.",
                "",
                "Что проверить:",
                "журнал импорта и результат последнего обмена с 1С.",
            ]
        )

    while lines and lines[-1] == "":
        lines.pop()
    return "\n".join(lines)


def wrap_acceptance_test_message(body: str, scenario_name_ru: str) -> str:
    return "\n".join(
        [
            "🧪 ТЕСТОВОЕ СООБЩЕНИЕ",
            "",
            f"Проверяемый сценарий: {scenario_name_ru}",
            "",
            str(body or "").strip(),
        ]
    )


def apply_operator_message_to_envelope(envelope: dict[str, Any]) -> dict[str, Any]:
    """Overwrite action.text with full operator message when not already full."""
    out = dict(envelope)
    action = dict(out.get("action") or {})
    existing = str(action.get("text") or "")
    if is_full_operator_message(existing):
        return out
    run = out.get("run") or {}
    text = format_operator_telegram_message(
        {
            "summary_code": run.get("summary_code"),
            "normalized_status": run.get("normalized_status"),
            "reason_codes": run.get("reason_codes") or [],
            "observed_at": out.get("observed_at"),
            "generated_at": out.get("generated_at"),
            "domain": (out.get("site") or {}).get("domain") or "bzpm.ru",
            "error_summary": existing if run.get("normalized_status") == "FAILED" else None,
        }
    )
    action["text"] = text
    out["action"] = action
    return out
