# Chat-Local vs MARS Capability Boundary v1

## Core principle

**A chat once did it ≠ MARS can reliably do it.**

---

## What a strong Web-GPT chat can do (evidence: Triumph outcomes)

From repository outcomes attributable to chat-era work (chat itself **not in repo**):

- Design search-intent architecture from business context
- Articulate doctrine (`generation-logic-v0.md`)
- Propose tier S/A route segmentation (`intent-groups-v1.md`)
- Structure JSON campaign instances with commercial judgment
- Iterate exporter fixes across versions (documented in battle lessons)

These require **general PPC expertise + project context in the chat window**.

---

## What is lost when the chat ends

| Lost | Triumph mitigation in MARS |
|------|---------------------------|
| Tacit phrase rejection reasoning | Partially frozen in JSON + SE rules — **not complete** |
| Session-local tradeoff decisions | Freeze docs + lessons learned |
| Unwritten operator preferences | **SAFE UNKNOWN** unless captured |
| Step sequence discipline | Reproduction steps in stable state |

---

## What is NOT automatically available to Cursor

- Chat history from Triumph build sessions
- Operator's unstored Wordstat sessions (if any)
- Commercial judgment without reading frozen artifacts
- Implicit "obvious reject" patterns not encoded in rules

Cursor can **read** frozen JSON, run validation-cli, run contract validator — **cannot inherit chat judgment**.

---

## What is NOT automatically available to ORCA scripts

| Script | Reads | Does not read |
|--------|-------|---------------|
| `run-clean-room-semantic-pipeline-v1.mjs` | MIG Wordstat, service scope regex | Campaign contract, P0-C, Triumph laws |
| `validate-campaign-production-contract.mjs` | Contract JSON, production datasets | **Not invoked** by clean-room semantic pipeline |
| Triumph `validation-cli` | Triumph JSON schema rules | Corvonero phrases |

---

## What must be captured as contract

- Authority order (operator > scope > architecture > evidence > rules > classifier)
- Invariants: scope, seeds, HOLD, semantics, negatives order
- ABSTAIN and commercial evidence requirements
- Export ≠ launch; technical PASS ≠ commercial PASS

**Status:** Captured in `ORCA-CAMPAIGN-PRODUCTION-CONTRACT-v1.md` (uncommitted) — **capture done; consumption missing**.

---

## What must be integrated into workflow

1. Contract validator **before** semantic admission batch accept (or per-phrase record gate)
2. Architecture freeze **before** bulk Wordstat expansion
3. Protected operator seeds registry **before** classifier EXCLUDE
4. P0-C decision semantics in admission script (or human annotation loop)

---

## What must be enforced by validators

- INV-SEM-01 informational block
- INV-SEED-01 protected seeds
- INV-SCOPE-01 service disappearance blocks export
- Commercial evidence fields on ACCEPT (P0-B schema)

**Current:** Triumph export path partial; Corvonero semantic path **none**.

---

## What still requires human judgement

- Operator semantic sign-off on ambiguous phrases (P0-C)
- Launch approval
- Controlled test charter per phrase
- Final Commander dry-run

---

## Anti-pattern statement (mandatory)

Future claims must **not** state:

> "ORCA can build campaigns like Triumph because a Web-GPT chat once did."

Valid claim:

> "ORCA can reproduce Triumph **export** when operator supplies frozen JSON, runs validation-cli, cross-negatives, and human Commander review — documented in battle stable state."

Valid claim:

> "ORCA **cannot** yet reproduce Triumph **semantic admission** for a new corpus without integrating P0-C + contract + architecture freeze."
