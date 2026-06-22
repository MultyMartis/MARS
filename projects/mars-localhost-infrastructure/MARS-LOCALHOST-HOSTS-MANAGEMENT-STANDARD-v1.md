# MARS Localhost — Hosts Management Standard v1

**Document type:** Hosts management standard  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-02

---

## Principle

`.test` domains resolve via **operator-controlled, idempotent** updates to the Windows hosts file. No permanently running privileged service.

---

## Managed block format

```text
# BEGIN MARS LOCALHOST MANAGED
127.0.0.1 mli-smoke-001.test
127.0.0.1 fws-0001.test
# END MARS LOCALHOST MANAGED
```

Domains are driven by `D:\MARS-Localhost\runtime\registries\mli-hosts-domains.txt` (runtime) with built-in defaults in `add-mli-host.ps1`.

Only entries inside this block are owned by MLI scripts.

---

## Canonical scripts (runtime)

| Script | Purpose |
|--------|---------|
| `D:\MARS-Localhost\tools\hosts\add-mli-host.cmd` | Add or refresh managed block |
| `D:\MARS-Localhost\tools\hosts\remove-mli-host.cmd` | Remove managed block only |
| `D:\MARS-Localhost\tools\hosts\add-mli-host.ps1` | PowerShell implementation |
| `D:\MARS-Localhost\tools\hosts\remove-mli-host.ps1` | PowerShell implementation |

---

## Behaviour rules

1. **Elevation** only when a hosts change is required.
2. **Backup** hosts to `D:\MARS-Localhost\backups\runtime\hosts\` before mutation.
3. **Idempotent** — repeated add is a no-op when block unchanged.
4. **Non-destructive** — never remove non-MLI entries.
5. **No secrets** in scripts or output.
6. Laragon Auto Virtual Hosts may also update hosts when Laragon UI runs elevated; MLI scripts remain the documented operator path for Cursor/automation.

---

## Operator command (elevation required)

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "D:\MARS-Localhost\tools\hosts\add-mli-host.ps1"
```

Run from an **Administrator** PowerShell session if UAC prompt is unavailable to automation.

---

## Verification

After add: `http://mli-smoke-001.test/` must resolve to `127.0.0.1` without manual `Host` header.

---

## Related

- [MARS-LOCALHOST-DOMAIN-STANDARD-v1.md](MARS-LOCALHOST-DOMAIN-STANDARD-v1.md)
- [MARS-LOCALHOST-VHOST-PROVISIONING-STANDARD-v1.md](MARS-LOCALHOST-VHOST-PROVISIONING-STANDARD-v1.md)

---

*Hosts management standard v1 — MLI-02.*
