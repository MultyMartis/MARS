# Forge WordPress — Research Adaptation Register v1

**Document type:** Research → MARS rule traceability  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-01

**Source:** [AG-WP-001-GLOBAL-WORDPRESS-DEVELOPMENT-RESEARCH-v1.md](../../../../workspaces/website-factory-operations/internal-agent-seeds/AG-WP-001-forge-wordpress/research/AG-WP-001-GLOBAL-WORDPRESS-DEVELOPMENT-RESEARCH-v1.md) — **evidence only, not authority**.

---

## Register

| Research finding | Classification | MARS adaptation | Resulting rule | Confidence |
|------------------|----------------|-----------------|----------------|------------|
| Spec-first / plan-first | **ADOPT** | Align with Factory cross-layer pipeline; G5 spec gate | R-SPEC: no code before approved IMPLEMENTATION-SPEC | High |
| Plan-first (reviewable plan) | **ADOPT** | WAD + design package before L8 | FWP-03–06 gates | High |
| Sandbox-first | **ADOPT** | Windows local/DEV; no production agent | R-ENV-01–03 | High |
| Repository / project instructions | **ADOPT** | AGENTS.md + FW-02 coding standard; LOC-ZONE project docs | R-VC-*; subsystem pack as SoT | High |
| Worktree/branch isolation | **ADAPT** | Git branch per implementation; Cursor isolation — no mandatory worktree product | Human merge approval | Medium |
| Version-controlled content model | **ADOPT** | ACF Local JSON; CPT in plugin | R-ACF-01–02; R-TF-02 | High |
| Theme/functionality separation | **ADOPT** | Proportionality for simple sites | R-TF-01–03 | High |
| Curated editor | **ADOPT** | ADMIN-UX-MAP; default minimal edit surface | R-UX-01–04 | High |
| ACF Local JSON | **ADOPT** | Preferred layer when ACF used | R-ACF-02 | High |
| PHPCS/WPCS | **ADOPT** | WV2 required class | Tooling: PHPCS required (design) | High |
| Playwright E2E | **ADAPT** | WV5/WV6 candidate — FW-03 tooling | Deferred runner implementation | Medium |
| Visual regression | **ADOPT** | WV6; operator law for PIXEL_PERFECT | VISUAL-QA-REPORT blocking | High |
| Human merge / PR gate | **ADOPT** | MARS git discipline; no autonomous push | Human control: APPROVAL | High |
| Production credential boundary | **ADOPT** | WPilot precedent; no prod in Forge | PROHIBITED production access | High |
| Typed operations (Abilities API) | **DEFER** | Sandbox-only if FW-03+ | R-MCP-01 | Medium |
| WordPress MCP / Playground MCP | **DEFER** | Tooling FW-03 evaluation | DEV-ONLY if adopted | Low–Medium |
| WordPress Playground | **ADAPT** | Candidate local stack — not sole mandate | FW-03 selection | Medium |
| Block themes (FSE) | **ADAPT** | Per-project WAD; not Factory default | R-ARCH-02 | Medium |
| Page builders (Elementor, etc.) | **REJECT** as Factory-native | Mode C legacy only | Mode A/B builder ban | High |
| Headless WordPress | **REJECT** as default | Mode D charter only | Mode D gate | Medium |
| Enterprise tooling (VIP, Docker CI) | **ADAPT** | Patterns adopted; Docker not mandatory | Tooling: Docker DEFERRED | Medium |
| ACF as universal layer | **ADAPT** | **Preferred**, not mandatory | R-ACF-01–04 | Medium |
| Multi-step supervised pipeline | **ADOPT** | FWP lifecycle + architecture layers | Full FW-01 pack | High |
| Item-by-item surface selection | **ADOPT** | BLOCK-TO-WP-MAPPING required | FWP-05 artifact | High |
| Content model as separate artifact | **ADOPT** | FWP-04 before implementation | CONTENT-MODEL gate | High |
| Plugin governance / security scan | **ADOPT** | PLUGIN-REGISTER + WV4 | Security Reviewer role | High |
| `assertEqualHTML()` / PHPUnit | **ADAPT** | WV3 candidate — FW-03 | Optional PHP tests | Medium |
| AI-discoverable ACF (6.8+) | **DEFER** | Post-pilot agent tooling | Not FW-01 | Low |
| Interactivity API / Block Bindings | **ADAPT** | Mode B option | WAD per-section | Medium |
| DataForm/DataViews admin | **DEFER** | Complex admin plugins only | Admin UX standard FW-02 | Low |

---

## Rejected imports (compatibility failures)

| External practice | Rejection reason |
|-------------------|------------------|
| Autonomous production deploy | MARS human-supervised model |
| Builder-first bespoke | Factory Gulp ownership |
| Runtime agent in live admin | Security + WPilot split |
| Theme-embedded portable CPT | WordPress portability |

---

## Confidence notes

- **High:** Aligns with MARS governance + multiple research sources + existing Factory patterns.
- **Medium:** Valid externally; MARS tooling or pilot evidence pending.
- **Low–Medium:** Emerging WordPress APIs — defer until FW-03+.

---

## Related documents

- [FORGE-WORDPRESS-ARCHITECTURAL-DECISIONS-v1.md](FORGE-WORDPRESS-ARCHITECTURAL-DECISIONS-v1.md)
- [FORGE-WORDPRESS-RESEARCH-REGISTER-v1.md](FORGE-WORDPRESS-RESEARCH-REGISTER-v1.md)

---

*Research adaptation register v1 — traceability only.*
