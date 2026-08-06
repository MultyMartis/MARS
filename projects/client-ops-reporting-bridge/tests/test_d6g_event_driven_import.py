"""Phase 1B-D6G focused regression (offline)."""
from __future__ import annotations

import unittest
from pathlib import Path

from client_ops_reporting_bridge.import_condition import (
    CATALOG_SUCCESS_OFFERS_INPUT_MISSING,
    FULL_SUCCESS,
    IMPORT_ERROR,
    NO_FRESH_IMPORT,
    classify_import_report,
)
from client_ops_reporting_bridge.telegram_operator_message import format_operator_telegram_message


class D6GClassificationTests(unittest.TestCase):
    def test_r10_success_terminal(self):
        c = classify_import_report(
            fresh_import_confirmed=True,
            catalog_input_files=["import0_1.xml"],
            offers_input_files=["offers0_1.xml"],
            catalog_phase_ok=True,
            offers_phase_ok=True,
            offers_processed_count=1,
        )
        self.assertIn(c["report_class"], {FULL_SUCCESS, "CATALOG_AND_OFFERS_SUCCESS"})

    def test_r11_missing_offers_attention(self):
        c = classify_import_report(
            fresh_import_confirmed=True,
            catalog_input_files=["import0_1.xml"],
            offers_input_files=[],
            catalog_phase_ok=True,
            offers_phase_ok=True,
            offers_processed_count=0,
        )
        self.assertEqual(c["report_class"], CATALOG_SUCCESS_OFFERS_INPUT_MISSING)
        text = format_operator_telegram_message(
            {
                "report_class": c["report_class"],
                "summary_code": c["summary_code"],
                "reason_codes": c["reason_codes"],
                "domain": "bzpm.ru",
                "observed_at": "2026-08-06T12:30:00+07:00",
            }
        )
        self.assertIn("Импорт 1С выполнен не полностью", text)
        self.assertIn("могли не обновиться", text)
        self.assertNotIn("event_id", text)
        self.assertNotIn("run_id", text)

    def test_r12_failed_terminal(self):
        c = classify_import_report(
            fresh_import_confirmed=True,
            catalog_input_files=["import0_1.xml"],
            offers_input_files=[],
            catalog_phase_ok=False,
            import_error=True,
        )
        self.assertEqual(c["report_class"], IMPORT_ERROR)

    def test_r17_watchdog_no_fresh(self):
        c = classify_import_report(fresh_import_confirmed=False, monitor_completion_confirmed=True)
        self.assertEqual(c["report_class"], NO_FRESH_IMPORT)
        text = format_operator_telegram_message(
            {
                "report_class": c["report_class"],
                "summary_code": c["summary_code"],
                "reason_codes": c["reason_codes"],
                "domain": "bzpm.ru",
                "observed_at": "2026-08-06T13:05:00+07:00",
            }
        )
        self.assertIn("Свежий импорт 1С не обнаружен", text)

    def test_r20_ux_preserved_success(self):
        text = format_operator_telegram_message(
            {
                "report_class": FULL_SUCCESS,
                "summary_code": "FULL_IMPORT_SUCCESS",
                "domain": "bzpm.ru",
                "observed_at": "2026-08-06T12:15:00+07:00",
            }
        )
        self.assertTrue(text.startswith("✅ Импорт 1С завершён успешно"))
        self.assertIn("06.08.2026, 12:15", text)


class D6GContractPresenceTests(unittest.TestCase):
    def test_runner_and_admin_sources_exist(self):
        root = Path(__file__).resolve().parents[3]
        for rel in [
            "projects/ocpilot/sites/site-002/tools/mars_1c_import_wrapper.php",
            "projects/ocpilot/sites/site-002/tools/mars_1c_import_run_contract.php",
            "projects/ocpilot/sites/site-002/opencart-admin/mars_1c_exchange/admin/controller/tool/mars_1c_exchange.php",
        ]:
            self.assertTrue((root / rel).is_file(), msg=rel)

    def test_wrapper_mentions_d6g_contract(self):
        root = Path(__file__).resolve().parents[3]
        wrapper = (root / "projects/ocpilot/sites/site-002/tools/mars_1c_import_wrapper.php").read_text(
            encoding="utf-8"
        )
        self.assertIn("mars_1c_import_run_contract.php", wrapper)
        contract = (root / "projects/ocpilot/sites/site-002/tools/mars_1c_import_run_contract.php").read_text(encoding="utf-8")
        self.assertIn("ATTENTION_OFFERS_INPUT_MISSING", contract)
        self.assertIn("mars_1c_classify_terminal", wrapper)
        self.assertIn("mars_mode_enqueue", wrapper)
        self.assertIn("1.2.0", wrapper)


if __name__ == "__main__":
    unittest.main()
