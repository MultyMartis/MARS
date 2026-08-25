# i-SEO Sales Manager Bot

**project_id:** `iseo-sales-manager-bot`  
**Classification:** External operational product — n8n + Gmail + Google Sheets + Telegram  
**Logical owner:** OPS  
**Supporting systems:** ATLAS · MetaBOT SEO Content Agent patterns · MetaBOT Programmer / Developer · MARS Survivability / GitGuard  

**STATUS:** PRODUCTION STABLE  
**Stable designation:** [Sales Manager v2 — Production Stable Baseline 2026-08-17](baselines/PRODUCTION-STABLE-BASELINE-2026-08-17.md)  
**Freeze commit:** `35819a63bed132f2ccdb9e2d468e3ec3de9d23fe`  
**Start here after chat loss:** [FINAL-HANDOFF.md](FINAL-HANDOFF.md) · Agent brain: [AGENTS.md](AGENTS.md)

Older “Phase 3A / planned / runtime not started” statements in historical packs are **superseded** for production status. Phase 2/3A packs remain architecture history.

---

## Purpose

Human-supervised sales lead intake and manager assist for **i-SEO** (ORG-0003):

- intake lead emails from Gmail (full-source mode);
- durable RAW / full source logging;
- CLEAN normalized manager-facing lead state;
- Telegram card for managers (copy-ready first reply only — **never** auto-send to clients);
- Admin Telegram surface for lifecycle actions, raw source view, reminders, AI mode, health, stats, and config.

---

## Production workflows (stable)

| Workflow | ID | Role | State |
|----------|----|------|-------|
| **i-SEO Sales Manager - Operational.dev** | `xSnXPy8cEHoZw6xG` | Scheduled Gmail intake → parse → RAW → CLEAN → Telegram manager card → Gmail labels | **active** |
| **i-SEO Sales Manager - Admin.dev** | `wLrLp4WQHm1VJmxz` | Telegram admin + callbacks (processed / spam / raw source) + reminders | **active** |
| **Sales-Manager-v2** | `h8I2Tl2yl4uzhUnB` | Inactive reference | **inactive** |
| **Sales-Manager-v1** | `cJGoQUqIIHull4p7` | Legacy inactive | **inactive** |

Host: `n8n.ai-metacode.com` · **No workflow copies.** · AI: **OFF** · Reminders: **Mon–Fri 10:00 Europe/Moscow**.

Production model: `Gmail → durable RAW/full source → CLEAN → Telegram manager card`.

---

## Authority split

| Layer | Role |
|-------|------|
| **n8n** | Execution truth (external) |
| **Google Sheets** | **Current** durable RAW / CLEAN / CONFIG / diagnostics (operational persistence today) |
| **PostgreSQL** | **Preferred successor** system of record — roadmap only; not live |
| **Telegram** | Manager cards + admin commands |
| **MARS (`projects/iseo-sales-manager-bot/`)** | Architecture, contracts, baselines, evidence — **does not execute** the bot |

Sheets are honest current reality. They are **not** the preferred long-term architecture. See [SHEETS-DEPENDENCY-MAP.md](architecture/SHEETS-DEPENDENCY-MAP.md) and [DB-FIRST-SUCCESSOR-BLUEPRINT.md](roadmap/DB-FIRST-SUCCESSOR-BLUEPRINT.md).

---

## Document map (canonical)

| Area | Path |
|------|------|
| **Final handoff** | [FINAL-HANDOFF.md](FINAL-HANDOFF.md) |
| **Agent brain** | [AGENTS.md](AGENTS.md) |
| **Doc authority hierarchy** | [knowledge/DOC-AUTHORITY-HIERARCHY.md](knowledge/DOC-AUTHORITY-HIERARCHY.md) |
| **Current architecture** | [architecture/CURRENT-PRODUCTION-ARCHITECTURE.md](architecture/CURRENT-PRODUCTION-ARCHITECTURE.md) |
| **Stable baseline** | [baselines/PRODUCTION-STABLE-BASELINE-2026-08-17.md](baselines/PRODUCTION-STABLE-BASELINE-2026-08-17.md) |
| Acceptance / known state | [baselines/PRODUCTION-STABLE-ACCEPTANCE-MATRIX-2026-08-17.md](baselines/PRODUCTION-STABLE-ACCEPTANCE-MATRIX-2026-08-17.md) · [baselines/PRODUCTION-STABLE-KNOWN-STATE-2026-08-17.md](baselines/PRODUCTION-STABLE-KNOWN-STATE-2026-08-17.md) |
| Data / lifecycle / Gmail / Telegram / reminder / admin | [architecture/DATA-STATE-MODEL.md](architecture/DATA-STATE-MODEL.md) · [LEAD-LIFECYCLE-CURRENT.md](architecture/LEAD-LIFECYCLE-CURRENT.md) · [GMAIL-INTAKE-CONTRACT.md](architecture/GMAIL-INTAKE-CONTRACT.md) · [TELEGRAM-PRODUCT-CONTRACT.md](architecture/TELEGRAM-PRODUCT-CONTRACT.md) · [REMINDER-CONTRACT.md](architecture/REMINDER-CONTRACT.md) · [ADMIN-OPERATOR-CONTRACT.md](architecture/ADMIN-OPERATOR-CONTRACT.md) |
| Sheets map | [architecture/SHEETS-DEPENDENCY-MAP.md](architecture/SHEETS-DEPENDENCY-MAP.md) |
| Lessons / anti-patterns | [knowledge/LESSONS-LEARNED.md](knowledge/LESSONS-LEARNED.md) · [knowledge/ANTI-PATTERNS.md](knowledge/ANTI-PATTERNS.md) |
| Runbooks / recovery | [runbooks/OPERATIONAL-RUNBOOKS.md](runbooks/OPERATIONAL-RUNBOOKS.md) · [recovery/RECOVERY-GUIDE.md](recovery/RECOVERY-GUIDE.md) |
| Reproduce for new client | [playbooks/REPRODUCE-SALES-MANAGER-FOR-NEW-PROJECT.md](playbooks/REPRODUCE-SALES-MANAGER-FOR-NEW-PROJECT.md) |
| Checklists | [checklists/](checklists/) |
| DB-first roadmap | [roadmap/DB-FIRST-SUCCESSOR-BLUEPRINT.md](roadmap/DB-FIRST-SUCCESSOR-BLUEPRINT.md) · [roadmap/DB-FIRST-MIGRATION-ROADMAP.md](roadmap/DB-FIRST-MIGRATION-ROADMAP.md) |
| Deferred product / research | [roadmap/DEFERRED-PRODUCT-ROADMAP.md](roadmap/DEFERRED-PRODUCT-ROADMAP.md) · [roadmap/DEEP-RESEARCH-BACKLOG.md](roadmap/DEEP-RESEARCH-BACKLOG.md) |
| Project-neutral template | [roadmap/PROJECT-NEUTRAL-TEMPLATE.md](roadmap/PROJECT-NEUTRAL-TEMPLATE.md) |
| Evidence / reports (historical) | [evidence/](evidence/) · [reports/](reports/) |
| Phase 2 architecture (historical) | [architecture/](architecture/) `*-v1.md` |

---

## Hard constraints (operator-attested / freeze)

1. Exactly **two** active production workflows (Operational.dev + Admin.dev); v2 remains inactive reference.  
2. AI processing is **optional**; current stable state **AI OFF**.  
3. AI OFF: no OpenRouter call; zero AI tokens; fully operational.  
4. First replies are for **manual manager copy only**.  
5. **Never** send replies automatically to real clients.  
6. `📄 Исходная заявка` shows literal source (not field reconstruction, not CLEAN substitute).  
7. Do not discuss or embed OpenRouter / Gmail / Telegram credentials in docs or exports.  
8. Preserve foreign WIP; selective staging only when explicitly chartered.  
9. Any post-freeze behavior change = **new explicit phase**.  
10. Do not treat Sheets as the preferred target architecture for successors.

---

## Secrets and evidence

| Kind | Where |
|------|-------|
| Secrets / credentials | n8n credential store + CONFIG **references** (never values in Git) |
| Stable evidence | `evidence/stable-baseline-20260817/` |
| TMP acceptance tooling | May live under `X:\AI MARS STORAGE\incoming\…` — **not** production runtime |

---

## Not claimed

- Implemented multi-agent runtime inside MARS.  
- Full CRM / OPS-as-CRM.  
- Auto-reply to clients.  
- Natural Monday reminder live acceptance **PASS** (still **PENDING OBSERVATION** unless later evidence supersedes).  
- Live PostgreSQL migration completed.

---

## Next

Treat [FINAL-HANDOFF.md](FINAL-HANDOFF.md) and the 2026-08-17 baseline as canonical. Observe the first natural Monday 10:00 MSK reminder if not yet accepted. Use a separate deep-research phase before implementing DB-first next generation. Do not begin another Sales Manager behavior phase automatically.

---

*Knowledge consolidation: 2026-08-25.*  
*Stable freeze: 2026-08-17.*  
*Historical: Phase 2 / 2R / 3A documentation packs (2026-07-30).*
