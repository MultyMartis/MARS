# Configs

**Area:** Operator-supplied runtime configuration fixtures  
**Status:** R1.2 — sample fixtures only; no credential resolution

---

## Purpose

Holds JSON configuration files consumed by the EAR Runtime CLI via `--config`. Configs describe site/pilot binding, connector class, scope, and output targets — **not** inline secrets.

---

## Current state

| Field | Value |
|-------|-------|
| **Sample configs** | **YES** — `sample-r1-site-001.json` |
| **Credential resolution** | **NONE** |
| **Live access** | **FORBIDDEN** |

---

## Sample files

| File | Description |
|------|-------------|
| [sample-r1-site-001.json](sample-r1-site-001.json) | PILOT-001 / SITE-001 fixture — placeholder refs only, `dry_run: true` |

---

## Security rules

- **No** passwords, tokens, keys, or inline secrets in committed configs.
- `credential_ref` is an **external reference label** — resolved outside git in later phases (not R1.2).
- Placeholder values use `SAFE_UNKNOWN_*` prefixes where real paths are unknown.

---

## Usage

From `runtime/`:

```text
py -3 cli.py --config configs/sample-r1-site-001.json
```

Validation is performed by [../shared/config_loader.py](../shared/config_loader.py). Invalid configs fail closed with a non-zero exit code.
