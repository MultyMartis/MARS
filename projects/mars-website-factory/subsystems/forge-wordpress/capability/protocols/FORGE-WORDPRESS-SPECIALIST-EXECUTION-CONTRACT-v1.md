# Forge WordPress Specialist Execution Contract v1

**Document type:** Mandatory execution protocol  
**Version:** v1  
**Stage:** FW-04  
**Applies to:** Forge WordPress Implementation Specialist (Cursor Agent)

---

## Mandatory cycle

Every Forge WordPress task **must** follow this cycle in order:

```text
1. PREFLIGHT
2. CONTEXT LOAD
3. SCOPE LOCK
4. PLAN
5. HUMAN GATE
6. IMPLEMENT
7. SELF-VALIDATE
8. INDEPENDENT VALIDATE
9. REPORT
10. HUMAN ACCEPTANCE
```

Skipping stages is **forbidden** unless the task charter explicitly limits scope (e.g. inspection-only).

---

## Stage definitions

### 1. PREFLIGHT

| Field | Value |
|-------|-------|
| **Inputs** | Task prompt, project identity, stage ID |
| **Allowed actions** | `git status`, read intake, verify frontend approval state |
| **Outputs** | Preflight checklist result |
| **Stop conditions** | Missing project ID, unapproved frontend, production target |
| **Required report** | Preflight section in task report |
| **Human gate** | None |

### 2. CONTEXT LOAD

| Field | Value |
|-------|-------|
| **Inputs** | Tier list per [FORGE-WORDPRESS-CONTEXT-LOADING-MODEL-v1.md](FORGE-WORDPRESS-CONTEXT-LOADING-MODEL-v1.md) |
| **Allowed actions** | Read authorized documents only |
| **Outputs** | Context load manifest (files read, tiers loaded) |
| **Stop conditions** | Required authority missing; context overload |
| **Required report** | Inputs section listing loaded authorities |
| **Human gate** | None |

### 3. SCOPE LOCK

| Field | Value |
|-------|-------|
| **Inputs** | [FORGE-WORDPRESS-FILESYSTEM-SCOPE-CONTRACT-v1.md](FORGE-WORDPRESS-FILESYSTEM-SCOPE-CONTRACT-v1.md) |
| **Allowed actions** | Declare allowed write, read-only, forbidden scope |
| **Outputs** | Scope declaration block in prompt/report |
| **Stop conditions** | Write target outside allowed scope |
| **Required report** | Scope section |
| **Human gate** | None |

### 4. PLAN

| Field | Value |
|-------|-------|
| **Inputs** | Skills for current phase, prior artifacts |
| **Allowed actions** | Draft plans, maps, specs — **no code** unless task is implementation |
| **Outputs** | Plan artifact or implementation spec draft |
| **Stop conditions** | WAD missing before implementation planning; content model missing before ACF |
| **Required report** | Plan summary |
| **Human gate** | **Required** before IMPLEMENT for architecture, content model, implementation spec |

### 5. HUMAN GATE

| Field | Value |
|-------|-------|
| **Inputs** | Plan artifacts from stage 4 |
| **Allowed actions** | Present plan; wait for operator approval |
| **Outputs** | Recorded approval or revision request |
| **Stop conditions** | No approval — do not proceed to IMPLEMENT |
| **Required report** | Gate status: APPROVED / REVISION REQUIRED / BLOCKED |
| **Human gate** | **BLOCKING** |

### 6. IMPLEMENT

| Field | Value |
|-------|-------|
| **Inputs** | Approved plan, WAD, content model, implementation spec |
| **Allowed actions** | Write theme/plugin files within scope; run approved local commands |
| **Outputs** | Implementation files |
| **Stop conditions** | Plan not approved; scope violation; unsafe command |
| **Required report** | Files created/updated |
| **Human gate** | None during implementation; stop on blocker |

**Forbidden before this stage:**

- Implementation before approved plan
- Implementation before WAD
- Implementation before content model (when content-driven)
- Silent architecture changes
- Silent plugin additions
- Silent database changes
- Production commands

### 7. SELF-VALIDATE

| Field | Value |
|-------|-------|
| **Inputs** | Implementation output, validation plan |
| **Allowed actions** | Run self-check skills (FW-SK-11 partial); PHPCS read; structural checks |
| **Outputs** | Self-validation notes |
| **Stop conditions** | Blocking self-check failure |
| **Required report** | Validation section (self) |
| **Human gate** | None |

### 8. INDEPENDENT VALIDATE

| Field | Value |
|-------|-------|
| **Inputs** | Artifacts, diff, validator profiles FW-V-01–07 |
| **Allowed actions** | Independent Cursor pass or operator-assigned review |
| **Outputs** | Validator reports |
| **Stop conditions** | Blocking validator finding |
| **Required report** | Validation section (independent) |
| **Human gate** | Visual parity (WV6) — operator approval required |

Per [FORGE-WORDPRESS-VALIDATOR-INDEPENDENCE-POLICY-v1.md](FORGE-WORDPRESS-VALIDATOR-INDEPENDENCE-POLICY-v1.md): implementer **must not** approve own WV6 or security pass.

### 9. REPORT

| Field | Value |
|-------|-------|
| **Inputs** | All stage outputs |
| **Allowed actions** | Write report per [FORGE-WORDPRESS-REPORTING-STANDARD-v1.md](FORGE-WORDPRESS-REPORTING-STANDARD-v1.md) |
| **Outputs** | `# REPORT — <TASK NAME>` |
| **Stop conditions** | None |
| **Required report** | Full report |
| **Human gate** | None |

### 10. HUMAN ACCEPTANCE

| Field | Value |
|-------|-------|
| **Inputs** | Complete report |
| **Allowed actions** | Operator reviews and accepts or requests revision |
| **Outputs** | Acceptance record |
| **Stop conditions** | Rejection — return to appropriate stage |
| **Required report** | Next authorized action |
| **Human gate** | **BLOCKING** for stage completion |

---

## Global prohibitions

- Implementation before approved plan
- Implementation before WAD
- Implementation before content model (when applicable)
- Silent architecture changes
- Silent plugin additions
- Silent database changes
- Production commands or production URLs in artifacts
- Autonomous git commit (per [FORGE-WORDPRESS-GIT-WORKFLOW-v1.md](FORGE-WORDPRESS-GIT-WORKFLOW-v1.md))

---

## Related

- [FORGE-WORDPRESS-CONTEXT-LOADING-MODEL-v1.md](FORGE-WORDPRESS-CONTEXT-LOADING-MODEL-v1.md)
- [FORGE-WORDPRESS-FILESYSTEM-SCOPE-CONTRACT-v1.md](FORGE-WORDPRESS-FILESYSTEM-SCOPE-CONTRACT-v1.md)
- [FORGE-WORDPRESS-VALIDATOR-INDEPENDENCE-POLICY-v1.md](FORGE-WORDPRESS-VALIDATOR-INDEPENDENCE-POLICY-v1.md)
- [FORGE-WORDPRESS-REPORTING-STANDARD-v1.md](FORGE-WORDPRESS-REPORTING-STANDARD-v1.md)
- [FORGE-WORDPRESS-GIT-WORKFLOW-v1.md](FORGE-WORDPRESS-GIT-WORKFLOW-v1.md)

---

*Execution contract v1 — human-supervised; no autonomous bypass.*
