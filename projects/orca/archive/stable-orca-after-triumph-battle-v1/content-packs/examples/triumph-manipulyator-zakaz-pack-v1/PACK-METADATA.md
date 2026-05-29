# Pack Metadata — triumph-manipulyator-zakaz-pack-v1

```yaml
pack_id: triumph-manipulyator-zakaz-pack-v1
pack_version: v1.0
pack_type: master
project_ref: triumph-manipulator-krasnodar
route_slug: ""  # master hot — canonical URL is /
canonical_url: https://manipulator-triumph.ru/
locale: ru-RU
artifact_state: draft
content_mode: MODE_1
semantic_lock: active  # doctrine + as-built locks; formal handoff still pending
created_at: 2026-05-28
updated_at: 2026-05-28
author_operator: orca-calibration-pack-authoring
```

## Page identity

| Field | Value |
|-------|--------|
| Page name | Аренда манипулятора в Краснодаре |
| Landing type | `master_hot` |
| Intent tier | S — hot general commercial |
| Robots default | `noindex,nofollow` |
| Document title (as-built) | Аренда манипулятора в Краснодаре \| Триумф |
| Meta description (as-built) | Заказать манипулятор 5 т в Краснодаре: борт 5 т, стрела 3 т. Подача по городу и краю. Расчёт по задаче. |

## PPC envelope

| Field | Value |
|-------|--------|
| `campaign_ref` | `triumph-s-tier-draft-v1` |
| `group_id` | `grp_fc12_zakaz` |
| `group_label` | 12 — Заказать манипулятор |
| `display_path` | `zakaz-manip` |
| `blueprint_id` | `01-master-hot-general` |
| `intent_continuity_rule` | Hero — заказ, подача, квалификация задачи |
| `intent_continuity_ack` | **false** (instance JSON — до operator sign-off) |

## Primary ads (instance draft)

| ad_id | headline_1 | headline_2 |
|-------|------------|------------|
| `ad_fc12_a1` | Заказать манипулятор в Краснодаре | Подача на объект |
| `ad_fc12_a2` | Аренда манипулятора Краснодар | Цена по задаче |

**Pack recommendation:** `primary_ad_variant: ad_fc12_a2` until H1 strategy covers A1 — см. `ppc/headline-alignment` via `ppc/intent-continuity.md`.

## Visual semantics bundle (as-built G2)

```yaml
visual_semantics:
  version: v0
  route_id: master_hot
  group_id: grp_fc12_zakaz
  fields:
    hero_priority: capability_first
    trust_mode: operational_proof
    compactness_level: compact
    visual_density: high
    cta_priority: form
    proof_priority: hero_strip
    mobile_critical: [form_submit, capability_scan]
    qualification_mode: hero_notice_plus_tasks
    hero_layout_mode: grid_form_aside
    visual_noise_risk: high
    semantic_focus: [one_machine, use_case_fit]
    conversion_intent_weight: hot
```

**Note:** `qualification_mode` updated vs calibration draft `tasks_section_only` — as-built v5 includes `hero__notice` (см. `content/hero.md`).

## Source artifacts

| Path | Role |
|------|------|
| `projects/orca/ppc/triumph-manipulator/landing-pages/01-master-hot-general.md` | Doctrine blueprint |
| `projects/orca/calibration/triumph-manipulator/` | Implementation calibration |
| `projects/orca/visual-semantics/triumph-calibration/` | Visual drift findings |
| `workspaces/triumph-manipulator-landing-v5/src/pages/index.html` | Section graph |
| `projects/orca/content-packs/examples/triumph-manipulyator-5-tonn-pack-v0.md` | Structural pattern only |

## Section order (as-built)

1. Hero — `v5-ppc/zakaz/screen-01-hero.html`
2. Specs — `screen-02-specs.html`
3. Tasks — `screen-02-tasks.html`
4. Order steps — `screen-02b-order-steps.html`
5. Pricing factors — `screen-02c-pricing-factors.html`
6. Trust + reviews — `v5-page01/screen-03-trust-reviews.html` (shared)
7. B2B — `v5-page01/screen-03b-b2b.html` (shared)
8. Dark proof strip — `v5-page01/dark-proof-strip.html` (shared)
9. FAQ — `screen-04-faq.html`
10. Final CTA + footer — `final-contact-cta.html` + `landing-footer.html`

## Export metadata (future DOCX)

| Field | Value |
|-------|--------|
| `export_format` | docx (planned — pilot currently 5-ton only) |
| `export_profile` | `master-hot-v1` (proposed) |
| `semantic_lock_snapshot` | active (partial artifact trail) |
