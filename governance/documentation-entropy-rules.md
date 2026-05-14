# MARS — Documentation entropy rules

**Status:** **documented** — governance-only, Phase S3. **No** automated doc linting, **no** policy engine, **no** claims that entropy is “prevented” by tooling.

**Purpose:** Reduce **uncontrolled growth** of Markdown and parallel philosophies so operators can still find authoritative truth.

---

## 1. When **not** to create a new document

Create **no** new `.md` file when:

- the content is a **one-line** correction to an existing authoritative file;
- the topic already has a **home** in governance, a registry, or a pack index — extend that file or add a short subsection;
- you are only **restating** [AGENTS.md](../AGENTS.md) or [README.md](../README.md) without new scope;
- the goal is “visibility” for a single task — use lifecycle log, commit message, or scoped note in an existing operational file instead;
- the new doc would **duplicate** terminology or philosophy already in [web-gpt-sources/](../web-gpt-sources/) or governance — **merge** or **link**, do not fork vocabulary.

---

## 2. When to merge docs

Merge (into one file or one clearly owned section) when:

- two files describe the **same boundary** (e.g. two “registry vs runtime” explainers);
- titles differ but **audience and normative claims** overlap;
- maintenance is clearly **split-brain** (both get half-updates).

Prefer **one authoritative doc** plus a **single line** in `governance/README.md` or a pack index pointing to it.

---

## 3. When to deprecate docs

Deprecate (header banner + pointer forward, **human** decision) when:

- a contract or map is **superseded** by a versioned replacement — keep a stub that states **superseded by** and date;
- content is **historical** only (legacy import, old phase) — mark **historical input**, not normative;
- the file creates **terminology fork** risk — redirect to canonical vocabulary ([identity-and-naming-rules.md](identity-and-naming-rules.md), [enforcement/terminology-boundaries.md](enforcement/terminology-boundaries.md)).

**Deprecate** does **not** mean silent delete (repo policy: no delete without explicit instruction). Use explicit banner text.

---

## 4. When to create indexes instead

Prefer a new **index** (table of links + one-line descriptions) when:

- the problem is **navigation**, not new semantics;
- many paths exist but **one** governance story should stay central;
- a pack or folder has grown enough that “open everything” is the failure mode.

Indexes are **not** canonical by default for conflicting claims — see precedence in [registry-source-of-truth.md](registry-source-of-truth.md).

---

## 5. Duplicate philosophy and terminology forks

- **Duplicate philosophy:** if a new doc repeats “what MARS is,” **link** [README.md](../README.md), [AGENTS.md](../AGENTS.md), and [system-boundaries.md](system-boundaries.md) instead of rewriting.
- **Terminology forks:** new terms for existing concepts require **explicit** rationale in a governance-facing edit (lifecycle note or contract), not a shadow glossary in a random folder.

---

## 6. Stale references

- Prefer **relative links** and **stable filenames**; when renaming, **one** PR-style pass updates pointers (human).
- If external IDs or live systems drift, mark the row or map **stale as of (date)** or **SAFE UNKNOWN** until verified — do not imply auto-refresh.

---

## 7. Warning signs of entropy

| Signal | Risk |
|--------|------|
| Multiple “start here” docs | Onboarding collapse |
| Same risk described in five places | Update skew |
| New folder per brainstorm | Orphan paths |
| README promises not mirrored in registry | Claim drift |
| “vNext” docs without owner or stage | Speculative stack sprawl |

---

## 8. Bad growth patterns (examples)

- **Mirror READMEs:** every subfolder gets a long essay duplicating root posture.
- **Parallel governance:** `notes/governance-really-final.md` competing with `governance/*`.
- **Chat dumps:** pasting assistant transcripts as normative architecture.
- **Per-task philosophy:** each ticket spawns a new principles file instead of a lifecycle line.
- **Silent supersession:** old contract left authoritative-looking while a new doc contradicts it.

---

## 9. SAFE UNKNOWN

If ownership, audience, or canonical file for a topic is unclear, **do not** add another parallel doc — record **SAFE UNKNOWN** in lifecycle or the existing owner doc and resolve in a **single** deliberate edit later.
