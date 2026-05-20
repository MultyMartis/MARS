# MARS v2 — Operational chat discipline

**Status:** **CORE** / **OPERATIONAL**

---

## Purpose

Multi-chat workflows: **one role per chat**, lane isolation, human-supervised execution. Reduce entropy — prompt drift, lane contamination, chat memory as false SoT.

**Post–Cycle 8 default:** operational delivery chats — not Governance/Validation unless chartered.

---

## Declare at start

```
ACTIVE LANE: A | B | Runtime
CHAT TYPE: <see table>
```

| Chat type | Scope |
|-----------|--------|
| **Frontend Production** | `workspaces/*`, client projects |
| **Website Factory** | Factory methodology, contracts (Lane B) |
| **Governance** | `governance/*` maintenance — **not** default delivery |
| **Runtime Research** | `mars-runtime/` — boundary language only |
| **Validation** | Audits, REPORT verify — event-driven, not blocking startup |
| **Design Production** | Visual/mockups — no runtime claims |
| **Migration** | Bootstrap hygiene — then exit to operational lane |
| **External Systems** | MetaBOT, n8n, deploy — explicit boundaries |

**Invalid:** Lane A + Chat type Governance without charter.

---

## Lane rules

- **One primary lane** per execution batch (one prompt → one REPORT).  
- Cross-lane batch = explicit charter + forbidden paths.  
- Wrong lane → stop; do not fix forward with broad edits.

---

## Source priority

| P | Source |
|---|--------|
| P0 | `AGENTS.md` |
| P1 | This pack (`web-gpt-sources/mars-v2-final/`) |
| P2 | In-repo docs for task (OPERATIONAL-INDEX row, contracts) |
| P3 | Current user charter |
| P4 | Pasted evidence (`git status`, file contents) |
| P5 | Old chats / exports — **historical only** |

Missing P4 → **SAFE UNKNOWN**, do not upgrade P5.

---

## Avoid governance gravity

| Anti-pattern | Risk |
|--------------|------|
| Universal super-chat | Wrong-lane edits, mythology |
| Governance chat for landing HTML | Scope corruption |
| Full S0–S7 read before delivery | Operator fatigue, no ship |
| Chat memory as SoT | Stale vs current tree |

**Handoff:** close with REPORT → new chat declares lane/type + fresh `git status`.

---

## Cursor prompt hygiene

- Metadata **outside** copy block; body = plain text, no nested fences.  
- Include: GOAL, SCOPE, forbidden paths, lane/type, REPORT requirement.  
- State: no commit unless ordered.  
- No mega-prompts by default — split governance vs implementation.

---

## REPORT standard

```
# REPORT — <task name>

## What was done
## Files affected
## SAFE UNKNOWN
## Risks
## Next step
```

Plus when applicable: git summary, SECURITY RISK, explicit no-commit.

---

## Pre-flight (major work)

Operator pastes:

```
git status --short -uall
```

Declare: lane, scope, forbidden paths, commit intent.

---

## Anti-chaos summary

- Operational-first; stabilization already done — ship work  
- No fake runtime / hidden orchestration  
- No vendor pollution in packs  
- One REPORT format per batch  

*Cross-ref: `00` behavior · `02` loop · `06` bootstrap · `08` ecosystem state.*
