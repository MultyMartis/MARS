# REPORT — SITE-002 First Controlled Production Change

**OCPilot run:** 4.173  
**Operation ID:** SITE-002-PROD-TEXT-CHANGE-01  
**Date:** 2026-07-04  
**Environment:** PRODUCTION  
**Production URL:** https://bzpm.ru/

---

## 1. Scope

Controlled single-file Production deploy for SITE-002 warranty page.

Exact replacement:

```text
понятный порядок действий
```

to:

```text
чёткий порядок действий
```

Only one authorized file was in scope.

---

## 2. Pre-flight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS\` |
| Volume | `X:` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD before operation | `5a6d1bc367658419eb997c9b9074689fa6ad6971` |
| Previous OCPilot run | 4.172 |
| Current OCPilot run | 4.173 |
| Foreign WIP | Preserved; not staged by this operation |

Authority confirmed:

| Field | Value |
|-------|-------|
| Production baseline before | `SITE-002-STABLE-PROD-INITIAL-01` |
| Application root | `/bzpm.ru/` |
| FTP login root | `/` |
| FTP-visible public root | `/public_html/` |
| Production status | READY FOR FIRST CONTROLLED PRODUCTION CHANGE |

---

## 3. Target

| Field | Value |
|-------|-------|
| Page | https://bzpm.ru/guarantee |
| Hosting path | `/bzpm.ru/public_html/catalog/view/theme/default/template/information/guarantee.twig` |
| FTP-visible path | `/public_html/catalog/view/theme/default/template/information/guarantee.twig` |
| Target file count | 1 |

---

## 4. Source acquisition

Fresh Production file was downloaded immediately before preparation.

| Field | Value |
|-------|-------|
| Local source | `source/guarantee.twig` |
| Remote size | 46856 bytes |
| Remote modified time | `213 20260701180721` |
| Download timestamp | `2026-07-03T18:38:26+00:00` |
| Source SHA-256 | `f10dedc1ce196eebcf7024c916a581e4599b624fe2aee5c1a115afc817089556` |

---

## 5. Precondition

| Check | Result |
|-------|--------|
| Old text match count | 1 |
| New text before deploy | 0 |
| Precondition | PASS |

---

## 6. Backup

| Backup | SHA-256 |
|--------|---------|
| `backup/guarantee.twig.pre-change.bak` | `f10dedc1ce196eebcf7024c916a581e4599b624fe2aee5c1a115afc817089556` |
| Source | `f10dedc1ce196eebcf7024c916a581e4599b624fe2aee5c1a115afc817089556` |

`backup_sha256 == source_sha256`: PASS.

---

## 7. Dry-run

| Check | Result |
|-------|--------|
| Remote files to upload | 1 |
| Remote files to delete | 0 |
| Remote files to rename | 0 |
| Replacement count | 1 |
| Backup available | YES |
| Rollback file available | YES |
| Database impact | NONE |
| CSS/JS impact | NONE |
| Diff scope | PASS — one semantic line replacement |

Prepared SHA-256:

```text
0bf5aee97f1c1b52b9715b4f6cdeaa5116aff9f7e2377fe27a80b9b2bf166fe6
```

---

## 8. Rollback readiness

Rollback file prepared before upload:

```text
rollback/guarantee.twig
```

| Check | Result |
|-------|--------|
| Rollback SHA-256 | `f10dedc1ce196eebcf7024c916a581e4599b624fe2aee5c1a115afc817089556` |
| Rollback equals source | PASS |
| Rollback plan manifest | CREATED |

Rollback was not executed because deploy and verification passed.

---

## 9. Deploy

Final pre-upload check downloaded the remote file again:

| Check | Result |
|-------|--------|
| `remote_pre_upload_sha256` | `f10dedc1ce196eebcf7024c916a581e4599b624fe2aee5c1a115afc817089556` |
| Equals source SHA-256 | PASS |

Upload:

| Field | Value |
|-------|-------|
| Uploaded local file | `prepared/guarantee.twig` |
| Remote target | `/public_html/catalog/view/theme/default/template/information/guarantee.twig` |
| Upload count | 1 |
| Deletes / renames / directory operations | 0 / 0 / 0 |

---

## 10. File-level verification

Remote file was downloaded after upload as:

```text
verification/remote-after-upload.twig
```

| Check | Result |
|-------|--------|
| Remote after SHA-256 | `0bf5aee97f1c1b52b9715b4f6cdeaa5116aff9f7e2377fe27a80b9b2bf166fe6` |
| Prepared SHA-256 | `0bf5aee97f1c1b52b9715b4f6cdeaa5116aff9f7e2377fe27a80b9b2bf166fe6` |
| Hash match | PASS |
| Old text count | 0 |
| New text count | 1 |

---

## 11. HTTP verification

| Check | Result |
|-------|--------|
| URL | https://bzpm.ru/guarantee |
| Status code | 200 |
| New phrase in normalized HTML | 1 |
| Old target phrase in normalized HTML | 0 |
| HTTP verification | PASS |

Response evidence recorded in `manifests/http-verification.json`.

---

## 12. Visual verification

| Viewport | Result | File |
|----------|--------|------|
| Desktop 1440×1200 | PASS | `verification/desktop-guarantee.png` |
| Mobile 390×844 | PASS | `verification/mobile-guarantee.png` |

Checks passed:

- Page opened successfully.
- Changed paragraph text was visible.
- Old target phrase was absent.
- No visible Twig/PHP error marker was detected.
- Page body was not blank.

---

## 13. Rollback status

```text
READY — NOT EXECUTED
```

Rollback readiness is verified by source/rollback SHA equality and saved rollback plan. No automatic rollback condition was triggered.

---

## 14. Storage artefacts

Deployment root:

```text
X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-TEXT-CHANGE-01\
```

Created subfolders:

```text
source\
prepared\
backup\
verification\
rollback\
manifests\
logs\
```

Key manifests:

- `operation.json`
- `precondition.json`
- `dry-run.md`
- `dry-run.json`
- `rollback-plan.md`
- `rollback-plan.json`
- `deploy-manifest.json`
- `file-hashes.json`
- `http-verification.json`
- `visual-verification.json`
- `operation-receipt.json`

---

## 15. Checkpoint

Created Production checkpoint:

```text
SITE-002-STABLE-PROD-TEXT-CHANGE-01
```

Storage:

```text
X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\baselines\SITE-002-STABLE-PROD-TEXT-CHANGE-01\
```

Repository:

```text
projects/ocpilot/sites/site-002/baselines/SITE-002-STABLE-PROD-TEXT-CHANGE-01.md
```

Parent baseline: `SITE-002-STABLE-PROD-INITIAL-01`.

---

## 16. Authority updates

Updated scoped repository authority:

- `projects/ocpilot/sites/site-002/production-profile.md`
- `projects/ocpilot/sites/site-002/site-passport.md`
- `projects/ocpilot/sites/site-002/project-access-brief.md`
- `projects/ocpilot/sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md`
- `projects/ocpilot/OCPILOT-STATE.md`
- `projects/ocpilot/OPERATIONAL-INDEX.md`

Recorded proof boundary:

```text
single-file text-only FTP deploy with backup and rollback readiness
```

No generic deploy tooling claim was made.

---

## 17. Remote mutation summary

```text
Remote uploads: 1
Remote edits through upload: 1
Remote deletes: 0
Remote renames: 0
Database operations: 0
Admin saves: 0
```

---

## 18. Git status

Repository Git handling is scoped to repository files of this operation only. Storage artefacts, secrets, Production Twig files, backups, screenshots, HTML captures, and manifests under Storage are excluded from Git.

Foreign WIP existed before this operation and remains outside the operation scope. Full-tree `git diff --check` reports unrelated whitespace issues in foreign WIP; scoped `git diff --check -- <operation files>` passes.

---

## 19. Final verdict

```text
SITE-002 FIRST CONTROLLED PRODUCTION CHANGE COMPLETE — DEPLOY AND ROLLBACK READINESS VERIFIED
```
