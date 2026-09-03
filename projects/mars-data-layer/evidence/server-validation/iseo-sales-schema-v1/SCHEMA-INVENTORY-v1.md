# SCHEMA-INVENTORY-v1 (server PG18)

**Owner for all listed DDL objects:** `mars_migrator`  
**Source:** post-apply inventory on `mars` @ VEESP-N8N-01  
**Raw:** `SCHEMA-INVENTORY-RAW-v1.md`

| Object | Type | Owner | Expected | Valid |
|---|---|---|---|---|
| mars_core.schema_migrations | table | mars_migrator | yes | yes |
| mars_core.apps | table | mars_migrator | yes | yes |
| mars_core.data_contract_versions | table | mars_migrator | yes | yes |
| mars_core.workflow_releases | table | mars_migrator | yes | yes |
| app_iseo_sales.inbound_events | table | mars_migrator | yes | yes |
| app_iseo_sales.leads | table | mars_migrator | yes | yes |
| app_iseo_sales.lead_events | table | mars_migrator | yes | yes |
| app_iseo_sales.lead_dedup_keys | table | mars_migrator | yes | yes |
| app_iseo_sales.idempotency_keys | table | mars_migrator | yes | yes |
| app_iseo_sales.deliveries | table | mars_migrator | yes | yes |
| app_iseo_sales.jobs | table | mars_migrator | yes | yes |
| app_iseo_sales.audit_logs | table | mars_migrator | yes | yes |
| app_iseo_sales.errors | table | mars_migrator | yes | yes |
| app_iseo_sales.config | table | mars_migrator | yes | yes |
| app_iseo_sales.access_rules | table | mars_migrator | yes | yes |
| app_iseo_sales.register_inbound_event | function | mars_migrator | yes | yes |
| app_iseo_sales.upsert_lead | function | mars_migrator | yes | yes |
| app_iseo_sales.change_lead_status | function | mars_migrator | yes | yes |
| app_iseo_sales.enqueue_delivery | function | mars_migrator | yes | yes |
| app_iseo_sales.enqueue_job | function | mars_migrator | yes | yes |
| app_iseo_sales.claim_jobs | function | mars_migrator | yes | yes |
| app_iseo_sales.get_lead | function | mars_migrator | yes | yes |
| app_iseo_sales.list_pending_leads | function | mars_migrator | yes | yes |
| app_iseo_sales.fn_is_allowed_status_transition | function | mars_migrator | yes | yes |
| uq_inbound_events_source | unique index | mars_migrator | yes | yes |
| uq_leads_lead_id | unique index | mars_migrator | yes | yes |
| uq_leads_source_message_id | unique index | mars_migrator | yes | yes |
| uq_deliveries_idempotency_key | unique index | mars_migrator | yes | yes |
| uq_jobs_dedupe_key | unique index | mars_migrator | yes | yes |
| idx_jobs_status_available | index | mars_migrator | yes | yes |
| idx_deliveries_status_available_pending_retry | index | mars_migrator | yes | yes |

**Notes**

- `mars_core` contains control metadata only (no iSEO business rows from this wave beyond migration registry / seed apps as defined by migrations).
- Sequences (`*_id_seq`) and PK/UQ indexes present per RAW inventory (72 catalog rows + 9 functions).
- Placeholder / empty `app_seo_content` used for isolation checks in permission suite (no SEO Content model).
