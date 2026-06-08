# SITE-001 W1 Write Charter v1

**Type:** Write authorization charter — **documentation only**; no site modification performed in authoring  
**Date:** 2026-06-08  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Platform:** ocStore / OpenCart **3.0.3.8 (rs.2)** · active theme **`auto`**  
**Phase:** W1 — Brand Replacement (Hmelnickiy → SIBCAR / СИБКАР)

**Supersedes for W1 writes:** read-only limits in [AUDIT-CHARTER.md](../AUDIT-CHARTER.md) **only** for the scoped waves below, **after** operator confirms this charter on [project-access-brief.md](../project-access-brief.md) and pre-write backup (C-08 execution).

**Binding specifications:**

| Document | Role |
|----------|------|
| [SITE-001-W1-EXECUTION-PACK-v1.md](SITE-001-W1-EXECUTION-PACK-v1.md) | Target map, waves W1A–W1F, demo contacts |
| [SITE-001-W1-CHANGE-REQUEST-v1.md](SITE-001-W1-CHANGE-REQUEST-v1.md) | Formal change request |
| [SITE-001-W1-ROLLBACK-PLAN-v1.md](SITE-001-W1-ROLLBACK-PLAN-v1.md) | Rollback tiers T1–T3 |
| [SITE-001-W1-BACKUP-PROCEDURE-v1.md](SITE-001-W1-BACKUP-PROCEDURE-v1.md) | Pre-write backup checklist |
| [boundaries.md](../../../boundaries.md) | Program-wide forbidden operations |

---

## 1. Environment

| Field | Value |
|-------|-------|
| **Authorized environment** | **TEST only** |
| **TEST URL** | `https://sibcar.new-site.space/` |
| **Production** | **FORBIDDEN** — separate authorization required |
| **Staging / DEV / other hosts** | **FORBIDDEN** unless new charter issued |
| **store_id** | **0** (single store confirmed W0.5) |

Any session that cannot confirm TEST host and folder is **halted** (T3).

---

## 2. Allowed execution scope

Human-supervised writes permitted **only** on TEST, **only** within these waves and surfaces:

| Wave | Allowed operations | Access channel |
|------|-------------------|----------------|
| **W1A** | Admin → System → Settings → Store: `config_name`, `config_owner`, `config_address`, `config_email`, `config_telephone`, `config_meta_title`, `config_meta_description`, `config_meta_keyword`, `config_mail_smtp_username` | OpenCart admin UI |
| **W1B** | Theme template edits: `header.twig`, `footer.twig`, `home.twig`, `contact.twig`, `about.twig`, `header_cup*.html` — brand strings, phones, alt text, copyright, legal line, WhatsApp link per execution pack | FTP/SFTP |
| **W1C** | Information pages (IDs 3,5,7,8,9,10,11,12,13,16); custom `about.php`, `contact.php` and associated twig — brand/legal text only | Admin UI + FTP/SFTP |
| **W1D** | Logo/favicon upload and path updates: `/img/logo*.svg`, `/favicon/*`, `image/catalog/logo_balck.png`, `config_logo`, `config_icon`; optional archive of `logo - hmel.svg` | FTP/SFTP + admin *(after C-03)* |
| **W1E** | Residual per-page meta; OG image fix (`/img/preview.jpg`); confirm store meta propagation | Admin + FTP/SFTP |
| **W1F** | **Read-only** QA — grep, screenshots, cache clear, visual walkthrough | Read-only + admin cache tools |

**Supporting read-only actions** (any wave): theme/modification cache clear; view-source verification; sanitized settings read-back; legacy dictionary grep per execution pack §2.

**Values:** Apply only targets from [SITE-001-W1-EXECUTION-PACK-v1.md](SITE-001-W1-EXECUTION-PACK-v1.md) §1–§5. Demo contacts marked `[DEMO]` are **TEST placeholders** — not production targets.

---

## 3. Forbidden scope

| Category | Forbidden on TEST without new charter |
|----------|--------------------------------------|
| **Environment** | Production, DNS, domain, SSL, `robots.txt` Host/Sitemap changes |
| **Catalog** | Product import, category tree edits, price/stock bulk changes |
| **Code architecture** | Controller/model/ocMod/vQmod logic changes beyond listed W1C string edits |
| **Extensions** | Install/uninstall/enable/disable modules; extension config tables |
| **Database** | Destructive SQL (DROP, TRUNCATE, mass DELETE); schema changes |
| **Security** | `config.php` edits; credential exposure; admin user creation |
| **Theme redesign** | Layout/CSS/JS refactors beyond brand/contact string replacement |
| **Autonomous agent writes** | Any write without operator present and session-confirmed scope |
| **EAR / SFTP automation** | Mode 2 / PILOT-001 without HG-4 authorization (see EAR dry-run decision) |
| **Held items** | Yandex verification meta; vendor `MCA` author meta; legacy domain in `robots.txt` |
| **Banking / full requisites** | Full bank block on footer unless operator expands scope in writing |

**Default OCPilot forbidden list** remains in force for anything not explicitly listed in §2.

---

## 4. Operator authority

| Role | Authority |
|------|-----------|
| **Session operator** | Executes changes on TEST under this charter; confirms target host, wave scope, and backup before each write wave |
| **Write approver (HITL)** | **Named operator / program owner** — must approve wave start and sign off wave completion. *Name to be recorded on [project-access-brief.md](../project-access-brief.md) at charter activation.* |
| **OCPilot agent / assistant** | Documentation, checklists, grep analysis, session reports (`# REPORT — …`). **No autonomous FTP/admin/DB writes.** |
| **Atlas / legal source** | LE-0005 attested data supplies legal text only; does not authorize writes without operator |

**Session rules:**

1. One wave per supervised session where practical (W1A → W1B → …).
2. Operator verbal/written **GO** required before first edit in each wave.
3. Agent proposes; operator executes writes **or** explicitly delegates channel control for that wave.
4. End each session with `# REPORT — SITE-001 W1 <wave>` noting outcome and evidence paths.

---

## 5. Rollback authority

| Role | Authority |
|------|-----------|
| **Session operator** | Initiate **T1** (wave rollback) when verification fails within the same session |
| **Write approver** | Authorize **T2** (full TEST restore) when T1 insufficient or multi-wave delta unknown |
| **Any supervisor present** | **T3** emergency halt — stop all writes immediately; escalate to T2 after environment re-confirmation |

Rollback execution follows [SITE-001-W1-ROLLBACK-PLAN-v1.md](SITE-001-W1-ROLLBACK-PLAN-v1.md). No further writes until rollback verification passes or new session chartered.

---

## 6. Approval chain

```
Program discovery complete (W0, W0.5, W1 Execution Pack)
        ↓
Pre-execution package (this charter + CR + rollback + backup procedure) — CREATED
        ↓
Operator: execute fresh backup per C-08 procedure → evidence recorded
        ↓
Operator: update project-access-brief — write YES on TEST + named approver
        ↓
Write approver: sign Change Request v1 (SITE-001-W1-CHANGE-REQUEST-v1.md)
        ↓
Execution Authorization review (SITE-001-W1-EXECUTION-AUTHORIZATION-v1.md) — AUTHORIZED WITH NOTES minimum
        ↓
Per-wave: operator GO → supervised W1A..W1F → session REPORT
        ↓
W1F QA pass → Phase 1 TEST complete (production still separate gate)
```

**HG authorization path:** Human-supervised gate per [access-and-safety.md](../../../access-and-safety.md) and [shared/external-access-patterns/safety-boundaries.md](../../../../shared/external-access-patterns/safety-boundaries.md). EAR acquisition path exists for snapshots but **does not** replace this charter for CMS content writes.

---

## 7. Wave authorization model

| Wave | Pre-requisites | Authorized by | Stop conditions |
|------|----------------|---------------|-----------------|
| **W1A** | C-08 backup executed; access brief write flags; CR approved; this charter active | Write approver + operator GO | Admin save error; unexpected keys touched; wrong environment |
| **W1B** | W1A complete; theme write flag on brief; WhatsApp decision (C-04) for link handling | Write approver + operator GO | Template parse error; visible regression on homepage |
| **W1C** | W1A recommended complete; legal block §5 approved at session | Write approver + operator GO | Wrong information_id; legal text deviation without approval |
| **W1D** | **C-03** logo assets staged; W1B alt text aligned | Write approver + operator GO | Missing assets; broken image paths |
| **W1E** | W1A–W1C complete | Write approver + operator GO | OG/meta regression |
| **W1F** | W1A–W1E complete (W1D may be skipped if C-03 open) | Write approver | Legacy grep hits > 0; demo contacts missing |

**Parallelism:** Waves are **sequential** (W1A → W1B → W1C → W1D → W1E → W1F). No parallel write sessions on TEST.

**W1D exception:** W1A/B/C/E may proceed while W1D blocked on C-03; W1F may run with note «W1D deferred».

---

## 8. Charter activation checklist

| # | Item | Owner | Status |
|---|------|-------|--------|
| CH-01 | This document reviewed | Program owner | ☐ |
| CH-02 | [project-access-brief.md](../project-access-brief.md) updated — file/DB/theme writes **YES** on TEST | Operator | ☐ |
| CH-03 | Named write approver recorded on access brief | Operator | ☐ |
| CH-04 | Fresh backup executed per [SITE-001-W1-BACKUP-PROCEDURE-v1.md](SITE-001-W1-BACKUP-PROCEDURE-v1.md) | Operator | ☐ |
| CH-05 | Change Request signed | Write approver | ☐ |

Charter is **inactive** until CH-02 through CH-05 are **PASS**.

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-08 | **CREATED** — W1 Write Charter v1; TEST only; waves W1A–W1F |

*SITE-001 W1 Write Charter v1 — planning only; no site modifications performed.*
