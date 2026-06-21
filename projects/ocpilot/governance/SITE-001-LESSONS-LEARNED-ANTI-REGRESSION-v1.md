# REPORT — SITE-001 LESSONS LEARNED / ANTI-REGRESSION UPDATE

**Type:** Governance update — lessons learned and anti-regression rules  
**Date:** 2026-06-10  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Scope:** Website Factory · OCPilot · Web-GPT workflow — **system rules only**

**Evidence base (read-only):**

| Source | Role |
|--------|------|
| [SITE-001-AI-WORKFLOW-FAILURE-AUDIT-v1.md](../sites/site-001/reports/SITE-001-AI-WORKFLOW-FAILURE-AUDIT-v1.md) | Primary failure audit |
| [SITE-001-RESTORE-POINT-REGISTRY-v1.md](../sites/site-001/reports/SITE-001-RESTORE-POINT-REGISTRY-v1.md) | Restore points + WF-V3 transition intent |
| W3 chain | W3-V · W3V2 · W3UX-C1 · W3ATMOSPHERE · W3VIS · W3WF-01 |
| W4 chain | W4 Used PDP · W4.1 Header & Hero · W4.1 Visual Proof Pack |
| W5 chain | Concept Workshop · W5-A · W5-A-S · W5-C |
| WF-V2 chain | GAP Analysis · W1–W4 execution reports |
| WF-V3 planning | **SAFE UNKNOWN** — intent in Restore Registry only; dedicated plan **not found in repo** |

**Explicit exclusions (honored):** No site modifications · No FTP · No CSS/Twig/PHP/JS · No TEST writes · No state/index updates · No charters · No implementation plans · No WF-V3 launch · No changes to existing rule documents

---

## 1. Executive Summary

### Главная ошибка

**Технический PASS подменял продуктовый PASS.** Цепочка Web-GPT → Website Factory → OCPilot авторизовала следующую волну при **HITL PENDING** на всех предыдущих. Автоматическая верификация (8-URL matrix, CSS markers, byte match) считалась достаточной для продолжения pipeline, хотя операторский запрос «3→7/10» и Visual Proof Pack фиксировали homepage **3/10**, GAP **25–30/100**, и Visual Change Failure Audit требовал **STOP** новых design CSS.

### Вторичная ошибка

**Потеря единого design authority и накопление cosmetic loop.** Три конкурирующих направления (Graphite Salon → Concept B Modern Dealer → WF V2 Light Clean Showroom) реализовывались параллельно без supersession gate. OCPilot и Web-GPT продолжали append-only CSS (146 KB → 222 KB, 10+ override blocks) и «cleanup после cleanup» вместо раннего clean-room prototype при GAP <50/100.

### Что обязательно менять

1. **Двухконтурная модель приёмки:** AUTOMATED PASS ≠ VISUAL ACCEPT — отдельные поля, отдельные гейты.
2. **HITL PENDING = HARD STOP** для авторизации следующей волны (Web-GPT) и для рекомендации next wave (OCPilot).
3. **Design authority lock** — один активный concept; screen blueprint в repo до implementation charter.
4. **Cosmetic loop cap** — максимум 2 последовательных visual pass <7/10 → architecture review или clean-room.
5. **CSS layer budget** — эскалация при >8 SITE blocks или >200 KB в `main.css`.
6. **GAP trigger** — alignment <50/100 vs target concept → clean-room prototype, не ещё один append block.
7. **Freeze WF-V2** на TEST; **WF-V3 только после** публикации этих правил и operator visual review.

### Классификация ошибок

| Класс | Примеры | Действие |
|-------|---------|----------|
| **Разовые** | Partial twig deploy W2A (исправлен в сессии); W3VIS rollback same day; W3-C operator rejection → rollback | Сохранить rollback discipline; не кодифицировать как системный gate |
| **Системные** | HITL PENDING не блокирует pipeline; PASS WITH NOTES читается как success; три design authority; append-only без budget; agent self-score 7/10; GAP ignored | **Обязательные правила** (§3–§6) |
| **Предотвращаемые правилами** | Cosmetic loop; false PASS; OCPilot as designer; delayed clean-room; visual score inflation; homepage omission in first-impression program | **Findings F-01..F-15 + gates** |

---

## 2. Anti-Regression Findings

### F-01 — Technical PASS != Visual PASS

**Problem:** OCPilot decision docs и Web-GPT authorization chain трактовали automated PASS (URLs 200, markers present, regression matrix) как wave completion, хотя visual criteria оставались PENDING.

**Evidence:**
- [SITE-001-W5A-STABILIZATION-DECISION-v1.md](../sites/site-001/reports/SITE-001-W5A-STABILIZATION-DECISION-v1.md) — stabilization **PASS WITH NOTES**; W5-A COMPLETE **NO**; criterion 5 «feels intentional» **PENDING** → W5-C всё равно выполнен.
- [SITE-001-W5C-USED-PDP-DECISION-v1.md](../sites/site-001/reports/SITE-001-W5C-USED-PDP-DECISION-v1.md) — automated **PASS** при 7/7 visual HITL **PENDING**.
- [SITE-001-AI-WORKFLOW-FAILURE-AUDIT-v1.md](../sites/site-001/reports/SITE-001-AI-WORKFLOW-FAILURE-AUDIT-v1.md) §4 — таблица false PASS по всем волнам W3–WF-V2.

**Why it happened:** Единое поле «PASS WITH NOTES» смешивало deploy hygiene и perception outcome. OPERATIONAL-INDEX и state conflate TECH DONE с visual acceptance.

**Risk:** Любой будущий проект повторит 48h cosmetic loop с ощущением прогресса при стагнации perception class.

**Required Rule:** Decision reports **обязаны** содержать два независимых вердикта: `AUTOMATED_PASS` (yes/no) и `VISUAL_ACCEPT` (ACCEPT / REJECT / PENDING / WAIVED). Authorization chain читает только `VISUAL_ACCEPT`.

**Classification:** Системная · Предотвращается правилами

---

### F-02 — HITL Pending Escalation

**Problem:** `operator visual HITL PENDING` фиксировался честно в decision docs, но **никогда не эскалировался** в STOP и не блокировал следующую волну.

**Evidence:**
- Failure audit §3.A3 — every decision doc: automated PASS + HITL PENDING → next charter authorized.
- Restore Registry B.7 — W1/W2/W2A automated PASS; visual sign-off **PENDING** on all WF-V2 waves.
- W5-A-S decision: W5-B **NO** until W5-A accepted — формально верно, но W5-C authorized без operator close.

**Why it happened:** HITL был optional human step, не hard gate в Web-GPT prompt checklist. Нет SLA или escalation rule для deferred review.

**Risk:** HITL deferrable forever; pipeline velocity без product truth.

**Required Rule:** `HITL PENDING` > 0 waves = **HARD STOP** for new implementation prompts. Escalation: (1) operator review session artifact, or (2) explicit dated WAIVE with scope limit. Max 1 wave PENDING without escalation trigger.

**Classification:** Системная · Предотвращается правилами

---

### F-03 — Cosmetic Loop Trap

**Problem:** После Visual Change Failure Audit **STOP** и W4.1 Proof Pack homepage **3/10**, команда выполнила 15+ последовательных visual passes (W4→W5→WF-V2-W4) той же стратегии: CSS append → cleanup → anatomy → layout → surface cleanup.

**Evidence:**
- Failure audit §5 — cosmetic loop diagram (W3-V through WF-V2-W4).
- [SITE-001-W4-1-VISUAL-PROOF-PACK-v1.md](../sites/site-001/reports/SITE-001-W4-1-VISUAL-PROOF-PACK-v1.md) — homepage first screen **3/10**; verdict PARTIAL SUCCESS.
- WF-V2-W2S executed without separate decision doc — «cleanup after cleanup» signal.

**Why it happened:** Each wave returned automated PASS → hope that cumulative patches reach redesign without homepage/catalog scope or clean-room.

**Risk:** CSS debt compounds; perception ceiling ~6/10 on legacy OC DOM; operator trust erodes.

**Required Rule:** **Cosmetic Loop Cap** — 2 consecutive target-screen scores <7/10 (operator or Visual Proof Pack) → **STOP** append-only CSS; mandatory Website Factory architecture review or clean-room charter. **No third CSS-only pass** on same route family without twig consolidation or prototype fork.

**Classification:** Системная · Предотвращается правилами

---

### F-04 — OCPilot Acting As Designer

**Problem:** OCPilot принимал решения о visual direction без Website Factory sign-off — «hybrid» header, agent-estimated 7–8/10, ad hoc composition rules C-01..C-11 без source doc.

**Evidence:**
- WF-V2-W1 — hybrid header when spec `02` mandated light header; HITL override noted without WF decision artifact.
- W4/W5-C decisions — agent est. **7–8/10** without operator binding.
- W2A decision N-W2A-03 — «PDP Composition Audit doc not found» — rules applied ad hoc in CR.

**Why it happened:** Charters ambiguous; Web-GPT authorized implementation without pixel blueprint; OCPilot filled gaps to unblock execution.

**Risk:** Implementation invents design; conflicts with target concept; irreversible surface debt (W5-C card-in-card).

**Required Rule:** OCPilot **implements only** — charters must cite Website Factory screen blueprint ID + verified repo path. Ambiguity → **STOP**, request WF clarification. **No agent visual scores** in decision docs; only `operator score: PENDING`.

**Classification:** Системная · Предотвращается правилами

---

### F-05 — Website Factory Authority Loss

**Problem:** Три конкурирующих design authority без hard supersession: Graphite Salon (W3WF READY) → Concept B Modern Dealer (W5) → WF V2 Light Clean — implementation overlapped.

**Evidence:**
- [SITE-001-W3WF-01-VISUAL-IMPACT-DECISION-v1.md](../sites/site-001/reports/SITE-001-W3WF-01-VISUAL-IMPACT-DECISION-v1.md) — READY despite LOW–MEDIUM delta and cosmetic risk MEDIUM–HIGH acknowledged.
- [SITE-001-WEBSITE-FACTORY-DECISION-v1.md](../sites/site-001/reports/SITE-001-WEBSITE-FACTORY-DECISION-v1.md) — Graphite Salon authorized.
- [SITE-001-WF-V2-GAP-ANALYSIS-v1.md](../sites/site-001/reports/SITE-001-WF-V2-GAP-ANALYSIS-v1.md) — W5 moved **opposite** to WF V2 target; paradox documented, not resolved before W1.

**Why it happened:** No single-concept lock; supersession without retired tokens/hooks list; Concept Workshop good decision undermined by implementation bypass (W5-A reproduced 3-band dark shell).

**Risk:** Cascade war in CSS; operator cannot tell which concept is «active»; GAP grows while waves continue.

**Required Rule:** **One active design authority per site** — supersession doc must list retired tokens, hooks, and screens. No parallel mandates. Concept lock minimum 30 days or until operator supersession charter.

**Classification:** Системная · Предотвращается правилами

---

### F-06 — CSS Layer Debt

**Problem:** Append-only override discipline без layer budget — `main.css` 146 KB → 222 KB, 10+ SITE-001 blocks, specificity escalation.

**Evidence:**
- W3-V execution — «append-only override block» repeated per wave.
- Restore Registry A.4 vs B.3 — 146,267 bytes → 212,975 bytes (post-W3 snapshot).
- WF-V2-W4 — surface cleanup admits debt from W5-C+W2+W2S; main.css still 221 KB after W4.

**Why it happened:** Rollback-friendly append model favored over consolidation; no KB/block threshold gate.

**Risk:** Each new wave fights previous selectors; subtractive passes cannot flatten nested DOM; maintenance cost explodes.

**Required Rule:** **CSS Layer Budget** — before new override: report block count + total KB. Threshold: >8 SITE blocks OR >200 KB in `main.css` → **ESCALATE** to architecture review / consolidation / clean-room. No fourth append-only CSS wave on same route family without review.

**Classification:** Системная · Предотвращается правилами

---

### F-07 — Delayed Clean-Room Declaration

**Problem:** GAP analysis **25–30/100** и Failure Audit STOP не triggered clean-room prototype; WF-V2 continued as patches on V1.

**Evidence:**
- [SITE-001-WF-V2-GAP-ANALYSIS-v1.md](../sites/site-001/reports/SITE-001-WF-V2-GAP-ANALYSIS-v1.md) — CRITICAL gap; homepage not started (W5-B never chartered).
- Failure audit — GAP came **after** W5-C damage (shadows/cards); anatomy rebuild W2A came **after** flat/cleanup passes.
- Restore Registry E — WF-V3 intent documented; **no dedicated planning report in repo**.

**Why it happened:** No numeric GAP trigger rule; hope that WF-V2 waves on legacy DOM would close 70-point gap.

**Risk:** Months of experimental patches on TEST without merge path; WF-V3 starts late with heavier debt.

**Required Rule:** **Clean-Room Trigger** — GAP alignment <50/100 vs signed target concept OR 2 failed cosmetic loops OR legacy DOM blocks target perception class → declare clean-room prototype (isolated twig/CSS bundle or `prototype-*` route) **before** further production TEST patches.

**Classification:** Системная · Предотвращается правилами

---

### F-08 — Visual Score Inflation

**Problem:** Agent-estimated 7–8/10 в decision docs создавали ложное ощущение threshold met, пока Proof Pack показывал 3–6/10 на target screens.

**Evidence:**
- W5-C decision — agent est. 7–8/10; operator HITL required but upstream read as met threshold.
- W4.1 Proof Pack — homepage **3/10**, header **5/10** vs automated 9/9 PASS.
- W3ATMOSPHERE — cap ~6/10 documented; W3WF still READY as «finishing».

**Why it happened:** No ban on agent scores; no binding operator score field; inflated estimates used in impact threshold lines.

**Risk:** Web-GPT authorizes next wave citing agent score; operator never consulted.

**Required Rule:** **No agent-estimated perception scores** in OCPilot decision or execution reports. Scoring only via Visual Proof Pack template (zone table) or operator HITL form. Agent may note «automated inconclusive» — never numeric est. ≥6/10.

**Classification:** Системная · Предотвращается правилами

---

### F-09 — Visual Failure Audit STOP Not Enforced

**Problem:** Visual Change Failure Audit (2026-06-09) directive **STOP new design CSS** не удержан как hard gate — W4/W4.1/W5/WF-V2 continued.

**Evidence:** Failure audit §2 timeline — Visual Change Failure Audit → **STOP** → W4 Used PDP followed same day/next.

**Why it happened:** Audit was diagnostic, not wired to authorization checklist; no STOP latch in Web-GPT workflow.

**Risk:** Honest audits become theater; team learns audits are ignorable.

**Required Rule:** **Audit STOP Latch** — any audit with explicit STOP directive blocks new CSS/twig design waves until operator expectation workshop artifact filed and Website Factory re-authorizes scope.

**Classification:** Системная · Предотвращается правилами

---

### F-10 — Homepage Omission in First-Impression Program

**Problem:** «First impression» program (W5 Blueprint, Concept B) churned header/PDP while **homepage first screen unchanged** — largest perception gap.

**Evidence:**
- W4.1 Proof Pack — homepage **3/10**; W5-B (homepage) never chartered while W5-C ran.
- GAP Analysis — homepage hero CRITICAL gap; W5-B not started.

**Why it happened:** PDP/header easier to patch; homepage requires structural charter; no mandatory homepage gate in first-impression scope.

**Risk:** Operator sees no sitewide redesign despite many waves; 3-second test fails on entry route `/`.

**Required Rule:** **Homepage First-Screen Gate** — any «first impression» or «redesign progress» program must include homepage in Visual Proof Pack **before** marking phase progress. Homepage <6/10 → cannot authorize PDP-only waves as «redesign continuation».

**Classification:** Системная · Предотвращается правилами

---

### F-11 — Ghost Design Assets

**Problem:** WF-V2 GAP/plan reference `design/wf-v2-concept/` PNGs **not found in repo** at audit time — implementation against ghost references.

**Evidence:** Failure audit UNKNOWN table; GAP Analysis cites `01-sibcar-v2-concept.png`, `02-sibcar-v2-specification.png`.

**Why it happened:** Design assets stored externally or never checked in; no repo-existence gate before charter.

**Risk:** OCPilot interprets missing mocks; hybrid overrides; untestable alignment.

**Required Rule:** **Blueprint Repo Check** — implementation charter invalid unless every cited PNG/spec path **verified to exist** in repo or documented external storage with manifest link.

**Classification:** Системная · Предотвращается правилами

---

### F-12 — QA Audit Trail Gap

**Problem:** Reports cite `projects/ocpilot/sites/site-001/qa/*` screenshots; folder **empty or untracked** in git at audit time.

**Evidence:** Failure audit §3.D5; W4.1 Proof Pack evidence index points to qa paths.

**Why it happened:** Screenshots captured locally without git/storage policy; verification paths in reports only.

**Risk:** Post-hoc audit impossible; HITL cannot be reconstructed; false confidence in evidence.

**Required Rule:** **Screenshot Gate** — execution report incomplete unless before/after paths **verified on disk** at report time; storage policy (git or `C:\AI MARS STORAGE` manifest) required before wave marked AUTOMATED_PASS.

**Classification:** Системная · Предотвращается правилами

---

### F-13 — Composition Audit Missing as Deliverable

**Problem:** W2A CR cites composition rules C-01..C-11; no `COMPOSITION-AUDIT` file in reports tree — rules applied ad hoc.

**Evidence:** W2A decision N-W2A-03; Failure audit §3.C6.

**Why it happened:** Composition audit mandated in CR text, not as Website Factory deliverable gate.

**Risk:** Anatomy/layout waves without traceable design authority; inconsistent PDP structure.

**Required Rule:** **Composition Audit Deliverable** — anatomy/layout charters require `*-COMPOSITION-AUDIT-v1.md` from Website Factory with rule IDs; OCPilot CR must cite IDs, not paraphrase.

**Classification:** Системная · Предотвращается правилами

---

### F-14 — WF-V(n+1) Before WF-V(n) Closed

**Problem:** WF-V3 named in Restore Registry while WF-V2 still executing W4 on TEST; no freeze decision artifact.

**Evidence:** Restore Registry E — next intended transition WF-V3; B.1 scope vs W4 execution **LIKELY YES** on live TEST.

**Why it happened:** Strategic exit documented before experimental branch frozen; parallel planning and execution.

**Risk:** Unclear which branch is canonical; restore confusion; continued debt on «frozen» branch.

**Required Rule:** **Branch Freeze Gate** — WF-V{n} experimental branch requires formal FREEZE decision before WF-V{n+1} planning or implementation authorization.

**Classification:** Системная · Предотвращается правилами

---

### F-15 — Card-in-Card Architecture Approved

**Problem:** W5-C commercial stage added nested cards + shadows **opposite** to subsequent WF V2 subtractive target — should have been caught at design review.

**Evidence:** GAP Analysis — W5-C HIGH gap on used PDP; Failure audit §5 item 2.
- W5-C decision — `w5c-commercial-stage` unified deck with shadows.

**Why it happened:** Concept B «magazine stage» interpreted as raised panels; no anti-pattern check vs future/light target; no flat-showroom rule.

**Risk:** Subtractive waves (W2/W4) fight symptoms; cannot reach flat showroom class.

**Required Rule:** Website Factory **Anti-Pattern Check** — when target includes «flat showroom» / subtractive surfaces, reject blueprints with card-in-card, nested shadow stacks, or >2 container depths per zone.

**Classification:** Системная (process) · Разовая ошибка W5-C (конкретный blueprint) · Предотвращается правилами

---

## 3. New Website Factory Rules

Правила ниже — **новые обязательные** для всех Website Factory → OCPilot handoffs. Не заменяют существующие `DESIGN-SYSTEM-RULES-v1.md`; дополняют operational layer SITE-001 выявил как отсутствующий.

| ID | Rule | Trigger | Enforcement |
|----|------|---------|-------------|
| **WF-AR-01** | **Design authority before implementation** — один active concept per site; supersession doc lists retired tokens/hooks | New concept or direction change | No OCPilot charter without supersession or lock confirmation |
| **WF-AR-02** | **Screen architecture first** — per target screen: DOM zones, surface rules, anti-patterns, reference PNG path | Any implementation wave beyond FINISHING | Blueprint file + repo asset check |
| **WF-AR-03** | **Clean-room declaration** — if legacy DOM prevents target perception class, declare prototype route; do not approve more `main.css` tail overrides | GAP <50/100 or 2 failed cosmetic loops | Design-only task until prototype charter |
| **WF-AR-04** | **Stop cosmetic loop** — label token/color passes explicitly **FINISHING** (max +1 perception point) or **REJECT**; never **REDESIGN** | CSS-only charter request | REJECT if target is composition change |
| **WF-AR-05** | **Prototype before integration** — target concept judged on isolated prototype before merge to production theme | New visual class or concept supersession | Prototype PASS required |
| **WF-AR-06** | **Single concept lock 30 days** — no superseding direction without operator charter | Parallel concept proposals | Hold conflicting briefs |
| **WF-AR-07** | **Composition audit deliverable** — `*-COMPOSITION-AUDIT-v1.md` with rule IDs before anatomy/layout waves | Twig restructure charters | CR cites rule IDs |
| **WF-AR-08** | **Visual Proof Pack review** — Website Factory reviews zone scores before recommending operator PASS | Post-execution evidence | FAIL recommendation if homepage <6/10 in first-impression scope |
| **WF-AR-09** | **Anti card-in-card** — reject blueprints with nested cards/shadows when target is flat showroom | Blueprint review | REJECT or revise |
| **WF-AR-10** | **Blueprint repo check** — every cited asset path verified exists or external manifest linked | Pre-charter | INVALID charter if ghost path |
| **WF-AR-11** | **Homepage mandatory in first impression** — W5-B-equivalent cannot be deferred while PDP/header waves continue | First-impression program | Block «progress» claims |
| **WF-AR-12** | **Conflict resolution artifact** — mock vs spec conflicts (e.g. dark mock vs light spec) resolved in writing before W1 | Spec paradox detected | No implementation |
| **WF-AR-13** | **GAP response plan** — alignment score + mandatory response: clean-room / reversal / scope reduction | GAP analysis complete | No READY without response class |

---

## 4. New OCPilot Rules

| ID | Rule | Trigger | Enforcement |
|----|------|---------|-------------|
| **OC-AR-01** | **Technical PASS ≠ Visual PASS** — separate `AUTOMATED_PASS` and `VISUAL_ACCEPT` fields in every decision report | Post-execution decision | Never single «PASS WITH NOTES» for authorization |
| **OC-AR-02** | **Implements; does not invent** — ambiguous charter → STOP, request WF clarification | Missing blueprint ID or ghost asset | No deploy |
| **OC-AR-03** | **CSS layer budget** — pre-write report: SITE block count, `main.css` KB, line count | Before CSS override | >8 blocks or >200 KB → ESCALATE, no write without approval |
| **OC-AR-04** | **Three-strike append rule** — 3 append-only CSS waves on same route family → architecture review required | Wave planning | No 4th append without consolidation/clean-room |
| **OC-AR-05** | **Screenshot gate** — before/after paths verified on disk; manifest in execution report | Post-deploy | Incomplete report if paths missing |
| **OC-AR-06** | **No agent visual scores** — only `operator score: PENDING` or Proof Pack zone table | Decision/execution docs | Remove est. 7–8/10 pattern |
| **OC-AR-07** | **Partial twig deploy = FAIL** — DOM snapshot diff until full file verified | Twig deploy | W2A lesson |
| **OC-AR-08** | **HITL before next wave recommendation** — cannot recommend next wave if VISUAL_ACCEPT = PENDING | Decision closeout | Escalate to Web-GPT STOP |
| **OC-AR-09** | **Preserve rollback discipline** — backup-before-write; parent backup cited | Every write wave | Continue Phase 1 pattern |
| **OC-AR-10** | **Hybrid override forbidden** — spec deviation (e.g. hybrid header) without WF written decision | Charter vs spec conflict | STOP |
| **OC-AR-11** | **Composition audit citation** — anatomy CR must cite WF composition rule IDs | W2A-class waves | No ad hoc C-xx in CR only |
| **OC-AR-12** | **Cache risk annotation** — note `max-age` in report; not a PASS substitute for visual | CSS deploy | Operator hard-refresh reminder |

---

## 5. New Web-GPT Workflow Rules

| ID | Rule | Trigger | Enforcement |
|----|------|---------|-------------|
| **WG-AR-01** | **No implementation after failed visual review** — Proof Pack zone <7/10 on target screen → no new impl prompt for that scope | Post Proof Pack / operator feedback | HARD STOP |
| **WG-AR-02** | **No wave chaining with HITL pending** — previous wave VISUAL_ACCEPT must be ACCEPT or dated WAIVE | Charter authoring | Do not authorize |
| **WG-AR-03** | **Escalation rules** — 2 consecutive <7/10 → Website Factory architecture review or clean-room; no 3rd CSS pass | Cosmetic loop detection | Escalate, don't charter |
| **WG-AR-04** | **Design authority precedence** — Website Factory signed blueprint > OCPilot interpretation > agent improvisation | Conflict | Design-only task |
| **WG-AR-05** | **Audit STOP latch** — honor Visual Failure Audit STOP until expectation workshop artifact | Audit with STOP | No CSS/twig design waves |
| **WG-AR-06** | **One active design authority** — no parallel Graphite + Light mandates; supersession required | New direction prompt | Reject stacked mandates |
| **WG-AR-07** | **GAP <50/100 → clean-room** — block WF-V2-style production patches; authorize prototype only | GAP analysis | No append chain |
| **WG-AR-08** | **Homepage gate in first impression** — cannot claim redesign progress if homepage first screen unchanged | Program status | Honest status only |
| **WG-AR-09** | **No WF-V{n+1} while WF-V{n} HITL open** — applies W3/W4/W5/WF-V2 families | Branch transitions | Freeze first |
| **WG-AR-10** | **Do not ask OCPilot to be designer** — charters reference WF blueprint IDs only | Prompt drafting | Remove «hybrid» / «interpret concept» language |
| **WG-AR-11** | **False progress prohibition** — OPERATIONAL summaries must distinguish TECH DONE vs VISUAL ACCEPTED | Run logging | No DONE without visual column |
| **WG-AR-12** | **Operator expectation match** — if operator asked 3→7/10, CSS-only FINISHING waves insufficient; charter must say composition or clean-room | Task intake | Re-scope before impl |

---

## 6. Mandatory Gates

### Visual Gate

| Field | Definition |
|-------|------------|
| **Trigger** | Any wave claiming visual impact; post-execution decision; first-impression program checkpoint |
| **Pass condition** | Visual Proof Pack or operator HITL: target screens ≥7/10 (or program threshold); `VISUAL_ACCEPT = ACCEPT` |
| **Fail condition** | Any target screen <7/10; operator «не вижу изменений»; Proof Pack PARTIAL with homepage <6/10 in first-impression scope → **FAIL**; blocks next implementation authorization |

---

### HITL Gate

| Field | Definition |
|-------|------------|
| **Trigger** | Every OCPilot visual wave decision closeout; before Web-GPT next charter |
| **Pass condition** | Operator visual **ACCEPT** with dated note, or explicit **WAIVE** with scope limit and operator signature |
| **Fail condition** | `HITL PENDING` on closing wave; >1 wave with cumulative PENDING → **HARD STOP** until escalation session |

---

### Clean-Room Gate

| Field | Definition |
|-------|------------|
| **Trigger** | GAP alignment <50/100 vs signed concept; 2 failed cosmetic loops; Failure Audit STOP; legacy DOM blocks target class |
| **Pass condition** | Clean-room plan artifact exists; prototype route scoped; operator authorizes prototype charter only |
| **Fail condition** | Further production TEST append patches authorized while trigger active → **FAIL** governance |

---

### Layer Debt Gate

| Field | Definition |
|-------|------------|
| **Trigger** | Pre-write CSS override; 3rd append on same route family; post-wave `main.css` size check |
| **Pass condition** | ≤8 SITE blocks AND ≤200 KB OR architecture review APPROVED consolidation/clean-room |
| **Fail condition** | >8 blocks OR >200 KB without review; 4th append-only CSS on same route → **FAIL** — no write |

---

### Architecture Gate

| Field | Definition |
|-------|------------|
| **Trigger** | Twig restructure; layout recomposition; concept supersession; first-impression program start |
| **Pass condition** | Website Factory screen blueprint + composition audit (if anatomy); repo assets verified; anti-pattern check PASS |
| **Fail condition** | Charter without blueprint; ghost assets; card-in-card vs flat target; mock/spec conflict unresolved → **FAIL** — design-only |

---

### Branch Freeze Gate

| Field | Definition |
|-------|------------|
| **Trigger** | Experimental branch (e.g. WF-V2) complete or abandoned; transition to WF-V{n+1} |
| **Pass condition** | Formal FREEZE decision; restore point registered; no new writes on frozen branch |
| **Fail condition** | WF-V{n+1} planning/impl while WF-V{n} still receiving patches or HITL open → **FAIL** |

---

### Audit STOP Gate

| Field | Definition |
|-------|------------|
| **Trigger** | Any project audit issuing explicit STOP directive (e.g. Visual Change Failure Audit) |
| **Pass condition** | Expectation workshop artifact filed; Website Factory re-authorizes scoped work |
| **Fail condition** | New design CSS/twig waves while STOP active → **FAIL** |

---

## 7. Recommended Governance Updates

Документы **не изменять сейчас** — только рекомендации для последующих governance waves.

| Path | Reason | Priority |
|------|--------|----------|
| `projects/ocpilot/knowledge/OCPILOT-VISUAL-ACCEPTANCE-GATE-v1.md` | Codify two-gate model (AUTOMATED vs VISUAL); HITL PENDING blocks authorization; scoring template | **P0 — blocking** |
| `projects/ocpilot/knowledge/OCPILOT-CSS-LAYER-BUDGET-v1.md` | Max blocks/KB thresholds; escalation to consolidation/clean-room | **P0 — blocking** |
| `projects/ocpilot/knowledge/WEBSITE-FACTORY-DESIGN-AUTHORITY-v1.md` | Single owner, supersession, blueprint required fields, repo asset check | **P0 — blocking** |
| `web-gpt-sources/` operator playbook (or mars-v2 execution model addendum) | Web-GPT prompt checklist: WG-AR-01..12 | **P0 — blocking** |
| `projects/ocpilot/templates/visual-proof-pack-template.md` | Standardize W4.1-style zone scoring; FAIL rules | **P1** |
| `projects/ocpilot/sites/site-001/reports/SITE-001-WF-V2-FREEZE-DECISION-v1.md` | Formal experimental branch freeze (complement Restore Registry) | **P1** |
| `projects/ocpilot/sites/site-001/reports/SITE-001-WF-V3-CLEAN-ROOM-PLAN-v1.md` | Registry references WF-V3; plan missing | **P1** (planning only — not impl) |
| `projects/ocpilot/sites/site-001/design/wf-v2-concept/README.md` + PNG exports | Ghost asset paths in GAP/plan | **P1** |
| `projects/ocpilot/sites/site-001/reports/SITE-001-PDP-COMPOSITION-AUDIT-v1.md` | Formalize C-01..C-11 from W2A mandate | **P2** |
| `projects/ocpilot/sites/site-001/qa/README.md` | Screenshot naming, storage policy — audit trail broken | **P1** |
| `projects/ocpilot/OCPILOT-STATE.md` | Split TECH DONE vs VISUAL ACCEPTED per wave | **P2** |
| `projects/ocpilot/OPERATIONAL-INDEX.md` | Visual HITL column on run rows | **P2** |
| `workspaces/website-factory-reference-v1/design-system/DESIGN-SYSTEM-RULES-v1.md` | Add operational handoff rules WF-AR-01..13 or companion doc | **P2** |
| `projects/ocpilot/governance/SITE-001-LESSONS-LEARNED-ANTI-REGRESSION-v1.md` | **This document** — canonical anti-regression for SITE-001 and future sites | **P0 — done** |

---

## 8. Final Decision

### A. Freeze WF-V2 — **YES**

- Rationale: [SITE-001-RESTORE-POINT-REGISTRY-v1.md](../sites/site-001/reports/SITE-001-RESTORE-POINT-REGISTRY-v1.md) defines `site-001-wfv2-final-experimental-20260610`; further TEST patches compound CSS debt without HITL closure.
- Action: **No new WF-V2-W* waves on TEST**; current TEST = experiment snapshot for learning only.
- Formal FREEZE decision doc recommended (P1) but freeze behavior effective from this governance update.

### B. Adopt new rules — **YES (this document)**

- Rules WF-AR-01..13, OC-AR-01..12, WG-AR-01..12, and gates §6 are **mandatory** for all future SITE-001 work and **recommended default** for all OCPilot project sites until site-specific charter says otherwise.
- Minimum viable before any implementation return: Visual Gate + HITL Gate + Layer Debt Gate + Design Authority rules.

### C. Start WF-V3 only after governance update — **YES**

- WF-V3 clean-room prototype **not authorized** by this document.
- Prerequisites: (1) P0 knowledge docs published; (2) WF-V2 frozen on TEST; (3) design assets in repo or manifest; (4) `SITE-001-WF-V3-CLEAN-ROOM-PLAN-v1.md` written; (5) operator visual review session on experimental vs rebrand baseline.
- Sequence:

```
1. Freeze WF-V2 on TEST (no writes)                    ← immediate
2. Adopt anti-regression rules (this doc)              ← immediate
3. Publish P0 knowledge + Web-GPT checklist          ← next governance task
4. Check in WF-V2 concept assets OR storage manifest
5. Write WF-V3 clean-room plan (planning only)
6. Operator visual review (screenshots)
7. Only then authorize WF-V3 prototype charter
```

### Proposed default for future projects (not only SITE-001)

| Rule cluster | Apply |
|--------------|-------|
| Two-gate acceptance (F-01) | All OCPilot visual sites |
| HITL HARD STOP (F-02) | All Web-GPT → OCPilot chains |
| Cosmetic loop cap (F-03) | All CSS-only visual programs |
| Design authority lock (F-05) | All Website Factory handoffs |
| CSS layer budget (F-06) | All OpenCart/ocStore theme override work |
| Clean-room trigger (F-07) | All concept alignment programs |
| Screenshot/QA trail (F-12) | All waves with visual claims |

---

## UNKNOWN / SECURITY

| Item | Status |
|------|--------|
| WF-V3 planning report | **MISSING** — Restore Registry intent only |
| `design/wf-v2-concept/` in repo | **NOT FOUND** at audit time |
| QA screenshots in git | **NOT FOUND** — paths in reports only |
| Operator actual HITL scores | **SAFE UNKNOWN** — all pending |
| WF-V2-W4 on live TEST | **LIKELY YES** — out of registry alias scope |
| Beget restore drill | **SAFE UNKNOWN** |

**SECURITY RISK:** None identified (governance documentation only).

---

*SITE-001 Lessons Learned / Anti-Regression v1 — governance only; no site modifications; no commit implied.*
