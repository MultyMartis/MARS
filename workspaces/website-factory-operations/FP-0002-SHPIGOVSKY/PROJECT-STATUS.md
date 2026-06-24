# FP-0002 — Project Status

**Factory Project:** FP-0002 — Shpigovsky.ru  
**Last updated:** 2026-06-24 (V7 Package #001 Phase 3C)

## Workspace versions (2026-06-24)

| Workspace | Path | Lifecycle | Tag / parent |
|-----------|------|-----------|--------------|
| **V6** | `workspaces/fp-0002-shpigovsky-v6/` | **FROZEN_FALLBACK** | `fp-0002-v6-final-before-v7-operator-stable-01` |
| **V7** | `workspaces/fp-0002-shpigovsky-v7/` | **ACTIVE_DEVELOPMENT** | Parent: V6 final stable |

```text
V7 design authority: workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/Spig_v1.2.fig
V7 design authority SHA-256: BAE5D91C74B5A22AFC610F7C7845B9BADC6B87EC8DA85C5705ECF4EEC4DE3041
Historical Figma (Шпиговский.fig): DO NOT USE FOR NEW WORK
Factory Figma rules: projects/mars-website-factory/figma-inspection-authority-rules-v1.md
package_001: IN_PROGRESS
package_001_phase_1_figma_rules: COMPLETE
package_001_phase_2_head: COMPLETE_PENDING_OPERATOR_REVIEW
package_001_phase_3a_intro_content: COMPLETE_PENDING_OPERATOR_REVIEW
package_001_phase_3b_founder_quote_svg: COMPLETE_PENDING_OPERATOR_REVIEW
package_001_phase_3b_gallery_captions: COMPLETE_PENDING_OPERATOR_REVIEW
package_001_phase_3c_recovery_life: COMPLETE_PENDING_OPERATOR_REVIEW
new_recovery_block: COMPLETE_PENDING_OPERATOR_REVIEW
section_spacing_cleanup: NOT_STARTED
global_visual_polish: NOT_STARTED
```

## Milestone (2026-06-23)

**FP-0002 WORDPRESS FOUNDATION CLOSURE (FW-06A.1)** — local runtime `shpigovsky.test` validated: direct domain PASS, `wp db check` PASS, Playwright foundation smoke PASS. Theme integration **LOCKED** until Frontend Production Pass and FW-06B.

## MLI-03R.1 post-reboot (2026-06-24)

After full Windows reboot, MySQL datadir/config drift broke DB connectivity. Remediation restored authoritative `my.ini`, loopback binding, and X Protocol disable. **No reinstall, no DB recreate, no password rotation.**

```text
FP-0002 WordPress foundation:
READY — POST-REBOOT VALIDATED

Evidence:
wp db check PASS; HTTP 200; Playwright 5/5; controlled MySQL restart PASS
Report: projects/mars-localhost-infrastructure/reports/MARS-LOCALHOST-MLI-03R1-MYSQL-8.4-AUTHENTICATION-REMEDIATION-v1.md
```

---

## Phase

| Field | Value |
|-------|-------|
| **Phase** | **Foundation** |

---

## Website Factory status

| Field | Value |
|-------|-------|
| **Website Factory Status** | **Pre-Onboarding** |

Manifest enrollment (Playbook 01), registry enrollment (Playbook 02), and RT-G04 substrate (POC-01…POC-10) are **not started** for FP-0002.

---

## Production lanes

| Lane | Status |
|------|--------|
| **Frontend** | **V7 ACTIVE_DEVELOPMENT** — Package #001 Phase 3C complete pending operator review (recovery-life section) |
| **WordPress** | **Foundation READY — POST-REBOOT VALIDATED (MLI-03R.1)** — local runtime `shpigovsky.test`; theme integration **LOCKED** until Production Pass + FW-06B |
| **QA** | Not Started |
| **Delivery** | Not Started |

---

## Design and inventory

| Field | Value |
|-------|-------|
| **Design Materials** | Awaiting Intake |
| **Page Inventory** | **Updated** — `foundation/FP-0002-V6-PAGE-INVENTORY.md` in V6 workspace |
| **Block Inventory** | **Updated** — `reviews/services-page/reuse-only/FP-0002-HOME-BLOCK-INVENTORY-v1.md` |

---

## Services page status

| Field | Value |
|-------|-------|
| `services_foundation` | COMPLETE |
| `services_rejected_unique_implementation` | REVERTED (`25bfbce`) |
| `services_reuse_matrix` | COMPLETE |
| `services_page_mode` | REUSE_ONLY |
| `services_exact_reused_blocks` | header, program, founder, comfort, FAQ, final form, footer, modal |
| `services_new_unique_blocks` | 0 |
| `services_unimplemented_blocks` | hero, addictions, mental-health, eating-disorders |
| `services_unique_blocks` | REJECTED_AND_REVERTED |

---

## ATLAS linkage

| Check | Status |
|-------|--------|
| PRJ-0012 attested | **Yes** — AT-W3-SHPIG-01 |
| WEB-SHPIG-01 attested | **Yes** — AT-W4-SHPIG-01 |
| DOM-SHPIG-01 attested | **Yes** — AT-W5-SHPIG-01 |
| ORG-0008 attested | **Yes** — AT-W1D-SHPIG-01 |
| Factory manifest bind | **No** — pending onboarding |

---

## Intake

| Intake area | Status |
|-------------|--------|
| Structure | **Ready** — INCOMING/ scaffold created |
| Design materials | **Empty** — awaiting client/operator intake |
| Content | **Empty** |
| Access / hosting | **Empty** |

---

## Next gate

**Package #001 Phase 2** — head/favicon/OG implemented; operator review for SEO copy and OG asset. Content migration and visual polish phases not started.

---

*Status register only. Not a runtime state store.*
