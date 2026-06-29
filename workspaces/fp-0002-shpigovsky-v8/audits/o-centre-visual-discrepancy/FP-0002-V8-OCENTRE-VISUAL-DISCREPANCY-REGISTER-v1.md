| ID | Region | Viewport | Type | Current | Canonical | Severity | Root cause | Correction class |
|---|---|---|---|---|---|---|---|---|
| VD-001 | OC-INST-FOUNDER | both | ORDER | Founder quote after program CTA | Founder quote embedded in institutional band after body copy | CRITICAL | 12-block charter collapsed founder into separate late block | HTML_ORDER_ONLY |
| VD-002 | OC-CTA-1 | both | MISSING_REGION | No CTA between who-we-treat and approach | С чего начать at 1:2328 before approach | HIGH | Reconciled composition omitted first CTA | HTML_ORDER_ONLY |
| VD-003 | OC-WHO-TREAT | both | MISSING_REGION | Text-only category section | Group photo Rectangle 4263 + four card grid in 1:2310 | CRITICAL | services-category-section-v2 used without galleryHtml | UNIQUE_PARTIAL_RESTRUCTURE |
| VD-004 | OC-APPROACH | both | WRONG_GROUPING | Inline program-approach-band | Separate Программа центра frame with staff photo + cards + landscape bleed | HIGH | Approach merged into page inline block | EXISTING_PARTIAL_REUSE |
| VD-005 | OC-CLINIC-LANDSCAPE | both | MISSING_REGION | Not included on page | Large territory/clinic bleed after approach cards | HIGH | Charter optional reuse never wired | EXISTING_PARTIAL_REUSE |
| VD-006 | OC-INFRA | both | WRONG_GROUPING | Single CSS auto-grid for 20 assets | Text-interleaved photo subgroups in 1:2440 | CRITICAL | Asset manifest interpreted as collage | UNIQUE_PARTIAL_RESTRUCTURE |
| VD-007 | OC-INFRA | both | DECORATION | No section background raster | 1:2440 decorative fill opacity 0.1 | HIGH | Decorative layers not parsed in implementation | DECORATIVE_LAYER_IMPLEMENTATION |
| VD-008 | OC-INST | both | CONTENT | Typo Шпиговсикй preserved | Same typo in Figma 1:2282 | LOW | Canonical copy fidelity | NO_CHANGE |
| VD-009 | OC-PROGRAM | both | ORDER | Program before misplaced mid-CTA | Program after approach + landscape | MEDIUM | CTA/founder order drift | HTML_ORDER_ONLY |
| VD-010 | OC-SPECIALISTS | both | SPACING | V8 canonical component | Figma tail acceptable via V8 canon | ACCEPTABLE_CANON_DIFFERENCE | Shared component authority | NO_CHANGE |
| VD-011 | OC-REVIEWS | both | SPACING | V8 canonical component | Figma tail acceptable via V8 canon | ACCEPTABLE_CANON_DIFFERENCE | Shared component authority | NO_CHANGE |
| VD-012 | OC-FINAL-FORM | both | COMPONENT_BOUNDARY | CF-009 final form | Figma faq frame is final form not accordion | ACCEPTABLE_CANON_DIFFERENCE | Content blocker resolution | NO_CHANGE |
| VD-013 | page | desktop | GEOMETRY | Shorter cumulative height | Figma 12830px frame | MAJOR | Missing subregions + flat spacing | SCOPED_SCSS |
| VD-014 | OC-APPROACH | both | CONTENT | Four card titles only | Four cards with Lorem body omitted by policy | ACCEPTABLE_CANON_DIFFERENCE | Lorem omission authorized | NO_CHANGE |
| VD-015 | OC-INFRA | mobile | RESPONSIVE | Mobile-only assets 19/20 present | Mobile-only assets required | LOW | Visibility classes correct; grouping wrong | UNIQUE_PARTIAL_RESTRUCTURE |
