# MARS v2 — Bootstrap and migration

**Status:** **OPERATIONAL**

---

## Starting a new Web-GPT MARS v2 chat

### 1. Charter message (initialization)

Include:

- Repo: **`D:\AI MARS`**
- Mode: **AGENT** or advisory per user
- Rules: `AGENTS.md` honesty; **SAFE UNKNOWN**; Russian for user-facing text if requested
- Git: **no** stage/commit/push unless explicit order; never `git add .`

### 2. Load this pack (order)

Use [README.md](README.md) load order:

1. `00_MARS_v2_PROJECT_BEHAVIOR.md`  
2. `01_MARS_v2_GOVERNANCE_CORE.md`  
3. `02_MARS_v2_EXECUTION_MODEL.md`  
4. `03_MARS_v2_REALITY_AND_BOUNDARIES.md`  
5. `04_MARS_v2_WEBSITE_FACTORY_CONTEXT.md` (if Factory work)  
6. `05_MARS_v2_RUNTIME_BOUNDARY.md`  
7. `06_MARS_v2_BOOTSTRAP_AND_MIGRATION.md` (this file)

**Minimum truth bundle:** `00` + `03` + `05`.

### 3. Fresh repo evidence

New chat has **zero** IDE/git attachment. Require:

```
git status --short -uall
```

from user before claiming clean tree, lane purity, or commit state.

### 4. Lane verification

Record before work:

| Field | Example |
|-------|---------|
| **Active lane** | A / B / Runtime (one primary per batch) |
| **Allowed paths** | Per lane table in `00` |
| **Forbidden paths** | e.g. Lane A → no governance rewrites |
| **Next commit** | Planned lane or “no commit planned” |

### 5. Begin scoped work

- Small change set matching lane  
- Close with `# REPORT — …` if task required deliverable  

---

## Reconstructing context (without old chat memory)

| Need | Source in repo (re-verify) |
|------|----------------------------|
| What MARS is / is not | `README.md`, `AGENTS.md` |
| Stage / roadmap posture | `governance/master-build-map.md`, `logs/lifecycle-log.md` |
| Project facts | `registry/project-registry.md` |
| Factory entry | `projects/mars-website-factory/OPERATIONAL-INDEX.md` |
| Runtime honesty | `mars-runtime/README.md`, this pack `05` |
| Tools/helpers | `tools/README.md` — manual pilots only |

**Do not** treat chat exports as SoT.

---

## Old chat migration artifacts

Legacy folder: `web-gpt-sources/chat-migration/` — **HISTORICAL** aids.

| Artifact | Use |
|----------|-----|
| `10-new-chat-bootstrap-sequence.md` | Superseded in spirit by this pack + `00` |
| `06-runtime-boundaries.md` | Consolidated into `05` |
| `07-safe-unknown-boundaries.md` | Consolidated into `03` |
| `02-current-operational-state.md` (if any) | **Snapshot only** — replace with fresh `git status` |

**Historical only:** pasted migration bundles, old numbered `web-gpt-sources/*.md` topics, superseded phase notes.

**Must re-verify from repo:** governance vs legacy pack conflicts, registry rows, R1 scope, MetaBOT vs legacy seo-agent folder, Triumph V2 canonical paths (`V2-CANONICAL-STATE.md` in project pack).

---

## What the new chat must acknowledge

- MARS = **governance-centered operational intelligence**; **documentation-first** Phase 1  
- **HITL** for risky moves  
- Triumph, Website Factory, MetaBOT = **different** canonical folders and execution owners  
- Font Awesome Pro = **local licensed asset**, **EXCLUDED** from packs  

## What the new chat must NOT assume

- Scheduler, validator service, auto-deploy, hidden daemon  
- Prior chat committed or cleaned the tree  
- `seo-content-agent/` is canonical (use **metabot** pack)  
- Vendor/font trees cleared for commit without operator license confirmation  

---

## Onboarding minimum (repo-native)

If operator opens repo directly (not only Web-GPT):

1. `README.md`  
2. `AGENTS.md`  
3. `governance/README.md` (task-scoped)  
4. `governance/parallel-cursor-chat-work-mode-v0.md` (if multi-chat Cursor)  

Stop unless task needs deeper files.

---

## Conflict resolution

If this pack disagrees with `governance/` or `AGENTS.md`:

- Treat **governance + AGENTS** as honesty baseline  
- Mark conflicting slice **SAFE UNKNOWN** until human reconciles in-repo  

---

## Recommended next step after pack load

1. User pastes fresh **`git status --short -uall`**.  
2. Declare **lane** and **scope** for the batch.  
3. Open **one** authoritative in-repo doc for the task (registry row or pack index entry).  
4. Proceed with prompt → Cursor/Codex → REPORT loop per `02`.
