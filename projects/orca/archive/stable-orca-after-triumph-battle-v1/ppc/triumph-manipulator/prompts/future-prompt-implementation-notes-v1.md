# Future Prompt Implementation Notes v1

**Status:** Possibilities and targets only — **nothing in this document is implemented** in the Triumph Manipulator pack unless separately proven in-repo.

**Posture:** Post–Cycle 8 operational-first · human-supervised · isolated from MARS governance truth.

---

## What may be built later (not now)

### 1. Versioned prompt template files

- `prompts/templates/intake-v1.txt`  
- `prompts/templates/campaign-skeleton-v1.txt`  
- Semantic versioning aligned with `schema_version`  
- Changelog per template — operator-reviewed  

**Not built in Phase 6** — only architecture docs.

### 2. Cursor workflow integration

- `.cursor/rules` snippet referencing pack OPERATIONAL-INDEX Core Run  
- Session types: `orca-intake`, `orca-generate`, `orca-fix`  
- Mandatory attachment: intake brief + doctrine path  
- JSON-only output rule enforced in rule file  

**Boundary:** Cursor assists editing — no background agent.

### 3. Structured AI pipelines (human-triggered)

```
CLI or script:
  orca-ppc assist intake --brief in.json
  orca-ppc assist generate --from brief.json --out draft.json
  orca-ppc validate --in draft.json --report vr.json
  orca-ppc assist fix --doc draft.json --report vr.json --out draft2.json
```

Each step **blocks** on human confirmation flag file — no unattended chain.

### 4. Prompt registry (documentation index)

| prompt_id | version | class | doc_ref |
|-----------|---------|-------|---------|
| triumph.intake.master | 1 | intake | intake-prompt-patterns-v1.md |
| triumph.campaign.skeleton | 1 | generation | campaign-generation-prompts-v1.md |

Future registry is **catalog only** — not a running prompt router.

### 5. Prompt versioning policy

- Bump minor on wording tightening  
- Bump major on schema_version change  
- Never retro-edit templates without migration note  

### 6. n8n workflows (experimental lane)

Possible **human-triggered** flows (from [export/future-implementation-hooks-v0.md](../export/future-implementation-hooks-v0.md)):

| Flow | Trigger | Stops before |
|------|---------|--------------|
| Intake form → brief JSON | Webhook manual | Campaign gen |
| Validate webhook → Slack notify | After human uploads JSON | Export |
| Export notify → operator email | After G4 approval | Import |

**Forbidden in n8n design:**

- Scheduled launch loops  
- Auto-import to Direct API without human  
- Autonomous keyword expansion cron  
- Writing to governance/ or mars-runtime/  

### 7. Batch generation

Batch = multiple **documents** or **groups** processed sequentially with per-item human approval — not one-shot 1000 ads.

```
for group in approved_groups:
    wait human_approve(batch_item)
    generate ad JSON
```

---

## Integration with validation / exporter (future)

| Stage | Future tool | Pack contract today |
|-------|-------------|---------------------|
| Validate | `orca-validate` CLI | validation/*.md |
| Export | `orca-export` CLI | exporter/*.md |
| Prompt assist | `orca-assist` | prompts/*.md |

Prompt CLI must **not** embed validation logic — call validator module.

Exporter remains **transport-only** — [exporter/exporter-engine-overview-v1.md](../exporter/exporter-engine-overview-v1.md).

---

## MARS / Factory hooks (Phase 8+)

- Landing blueprint IDs in JSON → Factory page acceptance  
- Continuity registry for prompt lessons learned — optional, human-maintained  
- **No** default governance expansion  

---

## Explicit non-goals (all phases until chartered)

| Non-goal | Reason |
|----------|--------|
| Daemon / watcher | Autonomous runtime |
| Agent swarm | Policy + AGENTS.md honesty |
| Auto-launch | human-review-gates-v1.md |
| RAG over full pack per prompt | Context entropy — Core Run only |
| Prompt “optimizer” that rewrites live Direct | Human authority |

---

## Evidence rule

When implementation starts, update:

- [README.md](../README.md) operational status table  
- [OPERATIONAL-INDEX.md](../OPERATIONAL-INDEX.md) Core Run row  
- This file — move sections from “future” to “implemented” with file paths  

Until then: **SAFE UNKNOWN** on runtime availability.

---

## Suggested Phase 7 focus

n8n **human-triggered** workflow design doc — wire intake → notify → export prep without orchestration product claims. See pack README Phase table.
