# SCHEMA-INVENTORY-v1

**Date:** 2026-09-03  
**DB:** `mars` @ `127.0.0.1:5433`  
**Owner:** `mars_owner`  
**Source tip baseline:** `eb19cfad`

## mars_core

| Object | Type | Exists | Owner | Notes |
|--------|------|--------|-------|-------|
| mars_core | schema | Yes | mars_owner | core foundation |
| schema_migrations | table | Yes | mars_owner | release tracking |
| apps | table | Yes | mars_owner | |
| data_contract_versions | table | Yes | mars_owner | |
| workflow_releases | table | Yes | mars_owner | |
| (related indexes) | index | Yes | mars_owner | per migration 0002 |

## app_iseo_sales — tables

| Object | Type | Exists | Owner | Notes |
|--------|------|--------|-------|-------|
| inbound_events | table | Yes | mars_owner | unique (source_system, source_id) |
| leads | table | Yes | mars_owner | unique lead_id; versioned status |
| lead_dedup_keys | table | Yes | mars_owner | |
| lead_events | table | Yes | mars_owner | append-oriented domain events |
| access_rules | table | Yes | mars_owner | |
| deliveries | table | Yes | mars_owner | outbox/delivery intents |
| jobs | table | Yes | mars_owner | queue + lease |
| idempotency_keys | table | Yes | mars_owner | |
| errors | table | Yes | mars_owner | |
| audit_logs | table | Yes | mars_owner | |
| config | table | Yes | mars_owner | |

## app_iseo_sales — functions (selected)

| Object | Type | Exists | Owner | Notes |
|--------|------|--------|-------|-------|
| register_inbound_event | function | Yes | mars_owner | |
| upsert_lead | function | Yes | mars_owner | |
| change_lead_status | function | Yes | mars_owner | |
| enqueue_delivery | function | Yes | mars_owner | |
| enqueue_job | function | Yes | mars_owner | |
| get_lead | function | Yes | mars_owner | |
| list_pending_leads | function | Yes | mars_owner | |
| claim_jobs | function | Yes | mars_owner | SKIP LOCKED |
| fn_is_allowed_status_transition | function | Yes | mars_owner | |

## Placeholder / boundary

| Object | Type | Exists | Owner | Notes |
|--------|------|--------|-------|-------|
| app_seo_content | schema | Yes | mars_owner | placeholder; iseo_runtime has no USAGE |

Full machine inventory also captured via `05_inventory_and_explain.sql` / `_inventory-explain-pass2.log`.
