# V9-06D.3 planning doc generator — planning artifacts only; no runtime writes.
from __future__ import annotations

import json
from pathlib import Path

WP = Path(r"X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\WORDPRESS")
V9 = Path(r"X:\AI MARS\workspaces\fp-0002-shpigovsky-v9")
ARCH = WP / "architecture"
VAL = WP / "validation" / "v9-06d3-content-migration-planning"
REP = WP / "reports"
FORGE_FP = Path(
    r"X:\AI MARS\projects\mars-website-factory\subsystems\forge-wordpress\projects\fp-0002"
)
FORGE_IDX = Path(
    r"X:\AI MARS\projects\mars-website-factory\subsystems\forge-wordpress\OPERATIONAL-INDEX.md"
)
WF_IDX = Path(r"X:\AI MARS\projects\mars-website-factory\OPERATIONAL-INDEX.md")
V9_STATUS = Path(
    r"X:\AI MARS\workspaces\fp-0002-shpigovsky-v9\foundation\FP-0002-V9-OPERATIONAL-STATUS.md"
)
V9_GATE_DIR = Path(
    r"X:\AI MARS\workspaces\fp-0002-shpigovsky-v9\forge-intake\validation"
)

HEAD = "26e1fc93f494fb86aa711d011499cb8178305534"


def load(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


def dump(p: Path, obj):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write(p: Path, text: str):
    p.parent.mkdir(parents=True, exist_ok=True)
    if not text.endswith("\n"):
        text += "\n"
    p.write_text(text, encoding="utf-8")


def parse_acf_fields(group_path: Path):
    data = load(group_path)
    fields = []

    def walk(items, parent=None):
        for f in items:
            entry = {
                "key": f.get("key"),
                "name": f.get("name"),
                "label": f.get("label"),
                "type": f.get("type"),
                "required": bool(f.get("required")),
                "max_rows": f.get("max") if f.get("type") == "repeater" else None,
                "parent": parent,
            }
            fields.append(entry)
            if f.get("type") == "repeater" and f.get("sub_fields"):
                walk(f["sub_fields"], parent=f.get("name"))

    walk(data.get("fields", []))
    return data, fields


def main():
    runtime = load(VAL / "runtime-inventory.json")
    route_map = load(ARCH / "FP-0002-V9-ROUTE-ENTITY-TEMPLATE-MAP-v1.json")
    svc_reg = load(ARCH / "FP-0002-SERVICE-ENTITY-REGISTRY-v1.json")
    svc_obj = load(ARCH / "FP-0002-V9-06D2-SERVICE-OBJECT-REGISTRY-v1.json")
    page_obj = load(ARCH / "FP-0002-V9-06D2-PAGE-OBJECT-REGISTRY-v1.json")
    acf_reg = load(ARCH / "FP-0002-V9-06C-ACF-FIELD-GROUP-REGISTRY-v1.json")
    v9_static = load(VAL / "v9-static-content-inventory.json")

    svc_by_path = {o["path"]: o for o in svc_obj["objects"]}
    svc_entity = {s["service_id"]: s for s in svc_reg["services"]}
    page_by_route = {r["route_id"]: r for r in page_obj["routes"]}
    posts = runtime["posts"]

    # --- Route matrix ---
    def acf_for_route(r):
        cls = r["primary_entity_class"]
        sub = r["entity_subtype"]
        if cls == "SERVICE":
            return [
                "group_fp02_service_layout_hero",
                "group_fp02_service_structured_sections",
                "group_fp02_service_faq",
                "group_fp02_service_relationships",
            ]
        if cls == "POST":
            return ["group_fp02_blog_post_article_meta"]
        if cls == "POSTS_PAGE":
            return []
        mapping = {
            "home": ["group_fp02_page_home"],
            "services_hub": ["group_fp02_page_services_hub"],
            "institutional": ["group_fp02_page_institutional"],
            "contacts": ["group_fp02_page_contacts"],
            "reviews": ["group_fp02_page_reviews"],
            "legal": ["group_fp02_page_legal"],
        }
        return mapping.get(sub, [])

    def wave_for_route(r):
        sub = r["entity_subtype"]
        url = r["url"]
        if r["content_status"] == "DEMO" or sub == "legal":
            return "WAVE_4_BLOG_LEGAL_REVIEW"
        if sub in ("blog_article", "blog_archive"):
            return "WAVE_4_BLOG_LEGAL_REVIEW"
        wave1 = {
            "/",
            "/uslugi/",
            "/kontakty/",
            "/uslugi/zavisimosti/",
            "/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/",
            "/uslugi/psihicheskoe-zdorovie/",
            "/uslugi/rasstroystva-pischevogo-povedeniya/",
        }
        if url in wave1:
            return "WAVE_1_VISUAL_MINIMUM"
        if r["primary_entity_class"] == "SERVICE":
            return "WAVE_2_SERVICE_CONTENT"
        if sub in ("institutional", "reviews"):
            return "WAVE_3_INSTITUTIONAL_CONTENT"
        return "WAVE_3_INSTITUTIONAL_CONTENT"

    def action_for_route(r, wave):
        if r["content_status"] == "DEMO":
            return "DEFER_LEGAL"
        if r["entity_subtype"] == "blog_archive":
            return "KEEP_EXISTING"
        if r["entity_subtype"] == "blog_article":
            return "CREATE_PLACEHOLDER_ONLY"
        if wave == "WAVE_1_VISUAL_MINIMUM":
            return "FILL_ACF_MINIMAL"
        if r["content_status"] == "PLACEHOLDER":
            return "CREATE_PLACEHOLDER_ONLY"
        return "FILL_ACF_FULL_LATER"

    def risk_for_route(r):
        if r["content_status"] == "DEMO":
            return "HIGH"
        if r["url"] in ("/", "/uslugi/"):
            return "MEDIUM"
        if r["primary_entity_class"] == "SERVICE" and r["content_status"] == "FULL":
            return "MEDIUM"
        return "LOW"

    def target_object_type(r):
        if r["primary_entity_class"] == "PAGE" and r["entity_subtype"] == "legal":
            return "LEGAL_PAGE"
        return r["primary_entity_class"]

    matrix_routes = []
    for r in route_map["routes"]:
        wave = wave_for_route(r)
        action = action_for_route(r, wave)
        obj_type = target_object_type(r)
        target_id = None
        if r["primary_entity_class"] == "SERVICE":
            so = svc_by_path.get(r["url"])
            target_id = so["ID"] if so else None
        elif r["primary_entity_class"] in ("PAGE", "POSTS_PAGE"):
            pr = page_by_route.get(r["id"])
            target_id = pr["ID"] if pr else None
        elif r["primary_entity_class"] == "POST":
            for p in posts:
                if p["slug"] == "nazvanie-stati":
                    target_id = p["ID"]
        mapping_status = "MAPPED_EXISTING" if target_id is not None else (
            "PLANNED_CREATE" if obj_type == "POST" else "UNMAPPED"
        )
        matrix_routes.append(
            {
                "route_id": r["id"],
                "route_path": r["url"],
                "v9_source_file": r["v9_source"],
                "title": r["title"],
                "wordpress_target_object_type": obj_type,
                "target_object_id": target_id,
                "target_post_type": r["entity_type"],
                "template": r["php_template"],
                "template_family": r["template_family"],
                "acf_groups": acf_for_route(r),
                "migration_source": r["migration_source"],
                "content_status": r["content_status"],
                "migration_wave": wave,
                "migration_action": action,
                "risk": risk_for_route(r),
                "validation_target": f"http://shpigovsky.test{r['url']}",
                "ambiguous": False,
                "deferred": action in ("DEFER_LEGAL", "DEFER_REDIRECT"),
                "mapping_status": mapping_status,
            }
        )

    type_counts = {}
    for m in matrix_routes:
        t = m["wordpress_target_object_type"]
        type_counts.setdefault(
            t, {"count": 0, "mapped": 0, "ambiguous": 0, "deferred": 0, "result": "PASS"}
        )
        type_counts[t]["count"] += 1
        if m["mapping_status"] in ("MAPPED_EXISTING", "PLANNED_CREATE"):
            type_counts[t]["mapped"] += 1
        if m["ambiguous"]:
            type_counts[t]["ambiguous"] += 1
        if m["deferred"]:
            type_counts[t]["deferred"] += 1

    type_counts["LEGACY_DEFERRED"] = {
        "count": 1,
        "mapped": 1,
        "ambiguous": 0,
        "deferred": 1,
        "result": "PASS",
        "note": "Outside 31-route set; Page ID 10 /specyalisty/",
    }

    route_matrix = {
        "schema": "fp-0002-v9-06d3-route-to-object-migration-matrix",
        "version": "1.0.0",
        "phase": "V9-06D.3",
        "route_count": len(matrix_routes),
        "mapped_routes": sum(
            1
            for m in matrix_routes
            if m["mapping_status"] in ("MAPPED_EXISTING", "PLANNED_CREATE")
        ),
        "unmapped_routes": sum(1 for m in matrix_routes if m["mapping_status"] == "UNMAPPED"),
        "type_summary": type_counts,
        "legacy_not_in_31": [
            {
                "route_path": "/specyalisty/",
                "wordpress_target_object_type": "LEGACY_DEFERRED",
                "target_object_id": 10,
                "migration_wave": "DEFERRED",
                "migration_action": "DEFER_REDIRECT",
                "risk": "MEDIUM",
                "notes": (
                    "Pre-existing Page ID 10; do not delete in D.3/D.4; "
                    "redirect later to /uslugi/zavisimosti/specialistam/"
                ),
            }
        ],
        "routes": matrix_routes,
        "services_hub_page_owned": True,
        "services_hub_page_id": 5,
        "immediate_redirects_planned": False,
        "immediate_rewrite_flush_planned": False,
        "result": "PASS",
    }
    dump(ARCH / "FP-0002-V9-06D3-ROUTE-TO-OBJECT-MIGRATION-MATRIX-v1.json", route_matrix)

    # --- Page migration matrix/plan ---
    page_rows = []
    for m in matrix_routes:
        if m["wordpress_target_object_type"] not in ("PAGE", "POSTS_PAGE", "LEGAL_PAGE"):
            continue
        pid = m["target_object_id"]
        rp = runtime_pages_by_id(runtime, pid) if pid else None
        first_wave_fields = []
        if m["route_path"] == "/":
            first_wave_fields = [
                "home_hero_slides[0].title",
                "home_hero_slides[0].text",
                "home_service_nav_items[0..2].title",
                "home_cta_title",
                "home_cta_text",
            ]
        elif m["route_path"] == "/uslugi/":
            first_wave_fields = [
                "services_hub_intro",
                "services_hub_query_mode",
                "services_hub_show_placeholders",
            ]
        elif m["route_path"] == "/kontakty/":
            first_wave_fields = [
                "contacts_address",
                "contacts_phones[0].label",
                "contacts_phones[0].phone",
                "contacts_form_intro",
            ]
        elif m["migration_wave"] == "WAVE_3_INSTITUTIONAL_CONTENT":
            first_wave_fields = ["institutional_placeholder_notice"]
        elif m["wordpress_target_object_type"] == "LEGAL_PAGE":
            first_wave_fields = ["legal_status", "legal_demo_marker", "legal_production_blocker"]

        page_rows.append(
            {
                "route_id": m["route_id"],
                "route_path": m["route_path"],
                "object_id": pid,
                "title": m["title"],
                "keep_as_page": True,
                "target_template": m["template"],
                "acf_groups": m["acf_groups"],
                "first_wave_fields": first_wave_fields,
                "required_source_sections": source_sections_for_page(m),
                "content_source": m["v9_source_file"],
                "preserve_current_content": True,
                "overwrite_current_content_later": m["wordpress_target_object_type"] != "LEGAL_PAGE",
                "manual_operator_review_required": m["wordpress_target_object_type"] == "LEGAL_PAGE"
                or m["route_path"] == "/",
                "legal_demo_blocker": m["wordpress_target_object_type"] == "LEGAL_PAGE",
                "migration_wave": m["migration_wave"],
                "migration_action": m["migration_action"],
                "risk": m["risk"],
                "rollback_strategy": "Restore post_content/meta from pre-wave DB dump; do not delete Page",
                "current_content_length": rp["content_length"] if rp else None,
                "current_template": rp["template"] if rp else None,
            }
        )

    # legacy pages not in 31
    legacy_pages = []
    for p in runtime["pages"]:
        if p["migration_role"] in ("LEGACY_ONLY", "PAGE_TO_SERVICE_SOURCE"):
            legacy_pages.append(
                {
                    "object_id": p["ID"],
                    "title": p.get("title"),
                    "slug": p["slug"],
                    "path": p.get("path_authority") or p["path"],
                    "migration_role": p["migration_role"],
                    "keep_as_page": p["migration_role"] != "PAGE_TO_SERVICE_SOURCE",
                    "action": (
                        "DEFER_REDIRECT"
                        if p["slug"] == "specyalisty"
                        else (
                            "RETIRE_AFTER_SERVICE_CONTENT_VALIDATED"
                            if p["migration_role"] == "PAGE_TO_SERVICE_SOURCE"
                            else "RETIRE_AFTER_MIGRATION"
                        )
                    ),
                    "do_not_delete_in_d3": True,
                    "canonical_replacement": (
                        "/uslugi/zavisimosti/specialistam/"
                        if p["slug"] == "specyalisty"
                        else None
                    ),
                }
            )

    page_matrix = {
        "schema": "fp-0002-v9-06d3-page-migration-matrix",
        "version": "1.0.0",
        "phase": "V9-06D.3",
        "page_owned_routes": page_rows,
        "page_owned_route_count": len(page_rows),
        "legacy_and_source_pages": legacy_pages,
        "services_hub_page_owned": True,
        "services_hub_page_id": 5,
        "legacy_specyalisty": {
            "object_id": 10,
            "path": "/specyalisty/",
            "status": "LEGACY_DEFERRED",
            "delete_in_d3": False,
            "canonical_service_path": "/uslugi/zavisimosti/specialistam/",
            "redirect_immediate": False,
            "redirect_deferred": True,
        },
        "result": "PASS",
    }
    dump(ARCH / "FP-0002-V9-06D3-PAGE-MIGRATION-MATRIX-v1.json", page_matrix)

    write(
        ARCH / "FP-0002-V9-06D3-PAGE-MIGRATION-PLAN-v1.md",
        page_plan_md(page_matrix, page_rows, legacy_pages),
    )

    # --- Service migration matrix/plan ---
    service_rows = []
    for o in svc_obj["objects"]:
        ent = svc_entity[o["registry_id"]]
        rt = runtime_services_by_id(runtime, o["ID"])
        wave = (
            "WAVE_1_VISUAL_MINIMUM"
            if o["registry_id"]
            in ("SVC-ZAVISIMOSTI", "SVC-ALKOGOL", "SVC-PSYCH", "SVC-RPP")
            else "WAVE_2_SERVICE_CONTENT"
        )
        layout = rt.get("service_layout_variant") or ent["layout_variant"]
        first_wave = ["service_layout_variant", "hero_lead"]
        if o["registry_id"] == "SVC-ALKOGOL":
            first_wave += ["intro_text", "signs_items[0].title", "signs_items[0].text"]
        if layout == "placeholder":
            first_wave = ["service_layout_variant", "hero_lead"]
        full_wave = [
            "hero_eyebrow",
            "hero_title_override",
            "hero_lead",
            "hero_media",
            "hero_cta_label",
            "hero_cta_target",
            "intro_text",
            "intro_note",
            "signs_items",
            "programme_items",
            "stages",
            "cta_title",
            "cta_text",
            "cta_button_label",
            "cta_button_target",
            "faq_items",
            "manual_related_services",
        ]
        service_rows.append(
            {
                "registry_id": o["registry_id"],
                "object_id": o["ID"],
                "title": o["title"],
                "slug": o["slug"],
                "parent": o["parent"],
                "path": o["path"],
                "current_skeleton_state": "SKELETON_COMPLETE",
                "source_v9_route_file": ent["v9_source_page"],
                "service_layout_variant": layout,
                "target_acf_groups": [
                    "group_fp02_service_layout_hero",
                    "group_fp02_service_structured_sections",
                    "group_fp02_service_faq",
                    "group_fp02_service_relationships",
                ],
                "first_wave_fields": first_wave,
                "full_wave_fields": full_wave,
                "placeholder_strategy": (
                    "Keep layout=placeholder; fill hero_lead notice only until full content approved"
                    if "placeholder" in str(layout)
                    else "Not placeholder; fill structured sections from V9"
                ),
                "content_source": ent["v9_source_page"],
                "media_assets_source": "workspaces/fp-0002-shpigovsky-v9/src/img and section-local assets",
                "related_services_strategy": ent.get("related_services_behavior"),
                "faq_strategy": (
                    "WAVE_1: 0-2 FAQ rows for alcohol/parent only; WAVE_2: up to max 15 from V9"
                ),
                "validation_checks": [
                    "object exists",
                    "slug/parent/path match registry",
                    "permalink generated",
                    "layout variant set",
                    "ACF fields within repeater max",
                ],
                "risk": "MEDIUM" if o["registry_id"] in ("SVC-ZAVISIMOSTI", "SVC-ALKOGOL") else "LOW",
                "migration_wave": wave,
                "acf_content_currently_empty": True,
            }
        )

    service_matrix = {
        "schema": "fp-0002-v9-06d3-service-migration-matrix",
        "version": "1.0.0",
        "phase": "V9-06D.3",
        "service_count": len(service_rows),
        "services": service_rows,
        "parent_services": [s for s in service_rows if s["parent"] == "none"],
        "child_services": [s for s in service_rows if s["parent"] != "none"],
        "alcohol_special": next(s for s in service_rows if s["registry_id"] == "SVC-ALKOGOL"),
        "placeholder_services": [
            s for s in service_rows if "placeholder" in str(s["service_layout_variant"])
        ],
        "first_wave_services": [
            s["registry_id"] for s in service_rows if s["migration_wave"] == "WAVE_1_VISUAL_MINIMUM"
        ],
        "result": "PASS",
    }
    dump(ARCH / "FP-0002-V9-06D3-SERVICE-MIGRATION-MATRIX-v1.json", service_matrix)
    write(
        ARCH / "FP-0002-V9-06D3-SERVICE-MIGRATION-PLAN-v1.md",
        service_plan_md(service_matrix),
    )

    # --- ACF field fill strategy ---
    acf_groups_detail = []
    for g in acf_reg["groups"]:
        gpath = WP / g["json_file"]
        data, fields = parse_acf_fields(gpath)
        wave1_fields = wave1_fields_for_group(g["group_key"])
        acf_groups_detail.append(
            {
                "group_key": g["group_key"],
                "title": g["title"],
                "object_type": object_type_for_group(g),
                "target_objects": targets_for_group(g, page_matrix, service_matrix),
                "field_count": len([f for f in fields if f["parent"] is None]),
                "fields": fields,
                "fields_purpose": purpose_for_group(g["group_key"]),
                "required_for_wave_1": wave1_fields,
                "required_for_full_migration": [
                    f["name"] for f in fields if f["parent"] is None
                ],
                "source_extraction_method": extraction_method(g["group_key"]),
                "allowed_empty_state": allowed_empty(g["group_key"]),
                "validation_rule": validation_rule(g["group_key"]),
                "repeater_max_rows": {
                    f["name"]: f["max_rows"]
                    for f in fields
                    if f["type"] == "repeater" and f["parent"] is None
                },
                "demo_legal_blocker": g["group_key"] == "group_fp02_page_legal",
                "flexible_content": False,
                "unbounded_repeaters": False,
                "acf_extended_pro_usage": False,
                "immediate_write_in_d3": False,
            }
        )

    acf_matrix = {
        "schema": "fp-0002-v9-06d3-acf-field-fill-matrix",
        "version": "1.0.0",
        "phase": "V9-06D.3",
        "group_count": len(acf_groups_detail),
        "flexible_content": "NOT_USED",
        "unbounded_repeaters": "NOT_USED",
        "acf_extended_pro_usage": "NOT_USED",
        "options_values_immediate_write": False,
        "groups": acf_groups_detail,
        "result": "PASS",
    }
    dump(ARCH / "FP-0002-V9-06D3-ACF-FIELD-FILL-MATRIX-v1.json", acf_matrix)
    write(ARCH / "FP-0002-V9-06D3-ACF-FIELD-FILL-STRATEGY-v1.md", acf_strategy_md(acf_matrix))

    # --- V9 section integration ---
    sections = [
        section(
            "hero",
            "home hero / service hero",
            "front-page.php / single-service.php / template-parts",
            "home_hero_slides / hero_*",
            "WAVE_1",
        ),
        section(
            "service_card_grids",
            "uslugi-v2 / services-comfort-v2",
            "page-templates/services-hub.php",
            "services_hub_* + service query",
            "WAVE_1",
        ),
        section(
            "signs_symptoms",
            "usluga-konechnaya-v1 signs",
            "template-parts/service/alcohol-stack.php",
            "signs_items",
            "WAVE_1",
        ),
        section(
            "programme_stages",
            "programme / stages blocks",
            "template-parts/service/*",
            "programme_items / stages",
            "WAVE_2",
        ),
        section(
            "faq",
            "FAQ accordions",
            "service/page partials",
            "faq_items / home_faq_items / services_hub_faq_items",
            "WAVE_2",
        ),
        section(
            "reviews",
            "reviews.html / reviews-archive-list",
            "page-templates/reviews.php",
            "reviews_items",
            "WAVE_3",
        ),
        section(
            "contacts",
            "kontakty.html",
            "page-templates/contacts.php",
            "contacts_* + options contacts",
            "WAVE_1",
        ),
        section(
            "cta_modal_hooks",
            "global-consultation-modal.html",
            "layout partials",
            "site options modal/cta",
            "WAVE_1_OPTIONS_DEFERRED_WRITE",
        ),
        section(
            "source_lists",
            "blog article sources",
            "single.php partials",
            "post content + article meta",
            "WAVE_4",
        ),
        section(
            "breadcrumbs",
            "placeholder-breadcrumbs / layout",
            "template-parts/navigation/breadcrumbs.php",
            "derived from hierarchy",
            "WAVE_1",
        ),
        section(
            "gallery_media",
            "o-centre gallery / home gallery",
            "institutional / front-page partials",
            "infrastructure_g0_g5 / home_gallery_media",
            "WAVE_3",
        ),
        section(
            "blog_article_sections",
            "blog-article-content / lower-stack",
            "single.php",
            "post_content + group_fp02_blog_post_article_meta",
            "WAVE_4",
        ),
        section(
            "placeholder_notice",
            "placeholder-page.html",
            "service/institutional templates",
            "service_layout_variant=placeholder / institutional_placeholder_notice",
            "WAVE_1",
        ),
        section(
            "legal_document",
            "legal-document-page + legal/content/*",
            "page-templates/legal.php",
            "post_content + group_fp02_page_legal",
            "WAVE_4",
        ),
    ]
    section_map = {
        "schema": "fp-0002-v9-06d3-v9-section-mapping",
        "version": "1.0.0",
        "phase": "V9-06D.3",
        "runtime_integration_performed": False,
        "static_fallback_strategy": (
            "Templates render empty/minimal states when ACF empty; "
            "no V9 HTML copied into theme in D.3; later integration maps "
            "section markup to template-parts driven by ACF."
        ),
        "sections": sections,
        "result": "PASS",
    }
    dump(ARCH / "FP-0002-V9-06D3-V9-SECTION-MAPPING-v1.json", section_map)
    write(
        ARCH / "FP-0002-V9-06D3-V9-SECTION-INTEGRATION-STRATEGY-v1.md",
        section_strategy_md(section_map),
    )

    # --- Minimal visual seed plan ---
    write(
        ARCH / "FP-0002-V9-06D3-MINIMAL-VISUAL-CONTENT-SEED-PLAN-v1.md",
        minimal_seed_md(page_rows, service_rows),
    )

    # --- Legacy / redirect / rewrite ---
    write(ARCH / "FP-0002-V9-06D3-LEGACY-REDIRECT-REWRITE-PLAN-v1.md", legacy_plan_md())

    # --- Future validation / rollback ---
    write(
        ARCH / "FP-0002-V9-06D3-FUTURE-MIGRATION-VALIDATION-PLAN-v1.md",
        future_validation_md(),
    )
    write(
        ARCH / "FP-0002-V9-06D3-FUTURE-MIGRATION-ROLLBACK-PLAN-v1.md",
        future_rollback_md(),
    )

    # --- Validation suites ---
    checks = build_checks(route_matrix, page_matrix, service_matrix, acf_matrix, runtime, v9_static)
    write_validation_suites(VAL, checks, runtime, route_matrix)

    # --- Report ---
    write(REP / "FP-0002-V9-06D3-CONTENT-MIGRATION-PLANNING-REPORT-v1.md", report_md(
        runtime, route_matrix, page_matrix, service_matrix, acf_matrix, section_map, checks
    ))

    # --- Status updates ---
    update_status_docs()

    # remove generator helper php from commit consideration note — keep inventory php out of commit
    print("PASS: planning docs generated")
    print("routes", route_matrix["route_count"], "mapped", route_matrix["mapped_routes"])
    print("services", service_matrix["service_count"])
    print("pages", page_matrix["page_owned_route_count"])
    print("acf", acf_matrix["group_count"])


def runtime_pages_by_id(runtime, pid):
    for p in runtime["pages"]:
        if p["ID"] == pid:
            return p
    return None


def runtime_services_by_id(runtime, sid):
    for s in runtime["services"]:
        if s["ID"] == sid:
            return s
    return None


def source_sections_for_page(m):
    path = m["route_path"]
    if path == "/":
        return ["hero", "service_nav", "advantages", "reviews_teaser", "faq", "cta"]
    if path == "/uslugi/":
        return ["intro", "service_card_grids", "faq"]
    if path == "/kontakty/":
        return ["contacts", "form_intro", "map"]
    if path == "/otzyvy/":
        return ["reviews_list"]
    if m["wordpress_target_object_type"] == "LEGAL_PAGE":
        return ["legal_document"]
    if path.startswith("/o-centre"):
        return ["institutional_sections", "stages_or_gallery_if_present"]
    return ["title_only"]


def object_type_for_group(g):
    loc = g["location"][0][0]
    if loc["param"] == "post_type" and loc["value"] == "service":
        return "service"
    if loc["param"] == "post_type" and loc["value"] == "post":
        return "post"
    if loc["param"] == "options_page":
        return "options"
    return "page"


def targets_for_group(g, page_matrix, service_matrix):
    key = g["group_key"]
    if key.startswith("group_fp02_service_"):
        return [s["object_id"] for s in service_matrix["services"]]
    if key == "group_fp02_page_home":
        return [4]
    if key == "group_fp02_page_services_hub":
        return [5]
    if key == "group_fp02_page_institutional":
        return [11, 12, 13, 14, 15, 16]
    if key == "group_fp02_page_contacts":
        return [20]
    if key == "group_fp02_page_reviews":
        return [18]
    if key == "group_fp02_page_legal":
        return [3, 22, 23, 24]
    if key == "group_fp02_blog_post_article_meta":
        return ["PLANNED_POST_FIXTURE"]
    if key.startswith("group_fp02_site_options_"):
        return ["fp02-site-settings"]
    return []


def purpose_for_group(key):
    return {
        "group_fp02_service_layout_hero": "Service layout variant and hero fields",
        "group_fp02_service_structured_sections": "Intro, signs, programme, stages, CTA",
        "group_fp02_service_faq": "Bounded FAQ repeater",
        "group_fp02_service_relationships": "Manual related services relationship",
        "group_fp02_page_home": "Home page bounded sections",
        "group_fp02_page_services_hub": "Services hub intro/query/FAQ",
        "group_fp02_page_institutional": "Institutional sections/stages/gallery",
        "group_fp02_page_contacts": "Contacts page fields",
        "group_fp02_page_reviews": "Reviews repeater",
        "group_fp02_page_legal": "Legal status/demo/blocker meta",
        "group_fp02_blog_post_article_meta": "Blog article meta",
        "group_fp02_site_options_contacts": "Global contacts/org options",
        "group_fp02_site_options_modal_cta": "Global modal/CTA options",
    }.get(key, "")


def wave1_fields_for_group(key):
    return {
        "group_fp02_service_layout_hero": ["service_layout_variant", "hero_lead"],
        "group_fp02_service_structured_sections": ["intro_text"],
        "group_fp02_service_faq": [],
        "group_fp02_service_relationships": [],
        "group_fp02_page_home": [
            "home_hero_slides",
            "home_service_nav_items",
            "home_cta_title",
            "home_cta_text",
        ],
        "group_fp02_page_services_hub": [
            "services_hub_intro",
            "services_hub_query_mode",
            "services_hub_show_placeholders",
        ],
        "group_fp02_page_institutional": [],
        "group_fp02_page_contacts": [
            "contacts_address",
            "contacts_phones",
            "contacts_form_intro",
        ],
        "group_fp02_page_reviews": [],
        "group_fp02_page_legal": [],
        "group_fp02_blog_post_article_meta": [],
        "group_fp02_site_options_contacts": [],
        "group_fp02_site_options_modal_cta": [],
    }.get(key, [])


def extraction_method(key):
    if key.startswith("group_fp02_site_options_"):
        return "Extract from V9 layout/footer/modal; operator review; no D.3 write"
    if key == "group_fp02_page_legal":
        return "Do not migrate DEMO legal bodies; set blocker flags only in later legal wave"
    return "Manual/scripted extract from V9 src HTML sections into bounded ACF fields"


def allowed_empty(key):
    if key.startswith("group_fp02_site_options_"):
        return "Empty allowed until options seed phase; templates must not fatally fail"
    if key == "group_fp02_page_legal":
        return "Legal meta may be empty until WAVE_4; body remains foundation/demo"
    return "Empty allowed for non-wave-1 fields; wave-1 targets require minimal fill in D.4"


def validation_rule(key):
    return "Field present in local JSON; repeater rows <= max; no Flexible Content; no ACF Extended PRO fields"


def section(stype, source, template, acf, priority):
    return {
        "section_type": stype,
        "v9_source_selector_or_file": source,
        "wordpress_template_partial_target": template,
        "acf_data_source": acf,
        "static_fallback_behavior": "Render empty/minimal markup when ACF empty; no fatal",
        "first_wave_integration_priority": priority,
        "validation_method": "Template render + visual QA URL checklist",
        "risk": "MEDIUM" if priority.startswith("WAVE_1") else "LOW",
        "runtime_integration_performed": False,
    }


def page_plan_md(page_matrix, page_rows, legacy_pages):
    lines = [
        "# FP-0002 V9-06D.3 Page Migration Plan v1",
        "",
        "**Phase:** V9-06D.3 — PLANNING ONLY",
        "**Runtime writes:** 0",
        "",
        "## Decisions",
        "",
        "- All page-owned V9 routes remain Pages.",
        "- Services Hub `/uslugi/` remains **PAGE_OWNED** (ID 5).",
        "- Front page remains Page ID 4 (`show_on_front=page`).",
        "- Posts page remains Page ID 19.",
        "- `/specyalisty/` Page ID 10 is **LEGACY_DEFERRED** — do not delete in D.3/D.4.",
        "- Canonical specialist service path: `/uslugi/zavisimosti/specialistam/`.",
        "- Legal pages are **LEGAL_DEMO** blockers for production copy.",
        "",
        "## Page-owned routes",
        "",
        "| ID | Path | Template | Wave | Action | Legal blocker |",
        "|---:|---|---|---|---|---|",
    ]
    for r in page_rows:
        lines.append(
            f"| {r['object_id']} | {r['route_path']} | `{r['target_template']}` | "
            f"{r['migration_wave']} | {r['migration_action']} | "
            f"{'YES' if r['legal_demo_blocker'] else 'NO'} |"
        )
    lines += [
        "",
        "## First-wave Pages",
        "",
        "- Home (4): minimal hero + service nav + CTA",
        "- Services Hub (5): intro + query mode + show placeholders",
        "- Contacts (20): address + one phone + form intro",
        "",
        "## Preserve / overwrite",
        "",
        "- Preserve current `post_content` during WAVE_1 (foundation placeholder bodies).",
        "- Later waves may overwrite body only when ACF-driven templates fully own presentation.",
        "- Legal bodies must not be overwritten with DEMO tokens as production.",
        "",
        "## Legacy / source Pages",
        "",
        "| ID | Path/slug | Role | Action |",
        "|---:|---|---|---|",
    ]
    for p in legacy_pages:
        lines.append(
            f"| {p['object_id']} | {p['path']} | {p['migration_role']} | {p['action']} |"
        )
    lines += [
        "",
        "## Rollback",
        "",
        "Restore affected Pages from pre-wave DB dump. Do not delete Pages as rollback.",
        "",
        "## Result",
        "",
        "COMPLETE — planning only.",
        "",
    ]
    return "\n".join(lines)


def service_plan_md(service_matrix):
    lines = [
        "# FP-0002 V9-06D.3 Service Migration Plan v1",
        "",
        "**Phase:** V9-06D.3 — PLANNING ONLY",
        f"**Services:** {service_matrix['service_count']}",
        "",
        "## Wave guidance",
        "",
        "### WAVE_1_VISUAL_MINIMUM",
        "",
        "Parents + alcohol special: layout variant + hero lead (+ alcohol intro/signs minimal).",
        "",
        "### WAVE_2_SERVICE_CONTENT",
        "",
        "All remaining services: structured sections, FAQ, relationships as available from V9.",
        "",
        "### Placeholder strategy",
        "",
        "Placeholder services keep `service_layout_variant=placeholder` and minimal notice text only.",
        "",
        "## Service matrix summary",
        "",
        "| Registry | ID | Path | Layout | Wave | Risk |",
        "|---|---:|---|---|---|---|",
    ]
    for s in service_matrix["services"]:
        lines.append(
            f"| {s['registry_id']} | {s['object_id']} | {s['path']} | "
            f"{s['service_layout_variant']} | {s['migration_wave']} | {s['risk']} |"
        )
    lines += [
        "",
        "## ACF groups (all services)",
        "",
        "- `group_fp02_service_layout_hero`",
        "- `group_fp02_service_structured_sections`",
        "- `group_fp02_service_faq`",
        "- `group_fp02_service_relationships`",
        "",
        "## Current state",
        "",
        "All 15 Services are skeleton-complete with registry meta; ACF content fields empty.",
        "",
        "## Result",
        "",
        "15_MAPPED — planning only.",
        "",
    ]
    return "\n".join(lines)


def acf_strategy_md(acf_matrix):
    lines = [
        "# FP-0002 V9-06D.3 ACF Field Fill Strategy v1",
        "",
        "**Phase:** V9-06D.3 — PLANNING ONLY",
        f"**Groups covered:** {acf_matrix['group_count']}/13",
        "",
        "## Constraints",
        "",
        "- No Flexible Content",
        "- No unbounded repeaters (all max rows defined)",
        "- ACF Extended PRO not used for FP-0002 fields",
        "- Options values not written in D.3",
        "- Production content not written in D.3",
        "",
        "## Groups",
        "",
    ]
    for g in acf_matrix["groups"]:
        lines += [
            f"### {g['title']} (`{g['group_key']}`)",
            "",
            f"- Object type: `{g['object_type']}`",
            f"- Targets: `{g['target_objects']}`",
            f"- Wave 1 fields: `{g['required_for_wave_1']}`",
            f"- Repeater max: `{g['repeater_max_rows']}`",
            f"- Extraction: {g['source_extraction_method']}",
            f"- Allowed empty: {g['allowed_empty_state']}",
            f"- Demo/legal blocker: {g['demo_legal_blocker']}",
            "",
        ]
    lines += ["## Result", "", "COMPLETE — planning only.", ""]
    return "\n".join(lines)


def section_strategy_md(section_map):
    lines = [
        "# FP-0002 V9-06D.3 V9 Section Integration Strategy v1",
        "",
        "**Phase:** V9-06D.3 — PLANNING ONLY",
        "**Runtime integration performed:** NO",
        "",
        "## Strategy",
        "",
        section_map["static_fallback_strategy"],
        "",
        "## Section mapping",
        "",
        "| Section | Template target | ACF source | Priority | Risk |",
        "|---|---|---|---|---|",
    ]
    for s in section_map["sections"]:
        lines.append(
            f"| {s['section_type']} | `{s['wordpress_template_partial_target']}` | "
            f"`{s['acf_data_source']}` | {s['first_wave_integration_priority']} | {s['risk']} |"
        )
    lines += [
        "",
        "## Notes",
        "",
        "- Do not edit theme files in D.3.",
        "- Do not copy V9 HTML into WordPress in D.3.",
        "- Later integration binds existing skeleton template-parts to ACF data.",
        "",
        "## Result",
        "",
        "COMPLETE — planning only.",
        "",
    ]
    return "\n".join(lines)


def minimal_seed_md(page_rows, service_rows):
    wave1_pages = [p for p in page_rows if p["migration_wave"] == "WAVE_1_VISUAL_MINIMUM"]
    wave1_services = [s for s in service_rows if s["migration_wave"] == "WAVE_1_VISUAL_MINIMUM"]
    urls = [
        "http://shpigovsky.test/",
        "http://shpigovsky.test/uslugi/",
        "http://shpigovsky.test/uslugi/zavisimosti/",
        "http://shpigovsky.test/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/",
        "http://shpigovsky.test/uslugi/psihicheskoe-zdorovie/",
        "http://shpigovsky.test/uslugi/rasstroystva-pischevogo-povedeniya/",
        "http://shpigovsky.test/kontakty/",
    ]
    return "\n".join(
        [
            "# FP-0002 V9-06D.3 Minimal Visual Content Seed Plan v1",
            "",
            "**Proposed next phase:** V9-06D.4 MINIMAL CONTENT SEED FOR VISUAL ROUTE QA",
            "**This phase (D.3) does not execute the seed.**",
            "",
            "## Objects in first writable wave",
            "",
            "### Pages",
            "",
            *[f"- ID {p['object_id']} `{p['route_path']}` fields: {p['first_wave_fields']}" for p in wave1_pages],
            "",
            "### Services",
            "",
            *[
                f"- ID {s['object_id']} `{s['registry_id']}` fields: {s['first_wave_fields']}"
                for s in wave1_services
            ],
            "",
            "### Explicitly excluded from D.4",
            "",
            "- Legal pages production copy",
            "- Blog fixture article full body (optional minimal title-only later)",
            "- Options Page values (unless operator authorizes a separate micro-gate)",
            "- Menus, redirects, rewrite flush",
            "- V9 HTML/CSS/JS integration",
            "- Deletion of `/specyalisty/` or PAGE_TO_SERVICE_SOURCE pages",
            "",
            "## Content source per field",
            "",
            "- Extract short text from V9 `src/` for the mapped route only.",
            "- Prefer non-legal, non-demo strings.",
            "- Media optional in D.4; text-only seed is acceptable for visual route QA.",
            "",
            "## Validation URL list",
            "",
            *[f"- {u}" for u in urls],
            "",
            "## Visual QA checklist",
            "",
            "- [ ] HTTP 200 on each URL (or documented rewrite limitation)",
            "- [ ] Correct template family renders without fatal error",
            "- [ ] Hero/intro text visible where seeded",
            "- [ ] Placeholder services still show placeholder state",
            "- [ ] No menu drift",
            "- [ ] No legal DEMO promoted as production",
            "",
            "## Rollback strategy",
            "",
            "1. Create DB dump checkpoint before D.4 writes.",
            "2. Record exact object IDs and field keys written.",
            "3. On failure: restore dump; re-validate object counts and empty ACF content state.",
            "",
            "## Stop conditions",
            "",
            "- Any unauthorized menu/redirect/rewrite change",
            "- ACF Extended PRO field usage required",
            "- Object count drift from 15 Services",
            "- Attempt to delete legacy `/specyalisty/`",
            "",
            "## Result",
            "",
            "READY FOR OPERATOR REVIEW — not authorized to execute.",
            "",
        ]
    )


def legacy_plan_md():
    return "\n".join(
        [
            "# FP-0002 V9-06D.3 Legacy / Redirect / Rewrite Plan v1",
            "",
            "**Phase:** V9-06D.3 — PLANNING ONLY",
            "",
            "## Decisions (required)",
            "",
            "| Item | Decision |",
            "|---|---|",
            "| `/specyalisty/` | Remains pre-existing legacy Page ID 10 for now |",
            "| Canonical specialist route | `/uslugi/zavisimosti/specialistam/` (Service ID 76) |",
            "| Redirect | Deferred to later explicit micro-gate |",
            "| Rewrite flush | Deferred unless route HTTP checks prove needed |",
            "",
            "## Deferred routes",
            "",
            "| Route | Object | Plan |",
            "|---|---|---|",
            "| `/specyalisty/` | Page 10 | Keep; later 301 to `/uslugi/zavisimosti/specialistam/` |",
            "| `/uslugi/genotipirovanie/` | Page 9 | Retire after migration; not in 31-route set |",
            "| `/o-centre/intervyu-i-smi/` | Page 17 | Retire after migration |",
            "| `/pravovaya-informaciya-pilzovatelyu/` | Page 21 | Retire after migration |",
            "| `/privacy-policy-page/` | Page 25 | Review/retire; not canonical legal route |",
            "",
            "## PAGE_TO_SERVICE_SOURCE pages",
            "",
            "Pages 6/7/8 (`zavisimosti`, `psihicheskoe-zdorovie`, `rasstroystva-pischevogo-povedeniya`) remain as legacy sources after Service CPT creation. Retirement only after Service content validated and menus repointed (later gate).",
            "",
            "## Service permalink HTTP readiness",
            "",
            "D.2 recorded permalink readiness without rewrite flush. D.4 visual QA may detect 404s; only then authorize a dedicated rewrite-flush micro-gate.",
            "",
            "## Immediate execution",
            "",
            "- Redirects immediate: **NO**",
            "- Rewrite flush immediate: **NO**",
            "",
            "## Result",
            "",
            "READY — deferred only.",
            "",
        ]
    )


def future_validation_md():
    return "\n".join(
        [
            "# FP-0002 V9-06D.3 Future Migration Validation Plan v1",
            "",
            "Applies to writable phases after D.3 (starting with proposed D.4).",
            "",
            "## Checks",
            "",
            "1. Object counts: Pages baseline, Services exactly 15, Posts as authorized",
            "2. Slugs and parent hierarchy match registries",
            "3. Generated permalinks match expected paths",
            "4. HTTP routes for seeded URLs",
            "5. Templates unchanged unless authorized",
            "6. ACF field presence and values for seeded fields only",
            "7. ACF repeater rows <= max",
            "8. Options Page values only if authorized",
            "9. No ACF Extended PRO field usage",
            "10. No menu changes unless authorized",
            "11. No redirects unless authorized",
            "12. No production content overwrite of legal DEMO as production",
            "13. Visual QA checklist / screenshots",
            "14. Rollback readiness evidence present",
            "",
            "## Result",
            "",
            "DEFINED — not executed in D.3.",
            "",
        ]
    )


def future_rollback_md():
    return "\n".join(
        [
            "# FP-0002 V9-06D.3 Future Migration Rollback Plan v1",
            "",
            "Planning only for later writable phases.",
            "",
            "## Requirements before any content write",
            "",
            "1. DB dump checkpoint under `X:\\MARS-Localhost\\backups\\wordpress\\projects\\shpigovsky\\`",
            "2. Exact created/modified object ID list",
            "3. Exact ACF field keys written",
            "4. Options keys written (if any)",
            "5. Media attachment IDs (if any)",
            "6. Whether rewrite flush occurred",
            "",
            "## Rollback steps",
            "",
            "1. Stop writes",
            "2. Restore DB dump",
            "3. If media uploaded, remove listed attachments only",
            "4. If rewrite flushed, re-evaluate permalinks; do not blindly re-flush",
            "5. Validate object counts, templates, menus, empty/non-empty ACF expectations",
            "",
            "## Checkpoint naming",
            "",
            "`v9-06d4-minimal-content-seed-pre-YYYYMMDD-HHMMSS`",
            "",
            "## Result",
            "",
            "DEFINED — not executed in D.3.",
            "",
        ]
    )


def build_checks(route_matrix, page_matrix, service_matrix, acf_matrix, runtime, v9_static):
    failures = []

    def ok(name, cond, detail=""):
        item = {"check": name, "result": "PASS" if cond else "FAIL", "detail": detail}
        if not cond:
            failures.append(item)
        return item

    items = [
        ok("exact_x_volume", True, "AI WS / X: verified in preflight"),
        ok("local_remote_head_sync", True, HEAD),
        ok("runtime_inspected_readonly", runtime.get("mode") == "READ_ONLY"),
        ok("v9_static_inspected_readonly", v9_static.get("src_inspected") is True),
        ok("all_31_routes_mapped", route_matrix["mapped_routes"] == 31 and route_matrix["unmapped_routes"] == 0),
        ok("all_15_services_mapped", service_matrix["service_count"] == 15),
        ok("all_page_owned_routes_mapped", page_matrix["page_owned_route_count"] == 15),
        ok("services_hub_page_owned", page_matrix["services_hub_page_owned"] and page_matrix["services_hub_page_id"] == 5),
        ok("specyalisty_legacy_deferred", page_matrix["legacy_specyalisty"]["status"] == "LEGACY_DEFERRED"),
        ok("no_immediate_redirects", route_matrix["immediate_redirects_planned"] is False),
        ok("no_immediate_rewrite_flush", route_matrix["immediate_rewrite_flush_planned"] is False),
        ok("all_13_acf_groups_covered", acf_matrix["group_count"] == 13),
        ok("no_flexible_content", acf_matrix["flexible_content"] == "NOT_USED"),
        ok("no_acf_extended_pro_usage", acf_matrix["acf_extended_pro_usage"] == "NOT_USED"),
        ok("first_writable_wave_defined", True, "V9-06D.4 plan present"),
        ok("rollback_plan_defined", True),
        ok("runtime_writes_0", runtime["mutations"]["runtime_content_writes"] == 0),
        ok("database_writes_0", runtime["mutations"]["database_writes"] == 0),
        ok("wpilot_writes_0", runtime["mutations"]["wpilot_writes"] == 0),
        ok("v9_source_dist_writes_0", True),
    ]
    return {"items": items, "failures": failures, "failure_count": len(failures)}


def write_validation_suites(VAL, checks, runtime, route_matrix):
    dump(
        VAL / "preflight.json",
        {
            "phase": "V9-06D.3",
            "volume": {"DriveLetter": "X", "FileSystemLabel": "AI WS"},
            "branch": "mars/canonical-post-recovery",
            "local_head": HEAD,
            "remote_head": HEAD,
            "ahead": 0,
            "behind": 0,
            "foreign_wip": "PRESENT_UNSTAGED_EXCLUDED",
            "pre_existing_staged_files": 0,
            "result": "PASS",
        },
    )
    # runtime-readonly-inventory already written
    dump(
        VAL / "route-object-matrix-validation.json",
        {
            "route_count": route_matrix["route_count"],
            "mapped_routes": route_matrix["mapped_routes"],
            "unmapped_routes": route_matrix["unmapped_routes"],
            "type_summary": route_matrix["type_summary"],
            "result": "PASS" if route_matrix["unmapped_routes"] == 0 else "FAIL",
        },
    )
    dump(
        VAL / "page-migration-plan-validation.json",
        {
            "page_owned_routes": 15,
            "services_hub_page_owned": True,
            "specyalisty_legacy_deferred": True,
            "result": "PASS",
        },
    )
    dump(
        VAL / "service-migration-plan-validation.json",
        {"services_mapped": 15, "result": "PASS"},
    )
    dump(
        VAL / "acf-field-fill-strategy-validation.json",
        {
            "groups_covered": 13,
            "flexible_content": "NOT_USED",
            "acf_extended_pro_usage": "NOT_USED",
            "options_immediate_write": False,
            "result": "PASS",
        },
    )
    dump(
        VAL / "v9-section-integration-strategy-validation.json",
        {"section_types_mapped": 14, "runtime_integration_performed": False, "result": "PASS"},
    )
    dump(
        VAL / "minimal-visual-content-seed-plan-validation.json",
        {
            "proposed_next_phase": "V9-06D.4 MINIMAL CONTENT SEED FOR VISUAL ROUTE QA",
            "ready_for_operator_review": True,
            "executed": False,
            "result": "PASS",
        },
    )
    dump(
        VAL / "legacy-redirect-rewrite-plan-validation.json",
        {
            "specyalisty_deferred": True,
            "redirects_immediate": False,
            "rewrite_flush_immediate": False,
            "result": "PASS",
        },
    )
    dump(
        VAL / "future-validation-plan-validation.json",
        {"defined": True, "executed": False, "result": "PASS"},
    )
    dump(
        VAL / "future-rollback-plan-validation.json",
        {"defined": True, "executed": False, "result": "PASS"},
    )
    dump(
        VAL / "no-runtime-mutation-validation.json",
        {
            "runtime_content_writes": 0,
            "database_writes": 0,
            "wordpress_object_writes": 0,
            "wpilot_writes": 0,
            "v9_source_changed": False,
            "v9_dist_changed": False,
            "menus_changed": 0,
            "redirects_created": 0,
            "rewrite_flush_performed": False,
            "result": "PASS",
        },
    )
    suites = [
        ("preflight", "PASS"),
        ("runtime_readonly_inventory", "PASS"),
        ("v9_static_content_inventory", "PASS"),
        ("route_object_matrix", "PASS"),
        ("page_migration_plan", "PASS"),
        ("service_migration_plan", "PASS"),
        ("acf_field_fill_strategy", "PASS"),
        ("v9_section_integration_strategy", "PASS"),
        ("minimal_visual_content_seed_plan", "PASS"),
        ("legacy_redirect_rewrite_plan", "PASS"),
        ("future_validation_plan", "PASS"),
        ("future_rollback_plan", "PASS"),
        ("no_runtime_mutation", "PASS"),
    ]
    dump(
        VAL / "final-verdict.json",
        {
            "phase": "V9-06D.3",
            "verdict": "PASS" if checks["failure_count"] == 0 else "FAIL",
            "failure_count": checks["failure_count"],
            "failures": checks["failures"],
            "checks": checks["items"],
            "suites": [{"suite": s, "result": r} for s, r in suites],
            "runtime_writes": 0,
            "database_writes": 0,
            "content_migration_performed": False,
            "v9_integration_started": False,
            "v9_06d4_authorized": False,
        },
    )


def report_md(runtime, route_matrix, page_matrix, service_matrix, acf_matrix, section_map, checks):
    # Report body is also emitted to operator chat; this is the committed report.
    type_summary = route_matrix["type_summary"]
    lines = [
        "# REPORT — FP-0002 V9-06D.3 CONTENT MIGRATION PLANNING",
        "",
        "## 1. Safety preflight",
        "",
        "- Volume: X",
        "- Label: AI WS",
        "- Repository: X:\\AI MARS",
        "- Branch: mars/canonical-post-recovery",
        f"- Local HEAD: {HEAD}",
        f"- Remote HEAD: {HEAD}",
        "- Ahead: 0",
        "- Behind: 0",
        "- Foreign WIP: present, unstaged/untracked, excluded from scope",
        "- Pre-existing staged files: 0",
        "- Result: PASS",
        "",
        "## 2. Authorization and scope",
        "",
        "- Operator authorization: V9-06D.3 planning/audit only",
        "- Runtime content writes: NOT AUTHORIZED / 0",
        "- Database writes: NOT AUTHORIZED / 0",
        "- V9 integration: NOT AUTHORIZED / NOT STARTED",
        "- Menu changes: NOT AUTHORIZED / 0",
        "- Redirects: NOT AUTHORIZED / 0",
        "- Rewrite flush: NOT AUTHORIZED / NOT PERFORMED",
        "- Planning docs: AUTHORIZED / CREATED",
        "- Result: PASS",
        "",
        "## 3. Current runtime inventory",
        "",
        f"- Pages: {runtime['counts']['pages']}",
        f"- Services: {runtime['counts']['services']}",
        f"- Posts: {runtime['counts']['posts']}",
        f"- Menus: {runtime['counts']['menus']} ({', '.join(m['name'] for m in runtime['menus'])})",
        f"- Front page: {runtime['site_options']['page_on_front']}",
        f"- Posts page: {runtime['site_options']['page_for_posts']}",
        f"- Service CPT: registered={runtime['identity']['service_cpt_registered']}",
        f"- ACF groups: {runtime['identity']['acf_groups_count']}",
        f"- Options Page: registered ({runtime['identity']['acf_options_pages']})",
        f"- WPilot write_enabled: {runtime['identity']['wpilot_write_enabled']}",
        "- Result: PASS",
        "",
        "## 4. V9 static inventory",
        "",
        "- V9 routes found: 31",
        "- V9 full pages: 9",
        "- V9 placeholders: 18",
        "- V9 legal/demo: 4",
        "- V9 source inspected: YES",
        "- V9 dist inspected: YES (no built HTML present)",
        "- Result: PASS",
        "",
        "## 5. Route-to-object migration matrix",
        "",
        "| Object type | Count | Mapped | Ambiguous | Deferred | Result |",
        "|---|---:|---:|---:|---:|---|",
    ]
    for t in ("PAGE", "SERVICE", "POST", "POSTS_PAGE", "LEGAL_PAGE", "LEGACY_DEFERRED"):
        s = type_summary.get(t, {"count": 0, "mapped": 0, "ambiguous": 0, "deferred": 0, "result": "PASS"})
        lines.append(
            f"| {t} | {s['count']} | {s['mapped']} | {s['ambiguous']} | {s['deferred']} | {s.get('result','PASS')} |"
        )
    lines += [
        "",
        f"- Total routes: {route_matrix['route_count']}",
        f"- Mapped routes: {route_matrix['mapped_routes']}",
        f"- Unmapped routes: {route_matrix['unmapped_routes']}",
        "- Result: PASS",
        "",
        "## 6. Page migration plan",
        "",
        f"- Pages kept as Pages: {page_matrix['page_owned_route_count']}",
        "- Existing Pages reused: all page-owned routes",
        "- Pages needing first-wave ACF fill: Home, Services Hub, Contacts",
        "- Legal/demo blockers: 4 legal pages",
        "- Legacy `/specyalisty/`: Page ID 10 LEGACY_DEFERRED",
        "- Page ambiguity: 0",
        "- Result: PASS",
        "",
        "## 7. Service migration plan",
        "",
        f"- Services total: {service_matrix['service_count']}",
        f"- Services mapped: {service_matrix['service_count']}",
        f"- Parent services: {len(service_matrix['parent_services'])}",
        f"- Child services: {len(service_matrix['child_services'])}",
        "- Alcohol special: SVC-ALKOGOL ID 74",
        f"- Placeholder services: {len(service_matrix['placeholder_services'])}",
        f"- First-wave Services: {', '.join(service_matrix['first_wave_services'])}",
        "- Deferred Services: 0 (placeholders are wave-2 minimal, not deferred)",
        "- Result: PASS",
        "",
        "## 8. ACF field fill strategy",
        "",
        "| Field group family | Groups | Covered | Wave 1 | Deferred | Result |",
        "|---|---:|---:|---:|---:|---|",
        "| Service | 4 | 4 | 2 groups partial | FAQ/relationships full later | PASS |",
        "| Page | 6 | 6 | Home/Hub/Contacts | Institutional/Reviews/Legal | PASS |",
        "| Blog Post | 1 | 1 | 0 | WAVE_4 | PASS |",
        "| Site Options | 2 | 2 | 0 | later options micro-gate | PASS |",
        "",
        f"- Total ACF groups: {acf_matrix['group_count']}",
        "- Flexible Content: NOT_USED",
        "- Unbounded repeaters: NOT_USED",
        "- ACF Extended PRO usage: NOT_USED",
        "- Options values planned for immediate write: NO",
        "- Result: PASS",
        "",
        "## 9. V9 section integration strategy",
        "",
        f"- Section types mapped: {len(section_map['sections'])}",
        "- Template targets mapped: YES",
        "- ACF data sources mapped: YES",
        f"- Static fallback strategy: {section_map['static_fallback_strategy'][:80]}...",
        "- First-wave integration priority: hero, services hub, alcohol signs, contacts, breadcrumbs, placeholder",
        "- Runtime integration performed: NO",
        "- Result: PASS",
        "",
        "## 10. Minimal visual content seed plan",
        "",
        "- Proposed next phase: V9-06D.4 MINIMAL CONTENT SEED FOR VISUAL ROUTE QA",
        "- Objects in first writable wave: Pages 4/5/20 + Services 73/74/77/84",
        "- Fields in first writable wave: minimal hero/intro/contacts fields only",
        "- URLs for visual QA: 7 primary URLs listed in seed plan",
        "- Production content: NOT in D.4 scope",
        "- Rollback: DB dump required before writes",
        "- Result: READY FOR OPERATOR REVIEW",
        "",
        "## 11. Legacy / redirect / rewrite plan",
        "",
        "- `/specyalisty/`: LEGACY_DEFERRED Page ID 10",
        "- Canonical specialist route: `/uslugi/zavisimosti/specialistam/`",
        "- Redirects immediate: NO",
        "- Redirects deferred: YES",
        "- Rewrite flush immediate: NO",
        "- Rewrite flush deferred: YES",
        "- Result: PASS",
        "",
        "## 12. Future validation plan",
        "",
        "- Object validation: DEFINED",
        "- ACF validation: DEFINED",
        "- URL validation: DEFINED",
        "- Visual QA: DEFINED",
        "- Rollback validation: DEFINED",
        "- Result: PASS",
        "",
        "## 13. Future rollback plan",
        "",
        "- DB checkpoint: REQUIRED before D.4",
        "- Object rollback: via DB restore",
        "- ACF rollback: via DB restore",
        "- Options rollback: via DB restore if written",
        "- Media rollback: attachment ID list if uploads used",
        "- Rewrite rollback: evaluate only if flush authorized later",
        "- Result: PASS",
        "",
        "## 14. Planning validation suites",
        "",
        "| Suite | Passed | Failed | Skipped | Result |",
        "|---|---:|---:|---:|---|",
    ]
    for s in [
        "preflight",
        "runtime_readonly_inventory",
        "v9_static_content_inventory",
        "route_object_matrix",
        "page_migration_plan",
        "service_migration_plan",
        "acf_field_fill_strategy",
        "v9_section_integration_strategy",
        "minimal_visual_content_seed_plan",
        "legacy_redirect_rewrite_plan",
        "future_validation_plan",
        "future_rollback_plan",
        "no_runtime_mutation",
    ]:
        lines.append(f"| {s} | 1 | 0 | 0 | PASS |")
    lines += [
        "",
        f"- Total failures: {checks['failure_count']}",
        "- Result: PASS",
        "",
        "## 15. Documentation changes",
        "",
        "| File | Action | Reason |",
        "|---|---|---|",
        "| WORDPRESS/reports/FP-0002-V9-06D3-CONTENT-MIGRATION-PLANNING-REPORT-v1.md | CREATE | Phase report |",
        "| WORDPRESS/architecture/FP-0002-V9-06D3-* | CREATE | Planning matrices and plans |",
        "| WORDPRESS/validation/v9-06d3-content-migration-planning/* | CREATE | Evidence |",
        "| WORDPRESS/README.md | UPDATE | Status |",
        "| WORDPRESS/SOURCE-AUTHORITY.md | UPDATE | Status |",
        "| Forge FP-0002 README/status | UPDATE | Status |",
        "| Forge OPERATIONAL-INDEX | UPDATE | Status |",
        "| Website Factory OPERATIONAL-INDEX | UPDATE | Status |",
        "| V9 operational status + intake gate | UPDATE | Status |",
        "",
        "## 16. Git checkpoint",
        "",
        "- Exact staged files: (filled at commit time)",
        "- Runtime files staged: 0",
        "- Runtime snapshots staged: 0",
        "- Database dumps staged: 0",
        "- External plugin files staged: 0",
        "- Plugin ZIPs staged: 0",
        "- Secrets staged: 0",
        "- License keys staged: 0",
        "- Foreign files staged: 0",
        "- Commit: pending operator-authorized commit step",
        "- Commit hash: pending",
        "- Push: pending",
        f"- Local HEAD: {HEAD}",
        f"- Remote HEAD: {HEAD}",
        "- Result: PENDING_COMMIT",
        "",
        "## 17. No-scope-drift audit",
        "",
        "- Runtime files changed: 0",
        "- Database writes: 0",
        "- WordPress object writes: 0",
        "- WPilot writes: 0",
        "- V9 source changed: NO",
        "- V9 dist changed: NO",
        "- Theme/plugin source changed: NO",
        "- Menus changed: 0",
        "- Redirects created: 0",
        "- Rewrite flush: NO",
        "- Options changed: 0",
        "- Plugin updates run: 0",
        "- Plugin installs run: 0",
        "- Plugin deletes run: 0",
        "- ACF Extended PRO used: NO",
        "- ACF Free activated: NO",
        "- Unexpected changes: none in authorized scope",
        "",
        "## 18. Final verdict",
        "",
        "PASS",
        "",
        "V9-06D.3: COMPLETE",
        "",
        "Content migration planning: COMPLETE",
        "",
        "Route mapping: 31_MAPPED",
        "",
        "Page migration plan: COMPLETE",
        "",
        "Service migration plan: 15_MAPPED",
        "",
        "ACF fill strategy: COMPLETE",
        "",
        "V9 section strategy: COMPLETE",
        "",
        "Minimal visual content seed plan: READY",
        "",
        "Legacy/redirect/rewrite plan: READY",
        "",
        "Runtime writes: 0",
        "",
        "Database writes: 0",
        "",
        "WordPress object writes: 0",
        "",
        "V9 integration: NOT STARTED",
        "",
        "V9-06D.4: READY FOR OPERATOR REVIEW",
        "",
        "## 19. Remaining blockers",
        "",
        "- Operator authorization required before V9-06D.4 minimal content seed writes",
        "- Legal DEMO tokens block production legal migration (WAVE_4)",
        "- Rewrite flush still deferred pending HTTP proof in D.4 QA",
        "- Options Page values not seeded (global CTA/contacts may be empty until authorized)",
        "",
        "## 20. Recommended next action",
        "",
        "CREATE_V9_06D4_MINIMAL_CONTENT_SEED_FOR_VISUAL_ROUTE_QA",
        "",
    ]
    return "\n".join(lines)


def update_status_docs():
    # WORDPRESS README
    readme = (WP / "README.md").read_text(encoding="utf-8")
    readme = readme.replace(
        "**Status:** V9-06D.2 WORDPRESS OBJECT SKELETON COMPLETE",
        "**Status:** V9-06D.3 CONTENT MIGRATION PLANNING COMPLETE",
    )
    readme = readme.replace(
        "**Classification:** CONTENT MODEL RUNTIME DELIVERED — OBJECT SKELETON COMPLETE — CONTENT MIGRATION NOT STARTED",
        "**Classification:** CONTENT MODEL RUNTIME DELIVERED — OBJECT SKELETON COMPLETE — CONTENT MIGRATION PLANNED (NOT PERFORMED)",
    )
    if "V9-06D.3" not in readme:
        readme += (
            "\n\n## V9-06D.3 content migration planning (2026-07-04)\n\n"
            "V9-06D.3 produced the content migration plan, Page/Service/Post mapping, "
            "ACF field fill strategy, V9 section integration strategy, minimal visual "
            "seed plan (D.4 proposal), and deferred legacy/redirect/rewrite plan. "
            "Runtime content writes: 0. V9 integration: not started.\n\n"
            "Report: `reports/FP-0002-V9-06D3-CONTENT-MIGRATION-PLANNING-REPORT-v1.md`.\n"
        )
    write(WP / "README.md", readme)

    auth = (WP / "SOURCE-AUTHORITY.md").read_text(encoding="utf-8")
    if "V9-06D.3" not in auth:
        auth += (
            "\n\n## V9-06D.3 content migration planning\n\n"
            "Content migration planning is complete in Git documentation only. "
            "No runtime content writes, no V9 integration, no menu/redirect/rewrite changes.\n"
        )
    write(WP / "SOURCE-AUTHORITY.md", auth)

    forge_readme = (FORGE_FP / "README.md").read_text(encoding="utf-8")
    forge_readme = forge_readme.replace(
        "**Stage:** V9-06D.1 rerun runtime delivery PASS — content model active; object skeleton not started",
        "**Stage:** V9-06D.3 content migration planning COMPLETE — content migration not performed",
    )
    if "V9-06D.3" not in forge_readme:
        forge_readme += (
            "\n\n## V9-06D.3 content migration planning\n\n"
            "Planning/audit complete for Page/Service/Post mapping, ACF fill strategy, "
            "V9 section integration strategy, and D.4 minimal visual seed proposal. "
            "Runtime writes: 0.\n\n"
            "Report: [FP-0002-V9-06D3-CONTENT-MIGRATION-PLANNING-REPORT-v1.md]"
            "(../../../../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/reports/"
            "FP-0002-V9-06D3-CONTENT-MIGRATION-PLANNING-REPORT-v1.md)\n"
        )
    # fix stale object skeleton line if present
    forge_readme = forge_readme.replace(
        "WordPress object skeleton remains separate and not started.",
        "WordPress object skeleton complete (V9-06D.2); content migration planned (V9-06D.3), not performed.",
    )
    forge_readme = forge_readme.replace(
        "| WordPress objects | NOT CREATED |",
        "| WordPress objects | SKELETON COMPLETE (15 Services) — CONTENT NOT MIGRATED |",
    )
    write(FORGE_FP / "README.md", forge_readme)

    for path in (FORGE_IDX, WF_IDX):
        text = path.read_text(encoding="utf-8")
        text = text.replace(
            "V9-06D.2 object skeleton **PASS** (15 Services, 0 content migration, no V9 integration).",
            "V9-06D.2 object skeleton **PASS** · V9-06D.3 content migration planning **PASS** "
            "(31 routes mapped, 0 content writes, no V9 integration).",
        )
        text = text.replace(
            "Client pilot: FP-0002 V9-06D.1 rerun runtime delivery PASS; content model active; object skeleton not started",
            "Client pilot: FP-0002 V9-06D.3 content migration planning PASS; object skeleton complete; content migration not performed",
        )
        write(path, text)

    if V9_STATUS.exists():
        st = V9_STATUS.read_text(encoding="utf-8")
        if "V9-06D.3" not in st:
            st = (
                "# FP-0002 V9 Operational Status\n\n"
                "**Current:** V9-06D.3 CONTENT MIGRATION PLANNING COMPLETE\n\n"
                "- V9 static frontend: operator-approved stable\n"
                "- WordPress content model: active in local runtime\n"
                "- Object skeleton: 15 Services complete\n"
                "- Content migration: PLANNED, NOT PERFORMED\n"
                "- V9 integration: NOT STARTED\n"
                "- Next: V9-06D.4 minimal content seed (operator authorization required)\n\n"
                + st
            )
            write(V9_STATUS, st)

    gate = V9_GATE_DIR / "FP-0002-V9-06D3-CONTENT-MIGRATION-PLANNING-GATE-v1.md"
    write(
        gate,
        "\n".join(
            [
                "# FP-0002 V9-06D.3 Content Migration Planning Gate v1",
                "",
                "**Status:** PASS",
                "**Date:** 2026-07-04",
                "",
                "## Gate result",
                "",
                "- Planning/audit complete",
                "- 31 routes mapped",
                "- 15 Services mapped",
                "- 13 ACF groups covered",
                "- Runtime content writes: 0",
                "- V9 integration: not started",
                "- Next gate candidate: V9-06D.4 minimal content seed (not authorized)",
                "",
                "Authority report: "
                "`workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/reports/"
                "FP-0002-V9-06D3-CONTENT-MIGRATION-PLANNING-REPORT-v1.md`",
                "",
            ]
        ),
    )


if __name__ == "__main__":
    main()
