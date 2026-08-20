# ISEO-SU production form source (canonical MARS mirror)

These files mirror the accepted production docroot form/security surface after
`ISEO-SU-SITE-OPS-FORMS-ANTISPAM-AND-VALIDATION-01`.

| Path in this folder | Production path |
|---------------------|-----------------|
| `forms/*.php` (handlers + libs) | docroot `/*.php` |
| `js/common.js` | docroot `js/common.js` |

Service-tree `services/**/**__FORM.php` copies are thin `require` delegates to the root handlers and are regenerated from the same root authority when needed.

Do not enable `test_mode` in committed config for normal production.
