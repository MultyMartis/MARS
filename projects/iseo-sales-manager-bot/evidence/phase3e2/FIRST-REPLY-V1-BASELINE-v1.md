# FIRST-REPLY-V1-BASELINE-v1

**Baseline before Phase 3E.2**

- Template function: `buildFirstReplyDraft` in Parser 3.3 (`sm-reply-v1.1` era)
- Strengths: AI OFF; no auto-send; basic service branches; strip “ask for site” when provided/absent
- Defects closed by v2:
  - generic wording across services
  - over-asking / near-identical templates
  - weak acknowledgment of multi-stage Website+SEO
  - incomplete greeting / suppression contract
  - no structured reason codes for suppressed questions
  - message card still `sm-msg-v2.3`

v2 keeps semantic inputs from Lead Semantic Model v1 and replaces the draft generator.
