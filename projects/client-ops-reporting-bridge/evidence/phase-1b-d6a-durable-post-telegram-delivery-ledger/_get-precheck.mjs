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

const WORKFLOW_ID = 'tkM4H0G0gM3q9Foi';
const TABLE_ID = 'H6VYhwz7RXZCBMmu';
const EVENT_ID = 'c84e29bf-79b1-5aea-98c4-9dc8d651fc96';
const EXPECTED_VERSION = '3d2fd6fc-bc17-4e0f-b9e5-086c959afd29';

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

const creds = loadCredentials();
const dtCreds = loadDataTableCredentials();
const wf = await getWorkflow(WORKFLOW_ID, creds);
const nodes = Array.isArray(wf.nodes) ? wf.nodes : [];
const exec = await executionSnapshot(creds, WORKFLOW_ID);
const table = await getDataTable(dtCreds, TABLE_ID);
const tableData = table.data || table;
const columns = Array.isArray(tableData.columns) ? tableData.columns : [];
const filtered = await getDataTableRows(dtCreds, TABLE_ID, {
  limit: 20,
  filter: { filters: [{ columnName: 'event_id', condition: 'eq', value: EVENT_ID }] },
});
const filterRows = filtered.data?.data || filtered.data || [];
const eventRow = Array.isArray(filterRows) && filterRows[0] ? filterRows[0] : null;
const rowData = eventRow?.data || eventRow || {};
const all = await getDataTableRows(dtCreds, TABLE_ID, { limit: 50 });
const allRows = all.data?.data || all.data || [];
const out = {
  phase: '1B-D6A',
  method: 'GET_ONLY',
  workflow: {
    id: wf.id,
    name: wf.name,
    active: Boolean(wf.active),
    nodes: nodes.length,
    versionId: wf.versionId || null,
    node_names: nodes.map((n) => n.name),
    dataTable_ops: nodes
      .filter((n) => n.type === 'n8n-nodes-base.dataTable')
      .map((n) => ({ name: n.name, operation: n.parameters?.operation })),
    telegram: (() => {
      const t = nodes.find((n) => n.name === 'Telegram Notify Accepted');
      return t
        ? {
            continueOnFail: Boolean(t.continueOnFail),
            onError: t.onError || null,
            typeVersion: t.typeVersion,
          }
        : null;
    })(),
  },
  executions: exec,
  datatable: {
    id: TABLE_ID,
    name: tableData.name || null,
    columns: columns.map((c) => ({ name: c.name || c.id, type: c.type })),
    column_count: columns.length,
    rows: Array.isArray(allRows) ? allRows.length : (tableData.rowsCount ?? null),
  },
  event: {
    event_id: EVENT_ID,
    rows: Array.isArray(filterRows) ? filterRows.length : null,
    intake_state: rowData.intake_state ?? null,
    event_status: rowData.event_status ?? null,
    delivery_state: rowData.delivery_state ?? null,
  },
};
const match =
  out.workflow.active === false &&
  out.workflow.nodes === 17 &&
  out.executions.observable &&
  out.executions.count === 32 &&
  out.executions.running === 0 &&
  out.workflow.versionId === EXPECTED_VERSION &&
  out.datatable.column_count === 15 &&
  out.datatable.rows === 3 &&
  out.event.rows === 1 &&
  out.event.intake_state === 'FIRST_SEEN' &&
  out.event.event_status === 'ATTENTION' &&
  out.event.delivery_state === 'PENDING';
out.verdict = match ? 'D6A_LIVE_BASELINE_RECONFIRMED' : 'D6A_LIVE_BASELINE_DRIFT';
process.stdout.write(`${JSON.stringify(out, null, 2)}\n`);
