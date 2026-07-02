# SITE-002 Production Profile

**Site ID:** SITE-002  
**Project:** ЗПМ / BZPM  
**Document role:** Production environment registration — **not** connection authorization  
**Last updated:** 2026-07-02

---

## Profile status

| Field | Value |
|-------|-------|
| Profile status | **REGISTERED — NOT CONNECTED** |
| Remote access status | **NOT VERIFIED** |
| Production operations | **NOT YET AUTHORIZED** |

---

## Identity

| Field | Value |
|-------|-------|
| Site ID | SITE-002 |
| Project | ЗПМ / BZPM |
| Environment ID | `site-002-prod` |
| Environment type | **PRODUCTION** |
| Production URL | https://bzpm.ru/ |
| Historical TEST URL | https://zpm.new-site.space/ |
| Platform | ocStore / OpenCart |
| Exact platform version | **SAFE UNKNOWN** unless already verified |
| OCPilot owner | `projects/ocpilot/sites/site-002/` |
| Operator model | human-supervised / HITL |

---

## Environment roles

### Production

**URL:** https://bzpm.ru/

Current operational website authority. Production was created by transferring the approved TEST website. OCPilot treats this URL as the present-day operational target for SITE-002 Production work once connection is authorized.

### Historical TEST

**URL:** https://zpm.new-site.space/

Previous implementation and verification environment. Preserve as historical evidence and optional future test environment. **Do not treat as current Production authority.**

| Field | Value |
|-------|-------|
| Production parity with latest TEST checkpoints | **SAFE UNKNOWN** |

Do not claim that Production exactly matches TEST unless evidence proves it.

---

## Authority bindings

| Document | Path |
|----------|------|
| Site passport | [site-passport.md](site-passport.md) |
| Project access brief | [project-access-brief.md](project-access-brief.md) |
| OCPilot state | [../../OCPILOT-STATE.md](../../OCPILOT-STATE.md) |
| Operational index | [../../OPERATIONAL-INDEX.md](../../OPERATIONAL-INDEX.md) |
| Project site registry | [../../project-site-registry.md](../../project-site-registry.md) |
| Technical knowledge map | [knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) |
| Current M9.x baselines | [baselines/](baselines/) — TEST-proven checkpoints |
| Post-corporate-page checkpoints | Home Commercial Trust · Corporate Intro · Custom Proof Strip · Delivery Summary · PDP Body Category Classes |
| Production baseline placeholder | [baselines/SITE-002-PRODUCTION-BASELINE-PENDING.md](baselines/SITE-002-PRODUCTION-BASELINE-PENDING.md) |

---

## Current implementation inheritance

Production is **believed** to inherit the transferred TEST state including:

| Area | Evidence class |
|------|----------------|
| M9.13 About | TEST-proven implementation |
| M9.14 Delivery | TEST-proven implementation |
| M9.15 Payment | TEST-proven implementation |
| M9.16 Dealers | TEST-proven implementation |
| M9.17 Warranty | TEST-proven implementation |
| M9.18 Custom Manufacturing | TEST-proven implementation |
| Post-corporate polish checkpoints | TEST-proven implementation |
| Local Fonts checkpoint | TEST-proven implementation |
| Home Commercial Trust checkpoint | TEST-proven implementation |

| Classification | Value |
|----------------|-------|
| Implementation evidence | **TEST-PROVEN IMPLEMENTATION** |
| Production parity | **PRODUCTION PARITY NOT YET VERIFIED** |

---

## Storage bindings

**Production storage root:**

```text
X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\
```

| Subfolder | Purpose |
|-----------|---------|
| `backups\` | Scoped pre-change Production backups |
| `baselines\` | Promoted Production baseline artefacts (future) |
| `captures\` | Read-only remote inventory and page captures |
| `deployments\` | Deployment manifests and scoped deploy evidence |
| `verification\` | HTTP smoke, visual verification, operator sign-off evidence |
| `rollback\` | Rollback packages and restore evidence |
| `reports\` | Production operation reports |

**Shared image directories:** reuse existing SITE-002 shared image storage when appropriate. Do not duplicate the image library unless a Production-specific image area is explicitly required.

**Storage README:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\README.md`

---

## Credential binding

**Canonical secrets file:**

```text
X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md
```

| Section | Use |
|---------|-----|
| `TEST` | Historical TEST environment credentials |
| `PRODUCTION` | Production environment credentials — operator to populate |

**Supported categories:** FTP / SFTP · Hosting panel · OpenCart Admin · SSH · Database · DNS / Domain · Additional Notes

| Rule | Value |
|------|-------|
| Database access | **NOT AUTHORIZED BY DEFAULT** |
| Secrets in Git | **FORBIDDEN** |
| Credential testing (this registration) | **NOT PERFORMED** |

---

## Operation model

Future Production write sequence (human-supervised):

1. Read Production Profile
2. Read local secrets (`PRODUCTION` section)
3. Confirm exact target (URL, environment ID, remote path)
4. Create scoped backup
5. Prepare local diff and manifest
6. Obtain operator approval
7. Deploy exact scope
8. Verify HTTP and visual result
9. Keep rollback ready
10. Produce report

**Recommended operation identifier:** `SITE-002-PROD-YYYYMMDD-NN`

---

## Approval gates

Every Production **write** requires:

| Gate | Required |
|------|----------|
| Exact task scope | yes |
| Exact remote path | yes |
| Backup | yes |
| Rollback method | yes |
| Operator approval | yes |
| Post-change verification | yes |

Read-only inspection does **not** require a separate approval gate once Production connection has been explicitly authorized for read-only work.

---

## Protected zones

Protected by default — separate explicit task and operator authorization required:

| Zone | Notes |
|------|-------|
| `config.php` | Core configuration |
| `admin/config.php` | Admin configuration |
| `system/` | Core system |
| `storage/` | OpenCart storage |
| `image/catalog/` bulk operations | Mass image changes |
| Payment modules | Checkout-related |
| Checkout | Order flow |
| Cron | Scheduled jobs |
| Database | **NOT AUTHORIZED BY DEFAULT** |
| Server configuration | Hosting-level |
| DNS | Domain routing |
| Mail configuration | SMTP / mail |

Protected does **not** mean permanently forbidden.

---

## Deploy, rollback, and verification bindings (registered, not verified)

| Profile | Storage binding | Status |
|---------|-----------------|--------|
| Deploy profile | `production\deployments\` | REGISTERED, NOT VERIFIED |
| Rollback profile | `production\rollback\` | REGISTERED, NOT VERIFIED |
| Verification profile | `production\verification\` | REGISTERED, NOT VERIFIED |

Future Production tooling must:

- use the `PRODUCTION` section of the local secrets file;
- use `X:\` paths;
- avoid hardcoded credentials;
- avoid historical `C:\MARS Phenix` paths;
- support exact file scope;
- support backup and rollback;
- produce a manifest.

Deploy-tool preparation is a **separate task**.

---

## Registration state

| Item | State |
|------|-------|
| Production identity | **REGISTERED** |
| Production URL | **REGISTERED** |
| Storage bindings | **REGISTERED** |
| Credential slots | **REGISTERED** |
| Credentials populated | **OPERATOR ACTION REQUIRED** |
| Remote connection | **NOT PERFORMED** |
| Production baseline | **PENDING FIRST READ-ONLY CAPTURE** |
| Deploy profile | **REGISTERED, NOT VERIFIED** |
| Rollback profile | **REGISTERED, NOT VERIFIED** |
| Verification profile | **REGISTERED, NOT VERIFIED** |
| First Production change | **NOT YET AUTHORIZED** |

---

## Related documents

- Registration report: [reports/SITE-002-PRODUCTION-PROFILE-REGISTRATION.md](reports/SITE-002-PRODUCTION-PROFILE-REGISTRATION.md)
- External storage registry: [../../external-storage-registry.md](../../external-storage-registry.md)
- Recovery closeout: [reports/SITE-002-BZPM-RECOVERY-CLOSEOUT-REGISTRATION.md](reports/SITE-002-BZPM-RECOVERY-CLOSEOUT-REGISTRATION.md)
