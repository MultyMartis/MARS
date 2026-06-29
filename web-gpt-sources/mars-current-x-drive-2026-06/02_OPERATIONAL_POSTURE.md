# MARS — Operational Posture (X-Drive Pack 2026-06)

**Status:** **CORE**  
**Canonical reference:** [governance/mars-operational-evolution-state-after-cycles-1-8-v0.md](../../governance/mars-operational-evolution-state-after-cycles-1-8-v0.md)

---

## Post–Cycle 8 posture

| Dimension | State |
|-----------|--------|
| Governance | **Maintenance mode** — frozen baseline; light hygiene only |
| Primary effort | **Operational-first** — delivery before governance expansion |
| Default session | Lane **OPERATIONAL-INDEX** → ship work + **REPORT** |
| New governance waves | Require **explicit human charter** |

---

## Delivery-first workflow

1. Select **one lane** and **one programme OPERATIONAL-INDEX** per task batch.
2. Execute exact chartered scope — no scope creep.
3. Close with **REPORT** when deliverable required.
4. Git: selective staging — **no** `git add .`, **no** broad commits without charter.

---

## Foreign WIP protection

- Re-verify `git status` every session.
- **Preserve** foreign WIP — do not stage, restore, clean, or reset unrelated changes.
- Do not assume another chat committed work.

---

## X-drive filesystem boundary

| Rule | Detail |
|------|--------|
| MARS-controlled writes | Only within approved roots on `X:` |
| Volume preflight | Confirm label **AI WS** before filesystem mutation |
| Deprecated roots | `C:\AI MARS\`, `C:\MARS Phenix\`, `C:\AI MARS STORAGE\`, `D:\MARS-Localhost\`, `E:\MARS-Localhost\` — **write denied** |
| External reads | Exact operator authorization required |
| Destructive ops | Dry-run, checkpoint, approval, rollback evidence |

---

## Required session start

```text
1. Verify workspace is X:\AI MARS
2. Verify volume label is AI WS when filesystem work is involved
3. Read AGENTS.md and .cursorrules
4. Select one programme OPERATIONAL-INDEX
5. Inspect git status
6. Preserve foreign WIP
7. Execute exact scope
8. Close with REPORT
```

---

## Lanes (one primary per batch)

| Lane | Purpose | Typical paths |
|------|---------|---------------|
| **A** | Production delivery | `workspaces/*`, client programme workspaces |
| **B** | MARS core / docs / packs | `governance/*`, `projects/*`, `registry/`, `web-gpt-sources/` |
| **Runtime** | R1 experiments only | `mars-runtime/` (explicit charter) |

---

## REPORT closeout

When task requires reporting:

- Start with `# REPORT — <task/stage name>`
- List changed files, summary, git status
- Mark **UNKNOWN** / **SECURITY RISK** when applicable
- Default: **no commit** unless operator requests

---

## Selective Git discipline

| Allowed | Prohibited without charter |
|---------|---------------------------|
| Stage explicit task files | `git add .`, `git add -A` |
| One scoped commit per wave | `git commit -a`, `git stash`, `git reset`, `git clean` |
| Push when requested | Force push, broad restore |

---

*End of 02_OPERATIONAL_POSTURE — X-Drive Pack 2026-06.*
