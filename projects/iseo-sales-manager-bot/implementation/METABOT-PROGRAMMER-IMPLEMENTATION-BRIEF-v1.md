# METABOT PROGRAMMER IMPLEMENTATION BRIEF v1

**Product:** i-SEO Sales Manager Bot  
**Phase:** 3A — documentation package only  
**Grammar authority:** MetaBOT Developer (`n8n-workflow-json-grammar-v1`, `n8n-node-type-catalog-v14`, `n8n-import-safe-generation-rules-v1`, `safe-workflow-patch-protocol-v1`)  
**Status:** implementation-ready **specification** — sanitized Sales Manager JSON baselines **present** (Phase 3A.1); **no** live workflow copies created

---

## 1. Objective

Prepare exact patch specifications so Phase 3B can:

1. read-only audit live Sales-Manager-v2;
2. create at most **one** `i-SEO Sales Manager - Operational.dev` and **one** `i-SEO Sales Manager - Admin.dev`;
3. apply node-level patches using MetaBOT safe patch protocol against **sanitized v2 graph evidence**;
4. create sandbox Sheets tabs only after operator approval;
5. run synthetic fixtures F01–F21.

**Baseline files:** `baselines/Sales-Manager-v2.sanitized.json` (+ v1), node inventory, connection map.

---

## 2. Hard boundaries (Phase 3A)

| Action | Status |
|--------|--------|
| Live n8n access | **FORBIDDEN** |
| Workflow copy creation | **FORBIDDEN** |
| Google Sheets mutation | **FORBIDDEN** |
| Gmail / Telegram mutation | **FORBIDDEN** |
| Implementation JSON generation | **FORBIDDEN** |
| OpenRouter credential discussion | **FORBIDDEN** |
| Foreign WIP touch | **FORBIDDEN** |

---

## 3. Target workflows (exactly two)

| Name | Role |
|------|------|
| `i-SEO Sales Manager - Operational.dev` | Scheduled Gmail → RAW → process → CLEAN → Telegram → labels |
| `i-SEO Sales Manager - Admin.dev` | Telegram admin → auth → commands → CONFIG / health / stats |

**No** Execute Workflow / webhook dependency between them for v1. Shared state = CLEAN workbook tabs only.

---

## 4. Package map

| Spec | Path |
|------|------|
| Operational patch | [OPERATIONAL-WORKFLOW-PATCH-SPEC-v1.md](OPERATIONAL-WORKFLOW-PATCH-SPEC-v1.md) |
| Admin patch | [ADMIN-WORKFLOW-PATCH-SPEC-v1.md](ADMIN-WORKFLOW-PATCH-SPEC-v1.md) |
| Admin source selection | [ADMIN-SOURCE-SELECTION-v1.md](ADMIN-SOURCE-SELECTION-v1.md) |
| Sheets migration | [SHEETS-MIGRATION-SPEC-v1.md](SHEETS-MIGRATION-SPEC-v1.md) |
| Dedupe | [DEDUP-IMPLEMENTATION-SPEC-v1.md](DEDUP-IMPLEMENTATION-SPEC-v1.md) |
| Telegram formatter | [TELEGRAM-FORMATTER-SPEC-v1.md](TELEGRAM-FORMATTER-SPEC-v1.md) |
| Test harness | [TEST-HARNESS-SPEC-v1.md](TEST-HARNESS-SPEC-v1.md) |
| Sandbox apply gate | [SANDBOX-APPLY-GATE-v1.md](SANDBOX-APPLY-GATE-v1.md) |
| AI OFF / ON | Embedded in Operational + Phase 2 `AI-OFF-ON-CONTRACT-v1` (expanded in this package sections) |

Baseline gap: [../baselines/SOURCE-GAP-MANIFEST-v1.md](../baselines/SOURCE-GAP-MANIFEST-v1.md)

---

## 5. MetaBOT Programmer gates (must pass before import)

1. JSON parse.  
2. Node names unique.  
3. Connection targets exist.  
4. Credential refs = placeholders or operator-bound names only (no secret values).  
5. Sandbox: production side-effect nodes disabled or pointed at sandbox IDs.  
6. No live recipient / workbook IDs in committed JSON.  
7. AI OFF path has **no** execution connection to OpenRouter when `ai_enabled=false` (IF skip).  
8. Telegram fail never reaches PROCESSED.  
9. Error path preserves incoming Gmail label per policy.  
10. `same_message` never becomes business `repeat`.  
11. No `structuredClone` in Code nodes.  
12. Deterministic item always forwarded past skipped AI branch.

---

## 6. Enum authority (Phase 2 canonical)

Prefer Phase 2 LEAD-DATA-MODEL / AI-OFF-ON / TELEGRAM-UX over informal aliases:

| Field | Canonical values |
|-------|------------------|
| `quality_status` | `ok` \| `needs_data` \| `poor` \| `unusable` |
| `processing_mode` | `ai_off` \| `ai_on` \| `ai_fallback` |
| `ai_status` | `skipped` \| `ok` \| `fallback` \| `error` |
| `first_reply_source` | `template` \| `ai` \| `ai_fallback_template` |
| `duplicate_status` | `new` \| `reprocessed` \| `repeat` \| `possible` |
| `service` | `Audit` \| `SEO` \| `Direct` \| `Site` \| `Other` |
| `priority` | `low` \| `normal` \| `high` |

UX aliases used in informal briefs (`warning`↔`needs_data`, `bad`↔`unusable`/`poor`, `disabled`↔`skipped`) must **not** be written to Sheets.

---

## 7. Default CONFIG

`ai_enabled=false`. AI OFF path must remain fully operational with **zero** OpenRouter calls.

---

## 8. Next gate

[SANDBOX-APPLY-GATE-v1.md](SANDBOX-APPLY-GATE-v1.md) — Phase 3B only after explicit operator confirmations.

---

*Related: Phase 2 architecture pack · MetaBOT safe-workflow-patch-protocol-v1.*
