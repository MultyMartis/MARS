# P06 residue (not cleaned in P13)

Fixed only charter items.

Still present for a future P06 wave:

- `WP_ENVIRONMENT_TYPE = local` in production `wp-config.php`
- `WP_DEBUG_LOG_FILE` path pointing at historical `D:/MARS-Localhost/...`
- MU-plugin still suppresses all outgoing mail (`pre_wp_mail` → false)
- User `mars` (ID 3) remains; owns `support@polygon-ws.ru`
- `blog_public = 0` (indexing still deferred)
- Legacy `social_links` option rows retained (hidden in Admin)
- Historical localhost-era options beyond the approved user/email/notice items
