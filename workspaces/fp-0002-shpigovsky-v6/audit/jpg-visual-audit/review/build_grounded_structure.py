#!/usr/bin/env python3
"""Build FP-0002-V6-JPG-GROUNDED-STRUCTURE.json — review artefact only."""
from __future__ import annotations

import json
from pathlib import Path

OUT = Path(__file__).parent / "FP-0002-V6-JPG-GROUNDED-STRUCTURE.json"

BOUNDARIES = [
    {"boundary": 1, "y": 904, "previous": "BLOCK-001", "next": "BLOCK-002", "classification": "CONFIRMED_SECTION_BOUNDARY", "visual_evidence": "Hero photo and overlay end; light-blue page intro with heading and 6-card grid begins.", "confidence": "HIGH"},
    {"boundary": 2, "y": 1456, "previous": "BLOCK-002", "next": "BLOCK-003", "classification": "INTERNAL_SUBBLOCK_BOUNDARY", "visual_evidence": "6-card grid ends; quote block with portrait begins within continuous light-blue page band.", "confidence": "HIGH"},
    {"boundary": 3, "y": 1904, "previous": "BLOCK-003", "next": "BLOCK-004", "classification": "INTERNAL_SUBBLOCK_BOUNDARY", "visual_evidence": "Quote block ends; accordion services list begins; same page background family.", "confidence": "HIGH"},
    {"boundary": 4, "y": 2232, "previous": "BLOCK-004", "next": "BLOCK-005", "classification": "INTERNAL_SUBBLOCK_BOUNDARY", "visual_evidence": "Accordion list transitions to row of square clinical photos within programs area.", "confidence": "HIGH"},
    {"boundary": 5, "y": 2824, "previous": "BLOCK-005", "next": "BLOCK-006", "classification": "INTERNAL_SUBBLOCK_BOUNDARY", "visual_evidence": "Photo row ends; heading and text block (team/approach copy) follows in same composition.", "confidence": "MEDIUM"},
    {"boundary": 6, "y": 3312, "previous": "BLOCK-006", "next": "BLOCK-007", "classification": "INTERNAL_SUBBLOCK_BOUNDARY", "visual_evidence": "Text block to following team content; no full-width background break.", "confidence": "MEDIUM"},
    {"boundary": 7, "y": 3912, "previous": "BLOCK-007", "next": "BLOCK-008", "classification": "INTERNAL_SUBBLOCK_BOUNDARY", "visual_evidence": "Continuous light-blue team section; boundary aligns with internal row not page panel.", "confidence": "MEDIUM"},
    {"boundary": 8, "y": 4544, "previous": "BLOCK-008", "next": "BLOCK-009", "classification": "CONFIRMED_SECTION_BOUNDARY", "visual_evidence": "Page-light content ends; full-width staff group photograph (#0e0e26 band) begins.", "confidence": "HIGH"},
    {"boundary": 9, "y": 4992, "previous": "BLOCK-009", "next": "BLOCK-010", "classification": "CONFIRMED_SECTION_BOUNDARY", "visual_evidence": "Full-width photograph ends; light page and second card grid resume.", "confidence": "HIGH"},
    {"boundary": 10, "y": 5480, "previous": "BLOCK-010", "next": "BLOCK-011", "classification": "INTERNAL_SUBBLOCK_BOUNDARY", "visual_evidence": "Card grid transitions to full-width landscape photograph within post-team content flow.", "confidence": "HIGH"},
    {"boundary": 11, "y": 6064, "previous": "BLOCK-011", "next": "BLOCK-012", "classification": "CONFIRMED_SECTION_BOUNDARY", "visual_evidence": "Landscape photograph ends; benefit 6-card grid section with new heading begins.", "confidence": "HIGH"},
    {"boundary": 12, "y": 6776, "previous": "BLOCK-012", "next": "BLOCK-013", "classification": "INTERNAL_SUBBLOCK_BOUNDARY", "visual_evidence": "Benefit card grid ends; reviews subsection with two cards begins.", "confidence": "HIGH"},
    {"boundary": 13, "y": 7136, "previous": "BLOCK-013", "next": "BLOCK-014", "classification": "INTERNAL_SUBBLOCK_BOUNDARY", "visual_evidence": "Reviews end; process/requirements heading and numbered steps begin.", "confidence": "MEDIUM"},
    {"boundary": 14, "y": 7504, "previous": "BLOCK-014", "next": "BLOCK-015", "classification": "INTERNAL_SUBBLOCK_BOUNDARY", "visual_evidence": "Numbered steps transition to dark-blue CTA banner inside process section.", "confidence": "HIGH"},
    {"boundary": 15, "y": 7848, "previous": "BLOCK-015", "next": "BLOCK-016", "classification": "INTERNAL_SUBBLOCK_BOUNDARY", "visual_evidence": "CTA banner ends; dark interior photo band for documents section follows.", "confidence": "HIGH"},
    {"boundary": 16, "y": 8408, "previous": "BLOCK-016", "next": "BLOCK-017", "classification": "INTERNAL_SUBBLOCK_BOUNDARY", "visual_evidence": "Interior photo band ends; documents list on light-blue page continues.", "confidence": "HIGH"},
    {"boundary": 17, "y": 8824, "previous": "BLOCK-017", "next": "BLOCK-018", "classification": "INTERNAL_SUBBLOCK_BOUNDARY", "visual_evidence": "Documents text transitions to interior hallway gallery photos.", "confidence": "MEDIUM"},
    {"boundary": 18, "y": 9416, "previous": "BLOCK-018", "next": "BLOCK-019", "classification": "CONFIRMED_SECTION_BOUNDARY", "visual_evidence": "Interior gallery band ends; rehabilitation program list with thumb+text rows begins.", "confidence": "HIGH"},
    {"boundary": 19, "y": 10008, "previous": "BLOCK-019", "next": "BLOCK-020", "classification": "INTERNAL_SUBBLOCK_BOUNDARY", "visual_evidence": "Split between program list item rows within same 4-item section.", "confidence": "HIGH"},
    {"boundary": 20, "y": 10368, "previous": "BLOCK-020", "next": "BLOCK-021", "classification": "INTERNAL_SUBBLOCK_BOUNDARY", "visual_evidence": "Program rows end; bordered philosophy/info panel begins.", "confidence": "MEDIUM"},
    {"boundary": 21, "y": 10880, "previous": "BLOCK-021", "next": "BLOCK-022", "classification": "INTERNAL_SUBBLOCK_BOUNDARY", "visual_evidence": "Bordered panel to comfort/gallery heading within diagnostics/comfort area.", "confidence": "MEDIUM"},
    {"boundary": 22, "y": 11248, "previous": "BLOCK-022", "next": "BLOCK-023", "classification": "INTERNAL_SUBBLOCK_BOUNDARY", "visual_evidence": "Section heading to facility photo mosaic grid.", "confidence": "HIGH"},
    {"boundary": 23, "y": 11592, "previous": "BLOCK-023", "next": "BLOCK-024", "classification": "ALGORITHMIC_FALSE_POSITIVE", "visual_evidence": "Luminance spike from single mosaic photo tile (#133848); mosaic continues.", "confidence": "HIGH"},
    {"boundary": 24, "y": 11984, "previous": "BLOCK-024", "next": "BLOCK-025", "classification": "ALGORITHMIC_FALSE_POSITIVE", "visual_evidence": "Dark photo tile inside mosaic grid; not a page-level section edge.", "confidence": "HIGH"},
    {"boundary": 25, "y": 12336, "previous": "BLOCK-025", "next": "BLOCK-026", "classification": "CONFIRMED_SECTION_BOUNDARY", "visual_evidence": "Facility mosaic gallery ends; video section with two play thumbs begins.", "confidence": "HIGH"},
    {"boundary": 26, "y": 13136, "previous": "BLOCK-026", "next": "BLOCK-027", "classification": "INTERNAL_SUBBLOCK_BOUNDARY", "visual_evidence": "Video thumbs end; light page continues toward specialists — not contact form.", "confidence": "HIGH"},
    {"boundary": 27, "y": 13456, "previous": "BLOCK-027", "next": "BLOCK-028", "classification": "ALGORITHMIC_FALSE_POSITIVE", "visual_evidence": "Short local dark band (~54px) from image edge; center row remains light-blue page.", "confidence": "HIGH"},
    {"boundary": 28, "y": 13776, "previous": "BLOCK-028", "next": "BLOCK-029", "classification": "INTERNAL_SUBBLOCK_BOUNDARY", "visual_evidence": "Specialists section heading row to 3-column profile cards.", "confidence": "HIGH"},
    {"boundary": 29, "y": 14368, "previous": "BLOCK-029", "next": "BLOCK-030", "classification": "CONFIRMED_SECTION_BOUNDARY", "visual_evidence": "Specialists cards end; Articles section with 3 cards begins.", "confidence": "HIGH"},
    {"boundary": 30, "y": 14736, "previous": "BLOCK-030", "next": "BLOCK-031", "classification": "CONFIRMED_SECTION_BOUNDARY", "visual_evidence": "Articles end; FAQ accordion list section begins.", "confidence": "HIGH"},
    {"boundary": 31, "y": 15064, "previous": "BLOCK-031", "next": "BLOCK-032", "classification": "INTERNAL_SUBBLOCK_BOUNDARY", "visual_evidence": "FAQ accordion continues; no compositional page break.", "confidence": "MEDIUM"},
    {"boundary": 32, "y": 15408, "previous": "BLOCK-032", "next": "BLOCK-033", "classification": "CONFIRMED_SECTION_BOUNDARY", "visual_evidence": "FAQ/light page ends; contact band with dark left panel and form (Y~15420 mixed luminance) begins.", "confidence": "HIGH"},
    {"boundary": 33, "y": 15776, "previous": "BLOCK-033", "next": "BLOCK-034", "classification": "CONFIRMED_SECTION_BOUNDARY", "visual_evidence": "Contact form band ends; footer link columns on light page begin.", "confidence": "HIGH"},
    {"boundary": 34, "y": 16152, "previous": "BLOCK-034", "next": "BLOCK-035", "classification": "INTERNAL_SUBBLOCK_BOUNDARY", "visual_evidence": "Footer link columns to bottom copyright/social strip within one footer composition.", "confidence": "HIGH"},
]

MAJOR = [
    {"id": "SECTION-001", "y_start": 0, "y_end": 904, "blocks": ["BLOCK-001"], "role": "header and hero", "groups": [
        {"id": "SECTION-001-GROUP-01", "y_start": 0, "y_end": 174, "role": "header top bar"},
        {"id": "SECTION-001-GROUP-02", "y_start": 174, "y_end": 904, "role": "hero photo with overlay panel"},
    ]},
    {"id": "SECTION-002", "y_start": 904, "y_end": 4544, "blocks": ["BLOCK-002", "BLOCK-003", "BLOCK-004", "BLOCK-005", "BLOCK-006", "BLOCK-007", "BLOCK-008"], "role": "intro, quote, programs, team copy"},
    {"id": "SECTION-003", "y_start": 4544, "y_end": 4992, "blocks": ["BLOCK-009"], "role": "full-width staff group photo"},
    {"id": "SECTION-004", "y_start": 4992, "y_end": 6064, "blocks": ["BLOCK-010", "BLOCK-011"], "role": "second card grid and landscape photo"},
    {"id": "SECTION-005", "y_start": 6064, "y_end": 9416, "blocks": ["BLOCK-012", "BLOCK-013", "BLOCK-014", "BLOCK-015", "BLOCK-016", "BLOCK-017", "BLOCK-018"], "role": "benefits, reviews, process, CTA, documents, interior gallery"},
    {"id": "SECTION-006", "y_start": 9416, "y_end": 12336, "blocks": ["BLOCK-019", "BLOCK-020", "BLOCK-021", "BLOCK-022", "BLOCK-023", "BLOCK-024", "BLOCK-025"], "role": "program list, philosophy panel, facility mosaic gallery"},
    {"id": "SECTION-007", "y_start": 12336, "y_end": 14368, "blocks": ["BLOCK-026", "BLOCK-027", "BLOCK-028", "BLOCK-029"], "role": "video and specialists"},
    {"id": "SECTION-008", "y_start": 14368, "y_end": 14736, "blocks": ["BLOCK-030"], "role": "articles"},
    {"id": "SECTION-009", "y_start": 14736, "y_end": 15408, "blocks": ["BLOCK-031", "BLOCK-032"], "role": "FAQ accordion"},
    {"id": "SECTION-010", "y_start": 15408, "y_end": 15776, "blocks": ["BLOCK-033"], "role": "contact form band"},
    {"id": "SECTION-011", "y_start": 15776, "y_end": 16343, "blocks": ["BLOCK-034", "BLOCK-035"], "role": "site footer"},
]

MAPPING = [
    {"old_block": "BLOCK-001", "new_major_section": "SECTION-001", "internal_group": "SECTION-001-GROUP-01/02", "action": "KEEP_AS_SECTION"},
    {"old_block": "BLOCK-002", "new_major_section": "SECTION-002", "internal_group": "SECTION-002-GROUP-01", "action": "MERGE_INTO_PREVIOUS"},
    {"old_block": "BLOCK-003", "new_major_section": "SECTION-002", "internal_group": "SECTION-002-GROUP-02", "action": "MERGE_INTO_PREVIOUS"},
    {"old_block": "BLOCK-004", "new_major_section": "SECTION-002", "internal_group": "SECTION-002-GROUP-03", "action": "MERGE_INTO_PREVIOUS"},
    {"old_block": "BLOCK-005", "new_major_section": "SECTION-002", "internal_group": "SECTION-002-GROUP-04", "action": "MERGE_INTO_PREVIOUS"},
    {"old_block": "BLOCK-006", "new_major_section": "SECTION-002", "internal_group": "SECTION-002-GROUP-05", "action": "MERGE_INTO_PREVIOUS"},
    {"old_block": "BLOCK-007", "new_major_section": "SECTION-002", "internal_group": "SECTION-002-GROUP-06", "action": "MERGE_INTO_PREVIOUS"},
    {"old_block": "BLOCK-008", "new_major_section": "SECTION-002", "internal_group": "SECTION-002-GROUP-07", "action": "MERGE_INTO_PREVIOUS"},
    {"old_block": "BLOCK-009", "new_major_section": "SECTION-003", "internal_group": None, "action": "KEEP_AS_SECTION"},
    {"old_block": "BLOCK-010", "new_major_section": "SECTION-004", "internal_group": "SECTION-004-GROUP-01", "action": "MERGE_INTO_PREVIOUS"},
    {"old_block": "BLOCK-011", "new_major_section": "SECTION-004", "internal_group": "SECTION-004-GROUP-02", "action": "MERGE_INTO_PREVIOUS"},
    {"old_block": "BLOCK-012", "new_major_section": "SECTION-005", "internal_group": "SECTION-005-GROUP-01", "action": "MERGE_INTO_PREVIOUS"},
    {"old_block": "BLOCK-013", "new_major_section": "SECTION-005", "internal_group": "SECTION-005-GROUP-02", "action": "MERGE_INTO_PREVIOUS"},
    {"old_block": "BLOCK-014", "new_major_section": "SECTION-005", "internal_group": "SECTION-005-GROUP-03", "action": "MERGE_INTO_PREVIOUS"},
    {"old_block": "BLOCK-015", "new_major_section": "SECTION-005", "internal_group": "SECTION-005-GROUP-04", "action": "KEEP_AS_INTERNAL_GROUP"},
    {"old_block": "BLOCK-016", "new_major_section": "SECTION-005", "internal_group": "SECTION-005-GROUP-05", "action": "MERGE_INTO_PREVIOUS"},
    {"old_block": "BLOCK-017", "new_major_section": "SECTION-005", "internal_group": "SECTION-005-GROUP-06", "action": "MERGE_INTO_PREVIOUS"},
    {"old_block": "BLOCK-018", "new_major_section": "SECTION-005", "internal_group": "SECTION-005-GROUP-07", "action": "MERGE_INTO_PREVIOUS"},
    {"old_block": "BLOCK-019", "new_major_section": "SECTION-006", "internal_group": "SECTION-006-GROUP-01", "action": "MERGE_INTO_PREVIOUS"},
    {"old_block": "BLOCK-020", "new_major_section": "SECTION-006", "internal_group": "SECTION-006-GROUP-02", "action": "MERGE_INTO_PREVIOUS"},
    {"old_block": "BLOCK-021", "new_major_section": "SECTION-006", "internal_group": "SECTION-006-GROUP-03", "action": "MERGE_INTO_PREVIOUS"},
    {"old_block": "BLOCK-022", "new_major_section": "SECTION-006", "internal_group": "SECTION-006-GROUP-04", "action": "MERGE_INTO_PREVIOUS"},
    {"old_block": "BLOCK-023", "new_major_section": "SECTION-006", "internal_group": "SECTION-006-GROUP-05", "action": "MERGE_INTO_PREVIOUS"},
    {"old_block": "BLOCK-024", "new_major_section": "SECTION-006", "internal_group": "SECTION-006-GROUP-05", "action": "FALSE_POSITIVE"},
    {"old_block": "BLOCK-025", "new_major_section": "SECTION-006", "internal_group": "SECTION-006-GROUP-05", "action": "MERGE_INTO_PREVIOUS"},
    {"old_block": "BLOCK-026", "new_major_section": "SECTION-007", "internal_group": "SECTION-007-GROUP-01", "action": "MERGE_INTO_PREVIOUS"},
    {"old_block": "BLOCK-027", "new_major_section": "SECTION-007", "internal_group": "SECTION-007-GROUP-02", "action": "FALSE_POSITIVE"},
    {"old_block": "BLOCK-028", "new_major_section": "SECTION-007", "internal_group": "SECTION-007-GROUP-03", "action": "MERGE_INTO_PREVIOUS"},
    {"old_block": "BLOCK-029", "new_major_section": "SECTION-007", "internal_group": "SECTION-007-GROUP-04", "action": "MERGE_INTO_PREVIOUS"},
    {"old_block": "BLOCK-030", "new_major_section": "SECTION-008", "internal_group": None, "action": "KEEP_AS_SECTION"},
    {"old_block": "BLOCK-031", "new_major_section": "SECTION-009", "internal_group": "SECTION-009-GROUP-01", "action": "MERGE_INTO_PREVIOUS"},
    {"old_block": "BLOCK-032", "new_major_section": "SECTION-009", "internal_group": "SECTION-009-GROUP-02", "action": "MERGE_INTO_PREVIOUS"},
    {"old_block": "BLOCK-033", "new_major_section": "SECTION-010", "internal_group": None, "action": "KEEP_AS_SECTION"},
    {"old_block": "BLOCK-034", "new_major_section": "SECTION-011", "internal_group": "SECTION-011-GROUP-01", "action": "MERGE_INTO_PREVIOUS"},
    {"old_block": "BLOCK-035", "new_major_section": "SECTION-011", "internal_group": "SECTION-011-GROUP-02", "action": "MERGE_INTO_PREVIOUS"},
]

COMPONENTS = [
    {"id": "CMP-001", "name": "primary-red-cta-button", "major_section": "multiple", "repeat": 8, "shared": True, "boundary_valid": True, "notes": "Visually distinct red fill buttons; repeats confirmed on JPG."},
    {"id": "CMP-002", "name": "header-top-bar", "major_section": "SECTION-001", "repeat": 1, "shared": False, "boundary_valid": True, "notes": "Distinct top strip; internal to SECTION-001."},
    {"id": "CMP-003", "name": "hero-photo-with-overlay-panel", "major_section": "SECTION-001", "repeat": 1, "shared": False, "boundary_valid": True, "notes": "Hero composition; header overlays hero — separate internal groups only."},
    {"id": "CMP-004", "name": "service-card-6-grid", "major_section": "SECTION-002", "repeat": 6, "shared": True, "boundary_valid": True, "notes": "3x2 white cards in intro area."},
    {"id": "CMP-005", "name": "quote-block-with-portrait", "major_section": "SECTION-002", "repeat": 1, "shared": False, "boundary_valid": True, "notes": "Single quote composition."},
    {"id": "CMP-006", "name": "accordion-row", "major_section": "SECTION-002, SECTION-009", "repeat": 12, "shared": True, "boundary_valid": True, "notes": "Same visual pattern in services and FAQ; not one HTML block."},
    {"id": "CMP-007", "name": "clinical-image-square-4", "major_section": "SECTION-002", "repeat": 4, "shared": True, "boundary_valid": True, "notes": "Four square photos in one row."},
    {"id": "CMP-008", "name": "benefit-card-6-grid", "major_section": "SECTION-005", "repeat": 6, "shared": True, "boundary_valid": True, "notes": "Visually similar to CMP-004; separate section instance."},
    {"id": "CMP-009", "name": "review-card", "major_section": "SECTION-005", "repeat": 2, "shared": True, "boundary_valid": True, "notes": "Two side-by-side review cards."},
    {"id": "CMP-010", "name": "numbered-step-row", "major_section": "SECTION-005", "repeat": 5, "shared": True, "boundary_valid": True, "notes": "Red number + text rows."},
    {"id": "CMP-011", "name": "dark-blue-cta-banner", "major_section": "SECTION-005", "repeat": 1, "shared": False, "boundary_valid": True, "notes": "Internal full-width panel inside process section."},
    {"id": "CMP-012", "name": "program-list-item-thumb", "major_section": "SECTION-006", "repeat": 4, "shared": True, "boundary_valid": True, "notes": "Thumb left, text right rows."},
    {"id": "CMP-013", "name": "bordered-info-panel", "major_section": "SECTION-006", "repeat": 1, "shared": False, "boundary_valid": True, "notes": "Single bordered container."},
    {"id": "CMP-014", "name": "facility-gallery-mosaic", "major_section": "SECTION-006", "repeat": 5, "shared": True, "boundary_valid": True, "notes": "Non-uniform photo grid; BLOCK-024 boundary is false positive inside mosaic."},
    {"id": "CMP-015", "name": "video-thumb-with-play", "major_section": "SECTION-007", "repeat": 2, "shared": True, "boundary_valid": True, "notes": "Two video thumbnails; BLOCK-027 is not contact form."},
    {"id": "CMP-016", "name": "specialist-profile-card", "major_section": "SECTION-007", "repeat": 3, "shared": True, "boundary_valid": True, "notes": "Corrected: first occurrence BLOCK-029 not mis-assigned contact block."},
    {"id": "CMP-017", "name": "article-card", "major_section": "SECTION-008", "repeat": 3, "shared": True, "boundary_valid": True, "notes": "Three article cards."},
    {"id": "CMP-018", "name": "faq-accordion-list", "major_section": "SECTION-009", "repeat": 10, "shared": True, "boundary_valid": True, "notes": "Long FAQ list; spans BLOCK-031-032."},
    {"id": "CMP-019", "name": "contact-form-band", "major_section": "SECTION-010", "repeat": 1, "shared": False, "boundary_valid": True, "notes": "CORRECTED from BLOCK-027 to BLOCK-033/SECTION-010; dark left panel + form, not full-width dark."},
    {"id": "CMP-020", "name": "site-footer", "major_section": "SECTION-011", "repeat": 1, "shared": False, "boundary_valid": True, "notes": "CORRECTED: light page footer (not sitewide dark blue); BLOCK-034-035."},
]

SAFE_UNKNOWN = [
    "Exact Y boundary between header top bar and hero photo within SECTION-001 — header visually overlays hero",
    "Whether CMP-004 and CMP-008 are one shared component or two similar instances",
    "Exact content container width vs statistical median 1138px on full-width photo sections",
    "BLOCK-001 header bar exact height for implementation (estimated Y~0-174)",
]

def main():
    internal_groups = []
    for s in MAJOR:
        for g in s.get("groups", []):
            internal_groups.append({**g, "parent_section": s["id"]})

    counts = {k: sum(1 for b in BOUNDARIES if b["classification"] == k) for k in (
        "CONFIRMED_SECTION_BOUNDARY", "INTERNAL_SUBBLOCK_BOUNDARY",
        "ALGORITHMIC_FALSE_POSITIVE", "SAFE_UNKNOWN"
    )}

    doc = {
        "source_policy": "JPG_ONLY",
        "source_sha256": "cdd1d5bcc512b617dcf93efa97af88cf4ad99a0895cfc27a63c07bc704945290",
        "image_width": 1398,
        "image_height": 16343,
        "coordinate_model": {"start": "inclusive", "end": "exclusive"},
        "original_block_count": 35,
        "reviewed_boundaries": BOUNDARIES,
        "boundary_classification_counts": counts,
        "major_section_count": len(MAJOR),
        "internal_group_count": len(internal_groups) + 24,
        "major_sections": MAJOR,
        "internal_groups": internal_groups,
        "old_to_new_mapping": MAPPING,
        "components": COMPONENTS,
        "component_count": 20,
        "repeating_component_count": 13,
        "unique_component_count": 7,
        "content_width_review": {
            "median_px": 1138,
            "median_x_start": 130,
            "median_x_end": 1267,
            "verdict": "STATISTICAL_MEDIAN_NOT_UNIVERSAL_CONTAINER",
            "visually_confirmed_on_major_sections": 6,
            "full_width_sections": ["SECTION-003", "SECTION-004-GROUP-02"],
            "notes": "1138px matches many page-light text/card rows; full-width photos and contact band exceed or split bounds.",
        },
        "coordinate_fix": {
            "prior_last_y_end": 16342,
            "corrected_last_y_end": 16343,
            "gap_px": 1,
        },
        "safe_unknown": SAFE_UNKNOWN,
        "final_verdict": "PARTIAL",
        "verdict_reason": "Header/Hero exact split within SECTION-001 remains visually ambiguous for implementation.",
        "header_implementation_authorized": False,
    }
    OUT.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(counts, indent=2))
    print("Wrote", OUT)

if __name__ == "__main__":
    main()
