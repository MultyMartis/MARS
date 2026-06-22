# REPORT — MARS SEARCH PPC PRODUCTION — WAVE 1.2 LEGACY ENTRY-POINT LOCKDOWN V1

**Date:** 2026-06-23  
**Branch:** `mars/post-cycle8-live-tests`  
**HEAD (working tree):** `4621388` (includes unrelated `feat(mli)` after Wave 1.1 checkpoint)  
**Wave 1.1 checkpoint:** `715402f`  
**Wave 1 checkpoint:** `2b3020d`  
**Lifecycle checkpoint:** `43c4271`  
**Wave 1.2 status:** `IMPLEMENTED — OPERATOR REVIEW REQUIRED` (uncommitted)

---

## 1. Preflight

| Check | Result |
|-------|--------|
| Lifecycle checkpoint `43c4271` | Present in history |
| Wave 1 checkpoint `2b3020d` | Present in history |
| Wave 1.1 checkpoint `715402f` | Committed and pushed this task |
| Wave 1.1 was uncommitted at task start | Confirmed — selective checkpoint created |
| Wave 2 not started | Confirmed — no PAID SERP implementation |
| Corvonero frozen | Confirmed — E2E read-only tests only |
| Unrelated WIP not staged in W1.1 commit | Confirmed — 32 files only |

**Test reruns (all green):**

| Suite | Result |
|-------|--------|
| Synthetic matrix | 20/20 PASS |
| Bypass tests (Wave 1.1) | 15/15 PASS |
| Corvonero E2E | 9/9 PASS |
| Cursor task linter | VALID |
| Lifecycle validator | READY |
| Lockdown tests (Wave 1.2) | 12/12 PASS |

---

## 2. Operator Decisions W1.2-D1–D7

Recorded in:

- [`decisions/WAVE-1.2-OPERATOR-DECISIONS-v1.md`](../decisions/WAVE-1.2-OPERATOR-DECISIONS-v1.md)
- [`decisions/WAVE-1.2-OPERATOR-DECISIONS-v1.json`](../decisions/WAVE-1.2-OPERATOR-DECISIONS-v1.json)

| ID | Decision |
|----|----------|
| W1.2-D1 | Wave 1.1: `APPROVED — IMPLEMENTED AND TESTED` |
| W1.2-D2 | Wave 1: `FINAL LOCKDOWN AUTHORIZED` |
| W1.2-D3 | Wave 2: `BLOCKED UNTIL WAVE 1.2 OPERATOR REVIEW` |
| W1.2-D4 | Legacy CLIs: physical lockdown mandatory |
| W1.2-D5 | Missing components: `MISSING — CORRECTLY BLOCKED` |
| W1.2-D6 | Web-GPT: repository enforcement only; UI unavailable |
| W1.2-D7 | Corvonero: `FROZEN — READ-ONLY ENFORCEMENT TESTS ONLY` |

---

## 3. Wave 1.1 Approval and Checkpoint

**Commit:** `715402f` — `feat(ppc): wire search lifecycle entry points wave 1.1`  
**Pushed:** `origin/mars/post-cycle8-live-tests`

**Included (32 files):** gate API, receipts, subsystem adapters, output classification, artifact-resolver integration, Cursor linter, Web-GPT validator/starter, inventory, bypass/Corvonero tests, Wave 1.1 reports/decisions, gated wrappers, sync pack delta.

**Excluded:** Wave 1.2 lockdown code, Wave 2, Corvonero production artifacts, unrelated WIP.

---

## 4. Legacy Entry-Point Inventory

| Entry point | Path | Lockdown |
|-------------|------|----------|
| MIG direct CLI | `projects/mig/lib/runtime/run-mig-session.js` | PPC-mode detection + fail-closed |
| MIG gated | `projects/mig/tools/run-ppc-gated-session.mjs` | Canonical replacement |
| ORCA admission | `projects/orca/.../cli/orca-admission.mjs` | `integration:run` blocked unless `--diagnostic` or gate env |
| ORCA gated | `projects/orca/.../cli/orca-ppc-gate.mjs` | Canonical replacement |
| Triumph export | `projects/orca/.../exporter-cli/export.js` | Always blocked without gate |
| Sheet1 patch export | `projects/orca/.../sheet1-patch-export.js` | Always blocked without gate |
| Export gated | `projects/orca/.../run-ppc-gated-export.mjs` | Canonical replacement |

Full inventory: [`inventory/search-ppc-entry-point-inventory-v1.json`](../inventory/search-ppc-entry-point-inventory-v1.json) (v1.1.0)

---

## 5. Common Legacy Lockdown Pattern

**Module:** `runtime/src/legacy-entry-boundary.mjs` (+ `.cjs` bridge)

Ungated Search PPC invocation without lifecycle context:

1. Detects Search PPC workflow membership  
2. Refuses production execution  
3. Emits `LEGACY_ENTRY_POINT_REQUIRES_LIFECYCLE_GATE`  
4. Prints canonical gated replacement guidance  
5. Writes blocked execution receipt when possible  
6. Returns exit code `2`  
7. Creates no production output  

**Blocker message:**

```text
BLOCKED — LEGACY SEARCH PPC ENTRY POINT REQUIRES LIFECYCLE GATE
```

**Authorization env:** `MARS_SEARCH_PPC_LIFECYCLE_AUTHORIZED=1` (set only by gated wrappers after gate pass)

---

## 6. MIG Lockdown

- Search PPC CLI blocked when intake carries PPC markers (`mars_search_ppc`, `search_ppc`, manifest refs, etc.)
- Generic MIG module imports (`verify-runtime-mvp-v0.mjs`, `process-inbox.js`) unchanged — no PPC flags
- Gated wrapper sets lifecycle auth env before `runMigSession`
- Migration doc: [`projects/mig/docs/MIG-SEARCH-PPC-LEGACY-MIGRATION-v1.md`](../../mig/docs/MIG-SEARCH-PPC-LEGACY-MIGRATION-v1.md)
- `OPERATIONAL-INDEX.md` updated with gated path reference

---

## 7. ORCA Lockdown

- `contracts:validate`, `contracts:report`, `record:validate` — diagnostic, always allowed
- `integration:run` — blocked without `--diagnostic` or lifecycle authorization
- Diagnostic output wrapped with `output_class: diagnostic`, `may_authorize_downstream: false`
- `orca-ppc-gate.mjs` sets auth env before delegating to admission CLI
- Runtime README updated

---

## 8. Export Lockdown

- `export.js` and `sheet1-patch-export.js` block direct CLI (exit 2)
- Output path guard redirects ungated diagnostic output to quarantine directory
- `run-ppc-gated-export.mjs` sets auth env after export gate authorization
- XLSX generation success does not imply QA approval or launch

---

## 9. Caller and Documentation Migration

| Reference | Classification | Action |
|-----------|----------------|--------|
| `run-ppc-gated-session.mjs` | Active canonical | No change |
| `mig/OPERATIONAL-INDEX.md` | Active canonical | Updated |
| `orca runtime README` | Active canonical | Updated |
| `mig-operational-runtime-architecture-v1.md` | Historical | Not rewritten |
| Archive pilot docs | Historical | Preserved |
| Triumph `package.json` npm scripts | Active legacy | Documented LOCKED in external audit |

---

## 10. Output Path Protection

**Module:** `runtime/src/output-path-guard.mjs`

- Canonical production prefixes guarded (`projects/orca/projects/`, manifest state paths)
- Ungated legacy output redirected to `runtime/quarantine/legacy-output/`
- `rejectArtifactEntry` prevents diagnostic/proposal classes from production authority registration

---

## 11. n8n and External Automation Boundary

Audit: [`reports/EXTERNAL-AUTOMATION-BOUNDARY-AUDIT-v1.md`](EXTERNAL-AUTOMATION-BOUNDARY-AUDIT-v1.md)

- Repository `mars-bridge-workflow.json` — unrelated SEO stub
- No repository-wired Search PPC n8n workflow found
- Remote n8n runtime — **SAFE UNKNOWN** — deployment verification checklist provided

---

## 12. Web-GPT Boundary Finalization

Doc: [`web-gpt/WEB-GPT-BOUNDARY-FINALIZATION-v1.md`](../web-gpt/WEB-GPT-BOUNDARY-FINALIZATION-v1.md)

| Layer | Maturity |
|-------|----------|
| Repository enforcement | `IMPLEMENTED` |
| UI runtime enforcement | `UNAVAILABLE` |

Chat output remains `proposal` until saved, validated, and manifest-registered.

---

## 13. Real Lockdown Tests

**Suite:** `runtime/tests/run-lockdown-tests.mjs`  
**Results:** [`runtime/reports/lockdown-test-results-v1.json`](../runtime/reports/lockdown-test-results-v1.json) — **12/12 PASS**

All 12 required assertions covered: MIG block, MIG frozen block, ORCA diagnostic allow, ORCA production block, Corvonero ORCA block, export block, gated export before QA block, authority quarantine, receipt creation, no canonical mutation, inventory gated path, Web-GPT proposal-only.

---

## 14. Twenty-Path Bypass Re-Audit

Report: [`reports/MARS-SEARCH-PPC-BYPASS-RE-AUDIT-WAVE1-2-v1.md`](MARS-SEARCH-PPC-BYPASS-RE-AUDIT-WAVE1-2-v1.md)

| Disposition | Count |
|-------------|------:|
| CLOSED — EXECUTABLE PROOF | 14 |
| PARTIALLY CLOSED | 2 |
| OPEN | 1 |
| NOT TESTABLE — COMPONENT MISSING | 2 |
| PLATFORM BOUNDARY — CONTROLLED | 1 |

**Key closures since Wave 1.1:** path #10 (manifest not consumed), #18 reclassified (PAID SERP missing), #9 (Web-GPT platform boundary), #20 (project-specific confusion).

No open **critical executable** bypass remains.

---

## 15. Wave 1 Final Acceptance Assessment

| Criterion | Status |
|-----------|--------|
| Wave 1.1 checkpoint exists | Yes (`715402f`) |
| All production-capable entry points gated/blocked | Yes |
| Direct legacy cannot create canonical authority | Yes — executable proof |
| Canonical wrappers create receipts | Yes |
| Repository callers use gated paths | Documented + inventory |
| Output classification enforced | Yes |
| Corvonero blocked | Yes |
| Lockdown tests pass | 12/12 |
| No open critical executable bypass | Yes |
| Missing components honestly classified | Yes |
| Web-GPT boundary honest | Yes |

**Proposed status:**

```text
IMPLEMENTED — READY FOR OPERATOR OPERATIONAL APPROVAL
```

**Not self-approved as OPERATIONAL** — requires operator sign-off.

---

## 16. Wave 2 Readiness

All Wave 1 acceptance criteria pass subject to operator review of uncommitted Wave 1.2 implementation.

```text
WAVE 2 — READY FOR OPERATOR AUTHORIZATION
```

**Recommended Wave 2 first implementation:** `MIG PAID SERP — BUSINESS HOURS`

**Not implemented in this task.**

---

## 17. Files Created or Changed

### Wave 1.2 created (uncommitted)

| File |
|------|
| `runtime/src/legacy-entry-boundary.mjs` |
| `runtime/src/legacy-entry-boundary.cjs` |
| `runtime/src/output-path-guard.mjs` |
| `runtime/tests/run-lockdown-tests.mjs` |
| `runtime/reports/lockdown-test-results-v1.json` |
| `decisions/WAVE-1.2-OPERATOR-DECISIONS-v1.md` |
| `decisions/WAVE-1.2-OPERATOR-DECISIONS-v1.json` |
| `reports/REPORT-mars-search-ppc-wave1-2-legacy-lockdown-v1.md` |
| `reports/MARS-SEARCH-PPC-BYPASS-RE-AUDIT-WAVE1-2-v1.md` |
| `reports/EXTERNAL-AUTOMATION-BOUNDARY-AUDIT-v1.md` |
| `web-gpt/WEB-GPT-BOUNDARY-FINALIZATION-v1.md` |
| `projects/mig/docs/MIG-SEARCH-PPC-LEGACY-MIGRATION-v1.md` |

### Wave 1.2 modified (uncommitted)

| File |
|------|
| `projects/mig/lib/runtime/run-mig-session.js` |
| `projects/mig/tools/run-ppc-gated-session.mjs` |
| `projects/mig/OPERATIONAL-INDEX.md` |
| `projects/orca/semantic-intelligence/integration/runtime/cli/orca-admission.mjs` |
| `projects/orca/semantic-intelligence/integration/runtime/cli/orca-ppc-gate.mjs` |
| `projects/orca/semantic-intelligence/integration/runtime/README.md` |
| `projects/orca/ppc/triumph-manipulator/tools/exporter-cli/export.js` |
| `projects/orca/ppc/triumph-manipulator/tools/exporter-cli/sheet1-patch-export.js` |
| `projects/orca/ppc/triumph-manipulator/tools/run-ppc-gated-export.mjs` |
| `inventory/search-ppc-entry-point-inventory-v1.json` |
| `roadmap/MARS-SEARCH-PPC-LIFECYCLE-REPAIR-ROADMAP-v1.md` |

### Wave 1.1 checkpointed (`715402f`)

32 files — see section 3.

---

## 18. Git Status

- **Wave 1.1:** committed `715402f`, pushed  
- **Wave 1.2:** uncommitted on branch `mars/post-cycle8-live-tests` at `4621388`  
- **Not committed:** Wave 1.2 implementation per task instruction  
- Unrelated WIP (website-factory, ocpilot, fp-0002, etc.) remains unstaged

---

## 19. SAFE UNKNOWN

| Item | Note |
|------|------|
| Remote n8n Search PPC workflows | Not inspectable from repository |
| ABSTAIN automation ladder (bypass #8) | Wave 3 scope — remains OPEN |
| MIG uniform source-date enforcement (bypass #17) | Partial — Wave 2 enforcement |
| ORCA integration fixture path in lockdown test #3 | Uses diagnostic allow path; fixture location varies |

---

## 20. Operator Approval Items

1. Review and approve Wave 1.2 legacy lockdown implementation (uncommitted)  
2. Decide Wave 1 operational approval (`IMPLEMENTED — READY FOR OPERATOR OPERATIONAL APPROVAL`)  
3. Authorize Wave 2 start (`MIG PAID SERP — BUSINESS HOURS`)  
4. Verify external automation deployment checklist when n8n runtime accessible  
5. Confirm Corvonero remains frozen  

---

## 21. Recommended Next Action

**OPERATOR REVIEW OF MARS SEARCH PPC PRODUCTION WAVE 1.2**

Upon approval: commit Wave 1.2, then authorize Wave 2 implementation charter.

---

## 22. Stop Condition

Task complete:

- [x] Wave 1.1 checkpointed and pushed  
- [x] Legacy entry points physically locked  
- [x] Repository callers/docs migrated  
- [x] Output path protection implemented  
- [x] External automation boundary audited  
- [x] Web-GPT boundary finalized  
- [x] Lockdown tests 12/12 PASS  
- [x] Twenty-path bypass re-audit completed  
- [x] Wave 1 readiness and Wave 2 authorization assessment recorded  
- [x] Wave 1.2 left uncommitted for operator review  

**Not done (per instruction):** Wave 1 operational self-approval, Wave 2 implementation, Corvonero resume, Wave 1.2 commit.
