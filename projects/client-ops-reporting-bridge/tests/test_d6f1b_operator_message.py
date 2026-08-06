"""Phase 1B-D6F1B — Python operator message + import condition regression."""

from __future__ import annotations

import unittest

from client_ops_reporting_bridge.import_condition import (
    CATALOG_SUCCESS_OFFERS_INPUT_MISSING,
    FULL_SUCCESS,
    IMPORT_ERROR,
    NO_FRESH_IMPORT,
    classify_import_report,
)
from client_ops_reporting_bridge.telegram_operator_message import (
    format_operator_telegram_message,
    format_site002_local_time,
    wrap_acceptance_test_message,
)


class TestD6F1BOperatorMessage(unittest.TestCase):
    def test_local_time(self):
        self.assertEqual(
            format_site002_local_time("2026-08-06T11:20:00Z"),
            "06.08.2026, 18:20",
        )

    def test_success_russian(self):
        text = format_operator_telegram_message(
            {
                "report_class": FULL_SUCCESS,
                "observed_at": "2026-08-06T11:20:00Z",
            }
        )
        self.assertTrue(text.startswith("✅ Импорт 1С завершён успешно"))
        self.assertIn("Цены и остатки обработаны.", text)
        self.assertNotIn("UTC", text)
        self.assertNotIn("Offers", text)

    def test_missing_offers(self):
        text = format_operator_telegram_message(
            {
                "report_class": CATALOG_SUCCESS_OFFERS_INPUT_MISSING,
                "observed_at": "2026-08-06T11:20:00Z",
            }
        )
        self.assertIn("offers0_*.xml", text)
        self.assertNotIn("offers0-N", text)
        self.assertIn("могли не обновиться", text)
        self.assertNotIn("отключен", text.lower())

    def test_no_fresh(self):
        r = classify_import_report(fresh_import_confirmed=False)
        self.assertEqual(r["report_class"], NO_FRESH_IMPORT)
        text = format_operator_telegram_message(
            {
                "report_class": NO_FRESH_IMPORT,
                "observed_at": "2026-08-06T11:20:00Z",
            }
        )
        self.assertTrue(text.startswith("⚠️ Свежий импорт 1С не обнаружен"))

    def test_error(self):
        r = classify_import_report(
            fresh_import_confirmed=True,
            catalog_input_files=["import0_1.xml"],
            import_error=True,
        )
        self.assertEqual(r["report_class"], IMPORT_ERROR)
        text = format_operator_telegram_message(
            {
                "report_class": IMPORT_ERROR,
                "observed_at": "2026-08-06T11:20:00Z",
                "error_summary": "Ошибка фазы",
            }
        )
        self.assertIn("Ошибка: Ошибка фазы", text)
        self.assertNotIn("Каталог обновлён", text)

    def test_acceptance_wrapper(self):
        body = format_operator_telegram_message(
            {"report_class": FULL_SUCCESS, "observed_at": "2026-08-06T11:20:00Z"}
        )
        wrapped = wrap_acceptance_test_message(body, "Успешный импорт")
        self.assertTrue(wrapped.startswith("🧪 ТЕСТОВОЕ СООБЩЕНИЕ"))
        self.assertIn("Проверяемый сценарий: Успешный импорт", wrapped)
        self.assertNotIn("TEST-GALLERY", wrapped)

    def test_monitor_action_text_no_marker(self):
        r = classify_import_report(
            fresh_import_confirmed=True,
            monitor_completion_confirmed=False,
        )
        self.assertNotIn("маркер", r["action_text"].lower())
        self.assertNotIn("summary", r["action_text"].lower())


if __name__ == "__main__":
    unittest.main()
