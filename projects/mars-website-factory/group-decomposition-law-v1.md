# MARS Website Factory — Group Decomposition Law v1

**Status:** **Canonical Foundation Authority** — documented **human-operated** law for Website Factory frontend visual analysis and composition artifacts.  
**Not:** runtime orchestration, automated vision parser, layout linter, CI gate, or policy engine.

**Version:** v1  
**Date:** 2026-06-15

**Registry:** [registries.md §6](registries.md#6-frontend-production-rules)

**Provenance:** FP-0002 Shpigovsky.ru — JPG analysis test (2026-06-15). Agent correctly identified **two header rows** but **aggregated multiple distinct visual groups** into one abstract **«контактный блок» / CONTACT BLOCK**. **Not** a PDF, PNG, Layout Spec, or Visual Scale failure — a **missing pre–Layout Spec decomposition** failure.

**Peer authorities (detail — do not duplicate here):**

| Document | Role |
|----------|------|
| [layout-spec-law-v1.md](layout-spec-law-v1.md) | Layout Spec Gate — **downstream** of Group Decomposition; operator APPROVED before HTML/CSS |
| [canonical-clean-shell-v1.md](canonical-clean-shell-v1.md) | Clean Shell baseline — precedes composition artifacts |
| [design-source-to-frontend-mapping-governance-v1.md](design-source-to-frontend-mapping-governance-v1.md) | Token/spacing extraction — **does not** replace Group Decomposition |
| [frontend-failure-attribution-model-v1.md](frontend-failure-attribution-model-v1.md) | Failure class **GROUP AGGREGATION BEFORE DECOMPOSITION** |
| [website-factory-production-roadmap-v2-draft.md](website-factory-production-roadmap-v2-draft.md) | Phase C/F integration |
| [FP-0002-group-decomposition-lesson-v1.md](FP-0002-group-decomposition-lesson-v1.md) | Instance lesson — read-only provenance |

**Honesty boundary:** This law is **documentation discipline**. It does **not** claim an in-repo group-decomposition linter or automated gate unless a project explicitly adopts checklists as tooling.

---

## 1. Purpose

Close the **grouping gap** between approved **Visual SSOT** and **Layout Spec**.

[layout-spec-law-v1.md](layout-spec-law-v1.md) mandates a written Layout Spec before HTML/CSS. Layout Spec fields include row count and row composition — but agents still **collapse** multiple visually separable elements into **abstract mega-groups** at analysis time:

```text
LOGO · ADDRESS · SCHEDULE · PHONES · MESSENGERS · CTA  →  «CONTACT BLOCK»
MENU · SEARCH                                          →  (lost or merged into nav band)
```

That aggregation **poisons Layout Spec, Assembly Spec, and HTML** before markup starts — even when row count is correct.

**Group Decomposition** is the mandatory **first composition artifact**: name every **distinct visual group** per row **before** Layout Spec, Assembly Spec, or code.

**Required path:**

```text
Visual SSOT → Group Decomposition → Operator APPROVED → Layout Spec → … → HTML
```

**Forbidden path:**

```text
Visual SSOT → «I see rows and a contact area» → Layout Spec / HTML
```

---

## 2. Failure Class — GROUP AGGREGATION BEFORE DECOMPOSITION

| Field | Value |
|-------|-------|
| **Class ID** | `GROUP AGGREGATION BEFORE DECOMPOSITION` |
| **Definition** | Agent identified rows or zones but **merged two or more visually separable groups** into one **abstract aggregate label** without filing a Group Decomposition register with discrete **GROUP-IDs**. |
| **FP-0002 instance** | JPG test — ROW 1 decomposed as `logo \| contact \| CTA` instead of discrete Logo, Address, Schedule, Phones, Messengers, CTA groups; ROW 2 lost Search as separate group |
| **Expected capture point** | **Group Decomposition Gate** — before Layout Spec draft |
| **Why Layout Spec alone missed it** | Layout Spec can inherit wrong grouping from upstream analysis; verbal «two rows» is insufficient |
| **Failure cause token** | **GROUP AGGREGATION BEFORE DECOMPOSITION** — see [frontend-failure-attribution-model-v1.md](frontend-failure-attribution-model-v1.md) |
| **Attribution** | **Group Decomposition Gate** (agent/operator pair — operator if APPROVED decomposition that was wrong) |

**Distinction from Layout Spec failure:**

| Failure | Symptom |
|---------|---------|
| **LAYOUT SPEC SKIPPED** | No Layout Spec; jumped to HTML |
| **GROUP AGGREGATION BEFORE DECOMPOSITION** | Layout Spec or analysis uses **CONTACT BLOCK**-class labels; discrete groups not registered |

Both may coexist. Group Decomposition failure is **upstream**.

---

## 3. Authority Chain

Normative order for Website Factory frontend composition work:

```text
Visual SSOT (operator-approved)
        ↓
Group Decomposition          ← this law
        ↓
Layout Spec
        ↓
Assembly Spec
        ↓
Visual Scale Spec
        ↓
HTML/CSS
```

| Stage | Question answered |
|-------|-------------------|
| **Visual SSOT** | What does the design show? |
| **Group Decomposition** | What are the **named discrete groups** in each **ROW**? |
| **Layout Spec** | How do rows, zones, groups, containers, and hierarchy compose the block? |
| **Assembly Spec** | In what order are groups assembled and isolated? |
| **Visual Scale Spec** | How large / loud is each group relative to others? |
| **HTML/CSS** | Implementation — **downstream only** |

**Rule:** No stage may **rename or merge** groups registered in Group Decomposition without operator **REVISE** on Group Decomposition first.

**Rule:** Format of Visual SSOT (PDF · Figma · PNG · JPG) does **not** waive Group Decomposition.

---

## 4. GROUP DECOMPOSITION LAW (normative)

### 4.1 Mandatory before Layout Spec

It is **forbidden** to draft **Layout Spec**, **Assembly Spec**, or **Visual Scale Spec** for any scope until:

1. **Group Decomposition** artifact filed for that scope
2. **Operator decision** recorded: **APPROVED**
3. Visual SSOT reference cited

It is **forbidden** to start **HTML/CSS** without Group Decomposition **APPROVED** **and** Layout Spec **APPROVED** per [layout-spec-law-v1.md](layout-spec-law-v1.md).

### 4.2 Procedure

For each block scope (Header, Footer, Hero, section, page shell):

| Step | Action |
|------|--------|
| **G-1** | Split block into **ROW** register — top-to-bottom horizontal bands |
| **G-2** | For **each ROW**, list **distinct visual groups** left-to-right (reading order) |
| **G-3** | Assign each group a stable **GROUP-ID** (`GROUP-01`, `GROUP-02`, …) |
| **G-4** | Record **GROUP relationships** — adjacency, shared baseline, isolation intent (prose) |
| **G-5** | **Stop** — request operator **APPROVED** or **REVISE** |

### 4.3 One group = one visual object cluster

A **group** is a cluster that:

- Has **visible separation** from neighbors (whitespace, rule, background band, typographic tier, or control boundary)
- Would be **styled, moved, or hidden** as one unit in faithful implementation
- Contains **one primary semantic role** (logo mark, address text, schedule meta, phone cluster, messenger icons, CTA control, nav list, search control)

**Rule:** If the operator could point at two regions and say «these are different things», they **must** be different **GROUP-IDs**.

### 4.4 Forbidden aggregation

It is **forbidden** to use abstract aggregate labels **without** splitting into discrete GROUP-IDs first.

---

## 5. Required Outputs

Group Decomposition artifact **must** include:

### 5.1 ROW register

| Field | Content |
|-------|---------|
| **ROW-ID** | `ROW-01`, `ROW-02`, … top-to-bottom |
| **ROW label** | Short name — e.g. `TOP BAR`, `MAIN NAV ROW` |
| **Visual SSOT anchor** | Where row boundaries are visible in SSOT |

### 5.2 GROUP register

| Field | Content |
|-------|---------|
| **GROUP-ID** | `GROUP-01`, `GROUP-02`, … global within block scope |
| **ROW-ID** | Parent row |
| **Group name** | Concrete noun — `Logo`, `Address`, `Schedule`, `Phones`, `Messengers`, `CTA`, `Menu`, `Search` |
| **Contents** | Literal elements visible in SSOT (text, icons, controls) |
| **Position in row** | Left · center-left · center · center-right · right |
| **SAFE UNKNOWN** | Unreadable copy — **do not** merge unknowns into a blob |

### 5.3 GROUP relationships

| Field | Content |
|-------|---------|
| **Adjacency** | Which groups share a row band without merging |
| **Isolation** | Groups that **must not** collapse in Layout Spec (e.g. Phones ≠ Utility links) |
| **Cross-row pairs** | Optional vertical alignment pairs (e.g. Logo ROW-01 aligns with Logo ROW-02) — or explicit **none** |

### 5.4 Illustrative example (Header — structure only)

**ROW-01**

| GROUP-ID | Name | Contents |
|----------|------|----------|
| GROUP-01 | Logo | Brand mark |
| GROUP-02 | Address | City / street lines |
| GROUP-03 | Schedule | Hours string |
| GROUP-04 | Phones | One or more tel numbers |
| GROUP-05 | Messengers | Messenger icons |
| GROUP-06 | CTA | Primary action button |

**ROW-02**

| GROUP-ID | Name | Contents |
|----------|------|----------|
| GROUP-07 | Menu | Horizontal nav links |
| GROUP-08 | Search | Search icon / control |

**Forbidden summary for same header:**

```text
ROW-01: LOGO · CONTACT BLOCK · CTA
ROW-02: MENU (search omitted or implied)
```

---

## 6. Forbidden Patterns

The following labels are **violation signals** when used **instead of** discrete GROUP-IDs:

| Forbidden aggregate | Why |
|---------------------|-----|
| **CONTACT BLOCK** | Merges address, schedule, phones, messengers |
| **INFO BLOCK** / **INFO AREA** | Merges heterogeneous meta |
| **CONTENT CLUSTER** | Unnamed blob |
| **LEFT SIDE** / **RIGHT SIDE** | Positional fiction — not groups |
| **UTILITY GROUP** / **UTILITY AREA** | Merges region, hours, links, phones |
| **TOP BAR CONTENT** | Row label reused as group |
| **NAV AREA** (when search is separate) | Drops Search group |
| **CTA + phones** / **contact + CTA** | Cross-group merge |

**Rule:** Positional words (`left`, `right`, `center`) may describe **placement within a row** — they **do not** substitute for GROUP-IDs.

**Rule:** Any similar aggregate **without** downstream GROUP register split is a **violation**.

---

## 7. Operator Gate

After Group Decomposition is written, the agent **must stop**. **No Layout Spec** for that scope until decision.

### 7.1 Agent obligation

1. File Group Decomposition at agreed project path (e.g. `<PROJECT>-GROUP-DECOMPOSITION-<block-id>-vN.md`)
2. Present ROW register + GROUP register + relationships to operator
3. Request explicit decision
4. **Wait**

**Required request text (Russian or English equivalent):**

```text
Group Decomposition готов для <scope>.
Проверьте ROW и GROUP-ID против Visual SSOT.
Требуется решение: APPROVED или REVISE.
Layout Spec запрещён до APPROVED.
```

### 7.2 Operator decisions

| Decision | Meaning | Layout Spec |
|----------|---------|-------------|
| **APPROVED** | Discrete groups accepted | **Permitted** to draft |
| **REVISE** | Groups wrong, merged, or missing | **Forbidden** — fix decomposition; re-submit |

**Rule:** Group Decomposition **APPROVED** does **not** substitute for Layout Spec **APPROVED**.

---

## 8. Reporting

When Group Decomposition is filed or gated, REPORT must include:

```text
GROUP DECOMPOSITION — <block-id> — DRAFT | APPROVED | REVISE
GROUP DECOMPOSITION GATE — PASS (APPROVED) | FAIL (REVISE pending) | FAIL (SKIPPED)
ROW COUNT — <n>
GROUP COUNT — <n>
VISUAL SSOT REF — <SOURCE-ID or path>
```

Layout Spec for the same block must cite:

```text
GROUP DECOMPOSITION REF — <path> — APPROVED <date>
```

**Forbidden:** `GROUP DECOMPOSITION GATE — PASS` when decision is still pending.

---

## 9. Scope

**Applies to:** All Website Factory greenfield frontend — shell (Header, Footer), every production block/page slice, and any agent task that drafts Layout Spec from Visual SSOT.

**Factory-wide mandatory:** **Yes** — unless project charter documents explicit dated exception with Lead signature.

**Adoption path:** Factory-wide via pointer integration in roadmap, workflow map, registries, layout-spec law, clean shell, and failure attribution model — **not** a new governance wave.

**Does not modify:** FP-0002 workspace artefacts, frontend source code, or existing Layout Spec / Assembly Spec content in operations workspaces.

---

## 10. Changelog

| Date | Change |
|------|--------|
| 2026-06-15 | v1 — Group Decomposition Law promoted from FP-0002 JPG test; canonical Factory authority. |
