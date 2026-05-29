# Factory Handoff State v1

**Freeze:** ORCA Route Family Freeze v1 · 2026-05-28  
**Extends:** [orca-factory-coordination-protocol-v1.md](../../coordination/orca-factory-coordination-protocol-v1.md) — frozen snapshot, not a replacement

---

## Role split at freeze

### Website Factory — implementation layer

Factory **now** owns (post-handoff, human-operated build):

| Layer | Responsibility |
|-------|----------------|
| **Implementation** | V6 partials, HTML structure, `data-*` markers |
| **Presentation** | SCSS, spacing, typography fit, imagery crop |
| **Responsive / mobile** | Breakpoints, stack order, overflow fixes, touch targets |
| **QA (presentation)** | Build closure, visual drift reports, mobile findings |

Factory **does not** own: ad copy, intent tier, claim invention, FAQ semantic rewrite, pricing meaning, route strategy.

**Baseline workspace:** `workspaces/triumph-manipulator-landing-v6/`  
**Build status at freeze:** 1/12 routes built (`zakaz` / `index.html`); 11 scaffolds under `v5-ppc/`.

---

### ORCA — semantic authority layer

ORCA **now** owns (frozen for 12-route family):

| Layer | Responsibility |
|-------|----------------|
| **Semantic authority** | H1, lead, tasks, denied, qualification |
| **PPC continuity** | Group ↔ landing ↔ ad alignment |
| **Calibration** | Lessons, drift class, productive vs destructive |
| **Drift control** | `forbidden-drift`, semantic-lock, MODE 1 |
| **Content packs** | Production semantic packs (`*-pack-v1`) |
| **Exports** | DOCX/Markdown handoff structure (human-approved) |

ORCA **does not** own: gulp pipeline, deploy, responsive policy implementation, form backend.

---

## Handoff artifact (what Factory receives)

Per route, Factory intake expects:

```text
approved pack (MODE 1) + optional handoff MD + visual semantics (Profile A)
                 OR
flat website_copy pack (Profile B) + PACK-STATUS gates
```

**Minimum contract:** [factory-handoff-minimum-contract-v1.md](../../coordination/factory-handoff-minimum-contract-v1.md)  
**Readiness checklist:** [production-pack-readiness-checklist-v1.md](../../coordination/production-pack-readiness-checklist-v1.md)

---

## Handoff state by route (summary)

| Route | ORCA pack | Handoff MD | Factory page | Human `approved_for_factory` |
|-------|-----------|------------|--------------|------------------------------|
| zakaz | v1 full (draft) | **Missing** | V6 built | **false** |
| 5-tonn | v1 full | v5 handoff exists (path in coordination docs) | scaffold | pending |
| bytovki | v1 full | pending | scaffold | pending |
| 10 siblings (Profile B) | v1 flat, copy-ready | pending | scaffold | pending (pack allows factory) |

---

## What Factory returns (unchanged contract)

After implementation, Factory lane returns **human-reviewed**:

- Implementation report (files, build, URL path in workspace)
- Visual / responsive drift findings
- Mobile QA notes — **not** auto-blocking

ORCA consumes findings into calibration — **not** silent merge into packs.

---

## Pilot sequence (reference — not executed in freeze)

From [route-priority-roadmap-v1.md](../../coordination/route-priority-roadmap-v1.md):

1. Sign zakaz pack + resolve D2 H1 strategy  
2. Factory pilot: **5-tonn** (highest capability risk)  
3. Gate: one V6 page QA before accelerating H2 use-cases  
4. Wave: bytovki → stroymaterialy → vezdehod → …

**Freeze does not authorize starting pilots** — operator charter required.

---

## MODE 1 reminder

Under semantic lock MODE 1, Factory may **not** paraphrase locked copy or invent claims. Drift acceptance requires human sign-off per [orca-website-factory-semantic-lock-v0.md](../../intelligence/orca-website-factory-semantic-lock-v0.md).
