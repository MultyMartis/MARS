# FP-0002 V9-06E27B Exact Cleanup Plan v1

**Wave:** V9-06E27B  
**Result:** PASS  
**Authority:** E27A `proposed-e27b-cleanup-plan.json` Batch A

| Page ID | Path | Before | Action | Rollback |
|---:|---|---|---|---|
| 9 | `/uslugi/genotipirovanie/` | publish | trash | Restore from Trash or DB checkpoint |
| 10 | `/specyalisty/` | publish | trash | Restore from Trash or DB checkpoint |
| 17 | `/o-centre/intervyu-i-smi/` | publish | trash | Restore from Trash or DB checkpoint |
| 21 | `/pravovaya-informaciya-pilzovatelyu/` | draft | trash | Restore from Trash or DB checkpoint |
| 25 | `/privacy-policy-page/` | publish | trash | Restore from Trash or DB checkpoint |

## Boundaries

- No redirects
- No menu changes
- No permalink changes
- No rewrite flush
- Forbidden: pages #6, #7, #8

Evidence: `validation/v9-06e27b-low-risk-obsolete-cleanup/exact-cleanup-plan.json`
