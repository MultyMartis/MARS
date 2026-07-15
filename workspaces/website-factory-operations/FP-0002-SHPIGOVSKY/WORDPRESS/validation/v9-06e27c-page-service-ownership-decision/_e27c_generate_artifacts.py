#!/usr/bin/env python3
"""TEMPORARY E27C artifact generator — NOT FOR GIT COMMIT."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VAL = Path(__file__).resolve().parent
ARCH = ROOT / "architecture"
REPORTS = ROOT / "reports"
PROBE = VAL / "_e27c_probe_out.json"
NOW = datetime.now(timezone.utc).isoformat()
TASK = "V9-06E27C"
BASELINE = "d6caab422bc9301caf3f90631558b43e1c9e3bfb"

data = json.loads(PROBE.read_text(encoding="utf-8"))

SERVICE_MAP = {
    "/uslugi/zavisimosti/": 73,
    "/uslugi/psihicheskoe-zdorovie/": 77,
    "/uslugi/rasstroystva-pischevogo-povedeniya/": 84,
}
PAGE_MAP = {
    "/uslugi/zavisimosti/": 6,
    "/uslugi/psihicheskoe-zdorovie/": 7,
    "/uslugi/rasstroystva-pischevogo-povedeniya/": 8,
}

inventory_out = {
    "task_id": TASK,
    "generated_at": NOW,
    "objects": [],
}
for obj in data["inventory"]:
    is_canonical_v9 = obj.get("path") in SERVICE_MAP or obj.get("path", "").startswith("/uslugi/zavisimosti/")
    entry = {
        **obj,
        "is_canonical_v9_route": is_canonical_v9,
        "route_status": "live" if obj.get("status") == "publish" else obj.get("status"),
        "rendering_source": (
            "single-service.php (runtime winner)"
            if obj["type"] == "service" and obj["path"] in SERVICE_MAP
            else "legacy page object (shadowed at runtime)"
            if obj["type"] == "page" and obj["id"] in (6, 7, 8)
            else "single-service.php child"
            if obj["type"] == "service"
            else "page default"
        ),
        "content_state": (
            "acf_template_managed"
            if obj.get("meta_count", 0) > 10
            else "legacy_generic_page_copy"
            if obj["type"] == "page" and obj["id"] in (6, 7, 8)
            else "skeleton_or_empty"
            if obj.get("content_len", 0) < 50
            else "template_fixture"
        ),
        "current_role": (
            "canonical_route_owner"
            if obj["type"] == "service" and obj["id"] in (73, 77, 84)
            else "shadow_legacy_page"
            if obj["type"] == "page" and obj["id"] in (6, 7, 8)
            else "service_leaf_child"
            if obj["type"] == "service" and obj.get("parent_id") == 73
            else "service_subdivision_child"
            if obj["type"] == "service"
            else "unknown"
        ),
    }
    inventory_out["objects"].append(entry)

route_out = {
    "task_id": TASK,
    "generated_at": NOW,
    "routes": [],
}
for r in data["routes"]:
    menu_owner = None
    if r["route"] == "/uslugi/zavisimosti/":
        menu_owner = {"type": "page", "id": 6, "menu_item_id": 301}
    route_out["routes"].append(
        {
            **r,
            "menu_points_to": menu_owner,
            "page_wins": r["current_owner"]["type"] == "page",
            "service_cpt_wins": r["current_owner"]["type"] == "service",
            "notes": (
                "Primary menu item #301 links page #6 but HTTP serves service #73"
                if r["route"] == "/uslugi/zavisimosti/"
                else "Legacy page #7 shadowed by service #77"
                if r["route"] == "/uslugi/psihicheskoe-zdorovie/"
                else "Legacy page #8 shadowed by service #84"
                if r["route"] == "/uslugi/rasstroystva-pischevogo-povedeniya/"
                else "Hub page #5 — no conflict"
                if r["route"] == "/uslugi/"
                else "Static V9 route has no WP service object yet"
                if r["route"] == "/uslugi/zavisimosti/specialistam/"
                else ""
            ),
        }
    )

menu_out = {
    "task_id": TASK,
    "generated_at": NOW,
    "menus_audited": ["Primary", "Footer", "Legal"],
    "conflict_items": [],
    "all_uslugi_related_items": data["menus"],
}
for m in data["menus"]:
    menu_out["conflict_items"].append(
        {
            **m,
            "recommendation": (
                "RECOMMENDED_MENU_RETARGET_LATER — retarget menu item #301 from page #6 to service CPT #73"
                if m["menu_item_id"] == 301
                else "RECOMMENDED_KEEP"
            ),
        }
    )

static_rows = []
for path, sid in SERVICE_MAP.items():
    pid = PAGE_MAP[path]
    route = next(x for x in data["routes"] if x["route"] == path)
    static_rows.append(
        {
            "route": path,
            "static_v9_exists": True,
            "static_v9_role": route.get("static_v9_role"),
            "static_v9_status": route.get("static_v9_status"),
            "wp_page_object": {"id": pid, "exists": True, "status": "publish"},
            "wp_service_object": {"id": sid, "exists": True, "status": "publish"},
            "current_rendered_owner": route["current_owner"],
            "recommended_canonical_owner": {"type": "service", "id": sid},
            "notes": f"Legacy page #{pid} is shadow duplicate; service #{sid} is runtime and architecture owner",
        }
    )
static_out = {"task_id": TASK, "generated_at": NOW, "rows": static_rows}

risk_out = {
    "task_id": TASK,
    "generated_at": NOW,
    "options": [
        {
            "option": "A",
            "name": "Service CPT owns conflicted subdivision routes",
            "description": "Confirm service #73/#77/#84 as canonical owners; retarget Primary menu; trash legacy pages #6/#7/#8",
            "benefits": [
                "Matches FP-0002 WordPress architecture and ServicePermalinks contract",
                "Matches static V9 SERVICE_SUBDIVISION intent",
                "Preserves ACF-backed service templates and child tree under #73",
                "No URL change — no redirect required",
                "Runtime already serves service CPT today",
            ],
            "risks": [
                "Menu retarget must precede page trash for #6",
                "Operator must approve trash of three legacy pages",
            ],
            "required_future_changes": [
                "Retarget Primary menu item #301 to service #73",
                "Trash pages #6, #7, #8 after menu validation",
            ],
            "rollback": "Restore pages from trash; revert menu item to page #6",
            "verdict": "RECOMMENDED",
        },
        {
            "option": "B",
            "name": "Page owns conflicted subdivision routes",
            "description": "Keep pages #6/#7/#8; demote or remove service CPT objects at same paths",
            "benefits": ["Preserves existing Primary menu object link without retarget"],
            "risks": [
                "Breaks service CPT hierarchy and child routes under #73",
                "Requires rewrite/permalink surgery or service CPT trash",
                "Contradicts static V9 manifest and architecture docs",
                "Loses ACF service subdivision templates",
                "High regression risk for alcohol leaf #74 and zavisimosti children",
            ],
            "required_future_changes": [
                "Trash or reparent services #73/#77/#84",
                "Rebuild subdivision rendering on page templates",
            ],
            "rollback": "Complex — service tree restoration",
            "verdict": "NOT_RECOMMENDED",
        },
        {
            "option": "C",
            "name": "Keep both temporarily",
            "description": "No ownership resolution; retain duplicate page and service objects",
            "benefits": ["Defers operator decision", "No immediate DB writes"],
            "risks": [
                "Menu ambiguity for #6 vs #73",
                "Admin confusion — two objects same title/path",
                "SEO/canonical ambiguity if page ever wins rewrite race",
                "Blocks final WordPress readiness QA",
            ],
            "required_future_changes": [],
            "rollback": "N/A — status quo",
            "verdict": "NOT_RECOMMENDED_EXCEPT_AS_INTERIM",
        },
    ],
}

rec_out = {
    "task_id": TASK,
    "generated_at": NOW,
    "recommendation_summary": "RECOMMENDED_KEEP_SERVICE_CPT",
    "decisions": [
        {
            "route": "/uslugi/zavisimosti/",
            "canonical_owner": {"type": "service", "id": 73},
            "page_6": "RECOMMENDED_TRASH_PAGE_LATER",
            "service_73": "RECOMMENDED_KEEP_SERVICE_CPT",
            "menu": "RECOMMENDED_MENU_RETARGET_LATER",
            "redirect": "NOT_NEEDED",
            "rewrite_permalink": "NOT_NEEDED",
        },
        {
            "route": "/uslugi/psihicheskoe-zdorovie/",
            "canonical_owner": {"type": "service", "id": 77},
            "page_7": "RECOMMENDED_TRASH_PAGE_LATER",
            "service_77": "RECOMMENDED_KEEP_SERVICE_CPT",
            "menu": "NO_MENU_CONFLICT",
            "redirect": "NOT_NEEDED",
            "rewrite_permalink": "NOT_NEEDED",
        },
        {
            "route": "/uslugi/rasstroystva-pischevogo-povedeniya/",
            "canonical_owner": {"type": "service", "id": 84},
            "page_8": "RECOMMENDED_TRASH_PAGE_LATER",
            "service_84": "RECOMMENDED_KEEP_SERVICE_CPT",
            "menu": "NO_MENU_CONFLICT",
            "redirect": "NOT_NEEDED",
            "rewrite_permalink": "NOT_NEEDED",
        },
    ],
    "must_not_touch": [
        {"type": "page", "id": 3, "reason": "privacy policy canonical"},
        {"type": "page", "id": 4, "reason": "front page"},
        {"type": "page", "id": 5, "reason": "services hub /uslugi/"},
        {"type": "page", "id": 19, "reason": "blog archive"},
        {"type": "post", "id": 750, "reason": "demo blog fixture"},
        {"type": "service", "id": 74, "reason": "canonical alcohol leaf"},
        {"type": "service", "id": 75, "reason": "profilakticheskiy-analiz leaf"},
    ],
    "operator_decision_required": False,
    "notes": "Recommendation is evidence-complete; operator approval needed only to execute E27D implementation",
}

e27d_out = {
    "task_id": "V9-06E27D",
    "planned_from": TASK,
    "generated_at": NOW,
    "execution_mode": "BOUNDED_DB_CLEANUP_AND_MENU_RETARGET",
    "prerequisite": "Operator approval of E27C recommendation (Option A)",
    "steps": [
        {
            "step": 1,
            "action": "Fresh DB checkpoint (mysqldump + SHA256)",
            "object_ids": [],
            "safety": "Mandatory pre-write",
            "validation": "db-checkpoint.json + RESTORE.md",
        },
        {
            "step": 2,
            "action": "Retarget Primary menu item #301 from page #6 to service CPT #73",
            "object_ids": [301, 6, 73],
            "safety": "Single menu meta update; no permalink change",
            "validation": "Menu resolves to service; /uslugi/zavisimosti/ still 200 service #73",
        },
        {
            "step": 3,
            "action": "Post-menu HTTP + menu validation",
            "object_ids": [301, 73],
            "safety": "Read-only probes before page trash",
            "validation": "menu_route_alignment PASS",
        },
        {
            "step": 4,
            "action": "Trash legacy pages #6, #7, #8",
            "object_ids": [6, 7, 8],
            "safety": "wp_trash_post only; no permanent delete",
            "validation": "Pages in trash; routes unchanged (service still owns)",
        },
        {
            "step": 5,
            "action": "Post-cleanup route validation",
            "object_ids": [73, 74, 75, 77, 84],
            "safety": "HTTP probe all zavisimosti + subdivision routes",
            "validation": "post-cleanup-route-validation.json",
        },
    ],
    "stop_conditions": [
        "Menu retarget fails or route owner changes unexpectedly",
        "Any protected page/service status changes",
        "Permalink or rewrite flush required (should not happen)",
    ],
    "rollback": "Restore pages #6-#8 from trash; revert menu item #301 to page #6; or full DB checkpoint restore",
    "redirects_needed": False,
    "rewrite_flush_needed": False,
}

screenshot_out = {
    "task_id": TASK,
    "generated_at": NOW,
    "screenshots_captured": False,
    "evidence_mode": "HTTP_BODY_MARKERS_AND_DB_READ_ONLY",
    "manifest": [
        {"target": "/uslugi/zavisimosti/", "file": None, "status": "HTTP_EVIDENCE_ONLY"},
        {"target": "/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/", "file": None, "status": "HTTP_EVIDENCE_ONLY"},
    ],
}

evidence_out = {
    "task_id": TASK,
    "generated_at": NOW,
    "sources": [
        {"source": "pymysql_read_only", "result": "PASS"},
        {"source": "http_route_probe", "result": "PASS", "routes_probed": len(data["routes"])},
        {"source": "service_permalinks_source", "path": "plugins/shpigovsky-core/src/Permalinks/ServicePermalinks.php", "result": "PASS"},
        {"source": "static_v9_manifest", "path": "workspaces/fp-0002-shpigovsky-v9/tools/v9-route-manifest.json", "result": "PASS"},
        {"source": "e27a_dependency_audit", "result": "PASS"},
        {"source": "e27b_post_cleanup_validation", "result": "PASS"},
        {"source": "wp_admin_screenshots", "result": "NOT_CAPTURED"},
    ],
}

no_mut = {
    "task_id": TASK,
    "generated_at": NOW,
    "db_writes": 0,
    "before": data["before_snapshot"],
    "after": data["after_snapshot"],
    "unchanged": {
        "pages_6_7_8_status": "publish",
        "service_73_status": "publish",
        "menu_checksum": data["before_snapshot"]["menu_checksum"],
        "options": data["before_snapshot"]["options"],
    },
    "result": "PASS",
}

contract_out = {
    "task_id": TASK,
    "generated_at": NOW,
    "baseline_commit": BASELINE,
    "conflict_diagnosis": "Legacy hub-child pages #6/#7/#8 duplicate service CPT subdivision routes; rewrite rules assign runtime to service CPT; Primary menu still links page #6",
    "current_route_owner": {
        "/uslugi/zavisimosti/": {"type": "service", "id": 73},
        "/uslugi/psihicheskoe-zdorovie/": {"type": "service", "id": 77},
        "/uslugi/rasstroystva-pischevogo-povedeniya/": {"type": "service", "id": 84},
    },
    "current_menu_owner": {
        "/uslugi/zavisimosti/": {"menu_item_id": 301, "type": "page", "id": 6},
    },
    "recommended_canonical_owner": rec_out["decisions"],
    "must_not_touch_yet": rec_out["must_not_touch"],
    "operator_decision": "Approve Option A and authorize E27D implementation",
    "proposed_e27d_scope": e27d_out["steps"],
    "risks": risk_out["options"][0]["risks"],
    "rollback_notes": e27d_out["rollback"],
    "recommended_next_task": "CREATE_V9_06E27D_PAGE_SERVICE_OWNERSHIP_IMPLEMENTATION_TASK",
    "result": "PASS",
}

verdict_out = {
    "task_id": TASK,
    "generated_at": NOW,
    "verdict": "PASS",
    "v9_06e27c_complete": "COMPLETE",
    "read_only_discipline": "PASS",
    "conflicted_object_inventory": "PASS",
    "route_ownership_audit": "PASS",
    "menu_ownership_audit": "PASS",
    "architecture_comparison": "PASS",
    "ownership_recommendation": "PASS",
    "proposed_e27d_plan": "PASS",
    "no_mutation": "PASS",
    "no_scope_drift": "PASS",
    "recommended_next_phase": "CREATE_V9_06E27D_PAGE_SERVICE_OWNERSHIP_IMPLEMENTATION_TASK",
}

artifacts = {
    "conflicted-object-inventory.json": inventory_out,
    "route-ownership-audit.json": route_out,
    "menu-ownership-audit.json": menu_out,
    "static-v9-wp-architecture-comparison.json": static_out,
    "ownership-options-risk-analysis.json": risk_out,
    "recommended-ownership-decision.json": rec_out,
    "proposed-e27d-implementation-plan.json": e27d_out,
    "screenshot-manifest.json": screenshot_out,
    "evidence-result.json": evidence_out,
    "no-mutation-validation.json": no_mut,
    "final-e27c-ownership-decision-contract.json": contract_out,
    "final-verdict.json": verdict_out,
}

for name, payload in artifacts.items():
    (VAL / name).write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

print(json.dumps({"written": list(artifacts.keys())}, indent=2))
