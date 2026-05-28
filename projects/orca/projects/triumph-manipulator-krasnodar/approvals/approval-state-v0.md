# Triumph Manipulator Krasnodar — Approval State v0

**project_id:** `triumph-manipulator-krasnodar`  
**Date:** 2026-05-21  
**Authority:** Human operator only (per [approval-gates-contract-v0.md](../../artifacts/approval-gates-contract-v0.md))

This file is the **canonical gate record** for the project container. Summary also appears in [`PROJECT.md`](../PROJECT.md).

---

## Gate matrix

| Gate | State | Evidence / notes |
|------|--------|------------------|
| `approved_for_research_use` | **yes** | Search architecture, SERP methodology, and competitor inputs operational in validated pack |
| `approved_for_strategy` | **yes** | S-tier + Full Cycle v1.1 groups 11–12 documented in campaign structure |
| `approved_for_keywords` | **yes** | Validation CLI v1.1: passed, `export_allowed: true`, 0 blocking errors |
| `approved_for_factory` | **yes** | Page 01 production handoff; MODE 1 semantic lock; v4 workspace build exists |
| `approved_for_commander_import` | **no — human-only pending** | Transport v0.6 + sheet1-patch + ZIP checks validated; **no operator sign-off** in pack (`human_review.approved_for_commander_import: false`) |
| `approved_for_ads` | **no — pending QA** | Page 01 implemented; manual browser QA not completed ([`landing-qa/v5-page01-landing-qa-v0.md`](../landing-qa/v5-page01-landing-qa-v0.md)) |
| `approved_for_launch` | **no** | Requires `approved_for_ads` + Commander import + live URL verification + launch checklist |

---

## Distinctions (anti-drift)

| Statement | True? |
|-----------|--------|
| Validation CLI passed | **yes** — export prep survivability |
| Exporter produced 108-row patch | **yes** — dumb transport artifact |
| Commander transport rules validated (v0.6) | **yes** — technical transport |
| Operator signed Commander import in Direct UI | **no** — **SAFE UNKNOWN** until human records smoke test |
| Commander import transport validated | **yes** |
| `approved_for_commander_import` | **no** until human signs this gate |
| Landing page 01 built in Factory | **yes** |
| `approved_for_ads` for page 01 | **no** — pending manual browser QA |
| `approved_for_launch` | **no** |

**Forbidden inference:** Validation green → launch approved. Exporter success → Commander import approved.

---

## Per-artifact alignment

| Artifact | Gate implied | Container / pack path |
|----------|--------------|------------------------|
| Keyword instance | `approved_for_keywords` | `ppc/triumph-manipulator/schema/instances/triumph-s-tier-draft-v1.json` |
| Validation report | Supports export only | `ppc/triumph-manipulator/tools/validation-cli/output/validation-report.output.json` |
| XLSX patch v1.1 | Requires `approved_for_commander_import` before UI import | `ppc/triumph-manipulator/tools/exporter-cli/output/triumph-sheet1-patch-full-cycle-v1.1.xlsx` |
| v5 handoff page 01 | `approved_for_factory` | `ppc/triumph-manipulator/handoff/triumph-manipulator-v5-page-01-manipulyator-5-tonn-handoff.md` |
| Landing QA record | `approved_for_ads` | `landing-qa/v5-page01-landing-qa-v0.md` |

---

## Sign-off placeholders (operator fills)

When a gate moves to **yes**, append a dated block below.

```markdown
### approved_for_commander_import — YYYY-MM-DD
- approver: <name>
- scope: Full Cycle v1.1 sheet1-patch smoke import
- notes: <Direct UI outcome>
- safe_unknown_gaps: <remaining>
```

```markdown
### approved_for_ads — YYYY-MM-DD
- approver: <name>
- scope: route manipulyator-5-tonn
- notes: <browser QA device/browser>
- safe_unknown_gaps: <e.g. mobile CTA>
```

```markdown
### approved_for_launch — YYYY-MM-DD
- approver: <name>
- scope: Search campaign live
- notes: <checklist ref>
- safe_unknown_gaps: <CPC, moderation, etc.>
```

---

## SAFE UNKNOWN

- Client verbal approval without written record — **not approved**
- Staging vs production URL — registry declares production domain; deploy state **UNKNOWN**
- Partial route launch (page 01 only) — must be explicit in sign-off scope

---

## Related

- [`PROJECT.md`](../PROJECT.md)
- [`bridge-links.md`](../bridge-links.md)
- [`../../artifacts/approval-gates-contract-v0.md`](../../artifacts/approval-gates-contract-v0.md)
