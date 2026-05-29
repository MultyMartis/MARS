# NEXT-CHAT-MIGRATION-PROMPT v1

**Target chat name:** ORCA Upgrade After Battle Test  
**Target platform:** Web-GPT · MARS v2  
**Date prepared:** 2026-05-30  
**Source freeze:** `projects/orca/freeze/battle-pilot-triumph-search-v1/`

---

## Prompt (copy below this line)

---

**ACTIVE LANE:** B  
**CHAT TYPE:** ORCA System Architecture Upgrade  
**TARGET FOLDER:** `C:\AI MARS`  
**AGENT MODE:** Agent (human-supervised)

---

### CHAT TITLE

**ORCA Upgrade After Battle Test**

---

### GOAL

Analyze the first real Triumph Manipulator Search PPC battle cycle (ORCA → JSON → Exporter v1.4 → XLSX → Direct Commander import) and convert battle lessons into an improved ORCA system architecture — gates, transport model, checklists, and tooling roadmap.

**This chat produces architecture and documentation upgrades — NOT launch, NOT new XLSX, NOT ad/copy/keyword changes.**

---

### OPERATIONAL STATE (2026-05-30)

**Battle milestone frozen:** `projects/orca/freeze/battle-pilot-triumph-search-v1/`

| Component | State |
|-----------|-------|
| Route family (12 routes) | Frozen — `7666829` |
| URL canonical sync | Done — `f235bf1` |
| Exporter production baseline | Frozen — `2f01941` |
| Battle import file | v1.4 XLSX — Commander import **PASS** |
| Launch | **NOT approved** |
| Stable backups | `archive/stable-orca-after-triumph-battle-v1/` + Triumph PPC archive |

---

### KEY COMMITS

| Hash | Label |
|------|-------|
| `7666829` | ORCA route family freeze v1 |
| `f235bf1` | ORCA commander export URL synchronization v1 |
| `2f01941` | ORCA PPC exporter production baseline v1 |
| _(battle pilot commit)_ | ORCA battle pilot Triumph search stable v1 |

---

### WHAT HAPPENED (battle summary)

1. Built 12-route semantic family with differentiated content packs  
2. Created PPC JSON instance + validation-cli (345 rules)  
3. Iterated exporter v1.2 → v1.3 → v1.4 fixing transport bugs  
4. Synced URLs from legacy slugs to canonical `.html` on `manipulator-triumph.ru`  
5. Fixed duplicate ads (keyword×ad multiplication) via transport split v1.2  
6. Added bids (400–600 ₽) and cross-negatives in v1.3  
7. Fixed Commander minus syntax (wildcard ban) and metadata fidelity in v1.4  
8. **Real Direct Commander import PASS** with v1.4 XLSX  
9. **Post-import:** manual campaign strategy setup required for bids to appear in UI  
10. Budget / schedule — not in XLSX, set manually in Commander UI  

---

### CONFIRMED WORKING SYSTEMS

- ORCA semantic route family (12/12 packs)  
- JSON instance + validation-cli export gate  
- Exporter transport split (separate AD + KEYWORD rows)  
- Commander template v1 as Search Manual Bids SoT  
- URL canonical sync (registry + JSON + exporter)  
- Bid export (400–600 ₽, 10–90 ₽ spread)  
- Cross-negative matrix v1.4 (Commander-safe syntax)  
- Automated QA gates (`validate:launch-ready-v1.4`)  
- Direct Commander structural import  

---

### FAILURES FOUND (and fixed)

| Failure | Fix |
|---------|-----|
| Keyword×ad duplicate ads (108 rows) | Transport split v1.2 |
| Legacy URLs (11/12 routes wrong) | URL sync commit |
| Cross-negative wildcards rejected | v1.4 stem expansion |
| Wrong promotion URL (group landing vs root) | v1.4 metadata fidelity |
| Bids invisible until UI strategy setup | Documented post-import checklist |
| Budget/schedule not transportable | Accepted limit + checklist |

Full register: `freeze/battle-pilot-triumph-search-v1/FAILURES-AND-FIXES-v1.md`

---

### REQUIRED UPGRADES (from battle backlog)

**P0:**
- Final Website Copy Pack gate before Factory  
- Commander Export no-duplicate transport model (permanent architecture)  
- Commander-safe negative syntax (all export versions)  
- Post-import campaign settings checklist (formal gate)  
- URL registry/export sync gate (automated 3-layer check)  

**P1:**
- Automated cross-negative matrix builder  
- Bid priority model (intent tier → bid weight)  
- Commander hygiene scanner  
- Export readiness dashboard  
- Launch readiness checklist  

**P2:**
- DOCX/XLSX human artifacts  
- Future RSYA mode  
- Direct API research  
- Multi-project ORCA template  

Full backlog: `freeze/battle-pilot-triumph-search-v1/ORCA-UPGRADE-BACKLOG-v1.md`

---

### KEY READING (start here)

1. `projects/orca/freeze/battle-pilot-triumph-search-v1/README.md`  
2. `projects/orca/freeze/battle-pilot-triumph-search-v1/BATTLE-PILOT-SUMMARY-v1.md`  
3. `projects/orca/freeze/battle-pilot-triumph-search-v1/ORCA-LESSONS-LEARNED-v1.md`  
4. `projects/orca/freeze/battle-pilot-triumph-search-v1/ORCA-UPGRADE-BACKLOG-v1.md`  
5. `projects/orca/freeze/battle-pilot-triumph-search-v1/CAMPAIGN-SETTINGS-LAYER-v1.md`  
6. `projects/orca/OPERATIONAL-INDEX.md`  

---

### BOUNDARIES (non-negotiable)

- **NO** launch ads or set live budgets  
- **NO** change ad copy, keywords, URLs unless separate chartered task  
- **NO** generate new XLSX unless separate export task  
- **NO** git push unless explicitly requested  
- **NO** runtime, orchestration, or autonomous validation claims  
- **NO** governance expansion without explicit human charter  
- ORCA = human-supervised operational toolkit — not a bidding/launch product  

---

### NEXT ACTION PLAN (suggested for upgrade chat)

**Phase 1 — Architecture gates (P0):**
1. Design Final Website Copy Pack type + approval gate in content-packs workflow  
2. Document permanent no-duplicate transport model as ORCA PPC architecture pattern  
3. Promote `commander_negative_syntax_pass` to universal export validation  
4. Formalize post-import campaign settings checklist as separate READY gate  
5. Design URL registry/export sync automated check (3-layer)  

**Phase 2 — Tooling helpers (P1):**
6. Spec Commander hygiene scanner  
7. Spec export readiness dashboard (single QA view)  
8. Spec cross-negative matrix builder  

**Phase 3 — Optimization (P1):**
9. Design bid priority model (S/A/B tier → bid weight)  
10. Design launch readiness checklist (separate from export READY)  

**Deliverables:** Updated ORCA architecture docs, new gate contracts, tooling specs — **not** runtime code unless explicitly chartered.

---

### SAFE UNKNOWN

- Live SERP CPC calibration vs 400–600 ₽ defaults  
- Optimal Russian morphological coverage for cross-negatives  
- Conversion tracking / analytics verification pre-launch  
- Direct API feasibility vs Commander XLSX transport  
- RSYA template requirements  

---

### REPORT FORMAT

When completing upgrade work, start with:

```
# REPORT — ORCA Upgrade After Battle Test
```

Include: changed files, summary, git status, SAFE UNKNOWN, next action.

---

**END PROMPT**

---

## Usage notes

- Paste everything between "Prompt (copy below this line)" and "END PROMPT" into a new Web-GPT MARS v2 chat  
- Attach or reference `C:\AI MARS` workspace  
- Start with Phase 1 P0 items unless human redirects  
- Do not claim battle import was re-run in the upgrade chat unless explicitly done
