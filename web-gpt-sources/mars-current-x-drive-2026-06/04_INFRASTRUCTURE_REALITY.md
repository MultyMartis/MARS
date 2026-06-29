# MARS — Infrastructure Reality (X-Drive Pack 2026-06)

**SoT:** [governance/mars-infrastructure-reality-v1.md](../../governance/mars-infrastructure-reality-v1.md), [governance/mars-x-drive-root-authority-v1.md](../../governance/mars-x-drive-root-authority-v1.md)

---

## Canonical model

| Layer | Path | Role |
|-------|------|------|
| **Active Brain** | `X:\AI MARS\` | Single Git repository — governance, projects, workspaces, docs |
| **Storage Layer** | `X:\AI MARS STORAGE\` | Out-of-Git bulk — backups, archives, Knowledge Center, promoted artefacts |
| **Local Runtime** | `X:\MARS-Localhost\` | Laragon, CMS sites, databases, logs — execution only |

| Property | Required value |
|----------|----------------|
| Drive | `X:` |
| Volume label | **AI WS** |
| Branch (development) | `mars/canonical-post-recovery` |
| Recovery anchor (immutable) | `recovery/mars-phenix-2026-06-25` @ `fe9d9c8e` |

---

## Normative rules

1. **One Git repository** — `X:\AI MARS\` only for MARS brain and agent scope.
2. **Storage is out-of-Git** — not a second repo, not a governance root.
3. **Localhost is runtime** — not repository; governance stays on Active Brain.
4. **`X:\AI MARS\storage\`** — in-repo **documentation** folder (architecture contracts) — **≠** `X:\AI MARS STORAGE\`.
5. **MARS-controlled writes** — limited to approved roots on `X:`.
6. **External reads** — require exact operator authorization; prefer copy to `X:\AI MARS STORAGE\incoming\`.
7. **OS/Application caches** — may remain outside `X:` — not claimed as MARS-controlled.

---

## Deprecated operational roots

**Classification:** `NOT CURRENT OPERATIONAL PATH` · `WRITE DENIED` · `MAY REMAIN IN HISTORICAL EVIDENCE`

```text
C:\AI MARS\
C:\MARS Phenix\
C:\MARS Phenix\AI MARS\
C:\AI MARS STORAGE\
C:\MARS Phenix\AI MARS STORAGE\
D:\MARS-Localhost\
E:\MARS-Localhost\
```

Do **not** present these as current operational targets. Incident narratives and recovery reports **retain original paths** — do not rewrite.

---

## Historical vs active

| Path pattern | Classification |
|--------------|----------------|
| `X:\AI MARS\`, `X:\AI MARS STORAGE\`, `X:\MARS-Localhost\` | **Current operational** |
| `C:\MARS Phenix\AI MARS` | **Historical / deprecated** — Phoenix-era |
| `C:\AI MARS`, `C:\AI MARS STORAGE` | **Legacy hold** — pre-Phoenix |
| `D:\MARS-Localhost`, `E:\MARS-Localhost` | **Historical runtime** — incident evidence |
| Programme docs with old paths | **Drift pending** — X9 audit scope |

---

## Volume preflight

Before filesystem mutation: confirm drive `X:` and label **AI WS** (`Get-Volume -DriveLetter X`).  
Mismatch → **STOP — X VOLUME IDENTITY MISMATCH**.

---

*End of 04_INFRASTRUCTURE_REALITY — X-Drive Pack 2026-06.*
