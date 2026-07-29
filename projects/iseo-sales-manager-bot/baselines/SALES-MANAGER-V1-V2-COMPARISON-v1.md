# SALES MANAGER V1/V2 COMPARISON v1

**Product:** i-SEO Sales Manager Bot  
**Phase:** 3A  
**Evidence class:** **Documented logical graph** (Phase 2 / OPERATIONAL-INDEX) — **not** sanitized export diff  
**Blocked:** Exact node-ID / connection-hash comparison until `Sales-Manager-v1.sanitized.json` + `Sales-Manager-v2.sanitized.json` exist

---

## 1. Authority

| Source | Role |
|--------|------|
| Phase 2 docs + `OPERATIONAL-INDEX.md` known baseline | Logical stages and known defects |
| Operator Phase 3A decisions | Target behavior |
| Missing exports | Exact JSON baseline **BLOCKED** |

---

## 2. Documented Sales-Manager-v2 logical stages

```
Schedule Trigger
→ Gmail get many (incoming leads label)
→ Lead-Mail-Parser
→ RAW append
→ Prepare OpenRouter
→ AI #1
→ Normalize
→ Prepare normalizer
→ AI #2
→ Normalize Clean Lead
→ Find Duplicate
→ Mark Duplicate
→ IF Bad Quality
→ CLEAN append
→ Telegram
→ Gmail PROCESSED + remove incoming
· error label branch
```

Sales-Manager-v1: treated as **predecessor** of the same product line. Exact node delta **SAFE UNKNOWN** without exports. Operator intent: v2 is the live-ish baseline to patch toward Operational.dev.

---

## 3. Comparison table (logical / design)

| Change area | V1→V2 (documented) | Classification | Target Operational.dev |
|-------------|--------------------|----------------|------------------------|
| Dual AI (#1 + #2 normalizer) | Present in v2 | **regression** / defect driver | **REMOVE** AI #2; one call max |
| Empty `ai_reply` / weak reply | Known defect | **regression** | Deterministic templates + validated AI |
| RAW AI columns pre-AI | Known defect | **regression** | RAW = parser only |
| CLEAN missing reply/AI/priority | Known defect | **regression** | Full CLEAN v2 columns |
| Optimistic quality | Known defect | **regression** | Strict quality contract |
| Weak dedupe | Known defect | **regression** | DEDUP_INDEX + enums |
| No manager lifecycle | Gap | **unresolved** in v2 | Minimal lifecycle on CLEAN |
| Telegram enums / ISO noise | Known defect | **regression** | UX contract Russian labels |
| No Admin / CONFIG | Gap | **obsolete** as solo-ops model | Separate Admin.dev |
| Schedule + Gmail intake | Core path retained | **improvement** keep | Retain with bounds |
| Error Gmail label branch | Present | **improvement** keep | Expand per Telegram-fail policy |
| Active state | Export may show inactive | **unresolved** | Confirm live in 3B |

---

## 4. Nodes — expected add / remove / change (target vs v2)

### Added (Operational.dev target)

CONFIG read · Deterministic Lead Processor · IF AI Enabled · Validate AI Result · Merge AI or Fallback · DEDUP_INDEX lookup/upsert · LEAD_EVENTS · ERRORS · Update Last Success · Telegram success IF · Preserve Incoming on TG fail

### Removed

Prepare AI normalizer · AI #2 · RAW AI pretence writes

### Changed heavily

Parser · Prepare AI Request (single schema) · OpenRouter AI (gated) · Duplicate classify · CLEAN map · Telegram formatter · Gmail label timing

---

## 5. Remaining defects (carry into patch)

1. Dual AI cost / skip-branch item loss risk.  
2. Success labeling before final delivery gate.  
3. Dedupe treating same message / weak keys as business repeat.  
4. Malformed contacts (`44`, `#ERROR!`) entering indexes.  
5. No AI OFF zero-call path.  
6. No admin surface for AI toggle / health.

---

## 6. Regression risks for Phase 3B

| Risk | Mitigation |
|------|------------|
| Patch applied to wrong live workflow | Operator confirms exact workflow ID |
| Label storm on reprocess | `reprocessed` + optional suppress unchanged |
| Sheets quota from full CLEAN reads | DEDUP_INDEX only |
| Markdown Telegram parse failures | Plain text / safe HTML |
| Downstream refs to skipped AI branch | Always forward deterministic item |

---

## 7. Refresh rule

When sanitized v1/v2 JSON land, replace this document’s **Blocked** sections with:

- nodes added / removed / changed (exact names);
- connection map delta;
- expression corrections;
- active state diff;
- credential placeholder inventory.

Until then: **do not** treat this file as live n8n proof.

---

*Related: SOURCE-GAP-MANIFEST-v1 · OPERATIONAL-WORKFLOW-PATCH-SPEC-v1 · N8N-CHANGE-PLAN-v1.*
