# AGENTS.md — i-SEO Sales Manager Bot

**project_id:** `iseo-sales-manager-bot`  
**Audience:** Future MARS / Cursor Agents  
**Authority:** Invariants below + links to canonical docs. Do **not** treat historical Phase 2/3A packs or chat transcripts as override.

---

## 1. Stable designation (read first)

| Field | Value |
|-------|-------|
| Status | **PRODUCTION STABLE** |
| Designation | Sales Manager v2 — Production Stable Baseline 2026-08-17 |
| Freeze commit | `35819a63bed132f2ccdb9e2d468e3ec3de9d23fe` |
| Canonical start | [FINAL-HANDOFF.md](FINAL-HANDOFF.md) · [README.md](README.md) · [baselines/PRODUCTION-STABLE-BASELINE-2026-08-17.md](baselines/PRODUCTION-STABLE-BASELINE-2026-08-17.md) |
| Architecture | [architecture/CURRENT-PRODUCTION-ARCHITECTURE.md](architecture/CURRENT-PRODUCTION-ARCHITECTURE.md) |

MARS **documents** this product. **n8n** (`n8n.ai-metacode.com`) is execution truth.

---

## 2. Workflow authorities

| Workflow | ID | State |
|----------|----|-------|
| Operational.dev | `xSnXPy8cEHoZw6xG` | **active** — intake / RAW / CLEAN / cards |
| Admin.dev | `wLrLp4WQHm1VJmxz` | **active** — callbacks / reminders / admin |
| Sales-Manager-v2 | `h8I2Tl2yl4uzhUnB` | **inactive** reference |
| Sales-Manager-v1 | `cJGoQUqIIHull4p7` | **inactive** legacy |

**Prohibited:** casual workflow copies; reactivating v2 as production without charter.

---

## 3. Persistence reality vs target

- **Current:** Google Sheets = operational persistence / state (RAW, CLEAN, CONFIG, events, errors, dedupe). Document honestly.  
- **Target for successors:** **DATABASE-FIRST** — preferred **PostgreSQL**. Sheets → export/report/QA/migration only.  
- Maps: [architecture/SHEETS-DEPENDENCY-MAP.md](architecture/SHEETS-DEPENDENCY-MAP.md) · [roadmap/DB-FIRST-SUCCESSOR-BLUEPRINT.md](roadmap/DB-FIRST-SUCCESSOR-BLUEPRINT.md)  
- **Do not** migrate live production unless an explicit migration charter exists.

---

## 4. Product invariants

1. **AI OFF** — `ai_enabled=false`; OpenRouter disabled; deterministic path fully operational.  
2. **RAW ≠ CLEAN** — RAW = forensic visible source; CLEAN = operational normalized lead.  
3. **Gmail** — `simple=false`; capture full body **before** parse; snippet is not full-source authority.  
4. **Telegram actions** — ✅ Обработано · 🚫 Спам · 📄 Исходная заявка.  
5. **Raw button** — literal source; no field reconstruction; no CLEAN substitution; IP omitted; **no lifecycle mutation**.  
6. **Reminders** — Mon–Fri 10:00 Europe/Moscow; all still-actionable pending; Monday includes weekend backlog; exclude spam/processed/tests/archive; **notification only**.  
7. Natural Monday acceptance may still be **PENDING OBSERVATION** — do not claim PASS without evidence.  
8. **Never** auto-send replies to real clients.  
9. Re-delivery ≠ re-ingestion.  
10. Filtered Sheets lookups in callbacks — no broad RAW dumps (429 lesson).  
11. No secrets / raw PII in Git.  
12. Post-freeze behavior change = **new explicit phase**.

---

## 5. Canonical reading order

1. [FINAL-HANDOFF.md](FINAL-HANDOFF.md)  
2. [architecture/CURRENT-PRODUCTION-ARCHITECTURE.md](architecture/CURRENT-PRODUCTION-ARCHITECTURE.md)  
3. Topic contracts under `architecture/` (`DATA-STATE-MODEL`, `LEAD-LIFECYCLE-CURRENT`, `GMAIL-INTAKE-CONTRACT`, `TELEGRAM-PRODUCT-CONTRACT`, `REMINDER-CONTRACT`, `ADMIN-OPERATOR-CONTRACT`)  
4. [runbooks/OPERATIONAL-RUNBOOKS.md](runbooks/OPERATIONAL-RUNBOOKS.md) · [recovery/RECOVERY-GUIDE.md](recovery/RECOVERY-GUIDE.md)  
5. [knowledge/LESSONS-LEARNED.md](knowledge/LESSONS-LEARNED.md) · [knowledge/ANTI-PATTERNS.md](knowledge/ANTI-PATTERNS.md)  
6. For new clients: [playbooks/REPRODUCE-SALES-MANAGER-FOR-NEW-PROJECT.md](playbooks/REPRODUCE-SALES-MANAGER-FOR-NEW-PROJECT.md)  
7. Evidence/reports = history, not override  

Hierarchy: [knowledge/DOC-AUTHORITY-HIERARCHY.md](knowledge/DOC-AUTHORITY-HIERARCHY.md)

---

## 6. Git / worktree rules (MARS)

- Canonical branch: `mars/canonical-post-recovery`  
- Dirty MAIN / foreign WIP are normal — **do not** broad pull/reset/clean/stash/restore  
- Use clean worktree under `X:\AI MARS STORAGE\git-sync-*` for scoped commits  
- Never `git add .` / `-A` / `commit -a`  
- Stage allowlisted paths only  
- No force push  

---

## 7. Deferred (do not implement casually)

ACCESS vs DELIVERY, personal DND/mute, delivery modes, Lead Intake Anomaly Monitor, `/announce`, compact `/admin` panel, and Sheets→DB migration — see [roadmap/DEFERRED-PRODUCT-ROADMAP.md](roadmap/DEFERRED-PRODUCT-ROADMAP.md) and DB roadmaps. **CURRENT STABLE ≠ NEXT VERSION ROADMAP.**

---

## 8. What Agents must never assume

- That MARS runs the bot  
- That Sheets is the ideal long-term architecture  
- That AI is on  
- That Phase 2 lifecycle enums override live processed/spam button semantics  
- That TMP acceptance tooling is production runtime  
- That natural Monday reminder is accepted without evidence  

---

*Agent brain updated: 2026-08-25 knowledge consolidation.*
