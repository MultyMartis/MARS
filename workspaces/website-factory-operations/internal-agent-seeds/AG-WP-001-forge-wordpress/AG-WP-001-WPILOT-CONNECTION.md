# AG-WP-001 — Forge WordPress ↔ WPilot Connection Note

**Agent ID:** AG-WP-001  
**Status:** SEED  
**Date:** 2026-06-11  

---

## Purpose

Зафиксировать различие и дополнение между **Forge WordPress** (экспертное производственное направление) и **WPilot** (инструментальный мост) — без слияния ролей.

---

## Two roles (not one)

| Dimension | Forge WordPress (AG-WP-001) | WPilot |
|-----------|----------------------------|--------|
| **Classification** | Website Factory Internal Agent Seed | Program / Operational System (`projects/wpilot/`) |
| **Primary function** | Будущая экспертиза: *что* и *как* строить в WordPress из Factory Frontend | Инструмент: *безопасно* инспектировать и делать scoped changes на WP-сайте |
| **Knowledge** | Накапливается из реальных Factory-проектов | Документированные safety contracts, plugin MVP planning |
| **Runtime claim** | **None** (SEED) | Human-supervised workflow; plugin code exists under `projects/wpilot/plugin/` — **not** autonomous admin |
| **Status** | SEED | documented Phase 1 base |

```text
  ┌─────────────────────────┐     ┌─────────────────────────┐
  │   Forge WordPress       │     │        WPilot           │
  │   expertise direction   │     │   instrumental bridge   │
  │   (SEED)                │     │   (tool / ops system)   │
  └───────────┬─────────────┘     └───────────┬─────────────┘
              │                               │
              │    complementary — not same   │
              └───────────────┬───────────────┘
                              ▼
                    WordPress production work
                    (human-operated, evidence-based)
```

---

## How they complement each other

| Forge WordPress provides (future) | WPilot provides (documented) |
|-----------------------------------|------------------------------|
| Production discipline from Factory cases | Read-only inspection, dry-run, refusal-first mutation |
| Intent: Frontend → WordPress translation | Beget test-site workflow, backup/rollback discipline |
| Learning containers per project | REST/plugin surface (MVP planning pack) |
| «What good implementation looks like» — from evidence | «How to change safely on a live WP instance» |

**Forge WordPress does not execute WP changes.**  
**WPilot does not define Factory WordPress architecture.**

---

## Documented WPilot ↔ Factory link (planned)

From [projects/wpilot/README.md](../../../projects/wpilot/README.md):

- WPilot strategic direction: **Factory-native WordPress** as preferred long-term target.
- Relationship table: **MARS Website Factory** — «planned upstream source for Factory-native WordPress payloads».
- Status: **planned direction**, not runtime claim.

Forge WordPress SEED **aligns with** this direction narratively; **does not modify** WPilot docs in this charter.

---

## FP-0002 touchpoint

| Item | Location |
|------|----------|
| WPilot improvement inputs | [KNOWLEDGE-EXTRACTION/wpilot-improvements/](../../FP-0002-SHPIGOVSKY/KNOWLEDGE-EXTRACTION/wpilot-improvements/) |
| WordPress incoming lane | [INCOMING/06_WORDPRESS/](../../FP-0002-SHPIGOVSKY/INCOMING/06_WORDPRESS/) |

WPilot evolution notes from FP-0002 **feed WPilot**, not Forge WordPress rules directly.

---

## Explicit non-claims

| Do not claim | Truth |
|--------------|-------|
| Forge WordPress **is** WPilot | **False** — different classification |
| WPilot **is** the WordPress agent | **False** — tool/bridge; candidate agent roles listed as future only in WPilot README |
| Integration is live on FP-0002 | **SAFE UNKNOWN** |
| Plugin MVP equals Factory handoff | **False** — plugin MVP is bounded DEV scope |

---

## SAFE UNKNOWN

| Item | Status |
|------|--------|
| Concrete handoff payload format Factory → WPilot | **SAFE UNKNOWN** |
| Whether FP-0002 uses WPilot plugin | **SAFE UNKNOWN** |
| Agent card for `wp-*` roles in `agents/` | **SAFE UNKNOWN** — WPilot lists candidates only |

---

*Connection note only. WPilot unchanged. No integration implementation.*
