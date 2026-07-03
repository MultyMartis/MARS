# FP-0002 V9-06C Content Model Implementation Spec v1

**Status:** SOURCE IMPLEMENTED — NOT DELIVERED

## Scope

- `service` CPT source is implemented in Shpigovsky Core with `has_archive=false` and hierarchical `/uslugi/{service-path}/` contract.
- ACF Pro field group source definitions are implemented and canonical JSON source is generated under `WORDPRESS/acf-json/`.
- Runtime registration, object creation, menu changes, option changes and rewrite flush remain not performed.

## Field Groups

Total groups: 13. See `FP-0002-V9-06C-ACF-FIELD-GROUP-REGISTRY-v1.json`.

## Runtime Boundary

`SHPIGOVSKY_CORE_SKELETON` remains `true`; source implementation is ready for a later delivery phase only.
