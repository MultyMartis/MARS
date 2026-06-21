# WF-PR01 Pilot Intake Template v1

**Status:** **PUBLISHED** · **TEMPLATE ONLY** — do not treat as completed intake until operator fills with real project data  
**Date:** 2026-06-22  
**Contract:** [WF-PR01-PILOT-READINESS-CONTRACT-v1.md](WF-PR01-PILOT-READINESS-CONTRACT-v1.md)  
**Honesty boundary:** Empty template for first pilot intake. **Not** a fictitious project. **Not** pilot workspace authorization until P0 approval.

---

## Instructions

1. Copy this template into the pilot workspace as `pilot-intake-v1.md` **after** operator selects a real project — or store completed intake under `projects/mars-website-factory/pilot-readiness/intakes/` with pilot ID in filename.
2. Fill every field with **real paths and decisions** or explicit **SAFE UNKNOWN**.
3. Do not invent content to “complete” the form.
4. Gate **P0 — Pilot Input Approved** requires operator sign-off on this document.

---

## 1. Pilot Identity

| Field | Value |
|-------|-------|
| **Pilot ID** | `WF-PILOT-____` |
| **Project name** | |
| **Client / project owner** | |
| **Business type** | e.g. corporate service · local business · manufacturer landing |
| **Operator owner** | |
| **Intake date** | |
| **Production mode** | `PIXEL_PERFECT` \| `TEMPLATE_ART` — per [website-factory-production-modes-charter-v1.md](../website-factory-production-modes-charter-v1.md) |

---

## 2. Scope

| Field | Value |
|-------|-------|
| **Target page or page family** | |
| **Primary page URL/slug (planned)** | |
| **Secondary pages (if any, max 2)** | |
| **Expected section count (main page)** | |
| **Pilot class confirmation** | Corporate landing \| Service landing \| Small corporate \| Other (operator declare) |
| **Out of scope (explicit)** | |

---

## 3. Visual Sources

| Field | Path / reference |
|-------|------------------|
| **Visual source type** | Figma \| PNG/JPG \| PDF \| Mixed |
| **Desktop source** | |
| **Mobile source** | |
| **Tablet source (if any)** | |
| **Figma link or export path** | |
| **Source approval status** | Draft \| Final — operator-approved |
| **Source approval date** | |
| **Source approval owner** | |

---

## 4. Content Sources

| Field | Path / reference |
|-------|------------------|
| **Texts source** | doc \| spreadsheet \| Figma text \| live site copy |
| **Texts approval status** | |
| **Assets source** | |
| **Font source** | |
| **Icon source** | |
| **Logo files** | |

---

## 5. Interactions and Integrations

| Field | Value |
|-------|-------|
| **Required interactions** | accordion \| modal \| slider \| tabs \| other |
| **Required forms** | fields · validation · endpoint |
| **Required modal windows** | |
| **CMS target (if any)** | |
| **Pilot CMS boundary** | None \| deferred \| partial (declare) |
| **Third-party scripts** | analytics \| maps \| chat \| other |
| **Browser targets** | |

---

## 6. Layout and Responsive

| Field | Value |
|-------|-------|
| **Breakpoints if known** | |
| **Container width (desktop)** | |
| **Container padding rules** | |
| **Mobile layout authority present?** | Yes \| No — requires responsive decision sheet |
| **Responsive decision sheet path (if needed)** | |

---

## 7. Delivery

| Field | Value |
|-------|-------|
| **Required output** | static HTML dist \| staging deploy \| other |
| **Deadline** | |
| **Workspace path (planned)** | `workspaces/wf-pilot-____-____-frontend/` |
| **Branch strategy** | |

---

## 8. Operator Approval Points

| Gate | Required? | Notes |
|------|-----------|-------|
| **P0 — Pilot Input Approved** | **Yes** | |
| **P1 — Inventory Approved** | **Yes** | |
| **P2 — Foundation Approved** | **Yes** | P1+P2 merge allowed |
| **P3 — Desktop Approved** | **Yes** | |
| **P4 — Mobile Approved** | **Yes** | P3+P4 merge allowed |
| **P5 — Visual QA Reviewed** | **Yes** | |
| **P6 — Pilot Final Decision** | **Yes** | |

---

## 9. Known UNKNOWNs

| ID | Topic | Impact | Operator decision needed |
|----|-------|--------|--------------------------|
| U-01 | | | |
| U-02 | | | |

---

## 10. Forbidden Assumptions

List assumptions agents and implementers **must not** make without operator approval:

```text
-
-
-
```

Examples (delete if not applicable):

- Do not invent mobile layout without source or decision sheet.
- Do not paraphrase marketing copy.
- Do not substitute stock photography.
- Do not add sections not in visual source.

---

## 11. Candidate Matrix Reference

When evaluating whether this project is suitable for first pilot, attach scoring from [WF-PR01-PILOT-CANDIDATE-MATRIX-v1.md](WF-PR01-PILOT-CANDIDATE-MATRIX-v1.md).

| Verdict | |
|---------|---|
| **Scored by** | |
| **Score date** | |

---

## 12. P0 Approval Record

| Field | Value |
|-------|-------|
| **P0 status** | Pending \| Approved \| Rejected |
| **Approver** | |
| **Approval date** | |
| **Notes** | |

**P0 Approved signature block:**

```text
Pilot input reviewed and approved for bounded implementation.
Workspace creation authorized under WF-PR01 contract.
```

---

*Template: `projects/mars-website-factory/pilot-readiness/WF-PR01-PILOT-INTAKE-TEMPLATE-v1.md` · v1 · 2026-06-22*
