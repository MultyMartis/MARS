# Validation Tool Lifecycle — P18D-FU01

## Classification

### A. Reusable safe validation tools

- `WORDPRESS/validation/p18d-smtp-correct-and-verify.php`
- `WORDPRESS/validation/p18d-activate-delivery.php`
- `WORDPRESS/validation/p18d-form-qa.php`
- `WORDPRESS/validation/p18d-retire-suppression-mu.php`

These are useful controlled production helpers when executed intentionally by an operator/agent inside a bounded WordPress bootstrap.

## Lifecycle decision

- **Canonical owner:** source repository under `WORDPRESS/validation/`
- **Runtime posture:** source-only; upload/execute transiently when needed
- **Public webroot:** should **not** remain deployed/executable as persistent public files
- **Secrets:** none printed; password stays hidden

## FU01 disposition

- Scripts were treated as **source-only validation tools**, not persistent runtime endpoints.
- PHP namespace/import safety was normalized in source so the scripts are syntactically valid for controlled execution.
- FU01 production execution used transient `/tmp` bootstrap helpers; nothing was left exposed in public runtime.

## Rule

Production mutators/validators may exist in source, but they must not be left as browseable or long-lived public webroot artifacts after execution.
