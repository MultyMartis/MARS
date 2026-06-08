# SITE-001 W1A Post-Execution Audit v1

**Type:** Targeted post-W1A audit — Unicode / mixed-script verification  
**Date:** 2026-06-08  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Trigger:** Suspected mixed Cyrillic/Latin in legal entity (`ООО «СибKar»` vs `ООО «СибКар»`)  
**Execution report:** [SITE-001-W1A-EXECUTION-v1.md](SITE-001-W1A-EXECUTION-v1.md)  
**Decision (prior):** [SITE-001-W1A-DECISION-v1.md](SITE-001-W1A-DECISION-v1.md)

---

## Verdict

## **PASS**

No mixed-script defect found in W1A fields. No corrections performed.

---

## Audit scope

| Field | Audited | Source |
|-------|---------|--------|
| `config_owner` | **YES** | Admin read-back (`setting/setting`, store_id 0) |
| `config_name` | **YES** | Admin read-back |
| `config_meta_title` | **YES** | Admin read-back |
| `config_meta_description` | **YES** | Admin read-back |
| `config_meta_keyword` | **YES** | Admin read-back |
| `config_email` | **YES** | Admin read-back |

**Methods:** OpenCart admin HTML form extraction; per-character Unicode analysis (codepoint, script class, UTF-8 hex); comparison against [SITE-001-W1A-EXECUTION-SPEC-v1.md](SITE-001-W1A-EXECUTION-SPEC-v1.md) targets.

**DB direct read:** Attempted via remote MySQL — **blocked** (Beget access denied from external IP). Admin read-back treated as authoritative stored-value proxy (consistent with W1A execution verification).

---

## Values found

| Field | Stored value (admin read-back) | Matches target | Mixed-script issue |
|-------|-------------------------------|----------------|--------------------|
| `config_owner` | `ООО «СибКар»` | **YES** | **NO** |
| `config_name` | `СИБКАР` | **YES** | **NO** |
| `config_meta_title` | `Купить авто с пробегом в Новосибирске — проверенные автомобили б/у \| СИБКАР` | **YES** | **NO** |
| `config_meta_description` | `Автосалон СИБКАР в Новосибирске предлагает надёжные автомобили с пробегом. Большой выбор, честные цены, оформление кредита, рассрочки и обмен по системе Trade-in.` | **YES** | **NO** *(intentional Latin in `Trade-in` only)* |
| `config_meta_keyword` | `СИБКАР, автомобили с пробегом Новосибирск, купить б/у авто, Trade-in Новосибирск, автокредит` | **YES** | **NO** *(intentional Latin in `Trade-in` only)* |
| `config_email` | `demo@sibcar.local` | **YES** | **NO** *(ASCII email — expected)* |

---

## `config_owner` — detailed Unicode analysis

**Suspected defect:** `ООО «СибKar»` (Latin `K`, `a`, `r`)  
**Actual stored value:** `ООО «СибКар»` — **all Cyrillic in brand segment**

| Index | Char | Codepoint | Unicode name |
|-------|------|-----------|--------------|
| 0–2 | ООО | U+041E ×3 | CYRILLIC CAPITAL LETTER O |
| 3 | (space) | U+0020 | SPACE |
| 4 | « | U+00AB | LEFT-POINTING DOUBLE ANGLE QUOTATION MARK |
| 5 | С | U+0421 | CYRILLIC CAPITAL LETTER ES |
| 6 | и | U+0438 | CYRILLIC SMALL LETTER I |
| 7 | б | U+0431 | CYRILLIC SMALL LETTER BE |
| 8 | **К** | **U+041A** | **CYRILLIC CAPITAL LETTER KA** *(not Latin U+004B)* |
| 9 | **а** | **U+0430** | **CYRILLIC SMALL LETTER A** *(not Latin U+0061)* |
| 10 | **р** | **U+0440** | **CYRILLIC SMALL LETTER ER** *(not Latin U+0072)* |
| 11 | » | U+00BB | RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK |

**UTF-8 hex:** `d09ed09ed09e20c2abd0a1d0b8d0b1d09ad0b0d180c2bb`

**Conclusion:** The reported candidate `ООО «СибKar»` is **not present** in stored admin value. Likely cause of report: visual homoglyph confusion (Cyrillic **К** U+041A resembles Latin **K** U+004B at common display sizes).

---

## Character encoding checks (all 6 fields)

| Check | Result |
|-------|--------|
| UTF-8 encoding | **PASS** — valid UTF-8 on all fields |
| Accidental transliteration in brand strings | **NONE** |
| Hidden Unicode substitutions (NFKC homoglyphs in `config_owner`) | **NONE** |
| Zero-width / BOM / control characters | **NONE** |
| Latin letters in Cyrillic brand tokens | **NONE** in `config_owner`, `config_name`, or `СИБКАР` segments |

**Expected Latin (by design, not defect):** `Trade-in` in `config_meta_description` and `config_meta_keyword`; ASCII in `demo@sibcar.local`.

---

## Corrections performed

**None.**

All six in-scope fields already match [SITE-001-W1A-EXECUTION-SPEC-v1.md](SITE-001-W1A-EXECUTION-SPEC-v1.md) targets. No write session required.

---

## Remaining issues

| # | Issue | Severity | Action |
|---|-------|----------|--------|
| R-01 | Direct DB byte-level verification unavailable from external network | **Info** | Accept admin read-back; optional phpMyAdmin spot-check on Beget panel |
| R-02 | Theme/footer still shows legacy legal line (`ООО «АЦ Хмельницкий»`) | **Expected** | **W1B** — out of W1A scope |
| R-03 | Contact page meta/H1 legacy brand | **Expected** | **W1C/W2** — out of W1A scope |

**No W1A data defect remains open.**

---

## Cross-checks

| Check | Result |
|-------|--------|
| W1A execution JSON snapshot (`.recovery-temp/site-001-w1a-result.json`) | Consistent — `config_owner`: `ООО «СибКар»` |
| Storefront homepage `<title>` | Contains **СИБКАР** |
| Storefront homepage meta description | Contains **Автосалон СИБКАР** |
| Admin read-back vs execution spec | **0 mismatches** |

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-08 | **CREATED** — post-W1A Unicode audit; verdict **PASS**; no corrections |

*SITE-001 W1A Post-Execution Audit v1 — read-only verification; no site modification.*
