# PROD-P13 Production Intake

- captured_at: `2026-08-16T15:35:23.362334+00:00`
- files inspected: **57**
- MATCH: **54**
- DRIFT: **2**
- missing prod: **1**

## Drifted files

- `theme/assets/css/v9-style.css`
  - local `c5e175e07c4924e3…` (590073 B)
  - prod  `3314ea2527fbfecd…` (590069 B)
- `theme/assets/css/fp02-specialist-profile.css`
  - local `41b4a9d537a2f5a0…` (2620 B)
  - prod  `657b8d3eb05282ff…` (2626 B)

## MU-plugins

- `mars-local-runtime.php` (1580 B)

## Env signals (redacted)

```json
{
  "WP_ENVIRONMENT_TYPE": [
    "define( 'WP_ENVIRONMENT_TYPE', 'local' );"
  ],
  "WP_DEBUG": [
    "define( 'WP_DEBUG', true );",
    "define( 'WP_DEBUG_LOG', true );",
    "define( 'WP_DEBUG_DISPLAY', false );",
    "define( 'WP_DEBUG_LOG_FILE', 'D:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/debug.log' );"
  ],
  "WP_DEBUG_DISPLAY": [
    "define( 'WP_DEBUG_DISPLAY', false );"
  ],
  "WP_DEBUG_LOG": [
    "define( 'WP_DEBUG_LOG', true );",
    "define( 'WP_DEBUG_LOG_FILE', 'D:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/debug.log' );"
  ],
  "DISALLOW_FILE_EDIT": [
    "define( 'DISALLOW_FILE_EDIT', true );"
  ],
  "wpconfig_notice_needles": [
    "WP_ENVIRONMENT_TYPE"
  ]
}
```
