#!/usr/bin/env node
/**
 * ORCA Corvonero regression tests v4 — semantic + collision gates.
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { runRegressionTests } from './lib/collision-engine-v3.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, '..');

const dataset = JSON.parse(
  fs.readFileSync(path.join(ROOT, 'production/direct-commander-production-dataset-v4.json'), 'utf8')
);
const semantic = JSON.parse(
  fs.readFileSync(path.join(ROOT, 'production/validation/semantic-review-v4.json'), 'utf8')
);
const reviewWb = JSON.parse(
  fs.readFileSync(path.join(ROOT, 'production/validation/review-workbook-v4-result.json'), 'utf8')
);

const result = runRegressionTests(dataset.keywords, dataset.cross_negatives, dataset.global_negatives);

const collision = JSON.parse(
  fs.readFileSync(path.join(ROOT, 'production/validation/negative-collision-validation-v4.json'), 'utf8')
);

const report = {
  tested_at: new Date().toISOString(),
  version: 'v4',
  regression: result,
  semantic_review_passed: semantic.passed,
  review_workbook_evidence: reviewWb.evidence_populated,
  exported_collision_blocking: collision.collisions_after_correction,
  passed:
    result.passed &&
    collision.collisions_after_correction === 0 &&
    semantic.passed &&
    reviewWb.evidence_populated,
};

fs.writeFileSync(path.join(ROOT, 'production/validation/regression-tests-v4.json'), JSON.stringify(report, null, 2));

console.log(JSON.stringify(report, null, 2));
process.exit(report.passed ? 0 : 1);
