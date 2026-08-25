# Final Handoff — i-SEO Sales Manager Bot

**If the original Web-GPT conversation disappears, start here.**

| | |
|--|--|
| **Status** | PRODUCTION STABLE |
| **Designation** | Sales Manager v2 — Production Stable Baseline 2026-08-17 |
| **Freeze commit** | `35819a63bed132f2ccdb9e2d468e3ec3de9d23fe` |
| **Agent brain** | [AGENTS.md](AGENTS.md) |
| **Project root** | `X:\AI MARS\projects\iseo-sales-manager-bot\` (after sync) |

---

## Critical facts (60 seconds)

- Active: **Operational.dev** (`xSnXPy8cEHoZw6xG`) + **Admin.dev** (`wLrLp4WQHm1VJmxz`)
- Inactive: Sales-Manager-v2, Sales-Manager-v1
- Runtime: external n8n `n8n.ai-metacode.com` — MARS does **not** execute
- **AI OFF**
- Persistence **today:** Google Sheets (honest current SoR)
- Persistence **successor:** PostgreSQL preferred (roadmap only — do not migrate casually)
- Telegram: ✅ Обработано · 🚫 Спам · 📄 Исходная заявка
- Reminders: Mon–Fri 10:00 Europe/Moscow; natural Monday acceptance may still be **PENDING OBSERVATION**
- Raw source: literal body; filtered RAW-by-`lead_id`; no CLEAN reconstruction

---

## Canonical map

| Need | Path |
|------|------|
| Stable baseline | [baselines/PRODUCTION-STABLE-BASELINE-2026-08-17.md](baselines/PRODUCTION-STABLE-BASELINE-2026-08-17.md) |
| Current architecture | [architecture/CURRENT-PRODUCTION-ARCHITECTURE.md](architecture/CURRENT-PRODUCTION-ARCHITECTURE.md) |
| Data / state model | [architecture/DATA-STATE-MODEL.md](architecture/DATA-STATE-MODEL.md) |
| Lifecycle / dedupe | [architecture/LEAD-LIFECYCLE-CURRENT.md](architecture/LEAD-LIFECYCLE-CURRENT.md) |
| Gmail contract | [architecture/GMAIL-INTAKE-CONTRACT.md](architecture/GMAIL-INTAKE-CONTRACT.md) |
| Telegram contract | [architecture/TELEGRAM-PRODUCT-CONTRACT.md](architecture/TELEGRAM-PRODUCT-CONTRACT.md) |
| Reminders | [architecture/REMINDER-CONTRACT.md](architecture/REMINDER-CONTRACT.md) |
| Admin / operator | [architecture/ADMIN-OPERATOR-CONTRACT.md](architecture/ADMIN-OPERATOR-CONTRACT.md) |
| Sheets dependency map | [architecture/SHEETS-DEPENDENCY-MAP.md](architecture/SHEETS-DEPENDENCY-MAP.md) |
| Runbooks | [runbooks/OPERATIONAL-RUNBOOKS.md](runbooks/OPERATIONAL-RUNBOOKS.md) |
| Recovery | [recovery/RECOVERY-GUIDE.md](recovery/RECOVERY-GUIDE.md) |
| Lessons / anti-patterns | [knowledge/LESSONS-LEARNED.md](knowledge/LESSONS-LEARNED.md) · [knowledge/ANTI-PATTERNS.md](knowledge/ANTI-PATTERNS.md) |
| Reproduce for new client | [playbooks/REPRODUCE-SALES-MANAGER-FOR-NEW-PROJECT.md](playbooks/REPRODUCE-SALES-MANAGER-FOR-NEW-PROJECT.md) |
| Checklists | [checklists/](checklists/) |
| DB-first blueprint | [roadmap/DB-FIRST-SUCCESSOR-BLUEPRINT.md](roadmap/DB-FIRST-SUCCESSOR-BLUEPRINT.md) |
| DB migration roadmap | [roadmap/DB-FIRST-MIGRATION-ROADMAP.md](roadmap/DB-FIRST-MIGRATION-ROADMAP.md) |
| Deferred product | [roadmap/DEFERRED-PRODUCT-ROADMAP.md](roadmap/DEFERRED-PRODUCT-ROADMAP.md) |
| Deep research backlog | [roadmap/DEEP-RESEARCH-BACKLOG.md](roadmap/DEEP-RESEARCH-BACKLOG.md) |
| Project-neutral template | [roadmap/PROJECT-NEUTRAL-TEMPLATE.md](roadmap/PROJECT-NEUTRAL-TEMPLATE.md) |
| Doc hierarchy | [knowledge/DOC-AUTHORITY-HIERARCHY.md](knowledge/DOC-AUTHORITY-HIERARCHY.md) |
| Stable evidence | [evidence/stable-baseline-20260817/](evidence/stable-baseline-20260817/) |
| MARS registry | `X:\AI MARS\registry\project-registry.md` → `iseo-sales-manager-bot` |

---

## Hierarchy

```text
README / AGENTS
  → FINAL-HANDOFF (this file)
    → canonical topic docs (architecture/, baselines/)
      → runbooks / playbooks / checklists / recovery / roadmap
        → reports / evidence / Phase 2 *-v1.md (historical)
```

---

## Do not

- Change frozen production behavior without a new phase  
- Treat Sheets as preferred long-term architecture  
- Claim Monday natural reminder PASS without evidence  
- Commit secrets or raw PII  
- Broad-clean dirty MAIN worktrees  

Gate: `SM_FINAL_HANDOFF_COMPLETE`
