# SITE-001 Change Authorization Review v1

**Type:** Formal authorization review — **no** site modification, **no** runtime code, **no** FTP/deployment  
**Date:** 2026-06-07  
**Site:** SITE-001 — Автосалон СИБКАР  
**Platform:** ocStore / OpenCart **3.0.3.8 (rs.2)**  
**Environment:** **TEST** (`https://sibcar.new-site.space/`)  
**Phase under review:** Phase 1 — **Hmelnickiy → SIBKAR Brand Replacement**  
**Decision companion:** [SITE-001-CHANGE-AUTHORIZATION-DECISION-v1.md](SITE-001-CHANGE-AUTHORIZATION-DECISION-v1.md)

**Explicit exclusions:** EAR live pilot; HG-4; HG-4 follow-on gates; future pilots; OCPilot architecture changes; production environment.

---

## Executive summary

This review evaluates whether SITE-001 on **TEST** is ready for the **first controlled content-change operation**: replacement of legacy **Hmelnickiy / Хмельницкий** branding with **SIBKAR / СИБКАР** across name, legal entity, contacts, logos, basic texts, footer, meta, and OpenCart settings.

**Repository truth:** Intake is closed; baseline **`ocstore-3038-rs2`** is approved; backup is **operator-claimed** (Beget, 2026-05-31); access channels are **flagged available** but credential locations and write charter are **incomplete**; Run 5 read-only audit is **initialized but not executed**; no site snapshot or brand-reference inventory exists in repo or external bulk storage.

**Recommendation:** **NOT AUTHORIZED** for immediate Phase 1 execution. Operator may proceed to **pre-execution checklist** below; upon completion, re-issue decision as **AUTHORIZED WITH NOTES** for a supervised first modification session on TEST only.

---

## 1. Mission scope

### 1.1 In scope (Phase 1)

| # | Change class | Target state (operator intent) |
|---|--------------|--------------------------------|
| 1 | Brand name | **Хмельницкий** → **СИБКАР** (and agreed variants) |
| 2 | Legal entity information | **ООО «СибКар»** per attested counterparty card |
| 3 | Contacts | Phones, emails, messengers, addresses — operator-approved set |
| 4 | Logos | Header, favicon, footer marks — operator-supplied assets |
| 5 | Basic company texts | About, contacts, footer copy |
| 6 | Footer / company references | Theme + information pages + language strings |
| 7 | Meta information | Title, description, OG tags if present |
| 8 | OpenCart settings | Store settings and related `oc_setting` keys |

### 1.2 Out of scope (this review)

| Item | Reason |
|------|--------|
| Catalog import / vehicle load | Run 6+ planning |
| Theme redesign | Beyond brand replacement |
| Controller / ocMod code edits | Requires separate charter |
| Production URL / DNS | TEST only |
| Autonomous agent writes | Forbidden by [boundaries.md](../../../boundaries.md) |

### 1.3 Old-brand baseline (SAFE UNKNOWN in repo)

Mission context names legacy brand **Hmelnickiy / Хмельницкий**. **No** occurrence of that string appears in MARS documentation for SITE-001. Exact on-site spellings, transliterations, and image filenames are **SAFE UNKNOWN** until operator delivers a **brand grep baseline** from the live TEST site.

---

## 2. Sources reviewed

| ID | Source | Role |
|----|--------|------|
| S-SITE-01 | [site-passport.md](../site-passport.md) | Identity, TEST URL, baseline |
| S-SITE-02 | [project-access-brief.md](../project-access-brief.md) | Access inventory, permissions, backup, business goal |
| S-SITE-03 | [AUDIT-CHARTER.md](../AUDIT-CHARTER.md) | Current charter — **read-only only** |
| S-SITE-04 | [materials/INTAKE-COMPLETE.md](../materials/INTAKE-COMPLETE.md) | Intake closure |
| S-SITE-05 | [reports/RUN-5-FIRST-FINDINGS.md](RUN-5-FIRST-FINDINGS.md) | Evidence gaps |
| S-SITE-06 | [tasks/RUN-5-DATA-REQUEST.md](../tasks/RUN-5-DATA-REQUEST.md) | Minimum audit evidence |
| S-SITE-07 | [freeze/site-001-pre-runtime-bridge/AUDIT-BLOCKERS-v1.md](../../../freeze/site-001-pre-runtime-bridge/AUDIT-BLOCKERS-v1.md) | Run 5 blockers |
| S-SITE-08 | [freeze/site-001-pre-runtime-bridge/OCPILOT-STATE-SUMMARY-v1.md](../../../freeze/site-001-pre-runtime-bridge/OCPILOT-STATE-SUMMARY-v1.md) | Program freeze snapshot |
| S-SITE-09 | [intake-readiness-review.md](../../../intake-readiness-review.md) | Run 5 gate (read-only) |
| S-SITE-10 | [boundaries.md](../../../boundaries.md), [access-and-safety.md](../../../access-and-safety.md) | Write gates, backup rules |
| S-SITE-11 | [templates/change-request-template.md](../../../templates/change-request-template.md), [templates/rollback-plan-template.md](../../../templates/rollback-plan-template.md) | Change discipline |
| S-SITE-12 | [ATLAS-SIBCAR-EVIDENCE-VERIFICATION-v1.md](../../../../atlas/population/ATLAS-SIBCAR-EVIDENCE-VERIFICATION-v1.md) | Legal entity / partial contacts (E1 CC) |
| S-SITE-13 | EAR dry-run artefacts (context only — **not** execution authorization) | [SITE-001-DRY-RUN-DECISION-v1.md](../../../../ear-runtime/SITE-001-DRY-RUN-DECISION-v1.md) |

**Rule:** EAR Dry Run **PASS WITH NOTES** does **not** authorize site writes or live SFTP. It is **not** a Phase 1 execution gate.

---

## 3. Readiness assessment by change class

| Change class | Target data available? | Site inventory done? | Write charter? | Ready? |
|--------------|------------------------|----------------------|----------------|--------|
| Brand name (СИБКАР) | Partial — Atlas aliases; site title already «Автосалон СИБКАР» in passport | **No** — old-brand locations unknown | **No** | **NO** |
| Legal entity | **Yes** — LE-0005 / EV-W1C-CC-01 (INN, OGRN, address) | **No** — on-site legal blocks unknown | **No** | **NO** |
| Contacts | Partial — email `info_sibcar@mail.ru`; **phone/messengers SAFE UNKNOWN** | **No** | **No** | **NO** |
| Logos | **No** — assets not in repo/external materials index | **No** — current logo paths unknown | **No** | **NO** |
| Company texts | Partial — CC address/legal; marketing copy **SAFE UNKNOWN** | **No** | **No** | **NO** |
| Footer / references | **No** inventory | **No** | **No** | **NO** |
| Meta | **No** — live meta not captured | **No** | **No** | **NO** |
| OpenCart settings | Method known (admin + `oc_setting`); values **not captured** | **No** | **No** | **NO** |

---

## 4. Review questions — explicit answers

### Q1. Can Phase 1 begin safely?

**NO** — not in the current state.

**Blockers:** (a) no write authorization on [project-access-brief.md](../project-access-brief.md); (b) no pre-change snapshot or brand-reference inventory; (c) incomplete target contact pack; (d) logo assets not staged; (e) Run 5 site facts largely **SAFE UNKNOWN**; (f) backup restorability not independently verified.

**Safe to begin:** pre-execution checklist (§6) and read-only brand discovery on TEST under operator supervision.

---

### Q2. What information is still required from operator?

| Priority | Item | Why |
|----------|------|-----|
| **P0** | **Brand Replacement Pack v1** — approved strings: display name, legal lines, address, email, phone(s), messenger links, social URLs | Single source of truth for replacements |
| **P0** | **Old-brand search term list** — all Хмельницкий / Hmelnickiy variants operator expects on site | Drives grep and verification |
| **P0** | **Logo assets** — SVG/PNG, dimensions, favicon, dark/light if applicable | Cannot replace logos without files |
| **P0** | **Write charter sign-off** — update access brief: file edits + DB edits **YES** on TEST; named operator approver | Required by [boundaries.md](../../../boundaries.md) |
| **P0** | **Fresh backup confirmation** — file + DB, timestamp **after** checklist start, restore path tested or acknowledged | Write gate per [access-and-safety.md](../../../access-and-safety.md) |
| **P1** | **Admin URL** (non-secret path) | Supervised admin session |
| **P1** | **Credential channel confirmation** — which of FTP / admin / PMA is authorized for first session | Access brief still lists locations as SAFE UNKNOWN |
| **P1** | **Phone and messenger numbers** | Absent from EV-W1C-CC-01 |
| **P1** | **Site title policy** — confirm «Автосалон СИБКАР» vs «СИБКАР» vs legal name in footer | Atlas EFV-01 disambiguation |
| **P2** | **Optional:** marketing tagline, Yandex/Google verification meta (if replacing) | Phase 1 meta scope |

---

### Q3. What access is already sufficient?

| Access / fact | Status | Notes |
|---------------|--------|-------|
| TEST environment classification | **Sufficient** | Confirmed TEST; URL documented |
| Platform + baseline | **Sufficient for planning** | ocStore 3.0.3.8 (rs.2); `ocstore-3038-rs2` — **live version unverified** |
| Access channel availability (flags) | **Partially sufficient** | Brief marks FTP, SSH, PMA, admin, DB as **YES** — locations unconfirmed |
| Read-only audit charter | **Sufficient for discovery** | [AUDIT-CHARTER.md](../AUDIT-CHARTER.md) |
| External storage root | **Sufficient** | `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\` |
| Legal entity source (Atlas CC) | **Sufficient for legal block text** | Not sufficient alone for on-site execution |
| Backup (claimed) | **Partially sufficient** | Beget 2026-05-31 — **stale for first write**; needs refresh |
| Write permission | **Insufficient** | Explicitly **NO** on access brief |
| EAR / SFTP read-only pilot | **Not required for Phase 1** if operator uses admin/FTP directly — **not authorized for autonomous use** |

---

### Q4. What data must be collected before execution?

**Minimum pre-change evidence set:**

1. **Pre-change snapshot reference** — dated file backup + DB backup labels under external `backups/` (not necessarily full dump in git).
2. **Brand grep baseline** — search results for all old-brand terms across:
   - `oc_setting` (store keys)
   - `oc_information_description` (information pages)
   - Active theme templates and language files
   - `image/` logo paths (filenames + alt text if visible)
3. **Screenshots** — homepage, footer, contacts/about pages, admin → System → Settings → Store (sanitized).
4. **Theme identification** — active theme name (P2-A from [RUN-5-DATA-REQUEST.md](../tasks/RUN-5-DATA-REQUEST.md)).
5. **Extension/ocMod inventory** — high level (P2-B) — custom modules may embed brand strings.
6. **Store settings export** — sanitized list of keys: `config_name`, `config_owner`, `config_address`, `config_email`, `config_telephone`, `config_meta_title`, `config_meta_description`, `config_meta_keyword` (and multi-store rows if present).
7. **Signed Change Request** — from [change-request-template.md](../../../templates/change-request-template.md).
8. **Rollback plan instance** — from [rollback-plan-template.md](../../../templates/rollback-plan-template.md).

---

### Q5. What parts of the site are likely to contain old brand references?

**OpenCart / ocStore typical surfaces (verify on TEST):**

| Layer | Likely locations |
|-------|------------------|
| **Admin → Settings → Store** | Store name, owner, address, phone, email, meta title/description |
| **Database `oc_setting`** | Same keys persisted; possible extension-specific keys |
| **Information pages** | «О компании», «Контакты», privacy/terms if cloned from template |
| **Theme templates** | `catalog/view/theme/<active>/template/common/header.twig`, `footer.twig`, `home.twig` |
| **Language files** | `catalog/language/ru-ru/common/header.php`, `footer.php`, `mail/*.php` |
| **Images** | `image/catalog/logo*`, `image/<theme>/`, favicon at web root |
| **SEO** | `oc_seo_url` keyword segments; meta in layout controllers |
| **Email templates** | Order/mail language strings in `catalog/language/` and admin mail settings |
| **Extensions / ocMod** | Dealership modules, contact widgets, map modules — **SAFE UNKNOWN** until P2-B |
| **Modification cache** | `system/storage/modification/` — may retain old strings until refresh |
| **Structured data** | JSON-LD or microdata in theme — if template included dealership name |

---

### Q6. What risks exist for accidental leftovers?

| Risk | Severity | Mitigation |
|------|----------|------------|
| **Uncached ocMod copies** | High | Refresh modifications cache after text changes; re-grep |
| **Twig / OC cache** | Medium | Clear theme/cache after wave; verify storefront |
| **DB information pages not in admin UI list** | Medium | SQL grep on `oc_information_description` |
| **Image alt text and filenames** | Medium | Include `image/` in grep; replace assets not only HTML |
| **Multiple language packs** | Medium | If EN exists, grep both `ru-ru` and `en-gb` |
| **Extension config tables** | Medium | Inventory extensions first |
| **Email sender name / SMTP settings** | Low–Medium | Check mail settings if configured |
| **SEO URL slugs** | Low | Old brand in URL path — may need redirect plan (out of strict Phase 1 unless operator expands scope) |
| **Stale backup** | High | Fresh backup immediately before first write |
| **Operator brief / gate drift** | Medium | Align access brief before session |

---

### Q7. Can the operation be executed incrementally?

**YES** — **recommended**.

| Wave | Scope | Verification |
|------|-------|--------------|
| **W0** | Read-only discovery + grep baseline | No writes |
| **W1** | Admin store settings (`config_*` brand/contact/meta) | Storefront header/footer spot-check |
| **W2** | Information pages (about, contacts, legal) | Page content + footer links |
| **W3** | Logo / favicon upload + theme logo path | Visual + hard refresh |
| **W4** | Language file strings (if not DB-only) | Grep + UI sample |
| **W5** | Extension-specific configs (if any) | Operator sign-off per module |
| **W6** | Cache/modification refresh | Full grep for old-brand terms |
| **W7** | QA pass — checklist + screenshots | Sign-off |

Each wave: backup note, rollback scope limited to that wave where possible, `# REPORT — …` per session.

---

### Q8. Should backup/freeze be performed immediately before execution?

**YES — mandatory.**

| Requirement | Detail |
|-------------|--------|
| **Timing** | Immediately before **W1** (first write), not relying on 2026-05-31 claim alone |
| **Scope** | File backup + database backup of TEST instance |
| **Location** | External: `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups/` with dated label |
| **Freeze** | Optional metadata freeze document: pre-change screenshot set + settings export + grep baseline under `materials/phase1-pre-change-freeze/` |
| **Restore** | Operator confirms Beget restore path **before** W1 |

---

### Q9. What rollback strategy should be used?

| Tier | Trigger | Action |
|------|---------|--------|
| **T1 — Wave rollback** | Single wave fails verification | Restore only files/rows touched in that wave (if mapped); else T2 |
| **T2 — Full TEST restore** | Multiple failures / unknown delta | Beget file + DB restore to pre-W1 snapshot |
| **T3 — Operator halt** | Security concern, wrong environment | Stop; T2 after confirmation |

**Required artefact:** Completed [rollback-plan-template.md](../../../templates/rollback-plan-template.md) bound to Change Request ID, with pre-change snapshot paths and verification checks (storefront, admin login, sample information page, grep old-brand count = 0).

---

### Q10. What evidence should be collected before first modification?

| # | Evidence | Storage |
|---|----------|---------|
| 1 | Dated backup confirmation (file + DB) | External `backups/` + note in change request |
| 2 | Pre-change screenshot set (≥5 views) | External `materials/phase1-pre-change-freeze/` |
| 3 | Sanitized store settings export | External `materials/` |
| 4 | Old-brand grep report (files + DB) | External `materials/` + summary in repo report |
| 5 | Active theme + extension inventory | `theme-analysis/`, `extension-analysis/` when created |
| 6 | Approved Brand Replacement Pack v1 (operator sign-off) | External `materials/` |
| 7 | Signed Change Request + Rollback Plan | Repo `tasks/` or external `tasks/` |
| 8 | Write authorization on access brief | [project-access-brief.md](../project-access-brief.md) update |

---

## 5. Gate consistency check

| Check | Result |
|-------|--------|
| AUDIT-CHARTER allows writes | **FAIL** — read-only only |
| Access brief write permissions | **FAIL** — all write flags **NO** |
| Run 5 site evidence | **FAIL** — initialization only; B-EV-01..04 open |
| Target contact pack complete | **FAIL** — phone/messengers unknown |
| Logo assets staged | **FAIL** |
| Fresh backup | **FAIL** — stale claim only |
| Change Request + Rollback Plan | **FAIL** — not created |
| TEST environment confirmed | **PASS** |
| Baseline selected | **PASS** |
| Legal entity evidence (Atlas E1) | **PASS** — for legal text drafting only |

---

## 6. Pre-execution checklist (operator)

Use this checklist to unblock re-decision to **AUTHORIZED WITH NOTES**.

| # | Item | Owner | Done |
|---|------|-------|------|
| C-01 | Deliver **Brand Replacement Pack v1** (all target strings approved) | Operator | ☐ |
| C-02 | Deliver **old-brand search term list** | Operator | ☐ |
| C-03 | Stage **logo/favicon assets** in external `materials/` | Operator | ☐ |
| C-04 | Confirm **phones and messengers** | Operator | ☐ |
| C-05 | Update **project-access-brief** — write **YES** on TEST + approver name | Operator | ☐ |
| C-06 | Create **Change Request** + **Rollback Plan** instances | Operator + OCPilot | ☐ |
| C-07 | Run **read-only discovery** (W0): theme, settings export, grep baseline | Operator-supervised | ☐ |
| C-08 | Take **fresh file + DB backup**; record paths | Operator | ☐ |
| C-09 | Capture **pre-change screenshot set** | Operator | ☐ |
| C-10 | Confirm **admin URL** and session channel for W1 | Operator | ☐ |
| C-11 | Re-run this review or sign **DECISION v1.1** if all above **PASS** | Program owner | ☐ |

---

## 7. SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Exact old-brand strings on live TEST site | **SAFE UNKNOWN** — not in repo |
| Live platform version vs intake claim | **SAFE UNKNOWN** — no `index.php` proof |
| Active theme and extension set | **SAFE UNKNOWN** |
| Logo file paths on server | **SAFE UNKNOWN** |
| Whether prior partial rebranding occurred | **SAFE UNKNOWN** — business checklist ≠ proof |
| Backup restorability | **SAFE UNKNOWN** — not drill-verified |
| Multi-store configuration | **SAFE UNKNOWN** |
| Production site existence / drift | **SAFE UNKNOWN** — out of Phase 1 scope |

---

## 8. Related documents

| Document | Role |
|----------|------|
| [SITE-001-CHANGE-AUTHORIZATION-DECISION-v1.md](SITE-001-CHANGE-AUTHORIZATION-DECISION-v1.md) | Formal decision record |
| [project-access-brief.md](../project-access-brief.md) | Permissions gate |
| [AUDIT-CHARTER.md](../AUDIT-CHARTER.md) | Superseded for writes only after new write charter |
| [OPERATIONAL-INDEX.md](../../../OPERATIONAL-INDEX.md) | Program run index |

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-07 | **CREATED** — Phase 1 Brand Replacement authorization review; recommendation **NOT AUTHORIZED** for immediate execution |

*SITE-001 Change Authorization Review v1 — review and planning only; no site access performed.*
