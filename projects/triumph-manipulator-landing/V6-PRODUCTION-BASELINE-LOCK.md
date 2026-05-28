# Triumph V6 — production baseline lock (temporary)

**Status:** ACTIVE until explicit user override.  
**Type:** operational guard (rollout safety lock).  
**Purpose:** protect canonical V6 production baseline during route rollout/adaptation.

---

## Frozen canonical baseline (do not modify)

- `workspaces/triumph-manipulator-landing-v6/src/pages/index.html`
- `workspaces/triumph-manipulator-landing-v6/dist/index.html` (build output reference)
- Active zakaz partial chain
- Canonical V6 production semantics (hero/layout/CTA/FAQ/contact architecture)

Canonical index route is **REFERENCE / CONTROL / CALIBRATION baseline**.

---

## Forbidden during rollout/adaptation

- Editing canonical `index.html` directly for experiments
- Replacing active zakaz partials on canonical route
- Modifying canonical V6 semantics
- Using canonical index as live experimentation area
- Changing active production stack while adapting other routes
- Touching production-ready CTA hierarchy
- Modifying canonical FAQ/contact architecture
- Modifying canonical hero/layout semantics

---

## Required rollout mode for new routes

- Isolated work only (separate route/partials)
- Safe duplication from baseline first
- Adapt independently per route (e.g., `5-tonn`, other PPC pages, semantic variants)
- QA independently before any merge decision

---

## Unlock condition

Canonical V6 lock can be changed **only** by explicit user command in current operation context.

If override is not explicit, baseline remains frozen.
