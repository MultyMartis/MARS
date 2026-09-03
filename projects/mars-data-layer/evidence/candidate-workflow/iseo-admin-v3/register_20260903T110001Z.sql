
DELETE FROM mars_core.workflow_releases wr
USING mars_core.apps a
WHERE wr.app_id = a.id AND a.app_key='app_iseo_sales'
  AND wr.workflow_family='admin_runtime'
  AND wr.release_version IN ('Admin.v3.dev', 'Admin.dev');

INSERT INTO mars_core.workflow_releases (
  app_id, workflow_family, n8n_workflow_id, release_version,
  data_contract_version, status, git_export_hash, notes, metadata
)
SELECT a.id, 'admin_runtime', 'wLrLp4WQHm1VJmxz', 'Admin.dev',
  'iseo-sales-v1', 'active', NULL,
  'Production Sheets Admin.dev — remains active until joint PG cutover',
  jsonb_build_object('sheets_sot', true)
FROM mars_core.apps a WHERE a.app_key='app_iseo_sales';

INSERT INTO mars_core.workflow_releases (
  app_id, workflow_family, n8n_workflow_id, release_version,
  data_contract_version, status, git_export_hash, notes, metadata
)
SELECT a.id, 'admin_runtime', 'Zk9b1BiXpYN9rMMo', 'Admin.v3.dev',
  'iseo-sales-v1', 'candidate', '6c8526b255d41cd302d09dcc04450fa8cdf61047ea1898accbb565440cc5dfb1',
  'PG Admin candidate inactive; Manual inject only; zero Sheets writes',
  jsonb_build_object(
    'migration', '0006_admin_v3_runtime_functions',
    'credential_name', 'ISEO Runtime PG (v3)',
    'credential_id', 'XCmmOgzZ1RWT4Fg3',
    'role', 'iseo_runtime',
    'telegram_trigger', false
  )
FROM mars_core.apps a WHERE a.app_key='app_iseo_sales'
RETURNING id, status, n8n_workflow_id, release_version;
