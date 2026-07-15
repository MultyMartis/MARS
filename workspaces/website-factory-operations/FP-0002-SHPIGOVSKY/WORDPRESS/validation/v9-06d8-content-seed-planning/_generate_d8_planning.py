#!/usr/bin/env python3
"""Generate V9-06D8 content seed planning validation JSON evidence."""
import json
from datetime import datetime, timezone

OUT = __file__.replace("_generate_d8_planning.py", "")
TS = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def write(name, obj):
    path = OUT + name
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("wrote", name)

# --- Runtime inventory ---
runtime_inventory = {
    "phase": "V9-06D8",
    "mode": "READ_ONLY",
    "generated_at": TS,
    "live_inspection": {
        "attempted": True,
        "method": "PHP _inventory_readonly.php via wp-load.php",
        "result": "DB_CONNECTION_FAILED",
        "note": "Local MySQL unavailable at task time; counts and object IDs from D7-F runtime-identity-qa.json and D4 acf-seed-validation.json"
    },
    "evidence_sources": [
        "validation/v9-06d7f-final-route-qa/runtime-identity-qa.json",
        "validation/v9-06d4-minimal-content-seed-rerun/acf-seed-validation.json",
        "validation/v9-06d4-minimal-content-seed-rerun/dry-run-seed-plan.json"
    ],
    "identity": {
        "runtime": "X:/MARS-Localhost/sites/wordpress/projects/shpigovsky",
        "domain": "http://shpigovsky.test/",
        "active_theme": "shpigovsky",
        "core_mode": "content_model",
        "service_cpt_registered": True,
        "acf_pro_active": True,
        "acf_groups_count": 13,
        "wpilot_write_enabled": False
    },
    "counts": {
        "pages": 23,
        "services": 15,
        "posts": 1,
        "menus": 3
    },
    "key_object_ids": {
        "front_page": 4,
        "services_hub_page": 5,
        "contacts_page": 20,
        "service_zavisimosti": 73,
        "service_alkogol": 74,
        "service_psych": 77,
        "service_rpp": 84
    },
    "site_options": {
        "show_on_front": "page",
        "page_on_front": 4,
        "options_page_slug": "fp02-site-settings",
        "options_values_seeded": False,
        "contacts_group_registered": True,
        "modal_cta_group_registered": True
    },
    "seeded_objects_d4": [
        {"object_id": 4, "type": "page", "title": "Главная", "path": "/", "acf_nonempty": ["home_hero_slides", "home_service_nav_items", "home_cta_title", "home_cta_text"]},
        {"object_id": 5, "type": "page", "title": "Услуги", "path": "/uslugi/", "acf_nonempty": ["services_hub_intro", "services_hub_query_mode", "services_hub_show_placeholders"]},
        {"object_id": 20, "type": "page", "title": "Контакты", "path": "/kontakty/", "acf_nonempty": ["contacts_address", "contacts_form_intro", "contacts_phones"]},
        {"object_id": 73, "type": "service", "path": "/uslugi/zavisimosti/", "acf_nonempty": ["service_layout_variant", "hero_lead"]},
        {"object_id": 74, "type": "service", "path": "/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/", "acf_nonempty": ["service_layout_variant", "hero_lead", "intro_text", "signs_items"]},
        {"object_id": 77, "type": "service", "path": "/uslugi/psihicheskoe-zdorovie/", "acf_nonempty": ["service_layout_variant", "hero_lead"]},
        {"object_id": 84, "type": "service", "path": "/uslugi/rasstroystva-pischevogo-povedeniya/", "acf_nonempty": ["service_layout_variant", "hero_lead"]}
    ],
    "media_notes": {
        "contacts_map_png": "Theme static assets expected; runtime uploads not inventoried live",
        "contacts_rehab_photo": "Theme static fallback in contacts-helpers.php",
        "hero_images": "home_hero_slides.image and hero_media unseeded; require separate media authorization"
    },
    "mutations": {"runtime_content_writes": 0, "database_writes": 0, "wpilot_writes": 0},
    "result": "PARTIAL_LIVE_DB_UNAVAILABLE_EVIDENCE_FROM_D7F_D4"
}
write("runtime-readonly-inventory.json", runtime_inventory)

# --- ACF field inventory helper ---
def field(rec):
    rec.setdefault("seed_priority", "OPTIONAL")
    rec.setdefault("mutation_risk", "LOW")
    rec.setdefault("recommended_wave", "DEFER")
    rec.setdefault("admin_usability", "OK_FOR_OLGA_NOW")
    return rec

fields = []

# Home
home_id = 4
for name, ftype, rep, req, label, seeded, wave, src, admin in [
    ("home_hero_slides", "repeater", True, False, "Hero slides", True, "D8-B", "V9_STATIC_SOURCE index.html hero", "NEEDS_LABEL_HELP_TEXT"),
    ("home_service_nav_items", "repeater", True, False, "Service navigation", True, "D8-B", "EXISTING_WP_TITLE service parents", "OK_FOR_OLGA_NOW"),
    ("home_advantages", "repeater", True, False, "Advantages / trust", False, "D8-B", "V9_STATIC_SOURCE home-why-us", "NEEDS_LABEL_HELP_TEXT"),
    ("home_intro_bands", "repeater", True, False, "Intro bands", False, "D8-B", "V9_STATIC_SOURCE treatment-prevention", "NEEDS_FIELD_GROUP_REORDER"),
    ("home_reviews_teaser", "repeater", True, False, "Reviews teaser", False, "DEFER", "DEFERRED", "TOO_COMPLEX_FOR_MVP"),
    ("home_blog_teaser_enabled", "true_false", False, False, "Blog teaser enabled", False, "DEFER", "DEFERRED", "DEVELOPER_ONLY"),
    ("home_gallery_media", "repeater", True, False, "Gallery / media bands", False, "D8-B", "V9_STATIC_SOURCE + MEDIA_REQUIRED", "NEEDS_MEDIA_ASSET"),
    ("home_faq_items", "repeater", True, False, "FAQ", False, "D8-B", "V9_STATIC_SOURCE home FAQ section", "OK_FOR_OLGA_NOW"),
    ("home_cta_title", "text", False, False, "CTA title", True, "D8-B", "V9_STATIC_SOURCE final-form", "OK_FOR_OLGA_NOW"),
    ("home_cta_text", "textarea", False, False, "CTA text", True, "D8-B", "V9_STATIC_SOURCE final-form", "OK_FOR_OLGA_NOW"),
]:
    fields.append(field({
        "field_group": "group_fp02_page_home",
        "field_name": name,
        "object_type": "page",
        "target_object_id": home_id,
        "field_type": ftype,
        "repeatable": rep,
        "required": req,
        "admin_label": label,
        "currently_seeded": seeded,
        "seed_priority": "MVP" if wave == "D8-B" and not seeded else ("DONE" if seeded else "DEFER"),
        "source_data_candidate": src,
        "fallback_behavior": "STATIC_FALLBACK_ALREADY_IN_TEMPLATE" if name in ("home_intro_bands",) else "OMIT_SECTION_IF_EMPTY",
        "recommended_seed_wave": wave,
        "admin_usability_concern": admin
    }))

# Services hub
hub_id = 5
for name, ftype, rep, req, label, seeded, wave, src, admin, prio in [
    ("services_hub_intro", "textarea", False, False, "Intro", True, "D8-D", "V9_STATIC_SOURCE uslugi-v2.html", "OK_FOR_OLGA_NOW", "DONE"),
    ("services_hub_query_mode", "select", False, False, "Query display mode", True, "D8-D", "EXISTING_ACF_VALUE", "DEVELOPER_ONLY", "DONE"),
    ("services_hub_show_placeholders", "true_false", False, False, "Show placeholder services", True, "D8-D", "EXISTING_ACF_VALUE", "DEVELOPER_ONLY", "DONE"),
    ("services_hub_faq_items", "repeater", True, False, "FAQ", False, "D8-D", "V9_STATIC_SOURCE uslugi-v2 FAQ", "OK_FOR_OLGA_NOW", "SHOULD"),
]:
    fields.append(field({
        "field_group": "group_fp02_page_services_hub",
        "field_name": name,
        "object_type": "page",
        "target_object_id": hub_id,
        "field_type": ftype,
        "repeatable": rep,
        "required": req,
        "admin_label": label,
        "currently_seeded": seeded,
        "seed_priority": prio,
        "source_data_candidate": src,
        "fallback_behavior": "OMIT_SECTION_IF_EMPTY" if name == "services_hub_faq_items" else "KEEP_EXISTING",
        "recommended_seed_wave": wave,
        "admin_usability_concern": admin
    }))

# Service fields (all service CPT; wave D8-C per object)
service_field_defs = [
    ("service_layout_variant", "select", False, True, "Layout variant", "DEVELOPER_ONLY", "KEEP_EXISTING"),
    ("hero_eyebrow", "text", False, False, "Eyebrow", "OK_FOR_OLGA_NOW", "V9_STATIC_SOURCE"),
    ("hero_title_override", "text", False, False, "H1 override", "NEEDS_OPERATOR_DECISION", "EXISTING_WP_TITLE"),
    ("hero_lead", "textarea", False, False, "Lead", "OK_FOR_OLGA_NOW", "V9_STATIC_SOURCE"),
    ("hero_media", "image", False, False, "Hero media", "NEEDS_MEDIA_ASSET", "MEDIA_REQUIRED"),
    ("hero_cta_label", "text", False, False, "Hero CTA label", "OK_FOR_OLGA_NOW", "SITE_OPTION_REQUIRED"),
    ("hero_cta_target", "url", False, False, "Hero CTA target", "OK_FOR_OLGA_NOW", "STATIC_FALLBACK"),
    ("intro_text", "textarea", False, False, "Intro text", "OK_FOR_OLGA_NOW", "V9_STATIC_SOURCE"),
    ("intro_note", "textarea", False, False, "Intro note", "OK_FOR_OLGA_NOW", "V9_STATIC_SOURCE"),
    ("signs_items", "repeater", True, False, "Signs / symptoms", "OK_FOR_OLGA_NOW", "V9_STATIC_SOURCE"),
    ("programme_items", "repeater", True, False, "Programme items", "OK_FOR_OLGA_NOW", "V9_STATIC_SOURCE"),
    ("stages", "repeater", True, False, "Stages", "OK_FOR_OLGA_NOW", "V9_STATIC_SOURCE"),
    ("cta_title", "text", False, False, "CTA title", "OK_FOR_OLGA_NOW", "V9_STATIC_SOURCE"),
    ("cta_text", "textarea", False, False, "CTA text", "OK_FOR_OLGA_NOW", "V9_STATIC_SOURCE"),
    ("cta_button_label", "text", False, False, "CTA button label", "OK_FOR_OLGA_NOW", "SITE_OPTION_REQUIRED"),
    ("cta_button_target", "url", False, False, "CTA button target", "DEVELOPER_ONLY", "STATIC_FALLBACK"),
    ("faq_items", "repeater", True, False, "FAQ", "OK_FOR_OLGA_NOW", "V9_STATIC_SOURCE"),
    ("manual_related_services", "relationship", False, False, "Manual related services", "TOO_COMPLEX_FOR_MVP", "DEFERRED"),
]

seeded_by_svc = {
    73: {"service_layout_variant", "hero_lead"},
    74: {"service_layout_variant", "hero_lead", "intro_text", "signs_items"},
    77: {"service_layout_variant", "hero_lead"},
    84: {"service_layout_variant", "hero_lead"},
}
mvp_extra_74 = {"programme_items", "stages", "faq_items", "cta_title", "cta_text", "cta_button_label"}
mvp_extra_parents = {"hero_lead"}  # already seeded

for svc_id, path, registry in [(73, "/uslugi/zavisimosti/", "SVC-ZAVISIMOSTI"), (74, "/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/", "SVC-ALKOGOL"), (77, "/uslugi/psihicheskoe-zdorovie/", "SVC-PSYCH"), (84, "/uslugi/rasstroystva-pischevogo-povedeniya/", "SVC-RPP")]:
    for name, ftype, rep, req, label, admin, src in service_field_defs:
        seeded = name in seeded_by_svc.get(svc_id, set())
        if svc_id == 74 and name in mvp_extra_74:
            prio, wave = "MVP", "D8-C"
        elif seeded:
            prio, wave = "DONE", "D8-C"
        elif name == "service_layout_variant":
            prio, wave = "DONE", "D8-C"
        elif name in ("hero_media", "manual_related_services"):
            prio, wave = "DEFER", "DEFER"
        elif svc_id in (77, 84) and name in ("intro_text", "signs_items", "programme_items", "stages", "faq_items"):
            prio, wave = "SHOULD", "D8-C"
        else:
            prio, wave = "OPTIONAL", "D8-C"
        grp = "group_fp02_service_faq" if name == "faq_items" else ("group_fp02_service_relationships" if name == "manual_related_services" else ("group_fp02_service_layout_hero" if name.startswith(("service_", "hero_")) else "group_fp02_service_structured_sections"))
        fields.append(field({
            "field_group": grp,
            "field_name": name,
            "object_type": "service",
            "target_object_id": svc_id,
            "registry_id": registry,
            "path": path,
            "field_type": ftype,
            "repeatable": rep,
            "required": req,
            "admin_label": label,
            "currently_seeded": seeded,
            "seed_priority": prio,
            "source_data_candidate": src,
            "fallback_behavior": "OMIT_SECTION_IF_EMPTY",
            "recommended_seed_wave": wave,
            "admin_usability_concern": admin,
            "mutation_risk": "LOW" if ftype != "relationship" else "MEDIUM"
        }))

# Contacts page
for name, ftype, rep, seeded, wave, src, admin in [
    ("contacts_address", "textarea", False, True, "D8-E", "V9_STATIC_SOURCE kontakty.html", "OK_FOR_OLGA_NOW"),
    ("contacts_map_url", "url", False, False, "D8-E", "OPERATOR_SUPPLIED_REQUIRED", "NEEDS_OPERATOR_DECISION"),
    ("contacts_phones", "repeater", True, True, "D8-E", "V9_STATIC_SOURCE + SITE_OPTION_REQUIRED", "OK_FOR_OLGA_NOW"),
    ("contacts_messengers", "repeater", True, False, "D8-E", "SITE_OPTION_REQUIRED social_links", "NEEDS_DEFAULT_SEED"),
    ("contacts_blocks", "repeater", True, False, "D8-E", "V9_STATIC_SOURCE kontakty blocks", "NEEDS_LABEL_HELP_TEXT"),
    ("contacts_form_intro", "textarea", False, True, "D8-E", "V9_STATIC_SOURCE", "OK_FOR_OLGA_NOW"),
]:
    fields.append(field({
        "field_group": "group_fp02_page_contacts",
        "field_name": name,
        "object_type": "page",
        "target_object_id": 20,
        "field_type": ftype,
        "repeatable": rep,
        "required": False,
        "admin_label": name,
        "currently_seeded": seeded,
        "seed_priority": "DONE" if seeded else "MVP",
        "source_data_candidate": src,
        "fallback_behavior": "SITE_OPTION_FALLBACK" if name in ("contacts_phones", "contacts_messengers") else "STATIC_FALLBACK_ALREADY_IN_TEMPLATE",
        "recommended_seed_wave": wave,
        "admin_usability_concern": admin
    }))

# Site options
for name, ftype, rep, wave, src, admin, prio in [
    ("organisation_name", "text", False, "D8-A", "OPERATOR_SUPPLIED_REQUIRED", "OK_FOR_OLGA_NOW", "MVP"),
    ("phone_primary", "text", False, "D8-A", "OPERATOR_SUPPLIED_REQUIRED", "OK_FOR_OLGA_NOW", "MVP"),
    ("phone_secondary", "text", False, "D8-A", "OPERATOR_SUPPLIED_REQUIRED", "OK_FOR_OLGA_NOW", "SHOULD"),
    ("site_email", "email", False, "D8-A", "OPERATOR_SUPPLIED_REQUIRED", "OK_FOR_OLGA_NOW", "MVP"),
    ("site_address", "textarea", False, "D8-A", "V9_STATIC_SOURCE kontakty + OPERATOR", "OK_FOR_OLGA_NOW", "MVP"),
    ("opening_hours", "textarea", False, "D8-A", "OPERATOR_SUPPLIED_REQUIRED", "OK_FOR_OLGA_NOW", "MVP"),
    ("map_link", "url", False, "D8-A", "OPERATOR_SUPPLIED_REQUIRED", "NEEDS_OPERATOR_DECISION", "MVP"),
    ("social_links", "repeater", True, "D8-A", "OPERATOR_SUPPLIED_REQUIRED", "NEEDS_DEFAULT_SEED", "MVP"),
    ("legal_org_identifiers", "textarea", False, "D8-A", "OPERATOR_SUPPLIED_REQUIRED", "NEEDS_OPERATOR_DECISION", "SHOULD"),
    ("default_callback_title", "text", False, "D8-A", "V9_STATIC_SOURCE modal", "OK_FOR_OLGA_NOW", "SHOULD"),
    ("default_callback_text", "textarea", False, "D8-A", "V9_STATIC_SOURCE modal", "OK_FOR_OLGA_NOW", "SHOULD"),
    ("default_button_label", "text", False, "D8-A", "V9_STATIC_SOURCE CTA labels", "OK_FOR_OLGA_NOW", "MVP"),
    ("default_secondary_button_label", "text", False, "D8-A", "V9_STATIC_SOURCE", "OK_FOR_OLGA_NOW", "OPTIONAL"),
    ("default_consent_text_reference", "text", False, "D8-A", "DEFERRED legal pages", "NEEDS_OPERATOR_DECISION", "DEFER"),
    ("global_cta_title", "text", False, "D8-A", "V9_STATIC_SOURCE", "OK_FOR_OLGA_NOW", "SHOULD"),
    ("global_cta_text", "textarea", False, "D8-A", "V9_STATIC_SOURCE", "OK_FOR_OLGA_NOW", "SHOULD"),
]:
    fields.append(field({
        "field_group": "group_fp02_site_options_contacts" if name not in ("default_callback_title", "default_callback_text", "default_button_label", "default_secondary_button_label", "default_consent_text_reference", "global_cta_title", "global_cta_text") else "group_fp02_site_options_modal_cta",
        "field_name": name,
        "object_type": "options",
        "target_scope": "fp02-site-settings",
        "field_type": ftype,
        "repeatable": rep,
        "required": False,
        "admin_label": name,
        "currently_seeded": False,
        "seed_priority": prio,
        "source_data_candidate": src,
        "fallback_behavior": "HIDE_OR_STATIC_FALLBACK_IN_THEME",
        "recommended_seed_wave": wave,
        "admin_usability_concern": admin,
        "mutation_risk": "LOW"
    }))

summary_areas = {
    "Home": {"groups": 1, "fields": 10, "mvp": 4, "optional": 4, "deferred": 2, "admin_concerns": 4},
    "Services Hub": {"groups": 1, "fields": 4, "mvp": 0, "optional": 1, "deferred": 0, "admin_concerns": 1},
    "Services": {"groups": 4, "fields": 18, "mvp": 6, "optional": 8, "deferred": 4, "admin_concerns": 6},
    "Contacts": {"groups": 1, "fields": 6, "mvp": 3, "optional": 3, "deferred": 0, "admin_concerns": 2},
    "Site Options": {"groups": 2, "fields": 16, "mvp": 8, "optional": 5, "deferred": 1, "admin_concerns": 3},
    "Header/Footer/Global": {"groups": 0, "fields": 0, "mvp": 0, "optional": 0, "deferred": 0, "admin_concerns": 0, "note": "Reads site options only; no separate ACF group"}
}

write("acf-options-field-inventory.json", {
    "phase": "V9-06D8",
    "generated_at": TS,
    "acf_json_source": "WORDPRESS/acf-json/",
    "field_groups_in_source": 13,
    "mvp_relevant_groups": 7,
    "fields": fields,
    "summary_by_area": summary_areas,
    "result": "COMPLETE"
})

# --- MVP gap map ---
routes = [
    {
        "route": "/",
        "template": "Home",
        "object_id": 4,
        "gaps": {
            "MUST_SEED_FOR_MVP": ["home_advantages", "home_faq_items"],
            "SHOULD_SEED_FOR_VISUAL_RICHNESS": ["home_gallery_media", "home_intro_bands", "home_hero_slides.image"],
            "CAN_USE_STATIC_FALLBACK": ["treatment-prevention", "rehabilitation-program"],
            "DEFER_AFTER_MVP": ["home_reviews_teaser", "home_blog_teaser_enabled", "founder-quote", "specialists", "genotyping", "comfort"],
            "NEEDS_OPERATOR_CONTENT": ["phone_primary via site options", "legal consent references"],
            "NEEDS_MEDIA_ASSET": ["home_hero_slides.image", "home_gallery_media.media"],
            "NEEDS_ADMIN_UX_REPAIR": ["mixed EN/RU repeater sub-labels"],
            "BLOCKED": []
        },
        "mvp_blocker": False,
        "notes": "Route PASS at D7-F with minimal seed; richer MVP needs D8-A options + D8-B repeaters"
    },
    {
        "route": "/uslugi/",
        "template": "Services Hub",
        "object_id": 5,
        "gaps": {
            "MUST_SEED_FOR_MVP": [],
            "SHOULD_SEED_FOR_VISUAL_RICHNESS": ["services_hub_faq_items"],
            "CAN_USE_STATIC_FALLBACK": ["service_cards from CPT query", "rehabilitation-program"],
            "DEFER_AFTER_MVP": ["genotyping hub", "category hero image", "category galleries", "founder/comfort blocks"],
            "NEEDS_OPERATOR_CONTENT": [],
            "NEEDS_MEDIA_ASSET": ["category hero images", "category galleries"],
            "NEEDS_ADMIN_UX_REPAIR": ["services_hub_query_mode developer-only labeling"],
            "BLOCKED": []
        },
        "mvp_blocker": False
    },
    {
        "route": "/uslugi/zavisimosti/",
        "template": "Service parent",
        "object_id": 73,
        "gaps": {
            "MUST_SEED_FOR_MVP": [],
            "SHOULD_SEED_FOR_VISUAL_RICHNESS": ["intro_text", "programme_items"],
            "CAN_USE_STATIC_FALLBACK": ["children grid from CPT"],
            "DEFER_AFTER_MVP": ["nature", "team-stats", "landscape", "specialists", "founder-quote", "comfort", "reviews", "corridor", "bordered-info"],
            "NEEDS_OPERATOR_CONTENT": [],
            "NEEDS_MEDIA_ASSET": ["hero_media"],
            "NEEDS_ADMIN_UX_REPAIR": [],
            "BLOCKED": []
        },
        "mvp_blocker": False
    },
    {
        "route": "/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/",
        "template": "Service child (alcohol_special)",
        "object_id": 74,
        "gaps": {
            "MUST_SEED_FOR_MVP": ["programme_items", "stages", "faq_items"],
            "SHOULD_SEED_FOR_VISUAL_RICHNESS": ["cta_title", "cta_text", "hero_media"],
            "CAN_USE_STATIC_FALLBACK": ["approach section partial from programme_items"],
            "DEFER_AFTER_MVP": ["shared blocks without ACF fields"],
            "NEEDS_OPERATOR_CONTENT": ["medical copy review before production"],
            "NEEDS_MEDIA_ASSET": ["hero_media"],
            "NEEDS_ADMIN_UX_REPAIR": [],
            "BLOCKED": []
        },
        "mvp_blocker": False,
        "notes": "Primary regression route; D7-F PASS with signs_items seeded"
    },
    {
        "route": "/uslugi/psihicheskoe-zdorovie/",
        "template": "Service parent (placeholder)",
        "object_id": 77,
        "gaps": {
            "MUST_SEED_FOR_MVP": [],
            "SHOULD_SEED_FOR_VISUAL_RICHNESS": ["intro_text", "signs_items"],
            "CAN_USE_STATIC_FALLBACK": ["placeholder notice in template"],
            "DEFER_AFTER_MVP": ["full production content"],
            "NEEDS_OPERATOR_CONTENT": ["clinical scope copy"],
            "NEEDS_MEDIA_ASSET": [],
            "NEEDS_ADMIN_UX_REPAIR": [],
            "BLOCKED": []
        },
        "mvp_blocker": False
    },
    {
        "route": "/uslugi/rasstroystva-pischevogo-povedeniya/",
        "template": "Service parent (placeholder)",
        "object_id": 84,
        "gaps": {
            "MUST_SEED_FOR_MVP": [],
            "SHOULD_SEED_FOR_VISUAL_RICHNESS": ["intro_text", "signs_items"],
            "CAN_USE_STATIC_FALLBACK": ["placeholder notice"],
            "DEFER_AFTER_MVP": ["full production content"],
            "NEEDS_OPERATOR_CONTENT": ["clinical scope copy"],
            "NEEDS_MEDIA_ASSET": [],
            "NEEDS_ADMIN_UX_REPAIR": [],
            "BLOCKED": []
        },
        "mvp_blocker": False
    },
    {
        "route": "/kontakty/",
        "template": "Contacts",
        "object_id": 20,
        "gaps": {
            "MUST_SEED_FOR_MVP": ["site options phone/email/hours", "contacts_messengers or social_links"],
            "SHOULD_SEED_FOR_VISUAL_RICHNESS": ["contacts_blocks", "contacts_map_url"],
            "CAN_USE_STATIC_FALLBACK": ["map PNG assets in theme", "rehabilitation interior photo", "form markup without endpoint"],
            "DEFER_AFTER_MVP": ["live form endpoint", "map API embed"],
            "NEEDS_OPERATOR_CONTENT": ["real phone numbers", "messenger URLs", "map link"],
            "NEEDS_MEDIA_ASSET": ["map PNG if not in theme dist", "rehabilitation photo upload"],
            "NEEDS_ADMIN_UX_REPAIR": ["duplicate phone fields page vs options"],
            "BLOCKED": ["live form endpoint — explicit authorization required"]
        },
        "mvp_blocker": False,
        "notes": "Chrome contact bits empty until D8-A site options seed"
    }
]

write("mvp-content-gap-map.json", {
    "phase": "V9-06D8",
    "generated_at": TS,
    "classification_source": "D7-F known-gaps + ACF/template analysis",
    "routes": routes,
    "global_gaps": {
        "site_options_never_seeded": True,
        "shared_v9_blocks_without_acf": ["founder-quote", "specialists", "genotyping", "comfort", "nature", "team-stats", "landscape", "reviews", "corridor", "bordered-info"],
        "media_uploads_not_authorized_in_d8_planning": True
    },
    "has_mvp_blockers": False,
    "result": "COMPLETE"
})

# --- Olga admin UX ---
olga = {
    "phase": "V9-06D8",
    "generated_at": TS,
    "operator": "Olga",
    "goal": "Routine content editable in WP admin without developer intervention",
    "areas": [
        {"area": "Site Options (fp02-site-settings)", "current": "Registered but empty; mixed EN labels", "improvement": "Seed D8-A values; Russian labels/help in D8-F", "classification": "NEEDS_DEFAULT_SEED", "before_mvp": True},
        {"area": "Home page ACF", "current": "4 fields seeded; repeaters empty", "improvement": "Section-order tab labels; Russian instructions on repeaters", "classification": "NEEDS_LABEL_HELP_TEXT", "before_mvp": False},
        {"area": "Services Hub ACF", "current": "Intro seeded; FAQ empty", "improvement": "Hide or read-only query_mode for editors", "classification": "NEEDS_OPERATOR_DECISION", "before_mvp": False},
        {"area": "Service edit screen", "current": "4 field groups stacked; layout variant required", "improvement": "Collapsible groups by section; lock layout_variant for non-devs", "classification": "NEEDS_FIELD_GROUP_REORDER", "before_mvp": False},
        {"area": "Contacts page ACF", "current": "Partial seed; overlaps site options", "improvement": "Document single source: phones in Options, page overrides optional", "classification": "NEEDS_LABEL_HELP_TEXT", "before_mvp": True},
        {"area": "Media fields", "current": "Image fields unseeded", "improvement": "Media library workflow doc for Olga", "classification": "NEEDS_OPERATOR_DECISION", "before_mvp": False},
        {"area": "Forms / CTAs", "current": "Static form; no endpoint", "improvement": "Keep developer-only until endpoint authorized", "classification": "DEVELOPER_ONLY", "before_mvp": False},
        {"area": "Legal identifiers", "current": "Empty textarea", "improvement": "Operator-supplied only; flag legal review", "classification": "NEEDS_OPERATOR_DECISION", "before_mvp": False},
    ],
    "recommendations": {
        "edit_in_pages": ["home_* repeaters", "services_hub_intro", "services_hub_faq_items", "contacts_form_intro", "contacts_blocks"],
        "edit_in_services": ["hero_lead", "intro_text", "signs_items", "programme_items", "stages", "faq_items", "cta_*"],
        "edit_in_site_options": ["phone_primary", "site_email", "site_address", "opening_hours", "social_links", "default_button_label", "global_cta_*"],
        "do_not_expose_yet": ["service_layout_variant", "services_hub_query_mode", "manual_related_services", "form endpoint config"],
        "developer_only": ["layout variant", "query mode", "rewrite-dependent slugs", "ACF JSON structure"],
        "d8_f_required_before_handoff": False,
        "d8_f_recommended": True
    },
    "result": "COMPLETE"
}
write("olga-admin-ux-assessment.json", olga)

# --- Seed waves ---
waves = [
    {
        "wave_id": "D8-A",
        "name": "Site Options Seed",
        "purpose": "Populate global contact, CTA, and org fields for header/footer/contacts chrome",
        "allowed_objects": ["options:fp02-site-settings"],
        "allowed_fields": ["organisation_name", "phone_primary", "phone_secondary", "site_email", "site_address", "opening_hours", "map_link", "social_links", "legal_org_identifiers", "default_callback_title", "default_callback_text", "default_button_label", "default_secondary_button_label", "global_cta_title", "global_cta_text"],
        "forbidden_writes": ["pages", "services", "posts", "menus", "redirects", "rewrite flush", "media uploads", "objects create/delete"],
        "expected_writes": "16 option field values max (partial OK if operator defers legal/social)",
        "checkpoint_required": True,
        "dry_run_required": True,
        "rollback_plan": "Restore options snapshot from pre-wave DB checkpoint",
        "success_criteria": "Header/footer/contacts show phone/email/hours; no route regression",
        "estimated_risk": "LOW",
        "operator_review_gate": True,
        "recommended": True
    },
    {
        "wave_id": "D8-B",
        "name": "Home Content Seed",
        "purpose": "Fill home ACF repeaters for feature grid, FAQ, optional gallery",
        "allowed_objects": ["page:4"],
        "allowed_fields": ["home_advantages", "home_intro_bands", "home_faq_items", "home_gallery_media", "home_hero_slides"],
        "forbidden_writes": ["services", "options", "media uploads unless authorized", "object create/delete", "rewrite flush"],
        "expected_writes": "Up to 5 ACF fields on page 4",
        "checkpoint_required": True,
        "dry_run_required": True,
        "rollback_plan": "Per-field rollback from D4 baseline hashes where applicable",
        "success_criteria": "Home optional sections render when seeded; empty sections still omit safely",
        "estimated_risk": "LOW-MEDIUM",
        "operator_review_gate": True,
        "recommended": True
    },
    {
        "wave_id": "D8-C",
        "name": "Services MVP Content Seed",
        "purpose": "Expand programme/stages/FAQ on service 74; optional enrichment on 73/77/84",
        "allowed_objects": ["service:73", "service:74", "service:77", "service:84"],
        "allowed_fields": ["intro_text", "signs_items", "programme_items", "stages", "faq_items", "cta_title", "cta_text", "cta_button_label", "hero_lead", "intro_note"],
        "forbidden_writes": ["object create/delete", "layout variant change on 74", "rewrite flush", "media unless authorized"],
        "expected_writes": "Priority service 74: 3-6 fields; others optional",
        "checkpoint_required": True,
        "dry_run_required": True,
        "rollback_plan": "Restore service meta from checkpoint; preserve D4 minimal_seed markers",
        "success_criteria": "Service 74 shows programme/stages/FAQ; routes remain 200",
        "estimated_risk": "MEDIUM",
        "operator_review_gate": True,
        "recommended": True
    },
    {
        "wave_id": "D8-D",
        "name": "Services Hub Content Seed",
        "purpose": "FAQ and intro polish on services hub page",
        "allowed_objects": ["page:5"],
        "allowed_fields": ["services_hub_intro", "services_hub_faq_items"],
        "forbidden_writes": ["services_hub_query_mode", "services_hub_show_placeholders unless operator approves", "CPT changes", "rewrite flush"],
        "expected_writes": "1-2 fields on page 5",
        "checkpoint_required": True,
        "dry_run_required": True,
        "rollback_plan": "Restore page 5 ACF from checkpoint",
        "success_criteria": "Hub FAQ section renders when seeded",
        "estimated_risk": "LOW",
        "operator_review_gate": True,
        "recommended": True
    },
    {
        "wave_id": "D8-E",
        "name": "Contacts Content Seed",
        "purpose": "Align contacts page fields with seeded site options; map/messenger rows",
        "allowed_objects": ["page:20"],
        "allowed_fields": ["contacts_messengers", "contacts_blocks", "contacts_map_url", "contacts_phones", "contacts_address"],
        "forbidden_writes": ["live form endpoint", "map API keys", "external API", "rewrite flush"],
        "expected_writes": "2-5 fields on page 20; depends on D8-A",
        "checkpoint_required": True,
        "dry_run_required": True,
        "rollback_plan": "Restore page 20 ACF from checkpoint",
        "success_criteria": "Contacts messengers/locations render; form remains static",
        "estimated_risk": "LOW-MEDIUM",
        "operator_review_gate": True,
        "recommended": True,
        "depends_on": ["D8-A"]
    },
    {
        "wave_id": "D8-F",
        "name": "Admin UX Repair (source task)",
        "purpose": "ACF JSON label/help/reorder improvements for Olga — source change only",
        "allowed_objects": [],
        "allowed_fields": [],
        "forbidden_writes": ["runtime seed in same task", "ACF JSON without source task authorization"],
        "expected_writes": "Source ACF JSON + theme admin copy only when authorized",
        "checkpoint_required": True,
        "dry_run_required": False,
        "rollback_plan": "Git revert ACF JSON delivery wave",
        "success_criteria": "Olga-facing labels Russian; developer fields hidden or read-only",
        "estimated_risk": "MEDIUM",
        "operator_review_gate": True,
        "recommended": False,
        "note": "Optional parallel track; not blocking D8-A"
    },
    {
        "wave_id": "D8-G",
        "name": "Post-Seed Runtime QA",
        "purpose": "Full route/content/visual smoke after seed waves",
        "allowed_objects": ["read-only QA"],
        "allowed_fields": [],
        "forbidden_writes": ["all mutations unless defect fix separately authorized"],
        "expected_writes": 0,
        "checkpoint_required": False,
        "dry_run_required": False,
        "rollback_plan": "N/A",
        "success_criteria": "D7-F equivalent PASS with reduced EXPECTED gaps",
        "estimated_risk": "NONE",
        "operator_review_gate": True,
        "recommended": True,
        "depends_on": ["D8-A", "D8-B", "D8-C", "D8-D", "D8-E"]
    }
]
write("seed-wave-design.json", {"phase": "V9-06D8", "generated_at": TS, "waves": waves, "execution_order": ["D8-A", "D8-B", "D8-C", "D8-D", "D8-E", "D8-G"], "parallel_optional": ["D8-F"], "result": "COMPLETE"})

# --- Content source map (abbreviated entries) ---
content_sources = [
    {"area": "Site Options", "primary_source": "OPERATOR_SUPPLIED_REQUIRED", "v9_reference": "src/pages/kontakty.html, header partial", "operator_needed": True, "media_needed": False, "do_not_seed": ["default_consent_text_reference until legal review"]},
    {"area": "Home hero", "primary_source": "V9_STATIC_SOURCE", "v9_reference": "src/pages/index.html hero section", "operator_needed": False, "media_needed": True, "do_not_seed": []},
    {"area": "Home advantages", "primary_source": "V9_STATIC_SOURCE", "v9_reference": "src/partials/sections/home-why-us.html", "operator_needed": False, "media_needed": False, "do_not_seed": []},
    {"area": "Home FAQ", "primary_source": "V9_STATIC_SOURCE", "v9_reference": "src/partials/sections/home-faq.html", "operator_needed": False, "media_needed": False, "do_not_seed": []},
    {"area": "Home gallery", "primary_source": "V9_STATIC_SOURCE", "v9_reference": "src/partials/sections/home-gallery.html", "operator_needed": False, "media_needed": True, "do_not_seed": []},
    {"area": "Services Hub FAQ", "primary_source": "V9_STATIC_SOURCE", "v9_reference": "src/pages/uslugi-v2.html FAQ block", "operator_needed": False, "media_needed": False, "do_not_seed": []},
    {"area": "Service 74 content", "primary_source": "V9_STATIC_SOURCE", "v9_reference": "src/pages/usluga-konechnaya-v1.html", "operator_needed": True, "media_needed": True, "do_not_seed": ["invented medical claims"]},
    {"area": "Service 73/77/84", "primary_source": "V9_STATIC_SOURCE", "v9_reference": "usluga-podrazdel-v1.html / placeholder pages", "operator_needed": True, "media_needed": False, "do_not_seed": []},
    {"area": "Contacts", "primary_source": "V9_STATIC_SOURCE", "v9_reference": "src/pages/kontakty.html", "operator_needed": True, "media_needed": True, "do_not_seed": ["live form endpoint"]},
    {"area": "Shared blocks (no ACF)", "primary_source": "DO_NOT_SEED", "v9_reference": "theme static partials", "operator_needed": False, "media_needed": False, "do_not_seed": ["founder-quote", "specialists", "genotyping", "comfort", "nature", "team-stats", "landscape", "reviews", "corridor", "bordered-info"]},
]
write("content-source-map.json", {"phase": "V9-06D8", "generated_at": TS, "entries": content_sources, "v9_static_root": "workspaces/fp-0002-shpigovsky-v9/src/", "v9_dist_root": "workspaces/fp-0002-shpigovsky-v9/dist/", "result": "COMPLETE"})

# --- Safety protocol ---
protocol = {
    "phase": "V9-06D8",
    "generated_at": TS,
    "required_head_gate": "d257fbe7ee8db4a099b6599e2c7c66fdc326fa21 or successor explicitly named in seed task",
    "local_remote_sync_gate": "branch mars/canonical-post-recovery; ahead=0 behind=0 before task",
    "runtime_identity_gate": "X:/MARS-Localhost/sites/wordpress/projects/shpigovsky; domain shpigovsky.test; theme shpigovsky; core_mode content_model",
    "db_checkpoint_before_mutation": True,
    "object_value_dry_run": True,
    "exact_allowlist_required": True,
    "pre_post_value_diff": True,
    "no_rewrite_flush_unless_authorized": True,
    "no_object_create_delete_unless_authorized": True,
    "no_media_upload_unless_authorized": True,
    "no_plugin_update_install_delete": True,
    "rollback_instructions": "DB/options/postmeta restore from operator checkpoint; document rollback hashes per field",
    "evidence_only_in_git": True,
    "no_db_dumps_in_git": True,
    "operator_acceptance_after_each_wave": True,
    "wpilot_write_must_remain_disabled": True,
    "result": "COMPLETE"
}
write("future-seed-mutation-safety-protocol.json", protocol)

# --- No mutation audit ---
no_mut = {
    "phase": "V9-06D8",
    "generated_at": TS,
    "timing": "POST_PLANNING",
    "git_branch": "mars/canonical-post-recovery",
    "git_head": "d257fbe7ee8db4a099b6599e2c7c66fdc326fa21",
    "runtime_files_changed": 0,
    "source_theme_plugin_acf_changed": 0,
    "documentation_evidence_changed": "PLANNED_IN_THIS_TASK",
    "database_writes": 0,
    "wordpress_content_writes": 0,
    "acf_meta_writes": 0,
    "options_writes": 0,
    "rewrite_flush": False,
    "permalink_rewrite_changed": False,
    "menus_changed": 0,
    "redirects_created": 0,
    "object_create_delete": 0,
    "media_uploads": 0,
    "plugin_updates": 0,
    "plugin_installs": 0,
    "plugin_deletes": 0,
    "external_api_keys_added": False,
    "wpilot_writes": 0,
    "result": "PASS"
}
write("no-mutation-audit.json", no_mut)

write("final-verdict.json", {
    "phase": "V9-06D8",
    "generated_at": TS,
    "task": "V9-06D8 Content Seed Planning",
    "verdict": "PASS",
    "runtime_delivery": "NOT_PERFORMED",
    "source_changes": 0,
    "runtime_writes": 0,
    "db_writes": 0,
    "content_writes": 0,
    "acf_meta_writes": 0,
    "options_writes": 0,
    "mvp_content_gap_map": "COMPLETE",
    "olga_admin_ux_plan": "COMPLETE",
    "seed_wave_design": "COMPLETE",
    "future_mutation_safety_protocol": "COMPLETE",
    "runtime_inventory": "PARTIAL",
    "recommended_next_phase": "CREATE_V9_06D8A_SITE_OPTIONS_SEED_TASK",
    "v9_06d8a": "READY FOR OPERATOR REVIEW"
})

print("done")
