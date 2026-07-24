/**
 * Phase 1B-D1 — GET-only Data Table + live workflow capability discovery.
 * No mutations. No secrets printed. Safe to import (no live action on import).
 *
 * Usage:
 *   node discover-client-ops-datatable-capability-d1.mjs
 */

import { createHash } from 'node:crypto';
import { mkdirSync, writeFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  getWorkflow,
  listWorkflows,
  loadCredentials,
  n8nGet,
  normalizeBaseUrl,
} from '../../../metabot-seo-content-agent/integrations/n8n-readonly-exporter/lib/n8n-api-client.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(__dirname, '../../../..');
const WF_ID = 'tkM4H0G0gM3q9Foi';
const WF_NAME = 'MARS Client Ops Bridge — bzpm.ru';
const TABLE_NAME = 'MARS Client Ops Dedupe — bzpm.ru';
const TEMP_NAME = 'MARS Client Ops Telegram Semantics Probe — TEMP';
const LOCAL_OUT = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/evidence/phase-1b-d1/discovery-raw-sanitized.json',
);

function ensureDir(p) {
  mkdirSync(dirname(p), { recursive: true });
}

function redactLongTokens(text) {
  return String(text || '').replace(/[A-Za-z0-9_\-]{40,}/g, '[REDACTED_LONG]');
}

async function fetchOpenApi(creds) {
  const url = `${normalizeBaseUrl(creds.apiUrl)}/api/v1/openapi.yml`;
  const response = await fetch(url, {
    headers: {
      Accept: 'application/yaml, text/yaml, application/json, */*',
      'X-N8N-API-KEY': creds.apiKey,
    },
  });
  const text = await response.text();
  return { status: response.status, text };
}

function extractDataTablePaths(openapiText) {
  const matches = openapiText.match(/\/api\/v1\/data-tables[^\s"'`]*/g) || [];
  return [...new Set(matches)].sort();
}

function extractPathOperations(openapiText, pathPrefix) {
  const lines = openapiText.split(/\r?\n/);
  const ops = [];
  let currentPath = null;
  for (let i = 0; i < lines.length; i += 1) {
    const line = lines[i];
    const pathMatch = line.match(/^\s{2}(\/api\/v1\/data-tables[^:]*):/);
    if (pathMatch) {
      currentPath = pathMatch[1];
      continue;
    }
    if (!currentPath || !currentPath.startsWith(pathPrefix)) continue;
    const methodMatch = line.match(/^\s{4}(get|post|put|patch|delete):/i);
    if (methodMatch) {
      ops.push({ path: currentPath, method: methodMatch[1].toUpperCase() });
    }
  }
  return ops;
}

function summarizeWorkflow(wf) {
  const nodes = wf.nodes || [];
  const connections = wf.connections || {};
  const respondAccepted = connections['Respond Accepted']?.main?.[0] || [];
  const respondRejected = connections['Respond Rejected']?.main?.[0] || [];
  const webhook = nodes.find((n) => n.name === 'Webhook Intake');
  const telegram = nodes.find((n) => n.name === 'Telegram Notify Accepted');
  const fingerprint = nodes
    .map((n) => `${n.name}|${n.type}|${n.typeVersion}`)
    .join('||');
  return {
    id: wf.id,
    name: wf.name,
    active: wf.active,
    nodes: nodes.length,
    node_names: nodes.map((n) => n.name),
    node_types: nodes.map((n) => ({
      name: n.name,
      type: n.type,
      typeVersion: n.typeVersion,
    })),
    versionId: wf.versionId,
    connection_keys: Object.keys(connections).sort(),
    fingerprint_sha16: createHash('sha256').update(fingerprint).digest('hex').slice(0, 16),
    webhook: webhook
      ? {
          authentication: webhook.parameters?.authentication || null,
          credential_id: webhook.credentials?.httpHeaderAuth?.id || null,
          credential_name: webhook.credentials?.httpHeaderAuth?.name || null,
        }
      : null,
    telegram: telegram
      ? {
          credential_id: telegram.credentials?.telegramApi?.id || null,
          credential_name: telegram.credentials?.telegramApi?.name || null,
          chat_id: telegram.parameters?.chatId ?? null,
          type: telegram.type,
          typeVersion: telegram.typeVersion,
        }
      : null,
    pattern_b: {
      respond_accepted_targets: respondAccepted.map((c) => c.node),
      confirmed: respondAccepted.some((c) => c.node === 'Telegram Notify Accepted'),
    },
    rejected_reaches_telegram: respondRejected.some(
      (c) => c.node === 'Telegram Notify Accepted',
    ),
    data_table_nodes: nodes.filter((n) =>
      String(n.type || '').toLowerCase().includes('datatable'),
    ).length,
    data_store_nodes: nodes.filter((n) =>
      String(n.type || '').toLowerCase().includes('datastore'),
    ).length,
    http_request_nodes: nodes.filter((n) => n.type === 'n8n-nodes-base.httpRequest')
      .length,
    schedule_nodes: nodes.filter((n) =>
      String(n.type || '').toLowerCase().includes('schedule'),
    ).length,
  };
}

async function main() {
  const creds = loadCredentials();
  const out = {
    phase: '1B-D1',
    mode: 'GET_ONLY_DISCOVERY',
    timestamp_utc: new Date().toISOString(),
  };

  const all = await listWorkflows(creds);
  const list = all.data || all || [];
  out.workflow_exact_name_count = list.filter((w) => w.name === WF_NAME).length;
  out.temp_exact_name_count = list.filter((w) => w.name === TEMP_NAME).length;

  const wf = await getWorkflow(WF_ID, creds);
  out.workflow = summarizeWorkflow(wf);

  try {
    const execs = await n8nGet(
      `/api/v1/executions?workflowId=${WF_ID}&limit=1`,
      creds,
    );
    out.executions = execs?.count ?? null;
  } catch (err) {
    out.executions = null;
    out.executions_error = String(err instanceof Error ? err.message : err).slice(0, 200);
  }

  try {
    const running = await n8nGet(
      `/api/v1/executions?workflowId=${WF_ID}&status=running&limit=1`,
      creds,
    );
    out.running = running?.count ?? 0;
  } catch {
    out.running = null;
  }

  const openapi = await fetchOpenApi(creds);
  out.openapi_status = openapi.status;
  out.openapi_bytes = openapi.text.length;
  out.data_table_paths = extractDataTablePaths(openapi.text);
  out.data_table_operations = extractPathOperations(openapi.text, '/api/v1/data-tables');
  out.legacy_data_store_in_openapi = /data-store|dataStore/i.test(openapi.text);
  out.static_data_mentioned = /staticData|static.?data/i.test(openapi.text);
  const idx = openapi.text.indexOf('/api/v1/data-tables');
  out.openapi_datatable_excerpt = idx >= 0
    ? redactLongTokens(openapi.text.slice(Math.max(0, idx - 120), idx + 3500))
    : null;

  try {
    const tables = await n8nGet('/api/v1/data-tables', creds);
    const rows = tables.data || tables || [];
    out.data_tables = {
      ok: true,
      response_keys: tables && typeof tables === 'object' ? Object.keys(tables) : [],
      count: Array.isArray(rows) ? rows.length : null,
      exact_dedupe_name_count: Array.isArray(rows)
        ? rows.filter((t) => t.name === TABLE_NAME).length
        : null,
      inventory: Array.isArray(rows)
        ? rows.map((t) => ({
            id: t.id,
            name: t.name,
            column_count: Array.isArray(t.columns) ? t.columns.length : null,
            column_names: Array.isArray(t.columns)
              ? t.columns.map((c) => c.name || c.id || c)
              : null,
          }))
        : null,
    };
  } catch (err) {
    out.data_tables = {
      ok: false,
      error: String(err instanceof Error ? err.message : err).slice(0, 300),
    };
  }

  for (const path of [
    '/types/nodes.json',
    '/rest/node-types',
    '/api/v1/node-types',
  ]) {
    try {
      const data = await n8nGet(path, creds);
      const blob = JSON.stringify(data);
      const hits = [];
      for (const needle of [
        'dataTable',
        'DataTable',
        'n8n-nodes-base.dataTable',
        '@n8n/n8n-nodes-langchain',
      ]) {
        if (blob.includes(needle)) hits.push(needle);
      }
      out[`node_types_probe_${path.replace(/\W+/g, '_')}`] = {
        ok: true,
        hit_needles: hits,
        top_keys:
          data && typeof data === 'object' ? Object.keys(data).slice(0, 30) : typeof data,
      };
    } catch (err) {
      out[`node_types_probe_${path.replace(/\W+/g, '_')}`] = {
        ok: false,
        error: String(err instanceof Error ? err.message : err).slice(0, 200),
      };
    }
  }

  // OpenAPI schema property probes for upsert uniqueness
  const upsertIdx = openapi.text.indexOf('/rows/upsert');
  out.upsert_schema_excerpt = upsertIdx >= 0
    ? redactLongTokens(openapi.text.slice(upsertIdx, upsertIdx + 2200))
    : null;
  const createIdx = openapi.text.indexOf('/api/v1/data-tables:');
  out.create_table_schema_excerpt = createIdx >= 0
    ? redactLongTokens(openapi.text.slice(createIdx, createIdx + 2500))
    : null;

  ensureDir(LOCAL_OUT);
  writeFileSync(LOCAL_OUT, `${JSON.stringify(out, null, 2)}\n`, 'utf8');
  console.log(JSON.stringify(out, null, 2));
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  main().catch((err) => {
    console.error(String(err instanceof Error ? err.message : err));
    process.exitCode = 1;
  });
}
