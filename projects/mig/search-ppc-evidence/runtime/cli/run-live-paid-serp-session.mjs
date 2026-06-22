#!/usr/bin/env node
/**
 * Wave 2.1 — bounded live Paid SERP session runner
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { authorizeEvidenceCommand } from '../lib/gate.mjs';
import { validateBusinessHoursWindow } from '../lib/business-hours.mjs';
import { runLivePaidSerpSession } from '../lib/paid-serp-live-capture.mjs';
import { buildAdvertiserRegistry } from '../lib/competitor-registry.mjs';
import { loadJson, writeJson, nowIso, sha256File } from '../lib/utils.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

function parseArgs(argv) {
  const args = { _: [] };
  for (let i = 2; i < argv.length; i += 1) {
    const a = argv[i];
    if (a === '--manifest') args.manifest = argv[++i];
    else if (a === '--session') args.session = argv[++i];
    else if (a === '--queries') args.queries = argv[++i];
    else if (a === '--dry-run') args.dryRun = true;
    else args._.push(a);
  }
  return args;
}

async function main() {
  const args = parseArgs(process.argv);
  const session = loadJson(args.session);
  let querySet = loadJson(args.queries);
  if (session.query_filter?.length) {
    querySet = {
      ...querySet,
      queries: querySet.queries.filter((q) => session.query_filter.includes(q.query_id)),
    };
  }
  const manifestPath = args.manifest || session.manifest_path;

  const windowCheck = validateBusinessHoursWindow({
    projectTimezone: session.timezone,
    currentTimestamp: nowIso(),
    observationWindows: session.allowed_local_collection_windows,
    weekdayPolicy: session.weekday_policy,
    approvedExceptions: session.approved_exceptions || [],
  });

  const preLive = {
    checked_at: nowIso(),
    manifest_path: manifestPath,
    session_id: session.session_id,
    business_hours: windowCheck,
    query_count: querySet.queries.length,
    query_limit: session.query_limit,
    output_path: session.output_path,
    captcha_policy: session.captcha_policy,
    production_authority: false,
    evidence_class: 'TECHNICAL LIVE EVIDENCE',
  };

  const preLivePath = path.join(path.dirname(args.session), 'pre-live-validation-v1.json');
  writeJson(preLivePath, preLive);

  if (!windowCheck.allowed) {
    console.log(JSON.stringify({ status: 'LIVE SESSION BLOCKED', reason: windowCheck.status, pre_live: preLive }, null, 2));
    process.exit(3);
  }

  if (args.dryRun) {
    console.log(JSON.stringify({ status: 'PRE-LIVE OK — DRY RUN', pre_live: preLive }, null, 2));
    process.exit(0);
  }

  const auth = authorizeEvidenceCommand({
    manifestPath,
    cliCommand: 'paid-serp:run',
  });

  if (!auth.allowed) {
    console.error(JSON.stringify({ status: 'BLOCKED', blockers: auth.blockers }, null, 2));
    process.exit(2);
  }

  const result = await runLivePaidSerpSession({
    sessionConfig: session,
    querySet,
    receipt: auth.evidence_record,
  });

  const observations = result.summary.results.map((r) =>
    r.capture_dir ? loadJson(path.join(r.capture_dir, 'observation.json')) : null,
  ).filter(Boolean);
  const advertisers = buildAdvertiserRegistry(observations);

  const pack = {
    pack_id: `w2-1-live-evidence-${session.session_id}`,
    generated_at: nowIso(),
    evidence_class: 'TECHNICAL LIVE EVIDENCE',
    production_authority: false,
    session_summary_path: result.session_path,
    session_summary_sha256: sha256File(result.session_path),
    advertisers,
    limitations: [
      'Bounded technical validation — not production research',
      'Not semantic core or benchmark',
      'No strategic conclusions',
    ],
  };

  writeJson(path.join(session.output_path, 'live-evidence-pack-v1.json'), pack);
  console.log(JSON.stringify({ status: 'LIVE SESSION COMPLETE', summary: result.summary, pack_id: pack.pack_id }, null, 2));
  process.exit(result.ok ? 0 : 1);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
