# FP-0002 V8 O-Centre Correction Scope Manifest v1

| File/path | Current role | Expected action | Allowed | Reason |
|---|---|---|---:|---|
| src/pages/o-centre.html | Page include order | REORDER includes | YES | Composition fix |
| src/partials/sections/institutional-narrative.html | Institutional copy | RESTRUCTURE wrapper / founder context | YES | Founder placement |
| src/partials/sections/infrastructure-narrative.html | Infrastructure | RESTRUCTURE internal subgroups | YES | Not a gallery |
| inline program-approach-band in o-centre.html | Approach | KEEP content; fix order/context | YES | May extract partial later |
| src/partials/sections/clinic-landscape.html | Landscape band | ADD include after approach | YES | Proven reuse |
| src/partials/sections/founder-quote.html | CF-004 base | REFERENCE ONLY | NO | Placement change only |
| src/partials/sections/services-program-v2.html | Program | REFERENCE ONLY | NO | V8 canon |
| src/scss/style.scss (page-o-centre ranges) | Scoped styles | SCOPED additions | YES | Subgroup layouts + decoration |
| src/img/content/o-centre/decorative/o-centre-infrastructure-background.webp | OC-DEC-01 background | REFERENCE ONLY (exported) | NO | CSS wiring in Phase 6 only |
| src/js/main.js | Init | NO CHANGE | NO | JS not required |
