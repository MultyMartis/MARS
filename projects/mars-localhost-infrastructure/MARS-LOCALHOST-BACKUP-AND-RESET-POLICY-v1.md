# MARS Localhost — Backup and Reset Policy v1

**Document type:** Backup and reset policy  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-00

---

## Purpose

Predictable backup, reset, and rollback discipline for local runtimes without uncontrolled duplicate archives.

---

## Baseline before major changes

| Trigger | Action |
|---------|--------|
| MLI toolchain upgrade | DB dump + `runtime\laragon\` config snapshot if customized |
| Consumer major migration | Full site files + DB dump |
| Import of client dump | Baseline **before** import |
| Synthetic proof cycle | Optional lightweight baseline |

**Baseline location:** `E:\MARS-Localhost\databases\baselines\` and `backups\{platform}\`

---

## DB dump

- Naming per [database naming standard](MARS-LOCALHOST-DATABASE-NAMING-STANDARD-v1.md)
- Store under `databases\dumps\`
- Update manifest `backup_state` and `rollback_state`

---

## Site files backup

```text
E:\MARS-Localhost\backups\{platform}\{slug}_{yyyyMMdd}_{reason}.zip
```

Exclude `node_modules`, cache dirs, and logs unless debugging charter.

---

## Runtime config backup

Laragon vhost, PHP ini overrides, SSL certs (if custom) — under `backups\runtime\` before MLI-02+ changes.

---

## Reset of synthetic sites

| Step | Action |
|------|--------|
| 1 | Archive validation report to brain |
| 2 | Optional final dump to `databases\dumps\` |
| 3 | Drop database `mars_{platform}_{id}` |
| 4 | Delete or empty site folder |
| 5 | Set manifest `current_status` to `planned` or `archived` |

---

## Project retention

- **No** automatic deletion of `projects\` class sites
- Retention follows project passport and operator decision
- FP-0002 and other active passports are **untouched** by MLI-00

---

## Sandbox deletion

- Default: delete on experiment completion
- Idle **> 30 days** without manifest update → operator review for deletion

---

## Rollback evidence

Each rollback must reference:

- Backup file path(s)
- Manifest revision
- Short report in consumer or MLI `reports/` if non-trivial

---

## No uncontrolled duplicate archives

| Rule | Policy |
|------|--------|
| **BR-01** | One canonical backup set per operation — no scattered copies |
| **BR-02** | Large duplicates go to `archive\` or MARS STORAGE with index note |
| **BR-03** | Do not commit backups to Git |

---

## Related

- [MARS-LOCALHOST-RUNTIME-MANIFEST-CONTRACT-v1.md](MARS-LOCALHOST-RUNTIME-MANIFEST-CONTRACT-v1.md)
- [MARS-LOCALHOST-SITE-CLASSIFICATION-STANDARD-v1.md](MARS-LOCALHOST-SITE-CLASSIFICATION-STANDARD-v1.md)

---

*Backup and reset policy v1 — MLI-00.*
