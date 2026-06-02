# Survivability Preflight Checklist (v1)

**Status:** **documented** — operator checklist before starting AGENT.  
**Time target:** < 2 minutes

**Template:** [safe-agent-task-template-v1.md](safe-agent-task-template-v1.md)  
**Index:** [OPERATIONAL-INDEX.md](../OPERATIONAL-INDEX.md)

---

## Before AGENT start

- [ ] **Lane** declared (A or B)
- [ ] **Safe task template** pasted — all sections filled
- [ ] **TARGET FOLDER** is narrowest root (not whole repo for mutations)
- [ ] **ALLOWED PATHS** — absolute paths, minimal set
- [ ] **FORBIDDEN PATHS** include CRITICAL zones + unlisted workspaces
- [ ] **RISK CLASS** matches planned work
- [ ] **SNAPSHOT** — yes with id, or no with valid reason (SAFE/LOW only)
- [ ] **No unsafe prompt patterns** — no cleanup/wipe/fresh without paths ([safe-prompt-pattern-library-v1.md](../guardrails/safe-prompt-pattern-library-v1.md))
- [ ] **Protected zone check** — [protected-zones-registry-v1.md](../registries/protected-zones-registry-v1.md)
- [ ] **One workspace** — Lane A scoped to single `workspaces/<name>/`
- [ ] **Commit policy** — default no commit unless user requested
- [ ] **Chat name** — `Lane<A|B>-<target>-<phase>`

## If any box unchecked

**Do not start AGENT** — fix task block or switch to ASK read-only.

---

*End of Preflight Checklist v1.*
