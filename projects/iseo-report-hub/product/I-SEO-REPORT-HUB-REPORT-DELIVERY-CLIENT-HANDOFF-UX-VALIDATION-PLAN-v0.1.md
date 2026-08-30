# I-SEO Report Hub — Report Delivery Client Handoff UX Validation Plan v0.1

**Status:** VALIDATION PLAN / POLICY ONLY — no smoke execution in this charter wave  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-28  
**Authority:** Operator I-SEO Report Hub Report Delivery Client Handoff UX Charter 01  
**Related:**
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-CHARTER-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-DESIGN-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-DESIGN-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-IMPLEMENTATION-PLAN-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-VISUAL-QA-RESULT-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-VISUAL-QA-RESULT-v0.1.md)

---

## 1. Purpose

Define how to validate Client Handoff UX Implementation 01 (and this charter’s assumptions) without expanding public surface or breaking Public Share hardening.

This charter wave itself performs **docs only** — validation below is for the **next** implementation wave (and optional pre-checks).

---

## 2. Baseline validation

Before Implementation 01:

| Check | Expected |
|-------|----------|
| Branch | `mars/canonical-post-recovery` |
| Volume | `AI WS` on `X:` |
| Public Share Visual QA | COMPLETE; `PASS_WITH_MINOR_ISSUES` |
| schema_migrations | **9** |
| tables | **16** |
| report_exports | **4** |
| report_export_shares | **4** revoked / active **0** (or documented equivalent after later smoke) |
| Artifact checksums | v1/v2 HTML/PDF unchanged vs known hashes |
| Public route | still direct PDF stream |

---

## 3. Handoff readiness validation

| Case | Expect |
|------|--------|
| Export id 4 (styled PDF) | Readiness can pass when active share exists |
| Export ids 1–3 | Not shareable; checklist fails with clear reasons |
| Finalized + snapshot + ready PDF + metadata + active share | “Ready to handoff” affirmative |
| Missing active share | Not ready; CTA create |
| Revoked/expired only | Not ready; recreate |

---

## 4. Once URL validation

| Case | Expect |
|------|--------|
| Immediately after create | `{share_url}` present; copy pack enabled |
| Revisit shares page | once box gone; no reconstructed URL |
| Client templates without URL | disabled or clearly unavailable |
| Lost URL path | revoke + recreate restores once display |

---

## 5. Copy template validation

| Check | Expect |
|-------|--------|
| Short message | Russian template filled; includes URL + expiry |
| Formal email | Subject + body filled |
| Internal note | Operator fields; warnings present |
| No storage path | Client templates never include `storage/exports/...` |
| No token_hash | Never in UI or copy |
| No live token in Git docs/evidence | redact `[REDACTED_64HEX_TOKEN]` |

---

## 6. Token redaction

- Smoke logs / evidence / reports: redact plaintext tokens.
- DB remains hash-only.
- Clipboard contents are runtime-only; not committed.

---

## 7. Not shareable labels

| Surface | Expect after Implementation 01 |
|---------|--------------------------------|
| Export list | Badge **Not shareable** (not bare `No`) |
| Export detail | **Not shareable** + reason |
| Consistency | List and detail wording aligned |

---

## 8. Storage path de-emphasis

| Check | Expect |
|-------|--------|
| Auth export detail | Relative path not primary; under technical details if shown |
| Label | Internal artifact path |
| Client copy | Path absent |
| Public response | No path leak (existing hardening) |

---

## 9. No DB migration / no unintended mutation

For no-migration Implementation 01:

| Check | Expect |
|-------|--------|
| New migration files | **none** |
| schema_migrations | unchanged (**9**) unless separate DB-11 charter |
| Business tables | unchanged counts except intentional share smoke rows |
| report_exports | no mutation |
| Artifacts | unchanged checksums |
| After smoke | prefer active shares **0** (revoke QA shares) unless operator charter keeps one |

This charter wave: **zero** DB mutation.

---

## 10. Security restrictions

Validate still true:

- 64-hex token gate;
- malformed/invalid **404**;
- revoked/expired **410**;
- PDF attachment + nosniff + private/no-store + noindex headers;
- no public listing;
- no public landing HTML in MVP;
- no email send;
- no client portal.

---

## 11. Visual QA validation

Re-check Visual QA minors after Implementation 01:

| ID | Pass criteria |
|----|---------------|
| `UI-REL-STORAGE-PATH` | Path de-emphasized / disclosed as technical; not in handoff copy |
| `UI-LIST-SHARE-LABEL` | Unified **Not shareable** |

Optional: short regression smoke subset of Public Share Visual QA public route cases to prove stream unchanged.
