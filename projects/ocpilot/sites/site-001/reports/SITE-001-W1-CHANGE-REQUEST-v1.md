# SITE-001 W1 Change Request v1

**Status:** **READY FOR EXECUTION** — operator approval recorded  
**Requires human approval before execution.** *(satisfied — approver Андрей, 2026-06-08)*

**Type:** Formal change request — **documentation only**; no site modification performed in authoring  
**Date:** 2026-06-08  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`

---

## Request

| Field | Value |
|-------|-------|
| **ID** | CR-SITE-001-W1-2026-06-08 |
| **Site ID** | SITE-001 |
| **Date** | 2026-06-08 |
| **Requestor** | OCPilot Phase 1 program (operator-initiated pilot) |
| **Run reference** | OPERATIONAL-INDEX Run **4.101** — W1 Pre-Execution Package |
| **Phase** | W1 — Brand Replacement (Hmelnickiy → SIBCAR / СИБКАР) |
| **Charter** | [SITE-001-W1-WRITE-CHARTER-v1.md](SITE-001-W1-WRITE-CHARTER-v1.md) |
| **Execution spec** | [SITE-001-W1A-EXECUTION-SPEC-v1.md](SITE-001-W1A-EXECUTION-SPEC-v1.md) *(W1A)*; [SITE-001-W1-EXECUTION-PACK-v1.md](SITE-001-W1-EXECUTION-PACK-v1.md) *(full W1)*
| **Rollback plan** | [SITE-001-W1-ROLLBACK-PLAN-v1.md](SITE-001-W1-ROLLBACK-PLAN-v1.md) |

---

## Objective

Replace legacy **Hmelnickiy / Хмельницкий** branding on the SITE-001 **TEST** storefront with operator-approved **SIBCAR / СИБКАР** identity, attested legal entity data (LE-0005), and temporary demo contact placeholders — without catalog changes, theme redesign, or production deployment.

---

## Business reason

1. **Client onboarding** — Автосалон СИБКАР requires a rebranded TEST site before vehicle catalog load and SEO/Yandex Direct campaigns.
2. **OCPilot pilot** — First supervised write cycle to validate change control, backup/rollback discipline, and incremental wave execution on ocStore 3.0.3.8 (rs.2).
3. **Risk reduction** — Incremental W1A–W1F waves with grep QA minimize leftover legacy brand exposure before any production cutover (production **not** in scope).

---

## Affected components

| Component | Change summary | Primary wave |
|-----------|----------------|--------------|
| **OpenCart store settings** | `oc_setting` keys: name, owner, address, email, phone, meta, SMTP username | W1A |
| **Theme `auto` templates** | Header/footer/home/contact/about twig — phones, brand strings, alt, copyright, legal line | W1B |
| **Information pages** | 10 admin pages + custom about/contact controllers — brand and legal text | W1C |
| **Logo / favicon assets** | SVG/PNG/favicon set + `config_logo`, `config_icon` | W1D *(C-03)* |
| **Meta / OG** | Residual page meta; fix broken OG image reference | W1E |
| **Cache layer** | Theme/modification cache refresh post-change | W1F |

**Not affected:** product catalog, categories, extensions, `robots.txt` Host/Sitemap, DNS, production host, `config.php`, ocMod logic.

---

## Execution waves

Recommended order: **W1A → W1B → W1C → W1D → W1E → W1F**.

### W1A — Store Settings

| Field | Detail |
|-------|--------|
| **Method** | OpenCart admin → System → Settings → Store (store_id 0) |
| **Targets** | `config_name`, `config_owner`, `config_address`, `config_email`, `config_meta_title`, `config_meta_description`, `config_meta_keyword`, `config_mail_smtp_username` — see [SITE-001-W1A-EXECUTION-SPEC-v1.md](SITE-001-W1A-EXECUTION-SPEC-v1.md). **`config_telephone` excluded** — no phone change in W1A. |
| **Reference** | Execution pack §3.1 |
| **Verification** | Admin read-back; homepage title/meta view-source |

### W1B — Theme Contacts

| Field | Detail |
|-------|--------|
| **Method** | FTP/SFTP file edit |
| **Targets** | `catalog/view/theme/auto/template/common/header.twig`, `footer.twig`, `home.twig`; `information/contact.twig`, `about.twig`; `header_cup*.html` |
| **Reference** | Execution pack §3.2 |
| **Verification** | Storefront header/footer phone, alt text, copyright, H1 |
| **Note** | WhatsApp link requires operator decision (C-04) before session |

### W1C — Information Pages

| Field | Detail |
|-------|--------|
| **Method** | Admin HTML editor + FTP for controllers/twig |
| **Targets** | Information IDs 3,5,7,8,9,10,11,12,13,16; `catalog/controller/information/about.php`, `contact.php` |
| **Reference** | Execution pack §3.3 |
| **Verification** | Load each URL; grep for §2 legacy dictionary |

### W1D — Logos

| Field | Detail |
|-------|--------|
| **Method** | FTP upload + admin image paths |
| **Targets** | `/img/logo*.svg`, `/favicon/*`, `image/catalog/logo_balck.png`, `config_logo`, `config_icon` |
| **Reference** | Execution pack §3.4 |
| **Blocker** | **C-03** — logo assets not staged; wave **deferred** until assets in external `materials/` |

### W1E — Meta

| Field | Detail |
|-------|--------|
| **Method** | Admin + FTP |
| **Targets** | Per-page meta in controllers; OG `/img/preview.jpg`; confirm W1A meta propagation |
| **Reference** | Execution pack §3.5 |
| **Verification** | View-source on homepage + 3 service pages |

### W1F — QA

| Field | Detail |
|-------|--------|
| **Method** | Read-only grep + operator walkthrough + cache clear |
| **Targets** | Full §2 legacy dictionary; visual spot-check; screenshot evidence |
| **Reference** | Execution pack §3.6 |
| **Output** | `# REPORT — SITE-001 W1 QA` |

---

## Scope boundaries

| Field | Value |
|-------|-------|
| **Change type** | config / theme templates / information content / assets |
| **Read-only prep complete** | **yes** — W0 + W0.5 + W1 Execution Pack |
| **Target paths / tables** | See execution pack §3 and §7 rollback targets |
| **Out of scope** | Catalog, extensions, production, DNS, controller logic beyond W1C strings, EAR autonomous writes |

---

## Risk

| Field | Value |
|-------|-------|
| **Risk class** | **MEDIUM** (operator-assigned) — bounded TEST scope; reversible via T1/T2 |
| **Production impact** | **None** — TEST only |
| **Primary risks** | Leftover legacy brand strings; SMTP failure with demo email; phone display mismatch if W1B skipped; stale backup |
| **Rollback plan link** | [SITE-001-W1-ROLLBACK-PLAN-v1.md](SITE-001-W1-ROLLBACK-PLAN-v1.md) |

---

## Backup gate

| Field | Value |
|-------|-------|
| **File backup confirmed** | **YES** — operator confirmed 2026-06-08 (Beget; files backup created) |
| **DB backup confirmed** | **YES** — operator confirmed 2026-06-08 (database backup created) |
| **Backup location (external label)** | Beget backup system — operator-confirmed; archive filenames not recorded |
| **Prior backup (planning only)** | Beget 2026-05-31 — **superseded** by 2026-06-08 operator backup |

---

## Expected outcome

After successful W1A–W1F on TEST:

1. Storefront displays **СИБКАР** / **SIBCAR** branding per execution pack target map.
2. Legal blocks show **ООО «СибКар»** and attested LE-0005 address/requisites (formatted per operator session approval).
3. Demo phone `+7 (000) 000-00-00` and email `demo@sibcar.local` visible where mapped — marked **REPLACE BEFORE PRODUCTION**.
4. Legacy dictionary grep (execution pack §2) returns **zero** brand-context hits on scoped surfaces *(W1D may defer if C-03 open — document exception in QA report)*.
5. Post-change screenshot set stored under external `materials/phase1-post-change/`.
6. Session reports exist for each executed wave.

---

## Rollback trigger conditions

Execute rollback per [SITE-001-W1-ROLLBACK-PLAN-v1.md](SITE-001-W1-ROLLBACK-PLAN-v1.md) when **any** of:

| # | Condition | Typical tier |
|---|-----------|--------------|
| RT-01 | Wrong environment touched (not TEST URL) | **T3** → **T2** |
| RT-02 | Wave verification fails and cannot be corrected in session | **T1** or **T2** |
| RT-03 | Storefront or admin login broken after change | **T2** |
| RT-04 | Unintended files/tables modified outside wave scope | **T2** |
| RT-05 | Legacy brand grep shows unexpected widespread residue after wave | **T1** (same wave) or halt + **T2** |
| RT-06 | Operator or approver issues halt signal | **T3** |
| RT-07 | Security concern (credential exposure, wrong DB) | **T3** → **T2** |

---

## Approval (HITL)

| Field | Value |
|-------|-------|
| **Operator approval** | **APPROVED** |
| **Approved by** | **Андрей** |
| **Approved at** | **2026-06-08** |
| **Status** | **READY FOR EXECUTION** |
| **Conditions** | Fresh backup executed ✓; access brief write flags **YES** ✓; charter CH-01..CH-05 **PASS** ✓; WhatsApp decision before W1B |

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Named write approver | **Андрей** — recorded on access brief |
| SMTP deliverability with `demo@sibcar.local` | **SAFE UNKNOWN** — mail send test optional in W1F |
| Backup restore drill on Beget | **SAFE UNKNOWN** — operator acknowledgment required |
| Extension-specific brand keys | **SAFE UNKNOWN** — grep in W1F |

---

## Post-run

| Field | Value |
|-------|-------|
| **Report link** | `# REPORT — SITE-001 W1 <wave>` per session; final `# REPORT — SITE-001 W1 QA` |
| **Outcome** | *(pending)* — success / partial / rolled back / halted |

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-08 | **CREATED** — CR-SITE-001-W1-2026-06-08 |
| 2026-06-08 | **UPDATED** — operator approval **APPROVED**; approver **Андрей**; status **READY FOR EXECUTION**; backup gate satisfied |

*SITE-001 W1 Change Request v1 — planning only; no site modifications performed.*
