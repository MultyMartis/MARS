# SHEET DATA QUALITY FINDINGS v1

**Product:** i-SEO Sales Manager Bot  
**Phase:** 3A.1  
**Sources:** RAW + CLEAN XLSX (STORAGE) — no customer values reproduced

---

## 1. Executive findings

| ID | Finding | Severity | Tied defect |
|----|---------|----------|-------------|
| Q1 | RAW AI columns 100% empty while mapped | High | RAW pre-AI write |
| Q2 | CLEAN quality always ok (19/19) | High | Optimistic quality |
| Q3 | RAW client_contact errors ×6 | High | Parser / coercion |
| Q4 | email_subject all UNKNOWN | Medium | Parser subject |
| Q5 | Name overflow suspects ×8 | High | Parser field bleed |
| Q6 | CLEAN primary_contact formula-like ×10 | Medium | Contact normalization |
| Q7 | Duplicate lead_id repeat groups | Medium | Append without upsert |
| Q8 | CLEAN lacks first-reply columns | High | Schema gap |
| Q9 | Messenger nearly unused | Low | Extraction gap |
| Q10 | Customer domains present in workbook | Info | Keep out of Git docs |

## 2. RAW aggregates

Rows 19 on `lead-base`. AI fill 0%. `processing_status=parsed` universal. Phone-heavy contacts. Error-class values in `client_contact`.

## 3. CLEAN aggregates

Rows 19 on `lead-base-processed`. quality ok-only. duplicate new/repeat only (no reprocessed/possible). manager_status all new. Service SEO/Audit/Other present.

## 4. Parser drift evidence

Long names with thin request_text; subject always UNKNOWN; AI empties with CLEAN summaries filled; no parser_version column → exact build split **SAFE UNKNOWN**.

## 5. Implications

Recompute quality; exclude errors from DEDUP; treat repeated lead_id as reprocess candidates; historical tabs read-only; first sandbox AI OFF + synthetic only.
