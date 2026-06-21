# Reference Implementations — Index

**Classification:** discovery index — documentation only.  
**Status:** human-maintained register of proven reference implementations in MARS.  
**Is not:** a registry engine, runtime catalog, or deployment manifest.

**Purpose:** single discovery point for future reference implementations. Documents remain in their canonical project paths — this index links only; it does not move or duplicate source material.

---

## Registered reference implementations

| Field | WPilot |
|-------|--------|
| **Name** | WPilot (MetaCODE WPilot) |
| **Authority** | `WPILOT-RC5-PROVEN-CONNECTION-RUNTIME-2026-06-19` |
| **Lifecycle** | **Reference Implementation** |
| **Commit** | `648632acbdd42703427fd76a0cb1fd8d88641dcc` |
| **Runtime maturity** | `proven_content_writes` + `proven_connection_runtime` (DEV only — `https://dev.gktriumph.ru`) |
| **Primary documents** | [WPILOT-FINAL-STATE-RC5.md](../../wpilot/WPILOT-FINAL-STATE-RC5.md) · [WPILOT-AUTHORITY-STATE-RC5.md](../../wpilot/WPILOT-AUTHORITY-STATE-RC5.md) · [WPILOT-LIFECYCLE-STATE.md](../../wpilot/WPILOT-LIFECYCLE-STATE.md) · [WPILOT-MAINTENANCE-POLICY-v1.md](../../wpilot/WPILOT-MAINTENANCE-POLICY-v1.md) · [OPERATIONAL-INDEX.md](../../wpilot/OPERATIONAL-INDEX.md) |
| **Usage policy** | **Validation baseline and runtime reference** for CMS / Ecommerce Pilots family — pattern reuse (safety loop, connection tracking, local token standard) encouraged; **feature parity not required** for siblings. RC5 development focus **closed**; Sprint 3 **HOLD**; changes governed by [WPILOT-MAINTENANCE-POLICY-v1.md](../../wpilot/WPILOT-MAINTENANCE-POLICY-v1.md). Not MARS runtime; not autonomous CMS; not production deploy. |

**Family context:** [cms-ecommerce-pilots-family.md](../../ocpilot/cms-ecommerce-pilots-family.md)  
**Pattern doc:** [CMS-PILOT-RUNTIME-PATTERN-v1.md](../runtime-patterns/CMS-PILOT-RUNTIME-PATTERN-v1.md)  
**Registry row:** `wpilot` — [registry/project-registry.md](../../../registry/project-registry.md)

---

## Index maintenance rules

1. **Append only** when a human charter establishes a new reference implementation with proven runtime evidence and authority registration.
2. **Do not** infer reference status from partial prototypes or documentation-only packs.
3. **Link** to canonical project documents; do not copy or relocate source material into this folder.
4. **Update** this index when lifecycle, authority, or usage policy changes for a registered entry — with a dated note in the project pack, not silent drift.

---

## SAFE UNKNOWN

- Whether additional CMS Pilots (e.g. OCPilot) will reach Reference Implementation status — unknown until separate proof and human charter.
- Whether a unified cross-family reference index beyond CMS Pilots will exist — unknown; this index covers reference implementations registered here only.

---

*Reference Implementations Index · WPilot RC5 registered 2026-06-19.*
