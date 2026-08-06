/**
 * Build inactive sandbox workflow template for Client Ops Bridge.
 * Does not call n8n. Embeds Code@2 logic with HITL auth placeholder.
 *
 * Run: node build-template.mjs
 */
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { randomUUID } from 'node:crypto';
import { AUTH_PLACEHOLDER, WORKFLOW_NAME } from './client-ops-validator.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const outDir = resolve(__dirname, '../templates');
const outPath = join(outDir, 'mars-client-ops-bridge-bzpm-sandbox.template.json');

const validatorSrc = readFileSync(
  join(__dirname, 'client-ops-validator.mjs'),
  'utf8',
);

// Strip ESM exports for Code@2 embedding; keep function bodies.
const embeddedLib = validatorSrc
  .replace(/^export /gm, '')
  .replace(
    /import\s+.*?from\s+['"].*?['"];?\s*/g,
    '',
  );

const captureCode = `// Capture Request Metadata — Client Ops sandbox
const item = $input.first().json || {};
const headers = item.headers || item.header || {};
const body = item.body !== undefined ? item.body : item;
let rawBodyBytes = 0;
try {
  rawBodyBytes = Buffer.byteLength(JSON.stringify(body ?? {}), 'utf8');
} catch (e) {
  rawBodyBytes = 0;
}
return [{
  json: {
    headers,
    body,
    rawBodyBytes,
    received_at: new Date().toISOString(),
  }
}];
`;

const pipelineCode = `// Client Ops Process Gates — sandbox template
// AUTH SECRET BINDING: HITL_REQUIRED — placeholder must be replaced before apply.
${embeddedLib}

const item = $input.first().json || {};
const expectedSecret = ${JSON.stringify(AUTH_PLACEHOLDER)};

const result = processClientOpsRequest({
  headers: item.headers || {},
  body: item.body,
  rawBodyBytes: item.rawBodyBytes || 0,
  expectedSecret,
});

const accepted =
  result.response &&
  (result.response.result === 'ACCEPTED' || result.response.result === 'DUPLICATE');

return [{
  json: {
    http_status: result.http_status,
    response: result.response,
    evidence: result.evidence || {},
    branch_accepted: accepted,
    received_at: item.received_at || null,
  }
}];
`;

function ifEquals(leftExpr, rightValue, id) {
  return {
    conditions: {
      options: {
        caseSensitive: true,
        leftValue: '',
        typeValidation: 'strict',
        version: 3,
      },
      conditions: [
        {
          id,
          leftValue: leftExpr,
          rightValue,
          operator: {
            type: 'string',
            operation: 'equals',
            name: 'filter.operator.equals',
          },
        },
      ],
      combinator: 'and',
    },
    options: {},
  };
}

const nodes = [
  {
    parameters: {
      httpMethod: 'POST',
      path: 'mars-client-ops-bridge-bzpm-sandbox',
      responseMode: 'responseNode',
      options: {},
    },
    id: randomUUID(),
    name: 'Webhook Intake',
    type: 'n8n-nodes-base.webhook',
    typeVersion: 2.1,
    position: [0, 300],
  },
  {
    parameters: { jsCode: captureCode },
    id: randomUUID(),
    name: 'Capture Request Metadata',
    type: 'n8n-nodes-base.code',
    typeVersion: 2,
    position: [240, 300],
  },
  {
    parameters: { jsCode: pipelineCode },
    id: randomUUID(),
    name: 'Process Client Ops Gates',
    type: 'n8n-nodes-base.code',
    typeVersion: 2,
    position: [480, 300],
  },
  {
    parameters: ifEquals(
      '={{ String($json.branch_accepted) }}',
      'true',
      randomUUID(),
    ),
    id: randomUUID(),
    name: 'IF Accepted Branch',
    type: 'n8n-nodes-base.if',
    typeVersion: 2.3,
    position: [720, 300],
  },
  {
    parameters: {
      jsCode: `const j = $input.first().json || {};
return [{
  json: {
    http_status: j.http_status,
    response: j.response,
    evidence: j.evidence || {},
    received_at: j.received_at || null,
  }
}];`,
    },
    id: randomUUID(),
    name: 'Prepare Accepted Response',
    type: 'n8n-nodes-base.code',
    typeVersion: 2,
    position: [960, 180],
  },
  {
    parameters: {
      jsCode: `const j = $input.first().json || {};
return [{
  json: {
    http_status: j.http_status,
    response: j.response,
    evidence: j.evidence || {},
    received_at: j.received_at || null,
  }
}];`,
    },
    id: randomUUID(),
    name: 'Prepare Rejected Response',
    type: 'n8n-nodes-base.code',
    typeVersion: 2,
    position: [960, 420],
  },
  {
    parameters: {
      respondWith: 'json',
      responseBody: '={{ $json.response }}',
      options: {
        responseCode: '={{ $json.http_status }}',
      },
    },
    id: randomUUID(),
    name: 'Respond Accepted',
    type: 'n8n-nodes-base.respondToWebhook',
    typeVersion: 1.1,
    position: [1200, 180],
  },
  {
    parameters: {
      respondWith: 'json',
      responseBody: '={{ $json.response }}',
      options: {
        responseCode: '={{ $json.http_status }}',
      },
    },
    id: randomUUID(),
    name: 'Respond Rejected',
    type: 'n8n-nodes-base.respondToWebhook',
    typeVersion: 1.1,
    position: [1200, 420],
  },
  {
    parameters: {
      jsCode: `const j = $input.first().json || {};
const evidence = j.evidence || {};
const response = j.response || {};
return [{
  json: {
    sanitized_evidence: {
      gate: evidence.gate || null,
      code: evidence.code || null,
      event_id: evidence.event_id || response.event_id || null,
      dedupe: evidence.dedupe || response.dedupe || null,
      http_status: j.http_status,
      received_at: j.received_at || null,
    }
  }
}];`,
    },
    id: randomUUID(),
    name: 'Sanitized Internal Evidence',
    type: 'n8n-nodes-base.code',
    typeVersion: 2,
    position: [960, 300],
    disabled: true,
    notes:
      'Optional post-gate evidence shape. Disabled in first sandbox; does not send Telegram or write Storage.',
  },
];

const connections = {
  'Webhook Intake': {
    main: [[{ node: 'Capture Request Metadata', type: 'main', index: 0 }]],
  },
  'Capture Request Metadata': {
    main: [[{ node: 'Process Client Ops Gates', type: 'main', index: 0 }]],
  },
  'Process Client Ops Gates': {
    main: [[{ node: 'IF Accepted Branch', type: 'main', index: 0 }]],
  },
  'IF Accepted Branch': {
    main: [
      [{ node: 'Prepare Accepted Response', type: 'main', index: 0 }],
      [{ node: 'Prepare Rejected Response', type: 'main', index: 0 }],
    ],
  },
  'Prepare Accepted Response': {
    main: [[{ node: 'Respond Accepted', type: 'main', index: 0 }]],
  },
  'Prepare Rejected Response': {
    main: [[{ node: 'Respond Rejected', type: 'main', index: 0 }]],
  },
};

const template = {
  name: WORKFLOW_NAME,
  active: false,
  nodes,
  connections,
  settings: { executionOrder: 'v1' },
  meta: {
    templateCredsSetupCompleted: false,
    mars_template: true,
    mars_status: 'LOCAL_TEMPLATE_NOT_APPLIED',
    mars_auth_binding: 'HITL_REQUIRED',
    mars_auth_placeholder: AUTH_PLACEHOLDER,
    mars_dedupe: 'DEDUPE_DEFERRED_SANDBOX',
    mars_profile: 'PROFILE_B_REQUIRED',
    mars_site_id: 'SITE-002',
    mars_domain: 'bzpm.ru',
    mars_no_telegram: true,
    mars_no_manual_ui_assembly: true,
  },
  tags: [],
};

// Structural safety strip
for (const node of template.nodes) {
  if ('webhookId' in node) delete node.webhookId;
  if ('credentials' in node) delete node.credentials;
}

mkdirSync(outDir, { recursive: true });
writeFileSync(outPath, `${JSON.stringify(template, null, 2)}\n`);
console.log(`wrote ${outPath}`);
console.log(
  JSON.stringify(
    {
      name: template.name,
      active: template.active,
      nodes: template.nodes.map((n) => ({
        name: n.name,
        type: n.type,
        typeVersion: n.typeVersion,
        disabled: Boolean(n.disabled),
      })),
      auth_placeholder_present: JSON.stringify(template).includes(AUTH_PLACEHOLDER),
    },
    null,
    2,
  ),
);
