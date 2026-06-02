# Shared

**Area:** Cross-cutting runtime utilities  
**Status:** R1.2 — config loader only

---

## Purpose

Shared runtime utilities used across connectors, builders, and validators — common types, logging conventions, and config binding.

---

## Modules

| Module | Responsibility | Status |
|--------|----------------|--------|
| [config_loader.py](config_loader.py) | Load and validate operator JSON config files | **CREATED** (R1.2) |

### config_loader.py

- Parses JSON config from a local file path (standard library only).
- Validates required fields, enum constraints, and security rules.
- Returns a structured dict on success; raises `ConfigValidationError` on failure.
- **Does not** resolve `credential_ref`, access remotes, read secrets, or create outputs.

---

## Current state

| Field | Value |
|-------|-------|
| **Config loader** | **CREATED** |
| **Other implementations** | **NONE** |
| **Execution** | **NOT AUTHORIZED** |
| **Live access** | **FORBIDDEN** |
