# SITE-001 — Phase 1 Stable Checkpoint v1

**Type:** Official stable checkpoint — **documentation only**  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Platform:** ocStore **3.0.3.8 (rs.2)** · active theme **`auto`**

**Explicit exclusions (honored):** No site modifications. No DB writes. No FTP writes. No admin access. No cache clears.

---

## 1. Checkpoint purpose

This document records the **official stable recovery point** for SITE-001 Phase 1 Brand Replacement after final acceptance.

**Use this checkpoint when:**

- Starting Phase 2 work (UX, style, layout, catalog, vehicle, production preparation)
- Rolling back documentation or program state to the post-Phase-1 baseline
- Auditing what was in scope vs deferred at Phase 1 closure
- Proving TEST brand-replacement state before any future write session

**Supersedes for recovery purposes:** [SITE-001-PHASE1-STABLE-SNAPSHOT-v1.md](SITE-001-PHASE1-STABLE-SNAPSHOT-v1.md) (pre-W1G interim snapshot).

**Does not authorize:** production deployment, W1F-D/E execution, or Phase 2 writes without separate authorization.

---

## 2. Accepted scope

Phase 1 objective: replace legacy **АЦ Хмельницкий** brand identity with **СИБКАР** on TEST across authorized public surfaces and supporting store/theme/controller/SEO layers.

| Layer | In scope | Out of scope |
|-------|----------|--------------|
| Store settings (W1A) | Brand name, meta, owner, email | SMTP username (W1F-D deferred) |
| Theme `auto` (W1B) | Header, footer, home, visible copy | WhatsApp URL (C-04 open) |
| Custom controllers (W1C) | `/about`, `/contact/` meta + body | — |
| Logos + favicon (W1D) | SVG logo set, favicon pack | Orphan legacy assets (W1F-E deferred) |
| YML + robots (W1F-C1) | Shop metadata, Host/Sitemap | `backup_yml/` copies (W1F-E deferred) |
| Information pages (W1F-B) | 11 legal/service records | — |
| Product/category SEO (W1F-A) | Controller + template remediation | PDP HTTP when catalog empty |
| DB SEO cleanup (W1G) | Category 59 root, 203 product meta rows, admin JS default | Manufacturer custom SEO fields (SAFE UNKNOWN) |
| Mail identity | — | **Deferred W1F-D** |
| Production | — | **NOT AUTHORIZED** |

**Acceptance gate:** [SITE-001-PHASE1-FINAL-DECISION-v1.md](SITE-001-PHASE1-FINAL-DECISION-v1.md) — **PHASE 1 ACCEPTED WITH NOTES**

---

## 3. Completed waves

| Wave | Scope | Verdict | Date | Report |
|------|-------|---------|------|--------|
| **W1A** | Store Settings (admin) | **PASS WITH NOTES** | 2026-06-08 | [SITE-001-W1A-EXECUTION-v1.md](SITE-001-W1A-EXECUTION-v1.md) |
| **W1A Post-Audit** | Unicode / mixed-script check | **PASS** | 2026-06-08 | [SITE-001-W1A-POST-AUDIT-v1.md](SITE-001-W1A-POST-AUDIT-v1.md) |
| **W1B** | Theme branding (`auto`) | **PASS** | 2026-06-08 | [SITE-001-W1B-EXECUTION-v1.md](SITE-001-W1B-EXECUTION-v1.md) |
| **W1C** | Custom controllers `/about`, `/contact/` | **PASS** | 2026-06-08 | [SITE-001-W1C-EXECUTION-v1.md](SITE-001-W1C-EXECUTION-v1.md) |
| **W1D** | Logos + favicon | **PASS WITH NOTES** | 2026-06-08 | [SITE-001-W1D-EXECUTION-v1.md](SITE-001-W1D-EXECUTION-v1.md) |
| **W1F-C1** | YML generators + `robots.txt` | **PASS WITH NOTES** | 2026-06-08 | [SITE-001-W1F-C1-EXECUTION-v1.md](SITE-001-W1F-C1-EXECUTION-v1.md) |
| **W1F-B** | Legal / information pages | **PASS WITH NOTES** | 2026-06-08 | [SITE-001-W1F-B-EXECUTION-v1.md](SITE-001-W1F-B-EXECUTION-v1.md) |
| **W1F-A** | Product/category SEO controllers + templates | **PASS WITH NOTES** | 2026-06-08 | [SITE-001-W1F-A-EXECUTION-v1.md](SITE-001-W1F-A-EXECUTION-v1.md) |
| **W1G** | DB SEO cleanup + admin `product_form.twig` JS default | **PASS WITH NOTES** | 2026-06-09 | [SITE-001-W1G-SEO-DB-CLEANUP-v1.md](SITE-001-W1G-SEO-DB-CLEANUP-v1.md) |

**Not executed (deferred, documented):**

| Wave | Scope | Status |
|------|-------|--------|
| **W1F-D** | SMTP — `config_mail_smtp_username`, `anketa.php` sender | **DEFERRED — NOT AUTHORIZED** |
| **W1F-E** | `backup_yml/`, `productnew_Backup.twig`, orphan assets | **DEFERRED — NOT AUTHORIZED** |

---

## 4. Acceptance references

| Document | Role | Outcome |
|----------|------|---------|
| [SITE-001-W1-EXECUTION-AUTHORIZATION-v1.md](SITE-001-W1-EXECUTION-AUTHORIZATION-v1.md) | W1 write authorization | **AUTHORIZED WITH NOTES** |
| [SITE-001-PHASE1-STABLE-SNAPSHOT-v1.md](SITE-001-PHASE1-STABLE-SNAPSHOT-v1.md) | Pre-W1G interim checkpoint | **DONE** — superseded by this checkpoint |
| [SITE-001-PHASE1-FINAL-AUDIT-v1.md](SITE-001-PHASE1-FINAL-AUDIT-v1.md) | Interim HTTP audit | **DONE** |
| [SITE-001-PHASE1-FINAL-AUDIT-DECISION-v1.md](SITE-001-PHASE1-FINAL-AUDIT-DECISION-v1.md) | Interim decision (pre-W1G) | **COMPLETE WITH NOTES** |
| [SITE-001-W1G-SEO-DB-CLEANUP-v1.md](SITE-001-W1G-SEO-DB-CLEANUP-v1.md) | W1G execution | **PASS WITH NOTES** |
| [SITE-001-PHASE1-FINAL-ACCEPTANCE-v1.md](SITE-001-PHASE1-FINAL-ACCEPTANCE-v1.md) | Final acceptance package | **DONE** — 13/13 CLEAN |
| [SITE-001-PHASE1-FINAL-DECISION-v1.md](SITE-001-PHASE1-FINAL-DECISION-v1.md) | Final acceptance decision | **PHASE 1 ACCEPTED WITH NOTES** |
| [SITE-001-PHASE1-STABLE-CHECKPOINT-DECISION-v1.md](SITE-001-PHASE1-STABLE-CHECKPOINT-DECISION-v1.md) | Checkpoint gate decision | **APPROVED** |

**Authorization chain:** [SITE-001-W1-WRITE-CHARTER-v1.md](SITE-001-W1-WRITE-CHARTER-v1.md) · [SITE-001-W1-CHANGE-REQUEST-v1.md](SITE-001-W1-CHANGE-REQUEST-v1.md) · [project-access-brief.md](../project-access-brief.md)

**Inspection rule (active):** [OCPILOT-RULE-CONTROLLER-META-GENERATORS-v1.md](../../knowledge/OCPILOT-RULE-CONTROLLER-META-GENERATORS-v1.md)

---

## 5. Verification summary

**Method:** Read-only HTTP fetch + HTML parse (2026-06-09). Legacy dictionary applied to full response body. Geographic exception `ул. Богдана Хмельницкого` classified **GEOGRAPHICAL_REFERENCE** (allowed).

| Metric | Result |
|--------|--------|
| Required public URLs probed | **13** |
| HTTP 200 | **13** |
| Legacy dictionary **FAIL** | **0** |
| Legacy dictionary **CLEAN** | **13** |
| Brand replacement on TEST | **COMPLETE** for scoped public surfaces |

### 5.1 Verified URLs (all CLEAN)

| URL | Verdict |
|-----|---------|
| `/` | **CLEAN** |
| `/about` | **CLEAN** |
| `/contact/` | **CLEAN** |
| `/privacy-policy` | **CLEAN** |
| `/user-agreement` | **CLEAN** |
| `/autocredit` | **CLEAN** |
| `/tradein` | **CLEAN** |
| `/loan-terms` | **CLEAN** |
| `/cookie-files-policy` | **CLEAN** |
| `/cars/bmw` | **CLEAN** |
| `/cars/hyundai` | **CLEAN** |
| `/auto/` | **CLEAN** *(remediated W1G)* |
| `/auto/baic` | **CLEAN** |

### 5.2 Legacy dictionary scan

| Term | Hits | Notes |
|------|------|-------|
| `АЦ Хмельницкий` | **0** | Pre-W1G: `/auto/` — **remediated** |
| `Автоцентр Хмельницкий` | **0** | — |
| `ООО «АЦ Хмельницкий»` | **0** | — |
| `ац-хмельницкий.рф` | **0** | Public HTML only; SMTP deferred |
| `xn----7sbqmagfghm8fkh5f` | **0** | Public HTML only; `anketa.php` deferred |
| `Hmelnickiy` / `Khmelnitskiy` | **0** | — |
| `ул. Богдана Хмельницкого` | **4/page** | **GEOGRAPHICAL_REFERENCE — allowed** |

### 5.3 Unverified at checkpoint

| Surface | Status |
|---------|--------|
| Used-car product detail (PDP) | **NOT VERIFIED** — zero routable URLs on TEST |
| New-car product detail (PDP) | **NOT VERIFIED** — W1G DB remediated; live PDP probe blocked |
| Production environment | **NOT SCANNED** |
| SMTP / `anketa.php` | **DEFERRED** — not probed in acceptance run |

**Evidence:** `.recovery-temp/site-001-phase1-final-acceptance-verify.json`

---

## 6. Deferred items

| ID | Surface | Status | Wave | Severity |
|----|---------|--------|------|----------|
| D-01 | `config_mail_smtp_username` = `send@ац-хмельницкий.рф` | **KNOWN — W1A hold** | **W1F-D** | **CRITICAL** *(mail identity)* |
| D-02 | `catalog/controller/checkout/anketa.php:89` punycode sender | **DEFERRED** | **W1F-D** | **CRITICAL** *(mail identity)* |
| D-03 | `catalog/controller/product/backup_yml/*.php` | **DEFERRED** (inactive) | **W1F-E** | **LOW** |
| D-04 | `productnew_Backup.twig` | **DEFERRED** (backup template) | **W1F-E** | **LOW** |
| D-05 | Orphan legacy logo assets | **DEFERRED** | **W1F-E** | **LOW** |
| D-06 | C-04 WhatsApp URL decision | **OPEN** | W1B | **MEDIUM** |
| D-07 | C-10 Admin URL on access brief | **OPEN** | All | **LOW** |
| D-08 | New/used product detail HTTP sample | **NOT VERIFIED** | Acceptance note | **MEDIUM** |
| D-09 | Manufacturer custom SEO DB fields | **SAFE UNKNOWN** | Verify on demand | **MEDIUM** |
| D-10 | Independent Beget restore drill | **SAFE UNKNOWN** | Ops | **MEDIUM** |

Full inventory: [SITE-001-PHASE1-FINAL-ACCEPTANCE-v1.md](SITE-001-PHASE1-FINAL-ACCEPTANCE-v1.md) §3.

---

## 7. Rollback references

| Tier | Scope | Reference |
|------|-------|-----------|
| **T1** | Field-level DB + single admin file (W1G) | `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\w1g-seo-db-pre-replace-2026-06-09\rollback.sql` |
| **T2** | Per-wave FTP file backups | W1F-A, W1F-B, W1F-C1, W1D under `...\site-001\backups\` |
| **T3** | Pre-W1 operator backup (Beget files + DB) | [SITE-001-W1-BACKUP-PROCEDURE-v1.md](SITE-001-W1-BACKUP-PROCEDURE-v1.md) — operator-confirmed 2026-06-08 |
| **Plan** | Rollback tiers T1/T2/T3 | [SITE-001-W1-ROLLBACK-PLAN-v1.md](SITE-001-W1-ROLLBACK-PLAN-v1.md) |

**W1G rollback note:** Restore `admin/view/template/catalog/product_form.twig` from W1G backup + run `rollback.sql` + clear modification cache.

**Checkpoint recovery (documentation):** Git tag `site-001-phase1-stable-2026-06` (recommended) + this document set.

---

## 8. Known risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| Mail identity legacy (D-01, D-02) | Outbound mail may identify legacy domain | Execute **W1F-D** before production cutover |
| PDP HTTP unverified (D-08) | New-car `<title>` not signed off on live PDP | Spot-check when TEST inventory routable |
| `backup_yml/` inactive copies (D-03) | Legacy if backup controllers activated | Execute **W1F-E** before prod |
| Production environment unscanned | TEST evidence may not match prod | Separate prod audit before cutover |
| Independent restore drill unknown (D-10) | Rollback path documented but unproven | Operator restore drill on Beget |
| Manufacturer custom SEO fields (D-09) | Possible hidden legacy in DB | On-demand DB scan before prod |
| HITL sign-off pending | Write approver **Андрей** — acceptance WITH NOTES | Operator confirmation record |

**Production deployment:** **NOT AUTHORIZED** at this checkpoint.

---

## 9. Next recommended phase

| Priority | Activity | Notes |
|----------|----------|-------|
| **0** | **Freeze at this checkpoint** | No UX/style/layout/catalog/vehicle writes until Phase 2 authorized |
| **1** | **W1F-D** | SMTP + `anketa.php` — mail identity |
| **2** | **W1F-E** | Backup YML, backup templates, orphan assets |
| **3** | **PDP spot-check** | When TEST inventory routable |
| **4** | **Phase 2 planning** | UX, style, layout, catalog, vehicle, production prep — documentation parallel only |

Phase 2 work must reference this checkpoint as the baseline recovery point.

---

## 10. Checkpoint status

| Field | Value |
|-------|--------|
| Checkpoint ID | `SITE-001-PHASE1-STABLE-CHECKPOINT-v1` |
| Decision | **APPROVED** — [SITE-001-PHASE1-STABLE-CHECKPOINT-DECISION-v1.md](SITE-001-PHASE1-STABLE-CHECKPOINT-DECISION-v1.md) |
| Program state | **ACTIVE** — [OCPILOT-STATE.md](../../OCPILOT-STATE.md) |
| Operational run | **4.110** — [OPERATIONAL-INDEX.md](../../OPERATIONAL-INDEX.md) |
| Recommended git tag | `site-001-phase1-stable-2026-06` |

*SITE-001 Phase 1 Stable Checkpoint v1 — TEST only; documentation only; no commit.*
