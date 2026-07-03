# FP-0002 V9-06D.1 Activation Validation v1

**Result:** PASS — content model activation verified in local runtime.

## Runtime activation

- `SHPIGOVSKY_CORE_MODE`: `content_model`
- `SHPIGOVSKY_CORE_SKELETON`: `false`
- Enabled modules: ContentTypes, Permalinks, Fields, Settings, Admin, Validation.
- Deferred modules: Migrations, Forms, object creation, content migration, redirects, rewrite flush.

## Service CPT

- Registered: yes
- Public: true
- Hierarchical: true
- Has archive: false
- REST: true
- Taxonomies: 0
- Service objects: 0

## ACF / Options Page

- ACF PRO active: true
- ACF local field groups discoverable: 13
- Runtime ACF JSON files: 13
- Options Page: `fp02-site-settings` registered
- ACF Extended PRO usage: 0
- ACF Free active: false

## Runtime health and immutability

- Frontend: HTTP 200
- wp-admin: HTTP 200
- Pages changed: 0
- Posts changed: 0
- Services created: 0
- Menus changed: 0
- Plugin activation changed: 0
- Rewrite flush performed: false

## Evidence

- `WORDPRESS/validation/v9-06d1-runtime-delivery-rerun/content-model-activation.json`
- `WORDPRESS/validation/v9-06d1-runtime-delivery-rerun/object-immutability.json`
- `WORDPRESS/validation/v9-06d1-runtime-delivery-rerun/wordpress-activation-smoke.json`
