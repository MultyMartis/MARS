# MIG Research Pack — Draft

## Session Header

| Field | Value |
|-------|-------|
| Session ID | mig-20260603-9a166b |
| Stage | draft |
| Created | 2026-06-04T14:00:00.000Z |
| Operator | op-or10-verify |
| Niche | manipulator rental |
| Region | Krasnodar Krai |
| City | Krasnodar |
| Business type | local_service |
| Search engine | yandex |
| Device | mobile |
| SERP mode | manual |
| MIG phase | 2 |

## Queries

### Seed queries

- аренда манипулятора Краснодар

### Query used (single SERP pass)

- аренда манипулятора Краснодар

### Query coverage notes

- Single-query pass: аренда манипулятора Краснодар
- Seed queries (1): аренда манипулятора Краснодар

## SERP Summary

| Field | Value |
|-------|-------|
| Query | аренда манипулятора Краснодар |
| Captured at | 2026-06-04T14:00:00.000Z |
| SERP type | local commercial |
| Maps / local pack | present |
| Ads | Top ads: 1; Bottom ads: 0; Patterns: price from |

### Aggregators

- 2GIS

### Marketplaces

- Avito

### Offer patterns

- SAFE UNKNOWN

### CTA patterns

- SAFE UNKNOWN

### Landing observations

- SAFE UNKNOWN

### Organic results (normalized)

1. Манипулятор-Сервис Краснодар — https://manipulator-krd.ru/
2. Кран-Логистик — https://kran-logistik.ru/uslugi
3. Авито — аренда спецтехники — https://www.avito.ru/krasnodar/spetstehnika

## Competitor Observations

| Field | Value |
|-------|-------|
| Discovery pass | 2026-06-03T19:59:12.277Z |
| Phase | 2 |
| Query ref | аренда манипулятора Краснодар |
| Section grade | B |
| Coverage | complete |
| Competitor count | 3 |

| ID | Name | Domain | Types | Strength | Grade | First query |
|----|------|--------|-------|----------|-------|-------------|
| mig-20260603-9a166b-c001 | Манипулятор-Сервис Краснодар | manipulator-krd.ru | serp_organic | single | B | аренда манипулятора Краснодар |

**Rules:** rule_serp_organic_top_n

| mig-20260603-9a166b-c002 | Кран-Логистик | kran-logistik.ru | serp_organic | single | B | аренда манипулятора Краснодар |

**Rules:** rule_serp_organic_top_n

| mig-20260603-9a166b-c003 | Авито — аренда спецтехники | avito.ru | serp_organic, aggregator, marketplace_listing | multi_surface | B | аренда манипулятора Краснодар |

**Rules:** rule_serp_organic_top_n, rule_aggregator_domain, rule_marketplace_domain, rule_multi_surface

### Discovery coverage

- SAFE UNKNOWN — multi-query coverage not computed (single-query session or legacy path)

### Cross-query recurrence

- SAFE UNKNOWN — cross-query recurrence not evaluated

## Website capture summary

| Snapshot | Competitor | URL | Status | Grade | Render |
|----------|------------|-----|--------|-------|--------|
| mig-20260603-9a166b-ws001 | mig-20260603-9a166b-c001 | https://manipulator-krd.ru/ | failed | X | unknown |
| mig-20260603-9a166b-ws002 | mig-20260603-9a166b-c002 | https://kran-logistik.ru/uslugi | failed | X | unknown |

Session coverage: **minimal** · Section grade: **X**

## Website observations

### mig-20260603-9a166b-ws001 (manipulator-krd.ru)

- Ref: `snapshots/sites/mig-20260603-9a166b-ws001/website_snapshot.json`

### mig-20260603-9a166b-ws002 (kran-logistik.ru)

- Ref: `snapshots/sites/mig-20260603-9a166b-ws002/website_snapshot.json`

## Offer observations

- SAFE UNKNOWN — no offer strings visible on captured pages

## Pricing signals (visible)

- No pricing signals visible on captured pages

## CTA observations

- SAFE UNKNOWN — no CTA elements visible on captured pages

## Trust observations

- SAFE UNKNOWN — no trust phrases visible on captured pages


## Artifact Registry

| Artifact | Path | Notes |
|----------|------|-------|
| serp_result | serp_result.json | SERP capture SoT |
| competitors | competitors.json | Competitor discovery SoT (3 entities) |
| website_snapshots | website_snapshots.json | Website acquisition index (2 snapshots) |
| research_pack_draft | research_pack.draft.md | Human-readable projection |

### Competitor artifact reference

| Field | Value |
|-------|-------|
| Artifact file | competitors.json |
| Discovery pass | 2026-06-03T19:59:12.277Z |
| Competitor count | 3 |
| Section grade | B |
| Coverage | complete |
| Discovery mode | SAFE UNKNOWN |

### Website snapshots reference

| Field | Value |
|-------|-------|
| Artifact file | website_snapshots.json |
| Snapshot count | 2 |
| Website section grade | X |

Full competitor and snapshot objects remain in session artifacts — this pack is a projection only.

## SAFE UNKNOWN

- fixture-only manual SERP for OR-10 verification

### Website acquisition gaps

- Website capture partial: 1 competitor(s) skipped (see url_plan)

### Landing analysis gaps

- Landing Analysis pass not executed — structured landing analysis pending (legacy snapshot projection used)

## Status

Status: **draft**

This pack includes SERP, competitor discovery, and website capture projections (legacy snapshot path). Human review required before approval or ORCA handoff.

