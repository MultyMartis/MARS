# Ad type literal fix v0.5

**Phase:** ORCA Commander Ad Type Literal Fix v0.5  
**Scope:** Sheet1 ZIP patch only · col **2** on export rows **16+**  
**Posture:** Post–Cycle 8 operational-first · human-operated re-import

---

## Commander symptom (post–v0.4)

Warning: *«В некоторых строках не проставлен столбец «Тип объявления»»* — rows 16, 19, 23, 25–30 interpreted as text-graphic without explicit type.

**Cause:** v0.4 wrote transport mask `-` (or empty) in col 2 instead of the Commander dictionary literal.

---

## Fix

| Column | Header | v0.4 | v0.5 |
|--------|--------|------|------|
| **2** | Тип объявления | `-` | **Текстово-графическое** |

**Preserved from v0.4 (must not regress):**

- cols **64–66** (image / creative / moderation) → empty on rows 16+
- no image URLs in export block
- display URL short paths (v0.3)
- geo col 52 (v0.4)
- symbol normalization ×→x (v0.4)
- stale row removal after `lastExportRow`

---

## Implementation

| Module | Change |
|--------|--------|
| [mapping.js](mapping.js) | `SEARCH_ONLY_AD_TYPE_TRANSPORT = "Текстово-графическое"` |
| [sheet1-xml-builder.js](sheet1-xml-builder.js) | unchanged — patches `ads.ad_type` from `fillRow.ad_type_transport` |
| [commander-header-map-v0.json](commander-header-map-v0.json) | notes updated |

---

## Output

```bash
cd projects/orca/ppc/triumph-manipulator/tools/exporter-cli
npm run export:sheet1-patch:v0.5
```

**File:** `output/triumph-sheet1-patch-ad-type-v0.5.xlsx`

See [sample-ad-type-v0.5-run.md](sample-ad-type-v0.5-run.md).

---

## Human re-import checklist

- [ ] No warning about missing «Тип объявления»
- [ ] No popup about images/creatives in import data
- [ ] Campaign, groups, ads, phrases, fastlinks, display URL still valid

---

## SAFE UNKNOWN

- Whether Commander treats explicit «Текстово-графическое» + empty cols 64–66 differently from template-inherited type + cleared images — **requires human re-import**
- Whether combinatorics cols 26–35 still carry graphic metadata without popup — **not cleared** in v0.5
