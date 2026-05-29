# ORCA Commander Import Feedback Fix v0.1

**Phase:** Post-import refinement only · Lane B (External Systems)  
**Posture:** Post–Cycle 8 operational-first · evidence-first · human-operated  
**NOT:** Direct API · runtime · orchestration · autonomous launch

---

## Purpose

Improve Commander import quality after the **first successful import loop** (XLSX → Direct Commander → campaigns/groups/ads/phrases created). Refinements apply at **sheet1 ZIP patch** transport layer only.

---

## Problems addressed (v0.1)

| Issue | Root cause (evidence) | Fix |
|-------|----------------------|-----|
| Group names truncated / merged in Commander | All rows had `Номер группы` = **1** (template inheritance) | Distinct `group_number` per ORCA group (1…5) |
| `---autotargeting` garbage rows | Template row 16 phrase column | Suppress autotarget phrases in mapping + XML patch |
| Stale template rows visible | 103 trailing rows with old transport | Clear writable cells + mask visible cols with `-` |
| Metadata from old campaign | Rows 7–12 untouched in v0 | Patch type, negatives, promotion URL from JSON |
| Status literals unknown | `Draft` / `active` English in cells | Export **empty** status — Commander defaults (**SAFE UNKNOWN** for Russian literals) |
| Extension / display URL noise | Whitespace, domain case | `collapseWhitespace`, lowercase domain in display URL |

---

## Modules changed

| File | Role |
|------|------|
| [mapping.js](mapping.js) | Group name normalization, group ordinals, autotarget filter, status maps, metadata patches |
| [sheet1-xml-builder.js](sheet1-xml-builder.js) | `group_number` column, metadata block patch, stale-row transport mask |
| [sheet1-patch-export.js](sheet1-patch-export.js) | v0.1 label, metadata wiring, feedback stats |
| [commander-header-map-v0.json](commander-header-map-v0.json) | Verified `groups.group_number` → col 6 |

---

## Group naming rules

- Separator: ` — ` (em dash with spaces)
- Prefix: `01` … `05` from stable group order in document
- Strip machine suffixes (`_grp`, `__`)
- **No length truncation** — validation must catch SY-* limits

**Good:** `01 — Манипулятор 5 тонн`  
**Bad:** `01_1__grp`, `01 — Ман 1` (truncation in Commander UI may still occur if group_number wrong)

---

## Autotarget suppression

Patterns cleared (never exported):

- `---autotargeting`
- `---autotarget` (prefix match)

Strategy: **neutralize phrase cell** — do **not** delete `<row>` XML nodes.

---

## Stale-row strategy

Rows `16 + N` … end of template:

1. Clear entity IDs and writable PPC columns  
2. Mask `Название группы`, `Фраза`, headlines, description → `-`  
3. Preserve row structure (survivability-first)

---

## Metadata block (rows 7–12)

| Logical key | Row | Col | Source |
|-------------|-----|-----|--------|
| `campaigns.campaign_type` | 7 | 5 | `search` → `Единая перфоманс-кампания` |
| `campaigns.campaign_negatives` | 9 | 5 | JSON negatives → `-word` list |
| `campaigns.promotion_url` | 11 | 5 | First group `landing_route.final_url` |

**Not patched in v0.1:** order number, currency, Yandex Business org — template defaults remain.

---

## Status normalization

| Source | Exported value | Rationale |
|--------|----------------|-----------|
| `draft` / `active` (ads) | empty | Commander dictionary has no verified English literals |
| `active` (keywords) | empty | Same |

**SAFE UNKNOWN:** Exact Russian status strings Commander expects on import.

---

## Run

```bash
cd projects/orca/ppc/triumph-manipulator/tools/exporter-cli
npm run export:sheet1-patch:feedback
```

Output: `output/triumph-sheet1-patch-feedback-v0.1.xlsx`

See [sample-feedback-fix-run.md](sample-feedback-fix-run.md).

---

## v0.2 addendum — domain + max fastlinks

| Change | Detail |
|--------|--------|
| Production host | `https://manipulator-triumph.ru` (replaces `triumph-krd.ru` in fixtures) |
| Fastlinks doctrine | Target **8** per ad; transport cap `MAX_FASTLINKS_TRANSPORT` in mapping.js |
| Dedupe | `normalizeFastlinksForTransport()` — stable order, title+url dedupe, no truncation |
| Delimiter | `||` unchanged — **SAFE UNKNOWN** for 8-slot Commander cell limits |

See [domain-fastlinks-v0.2-notes.md](domain-fastlinks-v0.2-notes.md).

```bash
npm run export:sheet1-patch:v0.2
```

---

## v0.5 addendum — ad type literal

| Change | Detail |
|--------|--------|
| Commander warning | Missing «Тип объявления» when col 2 = `-` (v0.4) |
| Fix | `SEARCH_ONLY_AD_TYPE_TRANSPORT = "Текстово-графическое"` |
| Preserved | Image/creative cols 64–66 empty (v0.4) — popup must not return |

See [ad-type-literal-fix-v0.5.md](ad-type-literal-fix-v0.5.md).

```bash
npm run export:sheet1-patch:v0.5
```

---

## Distinction (required)

| Layer | Status |
|-------|--------|
| Documented transport refinement | **This phase** |
| Commander import success | **Human-verified** per session — not automated proof |
| Direct API / runtime | **Not claimed** |
