# MARS — Operational lessons and postmortems

**Status:** **documented** — governance-only, **Phase S7**. **Not** a mandatory template engine, **not** automated incident response.

**Purpose:** Lightweight **lessons-learned** discipline so failed experiments and partial wins become **governance assets** instead of mythology.

---

## 1. Principles

| Principle | Meaning |
|-----------|---------|
| **Failed experiments are acceptable** | Negative results reduce future drift if captured honestly. |
| **Lessons > mythology** | Narratives must bow to dated evidence and limits—[experiment-evidence-rules.md](experiment-evidence-rules.md). |
| **Postmortems are governance assets** | Short, factual writeups improve onboarding and anti-chaos posture—[documentation-entropy-rules.md](documentation-entropy-rules.md) (keep lean). |
| **SAFE UNKNOWN outcomes are acceptable** | Unknowns labeled beat fake certainty—[registry-source-of-truth.md](registry-source-of-truth.md). |
| **Operational reality overrides narrative** | If evidence contradicts a story, fix the story or mark **SAFE UNKNOWN**—[operational-survivability.md](operational-survivability.md). |

---

## 2. Lightweight postmortem sections

Use as a **checklist** (order flexible):

1. **Objective** — What hypothesis or pilot outcome was sought?  
2. **What happened** — Chronological facts, owners, systems touched.  
3. **Evidence** — Links, logs, commands, artifacts with evidence-state labels—[experiment-evidence-rules.md](experiment-evidence-rules.md).  
4. **What failed** — Explicit failures, including governance failures (wrong lane, bad naming).  
5. **What stabilized** — Items promoted per [experiment-to-pattern-transition.md](experiment-to-pattern-transition.md), if any.  
6. **What remains unknown** — **SAFE UNKNOWN** list + what would resolve each item.

Length target: **one screen** where possible; appendices for large logs.

---

## 3. Where to store

- Prefer project `notes/`, `logs/`, or task **REPORT** attachments per team habit—**no** mandated database.  
- If stored in-repo, avoid duplicating: one canonical postmortem path, others link.

---

## 4. Non-goals

- **No** blame rituals or HR process—keep technical and operational.  
- **No** implied 24/7 incident command—this is human-paced documentation.  
- **No** auto-tickets or workflow engine—see [tooling-boundary-rules.md](tooling-boundary-rules.md).

---

## 5. SAFE UNKNOWN

A postmortem that lacks **evidence** or **what remains unknown** is incomplete; upgrade evidence or label gaps rather than inferring success.
