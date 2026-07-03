# FP-0002 V9-06D.4 RERUN Minimal Content Seed Apply Plan v1

**Phase:** V9-06D.4 RERUN  
**Authority:** D.3 minimal visual content seed plan + operator authorization for HEAD `1b0fba0e854071d635766e3912802c38b860bf43`

## Scope

Authorized objects only:

| ID | Type | Path |
|---:|---|---|
| 4 | page | `/` |
| 5 | page | `/uslugi/` |
| 20 | page | `/kontakty/` |
| 73 | service | `/uslugi/zavisimosti/` |
| 74 | service | `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` |
| 77 | service | `/uslugi/psihicheskoe-zdorovie/` |
| 84 | service | `/uslugi/rasstroystva-pischevogo-povedeniya/` |

## Write method

- ACF fields via `update_field()` (ACF PRO public API)
- Skeleton/migration meta via `update_post_meta()`
- No native `post_content` / `post_excerpt` changes
- No Options Page writes
- No menu / redirect / rewrite flush

## Field plan summary

### Page 4 — Home

- `home_hero_slides[0].title/text`
- `home_service_nav_items[0..2].title`
- `home_cta_title`, `home_cta_text`
- meta: `migration_status=minimal_seed`, `seeded_by_phase=V9-06D.4`

### Page 5 — Services Hub

- `services_hub_intro`
- `services_hub_query_mode=grouped_by_parent`
- `services_hub_show_placeholders=1`
- meta: `migration_status`, `seeded_by_phase`

### Page 20 — Contacts

- `contacts_address`
- `contacts_phones[0].label/phone`
- `contacts_form_intro`
- meta: `migration_status`, `seeded_by_phase`

### Services 73 / 77 / 84

- `service_layout_variant` (subdivision)
- `hero_lead`
- meta: `migration_status=minimal_seed`, `seeded_by_phase=V9-06D.4`, `skeleton_status=MINIMAL_SEED`

### Service 74

- `service_layout_variant=alcohol_special`
- `hero_lead` (V9 leaf wording)
- `intro_text`
- `signs_items[0].title/text`
- meta: `migration_status`, `seeded_by_phase`, `skeleton_status`

## Safety gates

1. Preflight HEAD sync PASS
2. Runtime identity PASS
3. DB checkpoint PASS
4. Dry-run `SAFE_TO_APPLY_WITH_DB_CHECKPOINT`
5. Apply + authorized object validation PASS
6. Global immutability PASS
7. Rewrite flush NOT PERFORMED

## Result

Applied in local runtime. Evidence under `validation/v9-06d4-minimal-content-seed-rerun/`.
