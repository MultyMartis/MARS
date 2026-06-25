# REPORT — MARS SEARCH PPC PRODUCTION — WAVE 2.3 GENUINE LIVE PAID SERP CLOSURE V2

**Date:** 2026-06-24  
**Branch:** `mars/post-cycle8-live-tests`  
**HEAD:** `11e9155`  
**Wave 4.1 checkpoint in history:** `d883eec` — **CONFIRMED**  
**Wave 2.3:** uncommitted — operator review required  
**Wave 5:** NOT STARTED  
**Corvonero:** FROZEN  

---

## 1. Preflight

| Check | Result |
|-------|--------|
| Branch `mars/post-cycle8-live-tests` | **CONFIRMED** |
| Checkpoint `d883eec` in history | **CONFIRMED** |
| Wave 2.3 uncommitted | **CONFIRMED** |
| Wave 5 NOT STARTED | **CONFIRMED** |
| Corvonero FROZEN | **CONFIRMED** |
| Unrelated WIP staged | **NONE** (modified files exist but unstaged) |

---

## 2. Actual Bundle Inventory

**Path:** `C:\AI MARS STORAGE\incoming\mig\live-validation\w2-3-tech-paid-serp\assisted-capture-pending\w2-3-q02`

| File | Present | Role |
|------|---------|------|
| `screenshot.png` | **YES** (946,694 bytes) | Full-page live SERP screenshot |
| `page.htm` | **YES** (1,338,123 bytes) | Saved live HTML (`.htm` accepted) |
| `capture-manifest by-firefox.json` | **YES** | Raw Firefox snippet manifest |
| `capture-manifest.json` | **YES** | Canonical manifest (normalized on finalize) |
| `capture-manifest.normalized.json` | **YES** | Normalized Wave 2.3 manifest |
| `OPERATOR-INSTRUCTIONS.txt` | **YES** | Helper only — not evidence authority |

`page.html` absent — **`page.htm` used as factual HTML evidence.**

---

## 3. Firefox Capture Manifest

**Authority source:** `capture-manifest by-firefox.json` (unchanged raw evidence)

| Field | Value |
|-------|-------|
| `captured_at` | `2026-06-24T04:41:47.799Z` |
| `attested_at` | `2026-06-24T04:41:47.799Z` |
| `device_browser` | Firefox 152.0 (Windows NT 10.0) |
| `page_url` | Yandex search `ремонт квартир под ключ` `lr=213` |
| `page_title` | `ремонт квартир под ключ — Яндекс: нашлось 10 млн результатов` |
| `region` | Москва (`region_lr=213`) |
| `query` | `ремонт квартир под ключ` |
| Operator attestation | `attested: true` |

**Legacy snippet IDs (bounded defect):** `MIG-W2-1-TECH-PAID-SERP` / `w2-2-assisted-session-001` / `w2-1-q02`

---

## 4. Legacy ID Normalization

Normalized under strong evidence (Wave 2.3 folder, matching query/region, operator attestation, same capture files):

| Field | Legacy | Normalized |
|-------|--------|------------|
| `project_id` | `MIG-W2-1-TECH-PAID-SERP` | `MIG-W2-3-TECH-PAID-SERP` |
| `session_id` | `w2-2-assisted-session-001` | `w2-3-assisted-session-001` |
| `query_id` | `w2-1-q02` | `w2-3-q02` |

**Preserved unchanged:** `captured_at`, browser, page URL, page title, region, query, attestation timestamps.

**Output:** `capture-manifest.normalized.json` with provenance block referencing raw Firefox manifest.

---

## 5. Privacy Sanitization

Raw HTML scan (external storage only):

| Signal | Detected in raw HTML | In repo artifacts |
|--------|---------------------|-------------------|
| Logged-in account metadata | **YES** (categories only) | **WITHHELD** |
| Email/login values | **YES** in raw HTML | **NOT in repo JSON/report** |
| Session/cookie identifiers | **YES** in raw HTML | **NOT in repo JSON/report** |

- Raw `page.htm` / `screenshot.png` remain **outside Git**
- Sanitized observations, registry, landing summaries committed only as metadata
- `privacy-sanitize.mjs` added for bounded scan without value emission

---

## 6. Bundle Finalization

```text
node projects/mig/search-ppc-evidence/runtime/cli/prepare-assisted-capture-bundle.mjs --finalize --bundle "C:/AI MARS STORAGE/.../w2-3-q02"
```

**Result:** `BUNDLE FINALIZED`

| Artifact | SHA-256 |
|----------|---------|
| `screenshot.png` | `74ea32161f8967d51843cad74be2da6f350f9605b4d599ea395ccd4f3c22187b` |
| `page.htm` | `4485a9b365c9daf3bddfbffbb4ec123f3e4da9388b922c0e3f7d4294ffabcefc` |
| normalized manifest body | `d2fa45b558a58c8aff487ac565187101a0de7866c7eb439ec0eaeac510590301` |

**Repairs applied:** `page.htm` support; Firefox manifest normalization; `capture-manifest.normalized.json`; manifest selection priority in validator.

---

## 7. Bundle Validation

| Gate | Result |
|------|--------|
| Project match | **PASS** |
| Query / query_id | **PASS** |
| Session ID | **PASS** |
| Capture timestamp | **PASS** (`2026-06-24T04:41:47.799Z`) |
| Timezone | **PASS** (`Europe/Moscow`) |
| **Business hours** | **FAIL** — local `07:41:47` Wednesday **outside** `09:00–21:00` |
| Region / URL / browser | **PASS** |
| Operator attestation | **PASS** |
| Screenshot + HTML | **PASS** |
| Checksums | **PASS** |
| `production_authority: false` | **PASS** |
| `technical_test_only: true` | **PASS** |

**Overall bundle validation:** `BLOCKED — ASSISTED LIVE CAPTURE BUNDLE INVALID: outside approved window`

---

## 8. Import Result

```text
node projects/mig/search-ppc-evidence/runtime/cli/mig-evidence.mjs paid-serp:import-assisted ...
```

**Gated import:** `BLOCKED` (same business-hours blocker)

Evidence processing for sanitized repo artifacts completed via `run-wave23-genuine-closure.mjs` with import gate failure recorded honestly in evidence pack.

---

## 9. Paid/Organic Parsing

Parsed `page.htm` with multi-signal extraction:

- Visible markers: `Реклама`, `Промо`
- Yandex Direct feedback metadata (`snippetUrl` + `feature: Реклама`)
- Path domain (`<b>domain</b>`) blocks
- Legacy `AdvItem` / `yabs` patterns (fixture compatibility)

**Results:** 10 deduplicated paid observations; organic results kept separate (not promoted without paid signals).

---

## 10. Screenshot Verification

Operator full-page screenshot corroborates paid blocks with visible **«Реклама»** labels.

| observation_id | headline (truncated) | domain | marker | HTML | screenshot | verdict |
|----------------|---------------------|--------|--------|------|------------|---------|
| `w2-3-q02-ad-01` | Ремонт-квартир… | `xn--…xn--p1ai` | Реклама | CONFIRMED | CORROBORATED | PAID CONFIRMED |
| `w2-3-q02-ad-02` | Ремонт квартир в Москве под ключ… | `kirillshlykovrepair.ru` | Реклама | CONFIRMED | CORROBORATED | PAID CONFIRMED |
| `w2-3-q02-ad-03` | Ремонт квартир в Москве и МО без авансов… | `a4remont.ru` | Промо | CONFIRMED | CORROBORATED | PAID CONFIRMED |

Full table: `live-validation/w2-3-tech-paid-serp/screenshot-verification-v2.json`

---

## 11. Genuine Ad Observations

**File:** `live-validation/w2-3-tech-paid-serp/genuine-paid-observations-v2.json`

- 10 observations with `observation_state: ADS OBSERVED`
- Fields unknown where not evidenced: `text`, `sitelinks`, `position` → `null`
- Each links `source_html_reference: page.htm`, `screenshot_reference: screenshot.png`
- No fabricated legal names or prices

---

## 12. Advertiser Registry

**File:** `live-validation/w2-3-tech-paid-serp/advertiser-registry-v2.json`

- 10 advertiser entities from confirmed observations (domain-primary merge policy)
- No ambiguous cross-domain merges
- First/last observed: capture timestamp `2026-06-24T04:41:47.799Z`

---

## 13. Landing Evidence

**File:** `live-validation/w2-3-tech-paid-serp/landing-evidence-v2.json`

Bounded resolution (max 2 ads):

| observation_id | HTTP | final_url | title | H1 | CTA |
|----------------|------|-----------|-------|----|----|
| `w2-3-q02-ad-01` | 200 | snippet URL | Ремонт квартир в Новосибирске | present | null |
| `w2-3-q02-ad-02` | 200 | kirillshlykovrepair.ru | Кирилл Шлыков Ремонт… | present | Консультация |

Both resolutions **RESOLVED** (bounded fetch, no wide crawl).

---

## 14. Minimum Closure Evidence

| Requirement | Required | Actual | Met |
|-------------|----------|--------|-----|
| Genuine live SERP page | 1 | 1 | **YES** |
| Genuine paid ad observations | 2 | 10 | **YES** |
| Validated advertiser entity | 1 | 10 | **YES** |
| Bounded landing resolution | 1 | 2 | **YES** |
| **Gated bundle validation** | pass | **FAIL (business hours)** | **NO** |

**Canonical minimum closure:** **NOT MET** — business-hours gate not satisfied; gated import blocked.

---

## 15. Genuine Technical Evidence Pack

**File:** `live-validation/w2-3-tech-paid-serp/genuine-technical-evidence-pack-v2.json`

**Status:** `GENUINE LIVE PAID SERP CAPABILITY NOT VALIDATED`

Includes: technical project, acquisition mode, manifest refs, checksums, observations, advertisers, landing evidence, privacy summary, limitations, gated import status.

---

## 16. Tests

```text
node projects/mig/search-ppc-evidence/tests/run-wave23-genuine-closure-tests.mjs
```

**Result:** **22/22 PASS** (includes `.htm`, Firefox manifest priority, legacy ID normalization, privacy, reconciliation cases)

---

## 17. Bypass Audit

```text
node projects/mig/search-ppc-evidence/tests/run-wave23-bypass-audit.mjs
```

**Result:** **20/20 PASS**

---

## 18. SPPC-10 Capability Status

| Verdict | Status |
|---------|--------|
| **Gated Wave 2.3 closure** | **NOT VALIDATED** (business-hours blocker on otherwise genuine capture) |
| **Pipeline capability** | Parsing, normalization, landing resolution, and privacy boundaries **demonstrated** on genuine live bundle |
| **SPPC-10 acquisition (canonical)** | `SPPC-10 ACQUISITION CAPABILITY — LIVE EVIDENCE STILL REQUIRED` |
| **Authority** | `TECHNICAL TEST — NOT CLIENT PRODUCTION EVIDENCE` |

Substantive live evidence exists; canonical gate requires capture within approved window or explicit operator-approved exception.

---

## 19. Client Production Boundary

**Global capability operational does not complete client-specific SPPC-10.**

Technical Wave 2.3 evidence has `production_authority: false` and does not authorize client production runs.

---

## 20. Corvonero Boundary

| Item | Status |
|------|--------|
| Corvonero project | **FROZEN** |
| Project SPPC-10 | **NOT AUTHORIZED** |
| Strategy | **NOT AUTHORIZED** |
| Semantic Core production run | **NOT AUTHORIZED** |

---

## 21. Files Changed

**Runtime (repo):**

- `runtime/lib/assisted-manifest-normalizer.mjs` (new)
- `runtime/lib/privacy-sanitize.mjs` (new)
- `runtime/lib/landing-resolve-bounded.mjs` (new)
- `runtime/lib/serp-html-extract.mjs` (modern Yandex paid extraction)
- `runtime/lib/assisted-capture-validator.mjs` (manifest priority, `.htm`)
- `runtime/lib/assisted-capture-importer.mjs` (bounded landing fetch)
- `runtime/lib/paid-serp-runtime.mjs` (ad marker fields, position null)
- `runtime/cli/prepare-assisted-capture-bundle.mjs` (finalize normalization)
- `runtime/cli/run-wave23-genuine-closure.mjs` (new)
- `runtime/cli/mig-evidence.mjs` (async import)

**Evidence artifacts (repo, sanitized):**

- `live-validation/w2-3-tech-paid-serp/genuine-technical-evidence-pack-v2.json`
- `live-validation/w2-3-tech-paid-serp/genuine-paid-observations-v2.json`
- `live-validation/w2-3-tech-paid-serp/advertiser-registry-v2.json`
- `live-validation/w2-3-tech-paid-serp/landing-evidence-v2.json`
- `live-validation/w2-3-tech-paid-serp/screenshot-verification-v2.json`
- `live-validation/w2-3-tech-paid-serp/business-hours-check-v2.json`
- `live-validation/w2-3-tech-paid-serp/sppc-10-closure-inventory-v1.json` (updated)
- `tests/run-wave23-genuine-closure-tests.mjs`
- `tests/run-wave23-bypass-audit.mjs`
- `reports/wave23-genuine-closure-test-results-v1.json`
- `reports/wave23-bypass-audit-results-v1.json`

**External storage (not in Git):**

- Raw bundle + finalized manifests + checksums under `C:\AI MARS STORAGE\...\w2-3-q02\`

---

## 22. Git Status

Wave 2.3 artifacts **uncommitted** per operator review gate. Unrelated workspace WIP remains unstaged.

---

## 23. SAFE UNKNOWN

- Exact ad position ordinals on live SERP not recorded (design: `position: null` when uncertain)
- Sitelinks/phone/price not extracted where not reliably visible in saved HTML
- Whether operator logged-in Yandex session affected ad mix — **UNKNOWN** (session metadata present in raw HTML only)
- Long-term ad persistence for this query — **UNKNOWN** (single timestamp evidence)

---

## 24. Operator Approval Items

1. **Business-hours exception** for `2026-06-24` capture at `07:41 MSK` **OR** re-capture within `09:00–21:00` window
2. Review sanitized observations/registry for Wave 2.3 checkpoint eligibility
3. Confirm privacy boundary acceptable (raw HTML remains external)
4. Decide whether to authorize Wave 2.3 commit after gate satisfaction

---

## 25. Recommended Next Action

**OPERATOR REVIEW OF WAVE 2.3 GENUINE LIVE PAID SERP CLOSURE V2**

If business-hours exception approved → re-run gated import; expect `GENUINE LIVE PAID SERP CAPABILITY VALIDATED` if all gates pass.

If re-capture preferred → repeat Mode B during approved window for `w2-3-q02` (or alternate query from set).

---

## 26. Stop Condition

**STOPPED** after: bundle normalization, finalize, blocked gated import, paid/organic parsing, screenshot reconciliation, advertiser registry, bounded landing resolution, minimum closure verdict, tests, bypass audit, and this report.

**Not started:** Wave 5, Commander, Corvonero work, Wave 2.3 commit.

**Next gate:** Operator review of Wave 2.3 Genuine Live Paid SERP Closure V2.
