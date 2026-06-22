# Forge WordPress → WPilot Handoff Contract v1

**Document type:** Boundary contract (B3)  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-02  
**Authority:** Forge WordPress subsystem — FWP-11 gate

**Aligns with:** [FORGE-WORDPRESS-HANDOFF-BOUNDARIES-v1.md](../FORGE-WORDPRESS-HANDOFF-BOUNDARIES-v1.md) · WPilot [WPILOT-CHANGESET-v1.md](../../../../wpilot/WPILOT-CHANGESET-v1.md) · [WPILOT-RISK-CLASSES-v1.md](../../../../wpilot/WPILOT-RISK-CLASSES-v1.md) · [WPILOT-ROLLBACK-v1.md](../../../../wpilot/WPILOT-ROLLBACK-v1.md) · [WPILOT-TARGET-REGISTRY-v1.md](../../../../wpilot/WPILOT-TARGET-REGISTRY-v1.md)

**Honesty:** Package specification only — **does not** modify WPilot plugin, runtime, or RC5 status.

---

## 1. Purpose

Define the **mandatory handoff package** Forge WordPress delivers to WPilot before controlled WordPress operations. Formalizes boundary **B3**.

**WPilot does not own** theme architecture, content model design, or ACF schema — it **operates** approved packages.

---

## 2. Handoff gate (blocking)

WPilot intake requires:

```text
WV9 PASS
+
operator handoff approval (G10)
+
complete RELEASE-MANIFEST
+
no credentials in package
```

---

## 3. Handoff package (required elements)

| Element | Artifact / path | Notes |
|---------|-----------------|-------|
| **project identity** | Intake + passport refs | `project_id`, owner |
| **implementation mode** | WAD | A \| B \| C \| D |
| **Git revision** | Tag or SHA | Theme + plugin repos |
| **source path** | LOC-ZONE or repo URL | Human-readable |
| **build artifact** | Theme dist / enqueue manifest | Reproducible build notes |
| **theme package** | Theme directory or ZIP | Presentation only |
| **functionality plugins** | Custom plugin(s) | CPT, ACF, business logic |
| **ACF schema** | Local JSON paths | If ACF mode |
| **content model** | CONTENT-MODEL artifact | Summary + CPT/taxonomy map |
| **editable regions** | EDITABLE-REGIONS-MAP | Frozen vs editable |
| **template map** | TEMPLATE-MAP | WP templates ↔ pages |
| **CPT/taxonomy map** | CPT-TAXONOMY-MAP | URLs, archives |
| **plugin register** | PLUGIN-REGISTER | Approved third-party set |
| **environment requirements** | PHP, WP version, extensions | Minimum spec |
| **validation reports** | WV0–WV9 as applicable | Evidence bundle |
| **visual approval** | VISUAL-QA-REPORT + operator sign-off | PIXEL_PERFECT blocking |
| **admin UX approval** | WV7 + ADMIN-UX-MAP | Editor simulation |
| **known limitations** | Explicit list | Deferred features, SAFE UNKNOWN |
| **deployment instructions** | Human-readable steps | DEV/staging first |
| **backup requirements** | Pre-deploy backup policy | Aligns WPilot backup-first |
| **rollback notes** | Theme/plugin version pins | WPilot Rollback policy input |
| **change restrictions** | Mutation zones | WPilot Target Registry alignment |
| **operations ownership** | WPilot vs operator vs client | RACI summary |

### Explicitly excluded from package

| Excluded | Reason |
|----------|--------|
| **Production credentials** | [R-ENV-02](../FORGE-WORDPRESS-ARCHITECTURAL-DECISIONS-v1.md) |
| **Database dumps** (unless chartered) | Not SoT — [R-VC-06](../FORGE-WORDPRESS-ARCHITECTURAL-DECISIONS-v1.md) |
| **WPilot plugin source** | Separate product — Forge does not bundle metacode-wpilot |
| **Live content as authority** | Git + manifest SoT |

---

## 4. WPilot policy alignment

| WPilot concept | Forge handoff relationship |
|----------------|---------------------------|
| **ChangeSet** | Deploy/ops runs use ChangeSet container — package supplies `changeset_id` refs, approval evidence |
| **Risk Classes** | Package declares default risk for deploy class ops — human assigns per run |
| **Rollback** | Version pins + backup requirements feed rollback planning |
| **Target Registry** | EDITABLE-REGIONS-MAP defines mutation zones; frozen zones = restricted targets |
| **Mode A intake** | Factory-native packages are **preferred** WPilot long-term target — full manifest equivalence |

Forge WordPress **produces**; WPilot **operates**. No theme re-implementation by WPilot.

---

## 5. Acceptance outcomes

| Outcome | Definition |
|---------|------------|
| **ACCEPTED** | Package complete; WV9 pass; G10 approved — WPilot may plan DEV/staging ops |
| **CONDITIONAL ACCEPTANCE** | Minor gaps with tracked remediation — no production ops until closed |
| **REJECTED** | Missing WV reports, credentials in package, or architecture boundary violation |
| **RETURN TO FORGE WORDPRESS** | WV failures, incomplete manifest, visual/admin UX not approved |

---

## 6. Rejection conditions

| Condition | Outcome |
|-----------|---------|
| Missing RELEASE-MANIFEST | REJECTED |
| Missing EDITABLE-REGIONS-MAP | REJECTED (G10 block) |
| Credentials in package | REJECTED — security |
| WV6 fail (PIXEL_PERFECT) without waiver | REJECTED |
| WV7 fail — open editor surface | REJECTED |
| Plugin register incomplete | REJECTED |
| Theme contains CPT registrations | REJECTED — R-TF-02 violation |

---

## 7. Lifecycle mapping

| Stage | Contract role |
|-------|---------------|
| FWP-10 | RELEASE-MANIFEST assembly |
| FWP-11 | This contract + G10 |
| WV9 | Packaging validation |

---

## Related documents

- [templates/FORGE-WORDPRESS-WPILOT-HANDOFF-TEMPLATE-v1.md](../templates/FORGE-WORDPRESS-WPILOT-HANDOFF-TEMPLATE-v1.md)
- [templates/FORGE-WORDPRESS-RELEASE-MANIFEST-TEMPLATE-v1.md](../templates/FORGE-WORDPRESS-RELEASE-MANIFEST-TEMPLATE-v1.md)
- [projects/wpilot/README.md](../../../../wpilot/README.md)
- [standards/FORGE-WORDPRESS-FUNCTIONALITY-PLUGIN-STANDARD-v1.md](../standards/FORGE-WORDPRESS-FUNCTIONALITY-PLUGIN-STANDARD-v1.md)

---

*WPilot handoff contract v1 — B3 formalized; WPilot runtime unchanged.*
