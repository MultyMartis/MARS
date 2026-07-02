# FP-0002 V8 O-Centre Risk Register v1

**Date:** 2026-06-29

| Risk | Probability | Impact | Evidence | Mitigation | Gate |
|---|---|---|---|---|---|
| Accidental overwrite of operator manual polish | Medium | Critical | Shared SCSS touches all pages | Phase 0 hash guard; scope SCSS to new sections only | Pre-implementation backup |
| False reuse of `home-gallery` | Low | High | Gallery audit | Reject home-gallery; use comfort | Charter gate |
| False reuse of `home-staff-photo` | Low | Medium | Staff audit | Use specialists + clinic-landscape only if needed | Charter gate |
| Duplicate page-specific classes for shared blocks | Medium | High | Naming rules | Use canonical partials + modifiers only | Component gate |
| Gallery architecture duplication | Medium | Medium | Two gallery families on one page | Comfort + category grid — separate partials | Composition map |
| Missing About narrative assets | High | High | Asset inventory MISSING_SOURCE | Asset prep phase before pixel QA | Asset gate |
| Incomplete mobile design merge on desktop | Medium | Medium | Figma section name drift | Mobile-led comfort band verification | Visual QA |
| Content conflict inventory vs Figma FAQ | Medium | Medium | Design evidence | Operator confirm FAQ on About | Content gate |
| Old Figma `Шпиговский.fig` usage | Low | High | Authority split | Spig_v1.2.fig only | Source register |
| Asset export uncertainty | High | Medium | No V8 design folder | Export from Spig_v1.2.fig in prep task | Asset gate |
| Button/link drift (`comfort` href `#`) | Medium | Low | comfort.html | Fix in implementation | Integration phase |
| Page-wide duplicate IDs | Medium | High | Multi-slider page | DOM validation gate | Phase 6 QA |
| Modal duplicate initialization | Low | Medium | Single modal include | One modal per page | Build QA |
| Visual regression shared blocks | Medium | High | CF-003–012 protected | No SCSS edits to shared selectors | Protected list |
| V7 WIP structure copied | Medium | High | Rejected o-centre-v1 | Follow composition map not V7 | Charter |
| Subnav vs footer IA conflict | Medium | Medium | CF-006 | Anchors vs subpages — operator decision | Content gate |

**Critical open:** BLK-036–038 copy and assets.
**Mitigated:** Gallery and staff-photo false reuse.
