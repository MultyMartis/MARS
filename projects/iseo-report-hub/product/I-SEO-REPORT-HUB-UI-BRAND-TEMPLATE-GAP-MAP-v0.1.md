# I-SEO Report Hub — UI / Brand / Template Gap Map v0.1

**Status:** DISCOVERY / PLANNING ONLY  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-07  
**Wave:** UI Screenshot QA, Brand Style and Nikita Templates Discovery 01  
**Inputs:** UI Screenshot QA Inventory · i-SEO Brand Style Discovery · Nikita Templates Discovery · Demo Visual Shell Impl 02

---

## 1. UI Russian cleanup gaps

| Gap | Severity | Impl wave |
|-----|----------|-----------|
| Secondary CRUD/preview/blocks/period detail still English | BLOCKER | **Impl 03** |
| Machine keys (`executive_summary`, snapshot/export keys) on manager surfaces | BLOCKER / MAJOR | **Impl 03** (hide/collapse) |
| Stale «PDF export: not implemented» on period show | MAJOR | **Impl 03** |
| Snapshot admin page fully English | MAJOR | **Impl 03** (RU + technical collapse) |
| Shares/export titles expose `snapshot-1-pdf-v2` | MAJOR | **Impl 03** |
| Fixture Demo* / LOCAL_FIXTURE_ONLY | ACCEPTED | Keep; clearer «Тестовые данные» badge in Impl 03 |
| A–D manager surfaces mostly Russian | — | Done (Impl 01–02) |

---

## 2. Brand / style gaps

| Gap | Evidence | Impl wave |
|-----|----------|-----------|
| Accent red `#c8102e` ≠ live i-seo yellow `#facc15` | Live `css/main.css` + site-ops scratch | **Impl 03** brand layer |
| System font ≠ Manrope | Google Fonts on i-seo.su | **Impl 03** |
| Buttons not pill / not yellow-on-black CTA | Live CSS radius 100px + `#facc15` | **Impl 03** primary buttons |
| Sidebar slate vs marketing `#18181B` | Optional polish | **Impl 03** optional |
| Full dark marketing theme vs light admin | Intentional UX difference | **Keep light main** unless operator overrides |
| Client PDF chrome still old template | Impl 02 deferred | **Client Report Template** wave |
| Do not import full WP CSS | Risk | Policy for all waves |

---

## 3. Report structure gaps

| Gap | Vs Nikita / architecture | Wave |
|-----|--------------------------|------|
| Only 6 generic monthly fields | Nikita has rich work taxonomy; architecture has 13 blocks | **Nikita Data Model Charter 01** |
| No shop vs services profile | Two Nikita XLSX plans | Charter 01 |
| No KPI / positions / traffic / leads structured blocks | Architecture + Nikita analytics | Charter 01 + later impl |
| Weekly vs monthly separation weak in UI copy | Architecture weekly 9-block | Copy in Impl 03; model later |
| No internal vs client visibility flags | Needed for hub | Charter 01 |
| No AI vs manual field flags | Operator desire | Charter 01 |
| No evidence/attachments model in UI | Architecture Block 13 | Later |
| Client PDF section fidelity | Deferred since demo reviews | **Client Report Template Visual Alignment** |

---

## 4. Data / state gaps

| Item | Class | Action |
|------|-------|--------|
| Demo Client / Demo SEO Project / Demo Monthly Report | Fixture | Keep; badge |
| Periods 2026-07 finalized / 2026-08 archived+draft | Fixture weirdness | Not product bug |
| Exports = 4 (historical Impl evidence) | OK | No regen |
| Shares: prior active 0 / revoked 6; operator now reports active **id 7** `test-first-link` | Local test state | Optional **Local Share QA Cleanup 01** — do not revoke in Impl 03 |
| Full public share URL may be unrecoverable | Known once-URL design | Handoff UX already documents |

---

## 5. Risk classification

| Risk class | Examples | Safe in Impl 03? |
|------------|----------|------------------|
| View/CSS/copy only | RU strings, hide keys, yellow tokens, Manrope | **Yes** |
| DB / template migration | New blocks, profile types, KPI tables | **No** — later charter |
| Client PDF/template visual | `iseo_default_v1` redesign | **No** — separate charter |
| Share create/revoke / token | Cleanup active test link | **No** — optional cleanup wave |
| PDF regeneration | New artifacts | **No** |
| WordPress / i-seo.su mutation | Brand source | **Forbidden** |

---

## 6. Triangulation summary

| Axis | Current truth | Target truth | Immediate gap owner |
|------|---------------|--------------|---------------------|
| UI language | A–D RU; secondary EN | All manager pages RU | Impl 03 |
| Visual brand | Demo red shell | i-seo yellow + Manrope + keep admin shell | Impl 03 |
| Report fields | 6 generic keys | Nikita taxonomy + 13-block architecture | Nikita Charter 01 → later impl |
| Client artifact | Styled PDF v2 exists, chrome not brand-perfect | Brand + template sections | Client template charter |

---

## 7. SAFE UNKNOWN

- Whether operator prefers full dark admin.  
- Exact DB state of share id 7 at discovery time.  
- Full Nikita XLSX formula sheets beyond shared strings.
