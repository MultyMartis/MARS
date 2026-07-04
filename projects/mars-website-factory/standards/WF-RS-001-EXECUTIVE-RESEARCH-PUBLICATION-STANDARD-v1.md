# WF-RS-001 — Executive Research Publication Standard v1

**Standard ID:** WF-RS-001  
**Status:** **SUPERSEDED — migrated to ORCA-RS-001** (historical registration — link preserved)  
**Date:** 2026-07-02 (original) · **Migrated:** 2026-07-02  
**Authority (historical):** Website Factory methodology (`mars-website-factory`) — **incorrect subsystem registration**  
**Current normative standard:** [ORCA-RS-001](../../orca/standards/ORCA-RS-001-EXECUTIVE-RESEARCH-PUBLICATION-STANDARD-v1.md) — Executive Research Publication belongs to **ORCA**, not Website Factory. Website Factory **consumes** ORCA research publications.  
**Reference implementation:** BZPM Market Intelligence — Executive Presentation Package v2.1 RU — now cited under **ORCA-RS-001**  
**Path:** `projects/website-factory/execution-cases/bzpm-market-intelligence/executive-report/`

> **Migration notice (2026-07-02):** This document is preserved for link stability and revision history. Do **not** cite WF-RS-001 as the active owner of Executive Research Publication. Use **ORCA-RS-001** for normative authority. Body text below reflects the original 2026-07-02 registration unchanged.

**Related:** [research-standards-v1.md](../research-standards-v1.md) · [publication-standards-v1.md](../publication-standards-v1.md) · [website-factory-standards-register-v1.md](../website-factory-standards-register-v1.md) · [artifact-publication-semantics-v0.md](../artifact-publication-semantics-v0.md) · [ORCA-RS-001](../../orca/standards/ORCA-RS-001-EXECUTIVE-RESEARCH-PUBLICATION-STANDARD-v1.md)

---

## 1. Purpose

Fix the **two-level research model** for Website Factory. From this standard forward, **no research is complete** until an **Executive Research Package** is published.

Internal working materials remain valid and necessary — but they are **not** the client-facing or knowledge-registration outcome.

**Not claimed:** automated publication pipeline, CMS export, or validation engine.

---

## 2. Two-level research model

### Level 1 — Internal Research

Working analytical base. Operator-facing. May evolve during active research.

| Category | Examples |
|----------|----------|
| Registry | Entity/competitor registers, findings registers |
| Master Report | Consolidated internal narrative |
| Operator Notes | Session observations, UX notes |
| SERP | Query snapshots, leader lists |
| Evidence | Screenshots, captures, audit trails |
| Raw Data | Exports, scrapes, intermediate tables |
| Research Notes | Working markdown, decision logs |
| Working Excel | Operational spreadsheets, checklists |
| Intermediate Documents | Drafts, wave reports, packaging layers |

**Rules:**

- Level 1 **may** contain internal IDs, operator vocabulary, raw tables, and incomplete states.
- Level 1 **is not** sufficient for Research Freeze, Stable Publication, Client Delivery, or Knowledge Registration.
- Level 1 **does not** replace traceability — it feeds Level 2.

### Level 2 — Executive Research Package

Mandatory **final** deliverable of every completed Website Factory research program.

| Audience | Use |
|----------|-----|
| Client | First read, commercial meetings |
| Director / PM | Decision support, scope justification |
| Analytics / design / SEO / dev | Downstream project work |
| Future operators | Onboarding without internal context |

**Rules:**

- Self-contained: understandable **without** reading Registry or internal markdown.
- No dependency on operator session memory.
- Traceable via `sources.md`.
- Visually executive-grade (see §7).

---

## 3. Mandatory deliverables

Every completed research **must** ship an Executive Research Package folder containing:

| # | Artifact | Required | Purpose |
|---|----------|----------|---------|
| 1 | `Executive Research.xlsx` *(or project-named equivalent)* | **Yes** | Presentation dashboard — KPI, charts, cards |
| 2 | `Research Conclusions.docx` *(or project-named equivalent)* | **Yes** | Analytical conclusions and recommendations |
| 3 | `README.md` | **Yes** | Package purpose, composition, client read order |
| 4 | `sources.md` | **Yes** | Authority document map and traceability |
| 5 | `generator.py` *(or equivalent)* | **If generatable** | Reproducible regeneration from authority sources |

**Naming:** Project-specific filenames are allowed when prefixed consistently (e.g. `BZPM Market Research.xlsx`) — register exact names in `README.md`.

**Folder convention:** `executive-report/` or `executive-research/` under the research execution case root.

---

## 4. Executive Excel requirements

**Primary audience:** client, director, PM, presentation, commercial meeting.

| Principle | Requirement |
|-----------|-------------|
| Raw tables | **Minimum** — prefer aggregated views |
| Charts / diagrams | **Maximum** — visual KPI communication |
| Cards / KPI blocks | Required where metrics exist |
| Language | Client-appropriate; plain business Russian or English per project |
| Style | Consulting-grade layout (see §7) |
| Data | **No new facts** — presentation layer over Level 1 authority only |

**Forbidden as substitute:** Presentation Pack working Excel alone; internal registry exports; unformatted dump tables.

---

## 5. Executive Word requirements

**Primary audience:** analytics, architecture, design, SEO, development, future projects.

**Structure must include:**

1. Analytical conclusions (what the market/project reality is)
2. Practical recommendations (what to do on the site/product)
3. Pattern explanation (why patterns matter)
4. Priorities (ordered action list)
5. **Use** guidance (what to apply)
6. **Do not use** guidance (what to avoid)

Word **must not** duplicate Excel verbatim — complementary narrative layer.

---

## 6. Self-containment and traceability

### Self-containment

Executive Package **must**:

- Explain the research to someone who **never saw the project**
- Be understandable to the **client**
- **Not** require reading Registry
- **Not** require reading internal working markdown
- **Not** require access to operator-only materials

### Traceability

- Every material conclusion **must** trace to a Level 1 authority via `sources.md`
- `sources.md` **must** list authority paths, roles, and generation relationship
- Regeneratable packages **must** document regen command in `README.md`
- Data **must** be reproducible from declared sources (no chat-only facts)

---

## 7. Visual standard

Target presentation quality aligned with **McKinsey · BCG · PwC · Deloitte · KPMG** executive research style:

| Do | Do not |
|----|--------|
| Clear hierarchy | Decorative chrome |
| Structured sections | Visual overload |
| KPI-first dashboards | Operator-internal column noise |
| Consistent typography in Office outputs | Placeholder lorem |
| White space and scan rhythm | Raw registry dumps |

**Documentation only** — no automated style linter claimed.

---

## 8. Publication Gate

Research status **≠ COMPLETE** until **all** mandatory deliverables exist and pass operator review.

### Gate checklist

| Gate item | Blocks completion when absent |
|-----------|-------------------------------|
| Executive Research.xlsx | **Yes** |
| Research Conclusions.docx | **Yes** |
| README.md | **Yes** |
| sources.md | **Yes** |
| generator.py (if applicable) | **Yes** when package is declared generatable |

### Allowed only after Publication Gate

| Post-gate action | Permitted |
|------------------|-----------|
| Research Freeze | Yes |
| Stable Publication | Yes |
| Client Delivery | Yes |
| Knowledge Registration | Yes |
| Citation as Factory reference | Yes |

### Explicitly blocked before gate

- Marking research wave/program **COMPLETE**
- Registering research as Factory knowledge without Executive Package path
- Client handoff of internal Registry / Presentation Pack **as final deliverable**

---

## 9. Relationship to other layers

| Layer | Role relative to WF-RS-001 |
|-------|---------------------------|
| **Presentation Pack** (e.g. BZPM working Excel set) | Level 1 operational packaging — **not** final publication |
| **Registry / Master Report** | Level 1 authority — feeds generator; **not** client final |
| **Research Canon RV-01–03** | Foundry immutable snapshots — separate lane; WF-RS-001 applies to **execution-case research programs** |
| **artifact-publication-semantics-v0** | General artifact publication classes — WF-RS-001 adds **research-specific mandatory package** |

---

## 10. Reference implementation

| Field | Value |
|-------|-------|
| Program | BZPM Market Intelligence |
| Package | Executive Presentation Package v2.1 RU |
| Location | `projects/website-factory/execution-cases/bzpm-market-intelligence/executive-report/` |
| Excel | `BZPM Market Research.xlsx` |
| Word | `BZPM Research Conclusions.docx` |
| Generator | `generate_executive_report.py` |
| Status | **Reference implementation — read-only for standard authorship** |

Operators implementing new research **should** study BZPM structure; **must not** modify BZPM package when registering new standards.

---

## 11. Applicability

WF-RS-001 applies to **all Website Factory research programs** including:

- Market intelligence and competitor research
- Forensic / commercial page research (corporate, catalog, landing)
- Catalog UX intelligence
- Vertical profile and SERP research
- Client discovery research feeding IA, design, SEO, or development

**Excluded:** ad-hoc operator notes with no declared research program; Foundry RV canon snapshots (separate immutability rules).

---

## 12. Non-claims

- **Not** an automated publication engine
- **Not** a replacement for HITL review of conclusions
- **Not** proof that Excel/Word generation runs in CI
- **Not** a mandate to regenerate BZPM or any frozen client artifact

---

## 13. Revision history

| Date | Change |
|------|--------|
| 2026-07-02 | v1 — initial standard from BZPM Market Intelligence executive package practice |
| 2026-07-02 | **SUPERSEDED** — migrated to ORCA-RS-001; normative ownership transferred to ORCA; this file preserved for link stability |
