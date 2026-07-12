# REPORT — MetaBOT SEO Agent v14 PC14-FU-01 Sandbox Patch Proposal

**Date:** 2026-07-13  
**Classification:** Proposal-only · documentation · no live n8n mutation  
**Scope:** MetaBOT SEO Content Agent v14 (`@seo_content_agent_bot`) — Worker `Strict Cleanup` FU-01 family expansion  
**Lane:** B — MetaBOT / MetaBOT SEO Agent / MetaBOT Developer  
**Current PC statuses preserved:**  
- PC-14: `PC14_PRODUCTION_APPLIED_VERIFIED_WITH_FOLLOWUP_STRICT_BACKLOG`  
- PC14-FU-01 (this task): sandbox patch proposal only — **no apply**  
- PC-07: `PC07_PRODUCTION_APPLIED_VERIFIED`  
- PC-01: `PC01_MONITOR_NO_PATCH`

**Checkpoint commits verified:** `6263815c`, `1b954990`, `84dd9b07`, `af6fc35d`, `61bb6019`, `58c8f0b7`, `bc222072`, `46fc6335`, `c1915bc8`, `6704b174`, `6efd6afa`, `e3dc9ef7`, `e36ce56e`, `7e1c50ca`, `335b7f3c`, `688e1c03`, `96a8f08f`, `39a43028`, `1565dd9c`, `8af6d40d`, `bc8e63fb`, `abfd6d1c`, `459b7254`

**Constraints honored:** No live n8n mutation. No n8n API calls. No Telegram / OpenRouter / Sheets. No workflow / sandbox patch. No stage / commit / push. Foreign WIP preserved.

---

## 1. Executive Summary

This report defines a **future R1 sandbox patch** for PC14-FU-01: expand `Strict Cleanup` so five smoke residual families are cleaned with the same Unicode-boundary style as PC-14 R1, before `Strict Risk Scanner` runs.

| Item | Decision |
|------|----------|
| **Patch target** | Node `Strict Cleanup` **only** |
| **Version bump** | `v14-strict-cleanup-pc14-r1` → `v15-strict-cleanup-pc14-fu01-r1` |
| **Families** | `обеспеч*`, `контрол*`, `безопасн*`, `специализирован*`, `надежн*` / `надёжн*` |
| **Technique** | Phrase-first Unicode replacements; guarded morphology only when grammar-safe |
| **Non-targets** | `Format Run Pipeline`, `Strict Risk Scanner`, locks, memory, `/get`, Telegram, OpenRouter, Sheets, Intake, Admin |
| **Risk** | **R1** if scope stays cleanup + harness; broad `обеспечивает*` verbs → **FU-01B R2** split |
| **This task** | Proposal only — **does not apply** the patch |

**Smoke basis:** task `seo20260710153252t5pgjd`, Worker `3342`, `strict_risk_scan.count=8` with markers `обеспечения`, `обеспечение`, `контролируются`, `контроль`, `контроля`, `безопасности`, `специализированные`, `надежность`.

**Audit basis:** `459b7254` — FU-01 families are detected by scanner but not effectively cleaned; legacy `\b` Cyrillic rules do not fire; PC-14 R1 still works.

**Task status:** `COMPLETE — PC14-FU-01 sandbox patch proposal completed`  
**Next-step label:** `PC14_FU01_READY_FOR_SANDBOX_IMPLEMENTATION`

---

## 2. Preflight

| Check | Result |
|-------|--------|
| Working directory | `X:\AI MARS` — **PASS** |
| Volume `X:` label | `AI WS` — **PASS** |
| Git branch | `mars/canonical-post-recovery` — **PASS** |
| Staged changes | Empty — **PASS** |
| HEAD | `459b7254` — `docs(metabot): add pc14 fu01 strict family proposal` — **PASS** |
| `origin/mars/canonical-post-recovery` | Behind HEAD (local ahead ~10 MetaBOT docs commits; no pull/push) — **noted** |
| Checkpoints `6263815c` … `459b7254` (23) | All exist as commits — **PASS** |
| Live API / Telegram / OpenRouter / Sheets | None this session — **PASS** |
| Foreign WIP | Preserved — **PASS** |

**Authority docs read:** `AGENTS.md`, `.cursorrules`, `OPERATIONAL-INDEX.md`, `n8n-project-development-rules-v1.md`, `metabot-developer/safe-workflow-patch-protocol-v1.md`, `n8n-import-safe-generation-rules-v1.md`, `n8n-workflow-json-grammar-v1.md`, FU-01 audit/proposal, PC-14 closeout, operator smoke, production apply, sandbox implementation, strict cleanup audit.

**Evidence exports read:** `pc14-operator-smoke-verify-summary.json`, `pc14-operator-smoke-output-scan.json`, `pc14-production-strict-cleanup-node-diff.json`, `pc14-production-harness-results.json`, `SEO-Content-Agent-Beta-v14-Worker.production-pc14.after-patch.sanitized.json` (`Strict Cleanup` jsCode confirmed `v14-strict-cleanup-pc14-r1`, Unicode `BP`/`BS`/`rb()`, `families_patched: ['аккуратн','удобств','позволя']`).

---

## 3. Out-of-Scope Preserved

**OUT_OF_SCOPE_PRESERVED**

| Path / area | Signal |
|-------------|--------|
| Smart Reporter | not touched |
| I-SEO Report Hub | foreign WIP preserved |
| Website Factory / WordPress report hub | `M projects/mars-website-factory/...`, `M workspaces/website-factory-operations/...` — foreign WIP |
| FP-0002 | `M workspaces/fp-0002-*` — foreign WIP |
| OCPilot | `M projects/ocpilot/...` — foreign WIP |
| `.recovery-temp/`, `.restore-test-temp/`, `.tools/` | untracked foreign WIP |
| Live n8n / Telegram / OpenRouter / Sheets | no calls |
| Workflow / sandbox / production patch | **not performed** |
| Git stage / commit / push / pull / clean / reset / stash / restore | **not performed** |

---

## 4. Source Evidence

### 4.1 Smoke residual (PC-14 operator smoke)

| Field | Value |
|-------|-------|
| Task ID | `seo20260710153252t5pgjd` |
| Worker execution | `3342` (success) |
| Worker workflow | `p4mqb4VuPcemIDlC` — `SEO Content Agent Beta.v14 - Worker` |
| `strict_risk_scan.count` | **8** |
| `strict_risk_scan.verdict` | `reject` |
| Banner | `STRICT QA REJECT` present |
| PC-14 R1 families in SEO Текст | **0** hits (`PC14_TEXT_CLEANUP_PASS_TZ_RESIDUAL`) |
| PC-07 lock close | `done` with real `task_id` (not pending) |

### 4.2 Markers → FU-01 families

| Marker | Family |
|--------|--------|
| `обеспечения`, `обеспечение` | `обеспеч*` |
| `контролируются`, `контроль`, `контроля` | `контрол*` |
| `безопасности` | `безопасн*` |
| `специализированные` | `специализирован*` |
| `надежность` | `надежн*` / `надёжн*` |

### 4.3 Production baseline (post PC-14)

| Node | Version / state |
|------|-----------------|
| `Strict Cleanup` | `v14-strict-cleanup-pc14-r1`; Unicode `rb()`; R1 families only |
| `Strict Risk Scanner` | `v13-run-strict-risk-scanner-hard-v4` (detects all five FU-01 families) |
| `Format Run Pipeline` | Banner when `seoqa.verdict=reject` OR `strict_risk_scan.count > 0` |
| `Close Lock Before Sending` | `={{ $('Route Command').first().json.task_id }}` |

### 4.4 Gap (from FU-01 audit)

- Scanner detects FU-01 with Unicode boundaries.  
- Cleanup does **not** effectively clean them (local harness: samples unchanged; scan count stays > 0).  
- Legacy `\b` Cyrillic rules do not fire.  
- One legacy rule (`помогает обеспечить` → `…для обеспечения`) would **reintroduce** `обеспечения` if it ever matched — must be fixed/removed in FU-01.

---

## 5. Patch Target

| Field | Value |
|-------|-------|
| **Production source workflow** | `SEO Content Agent Beta.v14 - Worker` |
| **Production workflow ID** | `p4mqb4VuPcemIDlC` |
| **Future sandbox clone name** | `SEO Content Agent Beta.v14 - Worker.sandbox-pc14-fu01` |
| **Future sandbox webhook** | `seo-content-agent-worker-sandbox-pc14-fu01` |
| **Only node to patch** | `Strict Cleanup` |
| **Production mutation in this task** | **None** |
| **Sandbox mutation in this task** | **None** (proposal only) |

---

## 6. Non-Target Nodes

Do **not** change in FU-01 R1:

| Node / area | Reason |
|-------------|--------|
| `Format Run Pipeline` | Banner already correct; FU-01 must not touch banner logic |
| `Strict Risk Scanner` | Already detects FU-01; no scanner bug found |
| `Route Command` | Out of scope |
| `Close Lock Before Sending` | PC-07 guard — mapping must remain unchanged |
| `Close Single Lock Before Sending` | PC-07 guard |
| Finish Lock / Append Memory / Sheets write | Side effects; sandbox-disable only, no logic patch |
| `/get` nodes | Out of scope |
| Telegram send nodes | Out of scope |
| OpenRouter HTTP nodes | Out of scope |
| Intake / Admin workflows | Out of scope |
| Credentials, connections, workflow settings | Out of scope |
| Production activation state | Out of scope |

---

## 7. Proposed Version and Scope

### 7.1 Version

| From | To |
|------|----|
| `v14-strict-cleanup-pc14-r1` | `v15-strict-cleanup-pc14-fu01-r1` |

### 7.2 Metadata (proposed)

```javascript
strict_cleanup: {
  version: 'v15-strict-cleanup-pc14-fu01-r1',
  applied: true,
  replacements_count: /* pc14 + fu01 */,
  families_patched: [
    'аккуратн', 'удобств', 'позволя',           // preserve PC-14 R1
    'обеспеч', 'контрол', 'безопасн',
    'специализирован', 'надежн'
  ]
}
```

### 7.3 In-scope code changes

1. Keep existing PC-14 R1 Unicode helpers (`BP`, `BS`, `rb()`, `mapAcc`, convenience/позволя maps).  
2. Add `applyFu01Families(text)` **after** PC-14 family pass (or integrated with shared `rb()`).  
3. Phrase-first FU-01 replacement tables (§9–§13).  
4. Migrate/remove dead or counterproductive legacy `\b` rules that conflict with FU-01 (especially `безопасност*` → `условия перевозки`; `помогает обеспечить` → `…обеспечения`).  
5. Local harness only for verification (no live side effects).

### 7.4 Explicit non-goals

- No prompt / OpenRouter / Text Repair changes in R1.  
- No broad one-token swap of `обеспечивает*` verbs if grammar breaks → **FU-01B**.  
- No TZ/outline cleanup → **FU-02**.  
- No R3 multi-node hard-block redesign.

---

## 8. Unicode Boundary Strategy

Reuse PC-14 R1 helpers already in production `Strict Cleanup`:

```javascript
const BP = '(^|[^\\p{L}\\p{N}_])';
const BS = '(?=$|[^\\p{L}\\p{N}_])';

function rb(text, inner, to) {
  const re = new RegExp(`${BP}(${inner})${BS}`, 'giu');
  return text.replace(re, (m, p, w) => {
    replacements += 1;
    return `${p}${typeof to === 'function' ? to(w) : to}`;
  });
}
```

**Rules:**

| Rule | Detail |
|------|--------|
| Avoid ASCII `\b` for Cyrillic | Proven dead in FU-01 audit |
| Preserve left boundary group `p` | Do not eat punctuation/spaces |
| Support `ё`/`е` | Explicit alternation `е\|ё` or character class `[её]` |
| Phrase before morphology | Longer phrases first to avoid partial damage |
| Case | Prefer `giu`; preserve readability (title-case optional in harness review) |

**Optional phrase helper (pseudo-code):**

```javascript
function rp(text, phrase, replacement) {
  // phrase = literal or regex fragment without boundaries
  return rb(text, phrase.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), replacement);
  // or dedicated RegExp with BP/BS around escaped phrase
}
```

**Order inside `applyFu01Families`:**

1. High-confidence multi-word phrases (longest first).  
2. Specific noun phrases.  
3. Safe inflected standalone forms (case maps).  
4. Guarded family regex only when replacement is grammar-safe.  
5. Skip ambiguous verbs (`обеспечивает*`) unless a full phrase rewrite exists.

---

## 9. Replacement Strategy — `обеспеч*`

**Goal:** remove promise/guarantee tone without breaking verbs that need sentence rewrite.

### 9.1 High-confidence phrases (R1 — required)

| From | To |
|------|----|
| `для обеспечения безопасности перед работами` | `перед началом работ` |
| `обеспечение безопасности перед работами` | `отключение питания перед работами` |
| `обеспечение доступа к платам` | `доступ к платам` |
| `обеспечение доступа` | `получение доступа` |
| `для обеспечения доступа` | `для доступа` |
| `обеспечение качества` | `проверка результата` |

### 9.2 Legacy fix (R1 — required)

| From (legacy intent) | Action |
|----------------------|--------|
| `помогает обеспечить` → `используется для обеспечения` | **Remove or rewrite** to a form without `обеспеч*` (e.g. `используется для подготовки` / `поддерживает`) |

### 9.3 Deferred to FU-01B (do not force in R1)

| Forms | Reason |
|-------|--------|
| `обеспечивает`, `обеспечивают`, `обеспечивающий`, `обеспечивающая`, `обеспечивающее`, `обеспечивающие` | One-token swap often ungrammatical; needs sentence-level rewrite or prompt change |

### 9.4 Pseudo-code sketch

```javascript
// longest phrases first
text = rb(text, 'для обеспечения безопасности перед работами', 'перед началом работ');
text = rb(text, 'обеспечение безопасности перед работами', 'отключение питания перед работами');
text = rb(text, 'обеспечение доступа к платам', 'доступ к платам');
text = rb(text, 'для обеспечения доступа', 'для доступа');
text = rb(text, 'обеспечение доступа', 'получение доступа');
text = rb(text, 'обеспечение качества', 'проверка результата');
// do NOT blanket-replace обеспечивает*
```

**Acceptance:** no `обеспеч*` scanner hits on phrase samples; readable Russian; no new promise tone.

---

## 10. Replacement Strategy — `контрол*`

### 10.1 Phrase / form map (R1)

| From | To |
|------|----|
| `контролируются параметры` | `параметры фиксируются` |
| `параметры контролируются` | `параметры фиксируются` |
| `контроль качества` | `проверка результата` |
| `контроль после сборки` | `проверка после сборки` |
| `параметры контроля` | `проверяемые параметры` |
| `метод контроля` | `метод проверки` |
| `контроль давления` | `проверка давления` |
| `контроль температуры` | `проверка температуры` |
| standalone `контроль` | `проверка` |
| standalone `контроля` | `проверки` |

### 10.2 Notes

- Apply multi-word phrases **before** standalone `контроль`/`контроля`.  
- Preserve grammar in tables/headings (Unicode boundaries only; do not rewrite inside larger Cyrillic tokens).  
- Niche logistics legacy `контроль состояния и сохранности` → keep intent only if still needed; Unicode-ify; do not make it the only rule.  
- Prefer `фиксируются` / `проверка*` over empty deletion.

### 10.3 Pseudo-code sketch

```javascript
text = rb(text, 'контролируются параметры', 'параметры фиксируются');
text = rb(text, 'параметры контролируются', 'параметры фиксируются');
text = rb(text, 'контроль качества', 'проверка результата');
text = rb(text, 'параметры контроля', 'проверяемые параметры');
text = rb(text, 'метод контроля', 'метод проверки');
// ... pressure/temperature/after-assembly phrases ...
text = rb(text, 'контроль', 'проверка');
text = rb(text, 'контроля', 'проверки');
```

---

## 11. Replacement Strategy — `безопасн*`

### 11.1 High-confidence phrases (R1)

| From | To |
|------|----|
| `обеспечение безопасности перед работами` | `отключение питания перед работами` (also covered in §9) |
| `для обеспечения безопасности перед работами` | `перед началом работ` |
| `безопасность перед работами` | `подготовка перед работами` |
| `техника безопасности` | `регламент перед работами` |
| `требования безопасности` | `требования регламента` |

### 11.2 Standalone `безопасности`

**Do not** broad-replace unless context is known. Prefer phrase rules first.  
**Must remove** legacy universal `безопасност*` → `условия перевозки` (wrong niche semantics).

### 11.3 Principle

Prefer concrete procedure over abstract safety claims. Do not promise safety.

---

## 12. Replacement Strategy — `специализирован*`

### 12.1 Map (R1)

| From | To |
|------|----|
| `специализированные инструменты` | `инструменты для измерений` |
| `специализированный инструмент` | `инструмент для измерений` |
| `специализированное оборудование` | `оборудование для проверки` |
| `специализированные методы` | `методы проверки` |
| `специализированные приборы` | `измерительные приборы` |

### 12.2 Avoid

| Replacement | Why |
|-------------|-----|
| `профессиональный` | Marketing substitute |
| `экспертный` | Marketing substitute |
| Empty delete | Broken noun phrases |

Phrase-first; residual adjective morphology only if harness proves grammar-safe — otherwise leave for copy-review iteration, not production force-fit.

---

## 13. Replacement Strategy — `надежн*` / `надёжн*`

### 13.1 Map (R1)

| From | To |
|------|----|
| `надежность соединений` | `состояние соединений` |
| `надёжность соединений` | `состояние соединений` |
| `надежность работы` | `параметры работы` |
| `надёжность работы` | `параметры работы` |
| `надежная работа` | Prefer `работа без выявленных сбоев` (avoid `стабильная работа` unless scanner confirms `стабильн*` is allowed) |
| standalone `надежность` / `надёжность` | `состояние` **only** when phrase context supports it |

### 13.2 Notes

- Cover both `е` and `ё`.  
- Scanner morphology includes noun endings (`ость|ости|остью`) — cleanup must not stop at adjectives.  
- Avoid implied guarantees.  
- Legacy adj-only `\bнад[её]жн…\b` → `''` is dead/risky; replace with Unicode phrase-first + spacing-safe handling.

### 13.3 Pseudo-code sketch

```javascript
text = rb(text, 'над[её]жность соединений', 'состояние соединений'); // or two literal phrases
text = rb(text, 'над[её]жность работы', 'параметры работы');
// optional guarded noun residual only after phrases
```

---

## 14. Proposed Future Sandbox Workflow

| Field | Recommendation |
|-------|----------------|
| **Clone source** | Fresh clone of production Worker `p4mqb4VuPcemIDlC` (post–PC-14) |
| **Clone name** | `SEO Content Agent Beta.v14 - Worker.sandbox-pc14-fu01` |
| **Webhook path** | `seo-content-agent-worker-sandbox-pc14-fu01` |
| **Active** | `false` unless temporary activation required by established safe protocol for local-only tests |
| **Side-effect nodes** | Disable/bypass: OpenRouter, Telegram send, Finish Lock, Append Memory, any Sheets write — same pattern as PC-14 sandbox |
| **Patch scope in sandbox** | `Strict Cleanup` jsCode only |
| **Production** | Unchanged until separate production proposal + operator approval |
| **Protocol** | Follow `safe-workflow-patch-protocol-v1.md` Stages: clone → before export → patch → harness → after export → diff scope |

---

## 15. Proposed Test Matrix

### 15.1 FU-01 positive cleanup tests

| ID | Input | Expect |
|----|-------|--------|
| FU01-S01 | `для обеспечения безопасности перед работами` | Procedural neutral; no `обеспеч*` / `безопасн*` scanner hits |
| FU01-S02 | `обеспечение доступа к платам` | Access phrasing without `обеспеч*` |
| FU01-S03 | `контролируются параметры` | `параметры фиксируются` (or equiv.); no `контрол*` |
| FU01-S04 | `параметры контролируются` | Same |
| FU01-S05 | `контроль качества` | `проверка результата` |
| FU01-S06 | `параметры контроля` | `проверяемые параметры` |
| FU01-S07 | `метод контроля` | `метод проверки` |
| FU01-S08 | `специализированные инструменты` | `инструменты для измерений` |
| FU01-S09 | `специализированное оборудование` | `оборудование для проверки` |
| FU01-S10 | `специализированные методы` | `методы проверки` |
| FU01-S11 | `надежность соединений` | `состояние соединений` |
| FU01-S12 | `надёжность работы` | `параметры работы` (`ё` covered) |
| FU01-S13 | Combined: `Для обеспечения безопасности перед работами выполняется контроль качества, используются специализированные инструменты, проверяется надежность соединений.` | All five families neutralized; readable Russian; technical meaning preserved; `strict_risk_scan.count=0` when no other markers |

### 15.2 PC-14 R1 non-regression

| ID | Input | Expect |
|----|-------|--------|
| FU01-R01 | `аккуратное снятие деталей` | Still cleaned (PC-14 R1) |
| FU01-R02 | `для удобства восприятия` | Still cleaned / neutralized |
| FU01-R03 | `что позволяет определить` | Still cleaned / neutralized |
| FU01-R04 | Combined: `Аккуратное описание для удобства восприятия позволяет определить порядок проверки.` | All three R1 families cleaned; scan 0 for those families |

### 15.3 Clean text unchanged

| ID | Input | Expect |
|----|-------|--------|
| FU01-C01 | `Диагностика включает проверку давления, температуры и состояния электрических цепей.` | Unchanged (or harmless whitespace only); scan 0 |
| FU01-C02 | `После сборки фиксируются параметры работы устройства.` | Unchanged; scan 0 |
| FU01-C03 | `Разборка выполняется после отключения устройства от сети.` | Unchanged; scan 0 |

### 15.4 Banner tests (formatter untouched)

| ID | Scenario | Expect |
|----|----------|--------|
| FU01-B01 | Forced residual strict marker after cleanup | `STRICT QA REJECT` still appears via existing `Format Run Pipeline` |
| FU01-B02 | FU-01 markers removed + SEO QA approved | No banner |
| FU01-B03 | Banner logic diff | **Empty** — formatter not modified |

### 15.5 PC-07 guard

| ID | Check | Expect |
|----|-------|--------|
| FU01-G01 | `Close Lock Before Sending` mapping | Unchanged: `={{ $('Route Command').first().json.task_id }}` |
| FU01-G02 | Diff scope | Only `Strict Cleanup` (+ harness/evidence files); no lock/memory/`/get` nodes |
| FU01-G03 | Active job close semantics | Real `task_id`, not `pending` (verified on later production smoke, not this proposal) |

---

## 16. Sandbox Evidence Requirements

Future sandbox implementation task must produce:

| # | Artifact |
|---|----------|
| 1 | Safe sandbox clone of production Worker (name/webhook as §14) |
| 2 | Before/after **sanitized** workflow exports |
| 3 | jsCode-only / node-scope diff proving **only** `Strict Cleanup` changed |
| 4 | Local harness results (Cleanup → Scanner → optional Format for banner checks) |
| 5 | Evidence directory: `projects/metabot-seo-content-agent/exports/sandbox-pc14-fu01/2026-07-10/` |
| 6 | Report: `projects/metabot-seo-content-agent/reports/REPORT-metabot-seo-agent-v14-pc14-fu01-sandbox-patch-implementation.md` |
| 7 | Side-effect nodes disabled/bypassed in sandbox |
| 8 | Production Worker `updatedAt` / identity unchanged |
| 9 | No stage/commit unless separately requested |

**Harness classification:** `SANDBOX_PATCH_APPLIED_HARNESS_LOCAL` (same family as PC-14).

---

## 17. Production Gate Requirements

Do **not** open production proposal/apply until **all** are true:

| Gate | Requirement |
|------|-------------|
| Sandbox evidence | Exists under `exports/sandbox-pc14-fu01/...` |
| FU-01 positive tests | Pass (§15.1) |
| PC-14 R1 non-regression | Pass (§15.2) |
| Clean text tests | Pass (§15.3) |
| Banner tests | Pass without formatter changes (§15.4) |
| PC-07 guard | Mapping + diff scope verified (§15.5) |
| Diff scope | Only `Strict Cleanup` |
| Fresh production export | Exists and sanitized for proposal baseline |
| Raw rollback export | Exists under `local/` (not committed) |
| Operator approval | Explicit |

**Rollback requirements (for future apply wave):**

- Keep pre-patch raw Worker export under `local/`.  
- Keep sanitized before/after in repo evidence.  
- Rollback = restore `Strict Cleanup` jsCode to `v14-strict-cleanup-pc14-r1` only.  
- Do not rollback PC-07 lock mapping or PC-14 formatter as part of FU-01 failure.

---

## 18. Risk Classification

| Path | Risk | When |
|------|------|------|
| FU-01 sandbox/prod: `Strict Cleanup` + local harness only | **R1** (recommended) | Default |
| Touch prompts / `Format Run Pipeline` / SEO QA / generation | **R2** | Split out — do not fold into FU-01 |
| Broad `обеспечивает*` sentence rewrite / prompt supplement | **FU-01B R2** | If R1 phrases leave irreducible verbs |
| Multi-node central lexicon / delivery hard-block | **R3** | **Prohibited** |

**Recommendation:** Keep FU-01 as **R1**. Split unsafe grammar cases into **FU-01B** or later **FU-02** (TZ residuals), not into this sandbox patch.

**Go / no-go for this proposal:**

| Criterion | Result |
|-----------|--------|
| Replacement maps concrete enough for sandbox coding | **GO** |
| Scanner bug requiring scanner patch | **NO** — not found |
| Formatter change required | **NO** |
| Verb blanket map ready without grammar risk | **NO** — deferred FU-01B |
| Proposal apply now | **NO-GO** — proposal only |

---

## 19. Recommended Next Step

| Field | Value |
|-------|-------|
| **Next task** | PC14-FU-01 **sandbox implementation** — clone + patch `Strict Cleanup` only + harness |
| **Next-step label** | `PC14_FU01_READY_FOR_SANDBOX_IMPLEMENTATION` |
| **Why not copy-review block** | Phrase maps are operator-chartered and concrete; residual wording can iterate in harness |
| **Why not split now** | R1 phrase-first path covers smoke markers; verb residuals explicitly deferred |
| **Do not** | Patch production; touch formatter/scanner/locks; force `обеспечивает*` one-token swaps |

---

## 20. Files Created

| File | Action |
|------|--------|
| `projects/metabot-seo-content-agent/reports/REPORT-metabot-seo-agent-v14-pc14-fu01-sandbox-patch-proposal.md` | **Created** (this report) |

No existing docs modified. No staging. No commit. No push. No workflow / sandbox / production mutation.

---

## 21. Git Status

- **Branch:** `mars/canonical-post-recovery`
- **HEAD:** `459b7254` — `docs(metabot): add pc14 fu01 strict family proposal`
- **Ahead of origin:** local MetaBOT docs commits unpushed (no push authorized)
- **Staged:** empty
- **This task:** one new untracked report under `projects/metabot-seo-content-agent/reports/`
- **Foreign WIP:** preserved (Website Factory, OCPilot, fp-0002, `.recovery-temp/`, etc.) — **OUT_OF_SCOPE_PRESERVED**
- **Commit / push / pull / clean / reset / stash / restore:** not performed

---

## 22. SAFE UNKNOWN

| Item | Status |
|------|--------|
| Exact live n8n graph drift since smoke `3342` / `updatedAt` `2026-07-10T14:58:37.818Z` | **SAFE UNKNOWN** (no live GET this session) |
| Exact full-sentence contexts of all 8 smoke markers | **SAFE UNKNOWN** — markers/labels only in committed evidence |
| Whether Text Repair introduced vs preserved FU-01 markers on `3342` | **SAFE UNKNOWN** |
| Optimal default for every residual `обеспечивает` / bare `безопасности` without niche | **SAFE UNKNOWN** — deferred to FU-01B / harness copy iteration |
| Whether production `Strict Cleanup` changed after smoke | **SAFE UNKNOWN** without fresh live export before implement |
| Final sandbox workflow ID | **SAFE UNKNOWN** until clone is created |

---

## 23. Final Status

**`COMPLETE — PC14-FU-01 sandbox patch proposal completed`**

| Item | Status |
|------|--------|
| PC14-FU-01 sandbox patch proposal | Complete |
| Next-step label | `PC14_FU01_READY_FOR_SANDBOX_IMPLEMENTATION` |
| PC-14 | `PC14_PRODUCTION_APPLIED_VERIFIED_WITH_FOLLOWUP_STRICT_BACKLOG` (unchanged) |
| PC-07 | `PC07_PRODUCTION_APPLIED_VERIFIED` (unchanged) |
| PC-01 | `PC01_MONITOR_NO_PATCH` (unchanged) |
| Future patch risk | **R1** (`Strict Cleanup` + harness) |
| Split reserve | FU-01B R2 for `обеспечивает*` grammar-hard verbs |

---

Awaiting operator review.
