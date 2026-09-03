
DELETE FROM mars_core.workflow_releases wr
USING mars_core.apps a
WHERE wr.app_id = a.id
  AND a.app_key = 'app_iseo_sales'
  AND wr.workflow_family = 'operational_intake'
  AND wr.release_version = 'Operational.v3.rollback';

INSERT INTO mars_core.workflow_releases (
  app_id, workflow_family, n8n_workflow_id, release_version,
  data_contract_version, status, git_export_hash, notes, metadata
)
SELECT a.id, 'operational_intake', 'favawMOzVwtFMdyH', 'Operational.v3.rollback',
  'iseo-sales-v1', 'rollback', 'ac28d8e5268a57390713397e7cc960e5f9742fd75a130b44381bcd632c61607d',
  'PG-compatible rollback pin; inactive; same contract as v3 candidate',
  jsonb_build_object(
    'pinned_from', 'Operational.v3.dev',
    'pinned_from_id', 'NH4uV145Amrgnmkm',
    'credential_id', 'XCmmOgzZ1RWT4Fg3',
    'credential_name', 'ISEO Runtime PG (v3)',
    'role', 'iseo_runtime',
    'pin_ts', '20260903T100308Z'
  )
FROM mars_core.apps a WHERE a.app_key='app_iseo_sales'
RETURNING id, status, n8n_workflow_id, release_version;

SELECT release_version, status, n8n_workflow_id, left(git_export_hash,12) AS hash12
FROM mars_core.workflow_releases wr
JOIN mars_core.apps a ON a.id = wr.app_id
WHERE a.app_key='app_iseo_sales' AND wr.workflow_family='operational_intake'
ORDER BY wr.created_at;
