# REPORT — SITE-001 AI WORKFLOW FAILURE AUDIT

**Type:** AI workflow failure audit — read-only analysis  
**Date:** 2026-06-10  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Scope:** Web-GPT tasking · Website Factory design authority · OCPilot execution · verification gates · WF-V2 branch · transition to WF-V3

**Explicit exclusions (honored):** No site modifications · No FTP · No deploy · No CSS/Twig/PHP/JS/DB changes · No new design waves · No updates to `OCPILOT-STATE.md` or `OPERATIONAL-INDEX.md`

**Evidence sources:**

| Source | Role |
|--------|------|
| `projects/ocpilot/sites/site-001/reports/` | 160+ wave reports, decisions, charters |
| `projects/ocpilot/OCPILOT-STATE.md` | Program state (read-only; not modified) |
| `projects/ocpilot/OPERATIONAL-INDEX.md` | Run index (read-only; not modified) |
| `projects/ocpilot/sites/site-001/reports/SITE-001-RESTORE-POINT-REGISTRY-v1.md` | Restore points + WF-V3 transition intent |
| `projects/ocpilot/sites/site-001/design/wf-v2-concept/` | **SAFE UNKNOWN** — referenced in GAP/plan docs; **no files found in repo** at audit time |
| `projects/ocpilot/sites/site-001/qa/` | Screenshot paths cited in execution reports; **folder empty or not tracked in git** at audit time |

---

## 1. Executive summary

### Что пошло не так

Цепочка Web-GPT → Website Factory → OCPilot **многократно выбирала путь наименьшего технического риска** (CSS-only append-only волны, marker-based verification, автоматический PASS) вместо пути **продуктового результата** (композиция, визуальный класс, clean-room при конфликте DOM). За ~48 часов (2026-06-09 — 2026-06-10) на TEST накопилось **10+ визуальных слоёв** в `main.css` (~146 KB → ~222 KB), **4+ twig-хука** на одном PDP, и **три конкурирующих design authority** («Graphite Salon» → Concept B «Modern Dealer» → WF V2 «Light Clean Showroom»), при этом **ни одна волна не получила binding operator visual HITL** перед авторизацией следующей.

Операторский запрос «сайт должен выглядеть заметно иначе (3→7/10)» был **формально принят** (Concept Workshop, W5 Blueprint, WF-V2 GAP), но **операционно проигнорирован**: после честного [Visual Change Failure Audit](SITE-001-VISUAL-CHANGE-FAILURE-AUDIT-v1.md) (mixed cause: changes too weak) команда **не остановилась**, а продолжила ту же стратегию — ещё CSS, ещё anatomy patch, ещё surface cleanup — вместо раннего clean-room prototype.

### Что сработало

- **Phase 1** brand replacement — дисциплинированный baseline, rollback, acceptance.
- **Честные аудиты** — Visual Change Failure Audit, W4.1 Visual Proof Pack (PARTIAL SUCCESS), WF-V2 GAP Analysis (~25–30/100 alignment).
- **Структурный инсайт W4** — twig grouping на used PDP как единственный путь мимо «косметики».
- **Website Factory pivot** — Concept Workshop отверг incremental Concept A; W5 Blueprint зафиксировал composition-first.
- **Restore discipline** — backup chain, [Restore Point Registry](SITE-001-RESTORE-POINT-REGISTRY-v1.md), явный переход к **WF-V3**.
- **OCPilot execution hygiene** — charters, CR, rollback plans, 8-URL matrices, cache clear, working copies.

### Главный root cause

**Отсутствие обязательного visual acceptance gate между волнами.** Технический контракт OCPilot (файлы загружены, маркеры есть, URL 200) **подменял** продуктовый контракт (3-second test, composition score ≥7/10, operator sign-off). Web-GPT авторизовал следующую волну при **HITL PENDING** на всех предыдущих. Website Factory **не удерживал единый design authority** и разрешал implementation prompts без screen-level blueprint. Результат: **cosmetic loop на legacy OpenCart DOM**, который structurally не может дать target perception class.

---

## 2. Timeline of decisions

| Wave / task | Intent | What was done | Result | Verdict |
|-------------|--------|---------------|--------|---------|
| **Phase 1** (W1A–W1G) | Ребрендинг АЦ → СИБКАР; SEO/legacy cleanup | Admin + theme + controllers + logos + DB SEO; stable checkpoint | **ACCEPTED WITH NOTES**; 13/13 URLs clean | **SUCCESS** — правильный scope и gates |
| **W3 visual passes** (W3-V → W3V2 → W3UX-C1 → W3ATMOSPHERE) | «Освежить» UI без структуры | 4 append-only CSS blocks в `main.css`/`media.css` | Automated **PASS WITH NOTES** each; operator «не вижу изменений» | **PRODUCT FAIL** — косметика на уже-grey baseline; audit confirmed weak deltas |
| **W3VIS-01A/01B** | PDP hero hierarchy | CSS-only; rolled back same day | T1 rollback **PASS** | **CORRECT ROLLBACK** — task drift detected |
| **W3WF-01 planning** | Consolidate «Graphite Salon» | Impact map: LOW–MEDIUM delta vs live TEST | **READY FOR IMPLEMENTATION** then **ON HOLD** | **HONEST PLANNING** — но risk «ещё косметика» был известен и проигнорирован позже |
| **Visual Change Failure Audit** | Почему оператор не видит redesign | HTTP/CSS probe: CSS **is** live; cause = weak + expectation | **STOP** new design CSS | **GOOD DIAGNOSIS** — **не удержан** как hard gate |
| **W4 Used PDP** | Structural slice — stop cosmetic for PDP | `product.twig` wrappers + scoped CSS | **PASS WITH NOTES**; HITL pending; agent est. 7–8/10 | **PARTIAL** — правильный тип работ; visual unconfirmed |
| **W4.1 Header & Hero** | Header shell + promo discipline | Twig classes + W4.1 CSS | 9/9 automated PASS; Visual Proof Pack **PARTIAL SUCCESS** | **PARTIAL** — promo YES (8/10); homepage NO (3/10) |
| **Website Factory Concept Workshop** | Выбрать direction для first impression | Concept B «Modern Dealer» selected; A/C rejected | Implementation **STOPPED** pending charter | **GOOD DECISION** — composition over polish |
| **W5-A Header Shell** | 3-band → 1 dealer shell (Concept B) | `header.twig` DOM regroup + W5-A CSS | 8/8 PASS; HITL **PENDING**; W5-A COMPLETE **NO** | **TECH PASS / PRODUCT OPEN** — stabilization followed without HITL close |
| **W5-A-S Stabilization** | Fix promo overlap, dropdowns, density | Nav grouping + W5-A-S CSS | **PASS WITH NOTES**; criterion 5 «feels intentional» **PENDING** | **TECH PASS** — closed defects, not perception |
| **W5-C Used PDP** | Magazine/commercial stage (Concept B) | Twig commercial stage + heavy CSS (shadows, cards) | **PASS WITH NOTES**; agent est. 7–8/10; HITL pending | **PRODUCT FAIL (in retrospect)** — добавил card-in-card против будущего WF V2 |
| **WF-V2 GAP Analysis** | Сравнить live vs WF V2 concept | Score **~25–30/100**; paradox: W5 moved **opposite** to target | Documentation only | **CRITICAL TRUTH** — should have triggered clean-room **before** WF-V2-W1 |
| **WF-V2-W1 Header** | Light clean header per spec `02` | **Hybrid** header (not pure light); twig + CSS block | 8/8 PASS; HITL pending; note: HITL override | **MIXED** — tech OK; design authority conflict unresolved |
| **WF-V2-W2 Flat PDP** | Subtractive flat stage | CSS de-cardification + `wfv2-flat-pdp` hook | **PASS WITH NOTES**; HITL pending | **COSMETIC ON TOP OF W5-C** — cannot fully flatten nested DOM |
| **WF-V2-W2S Clean Stabilization** | Stabilize W2 flat pass | Additional CSS cleanup block | Executed; no separate decision doc | **LOOP SIGNAL** — cleanup after cleanup |
| **WF-V2-W2A Anatomy Rebuild** | DOM anatomy per composition audit C-01..C-11 | Major `product.twig` restructure; partial deploy fixed same session | **PASS WITH NOTES**; composition audit doc **not found in repo** | **RIGHT TYPE, LATE** — should have been W4/W5-C prerequisite |
| **WF-V2-W3 Layout Recomposition** | 68/32 hero, offer column reorder | Twig reorder + layout CSS only | **ACCEPT** — 8/8 PASS; charter says no more cosmetic | **TECH SUCCESS** — fourth PDP pass in 24h |
| **WF-V2-W4 Surface Cleanup** | Final subtractive CSS pass | Remove borders/shadows accumulated W5-C+W2+W2S | **DONE** 8/8 PASS; main.css **221 KB** | **ADMISSION OF DEBT** — cleaning surfaces previous waves added |
| **WF-V3 planning** | Clean-room prototype transition | **Only** mentioned in Restore Point Registry | **No dedicated planning report in repo** | **SAFE UNKNOWN** — intent documented; plan not written |

---

## 3. Root cause analysis

### A. Prompting errors by Web-GPT

| # | Error | Evidence |
|---|-------|----------|
| A1 | **Authorized CSS-only waves when operator wanted redesign** | W3-V charter after W3-UX audit explicitly said cosmetic insufficient; W3V2 + W3ATMOSPHERE followed anyway |
| A2 | **Did not enforce Visual Failure Audit STOP** | Audit 2026-06-09: STOP new design CSS → W4/W4.1/W5/WF-V2 continued |
| A3 | **Authorized next wave with HITL PENDING on all prior waves** | Every decision doc: automated PASS + «operator visual HITL PENDING» → next charter authorized |
| A4 | **Asked OCPilot to be implicit designer** | WF-V2-W1 «hybrid» override when spec `02` mandated light header; no Website Factory sign-off artifact |
| A5 | **Stacked conflicting design mandates** | Graphite Salon (W3WF) → Concept B graphite shell (W5) → WF V2 light subtractive — no single owner resolution before code |
| A6 | **Delayed structural work** | W4/W5-C added shadows/cards; anatomy rebuild (W2A) came **after** flat/cleanup passes |
| A7 | **No clean-room trigger rule** | GAP analysis 25–30/100 did not block WF-V2 implementation; append-only continued |
| A8 | **False progress narrative** | OPERATIONAL-INDEX Run summaries present waves as DONE without visual acceptance |

### B. Execution errors by OCPilot

| # | Error | Evidence |
|---|-------|----------|
| B1 | **Treated technical PASS as wave completion** | Decisions: «PASS WITH NOTES» while all visual criteria **PENDING** |
| B2 | **Append-only CSS discipline without layer budget** | W3-V execution: «append-only override block» repeated per wave; main.css 146 KB → 222 KB |
| B3 | **Agent self-scored visual impact** | W4/W5-C/W2 decisions: agent est. 7–8/10 without operator binding |
| B4 | **Composition audit mandate without source doc** | W2A decision N-W2A-03: «PDP Composition Audit doc not found» — items applied ad hoc |
| B5 | **Partial deploy on critical twig** | W2A N-W2A-01: first deploy partial; fixed same session — process fragility |
| B6 | **Product-correct execution isolated cases** | W3-C rollback, W3VIS rollback — **good** when operator directed; not proactive on weak visuals |

**Mitigation (what OCPilot did right):** backups, rollback plans, 8-URL regression, scope allow-lists, cache clear, honest «HITL PENDING» labels (even if ignored upstream).

### C. Design-authority errors by Website Factory

| # | Error | Evidence |
|---|-------|----------|
| C1 | **Three authorities without hard supersession gate** | Graphite Salon READY → Concept B → WF V2 concept; implementation overlapped |
| C2 | **Approved W3WF-01 knowing LOW–MEDIUM delta** | Impact decision: 30–40% casual notice; «косметика» risk MEDIUM–HIGH — still READY |
| C3 | **Concept B internal contradiction** | Workshop: graphite immersive nav; WF V2 spec `02`: **light** header — GAP doc flags paradox; no resolution artifact before W1 |
| C4 | **W5 Blueprint approved but W5-B (homepage) never chartered** | Largest gap (carousel homepage) untouched while PDP/header churn continued |
| C5 | **No screen architecture before OCPilot for WF-V2 waves** | GAP + plan exist; per-wave pixel blueprints for W2/W2A/W3 not in repo |
| C6 | **Composition audit referenced, not delivered** | W2A CR cites C-01..C-11; no `COMPOSITION-AUDIT` file in reports tree |
| C7 | **Good decisions undermined by implementation bypass** | Concept A rejected as «same 3/10» → W5-A still reproduced 3-band dark shell |

### D. Process errors

| # | Error | Evidence |
|---|-------|----------|
| D1 | **No visual scorecard gate between waves** | 3-second test documented in W5 blueprint; never blocking |
| D2 | **Cosmetic loop not capped** | W2 → W2S cleanup → W2A anatomy → W3 layout → W4 cleanup = 5 PDP waves post-GAP |
| D3 | **Operator HITL structurally deferrable forever** | «PENDING» never escalated to STOP |
| D4 | **Design assets not in repo** | `wf-v2-concept/` PNGs referenced but absent — implementation against ghost references |
| D5 | **QA screenshots not guaranteed in git** | Reports cite `qa/*`; folder empty/untracked — breaks audit trail |
| D6 | **WF-V3 named before WF-V2 frozen** | Registry: transition to WF-V3; WF-V2 still executing W4 on TEST |

### E. Verification errors

| # | Error | Evidence |
|---|-------|----------|
| E1 | **8-URL HTTP matrix ≠ visual quality** | All waves: PASS on URLs while visual proof pack shows homepage 3/10 |
| E2 | **CSS marker presence ≠ perception** | Failure audit: byte-exact match + markers; operator sees no change |
| E3 | **No before/after scoring in automated gate** | Visual Proof Pack manual; not wired to PASS/FAIL |
| E4 | **Cache risk acknowledged, not gated** | `max-age=604800` noted in every decision; not in verification script |
| E5 | **Composition criteria split from automated** | W2A/W3: composition checklist manual; automated only checks markers/order |
| E6 | **False PASS culture** | «PASS WITH NOTES» read as success by Web-GPT for next authorization |

---

## 4. False PASS cases

| Wave | What PASS meant | Why false for design | Required criterion |
|------|-----------------|----------------------|-------------------|
| **W3-V** | 7/7 URLs; CSS block present | 2–4% canvas luminance shift; operator no UX gain per W3-UX audit | Operator ≥6/10 sitewide or **STOP** cosmetic chain |
| **W3V2** | 7/7 URLs; tokens live | Incremental on W3-V; dual CSS layer (56× legacy red) | Legacy purge or structural charter — not another overlay |
| **W3ATMOSPHERE** | 24 screenshots; bytes match | Failure audit: **primary cause weak deltas**; cap ~6/10 | Visual impact ≥7/10 operator score **before** any new wave |
| **W3-C** (pre-rollback) | 7/7 PASS | Operator rejected visual direction → rolled back | **Operator HITL before PASS** (lesson learned) |
| **W4 Used PDP** | 6/6 markers; no leak | HITL pending; isolated PDP change; sitewide still 3/10 | Used PDP ≥7/10 **operator** + homepage plan locked |
| **W4.1 Header & Hero** | 9/9 automated | Proof pack: homepage **3/10**, header **5/10**, PARTIAL SUCCESS | **FAIL** on homepage first screen → no W5 until resolved |
| **W5-A** | 8/8 verify | W5-A COMPLETE **NO**; «feels intentional» PENDING | Operator sign-off **mandatory** before W5-C |
| **W5-A-S** | Stabilization tasks PASS | Criterion 5 inconclusive; W5-B blocked but W5-C still ran | Enforce W5-A COMPLETE gate |
| **W5-C** | 8/8; modals PASS | Added shadows/card-in-card **opposite** WF V2; HITL pending | Composition blueprint sign-off + anti-card-in-card check |
| **WF-V2-W1** | Hybrid header markers | GAP: alignment 25–30/100; hybrid ≠ spec `02` light | **Website Factory** screen sign-off vs mock `01`/`02` |
| **WF-V2-W2** | Subtractive CSS deployed | Flattening W5-C nested DOM from outside — limited | Anatomy-first or clean-room |
| **WF-V2-W2A** | DOM order C-08..C-11 | Showroom perception criterion 7 **PENDING** | 3-second operator test **before** W3 |
| **WF-V2-W3** | **ACCEPT** (strongest automated) | Layout changed; visual class still OC-template; no HITL | Layout + surface class ≥7/10 combined |
| **WF-V2-W4** | Surface cleanup 8/8 | Cleaning debt from W5-C/W2; main.css still 221 KB | Consolidation/architecture review, not another append block |

---

## 5. Cosmetic loop diagnosis

### The loop

```
Legacy OpenCart template (auto theme)
    → W3-V CSS pass          (tokens, radius, shadows)
    → W3V2 CSS pass          (identity tokens)
    → W3UX-C1 CSS pass       (catalog density)
    → W3ATMOSPHERE CSS pass  (atmosphere — terminal layer, still weak)
    → [Failure Audit: STOP]  (ignored)
    → W4 twig patch          (PDP wrappers — first structure)
    → W4.1 CSS+twig          (header polish — PARTIAL)
    → W5-A twig+CSS          (header shell — graphite)
    → W5-A-S CSS cleanup
    → W5-C twig+CSS          (commercial stage — MORE cards/shadows)
    → WF-V2-W2 CSS subtractive pass
    → WF-V2-W2S CSS cleanup
    → WF-V2-W2A twig anatomy rebuild
    → WF-V2-W3 twig+layout CSS
    → WF-V2-W4 CSS cleanup
```

### Why it could not reach target

1. **DOM grammar unchanged at sitewide level** — homepage carousel, catalog bordered grid, dark modals, footer slabs — untouched through WF-V2-W4.
2. **Card-in-card is structural** — W5-C `w5c-commercial-stage` + inner `car_main_info` shadows cannot be fully «subtracted» by CSS alone; W2A/W3/W4 fight symptoms.
3. **Competing surface systems** — W3ATMOSPHERE graphite atmosphere + W5-A dark shell + WF-V2 light subtractive = cascade war; each wave adds selectors.
4. **Append-only architecture** — base theme 7k lines + 10 override blocks; specificity escalation, not redesign.
5. **No single composition owner per screen** — OCPilot executed charters; nobody held pixel authority at implementation time.
6. **Perceptual ceiling of CSS-only** — Failure audit: cap ~6/10 for atmosphere scope; operator wanted 7/10+ **composition** class.

### Why team stayed in loop

- Each wave returned **automated PASS** → Web-GPT authorized next.
- **HITL PENDING** never blocked pipeline.
- **Gap analysis came after W5-C** — damage (shadows/cards) already deployed.
- **Hope that one more pass** (flat → clean → anatomy → layout → surface) would cumulate to redesign without homepage/catalog scope.
- **WF-V2 framed as «visual class change»** but implemented as **more patches on V1** instead of isolated prototype.

---

## 6. Useful discoveries to preserve

| Discovery | Why keep |
|-----------|----------|
| **Phase 1 discipline** | Charter → CR → backup → execute → verify → decision; brand cleanup reproducible |
| **Backup chain + Restore Registry** | `pre-w5a-header-shell-*` rebrand baseline; `pre-wfv2-w4-*` experimental snapshot; parent chain documented |
| **Visual Change Failure Audit** | Definitive: CSS loaded ≠ operator satisfaction; mixed cause taxonomy |
| **W4 structural insight** | Used PDP needs twig grouping — CSS-only insufficient for composition |
| **W4.1 Visual Proof Pack** | Honest PARTIAL SUCCESS scoring template (header 5, promo 8, homepage 3) |
| **Concept Workshop rejection of Concept A** | Formal record that incremental polish fails 3-second test |
| **W5 First Impression Blueprint** | Composition-first architecture (shell, showroom entry, magazine PDP) — **not fully executed** but correct frame |
| **WF-V2 GAP Analysis** | Quantified misalignment (25–30/100); paradox W5 vs WF V2 documented |
| **W2A composition criteria C-01..C-11** | Right anatomy rules — should be **design doc**, not ad hoc in CR |
| **W3-C / W3VIS rollback culture** | Operator rejection → T1 restore works |
| **Append-only lesson** | W3-V execution explicitly documents rollback = 2 files — reuse for consolidation policy |
| **WF-V3 / clean-room intent** | Registry freezes WF-V2 as experimental branch — correct strategic exit |

---

## 7. New agent rules

### For Web-GPT

1. **No implementation prompt without visual acceptance gate** — previous wave must have operator visual **ACCEPT** or explicit **WAIVE** with dated note; `HITL PENDING` = **HARD STOP**.
2. **If 2 consecutive visual passes score <7/10 operator (or agent+proof pack <7/10 on target screens), STOP cosmetic loop** — escalate to Website Factory for architecture review or clean-room charter; **no third CSS pass**.
3. **Do not ask OCPilot to invent visual direction** — charters may only reference Website Factory signed screen blueprints (PNG/spec IDs); «hybrid» overrides require **written WF decision**.
4. **On conflict «CSS cleanup vs new design» → Website Factory blueprint wins** — if blueprint missing, task is **design-only**, not OCPilot.
5. **After Visual Failure Audit STOP directive → no new CSS/twig waves** until operator expectation workshop artifact filed.
6. **One active design authority per site** — supersession must list **retired tokens/hooks**; no parallel Graphite + Light Clean mandates.
7. **GAP score <50/100 vs target concept → clean-room prototype required** before production TEST patches continue.
8. **Homepage first screen is mandatory** in any «first impression» program — cannot mark redesign progress if homepage unchanged (W4.1 lesson).
9. **Do not authorize WF-V{n+1} while WF-V{n} HITL open** — applies to all wave families (W3, W4, W5, WF-V2).

### For Website Factory

1. **Design owner must produce screen architecture before implementation** — per screen: DOM zones, surface rules, anti-patterns, reference PNG in repo path **verified to exist**.
2. **If old DOM prevents target perception → declare clean-room prototype** — isolated HTML/twig route or `prototype-*` theme prefix; do not approve more overrides on `main.css` tail.
3. **Do not approve token/shadow/color passes as redesign** — label explicitly **FINISHING** (max +1 perception point) or **REJECT**.
4. **Single concept lock for 30 days** — no superseding direction without operator charter; supersession doc must reconcile conflicts (Graphite vs Light).
5. **Composition audit is a deliverable file** — `SITE-001-*-COMPOSITION-AUDIT-v1.md` required before anatomy/layout waves; cite rule IDs in OCPilot CR.
6. **Visual Proof Pack is part of design QA** — Website Factory reviews before recommending PASS to operator.
7. **Reject card-in-card architectures** in blueprints when target is «flat showroom» — W5-C should have been caught at design review.

### For OCPilot

1. **OCPilot implements; does not invent visual direction** — if charter ambiguous, **STOP** and request WF clarification; do not ship «hybrid» without decision doc.
2. **Technical PASS ≠ visual PASS** — decision reports must use **AUTOMATED PASS** vs **VISUAL ACCEPT** separate fields; never «PASS WITH NOTES» alone for authorization chain.
3. **Before adding CSS override, check layer debt** — report: count of SITE-001 blocks in `main.css`, total KB, lines; if >8 blocks or >200 KB → **ESCALATE** architecture review.
4. **After 3 append-only CSS waves on same route family → require architecture review** — no fourth without twig consolidation or clean-room.
5. **Screenshots and HITL required before next wave recommendation** — execution report incomplete without before/after paths **verified on disk**.
6. **No agent-estimated 7/10** in decision docs — replace with «operator score: PENDING» only.
7. **Partial twig deploy = FAIL** until verified — W2A lesson; add DOM snapshot diff to verification.
8. **Preserve rollback discipline** — continue backup-before-write; cite parent backup in every execution report.

---

## 8. Recommended documentation updates

*Do not create/update now — proposals only.*

| Path | What to add | Why |
|------|-------------|-----|
| `projects/ocpilot/knowledge/OCPILOT-VISUAL-ACCEPTANCE-GATE-v1.md` | Two-gate model: AUTOMATED vs VISUAL; HITL PENDING blocks authorization; scoring template | Prevent false PASS culture |
| `projects/ocpilot/knowledge/OCPILOT-CSS-LAYER-BUDGET-v1.md` | Max blocks per file, KB threshold, escalation to consolidation/clean-room | Stop append-only debt |
| `projects/ocpilot/knowledge/WEBSITE-FACTORY-DESIGN-AUTHORITY-v1.md` | Single owner, supersession rules, blueprint required fields, repo asset check | Resolve Graphite/Light conflicts |
| `projects/ocpilot/sites/site-001/reports/SITE-001-WF-V3-CLEAN-ROOM-PLAN-v1.md` | Scope: isolated prototype routes; migration path from WF-V2 experimental; exit criteria | Registry references WF-V3 but plan missing |
| `projects/ocpilot/sites/site-001/design/wf-v2-concept/README.md` + PNG exports | Check in `01-sibcar-v2-concept.png`, `02-sibcar-v2-specification.png` or document external storage path | GAP/plan reference ghost paths today |
| `projects/ocpilot/sites/site-001/reports/SITE-001-PDP-COMPOSITION-AUDIT-v1.md` | Formalize C-01..C-11 from W2A mandate | W2A applied rules without source doc |
| `projects/ocpilot/sites/site-001/qa/README.md` | Screenshot naming, viewport, git-lfs or storage policy | QA folder empty in repo — audit trail broken |
| `projects/ocpilot/templates/visual-proof-pack-template.md` | Scoring table per zone; FAIL if homepage <6/10 in first-impression scope | Standardize W4.1-style honesty |
| `projects/ocpilot/OCPILOT-STATE.md` | Split **TECH DONE** vs **VISUAL ACCEPTED** per wave | Current state conflates (future edit) |
| `projects/ocpilot/OPERATIONAL-INDEX.md` | Run rows: add Visual HITL column | Runs marked DONE without visual acceptance |
| `web-gpt-sources/` (or operator playbook) | Web-GPT prompt checklist: no impl without VISUAL ACCEPT | Source of prompting errors |
| `projects/ocpilot/sites/site-001/reports/SITE-001-WF-V2-FREEZE-DECISION-v1.md` | Formal experimental branch freeze criteria | Complement restore registry |

---

## 9. Decision proposal

### A. Freeze WF-V2 as experimental branch — **RECOMMENDED YES**

- **Rationale:** [Restore Point Registry](SITE-001-RESTORE-POINT-REGISTRY-v1.md) already defines alias `site-001-wfv2-final-experimental-20260610` (post-W3; W4 likely live). Further patches on TEST **compound CSS debt** without HITL closure.
- **Action:** No new WF-V2-W* waves on TEST; treat current TEST as **experiment snapshot** for learning only.

### B. Start WF-V3 clean-room prototype — **RECOMMENDED YES (after rules update)**

- **Rationale:** GAP analysis proves legacy DOM + override stack cannot reach ~8/10 WF V2 class. Clean-room = isolated implementation (separate twig/CSS bundle or prototype pages) judged against concept PNG **before** merge to production theme.
- **Prerequisite:** `SITE-001-WF-V3-CLEAN-ROOM-PLAN-v1.md` + design assets in repo + visual acceptance gate doc active.
- **Not authorized by this audit** — planning task only.

### C. Update agent rules before returning to SITE-001 implementation — **RECOMMENDED YES (blocking)**

- **Rationale:** Without rule changes, next implementation session will repeat: automated PASS → next wave → HITL pending → cosmetic loop.
- **Minimum viable:** Visual acceptance gate + CSS layer budget + Website Factory blueprint check + ban agent 7/10 estimates.

### Proposed sequence

```
1. Freeze WF-V2 on TEST (no writes)
2. Publish agent rules (OCPilot knowledge + WF/Web-GPT checklists)
3. Check in WF-V2 concept assets OR document storage path
4. Write WF-V3 clean-room plan
5. Operator visual review session on experimental vs rebrand baseline (screenshots)
6. Only then authorize WF-V3 prototype implementation charter
```

---

## Audit answers (task questions 1–10)

| # | Question | Short answer |
|---|----------|--------------|
| 1 | Web-GPT tasking errors | CSS waves after known failure; HITL ignored; conflicting mandates; no clean-room trigger at GAP 25/100 |
| 2 | OCPilot tech OK / product wrong | Perfect FTP/verify/backup; append-only CSS; agent-scored visuals; implemented hybrid without WF sign-off |
| 3 | Website Factory authority | Three directions; W3WF approved as READY despite cosmetic risk; no composition audit file; W5-B skipped |
| 4 | Why WF-V2 too long | Automated PASS chain; HITL never blocking; subtractive hope on additive W5-C base; no prototype fork |
| 5 | False PASS reports | See §4 — marker/URL PASS while proof pack shows 3–6/10 |
| 6 | Useless auto verification for design | 8/8 URL, marker, byte match — no 3-second test, no composition score, no before/after diff gate |
| 7 | CSS layer debt decisions | Append-only per W3/W4/W5/WF-V2 wave; no consolidation; W5-C + W2 added then W4 removed |
| 8 | Composition-worsening decisions | W5-C card-in-card; W5-A graphite vs WF V2 light; W2A after cosmetic passes; homepage never restructured |
| 9 | Useful to preserve | Phase 1, backups, failure audit, W4 insight, concept workshop, GAP analysis, proof pack, restore registry |
| 10 | New rules | See §7 — visual gate, cosmetic loop cap, WF blueprint first, OCPilot layer budget |

---

## UNKNOWN / SECURITY

| Item | Status |
|------|--------|
| WF-V3 planning report | **MISSING** — only restore registry mention |
| `design/wf-v2-concept/` assets in repo | **NOT FOUND** — referenced in GAP/plan |
| QA screenshots in git | **NOT FOUND** in workspace — paths in reports only |
| Operator actual HITL scores | **SAFE UNKNOWN** — all pending |
| Live TEST state vs registry (W4 on TEST) | Registry: W4 **LIKELY YES** — operator should confirm |
| Beget restore drill | **SAFE UNKNOWN** |
| Production domain | **Not in scope** — TEST only |

**SECURITY RISK:** None identified in audit (read-only documentation).

---

*SITE-001 AI Workflow Failure Audit v1 — audit only; TEST only; no commit; no push; no site modifications.*
