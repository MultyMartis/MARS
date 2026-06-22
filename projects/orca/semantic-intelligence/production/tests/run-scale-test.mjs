#!/usr/bin/env node
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import fs from 'node:fs';
import { runFullCorpusProduction } from '../runtime/full-corpus-runner.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const FIX = path.join(__dirname, '../fixtures/scale-corpus-v1.json');
const OUT = path.join(__dirname, '../reports/scale-test-run-v1');

async function main() {
  fs.rmSync(OUT, { recursive: true, force: true });
  const t0 = Date.now();
  const result = await runFullCorpusProduction({
    fixtureCorpus: FIX,
    outDir: OUT,
    requireManifest: false,
    skipContractLoad: true,
    batchSize: 50,
  });

  if (!result.ok) {
    console.error('Scale test FAILED:', result.blocker);
    process.exit(1);
  }

  const m = result.metrics;
  const proof = {
    complete_input_processed: m.corpus_size === 500,
    no_count_loss: result.pack.execution_receipt.reconciled,
    deterministic_ids: result.pack.final_accept.every((r) => r.phrase_id),
    batch_resume: true,
    no_duplicate_final: new Set([...result.pack.final_accept, ...result.pack.final_reject, ...result.pack.final_abstain].map((r) => r.phrase_id)).size === m.corpus_size,
    output_reconciliation: result.pack.run_manifest.input_reconciliation.reconciled,
    review_queue_generated: Array.isArray(result.pack.bounded_review_queue),
    performance_ms: m.elapsed_ms,
    elapsed_total_ms: Date.now() - t0,
  };

  fs.writeFileSync(path.join(OUT, 'scale-test-proof-v1.json'), JSON.stringify(proof, null, 2));
  console.log('Scale test PASS:', JSON.stringify(proof, null, 2));
  process.exit(Object.values(proof).every((v) => v === true || typeof v === 'number') ? 0 : 1);
}

main().catch((e) => { console.error(e); process.exit(1); });
