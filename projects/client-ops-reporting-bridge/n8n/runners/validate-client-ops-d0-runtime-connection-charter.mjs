/**
 * Phase 1B-D0 — documentation / decision-pack validator (offline).
 * No live n8n mutation. No secret printing.
 */
import { existsSync, readFileSync, readdirSync, statSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(__dirname, '../../../..');
const PROJECT = resolve(REPO_ROOT, 'projects/client-ops-reporting-bridge');
const PACK = resolve(PROJECT, 'evidence/phase-1b-d0-runtime-connection-charter');
const CHARTER = resolve(
  PROJECT,
  'PHASE-1B-D0-INACTIVE-SANDBOX-NEXT-STEP-DECISION-AND-RUNTIME-CONNECTION-CHARTER.md',
);

const REQUIRED_PACK = [
  'README.md',
  'CURRENT-STATE-GAP-MATRIX.md',
  'DURABLE-DEDUPE-OPTIONS.md',
  'RUNTIME-CONNECTION-PATTERNS.md',
  'EVENT-ID-AND-DEDUPE-CONTRACT.md',
  'RUNTIME-PRODUCER-CONTRACT.md',
  'SECRET-AND-ENDPOINT-BOUNDARY.md',
  'RETRY-AND-FAILURE-SEMANTICS.md',
  'OBSERVABILITY-CONTRACT.md',
  'SCHEDULER-OWNERSHIP-DECISION.md',
  'ROLLBACK-ARCHITECTURE.md',
  'PRODUCTION-ACTIVATION-GATES.md',
  'NEXT-PHASE-DECISION.md',
  'SECURITY-REVIEW.md',
  'LIVE-GET-ONLY-RECONFIRMATION.json',
  'N8N-DATATABLE-CAPABILITY.json',
];

const SECRET_RES = [
  /\b\d{8,10}:[A-Za-z0-9_-]{30,}\b/,
  /api\.telegram\.org\/bot\d+/i,
  /CLIENT_OPS_WEBHOOK_AUTH_SECRET\s*=\s*\S+/i,
  /N8N_API_KEY\s*=\s*\S+/i,
  /https?:\/\/[^\s"'`]+\/webhook\/[^\s"'`]+/i,
];

const IMPLEMENTATION_CLAIM_RES = [
  /durable dedupe (is |was )?implemented/i,
  /push-webhook (is |was )?implemented/i,
  /runtime producer connected/i,
  /production activation (is |was )?authorized/i,
  /workflow (was )?activated in D0/i,
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

function main() {
  const gates = [];
  const fail = (id, detail) => gates.push({ id, ok: false, detail });
  const pass = (id, detail) => gates.push({ id, ok: true, detail });

  gates.push({ id: 'charter_exists', ok: existsSync(CHARTER) });
  for (const name of REQUIRED_PACK) {
    gates.push({ id: `pack_${name}`, ok: existsSync(resolve(PACK, name)) });
  }

  const next = readFileSync(resolve(PACK, 'NEXT-PHASE-DECISION.md'), 'utf8');
  const preferredNext =
    /Phase 1B-D1 — Durable Dedupe Design and Inactive Sandbox Implementation/.test(
      next,
    );
  gates.push({ id: 'next_phase_exact', ok: preferredNext });

  const patterns = readFileSync(
    resolve(PACK, 'RUNTIME-CONNECTION-PATTERNS.md'),
    'utf8',
  );
  const onePreferred =
    /\*\*PREFERRED\*\*/.test(patterns) &&
    /R1/.test(patterns) &&
    /\*\*FALLBACK\*\*/.test(patterns);
  gates.push({ id: 'one_preferred_runtime_pattern', ok: onePreferred });

  const dedupe = readFileSync(resolve(PACK, 'DURABLE-DEDUPE-OPTIONS.md'), 'utf8');
  const oneDedupe =
    /PRIMARY RECOMMENDATION/.test(dedupe) && /FALLBACK/.test(dedupe);
  const stageA = /SELECTED/.test(dedupe) && /mandatory before any runtime producer/i.test(dedupe);
  gates.push({ id: 'one_preferred_dedupe_architecture', ok: oneDedupe });
  gates.push({ id: 'dedupe_stage_ordering_A', ok: stageA });

  const charter = readFileSync(CHARTER, 'utf8');
  const noImplClaim = !IMPLEMENTATION_CLAIM_RES.some((re) => re.test(charter));
  gates.push({ id: 'no_implementation_claim_in_charter', ok: noImplClaim });

  const hitl = /HITL gates/i.test(charter) && /Production activation/i.test(charter);
  gates.push({ id: 'hitl_gates_present', ok: hitl });

  const prodForbidden =
    /FORBIDDEN WITHOUT NEW CHARTER/.test(charter) ||
    /does \*\*not\*\* authorize production activation/i.test(
      readFileSync(resolve(PACK, 'PRODUCTION-ACTIVATION-GATES.md'), 'utf8'),
    );
  gates.push({ id: 'production_activation_forbidden', ok: prodForbidden });

  const sched = readFileSync(
    resolve(PACK, 'SCHEDULER-OWNERSHIP-DECISION.md'),
    'utf8',
  );
  const dirtyBan =
    /must not\*\* run from dirty `X:\\AI MARS`/i.test(sched) ||
    /must not.*dirty `X:\\AI MARS`/i.test(sched);
  gates.push({ id: 'scheduler_dirty_main_prohibition', ok: dirtyBan });

  const live = JSON.parse(
    readFileSync(resolve(PACK, 'LIVE-GET-ONLY-RECONFIRMATION.json'), 'utf8'),
  );
  gates.push({
    id: 'live_inactive',
    ok: live.active === false && live.executions === 25 && live.nodes === 10,
  });
  gates.push({
    id: 'live_pattern_b',
    ok: live.pattern_b?.confirmed === true,
  });
  gates.push({
    id: 'live_no_production_connections',
    ok:
      live.connections?.production_monitor === false &&
      live.connections?.scheduler === false &&
      live.connections?.exporter_runtime === false,
  });

  const files = [CHARTER, ...walk(PACK)];
  let secretHits = 0;
  let urlHits = 0;
  for (const f of files) {
    const text = readFileSync(f, 'utf8');
    for (const re of SECRET_RES) {
      if (re.test(text)) {
        if (/webhook\//i.test(re.source)) urlHits += 1;
        else secretHits += 1;
      }
    }
  }
  gates.push({ id: 'secret_leakage_zero', ok: secretHits === 0, detail: String(secretHits) });
  gates.push({ id: 'full_url_leakage_zero', ok: urlHits === 0, detail: String(urlHits) });

  const failed = gates.filter((g) => !g.ok);
  for (const g of gates) {
    console.log(`${g.ok ? 'PASS' : 'FAIL'} ${g.id}${g.detail ? ` (${g.detail})` : ''}`);
  }
  console.log(
    failed.length === 0
      ? `D0 documentation validator: PASS (${gates.length}/${gates.length})`
      : `D0 documentation validator: FAIL (${gates.length - failed.length}/${gates.length})`,
  );
  process.exit(failed.length === 0 ? 0 : 1);
}

main();
