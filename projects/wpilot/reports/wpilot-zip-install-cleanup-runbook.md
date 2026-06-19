# WPilot ZIP Install — Operator Cleanup Runbook

**Purpose:** Remove ghost/duplicate WPilot plugin state on `dev.gktriumph.ru` (or any target) before installing **RC2** package.  
**Package:** `C:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc2.zip`  
**Do not use RC1** for retry after install failure.

---

## Prerequisites

- `manage_options` access to WordPress admin (or SFTP/FTP to `wp-content/plugins/`).
- RC2 ZIP built and validated (`metacode-wpilot-v0.3.0-rc2.inventory.json` → `"valid": true`).

---

## Step 1 — Remove all WPilot plugin folders

Via **SFTP/FTP** or hosting file manager, delete **every** folder under `wp-content/plugins/` whose name matches or contains WPilot, for example:

- `wp-content/plugins/metacode-wpilot/`
- `wp-content/plugins/metacode-wpilot-1/` (if WordPress created a suffix copy)
- `wp-content/plugins/metacode-wpilot-v0.3.0-rc1/` (if a versioned extract ever existed)
- Any `metacode-wpilot/metacode-wpilot/` nested tree

**Check:** No `metacode-wpilot.php` remains anywhere under `wp-content/plugins/`.

---

## Step 2 — Refresh Plugins page

1. Open **Plugins → Installed Plugins**.
2. Hard-refresh the browser (Ctrl+F5).

---

## Step 3 — Confirm no MetaCODE WPilot entries remain

- The plugins list must show **zero** rows titled **MetaCODE WPilot**.
- If a ghost row still appears after Step 1, the folder was not fully removed — repeat Step 1 and search for alternate paths (suffix folders, nested copies).

---

## Step 4 — Upload RC2 ZIP

1. **Plugins → Add New → Upload Plugin**.
2. Choose `metacode-wpilot-v0.3.0-rc2.zip`.
3. Click **Install Now**.
4. Confirm success message; **do not activate yet** if you want to verify folder layout first.

**Optional SFTP verify after upload:**

```
wp-content/plugins/metacode-wpilot/metacode-wpilot.php   ← must exist
wp-content/plugins/metacode-wpilot/admin/
wp-content/plugins/metacode-wpilot/includes/
wp-content/plugins/metacode-wpilot/languages/
```

There must be **no** `metacode-wpilot/metacode-wpilot/` nested folder.

---

## Step 5 — Activate plugin

1. Click **Activate** on the **single** MetaCODE WPilot entry.
2. Expected plugin file path: `metacode-wpilot/metacode-wpilot.php`.
3. If activation shows **«Файл плагина не найден»** — stop; folder layout is wrong or a duplicate ghost remains. Return to Step 1.

---

## Step 6 — Verify Settings → MetaCODE WPilot

1. Open **Settings → MetaCODE WPilot** (or admin menu entry as configured).
2. Confirm page loads without PHP fatal errors.
3. Optional: `GET /wp-json/wpilot/v1/ping` returns HTTP 200.

---

## Data retention warning

**Do not** drop these tables unless you intentionally want to reset WPilot backup/audit data:

- `wp_wpilot_backups`
- `wp_wpilot_audit_log`

(Table prefix may differ if `wp_` is not the site prefix.)

Removing plugin **files** does not remove these tables. Re-activation after clean install should reuse existing schema if tables already exist.

---

## RC1 vs RC2

| Item | RC1 | RC2 |
|------|-----|-----|
| Use for install retry | **No** | **Yes** |
| Path | `metacode-wpilot-v0.3.0-rc1.zip` | `metacode-wpilot-v0.3.0-rc2.zip` |

RC1 failed on DEV due to install-state collision with prior FTP deploy; RC2 is the operator retry package after full cleanup.
