# Triumph — Actor and Authority Map v1

**Critical rule:** `CHAT CAPABILITY` ≠ `ORCA SYSTEM CAPABILITY`

---

## Actor matrix

| Actor | Decisions made | Evidence supplied | Authority level | Outputs | Limitations | Captured in MARS? | Machine-enforced? |
|-------|----------------|-------------------|-----------------|---------|-------------|-------------------|-------------------|
| **Operator** | Business scope; 12 routes; campaign/group architecture; launch boundary; Corvonero intake/seeds; P0 approvals A/B/C | Briefs; MIG approvals; Commander UI steps | **Highest** — explicit decisions | Route freeze; JSON content; import strategy; D2/D7 freeze | Cannot be substituted by automation | **Partial** — freezes, decisions JSON, approval records | **No** — human gates documented only |
| **Web-GPT chat** (historical) | Likely semantic architecture, phrase curation, doctrine articulation, process design | **Not in repo** | **Chat-local** — non-transferable | Unknown chat artifacts | Ends when chat ends; not available to Cursor/ORCA scripts | **Partial** — outcomes frozen as docs/JSON | **No** |
| **Cursor** | Implementation of validation-cli, exporter, freezes, Corvonero pipelines, contract validator, SI docs | Code, markdown, JSON in repo | **Tool executor** — no business authority | Scripts, reports, audit packages | Follows task scope; does not auto-enforce contracts in all pipelines | **Yes** — git artifacts | **Partial** — only where scripts run checks |
| **MIG** | Wordstat Pass A (Corvonero); SERP/website (Triumph pilot) | `incoming/mig/` sessions | **Evidence provider** — not admission authority | Normalized Wordstat JSON; research packs | Triumph: keyword_pass off; frequencies ≠ admission | **Yes** | **No** |
| **ORCA (documentation + Triumph tools)** | Doctrine; validation rules; export transport; laws; contracts | Frozen packs under `ppc/triumph-manipulator/`, `freeze/`, `contracts/` | **Production rules** below operator | 345-rule validator; cross-negative matrix | Copilot — not autonomous launcher | **Yes** | **Partial** — Triumph export path only |
| **Validators** | Flag SE/CM/LM violations; contract invariant checks | Rule registries; test fixtures | **Advisory / structural** (Triumph); **commercial** (contract tool if invoked) | PASS/FAIL reports | Triumph: human triggers; Corvonero v6: structural PASS without commercial gate | **Yes** | **Partial** |
| **External PPC (Yandex Direct Commander)** | Import transport; bid UI visibility | Desktop import behavior | **Platform truth** for transport | Import PASS/FAIL | Budget/schedule not in XLSX | **Documented** in battle findings | N/A |

---

## Authority order (Triumph — proven)

From `ORCA-CAMPAIGN-PRODUCTION-CONTRACT-v1.md` (derived from Triumph):

1. Operator decisions  
2. Operator-approved scope  
3. Operator-approved architecture  
4. Verified evidence  
5. Production rules / contract  
6. Classifier suggestions (advisory)  
7. QA suggestions  
8. Export formatting  

**Triumph battle enforced this informally** via freeze-before-keywords, human validation trigger, and no auto-launch.

---

## Authority failures (Corvonero)

| Actor overreach | Evidence |
|-----------------|----------|
| Pipeline script as admission authority | `run-clean-room-semantic-pipeline-v1.mjs` regex `classifyIntent` + `commercialEligibility` accepted ~1892 phrases without operator sign-off per phrase |
| Classifier v4–v6 as business authority | `REPORT-orca-evidence-audit-and-commander-v5.md`; template identical evidence |
| Structural validator as commercial PASS | v6 PASS with scope loss — `orca-production-contract-integration-plan-v1.md` |
| Contract listed AUTH-03 but **not loaded** by clean-room pipeline | Manifest vs script imports |

---

## Chat vs MARS boundary (summary)

| Capability | Web-GPT chat | MARS after freeze |
|------------|--------------|-------------------|
| Design 12-route semantic architecture | Possible in chat | **Documented + frozen** in repo |
| Curate 64 phrases with commercial judgment | Possible in chat | **Encoded in JSON** — partial capture |
| Run 345 validation rules | No | **Yes** — validation-cli |
| Enforce scope lock on new project | No | **Only if** contract gate wired |
| Repeat without operator | No | **Only** documented workflows + tools |

**Operator discovery is correct:** a prior chat could "build process then make repeatable" — but repeatability required **freeze + tools + human gates**, not chat continuity. Current SI/P0 work risks **renaming** those freezes without **integrating** them into Corvonero admission.
