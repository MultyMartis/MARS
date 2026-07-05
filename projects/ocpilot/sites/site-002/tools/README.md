# SITE-002 Production read-only tools

Small site-specific helpers for Production capture and inspection. **Read-only by default.**

## Scripts

| Script | Purpose |
|--------|---------|
| `site-002-prod-readonly-capture.py` | FTP inventory + baseline download + HTTP checks (full capture) |
| `site-002-prod-http-capture.py` | HTTP-only checks when FTP unavailable |
| `site-002-prod-screenshots.py` | Playwright desktop/mobile screenshots |
| `site-002-prod-admin-readonly.py` | OpenCart admin read-only dashboard inspection |
| `site-002-prod-ftp-retry.py` | FTP retry — inventory + baseline download only (Run 4.171-R1) |
| `site-002-prod-ftp-path-verify.py` | FTP path model verification — read-only listing (Run 4.172) |
| `site-002-prod-text-change-01.py` | Exact single-file Production text deploy for `SITE-002-PROD-TEXT-CHANGE-01` |
| `site-002-prod-sort-az-01.py` | Exact single-controller Production catalog sort deploy for `SITE-002-PROD-SORT-AZ-01` |
| `site-002-prod-sort-menu-order-01.py` | Exact single-Twig Production catalog sort menu deploy for `SITE-002-PROD-SORT-MENU-ORDER-01` |

## Dependencies

- Python 3.x (stdlib + `paramiko` optional for SFTP diagnostics)
- `playwright` (`python -m playwright install chromium`)

## Credentials

Reads **only** the `## PRODUCTION` section from:

```text
X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md
```

No credentials are embedded in scripts or logs.

## Safety

- Read-only scripts have no upload/delete/rename commands
- Does not download `config.php`, `admin/config.php`, `.env`
- Sanitizes admin session tokens in stored observations

`site-002-prod-text-change-01.py` is the only write-capable helper in this folder. It is operation-specific, supports only `/public_html/catalog/view/theme/default/template/information/guarantee.twig`, has mandatory dry-run and rollback manifests, and has no delete or rename functions.
