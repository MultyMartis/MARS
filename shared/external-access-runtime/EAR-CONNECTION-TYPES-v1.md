# EAR Connection Types v1

Catalog of **potential** connectors for future read-only acquisition. **No connector is claimed implemented** in this repository at foundation freeze.

Each entry: future use, risks, read-only expectations, **SAFE UNKNOWN** where evidence is missing.

Align human gates with [shared/external-access-patterns/](../external-access-patterns/README.md).

---

## SFTP

| Aspect | Detail |
|--------|--------|
| **Future use** | Recursive file listing; selective download; manifest generation |
| **Risks** | Wrong remote root; symlink traversal; downloading `storage/cache` bulk; credential in scripts |
| **Read-only** | List + get only; no upload, rename, delete |
| **SAFE UNKNOWN** | Host-specific chroot layout for Beget/similar |

---

## FTP (plain / FTPS)

| Aspect | Detail |
|--------|--------|
| **Future use** | Legacy hosts without SFTP |
| **Risks** | Cleartext credentials; fragile listings; passive/active firewall issues |
| **Read-only** | RETR/LIST only; no STOR/DELE |
| **SAFE UNKNOWN** | Whether MARS will support plain FTP or FTPS-only |

---

## SSH

| Aspect | Detail |
|--------|--------|
| **Future use** | Remote `find`, checksums, selective `cat` of version files; optional DB CLI read-only |
| **Risks** | Operator runs destructive shell by mistake; key management; production shell access |
| **Read-only** | No `rm`, `mv`, redirect overwrite, or migration commands in EAR scripts (future) |
| **SAFE UNKNOWN** | Shared hosting may not grant SSH |

---

## phpMyAdmin exports

| Aspect | Detail |
|--------|--------|
| **Future use** | Schema export, `SHOW TABLES`, structure-only dumps for `database-metadata` |
| **Risks** | Full dump with PII; accidental import on wrong DB; browser session hijack |
| **Read-only** | Export/download only; no SQL run that mutates |
| **SAFE UNKNOWN** | Max export size on host |

---

## OpenCart admin

| Aspect | Detail |
|--------|--------|
| **Future use** | Extension list, version string, theme name, read-only settings screenshots **or** API if ever available |
| **Risks** | Misclick enables module; cache refresh side effects; session on production |
| **Read-only** | Navigation without save; no install/uninstall/edit |
| **SAFE UNKNOWN** | ocStore 3.0.3.8 admin routes for SITE-001 — operator to confirm |

---

## WordPress admin

| Aspect | Detail |
|--------|--------|
| **Future use** | WPilot Phase 3 — plugin/theme lists, core version |
| **Risks** | Plugin update click; user edit exposure |
| **Read-only** | View-only screens; no post/plugin install |
| **SAFE UNKNOWN** | REST read-only endpoints vs browser-only |

---

## File archives

| Aspect | Detail |
|--------|--------|
| **Future use** | Operator or EAR places `.zip` in quarantine; EAR extracts to external bulk, generates manifest |
| **Risks** | Zip bombs; malware; path traversal; stale archive |
| **Read-only** | Extract for inventory only; no repack to live host in v1 |
| **SAFE UNKNOWN** | Virus scan policy |

---

## Database snapshots

| Aspect | Detail |
|--------|--------|
| **Future use** | Table list, row counts, prefix, engine; optional sanitized sample |
| **Risks** | Full dump size; GDPR; secrets in `oc_setting` |
| **Read-only** | Metadata-first in v1 contract; full dump only with explicit charter |
| **SAFE UNKNOWN** | Whether consumers need full SQL for audit vs metadata-only |

---

## Hosting panel (generic)

| Aspect | Detail |
|--------|--------|
| **Future use** | Backup download links, PHP version, cron list (screenshot or export) |
| **Risks** | Panel actions that restart services; wrong account |
| **Read-only** | View/download; no DNS/email/delete site |
| **SAFE UNKNOWN** | Beget-specific panel patterns for SITE-001 |

---

## Browser-only evidence

| Aspect | Detail |
|--------|--------|
| **Future use** | Mode 0/1 fallback when no file protocol |
| **Risks** | Non-reproducible; OCR errors; no manifest |
| **Read-only** | Screenshot of read-only pages |
| **SAFE UNKNOWN** | Minimum acceptable evidence for version gate |

---

## Connector selection matrix (conceptual)

| Need | Preferred order |
|------|-----------------|
| Full file tree | SFTP / SSH → archive |
| Schema | PMA metadata → SSH mysql read-only |
| Extension list | OpenCart admin read-only → file scan |
| WordPress | WP admin read-only → file scan |

---

## Implementation disclaimer

Listing a connection type **does not** imply:

- Library choice
- Scheduled jobs
- Credential storage design beyond [EAR-SECURITY-MODEL-v1.md](EAR-SECURITY-MODEL-v1.md)

Phase 2 may implement a **subset** for OpenCart only.
