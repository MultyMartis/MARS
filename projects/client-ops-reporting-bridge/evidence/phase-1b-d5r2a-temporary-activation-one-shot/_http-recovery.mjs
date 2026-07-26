import { writeFileSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  getWorkflow,
  loadCredentials,
  normalizeBaseUrl,
} from '../../../metabot-seo-content-agent/integrations/n8n-readonly-exporter/lib/n8n-api-client.mjs';
import {
  getDataTableRows,
  loadDataTableCredentials,
} from '../../n8n/runners/lib/client-ops-n8n-datatable-client.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const EVIDENCE = __dirname;
const WORKFLOW_ID = 'tkM4H0G0gM3q9Foi';
const TABLE_ID = 'H6VYhwz7RXZCBMmu';
const EVENT_ID = 'c84e29bf-79b1-5aea-98c4-9dc8d651fc96';
const EXEC_ID = '3416';

const creds = loadCredentials();
const dtCreds = loadDataTableCredentials();
const wf = await getWorkflow(WORKFLOW_ID, creds);
const url = `${normalizeBaseUrl(creds.apiUrl)}/api/v1/executions/${EXEC_ID}?includeData=true`;
const response = await fetch(url, {
  method: 'GET',
  headers: { Accept: 'application/json', 'X-N8N-API-KEY': creds.apiKey },
});
const data = await response.json();
const runData = data?.data?.resultData?.runData || {};
const nodeNames = Object.keys(runData);
const summarizeNode = (name) => {
  const runs = runData[name];
  if (!Array.isArray(runs) || !runs[0]) return { present: false };
  return {
    present: true,
    has_error: Boolean(runs[0].error),
    execution_status: runs[0].executionStatus || null,
  };
};
const respondKeys = nodeNames.filter((n) => /respond|accepted|webhook/i.test(n));
const telegramKeys = nodeNames.filter((n) => /telegram/i.test(n));
const claimKeys = nodeNames.filter((n) => /claim|dedupe|insert/i.test(n));

const filtered = await getDataTableRows(dtCreds, TABLE_ID, {
  limit: 5,
  filter: { filters: [{ columnName: 'event_id', condition: 'eq', value: EVENT_ID }] },
});
const rows = filtered.data?.data || filtered.data || [];
const row = Array.isArray(rows) && rows[0] ? rows[0] : null;
const rowSanitized = row
  ? {
      event_id: row.event_id || row.data?.event_id || null,
      event_status: row.event_status || row.data?.event_status || null,
      intake_state: row.intake_state || row.data?.intake_state || null,
      delivery_state: row.delivery_state || row.data?.delivery_state || null,
      site_id: row.site_id || row.data?.site_id || null,
      keys: Object.keys(row.data || row).slice(0, 20),
    }
  : null;

const out = {
  method: 'GET_ONLY_POST_HTTP_RECOVERY',
  workflow_final_active: Boolean(wf.active),
  workflow_nodes: (wf.nodes || []).length,
  workflow_versionId: wf.versionId,
  execution: {
    id: EXEC_ID,
    status: data.status,
    finished: data.finished,
    mode: data.mode,
    startedAt: data.startedAt,
    stoppedAt: data.stoppedAt,
  },
  nodes_executed: nodeNames,
  respond_nodes: Object.fromEntries(respondKeys.map((k) => [k, summarizeNode(k)])),
  telegram_nodes: Object.fromEntries(telegramKeys.map((k) => [k, summarizeNode(k)])),
  claim_nodes: Object.fromEntries(claimKeys.map((k) => [k, summarizeNode(k)])),
  datatable_event_row_sanitized: rowSanitized,
  note: 'Producer stdout parse failed in orchestrator; HTTP status recovered via GET-only n8n evidence. Respond Accepted implies intake 202 for this workflow pattern when execution success + FIRST_SEEN row.',
};
writeFileSync(resolve(EVIDENCE, 'HTTP-RECOVERY-GETONLY.json'), JSON.stringify(out, null, 2) + '\n');
process.stdout.write(JSON.stringify(out, null, 2) + '\n');
