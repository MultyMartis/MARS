/**
 * Client Ops greenfield inactive sandbox create runner — SKELETON ONLY.
 *
 * THIS TASK MUST NOT EXECUTE APPLY.
 * Default mode: dry-run / design validation only.
 *
 * Future authorized charter may enable --apply with operator confirmation.
 * Do NOT use the GET-only n8n-readonly-exporter client for writes.
 */

import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { dirname, resolve, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { createInterface } from 'node:readline/promises';
import { stdin as input, stdout as output } from 'node:process';
import {
  AUTH_PLACEHOLDER,
  WORKFLOW_NAME,
} from '../harness/client-ops-validator.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const TEMPLATE = resolve(
  __dirname,
  '../templates/mars-client-ops-bridge-bzpm-sandbox.template.json',
);

const FORBIDDEN_TYPES = new Set([
  'n8n-nodes-base.telegram',
  'n8n-nodes-base.telegramTrigger',
]);

function loadTemplate() {
  return JSON.parse(readFileSync(TEMPLATE, 'utf8'));
}

function rejectPlaceholders(wf) {
  const blob = JSON.stringify(wf);
  if (blob.includes(AUTH_PLACEHOLDER) || blob.includes('HITL_REQUIRED')) {
    return {
      ok: false,
      code: 'AUTH_PLACEHOLDER_UNRESOLVED',
      message:
        'Auth secret placeholder still present. HITL must bind credential/env before apply.',
    };
  }
  return { ok: true };
}

function validateCreateCandidate(wf) {
  const errors = [];
  if (wf.name !== WORKFLOW_NAME) {
    errors.push(`workflow name must be exactly ${WORKFLOW_NAME}`);
  }
  if (wf.active !== false) errors.push('workflow must be inactive');
  if (wf.id) errors.push('template must not include workflow id');
  for (const node of wf.nodes || []) {
    if (node.webhookId) errors.push(`webhookId present on ${node.name}`);
    if (node.credentials) errors.push(`credentials present on ${node.name}`);
    if (FORBIDDEN_TYPES.has(node.type)) {
      errors.push(`forbidden node type ${node.type} on ${node.name}`);
    }
  }
  const ph = rejectPlaceholders(wf);
  if (!ph.ok) errors.push(ph.message);
  return errors;
}

function prepareCreatePayload(wf) {
  const nodes = structuredClone(wf.nodes || []);
  for (const node of nodes) {
    delete node.webhookId;
    delete node.credentials;
  }
  return {
    name: wf.name,
    nodes,
    connections: structuredClone(wf.connections || {}),
    settings: { executionOrder: wf.settings?.executionOrder || 'v1' },
  };
}

async function main() {
  const args = new Set(process.argv.slice(2));
  const apply = args.has('--apply');
  const wf = loadTemplate();
  const errors = validateCreateCandidate(wf);
  const payload = errors.length ? null : prepareCreatePayload(wf);

  const report = {
    runner: 'client-ops-greenfield-create-skeleton',
    mode: apply ? 'APPLY_REQUESTED' : 'DRY_RUN',
    template: TEMPLATE,
    workflow_name: wf.name,
    active: wf.active,
    validation_errors: errors,
    create_payload_prepared: Boolean(payload),
    network: false,
    executed_create: false,
    activated: false,
    note: 'Skeleton only. Write-capable client + HITL confirmation required for future apply.',
  };

  if (errors.length) {
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 2;
    return;
  }

  if (!apply) {
    console.log(JSON.stringify(report, null, 2));
    return;
  }

  // Apply path is intentionally incomplete in this charter.
  const rl = createInterface({ input, output });
  const confirmation = await rl.question(
    'Type CREATE-INACTIVE-CLIENT-OPS-SANDBOX to continue (will still abort in this skeleton): ',
  );
  rl.close();

  if (confirmation.trim() !== 'CREATE-INACTIVE-CLIENT-OPS-SANDBOX') {
    report.aborted = 'confirmation_mismatch';
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 3;
    return;
  }

  report.aborted = 'APPLY_NOT_IMPLEMENTED_IN_THIS_TASK';
  report.message =
    'Write-capable n8n client not invoked. Next charter must implement POST /api/v1/workflows via a separate write client, re-GET, sanitize evidence, and never activate.';
  console.log(JSON.stringify(report, null, 2));
  process.exitCode = 4;
}

main().catch((err) => {
  console.error(err instanceof Error ? err.message : String(err));
  process.exitCode = 1;
});
