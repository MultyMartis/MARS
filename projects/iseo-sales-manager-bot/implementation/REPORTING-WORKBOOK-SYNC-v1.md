# REPORTING WORKBOOK SYNC v1

Placement: shared safe functions inside Operational.dev / Admin.dev (no new workflow).

New real lead: backend LEADS + events + delivery → upsert reporting `Лиды` → append history → SYNC_STATE.

Lifecycle: backend commit → event → update reporting row → history → SYNC_STATE.

Call budget: no reporting IO on empty polls; one upsert/event per real change; stats refresh only after meaningful changes.


## 3F.2.1 keyed contract

Use explicit header→field map. Forbid index fallbacks. Map event codes to Russian labels before writing history/last-event cells.
