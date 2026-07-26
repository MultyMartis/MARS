# METALLKA — WPilot Install Rollback Plan v1

**Programme:** METALLKA-RU-SITE-OPS  
**Phase:** 4A — documentation only  
**Date:** 2026-07-26  
**Site:** `https://metallka.ru/`  
**Related charter:** [METALLKA-WPILOT-INSTALLATION-ONBOARDING-CHARTER-v1.md](METALLKA-WPILOT-INSTALLATION-ONBOARDING-CHARTER-v1.md)

```text
No rollback action is authorized or performed in Phase 4A.
```

---

## 1. Why stronger than CHANGE 0001

CHANGE 0001 mutated one WPBakery text field. WPilot onboarding introduces:

- new filesystem tree under `wp-content/plugins/metacode-wpilot/`;
- option `wpilot_options` (and `wpilot_schema_valid`);
- schema tables `{prefix}wpilot_backups` and `{prefix}wpilot_audit_log` on activation;
- optional token hash inside options.

Hosting-native Beget backup/restore remains the **primary** recovery backstop.

---

## 2. Pre-install baseline to capture (Phase 4B)

| Check | Expected before install |
|-------|-------------------------|
| Plugin directory `metacode-wpilot` | **ABSENT** |
| Active plugin row | **ABSENT** |
| Option `wpilot_options` | **ABSENT** |
| Option `wpilot_schema_valid` | **ABSENT** |
| Tables `%wpilot_backups%` / `%wpilot_audit_log%` | **ABSENT** |
| Public REST namespace `wpilot/v1` | **ABSENT** |
| Accepted package SHA | Recorded / re-verified |

Preserve accepted package hash:

`4a0b929cee34e8c6188a10991b0c120bb1e8ffdd09674418a32d920c2aa16bf6`

---

## 3. Emergency disable methods (ordered)

1. **WPilot admin Emergency Disable** (if admin reachable and plugin UI loads) — forces bridge/write off; does **not** remove plugin.  
2. **WP Admin → Plugins → Deactivate** MetaCODE WPilot.  
3. **Filesystem emergency:** rename or remove `wp-content/plugins/metacode-wpilot/` via SSH/SFTP **only under explicit rollback charter** if admin is locked.  
4. **Hosting restore:** Beget full restore if site integrity is compromised beyond plugin scope.

Deactivation (source): sets `bridge_enabled=false` and `write_enabled=false`; **preserves** options/token hash/tables.

---

## 4. Cleanup reality (source-proven)

| Mechanism | Cleans filesystem | Cleans options | Cleans tables | Notes |
|-----------|-------------------|----------------|---------------|-------|
| Deactivate | No | Partial (flags only) | No | Safe defaults off |
| Delete plugin via WP Admin | Removes plugin dir | **Likely retains** options | **Likely retains** tables | **No `uninstall.php`** |
| Manual directory delete | Removes dir | Retains | Retains | Residual DB state must be documented |
| Beget full restore | Restores prior FS+DB | Restores | Restores | Strongest clean rollback |

**Do not assume** uninstall/deactivation fully cleans WPilot state.

Residual options/tables after plugin removal are **acceptable to document** as residual SAFE UNKNOWN / known retention unless a separate cleanup charter authorizes DB deletes.

---

## 5. Failure / rollback matrix

### CASE A — ZIP upload/install fails before activation

| Item | Action |
|------|--------|
| Desired final state | WPilot **absent / inactive** |
| Actions | Do not activate; remove partial `metacode-wpilot/` directory **only if present and chartered** |
| Token | None |
| REST | None |
| Success of rollback | Site matches pre-install absence baseline |

### CASE B — Activation causes fatal / admin lockout

| Item | Action |
|------|--------|
| Immediate | Filesystem emergency disable (rename/remove plugin dir) or hosting restore if needed |
| Then | Validate frontend + WP Admin recovery |
| Token | Do not create |
| Document | Activation failure evidence; residual options/tables if any |

### CASE C — Activation succeeds but safe defaults invalid

| Item | Action |
|------|--------|
| Token | **Do not create** |
| Action | Deactivate + remove plugin per charter; document residual options/tables |
| Blocking label | `ROLLED BACK — WPILOT SAFE DEFAULT FAILURE` |
| Validate | Frontend/admin recovery; bridge/write remain off if residuals exist |

### CASE D — Token generation fails with safe defaults intact

| Item | Preferred final state |
|------|------------------------|
| Plugin | May **remain active** with safe defaults false **if** admin/frontend smoke PASS and operator accepts “installed, no token” |
| Bridge | Must stay off |
| Alternate | If operator prefers clean absence: deactivate/remove and document residuals |
| Charter default preference | **Remain active, no token, STOP** — retry token only under a new explicit approval |

### CASE E — Token generated but post-token safe defaults differ

| Item | Action |
|------|--------|
| Treat as | Onboarding failure |
| Immediate | Emergency disable / deactivate; do not use token; do not call REST |
| Local file | Do not keep a production token file if defaults corrupted — delete local token file if created; treat credential as compromised for ops purposes |
| Plugin FS | Remove/deactivate per operator choice; prefer Beget restore if state integrity unclear |
| Blocking label | `ROLLED BACK — WPILOT POST-TOKEN SAFE DEFAULT FAILURE` |

### CASE F — Frontend / admin regression after onboarding

| Item | Action |
|------|--------|
| Action | Rollback plugin onboarding (deactivate/remove; restore from Beget if needed) |
| Token local file | Remove if created |
| No | Trial-and-error production debugging beyond bounded evidence collection |

---

## 6. Distinguishing rollback classes

| Class | Typical remedy |
|-------|----------------|
| 1. Activation failure before meaningful state | Remove partial dir; confirm absence |
| 2. Activated but safe-default validation failure | Deactivate/remove; document residuals; no token |
| 3. Token-generation failure | Prefer leave active + safe; or remove if operator chooses |
| 4. Frontend/admin regression | Plugin rollback ± Beget restore |
| 5. Partial installation | Remove incomplete directory only |
| 6. Package-directory corruption | Remove dir; reinstall only under new approval from accepted ZIP |

---

## 7. Post-rollback validation (minimum)

- Public homepage HTTP 200; no fatal markers  
- WP Admin Dashboard loads  
- Plugins page loads  
- Page 52 editor opens (WPBakery)  
- WPilot absent **or** explicitly documented residual inactive/options/tables state  

---

## 8. What this plan does not authorize

- Automatic DB option/table DROP  
- Broad `git` / hosting experiments  
- Bridge enable “to test rollback”  
- Any WPilot REST call during rollback  

---

*METALLKA WPilot Install Rollback Plan v1 · Phase 4A preparation only.*
