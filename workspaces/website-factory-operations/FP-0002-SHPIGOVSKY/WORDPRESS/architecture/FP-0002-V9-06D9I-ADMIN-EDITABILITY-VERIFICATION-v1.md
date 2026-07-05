# FP-0002 V9-06D9I Admin Editability Verification v1

**Date:** 2026-07-05  
**Task:** V9-06D9-I

## Result: PASS

Home page #4 edit screen now has populated D9-H fields for all seeded text/repeater surfaces.

| Area | Status | Notes |
|------|--------|-------|
| Recovery intro heading/leads | PASS | Three scalar fields populated |
| Intro bands repeater | PASS | 6 rows title+text |
| Section headings (FAQ, specialists, comfort, reviews, articles) | PASS | Match frontend fallbacks |
| FAQ items | PARTIAL | 5 items from D8-B; admin editable |
| Advantages | PASS | 6 cards from D8-B |
| Hero slides | PARTIAL | Text populated; image empty (D9-J) |
| Gallery media | PARTIAL | Empty; theme fallback assets used |
| CTA fields | PASS | Pre-seeded |

Empty deferred fields retain frontend fallbacks via `inc/home-fallbacks.php`.

Evidence: `validation/v9-06d9i-controlled-acf-seed/admin-editability-verification.json`
