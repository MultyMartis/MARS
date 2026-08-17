> **Phase 3H.9 (2026-08-17):** False «Недостаточно прав» on raw lead was ACCESS/CONFIG Google Sheets `invalid_grant` mislabeled as a permission deny. Reminder 10:00 windows 15–17 Aug failed at CONFIG read with the same credential error before evaluation; 429 retry path was not applicable. Admin deny text + Sheets error classifier patched. Live Sheets OAuth reconnect by operator is still required before ADMIN_A raw retest and the next natural 4-recipient 10:00. Soak not restarted. Phase 3I.1 blocked. AI OFF.

# i-SEO Sales Manager Bot — Operational Index

**project_id:** `iseo-sales-manager-bot`  
**Process line:** ISEO-SALES-MANAGER-BOT  
**Primary logical owner:** OPS  
**Domain root:** [README.md](README.md)

---

## Current status

| Field | Value |
|-------|-------|
| **Status** | **PRODUCTION STABLE** |
| **Stable designation** | [Sales Manager v2 — Production Stable Baseline 2026-08-17](baselines/PRODUCTION-STABLE-BASELINE-2026-08-17.md) |
| **Active production** | Operational.dev **active** · Admin.dev **active** · Sales-Manager-v2 **inactive** reference |
| **AI** | **OFF** |
| **Reminders** | enabled · Mon–Fri · 10:00 Europe/Moscow · weekday gate on |
| **Raw source** | Literal Gmail/intake body via `📄 Исходная заявка` · filtered RAW lookup · legacy READ-only Gmail fallback |
| **Runtime** | External n8n (`n8n.ai-metacode.com`) — **not** executed from MARS |
| **Registry** | `project_id` **iseo-sales-manager-bot** (documentation registration; live product is external) |
| **Next** | Observe first natural Monday reminder if pending; any behavior change = **new explicit phase** |

**Supersession:** Older “planned / Phase 3A / Phase 3B NEXT / live parity SAFE UNKNOWN” index rows are historical relative to the 2026-08-17 stable freeze. Do not treat them as current production truth.

---

## Canonical stable docs

| # | Document | Role |
|---|----------|------|
| S1 | [baselines/PRODUCTION-STABLE-BASELINE-2026-08-17.md](baselines/PRODUCTION-STABLE-BASELINE-2026-08-17.md) | Canonical production baseline |
| S2 | [baselines/PRODUCTION-STABLE-ACCEPTANCE-MATRIX-2026-08-17.md](baselines/PRODUCTION-STABLE-ACCEPTANCE-MATRIX-2026-08-17.md) | Acceptance matrix |
| S3 | [baselines/PRODUCTION-STABLE-KNOWN-STATE-2026-08-17.md](baselines/PRODUCTION-STABLE-KNOWN-STATE-2026-08-17.md) | Known non-blockers |
| S4 | [evidence/stable-baseline-20260817/](evidence/stable-baseline-20260817/) | Sanitized freeze evidence |
| S5 | [reports/REPORT-iseo-sales-manager-bot-production-stable-baseline-freeze-2026-08-17.md](reports/REPORT-iseo-sales-manager-bot-production-stable-baseline-freeze-2026-08-17.md) | Freeze report |

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
| 1 | [architecture/TWO-WORKFLOW-ARCHITECTURE-v1.md](architecture/TWO-WORKFLOW-ARCHITECTURE-v1.md) | Phase 2 — superseded where conflicting with stable baseline |
| 2 | [architecture/LEAD-DATA-MODEL-v1.md](architecture/LEAD-DATA-MODEL-v1.md) | Phase 2 — see stable RAW/CLEAN contract |
| 3 | [architecture/LEAD-LIFECYCLE-v1.md](architecture/LEAD-LIFECYCLE-v1.md) | Phase 2 |
| 4 | [architecture/CONFIGURATION-MODEL-v1.md](architecture/CONFIGURATION-MODEL-v1.md) | Phase 2 — reminder keys live in production CONFIG |
| 5 | [architecture/TELEGRAM-UX-CONTRACT-v1.md](architecture/TELEGRAM-UX-CONTRACT-v1.md) | Phase 2 — see stable card actions + raw button |
| 6 | [architecture/ADMIN-COMMAND-CONTRACT-v1.md](architecture/ADMIN-COMMAND-CONTRACT-v1.md) | Phase 2 |
| 7 | [architecture/HEALTHCHECK-CONTRACT-v1.md](architecture/HEALTHCHECK-CONTRACT-v1.md) | Phase 2 |
| 8 | [architecture/AI-OFF-ON-CONTRACT-v1.md](architecture/AI-OFF-ON-CONTRACT-v1.md) | Phase 2 — current AI OFF matches contract default |

## Core Run — plans / ATLAS / Phase 3A (historical)

| # | Document | Status |
|---|----------|--------|
| 9–11 | [plans/](plans/) | Phase 2 historical |
| 12 | [atlas/ATLAS-REGISTRATION-RECOMMENDATION-v1.md](atlas/ATLAS-REGISTRATION-RECOMMENDATION-v1.md) | Recommendation only |
| 13–15 | [baselines/SOURCE-*.md](baselines/) · comparison | Phase 3A historical source-gap |
| 16–24 | [implementation/](implementation/) | Phase 3A implementation package historical |

## Reports

Recent production reports live under [reports/](reports/). Historical reports are **not** rewritten. Freeze report: [REPORT-iseo-sales-manager-bot-production-stable-baseline-freeze-2026-08-17.md](reports/REPORT-iseo-sales-manager-bot-production-stable-baseline-freeze-2026-08-17.md).

---

## Phase gates (historical → freeze)

| Phase | Scope | Status |
|-------|-------|--------|
| Phase 1–3A | Discovery → architecture → implementation package | Historical DONE |
| Live build / raw UX / reminders | Operator-chartered production phases | DONE (see evidence/) |
| **Stable freeze 2026-08-17** | Canonicalize accepted production contour | **DONE — PRODUCTION STABLE** |

---

## Forbidden without a new explicit phase

- Behavior changes to Gmail full-source, literal raw UX, lifecycle, dedupe, or reminder weekday policy
- Workflow copies / reactivation of Sales-Manager-v2 as production
- Enabling AI without charter
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

*Last updated: 2026-08-17 — Production Stable Baseline freeze.*
