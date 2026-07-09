# FP-0002 V9-06E27B Rollback Instructions v1

**Wave:** V9-06E27B  
**Checkpoint:** `v9-06e27b-low-risk-obsolete-cleanup-pre-20260709-171947`

## Per-page restore

| Page ID | Title | Restore action | Validation after restore |
|---:|---|---|---|
| 9 | Генотипирование | WP Admin → Pages → Trash → Restore; or `wp post update 9 --post_status=publish` | `/uslugi/genotipirovanie/` |
| 10 | Специалисты | Restore; or `wp post update 10 --post_status=publish` | `/specyalisty/` |
| 17 | Интервью и СМИ | Restore; or `wp post update 17 --post_status=publish` | `/o-centre/intervyu-i-smi/` |
| 21 | Правовая информация | Restore; or `wp post update 21 --post_status=draft` | `/pravovaya-informaciya-pilzovatelyu/` (draft) |
| 25 | Политика конфиденциальности (системная) | Restore; or `wp post update 25 --post_status=publish` | `/privacy-policy-page/` |

## Full DB restore

```text
mysql --host=127.0.0.1 --user=root mars_wp_fp0002 < "X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e27b-low-risk-obsolete-cleanup-pre-20260709-171947\mars_wp_fp0002.sql"
```

Evidence: `validation/v9-06e27b-low-risk-obsolete-cleanup/rollback-instructions.json`
