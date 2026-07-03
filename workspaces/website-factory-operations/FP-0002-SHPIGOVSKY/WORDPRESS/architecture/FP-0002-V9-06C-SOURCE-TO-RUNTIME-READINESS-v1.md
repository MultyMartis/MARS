# FP-0002 V9-06C Source-to-Runtime Readiness v1

**WordPress source implementation:** CONTENT MODEL COMPLETE — SOURCE ACTIVATION GATE RESOLVED BY V9-06C.1
**WordPress runtime implementation:** NOT STARTED

Runtime delivery requires a separate V9-06D/delivery strategy decision, explicit package manifest, backup/checkpoint, rewrite flush boundary, and WordPress object skeleton authorization.

## V9-06C.1 update

`SHPIGOVSKY_CORE_MODE` defaults to `content_model`; legacy `SHPIGOVSKY_CORE_SKELETON` is compatibility-derived and false in this mode. ContentTypes, Permalinks, Fields, Settings, Admin, and Validation modules are enabled in source after delivery. Migrations, Forms, object creation, content migration, redirects, and rewrite flush remain disabled.
