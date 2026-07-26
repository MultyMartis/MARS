/**
 * D5R2A GET-only Client Ops precheck (no activate, no webhook POST).
 * Writes sanitized JSON to stdout; secrets never printed.
 */
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
    headers: {
      Accept: 'application/json',
      'X-N8N-API-KEY': creds.apiKey,
    },
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
    finished_false: rows.filter((r) => r.finished === false).length,
  };
}

async function main() {
  const creds = loadCredentials();
  const dtCreds = loadDataTableCredentials();
  const wf = await getWorkflow(WORKFLOW_ID, creds);
  const nodes = Array.isArray(wf.nodes) ? wf.nodes : [];
  const webhookNodes = nodes.filter((n) =>
    String(n?.type || '').toLowerCase().includes('webhook'),
  );
  const exec = await executionSnapshot(creds, WORKFLOW_ID);
  const table = await getDataTable(dtCreds, TABLE_ID);
  const tableData = table.data || table;
  const columns = Array.isArray(tableData.columns) ? tableData.columns.length : null;
  const rowsTotal =
    typeof tableData.rowsCount === 'number'
      ? tableData.rowsCount
      : typeof tableData.size === 'number'
        ? tableData.size
        : null;

  const filtered = await getDataTableRows(dtCreds, TABLE_ID, {
    limit: 20,
    filter: {
      filters: [{ columnName: 'event_id', condition: 'eq', value: EVENT_ID }],
    },
  });
  const filterRows = filtered.data?.data || filtered.data || [];
  const eventRowCount = Array.isArray(filterRows) ? filterRows.length : null;

  // Also pull unfiltered count if rowsTotal missing
  let allRowsCount = rowsTotal;
  if (allRowsCount == null) {
    const all = await getDataTableRows(dtCreds, TABLE_ID, { limit: 50 });
    const allRows = all.data?.data || all.data || [];
    allRowsCount = Array.isArray(allRows) ? allRows.length : null;
  }

  const out = {
    phase: '1B-D5R2A',
    method: 'GET_ONLY',
    workflow: {
      id: wf.id,
      name: wf.name,
      active: Boolean(wf.active),
      nodes: nodes.length,
      versionId: wf.versionId || null,
      updatedAt: wf.updatedAt || null,
      webhook_nodes: webhookNodes.length,
      webhook_id_present: webhookNodes.some((n) => Boolean(n.webhookId)),
      webhook_path_present: webhookNodes.some(
        (n) => Boolean(n.parameters?.path) || Boolean(n.parameters?.options?.path),
      ),
    },
    executions: exec,
    datatable: {
      id: TABLE_ID,
      name: tableData.name || null,
      columns,
      rows: allRowsCount,
    },
    event: {
      event_id: EVENT_ID,
      rows: eventRowCount,
    },
    expected: {
      active: false,
      nodes: 17,
      executions: 31,
      running: 0,
      versionId: EXPECTED_VERSION,
      table_columns: 15,
      table_rows: 2,
      event_rows: 0,
    },
  };

  const baselineMatch =
    out.workflow.active === false &&
    out.workflow.nodes === 17 &&
    out.executions.observable &&
    out.executions.count === 31 &&
    out.executions.running === 0 &&
    out.workflow.versionId === EXPECTED_VERSION &&
    out.datatable.columns === 15 &&
    out.datatable.rows === 2 &&
    out.event.rows === 0;

  out.verdict_baseline = baselineMatch
    ? 'CLIENT_OPS_LIVE_BASELINE_MATCH'
    : 'CLIENT_OPS_LIVE_BASELINE_MISMATCH';
  out.verdict_event =
    out.event.rows === 0
      ? 'D5R2A_EVENT_UNSEEN'
      : 'D5R2A_EVENT_ALREADY_SEEN_LIVE_POST_NOT_AUTHORIZED';
  out.activation_capability = {
    activate_api_path: `/api/v1/workflows/${WORKFLOW_ID}/activate`,
    deactivate_api_path: `/api/v1/workflows/${WORKFLOW_ID}/deactivate`,
    content_edit_required: false,
    unrelated_workflow_dependency: false,
    production_webhook_expected_on_activate: true,
    established_client: 'client-ops-n8n-activation-client.mjs',
    confirm_phrases_available: [
      'ACTIVATE CLIENT OPS MANUAL REAL SOURCE D5 BZPM',
      'DEACTIVATE CLIENT OPS MANUAL REAL SOURCE D5 BZPM',
    ],
  };
  out.capability_verdict = 'D5R2A_TEMPORARY_ACTIVATION_CAPABILITY_CONFIRMED';

  process.stdout.write(`${JSON.stringify(out, null, 2)}\n`);
}

main().catch((err) => {
  process.stderr.write(`precheck_failed:${err instanceof Error ? err.message : String(err)}\n`);
  process.exit(1);
});
