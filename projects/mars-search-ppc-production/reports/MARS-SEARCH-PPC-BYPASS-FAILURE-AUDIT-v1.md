# MARS Search PPC — Bypass and Failure Audit v1

**Date:** 2026-06-22  
**Status:** `COMPLETE`  
**Method:** Explicit test of 20 charter failure paths against repository evidence  
**Companion:** [MARS-SEARCH-PPC-LIFECYCLE-GAP-AUDIT-v1.md](./MARS-SEARCH-PPC-LIFECYCLE-GAP-AUDIT-v1.md)

---

## Severity scale

| Level | Definition |
|-------|------------|
| **CRITICAL** | Can produce invalid launch/export or corrupt Semantic Core without machine stop |
| **HIGH** | Can advance strategy/production with material evidence gaps |
| **MEDIUM** | Process drift or operator overload; recoverable with review |
| **LOW** | Documentation or labeling risk |

---

## Failure path matrix

| # | Bypass | Current possibility | Evidence | Severity | Existing guard | Missing guard | Required repair |
|---|--------|:-------------------:|----------|:--------:|----------------|---------------|-----------------|
| 1 | Strategy created before dated analytical pack | **Yes** — in chat/workflow without manifest | Lifecycle validator detects `ppc_strategy_decision_record` before SPPC-12 complete (`validate-search-ppc-lifecycle.mjs` L164–167); Web-GPT contract forbids | **HIGH** | Validator rule; stage contract SPPC-13; execution contract | Validator **not mandatory** in chats; no strategist runtime gate | Wire validator to strategist entry; block `ppc_strategy_decision_record` registration until pack artifact exists |
| 2 | Campaign created before paid SERP evidence | **Yes** | Validator `PAID_SERP_EVIDENCE_MISSING` at SPPC-13+ without artifact or degradation approval (L139–149); synthetic-blocked fixture proves block | **CRITICAL** | Lifecycle validator when manifest at SPPC-13+ | Campaign Production CLIs do not call validator; MIG cannot produce evidence | Wave 2: MIG paid SERP mode; Wave 5: campaign entry requires manifest validation |
| 3 | Campaign created with approved degraded mode absent | **Yes** | `degraded_evidence_approvals.SPPC-10` checked in validator; synthetic-pre-strategy shows approved degradation path | **HIGH** | Validator checks `degraded_evidence_approvals`; `DEGRADED-EVIDENCE-MODE-v1.md` | No schema validation of degradation record completeness; campaign runtime unaware | Degraded approval schema validator; campaign CLI refuses without valid degradation or full SERP |
| 4 | Commander export created before QA | **Yes** — Triumph path historically possible | `FORBIDDEN_BEFORE['SPPC-19']` blocks `commander_export_artifact`; synthetic-blocked fixture | **CRITICAL** | Lifecycle validator; SPPC-19 contract; campaign contract export blockers | Triumph exporter can run outside manifest lifecycle | Commander export CLI must require manifest at SPPC-19 COMPLETED + QA artifact |
| 5 | Keywords clustered before admission | **Yes** — manual/chat | ORCA fixture `int-neg-007-ownership-before-accept`; admission contract forbids pre-admission ownership | **HIGH** | ORCA admission runtime (`1fcf3d2`) on admission path | No clustering producer; old Corvonero cluster maps exist but marked non-authoritative | Wave 3: clustering runtime with admission prerequisite check |
| 6 | Negatives generated before ownership | **Yes** — chat/manual scripts | SPPC-09 contract; campaign contract inline-negative rules; lifecycle stage order | **HIGH** | Documentation; stage prerequisites in machine contract | No negative-generation runtime enforcing SPPC-07 complete | Wave 3: negative intelligence module with ownership gate |
| 7 | Full corpus replaced by small pilot | **Yes** | P0-I 200-phrase pilot exists; reclassification decision forbids production substitution; SPPC-03 contract | **CRITICAL** | Charter text; P0-I reclassification; Corvonero full corpus preserved | **No runtime corpus row-count / provenance guard** | Wave 2–3: corpus intake validator comparing registered source registry totals vs intake artifact |
| 8 | ABSTAIN forwarded wholesale to operator | **Partially yes** | P0-I metrics show ABSTAIN queue; human-review-router I-05 exists; escalation ladder documented SPPC-05 | **MEDIUM** | ABSTAIN is valid outcome; router exists | Automated reassessment/adjudication **not implemented** (I-09 PLANNED DEFERRED) | Wave 3: implement reassessment + adjudication ladder before default human queue |
| 9 | Web-GPT chat continues despite missing artifacts | **Yes** | `WEB-GPT-SEARCH-PPC-EXECUTION-CONTRACT-v1.md` requires `BLOCKED — LIFECYCLE REQUIREMENT NOT MET` | **HIGH** | Execution contract; opening status block template | **No technical enforcement** in Web-GPT | Operator approval of contract + sync pack; mandatory manifest read in task starter |
| 10 | Manifest references contract but runtime does not consume it | **Yes** | Lifecycle contract + manifest template exist; MIG/ORCA/Campaign CLIs do not load manifest (placement decision notes fragmentation) | **CRITICAL** | Lifecycle validator can read both | Subsystems ignore manifest | Wave 1 completion: manifest consumption hooks in MIG/ORCA/Campaign entrypoints |
| 11 | Export changes semantic ownership | **Yes** — historically (Corvonero v1–v7) | `ORCA-CAMPAIGN-PRODUCTION-CONTRACT-v1` Section A scope lock; SPPC-20 transport-only; Triumph parity discipline | **CRITICAL** | Campaign contract; Commander stage contract | Export scripts not universally bound to contract validator | Wave 6: export parity validator mandatory; diff against production SoT |
| 12 | Strategy invents competitor information | **Yes** — chat | SPPC-13 forbidden list; analytical pack requires observed competitor fields | **HIGH** | Stage contract; Web-GPT forbidden outputs | No strategist output schema proving competitor field provenance | Wave 4: strategy record schema with evidence pointer requirements |
| 13 | Frequency determines commercial intent | **Yes** — legacy risk | SPPC-05/06 forbid frequency-only tiering; ORCA fixture `int-neg-004-topic-only-accept` | **HIGH** | Admission invariants; tier charter | No frequency-only lint on tier assignment artifacts | Wave 3: tier registry validator rejecting frequency-only rationale |
| 14 | Automatic bidding selected without analytics readiness | **Yes** | SPPC-18 contract blocks automated branch without conversion tracking | **HIGH** | Stage contract text | No bidding manifest validator | Wave 5: bidding strategy validator checking analytics prerequisites |
| 15 | Launch inferred from successful import/export | **Yes** | SPPC-21/22 separate; `final_launch_authority.granted` in manifest template | **CRITICAL** | Lifecycle stage separation; manifest field | No platform integration; operator discipline only | Wave 6: launch checklist artifact required before `launch_evidence_pack` |
| 16 | Post-launch data silently changes Semantic Core | **Yes** | SPPC-23 requires proposal-based versioned changes | **CRITICAL** | Stage contract | **No post-launch system exists** | Wave 7: governed proposal queue; no direct SoT mutation |
| 17 | Source dates and collection period missing | **Yes** — partial MIG sessions | SPPC-02 required fields; MIG handoff requires Date; Corvonero ledger has provenance | **HIGH** | MIG handoff contract; SPPC-02 contract | Not all MIG contracts enforce date passport uniformly | Wave 2: source registry schema validator (date/period mandatory) |
| 18 | Paid SERP collected outside business hours presented as market truth | **Yes** | SPPC-10 requires business-hours mode; **mode does not exist in MIG** | **CRITICAL** | Lifecycle documentation only | MIG mode + time passport validation | Wave 2: implement `PAID SERP — BUSINESS HOURS` with timestamp guard |
| 19 | Human review becomes primary classification engine | **Partially yes** | P0-I workbook optional; ABSTAIN queue exists; reclassification forbids mandatory manual review | **MEDIUM** | Reclassification decision; escalation ladder spec | Pilot workbook could be misused; I-09 deferred | Operator decision binding; deprecate workbook as default path; implement automated ladder |
| 20 | Project-specific process mistaken for universal capability | **Yes** | Triumph Commander freeze; Corvonero diagnostic; P0-I pilot — all explicitly bounded in docs | **HIGH** | Placement decision; freeze records; pilot reclassification | No capability matrix published per project | This gap audit + roadmap; label Triumph/Corvonero scope in operational indexes |

---

## Aggregate risk

| Severity | Count |
|----------|------:|
| CRITICAL | 7 |
| HIGH | 10 |
| MEDIUM | 2 |
| LOW | 0 |

**Top unblockers:** manifest runtime consumption (#10), MIG paid SERP mode (#2, #18), corpus-size guard (#7), export parity (#4, #11), post-launch governance (#16).

---

## Synthetic validator coverage map

| Failure # | Covered by lifecycle validator? |
|-----------|:-------------------------------:|
| 1 | Partial |
| 2 | Yes (when manifest used) |
| 3 | Partial |
| 4 | Yes (when manifest used) |
| 5–8 | No |
| 9 | No |
| 10 | N/A (meta) |
| 11–16 | No / partial |
| 17–20 | No |

---

## Related artifacts

- Gap audit: [MARS-SEARCH-PPC-LIFECYCLE-GAP-AUDIT-v1.md](./MARS-SEARCH-PPC-LIFECYCLE-GAP-AUDIT-v1.md)
- Repair roadmap: [../roadmap/MARS-SEARCH-PPC-LIFECYCLE-REPAIR-ROADMAP-v1.md](../roadmap/MARS-SEARCH-PPC-LIFECYCLE-REPAIR-ROADMAP-v1.md)
