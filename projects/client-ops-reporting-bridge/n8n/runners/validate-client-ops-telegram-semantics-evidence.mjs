/**
 * Validate Phase 1B-C0S semantics evidence pack (offline).
 */
import { existsSync, readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(__dirname, '../../../..');
const EVIDENCE = resolve(
  REPO_ROOT,
  'projects/client-ops-reporting-bridge/n8n/evidence/phase-1b-c0s-telegram-integration-semantics',
);

const REQUIRED = [
  'README.md',
  'TEST-CHARTER.json',
  'TEMP-WORKFLOW-MANIFEST.json',
  'LEVEL-1-STRUCTURAL-RESULT.json',
  'EXECUTION-ORDER-EVIDENCE.json',
  'SEMANTICS-DECISION.json',
  'ASYNC-BRANCH-EVALUATION.md',
  'CONTAINMENT-STATUS.md',
  'TEST-RESULTS.md',
  'SECURITY-REVIEW.md',
];

const SECRET_RE = [
  /\b\d{6,}:[A-Za-z0-9_-]{20,}\b/,
  /api\.telegram\.org\/bot/i,
  /https?:\/\/n8n\.ai-metacode\.com\/webhook\/[A-Za-z0-9_-]+/i,
  /CLIENT_OPS_WEBHOOK_AUTH_SECRET\s*=\s*\S+/i,
];

function main() {
  const gates = [];
  for (const name of REQUIRED) {
    const p = resolve(EVIDENCE, name);
    gates.push({ id: `file_${name}`, ok: existsSync(p) });
  }

  const decisionPath = resolve(EVIDENCE, 'SEMANTICS-DECISION.json');
  if (existsSync(decisionPath)) {
    const d = JSON.parse(readFileSync(decisionPath, 'utf8'));
    const allowed = new Set([
      'PATTERN_B_CONFIRMED',
      'PATTERN_A_REQUIRED',
      'ASYNC_BRANCH_PATTERN_CONFIRMED',
      'SEMANTICS_NOT_PROVEN',
    ]);
    gates.push({
      id: 'decision_allowed',
      ok: allowed.has(d.decision),
      detail: d.decision,
    });
    gates.push({
      id: 'telegram_cap',
      ok: (d.telegram_messages_attempted ?? 99) <= 1,
      detail: d.telegram_messages_attempted,
    });
    gates.push({
      id: 'delivered_cap',
      ok: (d.telegram_messages_delivered ?? 99) <= 1,
      detail: d.telegram_messages_delivered,
    });
  }

  let leak = 0;
  for (const name of REQUIRED) {
    const p = resolve(EVIDENCE, name);
    if (!existsSync(p)) continue;
    const text = readFileSync(p, 'utf8');
    for (const re of SECRET_RE) {
      if (re.test(text)) leak += 1;
    }
  }
  gates.push({ id: 'secret_url_leakage', ok: leak === 0, detail: leak });

  const failed = gates.filter((g) => !g.ok);
  console.log(
    JSON.stringify(
      {
        validator: 'validate-client-ops-telegram-semantics-evidence',
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
