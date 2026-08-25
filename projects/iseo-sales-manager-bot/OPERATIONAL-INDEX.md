# i-SEO Sales Manager Bot — Operational Index

**project_id:** `iseo-sales-manager-bot`  
**Process line:** ISEO-SALES-MANAGER-BOT  
**Primary logical owner:** OPS  
**Domain root:** [README.md](README.md) · **Handoff:** [FINAL-HANDOFF.md](FINAL-HANDOFF.md) · **Agent brain:** [AGENTS.md](AGENTS.md)

---

## Current status

| Field | Value |
|-------|-------|
| **Status** | **PRODUCTION STABLE** |
| **Stable designation** | [Sales Manager v2 — Production Stable Baseline 2026-08-17](baselines/PRODUCTION-STABLE-BASELINE-2026-08-17.md) |
| **Freeze commit** | `35819a63bed132f2ccdb9e2d468e3ec3de9d23fe` |
| **Active production** | Operational.dev **active** · Admin.dev **active** · Sales-Manager-v2 **inactive** reference |
| **AI** | **OFF** |
| **Persistence (current)** | Google Sheets (operational SoR today) |
| **Persistence (successor)** | PostgreSQL preferred — roadmap only |
| **Reminders** | enabled · Mon–Fri · 10:00 Europe/Moscow · weekday gate on · natural Monday acceptance **PENDING OBSERVATION** |
| **Raw source** | Literal Gmail/intake body via `📄 Исходная заявка` · filtered RAW lookup · legacy READ-only Gmail fallback |
| **Runtime** | External n8n (`n8n.ai-metacode.com`) — **not** executed from MARS |
| **Registry** | `project_id` **iseo-sales-manager-bot** in `registry/project-registry.md` |
| **Next** | Maintain stable contour; DB-first / deferred features require **new explicit phase** |

**Supersession:** Older “planned / Phase 3A / Phase 3B NEXT / live parity SAFE UNKNOWN” index rows are historical relative to the 2026-08-17 stable freeze. Do not treat them as current production truth.

---

## Canonical stable docs

| # | Document | Role |
|---|----------|------|
| S0 | [FINAL-HANDOFF.md](FINAL-HANDOFF.md) | Post-chat operator/Agent start |
| S1 | [baselines/PRODUCTION-STABLE-BASELINE-2026-08-17.md](baselines/PRODUCTION-STABLE-BASELINE-2026-08-17.md) | Canonical production baseline |
| S2 | [architecture/CURRENT-PRODUCTION-ARCHITECTURE.md](architecture/CURRENT-PRODUCTION-ARCHITECTURE.md) | Live architecture |
| S3 | [baselines/PRODUCTION-STABLE-ACCEPTANCE-MATRIX-2026-08-17.md](baselines/PRODUCTION-STABLE-ACCEPTANCE-MATRIX-2026-08-17.md) | Acceptance matrix |
| S4 | [baselines/PRODUCTION-STABLE-KNOWN-STATE-2026-08-17.md](baselines/PRODUCTION-STABLE-KNOWN-STATE-2026-08-17.md) | Known non-blockers |
| S5 | [evidence/stable-baseline-20260817/](evidence/stable-baseline-20260817/) | Sanitized freeze evidence |
| S6 | [reports/REPORT-iseo-sales-manager-bot-production-stable-baseline-freeze-2026-08-17.md](reports/REPORT-iseo-sales-manager-bot-production-stable-baseline-freeze-2026-08-17.md) | Freeze report |
| S7 | [architecture/SHEETS-DEPENDENCY-MAP.md](architecture/SHEETS-DEPENDENCY-MAP.md) | Current Sheets reality |
| S8 | [roadmap/DB-FIRST-SUCCESSOR-BLUEPRINT.md](roadmap/DB-FIRST-SUCCESSOR-BLUEPRINT.md) | Successor direction |

---

## Knowledge pack (2026-08-25 consolidation)

| Area | Path |
|------|------|
| Inventory / lessons / anti-patterns / hierarchy | [knowledge/](knowledge/) |
| Contracts (data, lifecycle, Gmail, Telegram, reminder, admin) | [architecture/](architecture/) `*-CURRENT*` / `*-CONTRACT*` / `DATA-STATE-MODEL` |
| Runbooks / recovery | [runbooks/OPERATIONAL-RUNBOOKS.md](runbooks/OPERATIONAL-RUNBOOKS.md) · [recovery/RECOVERY-GUIDE.md](recovery/RECOVERY-GUIDE.md) |
| Reproduce + checklists | [playbooks/](playbooks/) · [checklists/](checklists/) |
| Roadmap (DB, deferred, research, template) | [roadmap/](roadmap/) |

---

## Programme identity

| Field | Value |
|-------|-------|
| **Product name** | i-SEO Sales Manager |
| **Slug** | `iseo-sales-manager-bot` |
| **Business org** | ORG-0003 i-SEO Studio |
| **Primary manager user (v1)** | PER-0010 Дягилева Ольга (Оля) |
| **Owner / ops architect** | PER-0001 Русецкий Андрей *(multi-hat; operator attestation required for product edge)* |
| **Business owner signal** | PER-0011 Шваков Никита |
| **Pattern source** | MetaBOT SEO Content Agent patterns — reuse grammar, do not clone three workflows |

---

## Core Run — architecture (Phase 2 historical)

| # | Document | Status |
|---|----------|--------|
| 1–8 | [architecture/](architecture/) `*-v1.md` | Phase 2 — superseded where conflicting with stable baseline / CURRENT-* docs |

## Core Run — plans / ATLAS / Phase 3A (historical)

| # | Document | Status |
|---|----------|--------|
| 9–11 | [plans/](plans/) | Phase 2 historical |
| 12 | [atlas/ATLAS-REGISTRATION-RECOMMENDATION-v1.md](atlas/ATLAS-REGISTRATION-RECOMMENDATION-v1.md) | Recommendation only |
| 13–24 | [baselines/SOURCE-*.md](baselines/) · [implementation/](implementation/) | Phase 3A historical |

## Reports

Recent production reports live under [reports/](reports/). Historical reports are **not** rewritten.

---

## Phase gates

| Phase | Scope | Status |
|-------|-------|--------|
| Phase 1–3A | Discovery → architecture → implementation package | Historical DONE |
| Live build / raw UX / reminders | Operator-chartered production phases | DONE (see evidence/) |
| **Stable freeze 2026-08-17** | Canonicalize accepted production contour | **DONE — PRODUCTION STABLE** |
| **Knowledge consolidation 2026-08-25** | Handoff + reproduction + DB-first roadmap | **DONE (docs)** |
| DB-first migration / deferred product | Separate charters | **NOT STARTED** |

---

## Forbidden without a new explicit phase

- Behavior changes to Gmail full-source, literal raw UX, lifecycle, dedupe, or reminder weekday policy  
- Workflow copies / reactivation of Sales-Manager-v2 as production  
- Enabling AI without charter  
- Sheets → PostgreSQL cutover without migration charter  
- Broad git staging / clean / restore on dirty main worktree  
- Manual reminder trigger solely to “close” the pending natural observation  

---

## Related systems

| System | Relationship |
|--------|----------------|
| **OPS** | Logical owner of sales/ops assist contour |
| **MetaBOT SEO Content Agent** | Pattern source |
| **ATLAS** | Business reality IDs |
| **mars-survivability / GitGuard** | Selective staging, foreign WIP discipline |
| **iseo-report-hub** | Sibling i-SEO product — distinct `project_id` |

---

*Last updated: 2026-08-25 — Final knowledge consolidation (stable contour unchanged).*
