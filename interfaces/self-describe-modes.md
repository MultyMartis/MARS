# MARS — Self-Describe Modes v0



**Status:** **documented** — mode definitions for the **Self-Describe Engine** (see `interfaces/introspection-v0.md`). **No** prompts, **no** templates in-repo, **no** runtime.



---



## 1. Mode overview



| Mode | Input type | Primary sources (see `interfaces/introspection-v0.md` §6) |

|------|------------|--------------------------------------------------|

| **SELF DESCRIBE FULL** | FULL | system-registry, governance-documents, entity-registry, workflow docs (read-only), memory/control-plane README honesty; **may** include a short **lifecycle-log** summary from `logs/lifecycle-log.md` when present |

| **SELF DESCRIBE SHORT** | SHORT | system-registry, governance-documents (minimal), entity-registry (counts / names only if present) |

| **SELF DESCRIBE DEBUG** | DEBUG | system-registry, governance-documents, workflows (signals, stages), observability README, AGENTS.md honesty rules |

| **SELF DESCRIBE ENTITY** | ENTITY `<id>` | entity-registry (+ governance for status semantics) |

| **SELF DESCRIBE PROJECT** | PROJECT `<id>` | **`registry/project-registry.md`** (project-registry); resolve `<id>` against **documented** rows |



All modes obey **output rules** in `interfaces/introspection-v0.md` §7 and the **update rule** §8.



---



## 2. SELF DESCRIBE FULL



**Intent:** Full **system overview** for operators or agents that need **breadth**.



**Must include (when data exists):**



- **What MARS is** — from `README.md` / `web-gpt-sources/01_system.md`, without claiming shipped runtime unless repo proves it (`AGENTS.md`).

- **Phase and roadmap pointer** — `web-gpt-sources/14_roadmap.md`, root `README.md` **Current phase**.

- **Layer map** — Interface, Control Plane, Agents/Registry, Workflows, Memory, Storage, Security, Observability — as **documented** in architecture sources; label each as **documented** / **planned** / **legacy imported** where applicable.

- **Registry summary** — Agent catalog overview from `agents/registry.md` (table / roles), not fabricated roles.

- **Workflow summary** — Stages and Control Plane relation from `workflows/workflow-v0.md` and `workflows/execution-flow.md`.

- **Governance hooks** — Boundaries, execution model honesty, capability map pointers (`governance/`).



**Lifecycle-log (optional summary):**



- When **`logs/lifecycle-log.md`** exists, **FULL** mode **may** include a **brief** summary of recent **documented lifecycle events** (append-only discipline per governance). This is **not** live runtime telemetry.



**Must omit or SAFE UNKNOWN:**



- Live metrics, queue depth, secrets, or **fabricated** log lines not present in bound sources.



---



## 3. SELF DESCRIBE SHORT



**Intent:** **Compressed snapshot** for quick orientation (e.g. CLI `--short`, chat “tl;dr”).



**Must include:**



- One **paragraph** or equivalent **derived** from **system-registry** (what/phase/honesty).

- **Where to read more** — short list of paths (e.g. `interfaces/introspection-v0.md`, `agents/registry.md`, `workflows/workflow-v0.md`, `registry/project-registry.md`, `logs/lifecycle-log.md`).



**Must not:**



- Duplicate entire registry tables or roadmap sections from memory; **re-read** or **cite snapshot id** when implementing.



---



## 4. SELF DESCRIBE DEBUG



**Intent:** **Internal documentation state** — not live JVM/CPU debugging. Clarifies **what the repo claims exists** vs **planned**.



**Should include:**



- **Evidence-based implementation boundary** — e.g. “no application code under `mars-runtime/` for X” only if true after scan policy defined by implementer; until then, **SAFE UNKNOWN** at field level.

- **Signals and stages** — From `workflows/task-contract-v0.md` and `workflows/execution-flow.md` (**documented** vocabulary).

- **Issues** — Only **repo-grounded**: cite missing files, broken links, or contradictions against **read** sources — not “probably Redis is down.”



**Must not:**



- Fabricate **internal state** (connections, caches, last run ids) without **evidence** from **`logs/lifecycle-log.md`**, registry rows, or other **bound** artifacts.



---



## 5. SELF DESCRIBE ENTITY



**Intent:** Describe one **registry entity** (v0: **agent role** / **card**) by **entity passport** semantics.



**Resolution:**



- Map `<id>` to **entity-registry** (agent **name** or stable catalog id per `agents/registry.md`).

- Load **card** fields from registry row + any linked card file using the template `agents/agent-card-template.md`.



**If `<id>` is unknown:**



- Emit **SAFE UNKNOWN**: unknown id, suggest valid names from **current** registry read, cite `agents/registry.md`.



**Passport note:** Governance states there is **no** separate `entity-passport.md`; the **card** is the in-repo passport analog. Do not claim external passports unless **evidence** is provided.



---



## 6. SELF DESCRIBE PROJECT



**Intent:** Describe a **project** record from **project-registry**.



**v0 repository binding:**



- **Project-registry** is **`registry/project-registry.md`** (authoritative **documented** project rows for Phase 1).

- **Lifecycle-log** for governance events is **`logs/lifecycle-log.md`** — use when **DEBUG** / **FULL** need documented lifecycle context; it is **not** a substitute for future run-time audit pipelines.



**Required behavior:**



- **Read** `registry/project-registry.md` and resolve **PROJECT `<id>`** against **named** projects in that file.

- If `<id>` is **absent** or **ambiguous**, emit **SAFE UNKNOWN** for project-specific attributes and cite the registry path.

- Do **not** invent projects, paths, or statuses not present in the registry file.



---



## 7. Mode selection (informative)



| User intent (examples) | Mode |

|------------------------|------|

| “Explain MARS end-to-end” | FULL |

| “What is MARS in two sentences?” | SHORT |

| “What’s actually implemented in the repo?” | DEBUG |

| “What does the Validator Agent do?” | ENTITY `Validator Agent` (or canonical id) |

| “Describe project Acme” | PROJECT `Acme` — read **`registry/project-registry.md`**; **SAFE UNKNOWN** if id not in file |



---



## 8. Changelog (documentation)



| Date | Change |

|------|--------|

| 2026-04-27 | Initial **Self-Describe modes v0**. |

| 2026-04-27 | **Fix Pass v0:** bind **project-registry** → `registry/project-registry.md`, **lifecycle-log** → `logs/lifecycle-log.md`; **FULL** may summarize lifecycle-log; **PROJECT** reads registry file; removed incorrect “no file in repository” claims. |

