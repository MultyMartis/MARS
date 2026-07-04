# Remote Operations Layer (ROL)

**Status:** `MINIMAL_CHARTER`
**Maturity:** `L2 STRUCTURED_CONTRACT` / not implemented runtime
**Mode:** `HUMAN_INVOKED` / `NOT_AUTOMATED`
**project_id:** `mars-remote-operations-layer`

## What This Is

**ROL** = **Remote Operations Layer**.

ROL is the minimal repo-native charter and discipline pack for **safe, human-supervised remote operations** against external systems.

It exists so remote work is not improvised: target identity, environment class, action class, credentials boundary, backup/rollback, evidence, operator approval, and stop conditions must be explicit before any remote mutation is proposed or performed.

## Scope

ROL discipline applies when work may touch:

- hosting panels and accounts;
- FTP / SFTP;
- CMS admin surfaces;
- WordPress;
- OpenCart / ocStore;
- DB / phpMyAdmin;
- external APIs;
- n8n / MetaBOT live workflows;
- remote files;
- credentials / tokens (operator-managed only);
- live production surfaces.

## What This Is Not

- `EXCLUDED`: Not a runtime.
- `EXCLUDED`: Not an autonomous operator.
- `EXCLUDED`: Not a credential vault.
- `EXCLUDED`: Not a remote connector.
- `EXCLUDED`: Not permission to access live systems.
- `EXCLUDED`: Not a production control plane.
- `EXCLUDED`: Not a self-managing remote ops product.
- `EXCLUDED`: Not a runtime engine.
- `EXCLUDED`: Not automatic enforcement of remote policy.
- `EXCLUDED`: Not a replacement for WPilot, OCPilot, MetaBOT, or EAR.

Publishing this charter does **not** authorize any remote connection, credential use, or live mutation.

## Relationship To Other Surfaces

| Surface | Relationship |
|---|---|
| **WPilot / OCPilot / MetaBOT / EAR** | Consume ROL discipline when touching remote systems. Programme-specific authority remains in each programme's own OPERATIONAL-INDEX and contracts. ROL does not replace them. |
| **Agent Quality (AQ)** | Defines task/report quality patterns. ROL remote tasks should remain AQ-compatible. AQ does not authorize remote work. |
| **Survivability** | Defines local filesystem safety, protected zones, and halt discipline. ROL covers remote/external surfaces; Survivability covers local repo/storage/runtime roots. |
| **Evidence persistence discipline** | Defines proof and persistence classes. Remote evidence is `REMOTE_ONLY` unless captured and classified per that discipline. |

## Entry Points

| Surface | Use |
|---|---|
| [`OPERATIONAL-INDEX.md`](OPERATIONAL-INDEX.md) | Status, allowed/prohibited use, Core Run |
| [`contracts/remote-operations-charter-v1.md`](contracts/remote-operations-charter-v1.md) | Normative remote operations charter |
| [`templates/remote-task-starter-v1.md`](templates/remote-task-starter-v1.md) | Reusable remote task starter |
| [`gates/remote-report-gate-v1.md`](gates/remote-report-gate-v1.md) | Remote closeout REPORT gate |
| [`checklists/remote-preflight-checklist-v1.md`](checklists/remote-preflight-checklist-v1.md) | Preflight before remote ops |
| [`reports/master-11-rol-charter-minimal-surface-v1.md`](reports/master-11-rol-charter-minimal-surface-v1.md) | MASTER-11 creation report |

## Current Maturity

`MINIMAL_CHARTER`: documentation surfaces only.

ROL is ready for human-invoked use to prepare remote task charters, block unsafe remote tasks, and classify remote evidence requirements.

It does **not** implement connectors, credential storage, live access, or automatic remote policy enforcement.
