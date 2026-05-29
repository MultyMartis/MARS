# DUPLICATE ADS AUDIT v1

**Label:** `orca-commander-duplicate-ads-audit-v1`  
**Date:** 2026-05-29  
**Lane:** B — ORCA Duplicate Ads Audit  
**Mode:** Diagnostic only — no JSON/XLSX edits, no regeneration, no Commander import

---

## Source of truth chain

| Layer | Path | Role |
|-------|------|------|
| PPC instance | `projects/orca/ppc/triumph-manipulator/schema/instances/triumph-s-tier-draft-v1.json` | Canonical ad entities (`ad_id`, headlines, body, `landing_url`) |
| Draft builder | `projects/orca/ppc/triumph-manipulator/tools/_build-full-cycle-draft.js` | Regenerates the same graph (20 ads / 12 groups) |
| Exporter mapping | `projects/orca/ppc/triumph-manipulator/tools/exporter-cli/mapping.js` | `mapDocument()` + `mapTemplateFillRows()` |
| Commander transport | `tools/exporter-cli/sheet1-patch-export.js` → `sheet1-xml-builder.js` | 1:1 write of `templateFillRows` into sheet **Тексты** |
| On-disk XLSX (read-only) | `tools/exporter-cli/output/triumph-sheet1-patch-full-cycle-v1.xlsx` (82 rows) · `…-full-cycle-v1.1.xlsx` (108 rows) | Human import artifacts — **not modified** |

---

## Executive finding

**Root cause: exporter-cli `mapTemplateFillRows()` — keyword × ad Cartesian product (Source C).**

Each unique ad is repeated **once per keyword phrase** on every Commander transport row. Direct Commander treats each populated text row as a separate ad inside the group, so operators see **N copies** of the same headline/body/URL where **N = keyword count** for that group.

**Not caused by:** duplicate entities in JSON (Source A) or duplication inside `_build-full-cycle-draft.js` (Source B).

**Amplified by:** sheet1 XLSX patch (Source D) — writes one XML row per fill row without deduplicating ad text.

---

## Phase 1 — Groups summary

| group_id | group_name | ads_count | keywords_count | template_fill_rows (ads × keywords) |
|----------|------------|-----------|----------------|-------------------------------------|
| `grp_fc01_5ton` | 01 — Манипулятор 5 тонн | 2 | 6 | 12 |
| `grp_fc02_bytovka` | 02 — Перевозка бытовок | 2 | 5 | 10 |
| `grp_fc03_stroymaterialy` | 03 — Доставка стройматериалов | 1 | 5 | 5 |
| `grp_fc04_yurlica` | 04 — Манипулятор для юрлиц | 2 | 4 | 8 |
| `grp_fc05_6x6` | 05 — Манипулятор-вездеход 6x6 | 1 | 5 | 5 |
| `grp_fc06_oborudovanie` | 06 — Перевозка оборудования | 2 | 5 | 10 |
| `grp_fc07_konteynery` | 07 — Перевозка контейнеров | 1 | 5 | 5 |
| `grp_fc08_armatura` | 08 — Перевозка арматуры | 2 | 5 | 10 |
| `grp_fc09_kirpich` | 09 — Доставка кирпича и блоков | 1 | 5 | 5 |
| `grp_fc10_fbs` | 10 — ФБС и ЖБИ | 2 | 6 | 12 |
| `grp_fc11_kray` | 11 — Манипулятор по Краснодарскому краю | 2 | 6 | 12 |
| `grp_fc12_zakaz` | 12 — Заказать манипулятор | 2 | 7 | 14 |

**Totals:** 12 groups · 20 ads (JSON) · 61 keywords · **108** `templateFillRows` (current instance).

---

## Phase 2 — Ad inventory (JSON / logical export)

All 20 ads have unique `ad_id` per group. `mapDocument().ads` emits **20 rows** (one per `ad_id`, deduped).

**Example (reported case) — `grp_fc01_5ton` / `ad_fc01_a2`:**

| Field | Value |
|-------|-------|
| headline_1 | Манипулятор 5т - подача на объект |
| headline_2 | Краснодар и край |
| body | Заказать манипулятор 5 т. Стрела 3 т. Звонок и расчёт по адресу. |
| final_url | `https://manipulator-triumph.ru/5-tonn.html` |
| Instances in JSON | **1** |
| Instances in `templateFillRows` | **6** (= 6 keywords) |
| Instances expected in Commander | **1** |

Commander may display em dash (`—`) where JSON/export uses hyphen (`-`) after `normalizeTransportText()` — content-equivalent for duplicate detection.

---

## Phase 3 — Duplicate signatures (export transport)

**Criterion:** same `headline_1` + `headline_2` + `description` + `landing_url` within one group.

| Metric | JSON instance | `templateFillRows` (exporter-cli) |
|--------|---------------|-----------------------------------|
| Duplicate signatures | **0** | **20** (every ad in every multi-keyword group) |
| Extra transport rows | 0 | **88** (108 − 20) |
| Groups affected | 0 | **12 / 12** |

Full per-ad matrix: [DUPLICATE-ADS-MATRIX-v1.md](./DUPLICATE-ADS-MATRIX-v1.md).

---

## Phase 4 — Source attribution

| Source | Check | Result |
|--------|-------|--------|
| **A** — `triumph-s-tier-draft-v1.json` | Content-level dedupe inside groups | **Clear** — 20 distinct ads, 0 duplicate signatures |
| **B** — `_build-full-cycle-draft.js` | Same graph as JSON generator | **Clear** — defines 1 entity per `ad_id`, no copy loop |
| **C** — `exporter-cli` / `mapTemplateFillRows()` | Nested `for (ad) { for (kw) { push row } }` | **ROOT CAUSE** — multiplies ad text by keyword count |
| **D** — Commander XLSX / sheet1 patch | Rows written 1:1 from `templateFillRows` | **Transport channel** — does not add a second multiplication; propagates C |

### Evidence (mapping.js)

Documented row model:

```394:395:projects/orca/ppc/triumph-manipulator/tools/exporter-cli/mapping.js
 * Flat Commander "Тексты" rows: stable keyword×ad combinations per group.
```

Nested loops that duplicate ad columns on every keyword row:

```442:491:projects/orca/ppc/triumph-manipulator/tools/exporter-cli/mapping.js
      for (const ad of adList) {
        // ... fastlinks, callouts ...
        for (const kw of kwList) {
          const phrase = kw
            ? normalizeTransportText(normalizePhraseForTransport(kw.phrase || ""))
            : "";
          // ...
          fillRows.push({
            // ...
            headline_1: ad ? normalizeTransportText(ad.headline_1 || "") : "",
            headline_2: ad ? normalizeTransportText(ad.headline_2 || "") : "",
            description: ad ? normalizeTransportText(ad.description || "") : "",
            landing_url: ad ? collapseWhitespace(ad.landing_url || "") : "",
            // ...
          });
        }
      }
```

Contrast: `mapDocument()` ad sheet uses per-`ad_id` dedupe (`seenAds`) — **no** keyword multiplication.

Operator docs align: `sample-template-fill-run.md` — *«one row per keyword × ad per group»*.

---

## XLSX row count note (SAFE UNKNOWN vs proven)

| Artifact | Data rows (sheet1, from row 16) | Matches current JSON (108)? |
|----------|----------------------------------|-----------------------------|
| `triumph-sheet1-patch-full-cycle-v1.xlsx` | **82** (`_validate-full-cycle-v1.js`) | **No** — older/smaller keyword set |
| `triumph-sheet1-patch-full-cycle-v1.1.xlsx` | **108** (`_validate-full-cycle-v1.1.js`) | **Yes** |

Duplicate **mechanism** is identical; only **scale** differs with keyword count. Commander import file version = **UNKNOWN** unless operator confirms which XLSX was imported.

---

## Severity

| Level | Condition | Groups / ads |
|-------|-----------|--------------|
| **Critical** | ≥6 identical ad copies in group | `grp_fc01_5ton`, `grp_fc10_fbs`, `grp_fc11_kray`, `grp_fc12_zakaz` (7 for zakaz) |
| **High** | 5 copies (4 duplicates) | Remaining multi-keyword groups |
| **Medium** | 4 copies (3 duplicates) | `grp_fc04_yurlica` only |

Campaign-level impact: **all 12 groups** show duplicate ads after template-fill import.

---

## Fix recommendation (documentation only — not applied)

1. **Exporter row model (preferred):** Split Commander transport into **ad-only rows** (headlines + URL, empty or marker phrase) and **keyword-only rows** (phrase + match, no ad text) per Yandex Commander flat-table conventions — *or* set col 1 «Доп. объявление группы» so Commander links phrases to existing ads (currently **not set** in v0 — see `template-fill-notes-v0.md`).
2. **Alternative:** Export **one** combined row per ad (single primary keyword in phrase column; additional keywords via separate keyword-only rows or post-import UI).
3. **Operator workaround (immediate):** After import, delete redundant ads in Commander UI (keep one copy per unique headline triple + URL per group). Count to remove per group ≈ `ads_count × (keywords_count − 1)` for current JSON (**88** redundant ad entities total).
4. **Do not** “fix” by deleting keywords in JSON — keywords are intentional; the bug is **transport shape**, not semantic data.

---

## Limitations

- No live Commander API dump — findings inferred from export logic + operator report.
- No re-import test in this pass.
- Logical multi-sheet export (`mapDocument().ads`) is **not** the import path used for full-cycle Commander runs (sheet1 patch uses `templateFillRows`).

---

## Related artifacts

- [DUPLICATE-ADS-MATRIX-v1.md](./DUPLICATE-ADS-MATRIX-v1.md) — per-group/per-ad matrix
- `projects/orca/ppc/triumph-manipulator/tools/exporter-cli/template-fill-notes-v0.md`
- `projects/orca/ppc/triumph-manipulator/runs/full-cycle-v1/export-summary-v1.md`
