# Forge WordPress — Implementation Modes v1

**Document type:** Methodological mode registry  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-01

**Principle:** Modes describe **methodology**, not a single stack for all projects. **Page builders are not the Factory-native default path.**

---

## 1. Mode overview

| Mode | Label | Factory-native default? |
|------|-------|-------------------------|
| **A** | Factory-native custom implementation | **Yes** — default for new Factory frontend projects |
| **B** | Hybrid WordPress implementation | Allowed when WAD justifies |
| **C** | Legacy integration | Exception path — existing sites only |
| **D** | Specialized implementation | Charter-only |

---

## 2. Mode A — Factory-native custom implementation

| Attribute | Definition |
|-----------|------------|
| **Use case** | New project with **approved** Website Factory frontend (Gulp build); corporate/marketing sites; PIXEL_PERFECT or TEMPLATE_ART upstream. |
| **Allowed architecture** | Classic or hybrid theme carrying Factory HTML/CSS/JS; functionality plugin for CPT/taxonomies/ACF registrations; ACF as **preferred** content layer; selective ACF Blocks or PHP templates — per-section decision in WAD. |
| **Input requirements** | Factory VL6-complete frontend handoff; reproducible `npm run build`; block inventory; production mode declared. |
| **Restrictions** | No Elementor/WPBakery/The7 as primary implementation surface; no headless; no undeclared third-party builder dependency. |
| **Website Factory compatibility** | **Full** — designed for this path. |
| **WPilot compatibility** | **High** — aligns with Factory-native WordPress target in WPilot docs (handoff contract FW-02). |
| **Validation requirements** | WV6 visual parity weighted by `PIXEL_PERFECT`; WV7 admin UX; full WV chain. |
| **Entry gate** | FWP-02 Frontend Readiness PASS |
| **Exit gate** | FWP-11 WPilot Handoff approved |

---

## 3. Mode B — Hybrid WordPress implementation

| Attribute | Definition |
|-----------|------------|
| **Use case** | Factory frontend for shell/marketing pages; blog/news or repeatable sections reasonably served by Gutenberg patterns, core blocks, or ACF Blocks. |
| **Allowed architecture** | Hybrid theme; `theme.json` where beneficial; ACF Blocks bridge; Block Bindings for dynamic core blocks; functionality plugin for portable logic. |
| **Input requirements** | Mode A inputs + explicit hybrid justification in WAD (which sections are block-editor-owned). |
| **Restrictions** | Hybrid scope must be **bounded** in editable-regions map; no whole-site block-theme rewrite unless WAD approves; editor freedom only where chartered. |
| **Website Factory compatibility** | **Partial** — Factory assets remain SoT for branded shell; block zones documented separately. |
| **WPilot compatibility** | **Medium** — requires frozen block patterns and stricter handoff manifest. |
| **Validation requirements** | WV1 architecture compliance for hybrid matrix; WV6 for Factory-sourced sections; WV7 for editor surfaces. |
| **Entry gate** | WAD declares Mode B + section map |
| **Exit gate** | FWP-11 with hybrid manifest annex |

---

## 4. Mode C — Legacy integration

| Attribute | Definition |
|-----------|------------|
| **Use case** | Existing sites on The7, WPBakery, Elementor, or other legacy builder; incremental Factory frontend integration or template replacement. |
| **Allowed architecture** | Child theme or scoped template overrides; minimal functionality plugin; **no** full Factory-native rewrite without separate charter. |
| **Input requirements** | Legacy site audit; plugin inventory; hosting constraints; explicit **non-goals** for full parity. |
| **Restrictions** | Builders remain **legacy surface** — not promoted to Factory standard; Forge WordPress does not own builder license/vendor roadmap; reduced visual parity scope must be documented. |
| **Website Factory compatibility** | **Limited** — partial frontend packages only. |
| **WPilot compatibility** | **Variable** — operations may already run on legacy stack; handoff is **operational patch** not greenfield package. |
| **Validation requirements** | Reduced WV6 scope per WAD; WV4 security elevated; regression on legacy plugin set. |
| **Entry gate** | Legacy audit + operator charter |
| **Exit gate** | Scoped handoff — not full RELEASE-MANIFEST equivalence |

---

## 5. Mode D — Specialized implementation

| Attribute | Definition |
|-----------|------------|
| **Use case** | WooCommerce; multisite; multilingual (WPML/Polylang); headless (Next.js + WP API); complex CRM/ERP integrations. |
| **Allowed architecture** | **Charter-defined only** — not inferable from FW-01. |
| **Input requirements** | Separate FW charter; specialist reviewer; extended plugin register. |
| **Restrictions** | **Not** default for FP-0002 or Factory pilots; no Mode D without written charter. |
| **Website Factory compatibility** | **Case-by-case** — often partial frontend only. |
| **WPilot compatibility** | **Case-by-case** — may exceed current WPilot RC5 proven surface. |
| **Validation requirements** | Extended validation plan — FW-02+ standards. |
| **Entry gate** | Dedicated charter approved |
| **Exit gate** | Charter-defined |

---

## 6. Mode selection matrix (summary)

| Criterion | Mode A | Mode B | Mode C | Mode D |
|-----------|--------|--------|--------|--------|
| Visual fidelity to Factory frontend | Primary | Split zones | Reduced | Charter |
| Editor needs | Curated ACF | + block zones | Legacy builder | Charter |
| Content reuse / portability | High | Medium–High | Low | Charter |
| Project complexity | Low–Medium | Medium | High (legacy debt) | Very high |
| Shared hosting fit | **Good** | Good | Variable | Variable |
| Maintenance | Factory-aligned | Moderate | Higher | Charter |
| WPilot compatibility | **High** | Medium | Variable | Unknown |
| Team competence required | Factory + WP classic | + block editor | + legacy stack | Specialists |

**Default:** Mode A unless WAD documents otherwise.

---

## 7. Builders policy (explicit)

| Builder class | FW-01 status |
|---------------|--------------|
| Elementor / WPBakery / Divi / The7 native | **REJECT** as Factory-native primary path — Mode C only |
| ACF Blocks | **ADOPT** as hybrid bridge (Mode A/B) |
| Core Gutenberg / patterns | **ADOPT** selectively (Mode B) |
| Full block theme (FSE) | **ADAPT** — per-project WAD; not global default |

---

## 8. Related documents

- [FORGE-WORDPRESS-ARCHITECTURAL-DECISIONS-v1.md](FORGE-WORDPRESS-ARCHITECTURAL-DECISIONS-v1.md) §4.2
- [FORGE-WORDPRESS-ARCHITECTURE-v1.md](FORGE-WORDPRESS-ARCHITECTURE-v1.md) L3

---

*Implementation modes v1 — methodological registry only.*
