# Forge WordPress Filesystem Scope Contract v1

**Document type:** Filesystem authority boundary  
**Version:** v1  
**Stage:** FW-04

---

## Mandatory scope declaration

Every Forge WordPress Cursor prompt **must** include:

```text
Allowed write scope:
Read-only scope:
Forbidden scope:
```

Absence of scope declaration is a **preflight failure**.

---

## Allowed write scope

| Path class | Purpose |
|------------|---------|
| Active project WordPress workspace | Theme, functionality plugin, ACF JSON, local config |
| Forge WordPress project artifacts | WAD, maps, specs, validation reports for active project |
| Local validation output | Screenshots, diff reports, PHPCS output in project validation folder |
| Release output | Staged release package in project release folder |
| Capability task reports | When task explicitly authorizes report write |

**Typical pattern (FW-05+):**

```text
<project-wp-workspace>/wp-content/themes/<theme-slug>/
<project-wp-workspace>/wp-content/plugins/<plugin-slug>/
<project-artifacts>/forge-wordpress/
<project-artifacts>/validation/
<project-artifacts>/release/
```

Exact paths are declared per project intake — not invented by agent.

---

## Read-only scope

| Path class | Purpose |
|------------|---------|
| Approved frontend source | HTML, SCSS, assets, build output — **no edits** |
| MARS canonical standards | Contracts, standards, capability skills/validators |
| WPilot contracts | Handoff requirements — read for packaging |
| External evidence | Client briefs, design exports — read only |
| WordPress core (when local) | Reference only — no edits |
| Vendor plugins (when local) | Reference only — no edits without approval |

---

## Prohibited scope

| Path class | Reason |
|------------|--------|
| Unrelated projects | Scope isolation |
| Production hosting | No production access |
| Global system directories | Safety |
| Token / credential folders | Security |
| Unrelated MARS WIP | Contamination risk |
| WordPress core outside active runtime | Core is read-only reference |
| Client uploads outside controlled workspace | Data boundary |
| `agents/registry.md` | No autonomous registration |
| `.recovery-temp/` | Not project authority |
| FP-0002 or other client workspaces | Unless task explicitly targets that project |

---

## Scope enforcement

1. **Preflight:** Verify declared paths exist or will be created within allowed scope.
2. **During implementation:** STOP on first write outside allowed scope.
3. **Report:** List every path written; flag any read that touched forbidden scope.
4. **Git:** Follow [FORGE-WORDPRESS-GIT-WORKFLOW-v1.md](FORGE-WORDPRESS-GIT-WORKFLOW-v1.md) — selective staging only.

---

## Related

- [../../FORGE-WORDPRESS-REPOSITORY-AND-FILESYSTEM-MODEL-v1.md](../../FORGE-WORDPRESS-REPOSITORY-AND-FILESYSTEM-MODEL-v1.md)
- [../../FORGE-WORDPRESS-SAFE-COMMAND-POLICY-v1.md](../../FORGE-WORDPRESS-SAFE-COMMAND-POLICY-v1.md)
- [FORGE-WORDPRESS-SPECIALIST-EXECUTION-CONTRACT-v1.md](FORGE-WORDPRESS-SPECIALIST-EXECUTION-CONTRACT-v1.md)

---

*Filesystem scope contract v1.*
