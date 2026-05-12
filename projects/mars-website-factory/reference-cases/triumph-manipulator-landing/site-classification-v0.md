# Site classification — Triumph Manipulator Landing (v0)

**Registry SoT:** [Site Type Registry v0](../../site-type-registry-v0.md)

---

## Primary `site_type_id`

**`service_landing`** — primary classification row.

### Why `service_landing` (not generic `landing`)

| Registry signal | Fit for Triumph / manipulator |
|-----------------|--------------------------------|
| **primary_goal** | Qualified requests for a **service** (quote, booking, call) |
| **conversion_logic** | Trust-first then CTA; phone secondary acceptable |
| **SEO_model** | **`intent_pages`** + **`local_pack` when geography matters`** |
| **UX_model** | **`scan_and_act`** with **process** clarity |
| **content_depth** | **`medium`** — equipment classes, safety, scope need explanation |
| **trust_model** | Cases, certifications, service area, guarantees (where lawful) |

---

## Geo / commercial hybrid (documented divergence)

This URL behaves as **service_landing** with **strong geo-commercial intent** (regional traffic, service area, possibly map). That aligns with the registry row’s **`SEO_model`** note (`intent_pages` + `local_pack` when geography matters) — **not** a separate `geo_landing` **primary** type, because the page still **centers one service family** (manipulator operations) rather than a pure location hub.

**`notes` (for blueprint):** If the program later splits into **city cluster** URLs, each child URL should either remain `service_landing` per city or be reclassified with PM approval — **reclassification invalidates** IA and blueprints downstream.

---

## Conversion-focused

- **Category:** `conversion` (per registry).
- **commercial_intent:** `high` — aggressive **ethics** still apply (no false urgency, no fake local signals).

---

## Trust-heavy

- **trust_model** row expectations: proof before hard commit; **`HITL_required`** for regulated trades is `often`; for general commercial manipulator work, treat as **`selective`–`often`** until legal classifies.

---

## Forbidden patterns (from `service_landing` + case QA)

Apply registry **forbidden_patterns** for `service_landing`:

- Fake local addresses; “near you” without real service area.
- Medical/financial **guarantees** (N/A but forbidden if copy drifts).
- Review gating copy; unverifiable awards.

**Case-specific additions:**

- **Equipment capacity claims** without spec sheet alignment.
- **“Licensed everywhere”** without jurisdiction list.

---

## Classification QA checklist (manual)

| Check | Result (v0 doc run) |
|-------|----------------------|
| Competing primary CTAs | Rejected in blueprint — single primary |
| Site type / block compatibility | Pass with documented `service_scope` role mapping (see blueprint `notes`) |
| Hybrid documented | Pass |

---

*Classification v0 — reference execution only*
