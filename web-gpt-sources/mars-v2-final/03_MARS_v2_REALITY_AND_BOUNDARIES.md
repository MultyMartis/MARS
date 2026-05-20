# MARS v2 — Reality and boundaries

**Status:** **CORE**

---

## Operational vs conceptual

| Operational (today) | Conceptual / planned |
|---------------------|----------------------|
| Human + Cursor/Codex + REPORT | Autonomous orchestration |
| Markdown contracts & indexes | Control plane product |
| Lane OPERATIONAL-INDEX navigation | “Read everything first” bootstrap |
| Optional R1 manual scripts | Fleet-wide MARS runtime |

**Stabilization baseline achieved** — do not treat pre–Cycle 8 “endless stabilization” as blocking delivery.

---

## SAFE UNKNOWN (required)

When evidence is missing:

- **Unknown** — what is not known  
- **Why** — no file, no paste, stale map  
- **Verify** — `git status`, open path, live external check  
- **Risk if wrong** — lane mix, false deploy, license commit  

Prefer **SAFE UNKNOWN** over bare **UNKNOWN**. Mark when: git state not pasted, live integration unverified, deploy/secrets unnamed, Validator PASS without human evidence.

---

## Evidence tiers

| Strong | Weak |
|--------|------|
| Cited in-repo paths + behavior | Chat agreement alone |
| Pasted `git status` / command output | Filename implies runtime |
| Human REPORT with scope | Lifecycle log without map check |
| External live config (operator-verified) | Stale migration paste |

Always apply **three-way split** (documented · planned · legacy).

---

## Forbidden runtime claims (rewrite without proof)

- Fully **autonomous** agents/runtime/factory  
- **Production orchestrator** (in-repo)  
- **Automatic agent coordination** / self-managing production **now**  
- **Enforces policy** across repository  
- **Daemon** / queue consumer as **shipped MARS**  
- **End-to-end verified by MARS** without human scope  

**Allowed when accurate:** documented, contract v0, planned, experimental R1, human-in-the-loop, Web-GPT → Cursor path.

---

## Mythology warnings

| Pattern | Fix |
|---------|-----|
| Pilot named as capability | pilot / draft / experimental |
| Registry row = deployed tool | cite runtime-registry boundaries |
| Helpers = enforcers | restate S5 manual posture |
| Governance inflation | narrow SoT; maintenance only |

---

## External systems (BOUNDARY ONLY)

| System | MARS relationship |
|--------|-------------------|
| **MetaBOT** | External n8n; canonical `projects/metabot-seo-content-agent/` |
| **WPilot** | Documented bridge boundary |
| **Cursor / Web-GPT** | Execution surfaces — not MARS core |
| **Legacy `seo-content-agent/`** | **EXCLUDED** — use MetaBOT pack |

---

## Not MARS core

| Item | Class |
|------|-------|
| Triumph `workspaces/*/src/**` | **REPO-ONLY** delivery |
| Font Awesome Pro vendor tree | **EXCLUDED** from packs |
| `dist/`, build output | **EXCLUDED** — source only |
| Old numbered `web-gpt-sources/0*.md` | **REPO-ONLY** legacy |
| `chat-migration/` snapshots | Historical — re-verify |

**MARS is NOT:** production runtime, autonomous orchestration, governance engine.
