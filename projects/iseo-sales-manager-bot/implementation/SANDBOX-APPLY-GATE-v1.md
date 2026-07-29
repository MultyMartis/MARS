# SANDBOX APPLY GATE v1

**Product:** i-SEO Sales Manager Bot  
**Phase:** 3A defines gate · **Phase 3B** executes only after explicit operator approval  
**Protocol:** MetaBOT `safe-workflow-patch-protocol-v1` adapted to two-workflow Sales Manager

---

## 1. Verdict of Phase 3A relative to gate

Phase 3A prepares specs + optional sanitized baselines.  
**This gate is closed** until operator confirmations in §4 are collected.

Recommended next phase name:

**PHASE 3B — LIVE READ-ONLY AUDIT AND DEV WORKFLOW CREATION**

---

## 2. Phase 3B may

1. Access live n8n **read-only**.  
2. Identify exact Sales-Manager-v2 workflow (id + name).  
3. Create **one** `i-SEO Sales Manager - Operational.dev` copy.  
4. Optionally create **one** `i-SEO Sales Manager - Admin.dev` copy.  
5. Create sandbox sheet tabs **only after** operator approval.  
6. Apply patches to **.dev copies only**.  
7. Run synthetic fixtures with sandbox credentials/chats.  
8. Capture sanitized evidence + REPORT.

---

## 3. Phase 3B must not

| Forbidden |
|-----------|
| Modify original Sales-Manager-v2 |
| Activate Operational.dev automatically |
| Process real unread Gmail leads |
| Send to manager **production** chat |
| Call AI on real leads |
| Modify production Gmail labels |
| Auto-send client replies |
| Create disposable workflow copies per iteration |
| Create a third product workflow |
| Force-push / stage foreign WIP |

---

## 4. Required operator confirmations (checklist)

| # | Confirmation | Status |
|---|--------------|--------|
| 1 | Exact live workflow ID for Sales-Manager-v2 | **PENDING** |
| 2 | Exact RAW workbook | **PENDING** |
| 3 | Exact CLEAN workbook | **PENDING** |
| 4 | Manager Telegram bot/chat decision | **PENDING** |
| 5 | Admin Telegram bot/chat decision | **PENDING** |
| 6 | Approval to create v2 tabs | **PENDING** |
| 7 | Approval to create exactly two .dev workflows maximum | **PENDING** |
| 8 | Approval for read-only n8n audit | **PENDING** |
| 9 | Approval for synthetic sandbox tests | **PENDING** |
| 10 | Confirmation original workflow remains untouched | **PENDING** |

Additional recommended:

| # | Item |
|---|------|
| 11 | Source export drop completed + sanitized baselines promoted |
| 12 | AI remains OFF in CONFIG for first sandbox runs |
| 13 | Sandbox chat ids ≠ production manager chat |

---

## 5. Apply sequence (when opened)

1. Operator attestations §4 complete.  
2. Read-only export Sales-Manager-v2 → sanitize → refresh baselines if needed.  
3. Backup export of any existing .dev (if present).  
4. Create Operational.dev (inactive).  
5. Create Admin.dev (inactive) if approved.  
6. Create sandbox tabs per SHEETS-MIGRATION-SPEC.  
7. Apply node patches per OPERATIONAL / ADMIN specs.  
8. Run Programmer gates G1–G11.  
9. Run F01–F21 + Admin command tests with side effects disabled/sandbox-bound.  
10. REPORT + stop for promotion charter (not auto-prod).

---

## 6. Rollback (sandbox)

Per ROLLBACK-PLAN-v1: disable .dev → restore last good export → force `ai_enabled=false` → smoke `/health` + synthetic only.

---

## 7. Production boundary

Production / live label processing / production Telegram manager chat = **separate charter after** sandbox exit criteria.  
Maximum live copies forever for v1 product: one Operational + one Admin (naming may drop `.dev` later under charter).

---

## 8. Stop condition (this document’s authority)

Do **not** begin Phase 3B from Phase 3A automation. Human operator must explicitly open the gate.

---

*Related: METABOT-PROGRAMMER-IMPLEMENTATION-BRIEF-v1 · ROLLBACK-PLAN-v1 · safe-workflow-patch-protocol-v1.*
