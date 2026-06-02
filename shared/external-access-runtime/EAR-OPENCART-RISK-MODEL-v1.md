# EAR OpenCart Risk Model v1

**Purpose:** Per-channel acquisition risks, failure modes, and **expected EAR behavior** (documentation discipline — not automated enforcement).  
**Status:** design only — **no** runtime.  
**Phase:** 2C  
**Parent:** [EAR-OPENCART-ACQUISITION-DESIGN-v1.md](EAR-OPENCART-ACQUISITION-DESIGN-v1.md)

Aligns with [EAR-FAILURE-MODELS-v1.md](EAR-FAILURE-MODELS-v1.md) and [EAR-SECURITY-MODEL-v1.md](EAR-SECURITY-MODEL-v1.md).

---

## Risk categories (cross-channel)

| Category | Definition | EAR expected behavior |
|----------|------------|------------------------|
| **Credential exposure** | Secrets in git, logs, snapshot package, or chat | **Stop** assembly; redact; never Publish; operator rotates creds if leaked |
| **Partial evidence** | Section missing but level claimed | **Downgrade** quality at Validate; populate `safe-unknown`; block Publish at inflated level |
| **Version mismatch** | Metadata claim ≠ detected version files | Record both; prefer `Detected version`; flag in `safe-unknown` if unresolved |
| **Modified environments** | TEST evidence applied to PRODUCTION claim or vice versa | **Halt** Publish until `environment` reconciled; operator re-Request |
| **Missing artifacts** | Checklist item not delivered | `safe-unknown` entry with unblock hint; scoped re-Request |
| **False assumptions** | Consumer or operator infers completeness from empty sections | EAR docs + Validate gate; consumer guide blocks phases |
| **Read-only violations** | Write/install/SQL mutation during acquisition | **Halt** cycle; incident note; no Publish; separate charter for recovery |

---

## Per-channel risk register

### ZIP Archive

| Risk | Severity | Expected EAR behavior |
|------|----------|------------------------|
| Credential exposure in `config.php` | Critical | Reject git-bound copy; require redacted excerpt or external bulk only |
| Zip bomb / malware | High | Operator external scan policy; EAR does not auto-extract in v1 |
| Stale archive | Medium | Document `acquisition-log` date; `safe-unknown` if live corroboration missing |
| Wrong archive root | Medium | Validate manifest root folders; fail Level 1 if standard roots absent |
| Partial tree | Medium | Partial level only; list missing paths in `safe-unknown` |

---

### SFTP

| Risk | Severity | Expected EAR behavior |
|------|----------|------------------------|
| Credential exposure | Critical | No creds in package; `acquisition-log` channel name only |
| Accidental write | Critical | Halt; operator confirms read-only client settings |
| Wrong chroot root | High | Manifest sanity check vs OpenCart layout |
| Incomplete listing | Medium | Do not infer missing extensions; `safe-unknown` |
| Symlink traversal | Medium | Operator policy; document exclusions |

---

### FTP

| Risk | Severity | Expected EAR behavior |
|------|----------|------------------------|
| Cleartext credential interception | Critical | Prefer SFTP in Request; document FTPS-only if charter requires |
| Fragile listing | Medium | Retry or switch channel in hybrid path |
| Same as SFTP operational risks | Medium | Same behaviors |

---

### SSH

| Risk | Severity | Expected EAR behavior |
|------|----------|------------------------|
| Destructive command | Critical | Halt acquisition; no Publish; operator incident |
| Credential/key in scripts | Critical | No keys in git; external secrets only |
| Production shell access | High | Require TEST confirmation in Request |
| Read-only DB user missing | Medium | Fall back to PMA or `database-metadata` safe-unknown |

---

### Hosting Panel

| Risk | Severity | Expected EAR behavior |
|------|----------|------------------------|
| Wrong site/account | Critical | Verify `site_id` and URL in Request before Acquire |
| Accidental restore/delete | Critical | Operator supervision only; no EAR automation |
| Non-reproducible listing | Medium | Export to file; attach to external bulk; reference in metadata |
| Backup vs live mismatch | Medium | Record backup date; downgrade if stale |

---

### OpenCart Admin

| Risk | Severity | Expected EAR behavior |
|------|----------|------------------------|
| Misclick install/save | Critical | Halt; operator confirms no change; separate rollback charter if needed |
| Admin list ≠ filesystem | Medium | Corroborate with file channel or `safe-unknown` |
| Cache side effects | Low | Document in `acquisition-log`; do not treat as structural change without evidence |
| Session on production | High | Request must specify TEST; halt if mismatch |

---

### phpMyAdmin Export

| Risk | Severity | Expected EAR behavior |
|------|----------|------------------------|
| Full dump with PII | Critical | Reject for package; structure-only or table list |
| Accidental import | Critical | Operator discipline; read-only export path only |
| Secrets in `oc_setting` | High | Metadata keys only per spec; no row dumps in git |
| Export size limit | Medium | Partial table list + `safe-unknown` |

---

### Browser Evidence

| Risk | Severity | Expected EAR behavior |
|------|----------|------------------------|
| False assumptions from screenshots | High | Cap published level at **0** unless corroborated |
| Non-reproducible | Medium | Mark evidence type in `acquisition-log`; weak manifest |
| OCR/interpretation errors | Medium | Operator-verified text preferred over OCR |

---

### Hybrid Acquisition

| Risk | Severity | Expected EAR behavior |
|------|----------|------------------------|
| Timestamp mismatch across channels | High | Record window in `acquisition-log`; `safe-unknown` if conflict |
| Conflicting extension lists | Medium | Prefer filesystem scan; admin as secondary |
| Duplicate work / gaps | Low | Scoped re-Request for missing sections only |

---

## Validate-stage decision table

| Observation at Validate | EAR action |
|-------------------------|------------|
| Secret detected in candidate package | Fail; redact; no Publish |
| Level N required section missing | Downgrade to highest honest level or fail |
| Version mismatch unresolved | Publish at ≤1 with `safe-unknown` on version-dependent phases |
| `environment` PRODUCTION without charter | Fail |
| Read-only violation suspected | Fail; escalate per [EAR-FAILURE-MODELS-v1.md](EAR-FAILURE-MODELS-v1.md) |
| Residual unknowns acceptable for target level | Publish with documented `safe-unknown` |

---

## Consumer handoff risks

| Risk | Expected EAR behavior |
|------|------------------------|
| Consumer treats snapshot as live access | Consumer guide: snapshot only; no creds |
| Consumer runs phases blocked by `safe-unknown` | Consumer responsibility; cite snapshot level |
| Direct consumer FTP bypass | Discouraged — document in [EAR-OPENCART-DESIGN-DECISIONS-v1.md](EAR-OPENCART-DESIGN-DECISIONS-v1.md) |

---

## SAFE UNKNOWN

- Automated secret scanning at Validate — not implemented in-repo.
- Insurance/legal classification of PII in accidental dumps — operator/legal, not EAR.

---

## Cross-references

| Document | Use |
|----------|-----|
| [EAR-FAILURE-MODELS-v1.md](EAR-FAILURE-MODELS-v1.md) | Global failure taxonomy |
| [EAR-READINESS-GATES-v1.md](EAR-READINESS-GATES-v1.md) | G0–G4 gates |
| [EAR-OPENCART-SNAPSHOT-PATHS-v1.md](EAR-OPENCART-SNAPSHOT-PATHS-v1.md) | Path anti-patterns |
