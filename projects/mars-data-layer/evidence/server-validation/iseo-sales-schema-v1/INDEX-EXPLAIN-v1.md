# INDEX-EXPLAIN-v1

**Suite:** `tests/iseo_sales/05_inventory_and_explain.sql`
**Status:** PASS

**EXPECTED INDEX USAGE:** PASS (Index Scan / Bitmap Index Scan on hot paths where rows exist; Seq Scan acceptable on empty tables).

```
Output format is aligned.
     section     
-----------------
 === schemas ===
(1 row)

     nspname     |     owner     
-----------------+---------------
 app_iseo_sales  | <redacted>_migrator
 app_seo_content | <redacted>_migrator
 <redacted>_core       | <redacted>_migrator
(3 rows)

         section          
--------------------------
 === <redacted>_core tables ===
(1 row)

         object         | type  | exists |     owner     | notes 
------------------------+-------+--------+---------------+-------
 apps                   | table | t      | <redacted>_migrator | 
 data_contract_versions | table | t      | <redacted>_migrator | 
 schema_migrations      | table | t      | <redacted>_migrator | 
 workflow_releases      | table | t      | <redacted>_migrator | 
(4 rows)

            section            
-------------------------------
 === app_iseo_sales tables ===
(1 row)

      object      | type  | exists |     owner     | notes 
------------------+-------+--------+---------------+-------
 access_rules     | table | t      | <redacted>_migrator | 
 audit_logs       | table | t      | <redacted>_migrator | 
 config           | table | t      | <redacted>_migrator | 
 deliveries       | table | t      | <redacted>_migrator | 
 errors           | table | t      | <redacted>_migrator | 
 idempotency_keys | table | t      | <redacted>_migrator | 
 inbound_events   | table | t      | <redacted>_migrator | 
 jobs             | table | t      | <redacted>_migrator | 
 lead_dedup_keys  | table | t      | <redacted>_migrator | 
 lead_events      | table | t      | <redacted>_migrator | 
 leads            | table | t      | <redacted>_migrator | 
(11 rows)

             section              
----------------------------------
 === app_iseo_sales functions ===
(1 row)

             object              |   type   | exists |     owner     |                                                                                                                                                                                   notes                                                                                                                                                                                    
---------------------------------+----------+--------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 change_lead_status              | function | t      | <redacted>_migrator | p_lead_id text, p_expected_version integer, p_from_status text, p_to_status text, p_actor_type text, p_actor_id text, p_idempotency_key text, p_correlation_id text, p_close_reason text, p_notes text
 claim_jobs                      | function | t      | <redacted>_migrator | p_worker text, p_limit integer, p_lease_seconds integer
 enqueue_delivery                | function | t      | <redacted>_migrator | p_lead_id text, p_channel text, p_recipient_principal_key text, p_recipient_telegram_user_id text, p_delivery_type text, p_payload jsonb, p_idempotency_key text, p_correlation_id text, p_available_at timestamp with time zone, p_delivery_id text
 enqueue_job                     | function | t      | <redacted>_migrator | p_job_type text, p_payload jsonb, p_priority integer, p_available_at timestamp with time zone, p_dedupe_key text, p_correlation_id text, p_lead_id text
 fn_is_allowed_status_transition | function | t      | <redacted>_migrator | p_from text, p_to text
 get_lead                        | function | t      | <redacted>_migrator | p_lead_id text
 list_pending_leads              | function | t      | <redacted>_migrator | p_limit integer
 register_inbound_event          | function | t      | <redacted>_migrator | p_source_system text, p_source_id text, p_payload jsonb, p_raw_text text, p_correlation_id text, p_gmail_thread_id text, p_received_at timestamp with time zone, p_subject text, p_from_email text, p_normalized_hash text, p_parser_version text, p_workflow_version text
 upsert_lead                     | function | t      | <redacted>_migrator | p_lead_id text, p_inbound_event_id bigint, p_source_message_id text, p_client_name text, p_primary_contact text, p_contact_type text, p_phone text, p_email text, p_messenger text, p_site text, p_service text, p_summary text, p_source text, p_manager_status text, p_form_metadata jsonb, p_data_contract_version text, p_workflow_version text, p_parser_version text
(9 rows)

                              section                               
--------------------------------------------------------------------
 === PUBLIC schema privileges (should be empty for app schemas) ===
(1 row)

     nspname     | public_usage | public_create 
-----------------+--------------+---------------
 <redacted>_core       | f            | f
 app_iseo_sales  | f            | f
 app_seo_content | f            | f
(3 rows)

            section             
--------------------------------
 === EXPLAIN: source lookup ===
(1 row)

                                           QUERY PLAN                                            
-------------------------------------------------------------------------------------------------
 Index Scan using uq_inbound_events_source on inbound_events  (cost=0.14..8.16 rows=1 width=500)
   Index Cond: ((source_system = 'gmail'::text) AND (source_id = 'msgid-synthetic-001'::text))
(2 rows)

             section             
---------------------------------
 === EXPLAIN: lead_id lookup ===
(1 row)

                                   QUERY PLAN                                    
---------------------------------------------------------------------------------
 Index Scan using uq_leads_lead_id on leads  (cost=0.14..8.16 rows=1 width=1558)
   Index Cond: (lead_id = 'LEAD_SYNTH000001'::text)
(2 rows)

            section             
--------------------------------
 === EXPLAIN: pending leads ===
(1 row)

                                                QUERY PLAN                                                 
-----------------------------------------------------------------------------------------------------------
 Limit  (cost=9.51..9.51 rows=2 width=1558)
   ->  Sort  (cost=9.51..9.51 rows=2 width=1558)
         Sort Key: updated_at
         ->  Bitmap Heap Scan on leads  (cost=4.16..9.50 rows=2 width=1558)
               Recheck Cond: (manager_status = ANY ('{new,pending}'::text[]))
               ->  Bitmap Index Scan on idx_leads_manager_status_updated  (cost=0.00..4.15 rows=2 width=0)
                     Index Cond: (manager_status = ANY ('{new,pending}'::text[]))
(7 rows)

             section             
---------------------------------
 === EXPLAIN: jobs available ===
(1 row)

                                             QUERY PLAN                                             
----------------------------------------------------------------------------------------------------
 Limit  (cost=8.18..8.18 rows=1 width=324)
   ->  Sort  (cost=8.18..8.18 rows=1 width=324)
         Sort Key: priority, available_at
         ->  Index Scan using idx_jobs_status_available on jobs  (cost=0.15..8.17 rows=1 width=324)
               Index Cond: ((status = ANY ('{pending,retry}'::text[])) AND (available_at <= now()))
(5 rows)

               section               
-------------------------------------
 === EXPLAIN: deliveries pending ===
(1 row)

                                                       QUERY PLAN                                                       
------------------------------------------------------------------------------------------------------------------------
 Limit  (cost=0.14..8.16 rows=1 width=488)
   ->  Index Scan using idx_deliveries_status_available_pending_retry on deliveries  (cost=0.14..8.16 rows=1 width=488)
         Index Cond: (status = 'pending'::text)
(3 rows)

TEST_OK=tests/iseo_sales/05_inventory_and_explain.sql

```
