# PARSER 3.2 BASELINE v1 — Phase 3E.1

**Status:** historical baseline before Parser 3.3 cutover.

| Field | Value |
|-------|-------|
| Parser | `sm-parser-v3.2` |
| Message format | `sm-msg-v2.2` (3D.8.x cards) |
| Semantic model | not present (flat fields only) |
| Website states | messenger/site split only; no `explicitly_absent` enum |
| Intent | heuristic / form-title bias risk (Audit default) |
| First reply | template; may re-ask known facts |

Local v3.2 reference modules existed only under private STORAGE incoming (not committed). Production after 3E.1 uses `sm-parser-v3.3` / `sm-msg-v2.3`.

**Regression:** harness H29 asserts Parser 3.2-compatible CLEAN field presence under 3.3.
