# Deep Research Backlog

## 1. PostgreSQL Schema Minimalism

**QUESTION:** What is the smallest schema that preserves RAW/CLEAN/events/dedupe?  
**WHY:** Avoid overbuilding CRM tables.  
**ASSUMPTION:** Current lifecycle remains small.  
**DECISION IMPACT:** Successor schema scope.

## 2. Gmail Source Fidelity

**QUESTION:** Which Gmail payload fields best preserve multilingual structured requests?  
**WHY:** Prevent raw-source regressions.  
**ASSUMPTION:** `text/plain` is usually best, HTML fallback still needed.  
**DECISION IMPACT:** Intake adapter design.

## 3. Callback Token Shape

**QUESTION:** What minimal token data guarantees safe lead resolution?  
**WHY:** Avoid broad reads and stale actions.  
**ASSUMPTION:** `lead_id` remains primary identity.  
**DECISION IMPACT:** Telegram callback contract.

## 4. Reminder Candidate Query

**QUESTION:** How should pending/actionable be represented in SQL?  
**WHY:** Candidate logic must be auditable.  
**ASSUMPTION:** Reminders remain notification-only.  
**DECISION IMPACT:** Status fields and indexes.

## 5. Monday Backlog Semantics

**QUESTION:** Should weekend backlog be all pending or only newly arrived weekend leads?  
**WHY:** Avoid over/under-notification.  
**ASSUMPTION:** Current stable includes weekend pending backlog.  
**DECISION IMPACT:** Reminder UX and query.

## 6. Operator Authorization Model

**QUESTION:** Should access and delivery recipients be separate tables?  
**WHY:** Admin rights and notification delivery are different concerns.  
**ASSUMPTION:** Future product may add delivery modes.  
**DECISION IMPACT:** Operator model.

## 7. Sheets Export Format

**QUESTION:** What Sheets export remains useful after PostgreSQL migration?  
**WHY:** Managers may still want human-readable sheets.  
**ASSUMPTION:** Sheets becomes read/report layer.  
**DECISION IMPACT:** Export schedule and columns.

## 8. Legacy Source Recovery

**QUESTION:** How long should READ-only Gmail fallback remain available?  
**WHY:** Legacy records may need source display.  
**ASSUMPTION:** Fallback must not replay ingestion.  
**DECISION IMPACT:** Retention and support policy.

## 9. Error Taxonomy

**QUESTION:** Which failures need operator-visible categories?  
**WHY:** Recovery runbooks need consistent signals.  
**ASSUMPTION:** Current ERRORS are lightweight.  
**DECISION IMPACT:** Observability model.

## 10. Delivery Retry Policy

**QUESTION:** What retry limits prevent duplicate Telegram noise?  
**WHY:** Delivery reliability and user trust.  
**ASSUMPTION:** Telegram delivery may fail transiently.  
**DECISION IMPACT:** Retry/backoff design.

## 11. Idempotency Guarantees

**QUESTION:** Which operations require strict idempotency keys?  
**WHY:** External systems can re-deliver callbacks.  
**ASSUMPTION:** Processed/spam repeats should be safe.  
**DECISION IMPACT:** Event and action tables.

## 12. AI Reintroduction Criteria

**QUESTION:** What evidence is required before AI can be enabled?  
**WHY:** Stable production is deterministic.  
**ASSUMPTION:** AI may be useful but risky.  
**DECISION IMPACT:** AI roadmap gate.

## 13. DND And Escalation

**QUESTION:** How should DND interact with urgent leads and backlog?  
**WHY:** Notification silence can hide work.  
**ASSUMPTION:** DND is not current production.  
**DECISION IMPACT:** Delivery product scope.

## 14. Admin Panel UX

**QUESTION:** Which admin actions are safe in Telegram?  
**WHY:** Avoid hidden high-risk controls.  
**ASSUMPTION:** Admin should stay operator-safe.  
**DECISION IMPACT:** `/admin` roadmap.

## 15. Stable Freeze Evidence Standard

**QUESTION:** What evidence is enough for future baseline freeze?  
**WHY:** Prevent premature PASS claims.  
**ASSUMPTION:** Natural observations may remain pending.  
**DECISION IMPACT:** Release governance.

