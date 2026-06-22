# MARS Localhost — Runtime Manifest Contract v1

**Document type:** Runtime manifest contract  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-00

---

## Purpose

Every sustained local runtime must have a **canonical pointer in the MARS brain** while runtime files remain on `D:\MARS-Localhost`.

---

## Storage

| Item | Location |
|------|----------|
| **Manifest SoT** | `C:\AI MARS\projects\mars-localhost-infrastructure\manifests\` |
| **Runtime files** | `D:\MARS-Localhost\` per directory standard |
| **Format** | JSON preferred; Markdown table manifest allowed for human-only sandboxes |

**Filename pattern:** `{runtime-id}.json` or `{platform}-{class}-{slug}.json`

---

## Required fields

| Field | Description |
|-------|-------------|
| **Runtime ID** | Stable MLI id (e.g. `MLI-RT-WP-FWS-0001`) |
| **Project / synthetic ID** | Consumer id (e.g. `FWS-0001`, `FP-0002`, `SITE-002`) |
| **Runtime class** | `synthetic` \| `projects` \| `sandboxes` |
| **Platform** | `wordpress` \| `opencart` \| `php` \| `other` |
| **MARS authority path** | Brain doc/passport path in `C:\AI MARS` |
| **Local runtime path** | Absolute path under `D:\MARS-Localhost\sites\...` |
| **Local URL** | Canonical URL (e.g. `https://fws-0001.test`) |
| **Database ID** | Database name per naming standard |
| **PHP version** | e.g. `8.2` — target for site |
| **DB version** | e.g. `MariaDB 10.11` |
| **Web server** | `apache` \| `nginx` |
| **Runtime owner** | Operator role accountable for D: files |
| **Implementation owner** | Consumer program (e.g. Forge WordPress) |
| **Operations owner** | Who may start/stop services |
| **Production target** | `NONE` for local-only; or external host ref if mirror (read-only) |
| **Backup state** | `none` \| `baseline` \| `current` + path ref |
| **Rollback state** | Last known good backup id |
| **Secrets location** | e.g. `C:\AI MARS\local\mli\{slug}\` — **no secret values** |
| **Current status** | `planned` \| `provisioning` \| `active` \| `hold` \| `archived` |
| **Last validation** | ISO date + report link in brain |

---

## Example (skeleton)

```json
{
  "runtime_id": "MLI-RT-WP-FWS-0001",
  "project_synthetic_id": "FWS-0001",
  "runtime_class": "synthetic",
  "platform": "wordpress",
  "mars_authority_path": "workspaces/forge-wordpress-synthetic/FWS-0001/",
  "local_runtime_path": "D:\\MARS-Localhost\\sites\\wordpress\\synthetic\\fws-0001",
  "local_url": "https://fws-0001.test",
  "database_id": "mars_wp_fws0001",
  "php_version": "8.2",
  "db_version": "MariaDB 10.11",
  "web_server": "apache",
  "runtime_owner": "operator",
  "implementation_owner": "forge-wordpress",
  "operations_owner": "operator",
  "production_target": "NONE",
  "backup_state": "none",
  "rollback_state": "none",
  "secrets_location": "C:\\AI MARS\\local\\mli\\fws-0001\\",
  "current_status": "planned",
  "last_validation": null
}
```

---

## Rules

| ID | Rule |
|----|------|
| **RM-01** | No runtime without manifest for `projects` class |
| **RM-02** | Synthetic validation cases require manifest before MLI-03 proof |
| **RM-03** | Manifest updates live in Git; D: paths may change only with manifest revision |
| **RM-04** | Secrets never stored in manifest body |
| **RM-05** | Consumer programs link **to** manifest; they do not replace it |

---

## Related

- [manifests/README.md](manifests/README.md)
- [MARS-LOCALHOST-SITE-CLASSIFICATION-STANDARD-v1.md](MARS-LOCALHOST-SITE-CLASSIFICATION-STANDARD-v1.md)

---

*Runtime manifest contract v1 — MLI-00.*
