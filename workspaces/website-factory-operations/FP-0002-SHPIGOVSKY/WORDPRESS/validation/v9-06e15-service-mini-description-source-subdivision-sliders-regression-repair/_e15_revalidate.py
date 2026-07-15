#!/usr/bin/env python3
"""E15 revalidate only — NOT FOR GIT."""
import importlib.util
from pathlib import Path

runner_path = Path(__file__).with_name("_e15_runner.py")
spec = importlib.util.spec_from_file_location("e15_runner", runner_path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

services_db = mod.load_services_db()
grouped = mod.validate_mini_descriptions_mode("grouped_by_parent", services_db)
flat = mod.validate_mini_descriptions_mode("flat", services_db)
sliders = mod.validate_sliders()
mod.json_write(mod.VAL / "post-repair-mini-description-source-validation.json", {"grouped": grouped, "flat": flat})
inventory = mod.build_final_inventory(grouped, flat, sliders, services_db)
mod.json_write(mod.VAL / "final-e15-service-mini-description-and-slider-inventory.json", {"services": inventory, "sliders": sliders})
mini_pass = grouped["result"] == "PASS" and flat["result"] == "PASS"
slider_pass = sliders["result"] == "PASS"
verdict = {
    "verdict": "PASS" if mini_pass and slider_pass else "PARTIAL",
    "e15_complete": "COMPLETE" if mini_pass and slider_pass else "PARTIAL",
    "operator_e14_mini_description_rejection": "ADDRESSED" if mini_pass else "PARTIAL",
    "all_service_cards_admin_when_filled": grouped["result"],
    "services_hub_grouped": grouped["result"],
    "services_hub_flat": flat["result"],
    "zavisimosti_specialists_slider": sliders["result"],
    "zavisimosti_reviews_slider": sliders["result"],
    "recommended_next": "CREATE_V9_06E16_OPERATOR_SERVICE_TREE_VISUAL_QA_TASK",
}
mod.json_write(mod.VAL / "final-verdict.json", verdict)
print(verdict)
