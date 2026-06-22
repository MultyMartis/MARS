#!/usr/bin/env node
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { runFullCorpusProduction } from '../runtime/full-corpus-runner.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const args = process.argv.slice(2);

async function main() {
  const opts = parseArgs(args);
  if (opts.help || !opts.command) {
    console.log('Usage: orca-semantic-production.mjs run --manifest <path> --out <dir>');
    console.log('       orca-semantic-production.mjs run --fixture-corpus <path> --out <dir> [--allow-missing-service-registry]');
    process.exit(opts.help ? 0 : 1);
  }

  if (opts.command === 'run') {
    const result = await runFullCorpusProduction({
      manifestPath: opts.manifest,
      fixtureCorpus: opts.fixtureCorpus,
      outDir: opts.out || path.join(__dirname, '../reports/_last-run'),
      allowMissingServiceRegistry: opts.allowMissingServiceRegistry,
      batchSize: opts.batchSize ? Number(opts.batchSize) : 100,
    });
    if (!result.ok) {
      console.error(result.blocker);
      process.exit(2);
    }
    console.log(`Run complete: ${result.runId}`);
    console.log(`Output: ${result.outDir}`);
    console.log(`Accept: ${result.metrics.accept} Reject: ${result.metrics.reject} Abstain: ${result.metrics.abstain}`);
    console.log(`Review queue: ${result.metrics.human_review_required} (${(result.metrics.review_ratio * 100).toFixed(1)}%)`);
    process.exit(0);
  }
}

function parseArgs(argv) {
  const o = { command: argv[0] };
  for (let i = 1; i < argv.length; i++) {
    if (argv[i] === '--manifest') o.manifest = argv[++i];
    else if (argv[i] === '--out') o.out = argv[++i];
    else if (argv[i] === '--fixture-corpus') o.fixtureCorpus = argv[++i];
    else if (argv[i] === '--allow-missing-service-registry') o.allowMissingServiceRegistry = true;
    else if (argv[i] === '--batch-size') o.batchSize = argv[++i];
    else if (argv[i] === '--help') o.help = true;
  }
  return o;
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
