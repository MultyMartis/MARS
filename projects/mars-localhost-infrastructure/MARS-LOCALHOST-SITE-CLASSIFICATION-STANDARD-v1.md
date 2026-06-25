# MARS Localhost — Site Classification Standard v1

**Document type:** Site class standard  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-00

---

## Purpose

Classify every site under `E:\MARS-Localhost\sites\` so consumers, backups, retention, and manifests behave consistently.

---

## Classes

### Synthetic

**Definition:** Artificial validation cases **without** client production data.

| Attribute | Value |
|-----------|-------|
| **Purpose** | Capability proof, smoke tests, toolchain validation |
| **Data** | Synthetic fixtures only; no client PII by default |
| **Examples** | `sites\wordpress\synthetic\fws-0001`, `sites\opencart\synthetic\ocs-0001`, `sites\php\synthetic\web-sim-0001` |
| **Authority** | Consumer program (e.g. Forge WordPress FWS-0001) + MLI manifest |
| **Registration** | **Required** — runtime manifest in brain before sustained use |

### Projects

**Definition:** Local runtime copies of **real** projects under controlled operator approval.

| Attribute | Value |
|-----------|-------|
| **Purpose** | Pilot implementation, local preview, import simulation |
| **Data** | Client data **only when explicitly approved** |
| **Examples** | `sites\wordpress\projects\shpigovsky`, `sites\opencart\projects\bzpm`, `sites\opencart\projects\sibcar` |
| **Authority** | Project passport in brain (`C:\AI MARS`) + MLI manifest |
| **Registration** | **Required** — link to FP-ID / site passport |

### Sandboxes

**Definition:** One-off experiments; disposable by default.

| Attribute | Value |
|-----------|-------|
| **Purpose** | Plugin tests, filter experiments, webhook spikes |
| **Data** | Minimal; prefer synthetic |
| **Examples** | `sites\wordpress\sandboxes\acf-test`, `sites\opencart\sandboxes\filter-test`, `sites\php\sandboxes\webhook-test` |
| **Authority** | Operator + optional lightweight manifest |
| **Registration** | **Recommended**; may use short-lived manifest |

---

## Creation rules

| ID | Rule |
|----|------|
| **SC-01** | Choose platform folder (`wordpress`, `opencart`, `php`, `other`) first |
| **SC-02** | Choose class (`synthetic`, `projects`, `sandboxes`) second |
| **SC-03** | Slug must be unique per `platform + class` |
| **SC-04** | Register local domain per [domain standard](MARS-LOCALHOST-DOMAIN-STANDARD-v1.md) |
| **SC-05** | Register database per [database naming standard](MARS-LOCALHOST-DATABASE-NAMING-STANDARD-v1.md) |
| **SC-06** | Create brain manifest before first DB population with non-synthetic data |
| **SC-07** | Do not place client projects in `synthetic\` |
| **SC-08** | Forge/OCPilot WIP sites must not collide with unrelated consumer slugs |

---

## Deletion rules

| Class | Default |
|-------|---------|
| **Synthetic** | Resettable after validation cycle; archive evidence to brain reports first |
| **Projects** | **No** auto-delete; retention per project passport + backup policy |
| **Sandboxes** | Delete when experiment ends; max **30 days** idle without manifest update (operator review) |

---

## Retention

| Class | Retention default |
|-------|-------------------|
| Synthetic | Keep until superseded by newer synthetic ID or explicit reset |
| Projects | Life of project local pilot + mandated backup window |
| Sandboxes | Short-lived; delete unless promoted to `projects\` |

---

## Backup

| Class | Backup expectation |
|-------|-------------------|
| Synthetic | Baseline before major toolchain change; optional after proof |
| Projects | **Required** before destructive change; DB dump + files |
| Sandboxes | Optional; operator discretion |

See [MARS-LOCALHOST-BACKUP-AND-RESET-POLICY-v1.md](MARS-LOCALHOST-BACKUP-AND-RESET-POLICY-v1.md).

---

## Authority

| Layer | Role |
|-------|------|
| **MARS brain** | Manifest, passport, approval for client data |
| **D: runtime** | Executing files only — not governance SoT |
| **Consumer** | Defines validation requirements; does not own D: root |

---

## Allowed data

| Class | Allowed |
|-------|---------|
| Synthetic | Fake content, generated users, public OSS plugins/themes |
| Projects | Approved client exports, sanitized dumps, design assets per charter |
| Sandboxes | Test fixtures; **no** production credentials |

Production credentials and live production DB imports are **prohibited by default**.

---

## Related

- [MARS-LOCALHOST-RUNTIME-MANIFEST-CONTRACT-v1.md](MARS-LOCALHOST-RUNTIME-MANIFEST-CONTRACT-v1.md)
- [MARS-LOCALHOST-DATA-AND-SECRETS-POLICY-v1.md](MARS-LOCALHOST-DATA-AND-SECRETS-POLICY-v1.md)

---

*Site classification standard v1 — MLI-00.*
