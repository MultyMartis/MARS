
DELETE FROM mars_core.workflow_releases wr
USING mars_core.apps a
WHERE wr.app_id = a.id
  AND a.app_key = 'app_iseo_sales'
  AND wr.workflow_family = 'operational_intake'
  AND wr.release_version = 'Operational.dev';

INSERT INTO mars_core.workflow_releases (
  app_id, workflow_family, n8n_workflow_id, release_version,
  data_contract_version, status, git_export_hash, activated_at, notes, metadata
)
SELECT a.id, 'operational_intake', 'xSnXPy8cEHoZw6xG', 'Operational.dev',
  'sheets-legacy-v1', 'active', 'e299a967dbffc57341dd24bf87e7c17bf885a74f760ffdebb6a9abb81672369d', now(),
  'Sheets production SoT; registered during cutover-prep; NOT PG runtime',
  jsonb_build_object(
    'runtime', 'google_sheets',
    'prep_ts', '20260903T100627Z',
    'hash_kind', 'workflow_summary_fingerprint'
  )
FROM mars_core.apps a WHERE a.app_key='app_iseo_sales'
RETURNING id, status, n8n_workflow_id, release_version;

SELECT wr.release_version, wr.status, wr.n8n_workflow_id, left(wr.git_export_hash,12) AS hash12
FROM mars_core.workflow_releases wr
JOIN mars_core.apps a ON a.id = wr.app_id
WHERE a.app_key='app_iseo_sales' AND wr.workflow_family='operational_intake'
ORDER BY wr.created_at;
