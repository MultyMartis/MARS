/**
 * Offline security scan for Client Ops programmer extension artifacts.
 */
import { existsSync, readdirSync, readFileSync, statSync } from 'node:fs';
import { join } from 'node:path';

const roots = [
  'projects/client-ops-reporting-bridge/n8n',
  'projects/client-ops-reporting-bridge/CLIENT-OPS-PROGRAMMER-CAPABILITY-EXTENSION.md',
  'projects/client-ops-reporting-bridge/PHASE-1B-B-INACTIVE-SANDBOX-WORKFLOW.md',
  'projects/client-ops-reporting-bridge/PHASE-1B-B1-NATIVE-WEBHOOK-AUTH-BINDING.md',
  'projects/client-ops-reporting-bridge/PHASE-1B-B2-AUTHENTICATED-SANDBOX-POST-VALIDATION.md',
  'projects/client-ops-reporting-bridge/PHASE-1B-C-TELEGRAM-BOT-INTAKE-AND-INTEGRATION-PREPARATION.md',
  'projects/client-ops-reporting-bridge/PHASE-1B-C0-TELEGRAM-CHAT-TARGET-DISCOVERY-RETRY.md',
  'projects/client-ops-reporting-bridge/PHASE-1B-C0R2-TELEGRAM-CHAT-TARGET-DISCOVERY-FINAL-RETRY.md',
  'projects/client-ops-reporting-bridge/PHASE-1B-C0S-TELEGRAM-INTEGRATION-SEMANTICS-VERIFICATION.md',
  'projects/client-ops-reporting-bridge/PHASE-1B-C1-TELEGRAM-SANDBOX-INTEGRATION-CONTROLLED-APPLY.md',
  'projects/client-ops-reporting-bridge/PHASE-1B-D0-INACTIVE-SANDBOX-NEXT-STEP-DECISION-AND-RUNTIME-CONNECTION-CHARTER.md',
  'projects/client-ops-reporting-bridge/PHASE-1B-D1-DURABLE-DEDUPE-DESIGN-AND-INACTIVE-SANDBOX-IMPLEMENTATION.md',
  'projects/client-ops-reporting-bridge/evidence/phase-1b-d0-runtime-connection-charter',
  'projects/client-ops-reporting-bridge/README.md',

  'projects/client-ops-reporting-bridge/ROADMAP.md',
  'projects/client-ops-reporting-bridge/PHASE-1-IMPLEMENTATION-READINESS.md',
  'projects/client-ops-reporting-bridge/PHASE-1-MVP-GATES.md',
  'projects/metabot-seo-content-agent/metabot-developer/client-ops-n8n-extension-v1.md',
];

function walk(p, out = []) {
  if (!existsSync(p)) return out;
  const st = statSync(p);
  if (st.isFile()) {
    out.push(p);
    return out;
  }
  for (const name of readdirSync(p)) walk(join(p, name), out);
  return out;
}

const patterns = [
  { id: 'telegram_bot_token', re: /\b\d{8,10}:[A-Za-z0-9_-]{30,}\b/ },
  { id: 'private_key', re: /BEGIN (RSA |OPENSSH )?PRIVATE KEY/ },
  {
    id: 'password_assignment',
    re: /password\s*[:=]\s*['"][^'"]{8,}/i,
  },
  {
    id: 'real_bearer',
    re: /Bearer\s+(?!SYNTHETIC_|REDACTED|<<<)[A-Za-z0-9._-]{20,}/,
  },
  {
    id: 'n8n_api_key',
    re: /N8N_API_KEY\s*=\s*['"]?[A-Za-z0-9_-]{20,}/,
  },
  { id: 'webhookId_field', re: /"webhookId"\s*:/ },
  {
    id: 'chat_id_numeric',
    re: /chat[_-]?id["']?\s*[:=]\s*["']?\d{6,}/i,
  },
];

const files = roots.flatMap((r) => walk(r));
const findings = [];

for (const f of files) {
  const text = readFileSync(f, 'utf8');
  if (f.endsWith('mars-client-ops-bridge-bzpm-sandbox.template.json')) {
    const wf = JSON.parse(text);
    if (wf.id || wf.versionId) {
      findings.push({ file: f, id: 'workflow_top_id' });
    }
    for (const node of wf.nodes || []) {
      if (node.webhookId) findings.push({ file: f, id: 'node_webhookId', node: node.name });
      if (node.credentials) {
        findings.push({ file: f, id: 'node_credentials', node: node.name });
      }
    }
  }
  for (const p of patterns) {
    if (p.re.test(text)) {
      // Operational Telegram chat IDs are permitted only in Phase 1B-C discovery evidence.
      if (
        p.id === 'chat_id_numeric' &&
        (/phase-1b-c-telegram-bot-intake[\\/](CHAT-TARGET-DISCOVERY|PROPOSED-INTEGRATION)\.json$/i.test(
          f.replace(/\\/g, '/'),
        ) ||
          /phase-1b-c0s-telegram-integration-semantics[\\/](SEMANTICS-DECISION|LEVEL-2-TELEGRAM-RESULT|PATTERN-A-RESULT|TEST-RESULTS|CONTAINMENT-STATUS)\.(json|md)$/i.test(
            f.replace(/\\/g, '/'),
          ) ||
          /phase-1b-c1-telegram-sandbox-controlled-apply[\\/].+\.(json|md)$/i.test(
            f.replace(/\\/g, '/'),
          ) ||
          /phase-1b-d0-runtime-connection-charter[\\/].+\.(json|md)$/i.test(
            f.replace(/\\/g, '/'),
          ) ||
          /phase-1b-d1-durable-dedupe[\\/].+\.(json|md)$/i.test(
            f.replace(/\\/g, '/'),
          ) ||
          /PHASE-1B-D0-INACTIVE-SANDBOX-NEXT-STEP-DECISION-AND-RUNTIME-CONNECTION-CHARTER\.md$/i.test(
            f.replace(/\\/g, '/'),
          ) ||
          /PHASE-1B-D1-DURABLE-DEDUPE-DESIGN-AND-INACTIVE-SANDBOX-IMPLEMENTATION\.md$/i.test(
            f.replace(/\\/g, '/'),
          ) ||
          /runners[\\/](run-client-ops-durable-dedupe-sandbox|lib[\\/]client-ops-dedupe-compose)\.mjs$/i.test(
            f.replace(/\\/g, '/'),
          ))
      ) {
        continue;
      }
      findings.push({ file: f, id: p.id });
    }
  }
}

console.log(
  JSON.stringify(
    {
      files_scanned: files.length,
      findings,
      allow_markers: [
        'SYNTHETIC_CLIENT_OPS_HARNESS_SECRET_v1_NOT_A_REAL_CREDENTIAL',
        '<<<HITL_REQUIRED:CLIENT_OPS_WEBHOOK_AUTH_SECRET>>>',
        'WRONG_SYNTHETIC_VALUE',
      ],
      verdict: findings.length === 0 ? 'CLEAN' : 'REVIEW',
    },
    null,
    2,
  ),
);
process.exitCode = findings.length === 0 ? 0 : 1;
