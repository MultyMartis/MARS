# FP-0002 Operator-Managed External Plugins v1

**Task:** FP-0002 V9-06B.2  
**Date:** 2026-07-04  
**Scope:** Installed ACF plugin admission; no install/update/delete/license action.

## Policy

Operator-managed external plugins are excluded from automatic plugin updates, bulk plugin update tasks, dependency refresh tasks, filesystem delivery, replacement from Git source, cleanup/deletion, mutating security hardening, and unattended remediation.

Any mutation requires explicit operator authorization naming the exact plugin and exact operation.

| Plugin | Basename | Version | Status | Classification | Use | Update policy | Delivery |
|---|---|---:|---|---|---|---|---|
| Advanced Custom Fields PRO | advanced-custom-fields-pro/acf.php | 6.8.5 | active | OPERATOR_MANAGED_EXTERNAL_DEPENDENCY | ALLOWED_AFTER_ADMISSION | ALWAYS_IGNORE_FOR_AUTOMATED_UPDATES | FORBIDDEN |
| Advanced Custom Fields: Extended PRO | acf-extended-pro/acf-extended.php | 0.9.2.3 | active | OPERATOR_MANAGED_EXTERNAL_DEPENDENCY | NOT APPROVED BY DEFAULT | ALWAYS_IGNORE_FOR_AUTOMATED_UPDATES | FORBIDDEN |
| Advanced Custom Fields | advanced-custom-fields/acf.php | 6.8.4 | inactive | INACTIVE_LEGACY_OR_FALLBACK_PLUGIN | NOT USED WHILE ACF PRO ACTIVE | DO_NOT_UPDATE_IN_THIS_TASK | FORBIDDEN |

## Baselines

| Plugin | Files | PHP | JS | Aggregate hash | Manifest |
|---|---:|---:|---:|---|---|
| Advanced Custom Fields PRO | 705 | 336 | 21 | 62dcbd1c1fb556b77ecf460f624c9c85dbf8165d2c3c40ea3028458c91308c42 | WORDPRESS/validation/v9-06b2-acf-admission/acf-pro-file-manifest.json |
| Advanced Custom Fields: Extended PRO | 612 | 519 | 36 | ac614f38670ec9c272ed8a39d52a6cc39d54899a5d1268a6714d73f9e4ff78aa | WORDPRESS/validation/v9-06b2-acf-admission/acf-extended-pro-file-manifest.json |

## Decisions

- ACF PRO: **ADMITTED** for public API use after dependency admission; V9-06C still needs separate operator authorization.
- ACF Extended PRO: **CLASSIFIED** but **NOT APPROVED** for FP-0002 use by default. Recommendation: KEEP_ACTIVE_BUT_NOT_USED.
- ACF Free: **INACTIVE_NOT_USED** while ACF PRO is active.

## Hard Denylist

Future update/deployment prompts must treat ACF PRO and ACF Extended PRO as denylisted for automatic updates, replacement, deletion, cleanup, and package delivery. ACF Free must not be activated, deleted, or updated in this admission context.
