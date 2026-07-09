# MetaBOT — n8n Project Development Rules v1

**Status:** **documented** — human-operated discipline for MARS-assisted n8n workflow design and evolution.  
**Applies to:** MetaBOT SEO Agent and future **MetaBOT-compatible** products unless a separate charter overrides.

**Not:** automated enforcement, CI policy, or n8n product configuration.

---

## Principles

1. **Live n8n is execution truth** — repo holds sanitized knowledge only.  
2. **No credentials in repo** — ever.  
3. **Read before write** — audit live + docs before proposing graph changes.  
4. **Operator approval before deploy** — MARS assists; operator executes.  
5. **Evidence after change** — reproducible record for rollback.

See [integration-boundary.md](integration-boundary.md), [metabot-developer-concept-v1.md](metabot-developer-concept-v1.md).

---

## 1. Read-only audit before changes

Before editing workflows or preparing new JSON:

| Step | Action |
|------|--------|
| A | Read canonical docs: [mega-map.md](mega-map.md), [workflow-map.md](workflow-map.md), task-specific workflow doc |
| B | Read [known-issues.md](known-issues.md) for regression risks |
| C | Inspect live n8n graphs (operator access) — node names, webhooks, credentials **by reference** |
| D | Compare to last sanitized export in `exports/` if any — note **legacy vs current** |
| E | Record gaps as **SAFE UNKNOWN** — do not guess node order or error branches |

**Forbidden:** proposing deploy from markdown paraphrase alone without live graph review.

---

## 2. Live n8n parity check

After doc or export updates, state parity explicitly:

| Parity level | Meaning |
|--------------|---------|
| **VERIFIED** | Operator attests live graph matches described behavior |
| **PARTIAL** | Known drift listed |
| **UNKNOWN** | No live access this session |

Parity applies to: workflow count (Intake/Worker/Admin), webhook paths, Telegram command routing, Sheets tables, Worker version (v13 reference).

---

## 3. Sanitized export discipline

| Rule | Detail |
|------|--------|
| Redact | API keys, tokens, OAuth secrets, private URLs with tokens |
| Redact | Personal data beyond what operator chooses to publish |
| Label | File name + doc note: `legacy`, `v13`, date, scope |
| Location | Committed: `exports/` only when sanitized · Full: `raw/` **gitignored** |
| Never | Commit inline credentials in Code nodes (MIG report **SECURITY RISK** precedent) |

---

## 4. No credentials in repo

- OpenRouter, Telegram, Google Sheets/service accounts — **n8n credentials** or env on host only.
- Docs may say “OpenRouter node in Worker” — not the key.
- `config/env.example` pattern (MIG style) — reference variable **names** only if added for MetaBOT ops docs.

---

## 5. Raw exports policy

| Storage | Allowed content |
|---------|-----------------|
| `projects/metabot-seo-content-agent/raw/` | Full n8n JSON — **local, gitignored** |
| `X:\AI MARS STORAGE\incoming\` | Operator bulk drops when chartered |
| Git repo | **Sanitized only** |

Operator must scrub before any commit.

---

## 6. Importable JSON policy

Importable workflow JSON in repo must:

- be **sanitized**;
- include header comment or companion doc: purpose, workflow role (Intake/Worker/Admin), version, **not for deploy without review**;
- avoid `Execute Workflow` chain ambiguity — document webhook handoff if following MetaBOT v13/v14 pattern;
- stay **namespaced** — SEO Agent paths must not collide with MIG `mig/*` webhooks.

**Distinction:** importable JSON = **candidate** for operator import · not auto-deployed.

---

## 7. Node code policy

| Rule | Detail |
|------|--------|
| Prefer | Shared library pattern for complex logic (MIG `session-spine` precedent) when reuse is real |
| Document | Code node purpose in workflow doc — not only inside minified JS |
| Avoid | Hardcoded API keys, spreadsheet IDs unless operator explicitly publishes non-secret IDs elsewhere |
| Review | Routing parsers (Telegram `task_raw`, `from:task_id`, `--strict`) against [telegram-commands.md](telegram-commands.md) |
| Security | No `eval` of untrusted input; validate webhook payloads at boundary |

---

## 8. Webhook contract policy

- Document: method, path, required fields, response shape — in prose or small schema doc.
- Webhook **utility ≠ orchestrator** — [governance/adapter-and-bridge-boundaries.md](../../governance/adapter-and-bridge-boundaries.md).
- Intake → Worker / Admin: prefer **Webhook → Webhook** pattern per MIG/MetaBOT design study unless live graph proves otherwise.
- MARS bridge payloads: align with [integrations/n8n-mars-bridge-map-code.txt](integrations/n8n-mars-bridge-map-code.txt) only when bridge is in scope.

**SAFE UNKNOWN** until published: formal JSON Schema for all webhooks.

---

## 9. Google Sheets schema documentation policy

- Document **table roles** ([storage-layer.md](storage-layer.md)): memory, `seo_active_jobs`, etc.
- Column-level detail: mark **SAFE UNKNOWN** unless exported schema or operator doc exists.
- Document quota/rate-limit risks ([known-issues.md](known-issues.md)).
- Do not commit live spreadsheet IDs unless operator approves as non-secret.

---

## 10. Telegram command documentation policy

- [telegram-commands.md](telegram-commands.md) tracks **intended** surface; live bot may differ.
- On change: update commands doc + [seo-specialist-user-guide.md](seo-specialist-user-guide.md) if user-visible.
- Document strict canonical forms: `/seoqa --strict from:task_id`, `/factcheck --strict from:task_id`.
- Bot handle `@seo_content_agent_bot` — **OPERATOR_CLARIFICATION**; verify in BotFather/live before claims.

---

## 11. OpenRouter prompt / model documentation policy

- Document **which stages** call models (outline, text, cleanup, seoqa, factcheck) at workflow level.
- Prompt text: prefer operator-owned evidence pack or sanitized excerpts — avoid dumping full production prompts without review.
- Model IDs: document in ops notes or evidence pack; **SAFE UNKNOWN** in repo unless operator publishes.
- Temperature / mode maps: reference [exports/workflow-sanitized-legacy.json](exports/workflow-sanitized-legacy.json) only as **legacy** hint.

---

## 12. Test cases before deployment

Minimum matrix before operator deploy approval:

| Area | Example checks |
|------|----------------|
| Intake | `/help`, busy/lock rejection, route to Worker |
| Worker | `/outline`, `/text`, `/run`, `/get`, reuse `from:` |
| Quality | `/seoqa --strict from:…`, `/factcheck --strict from:…` |
| Admin | `/locks`, health (quota-aware), `/stop-all-flow` |
| Locks | No duplicate concurrent conflict; note known pending drift |
| Sheets | Write/read round-trip on test row |

Record: **pass / fail / SAFE UNKNOWN** per case.

---

## 13. Operator approval before deployment

Required explicit operator sign-off for:

- import/replace workflow in n8n;
- credential or webhook URL changes;
- Telegram bot command behavior changes;
- Sheets schema changes;
- production model/prompt swaps affecting quality.

MARS agent sessions **stop** at prepared artifacts + instructions — not at live apply.

---

## 14. Rollback plan before deployment

Document before deploy:

1. Previous workflow export location (n8n history + sanitized file id).
2. Steps to re-import prior JSON.
3. Webhook path rollback if renamed.
4. Telegram bot webhook URL if changed.
5. Communication to SEO users if downtime expected.

---

## 15. Evidence pack after deployment

Use **MetaBOT Evidence Pack** structure:

```markdown
# MetaBOT Evidence — <change title>

## Summary
## Classification (REPO_EVIDENCED / OPERATOR / PLANNED)
## Workflows touched
## Live n8n ids (operator record)
## Test results
## Parity statement
## Docs updated
## Rollback executed? (yes/no/n/a)
## SAFE UNKNOWN remaining
```

Store: repo report under `projects/metabot-seo-content-agent/` or operator Storage — per task charter.

---

## 16. Report format after each workflow change

MARS session report should include:

1. **Executive summary** (1–3 sentences)
2. **Preflight** (branch, foreign WIP preserved)
3. **Files created/updated** (docs vs JSON)
4. **Execution boundary** reminder (MARS did not deploy)
5. **Evidence classification**
6. **SAFE UNKNOWN**
7. **Git status** (no commit unless requested)
8. **Final status** — COMPLETE / PARTIAL / BLOCKED

Align with MARS task closeout in [AGENTS.md](../../AGENTS.md).

---

## 17. Docs vs generated JSON vs live n8n

| Layer | Location | Authority |
|-------|----------|-----------|
| **Documentation** | `projects/metabot-seo-content-agent/*.md` | Product semantics, operator runbooks — **not** node-level truth unless verified |
| **Sanitized JSON** | `exports/` | Reference snapshot — **candidate** import |
| **Raw JSON** | `raw/` (gitignored) | Operator local truth copy |
| **Live n8n** | External | **Execution truth** |

**Rule:** Contradiction → trust live n8n, then update docs — not the reverse.

---

## 18. SEO Agent–specific notes

| Topic | Rule |
|-------|------|
| Workflow set | 3 current + File Export planned — do not claim 4th live without evidence |
| Research workflow | **PLANNED** — charter + MIG-informed design first |
| MIG patterns | Study [REPORT-mig-runtime-design-metabot-patterns-v1.md](../mig/reports/REPORT-mig-runtime-design-metabot-patterns-v1.md); separate webhook namespace |
| ORCA | Optional — not default for writer |
| Wordstat/Yandex | **SAFE UNKNOWN** — no complete claim without proof |

---

## 19. Forbidden operations (agents)

- Call live n8n API without explicit task charter and operator approval.
- Call Telegram, OpenRouter, Google Sheets APIs for this discipline doc work.
- `git add .` / commit credentials-bearing files.
- Replace live workflows from stale `workflow-sanitized-legacy.json` without parity review.

---

*Foundation Pack v1 · [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md)*
