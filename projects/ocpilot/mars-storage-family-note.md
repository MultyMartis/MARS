# MARS — External Storage Family Note

**Run:** OCPilot 3.7 (global note — documentation only)  
**Status:** family architecture guidance — **no** folders created for other systems in this run.

---

## Approved MARS bulk root

```
X:\AI MARS STORAGE
```

This is the **general MARS bulk-data root** for artifacts that should not live permanently in the git repository at `X:\AI MARS`.

**Migration evidence (pre-X-drive):** `C:\MARS Phenix\AI MARS STORAGE` · repo `C:\MARS Phenix\AI MARS` / `C:\AI MARS`.

The MARS repo holds documentation, governance references, operational metadata, and small durable artifacts. The storage root holds large binaries, vendor trees, site archives, snapshots, and temporary extracts.

**External storage is not a git repository by default.**

---

## Design principles

| Principle | Meaning |
|-----------|---------|
| **One root, many systems** | Single approved bulk root; each MARS entity gets its own top-level subfolder |
| **No mixed storage** | Do not place OCPilot ZIPs in `wpilot/` or dump unrelated files at storage root |
| **No dumping at root** | Files go only under the correct system folder |
| **Metadata in repo** | Passports, manifests, policies, and reports stay in `X:\AI MARS` |
| **Bulk outside repo** | Canonical ZIPs, promoted trees, site archives, DB snapshots, temp extracts |
| **Human-operated** | No automated storage engine, sync product, or enforcement layer claimed |

---

## Current top-level layout (Run 3.7)

```
X:\AI MARS STORAGE\
  README.md
  ocpilot\          ← created Run 3.7
```

---

## Future system folders (not created in Run 3.7)

Each global entity **must** have its own top-level folder when bulk storage is chartered:

| Entity | Illustrative folder | Notes |
|--------|---------------------|-------|
| **OCPilot** | `ocpilot\` | OpenCart pilot — **active** ([external-storage-registry.md](external-storage-registry.md)) |
| **WPilot** | `wpilot\` | WordPress pilot bulk — TBD |
| **ORCA** | `orca\` | Battle pilot / freeze artifacts — TBD |
| **MetaBOT** | `metabot\` | MetaBOT bulk — TBD |
| **Website Factory** | `website-factory\` | Factory exports — TBD |
| **Shared vendor/download** | `shared\` | Only if explicitly chartered; shared does not mean mixed baseline/site dumps |

Creating these folders requires a **separate human charter** per system — not implied by OCPilot Run 3.7.

---

## Credentials and secrets

| Rule | Meaning |
|------|---------|
| **Default: no credentials** | Storage root is not for API keys, DB passwords, or live `config.php` secrets |
| **Operator approval required** | If secrets must exist outside repo, operator must approve and define protection (encryption, access control) |
| **Never git-track secrets** | MARS repo policy unchanged — see per-system boundaries |

---

## How systems should reference this root

1. **System-specific registry** — e.g. OCPilot [external-storage-registry.md](external-storage-registry.md).
2. **Passports / manifests** — record external path + checksum, not bulk file lists in git.
3. **Family note (this doc)** — cross-system orientation only; not a substitute for per-system policy.
4. **Root README** — `X:\AI MARS STORAGE\README.md` for operator onboarding.

---

## Relationship to MARS governance

This note is **operational documentation** under `projects/ocpilot/` as the initiating Run 3.7 artifact. It does **not** expand governance catalog or claim registry engines. For external system boundaries in MARS, see governance docs only when explicitly chartered — not modified in Run 3.7.

---

## SAFE UNKNOWN

- Whether `X:\AI MARS STORAGE` will use cloud sync, NAS, or second-machine mirror — operator infrastructure.
- Whether a dedicated git repo or LFS will ever apply to storage root — **not recommended** as default.
- Exact folder names for WPilot/ORCA when chartered — may differ from illustrative table above.
