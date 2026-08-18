# LEADS ADMIN — P18C-FU01

| Check | Result |
|-------|--------|
| Top-level menu **Заявки** | PASS (`fp02-form-leads`, position 56) |
| List heading | PASS |
| Stats/filters render | PASS (empty business list; no PHP/DB error) |
| Capability | `manage_options` |
| Guest | `manage_options` false |

No lasting QA personal-data rows (`is_qa` deleted after persist smoke).
