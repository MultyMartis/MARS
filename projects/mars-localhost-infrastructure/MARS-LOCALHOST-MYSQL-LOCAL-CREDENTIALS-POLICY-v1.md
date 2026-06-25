# MARS Localhost — MySQL Local Credentials Policy v1

**Document type:** MySQL local credentials and exposure policy  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-02

---

## Principles

- **Local-only** credentials; never production reuse.
- **No passwords in Git** or brain documentation.
- Secrets in runtime-only files on D: (operator-controlled).

---

## Accounts

| Account | MLI-02 usage |
|---------|----------------|
| `root` | Laragon default local root — operator-managed password on D: only |
| Per-runtime users | **Recommended** from MLI-03 — `{slug}_app` with least privilege |

---

## Exposure (MLI-02 verified; superseded for bind by MLI-03R.1)

| Check | Finding |
|-------|---------|
| Server version | 8.4.3 |
| Local connection | **PASS** (`SELECT VERSION()`) |
| `bind_address` variable | **`127.0.0.1`** (MLI-03R.1 post-reboot) |
| Listening | **`127.0.0.1:3306` only** |
| X Protocol 33060 | **Disabled** (`mysqlx=0`) |
| Remote access | **Not intentionally enabled** |
| WordPress DB | **Not created** in MLI-02 |

---

## Naming

Follow [MARS-LOCALHOST-DATABASE-NAMING-STANDARD-v1.md](MARS-LOCALHOST-DATABASE-NAMING-STANDARD-v1.md).

---

## Dump / reset

Per [MARS-LOCALHOST-BACKUP-AND-RESET-POLICY-v1.md](MARS-LOCALHOST-BACKUP-AND-RESET-POLICY-v1.md). No production dumps on MLI host.

---

## MLI-03 recommendation

Create dedicated DB/user per WordPress runtime; restrict bind to `127.0.0.1` when compatible with Laragon profile. See [MARS-LOCALHOST-DATABASE-STANDARD-v1.md](MARS-LOCALHOST-DATABASE-STANDARD-v1.md) (MLI-03R.1).

---

*MySQL local credentials policy v1 — MLI-02; exposure updated MLI-03R.1.*
