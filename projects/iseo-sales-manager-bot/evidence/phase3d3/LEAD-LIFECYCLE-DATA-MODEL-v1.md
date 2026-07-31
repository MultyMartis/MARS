# LEAD LIFECYCLE DATA MODEL v1

Statuses: pending | processed | spam (default pending).  
CLEAN extended (+13 headers) to 65 columns including telegram_* refs and manager action stamps.  
Existing `processed_at` remains bot processing time; manager processed uses `manager_action_processed_at` / `closed_at`.  
LEAD_EVENTS append-only for manager actions.  
No RAW/CLEAN deletion on spam.
