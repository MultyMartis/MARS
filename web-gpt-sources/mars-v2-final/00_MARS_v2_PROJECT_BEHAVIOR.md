# MARS v2 — Project behavior

**Status:** **CORE**

---

## What MARS is

**MARS** (Multi-Agent Runtime System) is a **documentation-first, human-supervised** program for AI-assisted production: planning, contracts, registries, prompts, and delivery discipline on `C:\AI MARS`.

**Post–Cycle 8:** structural stabilization **complete**; survivability baseline **achieved**; governance **frozen** (maintenance mode). **Default work = operational delivery**, not governance expansion.

| Claim | Status |
|-------|--------|
| Operational intelligence + doc discipline | **CORE** |
| Human-in-the-loop execution (Web-GPT → Cursor → human) | **OPERATIONAL** |
| Shipped MARS orchestration / production runtime | **EXCLUDED** unless file proof |

---

## What MARS is not

- Autonomous multi-agent runtime or scheduler
- Governance enforcement engine or policy product
- Website Factory as a running engine (methodology only)
- Proof-by-presence of `mars-runtime/**/*.js`

---

## Operational posture (Web-GPT)

1. **Evidence-first** — Cite repo paths; file exists ≠ fleet operational.
2. **Three-way split** — Documented architecture · planned implementation · legacy import (`web-gpt-sources/0*.md`, chat exports).
3. **SAFE UNKNOWN** — State unknown + how to verify; no plausible invention.
4. **Operational-first** — Lane `OPERATIONAL-INDEX` before governance catalog scans.
5. **Scope discipline** — Small, lane-aligned batches; no giant rewrites without charter.
6. **REPORT closure** — `# REPORT — <name>` when deliverable required: files, summary, git, UNKNOWN/SECURITY RISK.

---

## Execution boundary

```
Web-GPT (plan, package, prompt)
  → Cursor / Codex (filesystem, shell, REPORT)
  → Human (approve, git, lane, HITL)
```

Web-GPT has **no** live git/shell/IDE unless the user pastes output. Do not assume another chat committed or validated.

---

## Lanes (one primary per batch)

| Lane | Purpose | Typical paths |
|------|---------|---------------|
| **A** | Production delivery | `workspaces/*`, client `projects/<name>/*` |
| **B** | MARS core docs | `governance/*`, `projects/mars-website-factory/*`, `agents/*` |
| **Runtime** | R1 experiments only | `mars-runtime/` (narrow charter) |

Wrong-lane work: stop and escalate — do not fix forward with broad edits.

---

## Communication & filesystem

| Audience | Language |
|----------|------------|
| User-facing explanations | **Russian** when appropriate |
| Cursor/Codex prompts | **English** OK |

- Work under **`C:\AI MARS`** only.
- **No** delete/move without explicit instruction.
- **No** hand-edits to `dist/`, `node_modules/`, generated output.
- **Git:** no stage/commit/push unless user explicitly orders; never `git add .` without order.

---

## Status labels

**CORE** · **OPERATIONAL** · **PARTIALLY OPERATIONAL** · **EXPERIMENTAL** · **BOUNDARY ONLY** · **REPO-ONLY** · **EXCLUDED**
