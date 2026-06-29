# FP-0002 Shpigovsky — Workspace V8

## ACTIVE TEMPORARY PRIORITY RULE

Before any FP-0002 frontend implementation, read:

[`FP-0002-PRIORITY-VISUAL-IMPLEMENTATION-PROTOCOL.md`](../website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-PRIORITY-VISUAL-IMPLEMENTATION-PROTOCOL.md)

- **Visual PASS:** OPERATOR ONLY
- **Commit before operator visual approval:** PROHIBITED
- **Mandatory report header:** REQUIRED
- **Web-GPT recovery source:** THIS PROTOCOL

| Field | Value |
|-------|-------|
| **Project** | FP-0002 Shpigovsky |
| **Workspace version** | V8 |
| **Status** | BOOTSTRAP_RECONCILIATION_COMPLETE — Git protected; browser parity verified |
| **Parent workspace** | `workspaces/fp-0002-shpigovsky-v7/` (`IMMUTABLE_STABLE_FALLBACK`) |
| **Bootstrap authority tag** | `fp-0002-v7-four-template-canonical-demo-baseline-01` |
| **Bootstrap commit** | `6eb493e9eadb2578c2223278d41bdfe6970e5637` |

## Purpose

V8 is the consolidation workspace. Target formula:

`ОДИН ВИЗУАЛЬНЫЙ БЛОК` → `ОДИН PARTIAL` → `ОДНА HTML-СТРУКТУРА` → `ОДНО СЕМЕЙСТВО КЛАССОВ` → `ОДИН CSS` → `ОДНО RESPONSIVE BEHAVIOR`

Bootstrap pass (2026-06-28): audit and parity only — **no class renaming**, **no consolidation edits**.

## Canonical four templates

| Template ID | Source page |
| ----------- | ----------- |
| FP0002-TPL-001 | `src/pages/index.html` |
| FP0002-TPL-002 | `src/pages/uslugi-v2.html` |
| FP0002-TPL-003 | `src/pages/usluga-podrazdel-v1.html` |
| FP0002-TPL-004 | `src/pages/usluga-konechnaya-v1.html` |

**Excluded from V8 bootstrap:** `o-centre-v1.html` (rejected WIP — not canonical).

## Design authority

| Source | Role |
|--------|------|
| `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/Spig_v1.2.fig` | ACTIVE |

## Build

```bash
npm ci
npm run build
```

## Key docs

- `../website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-PRIORITY-VISUAL-IMPLEMENTATION-PROTOCOL.md` — **read before any frontend task**
- `foundation/FP-0002-V8-OPERATIONAL-STATUS.md`
- `foundation/FP-0002-V8-COMPONENT-GATE-RULES-v1.md`
- `audits/component-family-audit-v8-bootstrap-01/`
- `plans/component-consolidation/FP-0002-V8-CONSOLIDATION-PLAN-v1.md`
