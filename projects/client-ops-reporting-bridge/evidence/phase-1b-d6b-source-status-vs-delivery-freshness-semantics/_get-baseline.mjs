import {
  getWorkflow,
  loadCredentials,
  normalizeBaseUrl,
} from '../../../metabot-seo-content-agent/integrations/n8n-readonly-exporter/lib/n8n-api-client.mjs';
import {
  getDataTable,
  getDataTableRows,
  loadDataTableCredentials,
} from '../../n8n/runners/lib/client-ops-n8n-datatable-client.mjs';

const WORKFLOW_ID = 'tkM4H0G0gM3q9Foi';
const TABLE_ID = 'H6VYhwz7RXZCBMmu';
const HIST = 'c84e29bf-79b1-5aea-98c4-9dc8d651fc96';
const SYN = 'd6a2a001-27d6-4a2e-bd6a-000000000001';
const EXPECTED_VERSION = 'dc8746bf-df9c-425d-9b3f-4ace452ac5ef';

async function executionSnapshot(creds, workflowId) {
  const url = `${normalizeBaseUrl(creds.apiUrl)}/api/v1/executions?workflowId=${encodeURIComponent(workflowId)}&limit=100`;
  const response = await fetch(url, {
    method: 'GET',
    headers: { Accept: 'application/json', 'X-N8N-API-KEY': creds.apiKey },
  });
  if (!response.ok) {
    return { observable: false, reason: `HTTP_${response.status}`, count: null, running: null };
  }
  const data = await response.json();
  const rows = Array.isArray(data) ? data : data?.data;
  if (!Array.isArray(rows)) {
    return { observable: false, reason: 'unexpected_shape', count: null, running: null };
  }
  return {
    observable: true,
    count: typeof data?.count === 'number' ? data.count : rows.length,
    running: rows.filter((r) => r.status === 'running').length,
  };
}

function rowFields(row) {
  const d = row?.data || row || {};
  return {
    event_id: d.event_id ?? null,
    intake_state: d.intake_state ?? null,
    event_status: d.event_status ?? null,
    delivery_state: d.delivery_state ?? null,
  };
}

const creds = loadCredentials();
const dtCreds = loadDataTableCredentials();
const wf = await getWorkflow(WORKFLOW_ID, creds);
const nodes = Array.isArray(wf.nodes) ? wf.nodes : [];
const exec = await executionSnapshot(creds, WORKFLOW_ID);
const table = await getDataTable(dtCreds, TABLE_ID);
const tableData = table.data || table;
const columns = Array.isArray(tableData.columns) ? tableData.columns : [];
const all = await getDataTableRows(dtCreds, TABLE_ID, { limit: 50 });
const allRows = all.data?.data || all.data || [];
const byId = Object.fromEntries(
  (Array.isArray(allRows) ? allRows : []).map((r) => {
    const d = r?.data || r || {};
    return [d.event_id, rowFields(r)];
  }),
);

const out = {
  phase: '1B-D6B',
  method: 'GET_ONLY',
  workflow: {
    id: wf.id,
    name: wf.name,
    active: Boolean(wf.active),
    nodes: nodes.length,
    versionId: wf.versionId || null,
    version_match: (wf.versionId || null) === EXPECTED_VERSION,
  },
  executions: exec,
  datatable: {
    id: TABLE_ID,
    name: tableData.name || null,
    columns: columns.length,
    rows: Array.isArray(allRows) ? allRows.length : null,
  },
  historical: byId[HIST] || null,
  synthetic: byId[SYN] || null,
};

console.log(JSON.stringify(out, null, 2));
