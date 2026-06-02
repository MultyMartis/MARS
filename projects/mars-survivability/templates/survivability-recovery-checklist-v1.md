# Survivability Recovery Checklist (v1)

**Status:** **documented** — operator checklist after incident or workspace failure.  
**Time target:** use fully — do not skip steps under pressure

**Protocol:** [workspace-quarantine-protocol-v1.md](../protocols/workspace-quarantine-protocol-v1.md)  
**Halt:** [operational-halt-protocol-v1.md](../protocols/operational-halt-protocol-v1.md)

---

## Immediate (first 5 minutes)

- [ ] **Stop AGENT** — no further mutations
- [ ] **HALT signal** acknowledged if agent still running
- [ ] **Read-only audit** — `git status`, list missing/changed paths
- [ ] **Do not** second-wave cleanup or delete-recreate
- [ ] **Log** — append to `logs/incidents/` (one-line minimum)

## Quarantine

- [ ] **Trigger identified** — contaminated / drift / broken / partial-rebuild
- [ ] **Human move** to `workspaces/_quarantine/q-<date>-<slug>-<condition>/`
- [ ] **QUARANTINE-MANIFEST.md** written
- [ ] **Production path frozen** — no fix-on-top

## Restore source selection

- [ ] **Snapshot** — manifest complete? ([snapshot-manifest-standard-v1.md](../protocols/snapshot-manifest-standard-v1.md))
- [ ] **Git** — known-good commit identified?
- [ ] **Template** — `_template-client-v1` or factory template?
- [ ] **SAFE UNKNOWN** marked where evidence missing

## Staging and promote

- [ ] Restore to `workspaces/_recovery/` first (recommended)
- [ ] **Integrity checks** — file presence, diff, optional build
- [ ] **Human promote** to production path
- [ ] **Rollback log** — `logs/rollback-history/`

## Post-recovery

- [ ] **Mandatory new chat** — [chat-context-drift-protocol-v1.md](../protocols/chat-context-drift-protocol-v1.md)
- [ ] **REPORT** — changed files, execution safety, SAFE UNKNOWN
- [ ] **Drill** — schedule D-02 if production incident

---

*End of Recovery Checklist v1.*
