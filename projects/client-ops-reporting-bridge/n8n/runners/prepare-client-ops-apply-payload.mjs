/**
 * Prepare local ignored apply payload for Client Ops inactive sandbox create.
 *
 * Does not edit the committed baseline template.
 * Auth mode for Phase 1B-B: AUTH_BLOCKED_INACTIVE_ONLY (placeholder retained).
 *
 * Output default:
 *   X:\AI MARS\local\client-ops-reporting-bridge\bzpm.ru\apply\mars-client-ops-bridge-bzpm.create-payload.json
 */

import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  AUTH_PLACEHOLDER,
  WORKFLOW_NAME,
} from '../harness/client-ops-validator.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(__dirname, '../../../..');
const TEMPLATE = resolve(
  __dirname,
  '../templates/mars-client-ops-bridge-bzpm-sandbox.template.json',
);
const DEFAULT_OUT = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/apply/mars-client-ops-bridge-bzpm.create-payload.json',
);

const AUTH_MODE = 'AUTH_BLOCKED_INACTIVE_ONLY';

function main() {
  const outArg = process.argv.find((a) => a.startsWith('--out='));
  const outPath = outArg ? resolve(outArg.slice('--out='.length)) : DEFAULT_OUT;

  const template = JSON.parse(readFileSync(TEMPLATE, 'utf8'));
  if (template.name !== WORKFLOW_NAME) {
    throw new Error(`Template name mismatch: ${template.name}`);
  }

  const payloadSource = structuredClone(template);
  delete payloadSource.id;
  delete payloadSource.versionId;
  delete payloadSource.tags;

  for (const node of payloadSource.nodes || []) {
    delete node.webhookId;
    delete node.credentials;
  }

  payloadSource.active = false;
  payloadSource.meta = {
    ...(payloadSource.meta || {}),
    mars_template: true,
    mars_status: 'APPLY_PAYLOAD_BLOCKED_INACTIVE',
    mars_auth_binding: AUTH_MODE,
    mars_auth_placeholder: AUTH_PLACEHOLDER,
    mars_dedupe: 'DEDUPE_DEFERRED_SANDBOX',
    mars_profile: 'PROFILE_B_REQUIRED',
    mars_site_id: 'SITE-002',
    mars_domain: 'bzpm.ru',
    mars_no_telegram: true,
    mars_no_manual_ui_assembly: true,
    mars_phase: '1B-B',
    templateCredsSetupCompleted: false,
  };

  const createPayload = {
    name: payloadSource.name,
    nodes: structuredClone(payloadSource.nodes),
    connections: structuredClone(payloadSource.connections),
    settings: {
      executionOrder: payloadSource.settings?.executionOrder || 'v1',
    },
  };

  mkdirSync(dirname(outPath), { recursive: true });
  writeFileSync(
    outPath,
    JSON.stringify(
      {
        auth_mode: AUTH_MODE,
        source_template: TEMPLATE,
        workflow_name: WORKFLOW_NAME,
        active: false,
        full_workflow_for_validation: payloadSource,
        create_payload: createPayload,
      },
      null,
      2,
    ),
    'utf8',
  );

  console.log(
    JSON.stringify(
      {
        ok: true,
        out: outPath,
        workflow_name: WORKFLOW_NAME,
        auth_mode: AUTH_MODE,
        active: false,
        node_count: createPayload.nodes.length,
        placeholder_retained: JSON.stringify(createPayload).includes(AUTH_PLACEHOLDER),
        credential_reference: false,
      },
      null,
      2,
    ),
  );
}

main();
