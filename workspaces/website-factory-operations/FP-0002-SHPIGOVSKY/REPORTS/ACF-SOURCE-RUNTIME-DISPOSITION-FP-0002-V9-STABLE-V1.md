# ACF Source/Runtime Disposition — FP-0002 V9 Stable v1

**Date:** 2026-07-18  
**Rule applied:** Do not broadly copy source-only JSON into runtime. PHP registration is canonical where referenced in `FieldGroups.php`.

## Summary

| Class | Count |
|-------|------:|
| Synced (present in source + runtime) | 23 |
| Source-only | 8 |
| Runtime-only product JSON | 0 |
| Theme/plugin product DIFF after canonization | 0 |

## Source-only groups

| Filename | Group key | Label | Active in JSON | PHP registration | Sync decision | Notes |
|----------|-----------|-------|----------------|------------------|---------------|-------|
| group_fp02_block_final_form.json | group_fp02_block_final_form | Reusable Block - Final Form | true | Yes (`FieldGroups.php`) | RETAIN_SOURCE_ONLY | PHP owns registration; runtime JSON not required |
| group_fp02_block_specialists.json | group_fp02_block_specialists | Reusable Block - Specialists | true | Yes | RETAIN_SOURCE_ONLY | Same |
| group_fp02_page_institutional_child.json | group_fp02_page_institutional_child | Page - Institutional Child | true | Yes | RETAIN_SOURCE_ONLY | Same |
| group_fp02_page_legal.json | group_fp02_page_legal | Page - Legal | true | Yes | RETAIN_SOURCE_ONLY | Same |
| group_fp02_page_ocentre_hub.json | group_fp02_page_ocentre_hub | Page - O-Centre Hub | true | Yes | RETAIN_SOURCE_ONLY / ACCEPTED_DEFERRED | Present in dirty source; runtime depends on PHP; admin FE validated in E61/E62C |
| group_fp02_service_faq.json | group_fp02_service_faq | Service - FAQ | true | Yes | RETAIN_SOURCE_ONLY | Legacy/FAQ surface; PHP registered |
| group_fp02_service_relationships.json | group_fp02_service_relationships | Service - Relationships | false | Yes | RETAIN_SOURCE_ONLY_DISABLED | Intentionally inactive (E62C hide) |
| group_fp02_service_structured_sections.json | group_fp02_service_structured_sections | Service - Structured Sections | false | Yes | RETAIN_SOURCE_ONLY_DISABLED | Intentionally inactive (E62C hide) |

## Decision

No source-only JSON was copied into runtime during Stable v1 closeout.  
No RELEASE_BLOCKER ACF gaps observed on validated admin/frontend surfaces.

## SAFE UNKNOWN

- Exact ACF Extended / DB-stored group duplication inventory beyond filesystem JSON: not fully re-audited in E63; prior waves soft-disabled duplicates.
