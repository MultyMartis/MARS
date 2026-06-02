# OCPilot — Knowledge Layer Storage Principles

**Run:** 3.6 — Baseline Storage Review  
**Status:** documented principles — **no** content collection in this run.

**Parent:** [knowledge/README.md](README.md)  
**Related:** [recommended-storage-model.md](../recommended-storage-model.md), [archive-intake-rules.md](../archive-intake-rules.md)

---

## Purpose

Define what the OCPilot **knowledge layer** is for — and what it must **not** become.

The knowledge layer supports human-operated OpenCart/ocStore audit and comparison. It is **reference knowledge**, not a mirror of the internet and not a second copy of vendor file trees.

---

## Reference knowledge vs archived internet

| | Reference knowledge | Archived internet |
|---|---------------------|-------------------|
| **Goal** | Explain concepts needed for OCPilot work | Hoard raw web pages «just in case» |
| **Scope** | Curated, version-aware, audit-relevant | Unbounded, duplicate, stale |
| **Size** | Small — markdown notes, maps, findings | Large — HTML dumps, forum threads, PDF mirrors |
| **Maintenance** | Updated when baselines or audit patterns change | Rotting copies of external sites |
| **Truth** | Linked to baseline identity or official source | May contradict current vendor docs |
| **In git** | Yes — when curated | **No** — link out instead |

**Rule:** If content exists authoritatively on the vendor site and OCPilot does not add interpretation, **do not archive it in repo**.

---

## Why OCPilot must not become a documentation dump

| Risk | Explanation |
|------|-------------|
| **Repo bloat** | Documentation dumps compete with baseline bulk for MARS survivability |
| **Stale truth** | Frozen forum answers mislead when OpenCart/ocStore versions change |
| **Duplication** | Same OCMOD tutorial copied five ways — no single operational truth |
| **Audit noise** | Operators cannot find project-specific findings among generic copies |
| **False completeness** | Large knowledge folder implies coverage — often illusion |
| **Drift from baselines** | Generic docs do not replace version-pinned baseline metadata |

OCPilot knowledge answers: *«What do we need to know for **this** audit program that is not already in passports, manifests, or official docs?»*

It does **not** answer: *«Can we store the entire OpenCart forum?»*

---

## What belongs in the knowledge layer

| Category | Examples | Storage |
|----------|----------|---------|
| **Official docs pointers** | Links to OpenCart/ocStore release notes with brief summary | Markdown in topic README |
| **Architecture maps** | MVC flow, admin vs catalog, modification pipeline | `knowledge/controllers/`, `knowledge/ocmod/` |
| **Version notes** | «3039 rs.1 differs from 3038 rs.2 in paths X, Y» — cross-ref comparison notes | `knowledge/ocstore/` + link to `comparison-notes/` |
| **ocStore-specific findings** | Distribution deltas, rs build behavior, Russian locale patterns | `knowledge/ocstore/` |
| **Database interpretation** | Prefix conventions, install SQL reading guide — not full SQL | `knowledge/database/` |
| **SEO URL behavior** | Routing audit checklist | `knowledge/seo-url/` |
| **Audit playbooks** | How to classify extension vs core during site audit | Future — short procedural notes |

**Qualities of keep-worthy knowledge:**

1. **Actionable** for Run 5+ audit or Run 6+ planning.
2. **Version-scoped** or explicitly marked cross-version.
3. **Curated** — one canonical note per topic where possible.
4. **Small** — prefer summary + external link over full copy.

---

## What does not belong

| Category | Examples | Instead |
|----------|----------|---------|
| **Random forum copies** | phpBB/StackExchange thread dumps | Link + one-line summary if ever needed |
| **Endless blog archives** | «Top 10 OpenCart tips» reposts | External bookmark |
| **Duplicated internet content** | Full OpenCart API HTML mirror | Link to official docs |
| **Vendor file trees** | OpenCart core PHP | `baselines/*/files/` local cache — not knowledge |
| **ZIP archives** | Extension packages, baseline ZIPs | External baseline storage |
| **Live site exports** | Production `catalog/` uploads | Project site workflow — external |
| **Governance copies** | MARS governance waterfall | Link to `governance/` — do not duplicate |
| **Unreviewed scraped content** | Automated crawl output | Forbidden without human curation charter |

---

## Relationship to baselines and storage model

```
Baselines (metadata in git)
  └── passports, manifests — WHAT version, WHAT paths

Baselines (bulk external / local cache)
  └── files/ trees — vendor truth for diff

Knowledge layer (curated markdown in git)
  └── HOW to interpret, HOW to audit, WHY ocStore differs

External official sources (links only)
  └── upstream docs, vendor release pages
```

Knowledge **complements** baselines; it **does not replace** manifests or promoted trees.

---

## Population rules (future)

1. **Human-authored only** — no automated web scraping into `knowledge/`.
2. **One topic — one owner note** — extend existing README before adding parallel files.
3. **Cite baseline or official source** — every finding links to evidence path or URL.
4. **Retire stale notes** — mark deprecated when new baseline supersedes.
5. **Size gate** — if a single knowledge artifact exceeds ~100 KB, split or move to external with index in repo.

---

## Topic folder intent (unchanged skeleton)

| Path | Keep-worthy content type |
|------|--------------------------|
| [opencart/](opencart/README.md) | Upstream concepts, version ladder |
| [ocstore/](ocstore/README.md) | Distribution-specific deltas |
| [database/](database/README.md) | Schema reading, prefix audit |
| [ocmod/](ocmod/README.md) | Modification system audit patterns |
| [controllers/](controllers/README.md) | MVC audit map |
| [models/](models/README.md) | Model layer patterns |
| [seo-url/](seo-url/README.md) | Routing and SEO URL checks |

Skeleton README stubs remain valid until curated content is added under charter.

---

## SAFE UNKNOWN

- Knowledge authoring schedule — not defined until post–Run 4 needs emerge.
- Whether bilingual (RU/EN) notes are required per topic — operator preference.
- Integration with external wiki — not planned in Run 3.6.
