# FP-0002 V9-06C Content Model Implementation Spec v1

**Status:** SOURCE IMPLEMENTED — NOT DELIVERED

## Scope

- `service` CPT source is implemented in Shpigovsky Core with `has_archive=false` and hierarchical `/uslugi/{service-path}/` contract.
- ACF Pro field group source definitions are implemented and canonical JSON source is generated under `WORDPRESS/acf-json/`.
- Runtime registration, object creation, menu changes, option changes and rewrite flush remain not performed.

## Field Groups

Total groups: 13. See `FP-0002-V9-06C-ACF-FIELD-GROUP-REGISTRY-v1.json`.

## Source Activation Boundary

V9-06C.1 supersedes the old coarse skeleton gate. `SHPIGOVSKY_CORE_MODE` defaults to `content_model`, and V9-06C content-model modules are enabled in source for delivery readiness.

Runtime delivery, object creation, migrations, content migration, redirects, rewrite flush, option writes, and ACF runtime DB sync remain not performed and require separate authorization.
