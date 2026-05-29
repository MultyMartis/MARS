# ORCA Display URL + Sitelink Routing Fix v0.3 — transport notes

**Phase:** Lane B · PPC transport refinement  
**NOT:** Direct API · runtime · auto-import · orchestration

---

## Commander display URL field (operator-confirmed)

| Constraint | Value |
|------------|-------|
| Field | Sheet **Тексты** col 49 — «Отображаемая ссылка» |
| Content | **Short display path only** — not full URL |
| Max length | **≈ 20** characters |
| Charset | `[a-z0-9-]` kebab-case |
| Forbidden | domain, `http`, `/`, Cyrillic in transport cell |

**Bad (pre-v0.3):** `manipulator-triumph.ru/manipulyator-5-tonn`  
**Good:** `manip-5-tonn`, `perevozka-byt`, `manip-dlya-b2b`

Display path is a **CTR/commercial artifact** — landing URL stays in col 48 unchanged.

---

## mapping.js v0.3

| Function | Role |
|----------|------|
| `normalizeDisplayPathForTransport()` | UTF-8 → ASCII translit, strip domain/slash, kebab-case, max 20 |
| `buildDisplayUrl()` | Returns **path only** for Commander col 49 |
| `normalizeFastlinksForTransport()` | Dedupe title+url **and** duplicate URLs; prefer known production slugs in sort |
| `isProductionFastlinkUrl()` | Slug ∈ production route table |

`exporter_version`: `orca-exporter-cli-display-url-routing-v0.3`

---

## Sitelink routing discipline

Fastlink `url` must map to **real landing slugs** from [landing-routing-schema-v1.md](../../schema/landing-routing-schema-v1.md):

| Slug | Route |
|------|-------|
| `manipulyator-5-tonn` | 5 t capability |
| `perevozka-bytovok` | бытовка use-case |
| `dostavka-stroymaterialov` | стройматериалы |
| `manipulyator-dlya-yurlic` | B2B |
| `manipulyator-vezdehod` | 6×6 |

**BAD:** same URL 3+ times per ad; root `/` as filler; placeholder hosts  
**GOOD:** primary group slug + cross-intent slugs; unique URL per slot (exporter enforces)

---

## Validation cross-reference

- **SY-06** — display path segment ≤ 20  
- **SY-17** — Commander display path format (v0.3)  
- **SY-18** — display path length warn/error thresholds  
- **SY-14** — duplicate fastlink URL (error)  
- **CM-11** — fastlink routing + diversity (v0.3)

---

## Run export

```bash
cd projects/orca/ppc/triumph-manipulator/tools/exporter-cli
npm run export:sheet1-patch:v0.3
```

Output: `output/triumph-sheet1-patch-display-url-routing-v0.3.xlsx`

---

## Human verification checklist

1. Excel opens workbook — no recovery dialog  
2. Col 49 «Отображаемая ссылка» — short paths only (no domain/slash)  
3. All display paths ≤ 20 chars, `[a-z0-9-]` only  
4. Col 48 landing URLs — full `https://manipulator-triumph.ru/.../` unchanged  
5. Fastlink URL columns — production slugs only; no repeated `||` URL segments per ad  
6. Sheet2/sheet3 SHA unchanged vs template (ZIP patch)  
7. Commander import — **human session only**

---

## SAFE UNKNOWN

- Whether Commander splits path_1/path_2 or single combined field on re-export  
- Exact Russian status literals after empty-status export  
- Dedicated pricing/intercity slugs not in v0.3 route table — confirm with site operator before adding URLs
