# SANDBOX APPLY GATE v1

**Product:** i-SEO Sales Manager Bot  
**Phase:** 3A.1 revalidated · **Phase 3B** executes only after explicit operator approval  
**Protocol:** MetaBOT `safe-workflow-patch-protocol-v1` adapted to two-workflow Sales Manager

---

## 1. Verdict relative to gate

Phase 3A.1 completed source ingest, sanitization, exact V1/V2 baselines, sheet schema forensics, and implementation reconciliation.

**Technically ready for operator sandbox-gate review:** YES (documentation / baselines).  
**This gate remains closed** until operator confirmations in §4 are collected.  
**Phase 3B is not auto-approved.**

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
| 2 | Exact RAW workbook (confirm export matches live `<RAW_WORKBOOK_ID>`) | **PENDING** |
| 3 | Exact CLEAN workbook (confirm export matches live `<CLEAN_WORKBOOK_ID>`) | **PENDING** |
| 4 | Manager Telegram bot/chat decision | **PENDING** |
| 5 | Admin Telegram bot/chat decision | **PENDING** |
| 6 | Authorization to create v2 tabs | **PENDING** |
| 7 | Authorization to create exactly two .dev workflows maximum | **PENDING** |
| 8 | Authorization for read-only n8n audit | **PENDING** |
| 9 | Authorization for synthetic sandbox tests | **PENDING** |
| 10 | Confirmation original workflow remains untouched | **PENDING** |

Additional:

| # | Item | Status |
|---|------|--------|
| 11 | Source export drop completed + sanitized baselines promoted | **DONE** (Phase 3A.1) |
| 12 | AI remains OFF in CONFIG for first sandbox runs | **PENDING** operator attest |
| 13 | Sandbox chat ids ≠ production manager chat | **PENDING** |

---

## 5. Export-evidenced constraints for Phase 3B patches

Confirmed from sanitized v2 (do not redesign away):

- Remove AI #2 chain (`Prepare-AI-Normalizer-Request`, `AI-Normalizer (AI #2)`).
- Stop RAW AI-column writes; keep RAW after parse.
- Replace full CLEAN duplicate read with `DEDUP_INDEX`.
- Add Telegram success IF before PROCESSED; on TG fail → ERROR label and **preserve** incoming.
- Bound Gmail fetch (`returnAll=true` is unsafe).
- Historical sheets `lead-base` / `lead-base-processed` remain untouched.

Sandbox default remains: **disabled=`true`** on Gmail mutate / Telegram send / OpenRouter until operator enables synthetic tests.

---

## 6. Apply sequence (when opened)

1. Operator attestations §4 complete.  
2. Read-only export Sales-Manager-v2 → sanitize → refresh baselines if drift.  
3. Backup export of any existing .dev (if present).  
4. Create Operational.dev (inactive).  
5. Create Admin.dev (inactive) if approved.  
6. Create sandbox tabs per SHEETS-MIGRATION-SPEC.  
7. Apply node patches per OPERATIONAL / ADMIN specs.  
8. Run Programmer gates G1–G11.  
9. Run F01–F21 + Admin command tests with side effects disabled/sandbox-bound.  
10. REPORT + stop for promotion charter (not auto-prod).

---

## 7. Rollback (sandbox)

Per ROLLBACK-PLAN-v1: disable .dev → restore last good export → force `ai_enabled=false` → smoke `/health` + synthetic only.

---

## 8. Production boundary

Production / live label processing / production Telegram manager chat = **separate charter after** sandbox exit criteria.  
Maximum live copies forever for v1 product: one Operational + one Admin (naming may drop `.dev` later under charter).

---

## 9. Stop condition

Do **not** begin Phase 3B from Phase 3A.1 automation. Human operator must explicitly open the gate.

---

*Related: METABOT-PROGRAMMER-IMPLEMENTATION-BRIEF-v1 · ROLLBACK-PLAN-v1 · safe-workflow-patch-protocol-v1 · Phase 3A.1 report.*
