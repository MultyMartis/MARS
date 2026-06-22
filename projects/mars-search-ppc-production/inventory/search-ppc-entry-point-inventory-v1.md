# MARS Search PPC — Entry Point Inventory v1 (Wave 1.1)

**Date:** 2026-06-22  
**Status:** `IMPLEMENTED — OPERATOR REVIEW REQUIRED`

Machine-readable: [search-ppc-entry-point-inventory-v1.json](./search-ppc-entry-point-inventory-v1.json)

---

## Summary

| Disposition | Count |
|-------------|------:|
| Wired via canonical gate | 12 |
| Wrapped (gated wrapper exists) | 8 |
| Quarantined / legacy | 9 |
| Missing runtime | 6 |
| Contract / doc only | 14 |

---

## Canonical gate surface

All wired entry points must call:

```bash
node projects/mars-search-ppc-production/runtime/cli/search-ppc-gate.mjs \
  --manifest <path> --action <action> [--stage SPPC-NN]
```

Or subsystem adapter: `mig-ppc-gate`, `orca-ppc-gate`, `campaign-ppc-gate`, `export-ppc-gate`.

---

## MIG (SPPC-02, 03, 04, 10, 11)

| Path | Command | Gate wired? |
|------|---------|-------------|
| `projects/mig/tools/mig-ppc-gate.mjs` | Adapter API | **Yes** |
| `projects/mig/tools/run-ppc-gated-session.mjs` | Gated wrapper | **Yes** |
| `projects/mig/lib/runtime/run-mig-session.js` | Direct session | **Quarantined** — use gated wrapper |
| `projects/mig/tools/run-task-file-adapter.ps1` | Inbox adapter | **Quarantined** |
| SPPC-10 paid SERP mode | — | **MISSING** |

---

## ORCA Semantic (SPPC-05–09)

| Path | Command | Gate wired? |
|------|---------|-------------|
| `orca-ppc-gate.mjs` | Gated CLI | **Yes** |
| `orca-admission.mjs` | Direct admission | **Quarantined** — wrap with gate |
| Tiers / ownership / clusters / negatives CLIs | — | **MISSING** |

---

## Campaign Production (SPPC-14–19)

| Path | Gate wired? |
|------|-------------|
| `campaign-ppc-gate.mjs` | **Yes** |
| `run-ppc-gated-campaign.mjs` | **Yes** |
| Corvonero `run-full-production-v*.mjs` | **Quarantined** |

---

## Commander Export (SPPC-20)

| Path | Gate wired? |
|------|-------------|
| `run-ppc-gated-export.mjs` | **Yes** |
| Triumph `exporter-cli/export.js` | **Quarantined** |

---

## AI PPC Strategist (SPPC-13)

**MISSING RUNTIME** — contract only: [strategist-entry-point-spec-v1.md](../contracts/strategist-entry-point-spec-v1.md)

---

## Cursor / Web-GPT

| Path | Enforcement |
|------|-------------|
| `validate-cursor-ppc-task.mjs` | **Executable linter** |
| `validate-webgpt-handoff.mjs` | **Handoff validator** |
| Web-GPT chat UI | **No runtime hook** — contract + handoff only |

---

## Related

- [REPORT-mars-search-ppc-wave1-1-entry-point-wiring-v1.md](../reports/REPORT-mars-search-ppc-wave1-1-entry-point-wiring-v1.md)
