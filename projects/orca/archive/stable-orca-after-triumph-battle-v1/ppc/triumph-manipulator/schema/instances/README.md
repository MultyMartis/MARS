# ORCA PPC JSON Instances — Triumph Manipulator

**Phase:** 3 — draft fixtures only  
**Status:** Example documents for schema review and future validator tests · **not** production campaigns

---

## Purpose

Holds **sample PPC project documents** that conform (conceptually) to [orca-ppc-document-v1.schema.json](../json/orca-ppc-document-v1.schema.json).

Use for:

- Human walkthrough of entity shape  
- Future validation engine golden/fixture tests  
- Prompt-system few-shot examples (with clear draft labeling)

---

## Files

| File | Description |
|------|-------------|
| [triumph-s-tier-draft-v1.json](triumph-s-tier-draft-v1.json) | S-tier / high-priority groups only — 1 campaign, 5 groups, draft human review |

---

## Fixture honesty

| Claim | Truth |
|-------|-------|
| Represents final Triumph campaigns | **No** — draft structure and copy for schema exercise |
| Approved for launch | **No** — `human_review.approved_for_launch` = false |
| Validated by engine | **No** — no validator in repo; manual checklist only |
| URLs are production-live | **SAFE UNKNOWN** — placeholders unless operator confirms |

---

## Before using a fixture

1. Read [../json/README.md](../json/README.md)  
2. Run future validator against schema (when implemented)  
3. Apply [../validation-schema-v1.md](../validation-schema-v1.md) manually today  
4. Obtain human review flags before any export or Commander import

---

## Adding instances

- Name: `{project}-{tier-or-scope}-{status}-v{N}.json`  
- Always set `human_review.required` appropriately  
- Never commit launch-approved fixtures without explicit operator charter
