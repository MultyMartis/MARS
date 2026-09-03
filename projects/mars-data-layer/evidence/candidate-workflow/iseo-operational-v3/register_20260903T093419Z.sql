
INSERT INTO mars_core.workflow_releases (
  app_id, workflow_family, n8n_workflow_id, release_version,
  data_contract_version, status, git_export_hash, notes, metadata
)
SELECT a.id, 'operational_intake', 'NH4uV145Amrgnmkm', 'Operational.v3.dev',
  'iseo-sales-v1', 'candidate', 'dcd9ddd595102aa8ec1e804ef08ea6efc6ef7d1bf21d37626c0eb3b4ad9b0601',
  'PG candidate inactive build; Sheets Operational.dev remains active',
  jsonb_build_object(
    'migration', '0005_v3_runtime_functions',
    'credential_name', 'ISEO Runtime PG (v3)',
    'credential_id', 'XCmmOgzZ1RWT4Fg3',
    'role', 'iseo_runtime'
  )
FROM mars_core.apps a WHERE a.app_key='app_iseo_sales'
RETURNING id, status, n8n_workflow_id;
