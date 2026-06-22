# Forge WordPress — Validation Architecture v1

**Document type:** WordPress validation layer charter  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-01

**Orthogonality:** **WV** (WordPress Validation) is **separate** from Factory **VL** (Validation Layers). Factory VL0–VL6 governs **upstream frontend** only. WV0–WV9 governs **WordPress implementation** after handoff into Forge WordPress.

**Alignment:** Semantics mirror [website-factory-validation-architecture-charter-v1.md](../../website-factory-validation-architecture-charter-v1.md) — blocking layers, evidence model, false-green closure — without merging VL and WV identifiers.

**Honesty:** Documented gates only — **not** automated enforcement product.

---

## 1. Planes

```text
PLANE 1 — WV0–WV9          WordPress implementation validation
PLANE 2 — Factory VL0–VL6  Upstream frontend (prerequisite — not re-run as WV)
PLANE 3 — Production mode  PIXEL_PERFECT | TEMPLATE_ART (inherited from Factory)
PLANE 4 — Human control    Operator acceptance — see human control model
```

**Rule:** Factory **PRODUCTION PASS** on frontend does **not** imply WordPress **RELEASE READY**.

---

## 2. WV layer registry

### WV0 — Input completeness

| Attribute | Definition |
|-----------|------------|
| **Scope** | FWP-01–02 artifacts; handoff manifest; passport fields |
| **Automated** | Manifest schema check (future) |
| **Validator** | Completeness checklist |
| **Human** | Operator confirms intake |
| **Blocking** | Missing handoff; missing production mode |
| **Report** | `WV0-INPUT-COMPLETENESS-REPORT` |

---

### WV1 — Architecture compliance

| Attribute | Definition |
|-----------|------------|
| **Scope** | WAD vs implementation; mode rules; theme/plugin boundary |
| **Automated** | — |
| **Validator** | Forge WordPress Architect (independent if implementer different) |
| **Human** | WAD compliance sign-off |
| **Blocking** | Mode violation; CPT in theme; builder as primary |
| **Report** | `WV1-ARCHITECTURE-COMPLIANCE-REPORT` |

---

### WV2 — Code quality

| Attribute | Definition |
|-----------|------------|
| **Scope** | PHPCS/WPCS; project ruleset; PHP syntax |
| **Automated** | PHPCS runner (FW-03) |
| **Validator** | WordPress Validator |
| **Human** | Waiver on non-critical sniff |
| **Blocking** | Critical WPCS security sniffs fail |
| **Report** | `WV2-CODE-QUALITY-REPORT` |

---

### WV3 — WordPress correctness

| Attribute | Definition |
|-----------|------------|
| **Scope** | Template hierarchy; hooks; enqueue; block registration; ACF sync |
| **Automated** | PHPUnit sample; `assertEqualHTML` where used (future) |
| **Validator** | WordPress Validator |
| **Human** | Functional spot-check |
| **Blocking** | Broken templates; ACF JSON out of sync |
| **Report** | `WV3-WORDPRESS-CORRECTNESS-REPORT` |

---

### WV4 — Security

| Attribute | Definition |
|-----------|------------|
| **Scope** | Sanitize/escape/nonces/capabilities; plugin vulnerability scan; dependency audit |
| **Automated** | PHPCS security sniffs; WPScan candidate |
| **Validator** | Security Reviewer |
| **Human** | Plugin approval |
| **Blocking** | Known vulnerable plugin; missing capability checks |
| **Report** | `WV4-SECURITY-REPORT` |

---

### WV5 — Functional QA

| Attribute | Definition |
|-----------|------------|
| **Scope** | Forms, navigation, CPT archives, search, admin publish flow |
| **Automated** | Playwright smoke (future) |
| **Validator** | WordPress Validator |
| **Human** | Editorial walkthrough |
| **Blocking** | Critical user path broken |
| **Report** | `WV5-FUNCTIONAL-QA-REPORT` |

---

### WV6 — Visual parity

| Attribute | Definition |
|-----------|------------|
| **Scope** | Frontend reference vs WordPress render |
| **Automated** | Screenshot diff / Playwright `toHaveScreenshot` (future) |
| **Validator** | Visual Parity Validator |
| **Human** | **Operator visual approval** (PIXEL_PERFECT — mandatory) |
| **Blocking** | Undocumented parity failure (PIXEL_PERFECT) |
| **Report** | `VISUAL-QA-REPORT` (artifact model) |

---

### WV7 — Admin UX

| Attribute | Definition |
|-----------|------------|
| **Scope** | Editable regions map compliance; editor restrictions; ACF UX |
| **Automated** | — |
| **Validator** | Admin UX Specialist |
| **Human** | Client editor simulation |
| **Blocking** | Unauthorized editable surface; missing locks |
| **Report** | `WV7-ADMIN-UX-REPORT` |

---

### WV8 — Performance and accessibility

| Attribute | Definition |
|-----------|------------|
| **Scope** | Lighthouse baseline; axe checks — **deferred tooling** |
| **Automated** | FW-03 |
| **Validator** | WordPress Validator |
| **Human** | Waiver for shared hosting constraints |
| **Blocking** | Critical a11y failure (charter TBD FW-02) |
| **Report** | `WV8-PERF-A11Y-REPORT` |

---

### WV9 — Packaging and handoff

| Attribute | Definition |
|-----------|------------|
| **Scope** | RELEASE-MANIFEST; ZIP integrity; WPILOT-HANDOFF completeness |
| **Automated** | Manifest linter (future) |
| **Validator** | WPilot Handoff Reviewer |
| **Human** | **BLOCKING** handoff acceptance |
| **Blocking** | Missing WV reports; credential in package |
| **Report** | `WV9-PACKAGING-HANDOFF-REPORT` |

---

## 3. WV flow

```text
WV0 → WV1 (post-design) → [implementation] → WV2–WV5 → WV6–WV7 → WV8 → WV9
```

Parallel allowed: WV2+WV3 after implementation; WV6+WV7 before WV9.

---

## 4. Factory VL crosswalk

| Factory VL | Relationship to WV |
|------------|-------------------|
| VL0–VL6 | **Prerequisite** — must be complete before Forge FWP-01 |
| VL6 PRODUCTION PASS | Frontend handoff eligibility — **not** WordPress release |
| Operator visual approval | Required upstream for PIXEL_PERFECT; **repeated** at WV6 for WP render |

---

## 5. False-green closure

| Anti-pattern | Closure |
|--------------|---------|
| PHPCS pass but visual fail | WV6 blocks despite WV2 pass |
| Local works; ACF JSON not committed | WV3 blocks |
| TECHNICAL PASS without operator | WV6/WV9 require human sign-off |
| Frontend PASS assumed for WP | Explicit WV0 handoff check |

---

## Related documents

- [FORGE-WORDPRESS-PROJECT-LIFECYCLE-v1.md](FORGE-WORDPRESS-PROJECT-LIFECYCLE-v1.md) FWP-08–09
- [website-factory-validation-architecture-charter-v1.md](../../website-factory-validation-architecture-charter-v1.md)

---

*Validation architecture v1 — WV separate from VL; not runtime.*
