
DELETE FROM mars_core.workflow_releases wr
USING mars_core.apps a
WHERE wr.app_id = a.id
  AND a.app_key = 'app_iseo_sales'
  AND wr.workflow_family = 'admin_runtime'
  AND wr.release_version = 'Admin.v3.rollback';

INSERT INTO mars_core.workflow_releases (
  app_id, workflow_family, n8n_workflow_id, release_version,
  data_contract_version, status, git_export_hash, notes, metadata
)
SELECT a.id, 'admin_runtime', '8uStgSN9brsxmz6g', 'Admin.v3.rollback',
  'iseo-sales-v1', 'rollback', '1e19672ac9a9ef79783a475e8950d33c007aba1237a58c0fd29434c6eb037f6a',
  'PG-compatible Admin rollback pin; inactive; never reactivate Sheets Admin.dev after PG_PRIMARY',
  jsonb_build_object(
    'pinned_from', 'Admin.v3.dev',
    'pinned_from_id', 'Zk9b1BiXpYN9rMMo',
    'credential_id', 'XCmmOgzZ1RWT4Fg3',
    'credential_name', 'ISEO Runtime PG (v3)',
    'role', 'iseo_runtime',
    'pin_ts', '20260903T110201Z',
    'pre_id_hash', 'd6373171a1f71fc7eb8810310dcf28d4384e04975c20eb054cc01fd101ae3de7'
  )
FROM mars_core.apps a WHERE a.app_key='app_iseo_sales'
RETURNING id, status, n8n_workflow_id, release_version;

SELECT wr.release_version, wr.status, wr.n8n_workflow_id, left(wr.git_export_hash,12) AS hash12
FROM mars_core.workflow_releases wr
JOIN mars_core.apps a ON a.id = wr.app_id
WHERE a.app_key='app_iseo_sales' AND wr.workflow_family='admin_runtime'
ORDER BY wr.created_at;
