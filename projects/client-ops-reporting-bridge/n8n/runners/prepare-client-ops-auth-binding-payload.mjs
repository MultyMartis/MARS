/**
 * Prepare local ignored PUT payload for Phase 1B-B1 native Header Auth binding.
 *
 * Reads live workflow via GET-only client, applies authentication-only delta,
 * writes proposed PUT payload under gitignored local/.
 *
 * Does not call PUT. Does not create credentials. Does not print secrets.
 *
 * Usage:
 *   node prepare-client-ops-auth-binding-payload.mjs --credential-id=<id>
 */

import { mkdirSync, writeFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  getWorkflow,
  loadCredentials,
} from '../../../metabot-seo-content-agent/integrations/n8n-readonly-exporter/lib/n8n-api-client.mjs';
import {
  ALLOWED_WORKFLOW_ID,
  ALLOWED_WORKFLOW_NAME,
  prepareWorkflowPutPayload,
} from './lib/client-ops-n8n-workflow-update-client.mjs';
import { AUTH_PLACEHOLDER } from '../harness/client-ops-validator.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(__dirname, '../../../..');
const EXPECTED_HOST = 'n8n.ai-metacode.com';
const CREDENTIAL_NAME = 'MARS Client Ops Webhook Auth — bzpm.ru';
const CREDENTIAL_TYPE = 'httpHeaderAuth';
const AUTH_MODE = 'AUTH_NATIVE_HEADER_CREDENTIAL_BOUND';
const HEADER_NAME = 'X-MARS-Client-Ops-Token';
const DEFAULT_OUT = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/apply/mars-client-ops-bridge-bzpm.auth-binding.put-payload.json',
);

function parseArgs(argv) {
  const args = { credentialId: null, out: DEFAULT_OUT };
  for (const a of argv) {
    if (a.startsWith('--credential-id=')) args.credentialId = a.slice('--credential-id='.length);
    else if (a.startsWith('--out=')) args.out = resolve(a.slice('--out='.length));
  }
  return args;
}

/**
 * Patch Process Client Ops Gates jsCode for native header auth.
 * @param {string} jsCode
 */
export function patchProcessGatesCode(jsCode) {
  let code = String(jsCode).replace(/\r\n/g, '\n');

  // 1) Replace invocation tail
  const invStart = code.lastIndexOf(
    'const item = $input.first().json || {};\nconst expectedSecret =',
  );
  if (invStart === -1) {
    throw new Error('Unable to locate Process Gates invocation tail.');
  }
  const invEnd = code.indexOf('});', invStart);
  if (invEnd === -1) {
    throw new Error('Unable to locate invocation closing.');
  }
  const afterInv = invEnd + 3;
  const newInvocation = `const item = $input.first().json || {};
// Native Webhook Header Auth rejects unauthorized requests before execution.
// Code-level shared-secret comparison removed; auth_mode=NATIVE_HEADER_AUTH.
const result = processClientOpsRequest({
  headers: item.headers || {},
  body: item.body,
  rawBodyBytes: item.rawBodyBytes || 0,
  authMode: 'NATIVE_HEADER_AUTH',
});`;
  code = `${code.slice(0, invStart)}${newInvocation}${code.slice(afterInv)}`;

  // 2) Replace auth gate inside processClientOpsRequest
  const expectedAssign = code.indexOf('const expectedSecret =');
  const bodyAssign = code.indexOf('const body = input.body;');
  if (expectedAssign === -1 || bodyAssign === -1 || bodyAssign < expectedAssign) {
    throw new Error('Unable to locate processClientOpsRequest auth region.');
  }

  const authReplacement = `if (input.authMode !== 'NATIVE_HEADER_AUTH') {
      const expectedSecret =
        input.expectedSecret === undefined
          ? SYNTHETIC_HARNESS_SECRET
          : input.expectedSecret;
      const auth = validateAuthInterface(headers, expectedSecret);
      if (!auth.ok) {
        const code = auth.code === 'AUTH_BINDING_UNRESOLVED' ? 'UNAUTHORIZED' : auth.code;
        return {
          http_status: httpStatusFor('REJECTED', code),
          response: buildRejectedResponse(code),
          evidence: {
            gate: 'auth',
            code: auth.code,
            note:
              auth.code === 'AUTH_BINDING_UNRESOLVED'
                ? 'HITL_REQUIRED_AUTH_BINDING'
                : undefined,
          },
        };
      }
    }
    // else: auth_mode=NATIVE_HEADER_AUTH — native Webhook Header Auth already enforced.

    `;

  // Keep content-type + size gates that sit between expectedSecret assign and auth call.
  const ctStart = code.indexOf('const ct = validateContentType(headers);', expectedAssign);
  if (ctStart === -1 || ctStart > bodyAssign) {
    throw new Error('Unable to locate content-type gate inside auth region.');
  }
  const authCall = code.indexOf(
    'const auth = validateAuthInterface(headers, expectedSecret);',
    ctStart,
  );
  if (authCall === -1 || authCall > bodyAssign) {
    throw new Error('Unable to locate validateAuthInterface call.');
  }

  code = `${code.slice(0, expectedAssign)}${code.slice(ctStart, authCall)}${authReplacement}${code.slice(bodyAssign)}`;

  // 3) Retire AUTH_PLACEHOLDER constant value
  code = code.replace(
    /const AUTH_PLACEHOLDER = '[^']*';/,
    "const AUTH_PLACEHOLDER = ''; // retired under NATIVE_HEADER_AUTH",
  );
  code = code.split(AUTH_PLACEHOLDER).join('');

  if (!code.startsWith('// auth_mode=NATIVE_HEADER_AUTH')) {
    code = `// auth_mode=NATIVE_HEADER_AUTH\n${code}`;
  }

  if (
    code.includes(AUTH_PLACEHOLDER) ||
    code.includes('HITL_REQUIRED:CLIENT_OPS_WEBHOOK_AUTH_SECRET')
  ) {
    throw new Error('Auth placeholder still present after patch.');
  }
  if (!code.includes("authMode: 'NATIVE_HEADER_AUTH'")) {
    throw new Error('authMode invocation missing after patch.');
  }
  if (!code.includes('auth_mode=NATIVE_HEADER_AUTH')) {
    throw new Error('Native auth marker missing after patch.');
  }

  return code;
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (!args.credentialId) {
    throw new Error('Required --credential-id=<id>');
  }

  const creds = loadCredentials();
  const host = new URL(creds.apiUrl).host;
  if (host !== EXPECTED_HOST) {
    throw new Error(`Unexpected API host ${host}`);
  }

  const live = await getWorkflow(ALLOWED_WORKFLOW_ID, creds);
  if (live.name !== ALLOWED_WORKFLOW_NAME) {
    throw new Error(`Live name mismatch: ${live.name}`);
  }
  if (live.active !== false) {
    throw new Error('Live workflow is active; abort prepare.');
  }
  if (live.id !== ALLOWED_WORKFLOW_ID) {
    throw new Error(`Live id mismatch: ${live.id}`);
  }

  const working = structuredClone(live);
  const webhook = (working.nodes || []).find((n) => n.type === 'n8n-nodes-base.webhook');
  const processNode = (working.nodes || []).find((n) => n.name === 'Process Client Ops Gates');
  if (!webhook || !processNode) {
    throw new Error('Required nodes missing on live workflow.');
  }

  webhook.parameters = {
    ...(webhook.parameters || {}),
    authentication: 'headerAuth',
  };
  webhook.credentials = {
    [CREDENTIAL_TYPE]: {
      id: args.credentialId,
      name: CREDENTIAL_NAME,
    },
  };

  processNode.parameters = processNode.parameters || {};
  processNode.parameters.jsCode = patchProcessGatesCode(processNode.parameters.jsCode || '');

  working.meta = {
    ...(working.meta || {}),
    mars_auth_binding: AUTH_MODE,
    mars_auth_header: HEADER_NAME,
    mars_dedupe: 'DEDUPE_DEFERRED_SANDBOX',
    mars_no_telegram: true,
    mars_phase: '1B-B1',
    templateCredsSetupCompleted: true,
  };

  const putPayload = prepareWorkflowPutPayload(working);
  const putWebhook = putPayload.nodes.find((n) => n.type === 'n8n-nodes-base.webhook');
  putWebhook.parameters.authentication = 'headerAuth';
  putWebhook.credentials = {
    [CREDENTIAL_TYPE]: {
      id: args.credentialId,
      name: CREDENTIAL_NAME,
    },
  };

  const bundle = {
    auth_mode: AUTH_MODE,
    workflow_id: ALLOWED_WORKFLOW_ID,
    workflow_name: ALLOWED_WORKFLOW_NAME,
    pre_put_versionId: live.versionId || null,
    pre_put_updatedAt: live.updatedAt || null,
    active: false,
    credential_ref: {
      type: CREDENTIAL_TYPE,
      id: args.credentialId,
      name: CREDENTIAL_NAME,
      header_name: HEADER_NAME,
    },
    allowed_delta: [
      'Webhook.parameters.authentication -> headerAuth',
      'Webhook.credentials.httpHeaderAuth reference',
      'Process Client Ops Gates jsCode: remove auth placeholder; auth_mode=NATIVE_HEADER_AUTH',
      'meta.mars_auth_binding / mars_phase markers',
    ],
    full_workflow_for_validation: working,
    put_payload: putPayload,
  };

  mkdirSync(dirname(args.out), { recursive: true });
  writeFileSync(args.out, JSON.stringify(bundle, null, 2), 'utf8');

  console.log(
    JSON.stringify(
      {
        ok: true,
        out: args.out.replace(/\\/g, '/'),
        workflow_id: ALLOWED_WORKFLOW_ID,
        auth_mode: AUTH_MODE,
        credential_id: args.credentialId,
        credential_name: CREDENTIAL_NAME,
        placeholder_absent: !JSON.stringify(putPayload).includes(AUTH_PLACEHOLDER),
        webhook_authentication: putWebhook.parameters.authentication,
        active: false,
        pre_put_versionId: live.versionId || null,
      },
      null,
      2,
    ),
  );
}

main().catch((err) => {
  console.error(
    JSON.stringify({
      ok: false,
      error: err instanceof Error ? err.message.slice(0, 300) : String(err).slice(0, 300),
    }),
  );
  process.exitCode = 1;
});
