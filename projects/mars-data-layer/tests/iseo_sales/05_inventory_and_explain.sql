-- Schema inventory + EXPLAIN sanity (read-only probes)
\pset format aligned
\pset tuples_only off

SELECT '=== schemas ===' AS section;
SELECT nspname, pg_catalog.pg_get_userbyid(nspowner) AS owner
FROM pg_namespace
WHERE nspname IN ('mars_core', 'app_iseo_sales', 'app_seo_content')
ORDER BY 1;

SELECT '=== mars_core tables ===' AS section;
SELECT c.relname AS object, 'table' AS type, TRUE AS exists,
       pg_catalog.pg_get_userbyid(c.relowner) AS owner, '' AS notes
FROM pg_class c
JOIN pg_namespace n ON n.oid = c.relnamespace
WHERE n.nspname = 'mars_core' AND c.relkind = 'r'
ORDER BY 1;

SELECT '=== app_iseo_sales tables ===' AS section;
SELECT c.relname AS object, 'table' AS type, TRUE AS exists,
       pg_catalog.pg_get_userbyid(c.relowner) AS owner, '' AS notes
FROM pg_class c
JOIN pg_namespace n ON n.oid = c.relnamespace
WHERE n.nspname = 'app_iseo_sales' AND c.relkind = 'r'
ORDER BY 1;

SELECT '=== app_iseo_sales functions ===' AS section;
SELECT p.proname AS object, 'function' AS type, TRUE AS exists,
       pg_catalog.pg_get_userbyid(p.proowner) AS owner,
       pg_get_function_identity_arguments(p.oid) AS notes
FROM pg_proc p
JOIN pg_namespace n ON n.oid = p.pronamespace
WHERE n.nspname = 'app_iseo_sales'
ORDER BY 1, 5;

SELECT '=== PUBLIC schema privileges (should be empty for app schemas) ===' AS section;
SELECT nspname,
       has_schema_privilege('public', nspname, 'USAGE') AS public_usage,
       has_schema_privilege('public', nspname, 'CREATE') AS public_create
FROM pg_namespace
WHERE nspname IN ('mars_core', 'app_iseo_sales', 'app_seo_content');

SELECT '=== EXPLAIN: source lookup ===' AS section;
EXPLAIN (FORMAT TEXT)
SELECT * FROM app_iseo_sales.inbound_events
WHERE source_system = 'gmail' AND source_id = 'msgid-synthetic-001';

SELECT '=== EXPLAIN: lead_id lookup ===' AS section;
EXPLAIN (FORMAT TEXT)
SELECT * FROM app_iseo_sales.leads WHERE lead_id = 'LEAD_SYNTH000001';

SELECT '=== EXPLAIN: pending leads ===' AS section;
EXPLAIN (FORMAT TEXT)
SELECT * FROM app_iseo_sales.leads
WHERE manager_status IN ('new', 'pending')
ORDER BY updated_at ASC
LIMIT 50;

SELECT '=== EXPLAIN: jobs available ===' AS section;
EXPLAIN (FORMAT TEXT)
SELECT * FROM app_iseo_sales.jobs
WHERE status IN ('pending', 'retry') AND available_at <= now()
ORDER BY priority ASC, available_at ASC
LIMIT 10;

SELECT '=== EXPLAIN: deliveries pending ===' AS section;
EXPLAIN (FORMAT TEXT)
SELECT * FROM app_iseo_sales.deliveries WHERE status = 'pending' LIMIT 50;
