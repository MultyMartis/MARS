# MARS — Runtime and Filesystem Boundaries (X-Drive Pack 2026-06)

**SoT:** [governance/mars-x-drive-root-authority-v1.md](../../governance/mars-x-drive-root-authority-v1.md), [projects/mars-survivability/](../../projects/mars-survivability/)

---

## Filesystem write boundary

| Rule | Detail |
|------|--------|
| MARS-controlled writes | **Only** within approved roots on `X:\` |
| Required volume label | **AI WS** — precheck before mutation |
| External reads | Exact operator authorization required |
| Deprecated roots | Write **denied** — historical reference only |

**Policy note:** Cursor can technically write elsewhere — MARS **policy** denies it; this is not OS-level enforcement.

---

## Approved canonical roots

```text
X:\AI MARS\
X:\AI MARS STORAGE\
X:\MARS-Localhost\
```

---

## Deprecated roots (write denied)

```text
C:\AI MARS\
C:\MARS Phenix\
C:\MARS Phenix\AI MARS\
C:\AI MARS STORAGE\
C:\MARS Phenix\AI MARS STORAGE\
D:\MARS-Localhost\
E:\MARS-Localhost\
```

**Classification:** `DEPRECATED ROOT — HISTORICAL REFERENCE — ACCEPTED` in evidence narratives only.

---

## Guard capability truth (honest)

| Capability | State |
|------------|-------|
| Drive allowlist | **CONFIGURED** |
| Canonical root allowlist | **CONFIGURED** |
| Deprecated root denylist | **CONFIGURED** |
| Volume label | **PRECHECK_REQUIRED** |
| Parent traversal (`..`) | **ENFORCED** (validator) |
| UNC rejection | **ENFORCED** (validator) |
| Reparse escape | **PARTIAL** (string-level only) |
| Automatic interception | **NOT ENFORCED** |
| Operator approval | **REQUIRED** (destructive ops) |
| Dry-run / checkpoint | **REQUIRED** (destructive ops) |

**Enforcement surfaces:** `AGENTS.md`, `.cursorrules`, Survivability validator — human-operated.

---

## Runtime honesty

| Claim | Status |
|-------|--------|
| MARS orchestrator / scheduler / queue | **EXCLUDED** — no repo proof |
| Autonomous agent fleet | **EXCLUDED** |
| Governance as runtime policy engine | **EXCLUDED** |
| `mars-runtime/` R1 scripts | **EXPERIMENTAL** — human-invoked only |
| MetaBOT execution | **EXTERNAL** n8n |

**Do not imply** production orchestrator, 24/7 MARS core, or self-managing runtime without path proof.

---

## Destructive operation boundary

Requires: exact path list · dry-run · checkpoint · operator approval · rollback method · audit evidence.

**Prohibited:** deletion/replacement of canonical roots or `X:\` volume root without operator charter.

---

*End of 10_RUNTIME_AND_FILESYSTEM_BOUNDARIES — X-Drive Pack 2026-06.*
