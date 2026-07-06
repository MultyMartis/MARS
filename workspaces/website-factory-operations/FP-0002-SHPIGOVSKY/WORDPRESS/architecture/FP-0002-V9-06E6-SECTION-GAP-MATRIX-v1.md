# FP-0002 V9-06E6 — Section Gap Matrix

| Static section | Before status | Repair | After |
|----------------|---------------|--------|-------|
| `page-service-subdivision-v1` body | MISSING | `shpigovsky_service_body_class()` | FIXED |
| Main wrapper | MATCH | preserve | PASS |
| Article wrapper | EXTRA | remove from stack | FIXED |
| Dependencies header/marker/footer | WRONG MARKUP | `children.php` | FIXED |
| Dependencies heading | WRONG CONTENT | static fallback | FIXED |
| Nature copy/structure | WRONG CONTENT | static V9 lorem | FIXED |
| Program modifiers/images | WRONG MARKUP | `program.php` subdivision branch | FIXED |
| Mid-cta source | MINOR DRIFT | `service-subdivision-cta-01` | FIXED |
| Team-stats cards | WRONG CONTENT | static V9 lorem | FIXED |
| Stages + shared blocks | MATCH | none | PASS |

**Deferred:** none

JSON: `validation/v9-06e6-service-subdivision-main-layout-repair/section-gap-matrix.json`
