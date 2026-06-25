# AG-WP-001 — Execution Workflow v1

**Document type:** Execution workflow  
**Version:** v1  
**Stage:** FW-07A  
**Date:** 2026-06-24

---

## Sequence overview

```text
0. Intake
1. Input validation
2. Runtime validation
3. Frontend inspection
4. Architecture proposal
5. Operator architecture approval
6. WordPress scaffolding
7. Content model implementation
8. Theme implementation
9. Functionality implementation
10. Plugin integration
11. Automated QA
12. Visual QA
13. Operator review
14. Corrections
15. Acceptance gate
16. Handoff
17. Freeze/checkpoint
```

---

## Phase detail

### 0. Intake

| Item | Detail |
|------|--------|
| Inputs | Project ID, operator task, FW phase authorization |
| Operations | `inspect_frontend_handoff` (preliminary) |
| Outputs | Intake log |
| Approval | Operator task acceptance |
| Rollback | N/A |
| Stop | FW-06B not authorized for integration |

### 1. Input validation

| Item | Detail |
|------|--------|
| Inputs | Full input contract fields |
| Operations | `inspect_frontend_handoff` |
| Outputs | Gate A report |
| Approval | Auto pass/fail; fail → stop |
| Rollback | N/A |
| Stop | Gate A failure |

### 2. Runtime validation

| Item | Detail |
|------|--------|
| Inputs | MLI runtime manifest |
| Operations | `inspect_wp_runtime` |
| Outputs | Environment validation report |
| Approval | R0 pre-authorized |
| Rollback | N/A |
| Stop | Wrong runtime, missing profile |

### 3. Frontend inspection

| Item | Detail |
|------|--------|
| Inputs | Approved commit checkout |
| Operations | `inspect_assets`, `inspect_forms`, `inspect_routes` |
| Outputs | Inspection report, block map draft |
| Approval | R0 |
| Stop | Source authority ambiguous |

### 4. Architecture proposal

| Item | Detail |
|------|--------|
| Operations | `draft_implementation_plan`, `draft_theme_architecture`, `draft_functionality_architecture`, `draft_content_model`, `draft_plugin_decision`, `draft_editor_governance` |
| Outputs | REVIEWABLE architecture pack |
| Approval | R1 — human review required |
| Rollback | Discard drafts |

### 5. Operator architecture approval

| Item | Detail |
|------|--------|
| Outputs | OPERATOR APPROVED architecture |
| Approval | **Human mandatory** |
| Stop | Rejection → revise phase 4 |

### 6. WordPress scaffolding

| Item | Detail |
|------|--------|
| Operations | `scaffold_theme`, `scaffold_functionality_plugin`, `scaffold_tests` |
| Outputs | Skeleton source |
| Approval | R2 — plan approved + Git checkpoint |
| Rollback | Git revert |

### 7. Content model implementation

| Item | Detail |
|------|--------|
| Operations | `generate_acf_json`, `draft_content_model` (apply) |
| Outputs | Version-controlled field config |
| Approval | R2 |
| Rollback | Git + DB if R3 migration started |

### 8. Theme implementation

| Item | Detail |
|------|--------|
| Operations | `generate_template`, `generate_template_part`, `apply_approved_source_change` |
| Outputs | Theme source |
| Approval | R2 |
| Stop | FCR if frontend defect blocks parity |

### 9. Functionality implementation

| Item | Detail |
|------|--------|
| Operations | `apply_approved_source_change` |
| Outputs | Plugin source |
| Approval | R2 |

### 10. Plugin integration

| Item | Detail |
|------|--------|
| Operations | `inspect_plugin_state` (R0), activation (R3) |
| Outputs | Active set matches register |
| Approval | R3 for activation |
| Rollback | Plugin inventory restore |

### 11. Automated QA

| Item | Detail |
|------|--------|
| Operations | `validate_php_syntax`, `validate_wpcs`, `validate_routes`, `validate_security` |
| Outputs | Gate C/D/H reports |
| Approval | Pass or waiver |
| Stop | Blocker failures |

### 12. Visual QA

| Item | Detail |
|------|--------|
| Operations | `validate_visual_fidelity`, `validate_rendering` |
| Outputs | Gate F report |
| Approval | Operator waiver for documented deviations |

### 13. Operator review

| Item | Detail |
|------|--------|
| Operations | `prepare_review_package` |
| Outputs | Review bundle |
| Approval | Gate I |

### 14. Corrections

| Item | Detail |
|------|--------|
| Operations | Scoped R2 fixes |
| Outputs | Updated source + reports |
| Rollback | Per failure contract |

### 15. Acceptance gate

| Item | Detail |
|------|--------|
| Outputs | Gate J eligibility statement |
| Approval | Operator |

### 16. Handoff

| Item | Detail |
|------|--------|
| Outputs | WPilot handoff package (when chartered) |
| Approval | Operator |

### 17. Freeze/checkpoint

| Item | Detail |
|------|--------|
| Operations | `create_checkpoint` |
| Outputs | Git commit, tag optional |
| Approval | Operator |

---

*Execution workflow v1 — human gates at architecture and acceptance.*
