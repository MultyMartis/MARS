# i-SEO Sales — Data Open Questions v1

**Document:** `ISEO-SALES-DATA-OPEN-QUESTIONS-v1`  
**project_id:** `mars-data-layer`  
**Date:** 2026-09-03  
**Rule:** only genuine blockers/uncertainties — no invented business rules  
**Update:** post shadow-migration forensic `20260903T091128Z`

---

## Q1. Exact `lead_id` generation algorithm

| Field | Content |
|-------|---------|
| **Question** | What exact algorithm mints production `lead_id` (`LEAD_<12 hex>` vs UUID/ULID vs `lead_<hex>`)? |
| **Evidence** | Live CLEAN collapse shows opaque text IDs; multiple historical shapes; import stores as `text` |
| **Classification** | **NON-BLOCKING** for PG_SHADOW; **OPERATOR DECISION REQUIRED BEFORE CUTOVER** for Toolkit mint freeze |
| **Consequence** | PG uniqueness on `lead_id` works; new minting must match product code |
| **Recommended default** | Keep opaque text uniqueness; mint in workflow/parser as today until single generator is documented |

---

## Q2. CLEAN / DEDUP writer: append vs upsert (live)

| Field | Content |
|-------|---------|
| **Question** | Is current production CLEAN/DEDUP writer still `append` with empty `matchingColumns` or restored to upsert? |
| **Evidence** | Forensic: RAW ~17.5k / CLEAN ~7.9k with few unique IDs → append-history confirmed in practice |
| **Classification** | **RESOLVED** for migration strategy (collapse latest + PG UNIQUE). Sheets hygiene optional ops fix |
| **Consequence** | Import must collapse duplicates; shadow dual-write must use PG upsert regardless |
| **Recommended default** | Treat Sheets as dirty append-capable; PG enforces uniqueness |

---

## Q3. Full `LEAD_DELIVERIES` / reminder ledger column enums

| Field | Content |
|-------|---------|
| **Question** | Exact status enum and full column set for deliveries? |
| **Evidence** | Live columns include `delivery_key`, `stable_lead_ref`, `delivery_status`, `delivered_at`, telegram refs; adapter maps to outbox enum; historical pending forced non-pending |
| **Classification** | **RESOLVED** enough for shadow; residual malformed/orphan rows documented |
| **Consequence** | Candidate workers must not resume historical cancelled/sent as pending |
| **Recommended default** | Keep adapter; treat unknown with message id as `sent` else `cancelled` for history |

---

## Q4. Dual lifecycle vocabularies

| Field | Content |
|-------|---------|
| **Question** | Should PG permanently support both CRM lifecycle and Telegram ops statuses? |
| **Evidence** | Collapsed live statuses in shadow: `new/pending/processed/spam` only (exact Sheets match) |
| **Classification** | **NON-BLOCKING**; soft product decision before Admin UX redesign |
| **Consequence** | CHECK admits union; runtime writers currently use ops subset |
| **Recommended default** | Keep union in V1 CHECK; document ops subset as runtime writers |

---

## Q5. Local PostgreSQL runtime availability

| Field | Content |
|-------|---------|
| **Question** | When will disposable local PG under `X:\MARS-Localhost\...` be installed? |
| **Evidence** | Shadow apply validated on server `mars-postgres` (PG18) this wave |
| **Classification** | **NON-BLOCKING** for shadow migration (server path proven) |
| **Consequence** | Local disposable still useful for offline tooling |
| **Recommended default** | Follow local DB contract; not required to claim shadow PASS |

---

## New residuals from shadow wave (not original Q1–Q4)

| Item | Classification |
|------|----------------|
| 67 deliveries with null `lead_id` (orphan stable_lead_ref) | **NON-BLOCKING** for shadow; **OPERATOR DECISION** before cutover UX |
| 1 malformed delivery row | **NON-BLOCKING** / UNKNOWN retained |
| DEDUP sheet empty keys | **RESOLVED** via synth `lead_dedup_keys` + constraints |
| ACCESS only 1 active admin at T0 | Fidelity PASS; re-check at cutover freeze |
