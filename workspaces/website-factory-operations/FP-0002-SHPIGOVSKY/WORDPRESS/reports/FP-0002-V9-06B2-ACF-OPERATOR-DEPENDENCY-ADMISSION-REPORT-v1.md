# FP-0002 V9-06B.2 ACF Operator Dependency Admission Report v1

**Date:** 2026-07-04  
**Mode:** read-only audit and repository documentation/evidence only  
**Runtime mutations:** 0  
**Database writes:** 0  
**Plugin file changes:** 0  
**V9-06C authorization:** NO

## Safety Preflight

| Field | Value |
|---|---|
| Volume | X: |
| Label | AI WS |
| Repository | X:\AI MARS |
| Branch | mars/canonical-post-recovery |
| Starting HEAD | recorded in final operator report |
| Pre-existing staged files | none |
| Foreign WIP | present outside V9-06B.2 scope; excluded from staging |

## Runtime Identity

| Field | Value |
|---|---|
| Runtime | X:\MARS-Localhost\sites\wordpress\projects\shpigovsky |
| Domain | http://shpigovsky.test |
| Theme | shpigovsky |
| Shpigovsky Core | shpigovsky-core/shpigovsky-core.php 0.1.0 active |
| WPilot | metacode-wpilot/metacode-wpilot.php 0.3.0 active |
| WPilot write_enabled | False |
| Frontend HTTP | 200 |
| wp-admin HTTP | 200 |

## Plugin Inventory

| Plugin | Basename | Version | Status | Classification | Update policy |
|---|---|---:|---|---|---|
| Advanced Custom Fields | advanced-custom-fields/acf.php | 6.8.4 | inactive | INACTIVE_LEGACY_OR_FALLBACK_PLUGIN | DO_NOT_UPDATE_IN_THIS_TASK |
| Advanced Custom Fields PRO | advanced-custom-fields-pro/acf.php | 6.8.5 | active | OPERATOR_MANAGED_EXTERNAL_DEPENDENCY | ALWAYS_IGNORE_FOR_AUTOMATED_UPDATES |
| Advanced Custom Fields: Extended PRO | acf-extended-pro/acf-extended.php | 0.9.2.3 | active | OPERATOR_MANAGED_EXTERNAL_DEPENDENCY | ALWAYS_IGNORE_FOR_AUTOMATED_UPDATES |
| MetaCODE WPilot | metacode-wpilot/metacode-wpilot.php | 0.3.0 | active | PROJECT_RUNTIME_PLUGIN | MANUAL_POLICY_ONLY |
| Shpigovsky Core | shpigovsky-core/shpigovsky-core.php | 0.1.0 | active | PROJECT_PLUGIN | SOURCE_CONTROLLED_SEPARATELY |

## ACF PRO Capability

| Capability | Available | Method | Result |
|---|---:|---|---|
| ACF API | True | function_exists(acf) | PASS |
| PRO marker/version | True | ACF_PRO/function/options-page marker | PASS |
| Repeater | True | acf_get_field_type(repeater)/class_exists | PASS |
| Options Page | True | function_exists(acf_add_options_page) | PASS |
| Relationship | True | acf_get_field_type(relationship)/class_exists | PASS |
| Gallery | True | acf_get_field_type(gallery)/class_exists | PASS |
| ACF JSON filters | True | WordPress filter API available for acf/settings filters | PASS |
| Local JSON path support | True | acf_get_setting or ACF_Local_JSON class | PASS |
| get_field | True | function_exists(get_field) | PASS |
| update_field | True | function_exists(update_field), not called | PASS |
| acf_add_local_field_group | True | function_exists(acf_add_local_field_group), not called | PASS |

Result: **SUFFICIENT**.

## ACF Free Conflict

- Installed: True
- Active: False
- Loaded: False
- Conflict: False
- Recommendation: KEEP_INACTIVE_DO_NOT_ACTIVATE_DO_NOT_DELETE_DO_NOT_AUTO_UPDATE
- Result: INACTIVE_NOT_USED

## ACF Extended PRO Audit

- Installed: True
- Active: True
- Version: 0.9.2.3
- Adds field types: True
- Adds admin UI: True
- Adds REST/API behavior: True
- Alters ACF JSON: True
- Required for FP-0002: False
- Risk: REVIEW_REQUIRED
- Recommendation: KEEP_ACTIVE_BUT_NOT_USED
- Result: CLASSIFIED_SEPARATELY

## File Integrity Baseline

| Plugin | Files | PHP files | JS files | Aggregate hash | Manifest |
|---|---:|---:|---:|---|---|
| Advanced Custom Fields PRO | 705 | 336 | 21 | 62dcbd1c1fb556b77ecf460f624c9c85dbf8165d2c3c40ea3028458c91308c42 | WORDPRESS/validation/v9-06b2-acf-admission/acf-pro-file-manifest.json |
| Advanced Custom Fields: Extended PRO | 612 | 519 | 36 | ac614f38670ec9c272ed8a39d52a6cc39d54899a5d1268a6714d73f9e4ff78aa | WORDPRESS/validation/v9-06b2-acf-admission/acf-extended-pro-file-manifest.json |

## Suspicious Pattern Scan

| Plugin | BENIGN_EXPECTED | REVIEW_REQUIRED | HIGH_RISK | BLOCKER | Result |
|---|---:|---:|---:|---:|---|
| Advanced Custom Fields PRO | 183 | 364 | 0 | 0 | REVIEW_REQUIRED |
| Advanced Custom Fields: Extended PRO | 201 | 574 | 0 | 0 | REVIEW_REQUIRED |

### Review-Required Pattern Summary

| Plugin | Pattern | Count | Classification | Note |
|---|---|---:|---|---|
| Advanced Custom Fields PRO | base64_decode | 3 | REVIEW_REQUIRED | Static vendor-context review; no HIGH_RISK/BLOCKER classification. |
| Advanced Custom Fields PRO | cron_creation | 2 | REVIEW_REQUIRED | Static vendor-context review; no HIGH_RISK/BLOCKER classification. |
| Advanced Custom Fields PRO | eval | 2 | REVIEW_REQUIRED | Static vendor-context review; no HIGH_RISK/BLOCKER classification. |
| Advanced Custom Fields PRO | external_url | 357 | REVIEW_REQUIRED | Static vendor-context review; no HIGH_RISK/BLOCKER classification. |
| Advanced Custom Fields: Extended PRO | curl_exec | 4 | REVIEW_REQUIRED | Static vendor-context review; no HIGH_RISK/BLOCKER classification. |
| Advanced Custom Fields: Extended PRO | exec | 8 | REVIEW_REQUIRED | Static vendor-context review; no HIGH_RISK/BLOCKER classification. |
| Advanced Custom Fields: Extended PRO | external_url | 559 | REVIEW_REQUIRED | Static vendor-context review; no HIGH_RISK/BLOCKER classification. |
| Advanced Custom Fields: Extended PRO | passthru | 2 | REVIEW_REQUIRED | Static vendor-context review; no HIGH_RISK/BLOCKER classification. |
| Advanced Custom Fields: Extended PRO | wp_insert_user | 1 | REVIEW_REQUIRED | Static vendor-context review; no HIGH_RISK/BLOCKER classification. |

## Operator-Managed Registry

- Registry MD: WORDPRESS/architecture/FP-0002-OPERATOR-MANAGED-EXTERNAL-PLUGINS-v1.md
- Registry JSON: WORDPRESS/architecture/FP-0002-OPERATOR-MANAGED-EXTERNAL-PLUGINS-v1.json
- ACF PRO: ADMITTED; use allowed after admission.
- ACF Extended PRO: classified separately; keep active but not used.
- ACF Free: inactive fallback; not used while PRO active.

## V9-06C Readiness

- ACF PRO: READY_FOR_V9_06C
- ACF Extended PRO: NOT_REQUIRED_FOR_V9_06C
- ACF Free: INACTIVE_NOT_USED
- ACF JSON: CAN_BE_INTEGRATED_LATER_WITH_CANONICAL_WORDPRESS_ACF_JSON_PATH
- Field implementation path: V9-06C may write canonical ACF JSON/groups only after separate operator authorization
- Blockers: 
- Result: READY FOR OPERATOR AUTHORIZATION

## Validation

| Field | Value |
|---|---:|
| Total checks | 13 |
| Passed | 13 |
| Failed | 0 |
| Result | PASS |

## Final Verdict

PASS

V9-06B.2: COMPLETE  
ACF PRO: ADMITTED  
ACF PRO use: ALLOWED  
ACF PRO update policy: ALWAYS_IGNORE  
ACF PRO delivery policy: FORBIDDEN  
ACF Extended PRO: CLASSIFIED  
ACF Extended PRO use: NOT APPROVED  
ACF Extended PRO update policy: ALWAYS_IGNORE  
ACF Free: INACTIVE_NOT_USED  
Operator-managed dependency registry: CREATED  
Security scan: REVIEW_REQUIRED  
Runtime mutations: 0  
Database writes: 0  
Plugin files changed: 0  
V9-06C: READY FOR OPERATOR AUTHORIZATION
