# HomeGateway v4.ai — Cockpit OS concept notes v0.1

**Статус:** **DRAFT** · **PLANNING** · Phase 2 · **CONCEPTUAL ONLY**

**Назначение:** зафиксировать направление **«Cockpit OS»** как UX/environment metaphor для HG v4.ai — без claim на реальную ОС или runtime.

---

## What «Cockpit OS» means (allowed)

**Cockpit OS** — рабочее название **концептуального направления** для единого операционного окружения оператора:

| Concept | Definition in HG |
|---------|------------------|
| **Unified operational environment** | Multi-view cockpit connected by shared shell, signals, block-screens |
| **Connected cockpit experience** | Modes, overlays, and cross-links — not isolated pages |
| **Operational surface layer** | Display and quick actions above MARS/n8n/bots — not control plane |
| **Modular cockpit workspace** | Composable block-screens in zone-based shell |
| **Operator-centric UX** | Solo studio owner; no enterprise team tropes |
| **Navigation layer** | Layered mode switching ([navigation-hierarchy-v0.1.md](navigation-hierarchy-v0.1.md)) |
| **Signal-oriented environment** | Urgency and status drive hierarchy, not equal widgets |

**Синонимы (допустимы в документации):** multi-view cockpit, operational workspace, cockpit system.

---

## What «Cockpit OS» does NOT mean (forbidden claims)

| Forbidden | Clarification |
|-----------|---------------|
| Real operating system | No kernel, processes, drivers, window manager |
| Runtime platform | No HG execution engine, no agent host |
| Orchestration engine | No workflow run, no MARS orchestration |
| Desktop environment replacement | Browser-based cockpit only |
| Autonomous system | No self-switching modes, no auto-remediation |
| Product SKU «OS» for marketing | Internal concept label unless operator renames |

**AGENTS.md alignment:** documentation-first; **no** implementation claim.

---

## Relationship to multi-view cockpit

```text
         ┌──────────────────────────────────────┐
         │     Cockpit OS (concept umbrella)     │
         │  unified env · operator · signals     │
         └───────────────────┬──────────────────┘
                             │
         ┌───────────────────┼───────────────────┐
         ▼                   ▼                   ▼
  Multi-view system    Navigation layer    Block-screen modules
  (operational views)  (L1/L2/L3)          (visual units)
```

[Cockpit OS] names the **whole**; [multi-view cockpit system](multi-view-cockpit-system-v0.1.md) names the **structural pattern**.

---

## Environment layers (conceptual stack)

| Layer | HG v0.1–2 reality |
|-------|-------------------|
| **Operator** | Human studio owner |
| **Cockpit OS (concept)** | UX environment metaphor |
| **Cockpit shell** | Zones: top, nav, canvas, rail, strip, overlay |
| **Operational views** | Modes A–H |
| **Block-screens** | Content modules |
| **External systems** | MARS docs, n8n, bots, sites — **display/link**, not embedded OS |

---

## Design values (Cockpit OS direction)

1. **Coherence** — same tokens, signals, and zone language everywhere.
2. **Contextual density** — environment adapts to mode, not one grid.
3. **Calm control** — high-tech aesthetic without anxiety defaults.
4. **Honest display** — mock/sample labeled; no fake live orchestration.
5. **Exit ramps** — external tools open in browser tab, not trapped UX.

---

## Evolution path (documentation only)

| Phase | Cockpit OS maturity (conceptual) |
|-------|----------------------------------|
| 0–1 | Single-hub thinking → **superseded** by multi-view (Phase 2) |
| 2 | Mode + navigation architecture defined (this doc set) |
| 3–4 | Visual + static shell demonstrating 2–3 modes |
| 5–6 | Admin + data — still **not** OS |
| 7+ | Live integrations — cockpit remains **surface**, not platform |

---

## Terminology guardrails for authors

| Write | Avoid |
|-------|-------|
| «Cockpit OS concept» | «HG OS ships in Q3» |
| «Operational environment» | «Platform kernel» |
| «Mode switch» | «OS process switch» |
| «Cockpit system» | «Orchestration layer» |

---

## SAFE UNKNOWN

- Whether «Cockpit OS» remains internal codename or appears in operator-facing UI.
- Trademark / naming collision check — not done.
- Relationship branding to MARS — display-only blocks only.

---

*Last updated: 2026-05-20 — Phase 2 conceptual notes only.*
