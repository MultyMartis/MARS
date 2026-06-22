# Forge WordPress Validation Standard v1

**Document type:** Operational validation standard  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-02  
**Source:** [FORGE-WORDPRESS-VALIDATION-ARCHITECTURE-v1.md](../FORGE-WORDPRESS-VALIDATION-ARCHITECTURE-v1.md)

**Honesty:** Documented gates — automation candidates deferred to FW-03.

---

## 1. Orthogonality

| Plane | Scope |
|-------|-------|
| **WV0–WV9** | WordPress implementation |
| **VL0–VL6** | Upstream Factory frontend — prerequisite, not re-run as WV |
| **Production mode** | `PIXEL_PERFECT` \| `TEMPLATE_ART` — inherited |
| **Human control** | Operator sign-off at WV6, WV9 |

**Rule:** Factory PRODUCTION PASS ≠ WordPress RELEASE READY.

---

## 2. WV layer operationalization

### WV0 — Input completeness

| Attribute | Value |
|-----------|-------|
| **Purpose** | Verify FWP-01–02 artifacts and B1 handoff |
| **Mandatory checks** | Handoff manifest; production_mode; page/block inventory; operator approval |
| **Optional checks** | ATLAS bindings |
| **Automation candidate** | Manifest schema linter (FW-03) |
| **Human check** | Operator confirms intake |
| **Blocking** | Missing handoff; missing production mode |
| **Report** | `WV0-INPUT-COMPLETENESS-REPORT` |

---

### WV1 — Architecture compliance

| Attribute | Value |
|-----------|-------|
| **Purpose** | WAD vs implementation; mode rules; theme/plugin boundary |
| **Mandatory checks** | Mode compliance; no CPT in theme; no builder primary (Mode A); FUNCTIONALITY-BOUNDARY |
| **Optional checks** | Hybrid matrix (Mode B) |
| **Automation candidate** | — |
| **Human check** | Architect sign-off |
| **Blocking** | R-TF-02 violation; Flexible Content as page builder |
| **Report** | `WV1-ARCHITECTURE-COMPLIANCE-REPORT` |

---

### WV2 — Code quality

| Attribute | Value |
|-----------|-------|
| **Purpose** | PHPCS/WPCS; PHP syntax |
| **Mandatory checks** | PHPCS run; critical sniffs |
| **Optional checks** | Full ruleset; PHPStan (FW-03) |
| **Automation candidate** | PHPCS runner |
| **Human check** | Waiver on non-critical sniff |
| **Blocking** | Critical WPCS security sniffs |
| **Report** | `WV2-CODE-QUALITY-REPORT` |

---

### WV3 — WordPress correctness

| Attribute | Value |
|-----------|-------|
| **Purpose** | Templates, hooks, enqueue, ACF sync |
| **Mandatory checks** | Template hierarchy; ACF JSON sync; enqueue order |
| **Optional checks** | PHPUnit smoke |
| **Automation candidate** | ACF sync diff |
| **Human check** | Spot-check archives, singles |
| **Blocking** | Broken templates; JSON out of sync |
| **Report** | `WV3-WORDPRESS-CORRECTNESS-REPORT` |

---

### WV4 — Security

| Attribute | Value |
|-----------|-------|
| **Purpose** | Escape/sanitize/nonces; plugin security |
| **Mandatory checks** | Coding standard §7 blocking set; plugin register complete |
| **Optional checks** | WPScan; dependency audit (FW-03) |
| **Automation candidate** | PHPCS security sniffs |
| **Human check** | Plugin approval |
| **Blocking** | Vulnerable plugin; missing capability checks |
| **Report** | `WV4-SECURITY-REPORT` |

---

### WV5 — Functional QA

| Attribute | Value |
|-----------|-------|
| **Purpose** | User paths work |
| **Mandatory checks** | Navigation; forms submit; CPT archives; search; admin publish |
| **Optional checks** | Playwright smoke (FW-03) |
| **Automation candidate** | Playwright |
| **Human check** | Editorial walkthrough |
| **Blocking** | Critical path broken |
| **Report** | `WV5-FUNCTIONAL-QA-REPORT` |

---

### WV6 — Visual parity

| Attribute | Value |
|-----------|-------|
| **Purpose** | Factory frontend authority vs WordPress render |
| **Mandatory checks** | Page-by-page comparison; known deviations documented |
| **Optional checks** | Screenshot diff (FW-03) |
| **Automation candidate** | Playwright `toHaveScreenshot` |
| **Human check** | **Operator visual approval** — mandatory PIXEL_PERFECT |
| **Blocking** | Undocumented parity failure (PIXEL_PERFECT) |
| **Report** | `VISUAL-QA-REPORT` |

**Factory authority:** Frontend reference = approved Factory commit/dist. Operator approval at Factory VL6 does **not** replace WV6 WP render approval.

---

### WV7 — Admin UX

| Attribute | Value |
|-----------|-------|
| **Purpose** | Curated editor compliance |
| **Mandatory checks** | ADMIN-UX-MAP; checklist §9; editor simulation |
| **Optional checks** | — |
| **Automation candidate** | — |
| **Human check** | Client editor simulation |
| **Blocking** | Unauthorized editable surface; missing locks |
| **Report** | `WV7-ADMIN-UX-REPORT` |

---

### WV8 — Performance and accessibility

| Attribute | Value |
|-----------|-------|
| **Purpose** | Baseline perf/a11y |
| **Mandatory checks** | Project-profile defined checks |
| **Optional checks** | Lighthouse; axe (FW-03) |
| **Automation candidate** | Lighthouse CI; axe-playwright |
| **Human check** | Waiver for hosting constraints |
| **Blocking** | **SAFE UNKNOWN** — critical a11y threshold deferred to project profile or FW-03 |
| **Report** | `WV8-PERF-A11Y-REPORT` |

**Threshold policy:** Not fixed in FW-02. Define per project in VALIDATION-PLAN or leave **SAFE UNKNOWN** until FW-03 tooling design.

---

### WV9 — Packaging and handoff

| Attribute | Value |
|-----------|-------|
| **Purpose** | RELEASE-MANIFEST; B3 package |
| **Mandatory checks** | Manifest complete; no credentials; WV reports attached; WPILOT-HANDOFF |
| **Optional checks** | ZIP integrity hash |
| **Automation candidate** | Manifest linter |
| **Human check** | **BLOCKING** G10 handoff acceptance |
| **Blocking** | Missing WV reports; credential in package |
| **Report** | `WV9-PACKAGING-HANDOFF-REPORT` |

---

## 3. Validation flow

```text
WV0 → WV1 (post-WAD) → [implementation] → WV2+WV3 → WV4 → WV5 → WV6+WV7 → WV8 → WV9
```

Parallel: WV2+WV3; WV6+WV7 before WV9.

---

## 4. False-green closure

| Anti-pattern | Closure layer |
|--------------|---------------|
| PHPCS pass, visual fail | WV6 blocks |
| Local works, JSON not committed | WV3 blocks |
| TECHNICAL PASS without operator | WV6/WV9 require human |
| Frontend PASS assumed for WP | WV0 explicit check |

---

## 5. Production mode matrix

| Mode | WV6 weight | WV8 weight |
|------|------------|------------|
| **PIXEL_PERFECT** | Blocking — operator mandatory | Project profile |
| **TEMPLATE_ART** | Documented deviations allowed | Project profile |

---

## Related documents

- [templates/FORGE-WORDPRESS-VALIDATION-REPORT-TEMPLATE-v1.md](../templates/FORGE-WORDPRESS-VALIDATION-REPORT-TEMPLATE-v1.md)
- [website-factory-validation-architecture-charter-v1.md](../../../website-factory-validation-architecture-charter-v1.md)

---

*Validation standard v1 — WV0–WV9 operationalized.*
