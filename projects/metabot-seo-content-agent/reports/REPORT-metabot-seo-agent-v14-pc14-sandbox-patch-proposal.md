# REPORT — MetaBOT SEO Agent v14 PC-14 Sandbox Patch Proposal

**Task:** PC-14 — Strict Cleanup Alignment + Reject Banner (proposal-only)  
**Classification:** Sandbox-first patch proposal · no live n8n mutation  
**Date:** 2026-07-10  
**Lane:** MetaBOT SEO Content Agent (`@seo_content_agent_bot`) — Intake / Worker / Admin  
**Checkpoint anchors:** `6263815c`, `1b954990`, `84dd9b07`, `af6fc35d`, `61bb6019`, `58c8f0b7`, `bc222072`, `46fc6335`, `c1915bc8`, `6704b174`, `6efd6afa`, `e3dc9ef7`, `e36ce56e`, `7e1c50ca`, `335b7f3c`, `688e1c03`  
**PC-07 status preserved:** `PC07_PRODUCTION_APPLIED_VERIFIED`  
**PC-01 status preserved:** `PC01_MONITOR_NO_PATCH`  
**Production baseline:** `SEO Content Agent Beta.v14 - Worker` (`p4mqb4VuPcemIDlC`) — **untouched**

---

## 1. Executive Summary

This report proposes a **staged R1 sandbox patch** for two Worker nodes only:

1. **`Strict Cleanup`** — align deterministic replacement lexicon and morphology with **`Strict Risk Scanner`**, using Unicode-aware Cyrillic boundaries instead of ASCII `\b`.
2. **`Format Run Pipeline`** — prepend a prominent **reject warning banner** when `seoqa.verdict === 'reject'` or `strict_risk_scan.count > 0`, while **keeping full text delivery** for operator continuity.

**Evidence basis:** PC-14 audit (`688e1c03`) and sanitized production Worker export (`exports/live-v14-evidence/2026-07-10/SEO-Content-Agent-Beta-v14-Worker.sanitized.json`). PC-07 smoke task `seo20260710103247agk8ki` showed markers `аккуратное`, `удобства`, `позволяет` surviving cleanup but triggering scanner + SEO QA `reject`.

**Risk level:** **R1** (two-node, deterministic, sandbox-first, reversible).

**PC-14 decision:** **`PC14_READY_FOR_SANDBOX_PATCH`**

**Task status:** **`COMPLETE — PC-14 sandbox patch proposal completed`**

---

## 2. Preflight

| Check | Result |
|-------|--------|
| Working directory | `X:\AI MARS` — **PASS** |
| Volume `X:` label | `AI WS` — **PASS** |
| Git branch | `mars/canonical-post-recovery` — **PASS** |
| Staged changes | Empty — **PASS** |
| HEAD | `688e1c03949b4a9f81892ef82f7b174e72dcf0e1` — **PASS** |
| Checkpoint `6263815c` | `6263815ce53a5570df864c21dd2dd713a9e4eaab` — **PASS** |
| Checkpoint `1b954990` | `1b9549900350e2e3e3e2ec26705737588132bffc` — **PASS** |
| Checkpoint `84dd9b07` | `84dd9b07c71c51dff75f293056c9846c3ade0e88` — **PASS** |
| Checkpoint `af6fc35d` | `af6fc35d65c019957c02127a518d8a748fcd6d92` — **PASS** |
| Checkpoint `61bb6019` | `61bb601944699109c5af918fb1b34319ca2f1820` — **PASS** |
| Checkpoint `58c8f0b7` | `58c8f0b7301378c0309dc005b79cf2408b43d982` — **PASS** |
| Checkpoint `bc222072` | `bc222072c69d7bf4e577fdca6100d2527343ea2d` — **PASS** |
| Checkpoint `46fc6335` | `46fc6335ef15cda26addb195b3fe49d66babaca8` — **PASS** |
| Checkpoint `c1915bc8` | `c1915bc8f0bcd0464cf655be2c4cc265ffb1a894` — **PASS** |
| Checkpoint `6704b174` | `6704b174c1e846739d001ad0e9eff8dc5bcb2d09` — **PASS** |
| Checkpoint `6efd6afa` | `6efd6afa626c48670e38bfa6c17e572ae80cfcb2` — **PASS** |
| Checkpoint `e3dc9ef7` | `e3dc9ef72f2a55c76879bcf945c09dfafd9b91d2` — **PASS** |
| Checkpoint `e36ce56e` | `e36ce56ed2343ec12d53c603d61cd84cd4fd3ebb` — **PASS** |
| Checkpoint `7e1c50ca` | `7e1c50ca047372ec865742b6f6fc676b96a399bc` — **PASS** |
| Checkpoint `335b7f3c` | `335b7f3c2d420b3a02f5aaea300b1b02946e1687` — **PASS** |
| Checkpoint `688e1c03` | `688e1c03949b4a9f81892ef82f7b174e72dcf0e1` — **PASS** |

**Authority docs read:** `AGENTS.md`, `.cursorrules`, `OPERATIONAL-INDEX.md`, `n8n-project-development-rules-v1.md`, `safe-workflow-patch-protocol-v1.md`, `n8n-import-safe-generation-rules-v1.md`, `n8n-workflow-json-grammar-v1.md`, PC-14 audit, issue backlog/test matrix, PC-07 operator smoke verification.

**Evidence exports read:** `SEO-Content-Agent-Beta-v14-Worker.sanitized.json`, `NODE-INVENTORY-v14.md`, `PROMPT-AND-CODE-NODE-INDEX-v14.md`, `RISK-AND-UNKNOWN-REGISTER-v14.md`.

**Live API / Telegram / OpenRouter / Sheets:** not called (proposal-only).

---

## 3. Out-of-Scope Preserved

**OUT_OF_SCOPE_PRESERVED**

| Area | Status |
|------|--------|
| Smart Reporter, I-SEO Report Hub, Website Factory, WordPress report hub | not touched |
| FP-0002, OCPilot workspaces | foreign WIP (`M`) preserved |
| `.recovery-temp/` | preserved (`??`) |
| Live n8n mutation (production or sandbox) | not performed |
| PC-07 reopen | not requested — `PC07_PRODUCTION_APPLIED_VERIFIED` |
| PC-01 | `PC01_MONITOR_NO_PATCH` preserved |
| Git stage / commit / push | not performed |

**Forbidden nodes (no diff in this proposal):** Intake, Admin, OpenRouter HTTP nodes, Telegram send nodes, lock nodes (`Close Lock Before Sending`, `Close Single Lock Before Sending`, `Finish Lock`), `/get` nodes, memory append nodes, credentials, webhooks.

---

## 4. Audit Basis

### 4.1 Root cause (from PC-14 audit)

| Layer | Behavior |
|-------|----------|
| **Strict Cleanup** | Last deterministic text mutation; lexicon **narrower** than scanner; uses `\b` |
| **Strict Risk Scanner** | Always-on on `/run`; Unicode boundaries; fuller morphology; **no text mutation** |
| **SEO QA** | Caps to `reject` when `strict_risk_scan.count > 0` |
| **Format Run Pipeline** | **Always** embeds full `content_markdown` in `=== 2. SEO Текст ===` regardless of verdict |

### 4.2 Smoke marker gap matrix

| Marker | Strict Cleanup (current) | Strict Risk Scanner | Gap |
|--------|--------------------------|---------------------|-----|
| `аккуратное` | Only `аккуратно` → `с учётом требований` | `аккуратн(ый\|ая\|ое\|…)` | Adjective/neuter forms missing |
| `удобства` | **Not in map** | `удобств(о\|а\|у\|ом)` + `удобн(ый\|…)` | Entire family missing |
| `позволяет` | `\bпозволяет\b` + 3 phrase rules; fallback `даёт возможность` | `позволя(ет\|ют\|ющий\|…\|ть)` + Unicode boundaries | `\b` unreliable for Cyrillic; morphology incomplete; fallback still soft-promise |

### 4.3 Current node versions (export evidence)

| Node | Version string in export |
|------|--------------------------|
| Strict Cleanup | `v13-strict-cleanup-after-text-repair` |
| Strict Risk Scanner | `v13-run-strict-risk-scanner-hard-v4` |
| Format Run Pipeline | (no version field; ~11755 chars jsCode) |

---

## 5. Proposed Patch Scope

| Field | Value |
|-------|-------|
| **Target workflow** | Sandbox clone only: `SEO Content Agent Beta.v14 - Worker.sandbox-pc14` |
| **Production workflow** | `SEO Content Agent Beta.v14 - Worker` (`p4mqb4VuPcemIDlC`) — **no change** |
| **Nodes to patch** | `Strict Cleanup`, `Format Run Pipeline` |
| **Patch stage** | R1 — deterministic alignment + formatter warning |
| **Risk** | R1 |
| **IB/TQ mapping** | IB-10 (repair regression guard via TQ-05), IB-11 (partial lexicon parity for 3 families), TQ-01, TQ-05 |

---

## 6. Strict Cleanup Patch Design

### 6.1 What changes

| Aspect | Current | Proposed R1 |
|--------|---------|-------------|
| Boundary style | ASCII `\b` on most rules | Unicode letter/digit boundaries matching scanner: `(^|[^\p{L}\p{N}_])…(?=$|[^\p{L}\p{N}_])` with prefix capture |
| `аккуратн*` | `аккуратно` only | Full adjective morphology + adverb |
| `удобств*` / `удобн*` | absent | Noun + adjective morphology |
| `позволя*` | partial `\bпозволяет\b`; fallback `даёт возможность` | Full morphology; structural rewrites; **remove** `даёт возможность` fallback |
| Version bump | `v13-strict-cleanup-after-text-repair` | `v14-strict-cleanup-pc14-r1` |
| Metadata | `strict_cleanup.applied` boolean | Add `strict_cleanup.replacements_count`, `strict_cleanup.families_patched: ['аккуратн','удобств','позволя']` |

### 6.2 Fields read / written

| Direction | Field |
|-----------|-------|
| **Reads** | `$json`, `$json.generated_text.content_markdown`, `$json.generated_text` (spread) |
| **Writes** | `generated_text.content_markdown` (mutated), `strict_cleanup` object |
| **Does not write** | `strict_risk_scan`, `seoqa`, `telegram_text`, lock fields, memory fields |

### 6.3 Boundary strategy (n8n Code node / Node.js)

**Recommended:** capture-boundary replacement (no lookbehind dependency).

```javascript
// Proposed helper — prefix-preserving Unicode boundary replace
const BOUNDARY_PREFIX = '(^|[^\\p{L}\\p{N}_])';
const BOUNDARY_SUFFIX = '(?=$|[^\\p{L}\\p{N}_])';

function replaceBounded(text, innerPattern, replacement) {
  const re = new RegExp(`${BOUNDARY_PREFIX}(${innerPattern})${BOUNDARY_SUFFIX}`, 'giu');
  return text.replace(re, (full, prefix, word) => {
    const next = typeof replacement === 'function' ? replacement(word) : replacement;
    return `${prefix}${next}`;
  });
}
```

**Why not lookbehind `(?<![\p{L}\p{N}_])`:** Node.js 10+ supports it with `u`, but n8n hosted version is **SAFE UNKNOWN** from repo evidence. Capture-boundary pattern is already proven in `Strict Risk Scanner` and is the safest portable choice.

**Do not migrate entire scanner lexicon in R1** — scope is limited to three smoke families plus existing replacements (retain current rules; only extend boundary style for new/edited rules).

### 6.4 Marker forms to cover

#### Family `аккуратн*`

| Form | Replacement strategy |
|------|---------------------|
| аккуратный, аккуратная, аккуратное, аккуратные | Morphology-matched `внимательный` / `внимательная` / `внимательное` / `внимательные` |
| аккуратного, аккуратной, аккуратным, аккуратных, аккуратными, аккуратную | Same stem map by ending |
| аккуратно | `внимательно` |
| Phrase: `аккуратное снятие` | → `внимательное снятие` (via adjective rule) |

**Inner pattern (aligned with scanner):** `аккуратн(ый|ая|ое|ые|ого|ых|ому|ыми|о|ой|ую)`

#### Family `удобств*` / `удобн*`

| Form | Replacement strategy |
|------|---------------------|
| удобство, удобства, удобству, удобством | Context phrase first: `для удобства` → `для наглядности`; bare noun → `условие` / `условия` / `порядок` by case ending |
| удобный, удобная, удобное, удобные (+ cases) | → `подходящий` forms or `нейтральный` forms by ending |
| удобно | → `наглядно` or `в таком формате` |

**Inner patterns (aligned with scanner):**

- `удобств(о|а|у|ом)`
- `удобн(ый|ая|ое|ые|ого|ых|ому|ыми|о)`

#### Family `позволя*`

| Form | Replacement strategy |
|------|---------------------|
| позволяет оценить / проверить / уточнить | Keep phrase-specific: `используется для оценки` etc. (existing) |
| позволяет (generic) | `при этом возможно` or `за счёт этого можно` — pick by following infinitive if present |
| позволяют | `при этом возможно` |
| позволить | `выполнить` / neutral infinitive rewrite |
| позволяющий/ая/ее/ие/их | → `связанный с возможностью` or delete participial clause if safe |

**Inner pattern (aligned with scanner):** `позволя(ет|ют|ющий|ющая|ющее|ющие|ющих|ть)`

**Remove:** `{ re: /\bпозволяет\b/giu, to: 'даёт возможность' }` — still implies benefit.

### 6.5 Proposed patch text (Strict Cleanup — insert/change block only)

Add near top of `cleanText()` after `let text = …`:

```javascript
// --- PC-14 R1: Unicode-boundary helpers ---
const BP = '(^|[^\\p{L}\\p{N}_])';
const BS = '(?=$|[^\\p{L}\\p{N}_])';
function rb(text, inner, to) {
  const re = new RegExp(`${BP}(${inner})${BS}`, 'giu');
  return text.replace(re, (m, p, w) => `${p}${typeof to === 'function' ? to(w) : to}`);
}

const ACC_MAP = {
  'ый':'внимательный','ая':'внимательная','ое':'внимательное','ые':'внимательные',
  'ого':'внимательного','ой':'внимательной','ому':'внимательному','ым':'внимательным',
  'ых':'внимательных','ыми':'внимательными','ую':'внимательную','о':'внимательно'
};
function mapAcc(word) {
  const m = String(word).match(/^аккуратн(.+)$/i);
  if (!m) return word;
  if (m[1] === 'о' && /^аккуратно$/i.test(word)) return 'внимательно';
  return 'внимательн' + (ACC_MAP[m[1].toLowerCase()] ? m[1].replace(/^(.+)$/, (_, e) => ACC_MAP[e.toLowerCase()].replace(/^внимательн/, '') || m[1]) : 'ый');
}
// Simpler production-safe approach: explicit replacements array using rb():
```

**Practical R1 replacement entries to add/replace in `replacements` array** (apply **before** generic `\b` rules; use `rb` or inline RegExp):

```javascript
// Phrase-first (удобство)
{ fn: t => rb(t, 'для\\s+удобств(а|о)', 'для наглядности') },
{ fn: t => rb(t, 'удобств(о|а|у|ом)', m => ({'о':'условие','а':'условия','у':'условию','ом':'условием'}[m] || 'условие')) },
{ fn: t => rb(t, 'удобн(ый|ая|ое|ые|ого|ых|ому|ыми|о)', /* map to подходящ-* */) },

// аккуратн* — replace existing аккуратно-only rule
{ fn: t => rb(t, 'аккуратн(ый|ая|ое|ые|ого|ых|ому|ыми|о|ой|ую)', w => /* morphology table */) },
{ fn: t => rb(t, 'аккуратно', 'внимательно') },

// позволя* — extend existing phrase rules; replace generic fallback
{ fn: t => rb(t, 'позволя(ет|ют|ющий|ющая|ющее|ющие|ющих|ть)', w => /* structural rewrite table */) },
```

**Post-pass:** retain existing whitespace/punctuation normalizer block unchanged.

### 6.6 Avoiding breakage on clean text

| Guard | Implementation |
|-------|----------------|
| Word boundaries | Unicode boundaries prevent partial matches inside longer tokens |
| Phrase-first ordering | Longer phrase rules before single-word rules |
| No broad stem deletion | Replace with neutral words, not empty string (except pre-existing empty-to rules) |
| Preserve markdown | Do not run cleanup on code fences / table pipes differently — current node operates on full markdown; **no change** to that scope in R1 |
| Regression control | PC14-T05 clean control; grep for false positives |

---

## 7. Format Run Pipeline Banner Design

### 7.1 What changes

Insert a **reject warning block** at the top of the formatted output when:

```javascript
const strictRiskScan = $json.strict_risk_scan || {};
const showRejectBanner =
  String(seoqa.verdict || '').toLowerCase() === 'reject' ||
  Number(strictRiskScan.count || 0) > 0;
```

**Do not hard-block** `=== 2. SEO Текст ===` body in R1.

### 7.2 Insertion point

After the header block:

```text
Task ID: …
SEO Pipeline /run
[Флаги: …]
[Таблицы: …]

<<< INSERT BANNER HERE >>>

=== 1. SEO ТЗ ===
```

In code terms: immediately after `text += \`Таблицы: …\n\n\`;` and **before** `text += '=== 1. SEO ТЗ ===\n\n';`.

### 7.3 Fields read / written

| Direction | Field |
|-----------|-------|
| **Reads** | `seoqa.verdict`, `strict_risk_scan.count`, `strict_risk_scan.violations`, `strict_risk_scan.labels`, `strict_risk_scan.details` |
| **Writes** | `text` (local), then `telegram_text`, `full_output_text` via `splitMessage(text)` |
| **Does not mutate** | `generated_text.content_markdown`, `seoqa`, `strict_risk_scan`, lock fields |

### 7.4 Banner text (text-only — no emoji; matches operator clarity preference)

```text
STRICT QA REJECT
Материал отправлен для проверки, но не готов к публикации.
Причина: обнаружены strict-маркеры: {marker_list}
Перед использованием текст нужно очистить или перегенерировать.

```

`{marker_list}` source priority:

1. `strict_risk_scan.violations` (deduped, lowercased)
2. fallback: `strict_risk_scan.labels`
3. cap display at 12 items; append `…` if more

If `strict_risk_scan.count === 0` but `seoqa.verdict === 'reject'`, banner still shows with:

`Причина: SEO QA verdict reject (см. блок SEO QA ниже).`

### 7.5 Proposed patch text (Format Run Pipeline)

```javascript
const strictRiskScan = $json.strict_risk_scan || {};

// ... existing header build through tables policy line ...

if (
  String(seoqa.verdict || '').toLowerCase() === 'reject' ||
  Number(strictRiskScan.count || 0) > 0
) {
  const markerList = uniqueStrings([
    ...arr(strictRiskScan.violations),
    ...arr(strictRiskScan.labels)
  ]).slice(0, 12);

  const reasonLine = markerList.length
    ? `Причина: обнаружены strict-маркеры: ${markerList.join(', ')}`
    : 'Причина: SEO QA verdict reject (см. блок SEO QA ниже).';

  text += [
    'STRICT QA REJECT',
    'Материал отправлен для проверки, но не готов к публикации.',
    reasonLine,
    'Перед использованием текст нужно очистить или перегенерировать.',
    ''
  ].join('\n');
}

// ... continue with === 1. SEO ТЗ === ...
```

### 7.6 Downstream effects

| Surface | Effect |
|---------|--------|
| **Telegram chunks** | Banner appears in part 1 (top of `text`); chunk splitter unchanged |
| **Memory (`Prepare Memory Row Run`)** | Stores `full_output_text` — **banner will be in memory** (consistent with operator visibility) |
| **`/get` retrieval** | Returns stored output — **banner visible on `/get`** for patched runs |
| **FINAL STRICT GATE (`strict=true`)** | Unchanged — still runs before banner; banner is additive |

---

## 8. Sandbox Workflow Proposal

### 8.1 Clone strategy

| Field | Value |
|-------|-------|
| **Action** | Create **new** sandbox clone from production Worker export (do not patch `Worker.sandbox-pc07` — PC-07 lock test artifact) |
| **Name** | `SEO Content Agent Beta.v14 - Worker.sandbox-pc14` |
| **Webhook path** | `seo-content-agent-worker-sandbox-pc14` |
| **Activation** | **Inactive** by default; activate only for chartered webhook tests |
| **Baseline export** | `exports/sandbox-pc14/2026-07-10/SEO-Content-Agent-Beta-v14-Worker.sandbox-pc14.before-patch.sanitized.json` |

### 8.2 Suppression for safe testing

| Component | Sandbox handling |
|-----------|------------------|
| **OpenRouter HTTP nodes** | Prefer **harness injection** — bypass LLM chain; inject mock `generated_text` at `Strict Cleanup` input |
| **Telegram send** | Disable `Send Telegram Run` OR replace with Code node `Sandbox Capture Output` writing to execution log |
| **Google Sheets lock/memory** | Use PC-07 pattern: synthetic `lock_key` prefix `sandbox-pc14:` only if full-path test required; **harness tests avoid Sheets** |
| **Production webhook** | Never point Intake to sandbox path without operator charter |

### 8.3 Harness-first test path (preferred)

```
Manual Trigger / Webhook (sandbox)
  → Inject Mock Run Item (code)
  → Strict Cleanup
  → Strict Risk Scanner
  → Inject Mock SEOQA (code, optional)
  → Format Run Pipeline
  → Sandbox Capture Output (code)
```

**Mock item minimum fields:**

```json
{
  "task_id": "sandbox-pc14-T01",
  "outline_only": false,
  "text_only": false,
  "generated_text": { "content_markdown": "…", "h1": "Тест" },
  "seoqa": { "verdict": "reject", "score": 70, "summary": "test" },
  "strict_risk_scan": { "count": 1, "violations": ["аккуратное"], "labels": ["аккуратный"] },
  "outline": { "h1": "Тест" },
  "flags": {}
}
```

### 8.4 Evidence artifacts (future sandbox apply task)

| Artifact | Path |
|----------|------|
| Before-patch sanitized export | `exports/sandbox-pc14/2026-07-10/*.before-patch.sanitized.json` |
| After-patch sanitized export | `exports/sandbox-pc14/2026-07-10/*.after-patch.sanitized.json` |
| Node diff JSON | `exports/sandbox-pc14/2026-07-10/pc14-strict-cleanup-format-diff.json` |
| Harness results | `exports/sandbox-pc14/2026-07-10/pc14-harness-results.json` |

---

## 9. Sandbox Test Plan PC14-T01–T08

### PC14-T01 — аккуратное marker cleanup

| Field | Value |
|-------|-------|
| **Input** | `аккуратное снятие деталей` in `generated_text.content_markdown` |
| **Nodes executed** | Inject → Strict Cleanup → Strict Risk Scanner |
| **Expected text** | No `аккуратное`; neutral phrase e.g. `внимательное снятие деталей` |
| **Expected strict scan** | `count = 0`; no `аккуратн` label |
| **Expected QA** | Not `reject` due to scan (mock QA may be `approved`) |
| **Expected banner** | N/A (scanner clean) |
| **Pass** | No `аккуратн` grep in post-cleanup text; scanner `count=0` |

### PC14-T02 — удобства marker cleanup

| Field | Value |
|-------|-------|
| **Input** | `для удобства восприятия` |
| **Nodes** | Inject → Strict Cleanup → Strict Risk Scanner |
| **Expected text** | No `удобства`/`удобство`; e.g. `для наглядности восприятия` |
| **Expected strict scan** | `count = 0` |
| **Pass** | No `удобств` / `удобн` hits |

### PC14-T03 — позволяет marker cleanup

| Field | Value |
|-------|-------|
| **Input** | `что позволяет определить состояние` |
| **Nodes** | Inject → Strict Cleanup → Strict Risk Scanner |
| **Expected text** | No `позволяет`; structural rewrite e.g. `при этом возможно определить состояние` |
| **Expected strict scan** | `count = 0` |
| **Pass** | No `позволя` substring |

### PC14-T04 — combined smoke regression

| Field | Value |
|-------|-------|
| **Input** | Excerpt from PC-07 smoke containing all three markers (operator-redacted sample or reconstructed brief output) |
| **Nodes** | Full harness through Strict Cleanup → Strict Risk Scanner → mock SEO QA |
| **Expected** | All three families neutralized; `strict_risk_scan.count = 0` if no other markers |
| **Expected QA** | Not `reject` from scan cap alone |
| **Pass** | Zero scanner hits for three families; compare to baseline `seo20260710103247agk8ki` behavior |

### PC14-T05 — clean control

| Field | Value |
|-------|-------|
| **Input** | Neutral service copy with no strict markers (200–400 words) |
| **Nodes** | Strict Cleanup → Strict Risk Scanner |
| **Expected** | Output identical or materially unchanged (allow whitespace normalizer only) |
| **Expected strict scan** | `count = 0` |
| **Expected banner** | No |
| **Pass** | No new banned tokens; Levenshtein ratio > 0.98 or byte-equal after normalize |

### PC14-T06 — reject banner if strict remains

| Field | Value |
|-------|-------|
| **Input** | Text with `гибкость` (scanner label `гибкость` — **not** in cleanup R1 map) |
| **Nodes** | Inject (skip cleanup or post-cleanup with marker) → Strict Risk Scanner → Format Run Pipeline |
| **Expected scan** | `count >= 1` |
| **Expected QA** | `reject` (mock or real) |
| **Expected banner** | **Present** at top; lists `гибкость` or label |
| **Expected delivery** | Full text still present in sandbox capture |
| **Pass** | Banner present; no workflow crash; `=== 2. SEO Текст ===` still populated |

### PC14-T07 — no banner on approved clean text

| Field | Value |
|-------|-------|
| **Input** | Clean text; `seoqa.verdict = approved`; `strict_risk_scan.count = 0` |
| **Nodes** | Format Run Pipeline |
| **Expected banner** | **Absent** |
| **Expected format** | Normal sections unchanged |
| **Pass** | `STRICT QA REJECT` not in output |

### PC14-T08 — PC-07 lock regression guard

| Field | Value |
|-------|-------|
| **Input** | N/A — diff review |
| **Nodes** | Compare sandbox patch diff vs production |
| **Expected** | **Zero** changes to `Close Lock Before Sending`, `Close Single Lock Before Sending`, `Finish Lock` |
| **Pass** | Node diff contains only `Strict Cleanup` + `Format Run Pipeline` |

---

## 10. Risk Analysis

| Risk | Level | Mitigation |
|------|-------|------------|
| Deterministic replacement awkward grammar | Medium | Phrase-first rules; morphology tables; PC14-T01–T03 human review |
| Unicode regex runtime incompatibility | Low–Medium | Use capture-boundary pattern already in scanner; test in sandbox Code node first |
| Accidental over-replacement | Medium | Unicode boundaries; PC14-T05 clean control |
| False negatives (markers remain) | Medium | Post-cleanup scanner gate; PC14-T04 smoke regression |
| False positives (clean words hit) | Low | Narrow families; no single-letter stems |
| Banner overuse | Low | Condition requires `reject` OR `count > 0`; PC14-T07 |
| Memory / `/get` banner persistence | Low (accepted) | Documented — intentional operator visibility |
| Operator UX confusion | Low | Text-only banner; markers listed explicitly |
| Lock / memory regression | Low | PC14-T08 diff guard; no lock node edits |
| Rollback complexity | Low | Two-node revert from before-patch export |
| IB-11 full lexicon drift | Deferred | R1 covers 3 families only — central module out of scope |

**Overall risk level:** **R1**

---

## 11. Acceptance Criteria

Future sandbox patch apply is accepted when:

1. Sandbox clone `Worker.sandbox-pc14` created; production `p4mqb4VuPcemIDlC` untouched.
2. Only `Strict Cleanup` and `Format Run Pipeline` changed.
3. PC14-T01 through PC14-T08 pass.
4. Strict scanner and cleanup cover the same smoke marker families (`аккуратн*`, `удобств*`, `позволя*`).
5. Reject banner appears when strict risk remains or QA reject.
6. No banner on clean approved output (PC14-T07).
7. No production OpenRouter/Telegram calls during harness tests.
8. No lock node diffs (PC14-T08).
9. Sanitized before/after/diff evidence under `exports/sandbox-pc14/`.
10. Operator review report with promotion recommendation.

---

## 12. Rollback Plan

### Sandbox rollback

1. Restore sandbox workflow from `*.before-patch.sanitized.json` via n8n import (operator).
2. Or reverse jsCode in the two nodes only.
3. Deactivate sandbox webhook if activated.

### Production rollback (only if promoted later)

1. Restore pre-patch production Worker export (dated snapshot before PC-14 apply).
2. Or reverse only `Strict Cleanup` + `Format Run Pipeline` jsCode.

### Rollback triggers

- Formatter Code node crash / execution error
- Text empty or corrupted after cleanup
- Banner on clean approved output (PC14-T07 fail)
- Smoke markers remain after cleanup (PC14-T01–T04 fail)
- Unexpected node diffs beyond allowlist
- Lock/memory regression
- Regex runtime errors in n8n execution log

---

## 13. Production Promotion Preconditions

Production apply **not authorized** by this proposal. Preconditions for a separate promotion charter:

| # | Precondition |
|---|--------------|
| 1 | PC14-T01–T08 pass on sandbox |
| 2 | Sanitized diff reviewed; only two nodes changed |
| 3 | Operator sign-off on replacement phrasing (Russian copy QA) |
| 4 | `safe-workflow-patch-protocol-v1.md` Stage 6–8 complete |
| 5 | Fresh production export taken immediately before apply |
| 6 | Post-apply operator smoke (non-destructive brief) |
| 7 | PC-07 lock regression re-check (`Close Lock Before Sending` unchanged) |
| 8 | Rollback export stored and path documented |

---

## 14. Proposed Next Prompt Outline

```markdown
# TASK — MetaBOT SEO Agent PC-14 Sandbox Patch Apply + Harness Verification

Lane: MetaBOT SEO Content Agent only.
Goal: Apply R1 patch to sandbox Worker.sandbox-pc14; run PC14-T01–T08 harness; capture evidence.

Constraints:
- Sandbox only. No production patch without separate promotion charter.
- Follow safe-workflow-patch-protocol-v1.md.
- Touch only Strict Cleanup + Format Run Pipeline.
- No Telegram production sends; no OpenRouter unless harness requires.
- No commit unless requested.

Read:
- REPORT-metabot-seo-agent-v14-pc14-sandbox-patch-proposal.md
- exports/live-v14-evidence/2026-07-10/SEO-Content-Agent-Beta-v14-Worker.sanitized.json

Deliver:
- Sandbox clone + patched export
- exports/sandbox-pc14/2026-07-10/pc14-strict-cleanup-format-diff.json
- exports/sandbox-pc14/2026-07-10/pc14-harness-results.json
- REPORT-metabot-seo-agent-v14-pc14-sandbox-patch-evidence.md

Final status: PC14_SANDBOX_PATCH_APPLIED | PC14_SANDBOX_PATCH_FAILED
```

---

## 15. Files Created

| Path | Action |
|------|--------|
| `projects/metabot-seo-content-agent/reports/REPORT-metabot-seo-agent-v14-pc14-sandbox-patch-proposal.md` | **Created** (this report) |

No existing docs modified. No staging. No commit.

---

## 16. Git Status

- **Branch:** `mars/canonical-post-recovery`
- **HEAD:** `688e1c03949b4a9f81892ef82f7b174e72dcf0e1`
- **Staged:** empty
- **This task:** one new untracked report under `projects/metabot-seo-content-agent/reports/`
- **Foreign WIP:** Website Factory, OCPilot, fp-0002 workspaces, `.recovery-temp/` — **OUT_OF_SCOPE_PRESERVED**
- **Commit / push:** not performed

---

## 17. SAFE UNKNOWN

| Item | Status |
|------|--------|
| Exact n8n host Node.js version (lookbehind support) | **SAFE UNKNOWN** — capture-boundary pattern chosen to avoid dependency |
| Whether `Worker.sandbox-pc07` should be retired before pc14 clone | **Operator decision** — recommend separate fresh clone |
| PC-07 smoke per-node text at Strict Cleanup input | **SAFE UNKNOWN** — no execution `3340` dumps in repo |
| Operator policy: emoji in Telegram warnings | **SAFE UNKNOWN** — proposal uses text-only banner |
| Full IB-11 lexicon parity across all nodes | **Deferred** — R1 limited to 3 smoke families |
| Morphology table correctness for all rare Russian cases | Requires sandbox copy QA (PC14-T01–T03) |

---

## 18. Final Status

| Label | Value |
|-------|-------|
| Task status | **`COMPLETE — PC-14 sandbox patch proposal completed`** |
| PC-07 | `PC07_PRODUCTION_APPLIED_VERIFIED` (unchanged) |
| PC-01 | `PC01_MONITOR_NO_PATCH` (unchanged) |
| PC-14 decision | **`PC14_READY_FOR_SANDBOX_PATCH`** |

Awaiting operator review.
