# FP-0002 V9-06E2 Repair Plan

**Date:** 2026-07-06  
**Evidence:** `validation/v9-06e2-legal-layout-menu-alignment-repair/repair-plan.json`

| Component | Planned action | Safety |
|-----------|----------------|--------|
| Legal width | Remove `.legal-document__container` 900px cap and `.legal-document__body` 820px cap in `v9-style.css` | CSS only; no content |
| Legal menu | Delete menu item #36 (#21 hub); reorder #37–#40 | No page delete |
| Page #21 | Set `post_status=draft` | Preserve object |
| Primary menu | Remove items #26 (Home), #28 (Специалисты); relabel #27; add page #6 Зависимости; reorder | Existing pages only |
| Privacy setting | No change | Already #3 from E1 |
| Rewrite flush | Not required | — |
