# HomeGateway v4.ai — information priority model v0.1

**Статус:** **DRAFT** · **PLANNING** · **POST-PROTOTYPE**  
**Назначение:** канонические **приоритеты внимания** P0–P3 и anti-overload дисциплина.

**Связанные:** [tactical-signal-philosophy-v0.1.md](tactical-signal-philosophy-v0.1.md) · [cockpit-spatial-architecture-v0.1.md](cockpit-spatial-architecture-v0.1.md) · [cognitive-load-and-density-notes-v0.1.md](cognitive-load-and-density-notes-v0.1.md)

---

## Core principle

**Not everything urgent-looking deserves foveal attention.**  
Priority assigns **where** information may appear and **how loud** it may be.

---

## Priority tiers

| Tier | Name | Attention | Spatial home | Visual loudness |
|------|------|-----------|--------------|-----------------|
| **P0** | Critical | Immediate foveal + peripheral | `info_area` top, `top_bar` chip, sticky sections | CRITICAL/OVERDUE tokens — restrained |
| **P1** | Active operational | Primary work | `main_area` | Standard surfaces |
| **P2** | Passive useful | Secondary scan | `main_area` secondary blocks, `favorites_used` | Muted |
| **P3** | Ambient | Peripheral glance | `system_status`, background hints | Minimal |

---

## Mapping examples

| Information | Tier | Notes |
|-------------|------|-------|
| OVERDUE deadline | **P0** | Persistent; survives Focus |
| CRITICAL due-today | **P0** | Not fullscreen |
| Active project editing | **P1** | Center canvas |
| Client list / next deadline hint | **P1** | Main Cockpit |
| MARS lane summary (display-only) | **P2** | Glance block |
| Project activity / recent links | **P2** | |
| Recurring reminder (14+ days) | **P2** → **P0** as date nears | Escalation path |
| Frequent links | **P2** | |
| n8n last-run OK | **P2** | Systems view |
| Theme / clock / connection stub | **P3** | `system_status` |
| Background system info | **P3** | No alarm styling |
| INFO distant deadline | **P3** in rail | Lower sort |

---

## Cognitive load control

| Mechanism | How |
|-----------|-----|
| **Tier caps** | Max 2 P0 rows with full emphasis visible at once in rail preview |
| **Density by mode** | Systems high ≠ Main high ([operational-modes-v0.1.md](operational-modes-v0.1.md)) |
| **Progressive disclosure** | P2 detail behind click/overlay |
| **Single global P0 strip** | One overdue chip in `top_bar` |

---

## Attention discipline

| Rule | Rationale |
|------|-----------|
| P0 cannot flood canvas | Prevents dashboard alarm wall |
| P1 owns `main_area` center | Work-first |
| P3 never uses CRITICAL color | Semantic honesty |
| Escalation is monotonic | INFO→WATCH→…→OVERDUE; no skip to red for attention |

---

## Anti-overload philosophy

| Symptom | Mitigation |
|---------|------------|
| Everything P0 | Strict level rules + sort |
| Widget equality | Spatial tri-focus |
| Notification blindness | Fewer, persistent, meaningful P0 |
| Fantasy UI noise | P3 stays calm ([visual-language-direction-v0.1.md](visual-language-direction-v0.1.md)) |

---

## Relationship to signal levels

Signal **level** (INFO…OVERDUE) maps to **priority band**, not 1:1 to P-tier:

| Level | Typical priority |
|-------|------------------|
| OVERDUE, CRITICAL | P0 |
| WARNING, WATCH | P1–P2 |
| INFO | P2–P3 |

---

## Mode interactions

| Mode | P0 behavior |
|------|-------------|
| Main | Rail + chip |
| Focus | Chip + compact overdue |
| Tactical full | Expanded P0 section |
| Systems | P0 only if operator-task overdue — not fake bot CRITICAL |

---

## SAFE UNKNOWN

- Auto priority from integrations — Phase 7.
- User override «pin to P0» — admin future.

---

*Last updated: 2026-05-24 — Information priority model.*
