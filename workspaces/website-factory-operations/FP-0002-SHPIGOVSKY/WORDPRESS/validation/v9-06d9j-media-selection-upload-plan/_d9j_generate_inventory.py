#!/usr/bin/env python3
"""Generate V9-06D9-J static media inventory JSON. TEMPORARY — NOT FOR GIT."""
import hashlib
import json
import os
import re
from datetime import datetime, timezone

OUT = os.path.dirname(os.path.abspath(__file__))
TS = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
V9_SRC = r"X:/AI MARS/workspaces/fp-0002-shpigovsky-v9/src"
THEME = r"X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/theme/shpigovsky/assets"
RUNTIME_THEME = r"X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/themes/shpigovsky/assets"
RUNTIME_BASE = "http://shpigovsky.test/wp-content/themes/shpigovsky/assets"

HOME_MEDIA = [
    ("hero", "hero", "img/hero/hero-main.png", "img/hero/hero-main.png", "home_hero_slides.image", 2230, 1246, "Шпиговский дом — центр профилактики и лечения зависимостей"),
    ("gallery", "gallery-01", "img/content/gallery/shpigovsky-gallery-01.webp", "img/content/gallery/shpigovsky-gallery-01.webp", "home_gallery_media[0].media", 621, 938, "Лечение зависимости от алкоголя"),
    ("gallery", "gallery-02", "img/content/gallery/shpigovsky-gallery-02.webp", "img/content/gallery/shpigovsky-gallery-02.webp", "home_gallery_media[1].media", 1113, 738, "Лудомания лечение зависимости"),
    ("gallery", "gallery-03", "img/content/gallery/shpigovsky-gallery-03.webp", "img/content/gallery/shpigovsky-gallery-03.webp", "home_gallery_media[2].media", 1171, 864, "Лечение подростковой зависимости"),
    ("gallery", "gallery-04", "img/content/gallery/shpigovsky-gallery-04.webp", "img/content/gallery/shpigovsky-gallery-04.webp", "home_gallery_media[3].media", 1296, 921, "Зависимость от постоянных покупок"),
    ("founder-quote", "founder-photo", "img/content/founder-sergey-shpigovsky.png", "img/content/founder-sergey-shpigovsky.png", None, 1281, 1278, "Сергей Юрьевич Шпиговский"),
    ("staff-photo", "staff-group", "img/content/pre-reviews/shpigovsky-staff-group.webp", "img/content/pre-reviews/shpigovsky-staff-group.webp", None, None, None, "Staff group photo"),
    ("clinic-landscape", "clinic-landscape", "img/content/pre-reviews/shpigovsky-clinic-landscape.webp", "img/content/pre-reviews/shpigovsky-clinic-landscape.webp", None, None, None, "Clinic landscape"),
    ("rehabilitation-requirements", "interior-corridor", "img/content/rehabilitation-requirements/shpigovsky-interior-corridor.webp", "img/content/rehabilitation-requirements/shpigovsky-interior-corridor.webp", None, None, None, "Interior corridor"),
    ("rehabilitation-program", "program-genotyping", "img/content/rehabilitation-program/program-genotyping.webp", "img/content/rehabilitation-program/program-genotyping.webp", None, None, None, "Genotyping program"),
    ("rehabilitation-program", "program-neuropsychology", "img/content/rehabilitation-program/program-neuropsychology.webp", "img/content/rehabilitation-program/program-neuropsychology.webp", None, None, None, "Neuropsychology program"),
    ("rehabilitation-program", "program-psychocorrection", "img/content/rehabilitation-program/program-psychocorrection.webp", "img/content/rehabilitation-program/program-psychocorrection.webp", None, None, None, "Psychocorrection program"),
    ("rehabilitation-program", "program-kinesiotherapy", "img/content/rehabilitation-program/program-kinesiotherapy.webp", "img/content/rehabilitation-program/program-kinesiotherapy.webp", None, None, None, "Kinesiotherapy program"),
    ("recovery-life", "section-bg", "img/content/recovery-life/recovery-life-section-bg.webp", "img/content/recovery-life/recovery-life-section-bg.webp", None, None, None, "Recovery life section background"),
    ("comfort", "comfort-room-01", "img/content/home-comfort/comfort-room-01.webp", "img/content/home-comfort/comfort-room-01.webp", None, 1957, 1113, "Comfort room 1"),
    ("comfort", "comfort-room-02", "img/content/home-comfort/comfort-room-02.webp", "img/content/home-comfort/comfort-room-02.webp", None, 1881, 1246, "Comfort room 2"),
    ("comfort", "comfort-room-03", "img/content/home-comfort/comfort-room-03.webp", "img/content/home-comfort/comfort-room-03.webp", None, 1623, 1155, "Comfort room 3"),
    ("comfort", "comfort-room-04", "img/content/home-comfort/comfort-room-04.webp", "img/content/home-comfort/comfort-room-04.webp", None, 1610, 1146, "Comfort room 4"),
    ("comfort", "comfort-room-05", "img/content/home-comfort/comfort-room-05.webp", "img/content/home-comfort/comfort-room-05.webp", None, 1276, 1136, "Comfort room 5"),
    ("comfort", "comfort-room-06", "img/content/home-comfort/comfort-room-06.webp", "img/content/home-comfort/comfort-room-06.webp", None, 2201, 1227, "Comfort room 6"),
    ("comfort", "logo-decor", "img/branding/logo.svg", "img/branding/logo.svg", None, None, None, "Comfort gallery logo decor"),
    ("videos", "interview-poster", "img/content/videos/sergey-shpigovsky-interview-poster.webp", "img/content/videos/sergey-shpigovsky-interview-poster.webp", None, None, None, "Interview video poster"),
    ("videos", "center-poster", "img/content/videos/shpigovsky-center-poster.webp", "img/content/videos/shpigovsky-center-poster.webp", None, None, None, "Center video poster"),
    ("videos", "interview-mp4", "video/sergey-shpigovsky-interview.mp4", "video/sergey-shpigovsky-interview.mp4", None, None, None, "Interview video file"),
    ("videos", "center-mp4", "video/shpigovsky-center.mp4", "video/shpigovsky-center.mp4", None, None, None, "Center video file"),
    ("specialists", "sergey-shpigovsky", "img/content/home-specialists/sergey-shpigovsky.webp", "img/content/home-specialists/sergey-shpigovsky.webp", None, 615, 605, "Сергей Юрьевич Шпиговский"),
    ("specialists", "maxim-kazakov", "img/content/home-specialists/maxim-kazakov.webp", "img/content/home-specialists/maxim-kazakov.webp", None, 657, 605, "Максим Михайлович Казаков"),
    ("specialists", "darya-kostyuk", "img/content/home-specialists/darya-kostyuk.webp", "img/content/home-specialists/darya-kostyuk.webp", None, 643, 610, "Дарья Владимировна Костюк"),
    ("specialists", "tatyana-shapiguzova", "img/content/home-specialists/tatyana-shapiguzova.webp", "img/content/home-specialists/tatyana-shapiguzova.webp", None, 643, 610, "Шапигузова Татьяна Андреевна"),
    ("articles", "article-alcohol", "img/content/home-articles/article-alcohol-dependence.webp", "img/content/home-articles/article-alcohol-dependence.webp", None, 1216, 1632, "Article teaser alcohol"),
    ("articles", "article-yoga", "img/content/home-articles/article-yoga-therapy.webp", "img/content/home-articles/article-yoga-therapy.webp", None, 1920, 1280, "Йога в терапии"),
    ("articles", "article-bos", "img/content/home-articles/article-bos-therapy.webp", "img/content/home-articles/article-bos-therapy.webp", None, 2048, 1365, "БОС-терапия"),
    ("final-form", "background", "img/content/home-final-form/home-final-form-background.webp", "img/content/home-final-form/home-final-form-background.webp", None, None, None, "Final form background"),
    ("recovery-intro", "decor", "img/decor/home-recovery-intro-decor.png", "img/decor/home-recovery-intro-decor.png", None, None, None, "Recovery intro decorative"),
    ("footer", "logo", "img/branding/logo.svg", "img/branding/logo.svg", None, None, None, "Site logo"),
    ("footer", "whatsapp", "img/social/whatsapp.svg", "img/social/whatsapp.svg", None, None, None, "WhatsApp icon"),
    ("footer", "telegram", "img/social/telegram.svg", "img/social/telegram.svg", None, None, None, "Telegram icon"),
    ("footer", "max", "img/social/max.svg", "img/social/max.svg", None, None, None, "MAX messenger icon"),
    ("ui", "external-link", "svg/external-link.svg", "svg/external-link.svg", None, 20, 20, "External link icon"),
    ("ui", "founder-quote-mark", "svg/founder-quote-mark.svg", "svg/founder-quote-mark.svg", None, 70, 55, "Founder quote mark (inline SVG in template)"),
]

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest().upper()

def file_info(base, rel):
    path = os.path.join(base, rel.replace("/", os.sep))
    if not os.path.isfile(path):
        return None
    ext = os.path.splitext(path)[1].lower().lstrip(".")
    return {
        "path": path.replace("\\", "/"),
        "exists": True,
        "size_bytes": os.path.getsize(path),
        "sha256": sha256(path),
        "file_type": ext,
    }

def classify(section, acf_field, file_type):
    if acf_field and "home_hero" in acf_field:
        return "UPLOAD_AND_SEED_D9K"
    if acf_field and "home_gallery" in acf_field:
        return "UPLOAD_AND_SEED_D9K"
    if file_type in ("svg",) or section in ("footer", "ui"):
        return "DO_NOT_UPLOAD_VENDOR_OR_ICON"
    if section == "founder-quote" or section == "specialists":
        return "OPERATOR_REVIEW_REQUIRED"
    if section in ("videos",) and file_type == "mp4":
        return "DEFER_UNTIL_CONTENT_REVIEW"
    if section in ("recovery-intro",) and "decor" in section:
        return "DO_NOT_UPLOAD_DECORATIVE"
    if section == "recovery-intro":
        return "KEEP_THEME_FALLBACK"
    if section in ("comfort", "articles", "rehabilitation-program", "rehabilitation-requirements", "clinic-landscape", "staff-photo", "recovery-life", "final-form"):
        return "KEEP_THEME_FALLBACK"
    return "KEEP_THEME_FALLBACK"

assets = []
for section, asset_id, v9_rel, theme_rel, acf, w, h, alt_hint in HOME_MEDIA:
    v9 = file_info(V9_SRC, v9_rel)
    th = file_info(THEME, theme_rel)
    rt = file_info(RUNTIME_THEME, theme_rel)
    usage = "THEME_FALLBACK_ACTIVE" if (rt or th) else "STATIC_ONLY"
    if v9 and th and v9["sha256"] == th["sha256"]:
        match = "V9_SRC_THEME_MATCH"
    elif v9 and th:
        match = "V9_SRC_THEME_MISMATCH"
    elif v9:
        match = "V9_SRC_ONLY"
    else:
        match = "MISSING_V9_SRC"
    runtime_url = f"{RUNTIME_BASE}/{theme_rel}" if (rt or th) else ""
    ft = (v9 or th or rt or {}).get("file_type", "")
    assets.append({
        "section": section,
        "asset_id": asset_id,
        "static_v9_path": f"workspaces/fp-0002-shpigovsky-v9/src/{v9_rel}",
        "theme_asset_path": f"WORDPRESS/theme/shpigovsky/assets/{theme_rel}",
        "runtime_url": runtime_url,
        "file_type": ft,
        "width": w,
        "height": h,
        "file_size_bytes": (v9 or th or rt or {}).get("size_bytes"),
        "sha256": (v9 or th or rt or {}).get("sha256"),
        "v9_theme_checksum_match": match,
        "current_usage": usage,
        "acf_target_field": acf,
        "upload_to_wp_recommended": acf is not None,
        "suggested_alt_text": alt_hint,
        "classification": classify(section, acf, ft),
    })

with open(os.path.join(OUT, "static-v9-media-inventory.json"), "w", encoding="utf-8") as f:
    json.dump({
        "phase": "V9-06D9-J",
        "generated_at": TS,
        "mode": "READ_ONLY",
        "authority": {
            "static_v9_src": V9_SRC,
            "static_v9_dist": "workspaces/fp-0002-shpigovsky-v9/dist/",
            "theme_assets": THEME,
            "runtime_theme_assets": RUNTIME_THEME,
        },
        "home_related_asset_count": len(assets),
        "assets": assets,
        "result": "PASS",
    }, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote static-v9-media-inventory.json")

# Gap analysis from snapshot if present
snap_path = os.path.join(OUT, "home-page-media-acf-snapshot.json")
wp_path = os.path.join(OUT, "current-wp-media-library-inventory.json")
snap = json.load(open(snap_path, encoding="utf-8")) if os.path.isfile(snap_path) else {}
wp = json.load(open(wp_path, encoding="utf-8")) if os.path.isfile(wp_path) else {"attachments": []}

hero_image_empty = True
if snap.get("home_hero_slides", {}).get("rows"):
    img = snap["home_hero_slides"]["rows"][0].get("image", {})
    hero_image_empty = bool(img.get("empty", True))

gap_fields = [
    {
        "field_name": "home_hero_slides.image",
        "field_key": "field_fp02_home_hero_image",
        "field_type": "image (repeater subfield)",
        "target_object": "page #4",
        "current_db_value": "text row present; image " + ("empty" if hero_image_empty else "attachment present"),
        "current_frontend_output": "theme fallback hero-main.png" if hero_image_empty else "ACF attachment URL",
        "fallback_asset_used_now": "assets/img/hero/hero-main.png",
        "recommended_media_source": "workspaces/fp-0002-shpigovsky-v9/src/img/hero/hero-main.png",
        "upload_needed": "YES",
        "seed_needed_after_upload": "YES",
        "risk": "MEDIUM",
        "notes": "Hero text already seeded D4/D8; image subfield empty — theme fallback active per D9-C",
    },
    {
        "field_name": "home_gallery_media",
        "field_key": "field_fp02_home_gallery_media",
        "field_type": "repeater (title, text, media image)",
        "target_object": "page #4",
        "current_db_value": "empty repeater",
        "current_frontend_output": "4 slides from shpigovsky_home_gallery_fallback_items()",
        "fallback_asset_used_now": "img/content/gallery/shpigovsky-gallery-01..04.webp",
        "recommended_media_source": "V9 src gallery webp set + fallback titles from home-fallbacks.php",
        "upload_needed": "YES",
        "seed_needed_after_upload": "YES",
        "risk": "MEDIUM",
        "notes": "Requires 4 attachments + repeater seed with title/text from static fallbacks",
    },
    {
        "field_name": "home_reviews_teaser",
        "field_key": "field_fp02_home_reviews_teaser",
        "field_type": "repeater (title, text — no image subfield in schema)",
        "target_object": "page #4",
        "current_db_value": "empty",
        "current_frontend_output": "static review cards in reviews.php template",
        "fallback_asset_used_now": "N/A — text cards only in current MVP",
        "recommended_media_source": "DEFER — production review content",
        "upload_needed": "NO",
        "seed_needed_after_upload": "OPERATOR_DECISION",
        "risk": "HIGH",
        "notes": "Deferred D9-I; not in D9-K MVP media scope",
    },
]

with open(os.path.join(OUT, "acf-media-field-gap-analysis.json"), "w", encoding="utf-8") as f:
    json.dump({"phase": "V9-06D9-J", "generated_at": TS, "fields": gap_fields, "result": "PASS"}, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote acf-media-field-gap-analysis.json")

# Classification rollup
by_class = {}
for a in assets:
    c = a["classification"]
    by_class.setdefault(c, []).append(a["asset_id"])
class_doc = {
    "phase": "V9-06D9-J",
    "generated_at": TS,
    "summary": {k: len(v) for k, v in by_class.items()},
    "items": [{"asset_id": a["asset_id"], "section": a["section"], "classification": a["classification"], "reason": a.get("suggested_alt_text", "")} for a in assets],
    "result": "PASS",
}
with open(os.path.join(OUT, "media-classification.json"), "w", encoding="utf-8") as f:
    json.dump(class_doc, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote media-classification.json")

# D9-K plan
upload_candidates = [a for a in assets if a["classification"] == "UPLOAD_AND_SEED_D9K"]
plan_items = []
for a in upload_candidates:
    plan_items.append({
        "source_file_path": a["static_v9_path"],
        "target_wordpress_filename": os.path.basename(a["static_v9_path"]),
        "target_title": a["suggested_alt_text"],
        "alt_text": a["suggested_alt_text"],
        "caption": "",
        "description": f"Home {a['section']} — seeded from static V9 authority",
        "intended_wp_parent": 4,
        "target_acf_field": a["acf_target_field"],
        "target_object_id": 4,
        "expected_attachment_type": "image",
        "expected_visual_impact": "SHOULD_MATCH_CURRENT_FALLBACK",
        "rollback_strategy": "Restore DB checkpoint + delete attachment IDs from manifest",
        "validation_method": "Post-seed visual regression + admin field verification",
    })

d9k = {
    "phase": "V9-06D9-K",
    "planned_not_executed": True,
    "generated_at": TS,
    "phases": {
        "K1": {"action": "DB checkpoint + media upload dry-run manifest review", "targets": "all K2 candidates", "safety": "Operator approves exact filename/field map", "result": "PLANNED"},
        "K2": {"action": "Upload 5 images (1 hero + 4 gallery)", "targets": plan_items, "safety": "No overwrite of existing attachments; manifest attachment IDs", "result": "PLANNED"},
        "K3": {"action": "Seed home_hero_slides[0].image + home_gallery_media repeater", "targets": ["field_fp02_home_hero_image", "field_fp02_home_gallery_item_media"], "safety": "Pre-values JSON for page 4 media fields only", "result": "PLANNED"},
        "K4": {"action": "Visual regression QA home + hero + gallery sections", "targets": ["/"], "safety": "Compare to D9-J baseline screenshots", "result": "PLANNED"},
        "K5": {"action": "Admin media UX QA", "targets": ["wp-admin page 4 edit screen"], "safety": "Verify image pickers show attachments", "result": "PLANNED"},
    },
    "upload_candidates": plan_items,
    "result": "PASS",
}
with open(os.path.join(OUT, "d9k-media-upload-seed-plan.json"), "w", encoding="utf-8") as f:
    json.dump(d9k, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote d9k-media-upload-seed-plan.json")

rollback = {
    "phase": "V9-06D9-K",
    "planned_not_executed": True,
    "generated_at": TS,
    "requirements": {
        "db_checkpoint": "Full mars_wp_fp0002 mysqldump before K2/K3",
        "uploads_manifest": "Exact list of new attachment IDs + file paths under wp-content/uploads",
        "pre_values_json": "home-page-4-media-pre-values.json capturing home_hero_slides and home_gallery_media",
    },
    "rollback_methods": [
        {"method": "db_restore", "steps": "Restore mysqldump from K1 checkpoint", "scope": "Preferred full rollback"},
        {"method": "attachment_delete", "steps": "Delete only manifest-listed attachment IDs if operator approves exact list", "scope": "Partial — does not revert ACF without DB restore"},
    ],
    "forbidden": ["broad uploads cleanup", "full uploads deletion", "wp media regenerate without separate approval"],
    "risks": [
        {"risk": "Hero visual change if wrong image uploaded", "prevention": "Checksum match hero-main.png from V9 src", "rollback": "DB checkpoint restore"},
        {"risk": "Gallery slide order mismatch", "prevention": "Seed order matches home-fallbacks.php", "rollback": "Clear repeater + restore checkpoint"},
        {"risk": "Orphan attachments", "prevention": "Manifest all created IDs", "rollback": "Delete manifest IDs only"},
    ],
    "result": "PASS",
}
with open(os.path.join(OUT, "d9k-risk-rollback-plan.json"), "w", encoding="utf-8") as f:
    json.dump(rollback, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote d9k-risk-rollback-plan.json")

print("DONE")
