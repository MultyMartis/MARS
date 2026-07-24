/**
 * Validate Phase 1B-C1 evidence pack (offline).
 */

import { existsSync, readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(__dirname, '../../../..');
const EVIDENCE = resolve(
  REPO_ROOT,
  'projects/client-ops-reporting-bridge/n8n/evidence/phase-1b-c1-telegram-sandbox-controlled-apply',
);

const REQUIRED = [
  'README.md',
  'APPLY-CHARTER.json',
  'PRE-APPLY-MANIFEST.json',
  'SANITIZED-STRUCTURAL-DIFF.json',
  'POST-APPLY-WORKFLOW-STATE.json',
  'SANDBOX-TEST-MANIFEST.json',
  'SANITIZED-WEBHOOK-RESULT.json',
  'SANITIZED-EXECUTION-RESULT.json',
  'SANITIZED-TELEGRAM-DELIVERY.json',
  'CONTAINMENT-STATUS.md',
  'ROLLBACK-READINESS.md',
  'TEST-RESULTS.md',
  'SECURITY-REVIEW.md',
];

const SECRET_RE = [
  /\b\d{6,}:[A-Za-z0-9_-]{20,}\b/,
  /api\.telegram\.org\/bot\d+/i,
  /CLIENT_OPS_WEBHOOK_AUTH_SECRET\s*=\s*\S+/i,
  /N8N_API_KEY\s*=\s*\S+/i,
];

function main() {
  const gates = [];
  for (const name of REQUIRED) {
    const p = resolve(EVIDENCE, name);
    gates.push({ id: `file_${name}`, ok: existsSync(p) });
  }

  const delivery = JSON.parse(
    readFileSync(resolve(EVIDENCE, 'SANITIZED-TELEGRAM-DELIVERY.json'), 'utf8'),
  );
  gates.push({ id: 'delivered_one', ok: delivery.delivered === 1 && delivery.attempts === 1 });
  gates.push({ id: 'duplicates_zero', ok: delivery.duplicates === 0 });
  gates.push({ id: 'credential_exact', ok: delivery.credential_id === '2bIC5376l7ElXb4B' });

  const exec = JSON.parse(
    readFileSync(resolve(EVIDENCE, 'SANITIZED-EXECUTION-RESULT.json'), 'utf8'),
  );
  gates.push({ id: 'executions_24_to_25', ok: exec.executions_before === 24 && exec.executions_after === 25 });
  gates.push({ id: 'respond_before_telegram', ok: exec.respond_before_telegram === true });
  gates.push({ id: 'telegram_runs_one', ok: exec.telegram_node_runs === 1 });

  const post = JSON.parse(readFileSync(resolve(EVIDENCE, 'POST-APPLY-WORKFLOW-STATE.json'), 'utf8'));
  gates.push({ id: 'final_inactive', ok: post.active === false });
  gates.push({ id: 'nodes_10', ok: post.nodes === 10 });
  gates.push({ id: 'pattern_b', ok: /Respond Accepted → Telegram Notify Accepted/.test(post.pattern_b_connection) });

  const webhook = JSON.parse(
    readFileSync(resolve(EVIDENCE, 'SANITIZED-WEBHOOK-RESULT.json'), 'utf8'),
  );
  gates.push({ id: 'http_202', ok: webhook.http_status === 202 });
  gates.push({ id: 'accepted', ok: webhook.business_result === 'ACCEPTED' });

  let leak = false;
  for (const name of REQUIRED) {
    const text = readFileSync(resolve(EVIDENCE, name), 'utf8');
    for (const re of SECRET_RE) {
      if (re.test(text)) leak = true;
    }
  }
  gates.push({ id: 'no_secret_leak', ok: !leak });

  const failed = gates.filter((g) => !g.ok);
  console.log(
    JSON.stringify(
      {
        validator: 'validate-client-ops-telegram-sandbox-c1-evidence',
        pass_count: gates.filter((g) => g.ok).length,
        fail_count: failed.length,
        gates,
        verdict: failed.length === 0 ? 'PASS' : 'FAIL',
      },
      null,
      2,
    ),
  );
  if (failed.length) process.exitCode = 2;
}

main();
