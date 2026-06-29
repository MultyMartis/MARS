# ATLAS Counterparty Card Storage — Operator Pointer v1

**Status:** **documented** — external evidence storage pointer (normative for operators).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-05  
**Parent:** [ATLAS-POPULATION-EXECUTION-PLAN-v1.md](../foundation/ATLAS-POPULATION-EXECUTION-PLAN-v1.md) · [ATLAS-COUNTERPARTY-CARD-MODEL-v1.md](../foundation/ATLAS-COUNTERPARTY-CARD-MODEL-v1.md)  
**Is not:** storage schema, DMS design, OCR specification, automated extraction, runtime implementation.

---

## 1. Purpose

This document points operators to the **external evidence storage** for Counterparty Cards. The actual card files **live outside git** — they are not committed to the MARS repository at `X:\AI MARS`.

Foundation documents define **what** a Counterparty Card is and **how** it flows through ATLAS. This document defines **where** operators manually place card files before population intake.

---

## 2. Canonical storage path

**External root (operator-maintained):**

```text
X:\AI MARS STORAGE\atlas\evidence\counterparty-cards\
```

| Path | Role |
|------|------|
| `C:\AI MARS STORAGE\atlas\` | ATLAS bulk evidence root |
| `C:\AI MARS STORAGE\atlas\evidence\` | Evidence artifacts (not registry records) |
| `X:\AI MARS STORAGE\atlas\evidence\counterparty-cards\` | Counterparty Cards only |

**In-storage README:** [COUNTERPARTY-CARD-STORAGE-README (external)](file:///X:/AI%20MARS%20STORAGE/atlas/evidence/counterparty-cards/README.md) — full operator rules at the storage location.

---

## 3. Organization folders (Wave 1)

| Folder | Organization slug |
|--------|-------------------|
| `polygon\` | Polygon |
| `metacode\` | MetaCode |
| `i-seo\` | I-SEO |
| `triumph\` | Triumph |
| `moscow-serm\` | Moscow SERM |
| `metallka\` | Metallka |

Each folder contains a `_PLACE_FILES_HERE.txt` placeholder. Replace nothing — add card files alongside it.

---

## 4. What belongs here

**Counterparty Cards only** — organization requisites and profile artifacts.

**Accepted formats:** PDF, DOCX, XLSX, JPG, PNG, TXT, copied messenger/email text (structured org profile).

**Do not place:**

- Contracts, acts, invoices, reports, technical specifications
- Contracts and acts belong to **OPS** — not ATLAS counterparty-card evidence
- MIG SERP packs or market research artifacts

Files are **evidence**, not canonical registry records.

---

## 5. ATLAS flow

```text
Counterparty Card → Evidence → Proposal → Review → Attestation → Registry
```

1. Operator places card file in the correct organization folder under external storage.
2. Steward references the file path as `evidence_ref` when building a proposal.
3. Review assigns evidence tier and checks boundaries.
4. Attestation promotes an Organization record — the file remains external evidence.

No automation, API, database, or extraction tooling is defined or required at this stage.

---

## 6. Relationship to MARS repo

| Location | Role |
|----------|------|
| `X:\AI MARS` | Git repository — ATLAS foundation, population plans, registry metadata |
| `X:\AI MARS STORAGE\atlas\evidence\counterparty-cards\` | External bulk evidence — Counterparty Card files |

**Rule:** Do not commit counterparty card files into the MARS git repository. Reference external paths in proposals and review notes only.

---

## 7. Operator next steps

1. Open `X:\AI MARS STORAGE\atlas\evidence\counterparty-cards\`.
2. Read the in-folder [README.md](file:///X:/AI%20MARS%20STORAGE/atlas/evidence/counterparty-cards/README.md).
3. Copy each organization's Counterparty Card / requisites file into the matching subfolder.
4. Use clear filenames (date, source, org name).
5. Notify the ATLAS steward that evidence is ready for Wave 1 organization proposals.

---

## 8. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-COUNTERPARTY-CARD-MODEL-v1.md](../foundation/ATLAS-COUNTERPARTY-CARD-MODEL-v1.md) | Card definition and boundaries |
| [ATLAS-ORGANIZATION-ACQUISITION-RULES-v1.md](../foundation/ATLAS-ORGANIZATION-ACQUISITION-RULES-v1.md) | Organization acquisition rules |
| [ATLAS-EVIDENCE-REQUIREMENTS-v1.md](../foundation/ATLAS-EVIDENCE-REQUIREMENTS-v1.md) | Evidence tiers |
| [ATLAS-WAVE-1-EXECUTION-v1.md](../foundation/ATLAS-WAVE-1-EXECUTION-v1.md) | Wave 1 execution |
| [X:\AI MARS STORAGE\README.md](file:///X:/AI%20MARS%20STORAGE/README.md) | MARS external bulk storage root |
