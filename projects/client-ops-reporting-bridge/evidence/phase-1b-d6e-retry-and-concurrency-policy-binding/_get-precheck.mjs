import { writeFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
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

const __dirname = dirname(fileURLToPath(import.meta.url));
const WORKFLOW_ID = 'tkM4H0G0gM3q9Foi';
const TABLE_ID = 'H6VYhwz7RXZCBMmu';
const HIST_EVENT = 'c84e29bf-79b1-5aea-98c4-9dc8d651fc96';
const D6A2_EVENT = 'd6a2a001-27d6-4a2e-bd6a-000000000001';
const EXPECTED_VERSION = 'dc8746bf-df9c-425d-9b3f-4ace452ac5ef';

async function executionSnapshot(creds, workflowId) {
  const url = `${normalizeBaseUrl(creds.apiUrl)}/api/v1/executions?workflowId=${encodeURIComponent(workflowId)}&limit=100`;
  const response = await fetch(url, {
    method: 'GET',
    headers: { Accept: 'application/json', 'X-N8N-API-KEY': creds.apiKey },
  });
  if (!response.ok) return { observable: false, reason: `HTTP_${response.status}`, count: null, running: null };
  const data = await response.json();
  const rows = Array.isArray(data) ? data : data?.data;
  if (!Array.isArray(rows)) return { observable: false, reason: 'unexpected_shape', count: null, running: null };
  return {
    observable: true,
    count: typeof data?.count === 'number' ? data.count : rows.length,
    running: rows.filter((r) => r.status === 'running').length,
  };
}

async function eventSnap(dtCreds, eventId) {
  const filtered = await getDataTableRows(dtCreds, TABLE_ID, {
    limit: 20,
    filter: { filters: [{ columnName: 'event_id', condition: 'eq', value: eventId }] },
  });
  const filterRows = filtered.data?.data || filtered.data || [];
  const eventRow = Array.isArray(filterRows) && filterRows[0] ? filterRows[0] : null;
  const rowData = eventRow?.data || eventRow || {};
  return {
    event_id: eventId,
    rows: Array.isArray(filterRows) ? filterRows.length : null,
    intake_state: rowData.intake_state ?? null,
    event_status: rowData.event_status ?? null,
    delivery_state: rowData.delivery_state ?? null,
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
const historical = await eventSnap(dtCreds, HIST_EVENT);
const d6a2 = await eventSnap(dtCreds, D6A2_EVENT);
const out = {
  phase: '1B-D6E',
  method: 'GET_ONLY',
  live_apply_performed: false,
  workflow: {
    id: wf.id,
    name: wf.name,
    active: Boolean(wf.active),
    nodes: nodes.length,
    versionId: wf.versionId || null,
  },
  executions: exec,
  datatable: {
    id: TABLE_ID,
    column_count: columns.length,
    rows: Array.isArray(allRows) ? allRows.length : (tableData.rowsCount ?? null),
  },
  historical,
  d6a2_synthetic: d6a2,
};
const match =
  out.workflow.active === false &&
  out.workflow.nodes === 20 &&
  out.executions.observable &&
  out.executions.count === 34 &&
  out.executions.running === 0 &&
  out.workflow.versionId === EXPECTED_VERSION &&
  out.datatable.column_count === 15 &&
  out.datatable.rows === 4 &&
  out.historical.rows === 1 &&
  out.historical.intake_state === 'FIRST_SEEN' &&
  out.historical.event_status === 'ATTENTION' &&
  out.historical.delivery_state === 'PENDING' &&
  out.d6a2_synthetic.rows === 1 &&
  out.d6a2_synthetic.intake_state === 'FIRST_SEEN' &&
  out.d6a2_synthetic.event_status === 'OK' &&
  out.d6a2_synthetic.delivery_state === 'SENT';
out.verdict = match ? 'D6E_LIVE_BASELINE_RECONFIRMED' : 'D6E_LIVE_BASELINE_DRIFT';
writeFileSync(resolve(__dirname, '_live-baseline-raw.json'), `${JSON.stringify(out, null, 2)}\n`, 'utf8');
process.stdout.write(`${JSON.stringify(out, null, 2)}\n`);
