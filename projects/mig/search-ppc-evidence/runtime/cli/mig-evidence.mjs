#!/usr/bin/env node
/**
 * MIG Search PPC Evidence CLI — Wave 2
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { authorizeEvidenceCommand } from '../lib/gate.mjs';
import { registerSource } from '../lib/source-registry.mjs';
import { intakeCorpus } from '../lib/corpus-intake.mjs';
import { normalizeCorpus } from '../lib/canonical-registry.mjs';
import { validateBusinessHoursWindow } from '../lib/business-hours.mjs';
import { runPaidSerpSession } from '../lib/paid-serp-runtime.mjs';
import { buildPackFromSession } from '../lib/competitor-pack.mjs';
import { buildEvidenceManifest } from '../lib/evidence-manifest.mjs';
import { loadJson, writeJson } from '../lib/utils.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const FIXTURES = path.join(__dirname, '../../fixtures');

function parseArgs(argv) {
  const args = { _: [] };
  for (let i = 2; i < argv.length; i += 1) {
    const a = argv[i];
    if (a === '--manifest') args.manifest = argv[++i];
    else if (a === '--dry-run') args.dryRun = true;
    else if (a === '--registry') args.registry = argv[++i];
    else if (a === '--source') args.source = argv[++i];
    else if (a === '--output') args.output = argv[++i];
    else if (a === '--corpus') args.corpus = argv[++i];
    else if (a === '--region') args.region = argv[++i];
    else if (a === '--session') args.session = argv[++i];
    else if (a === '--fixture') args.fixtures = [...(args.fixtures || []), argv[++i]];
    else args._.push(a);
  }
  return args;
}

async function main() {
  const args = parseArgs(process.argv);
  const command = args._[0];
  if (!command) {
    console.log(`Usage: node mig-evidence.mjs <command> --manifest <path> [options]

Commands:
  source:register       --source <json> --registry <path>
  corpus:intake         --registry <path> --output <dir>
  corpus:normalize      --corpus <path> --output <dir> [--region R]
  paid-serp:validate-window --session <json>
  paid-serp:run         --session <json> [--fixture <path>...]
  paid-serp:report      --session <path>
  competitors:build-pack --session <path> --output <path>
  evidence:status       --output <dir>
`);
    process.exit(1);
  }

  const auth = authorizeEvidenceCommand({
    manifestPath: args.manifest,
    cliCommand: command,
    dryRun: args.dryRun,
  });

  if (!auth.allowed) {
    console.error(JSON.stringify({ status: 'BLOCKED', blockers: auth.blockers }, null, 2));
    process.exit(auth.exit_code || 2);
  }

  let result;
  switch (command) {
    case 'source:register': {
      const record = loadJson(args.source);
      result = registerSource({ registryPath: args.registry, record });
      break;
    }
    case 'corpus:intake': {
      const registry = loadJson(args.registry);
      result = intakeCorpus({ sources: registry.sources, outputDir: args.output });
      break;
    }
    case 'corpus:normalize': {
      result = normalizeCorpus({
        corpusPath: args.corpus,
        outputDir: args.output,
        region: args.region,
      });
      break;
    }
    case 'paid-serp:validate-window': {
      const session = loadJson(args.session);
      result = validateBusinessHoursWindow({
        projectTimezone: session.timezone,
        currentTimestamp: session.current_timestamp,
        observationWindows: session.allowed_local_collection_windows,
        weekdayPolicy: session.weekday_policy,
        approvedExceptions: session.approved_exceptions,
      });
      break;
    }
    case 'paid-serp:run': {
      const session = loadJson(args.session);
      const fixtures = args.fixtures?.length
        ? args.fixtures
        : [path.join(FIXTURES, 'paid-serp/ads-observed.json'), path.join(FIXTURES, 'paid-serp/no-ads.json')];
      result = runPaidSerpSession({
        sessionConfig: session,
        fixturePaths: fixtures,
        receipt: auth.evidence_record,
      });
      break;
    }
    case 'competitors:build-pack': {
      const summary = loadJson(args.session);
      result = buildPackFromSession(summary, args.output);
      break;
    }
    case 'evidence:status': {
      const sourceRegistry = fs.existsSync(path.join(args.output, 'source-registry.json'))
        ? loadJson(path.join(args.output, 'source-registry.json'))
        : null;
      const intake = fs.existsSync(path.join(args.output, 'intake-report.json'))
        ? loadJson(path.join(args.output, 'intake-report.json'))
        : null;
      const canonical = fs.existsSync(path.join(args.output, 'canonical-registry.json'))
        ? loadJson(path.join(args.output, 'canonical-registry.json'))
        : null;
      result = buildEvidenceManifest({
        projectId: 'UNKNOWN',
        manifestPath: args.manifest,
        sourceRegistry,
        rawCorpus: intake,
        canonicalRegistry: canonical,
        paidSerpSessions: [],
        competitorPack: null,
        orcaSemanticArtifacts: {},
      });
      if (args.output) writeJson(path.join(args.output, 'evidence-manifest.json'), result.manifest);
      break;
    }
    default:
      console.error(`Unknown command: ${command}`);
      process.exit(1);
  }

  console.log(JSON.stringify(result, null, 2));
  process.exit(result.ok === false ? 2 : 0);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
