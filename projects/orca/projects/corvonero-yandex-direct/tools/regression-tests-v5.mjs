#!/usr/bin/env node
/**
 * ORCA Corvonero regression tests v5 — evidence gates.
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { runRegressionTests } from './lib/collision-engine-v3.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, '..');

const dataset = JSON.parse(fs.readFileSync(path.join(ROOT, 'production/direct-commander-production-dataset-v5.json'), 'utf8'));
const semantic = JSON.parse(fs.readFileSync(path.join(ROOT, 'production/validation/semantic-evidence-validation-v5.json'), 'utf8'));
const reviewWb = JSON.parse(fs.readFileSync(path.join(ROOT, 'production/validation/review-workbook-v5-result.json'), 'utf8'));
const collision = JSON.parse(fs.readFileSync(path.join(ROOT, 'production/validation/negative-collision-validation-v5.json'), 'utf8'));
const negRisk = JSON.parse(fs.readFileSync(path.join(ROOT, 'production/validation/negative-risk-validation-v5.json'), 'utf8'));
const v5Val = JSON.parse(fs.readFileSync(path.join(ROOT, 'production/validation/direct-commander-v5-validation.json'), 'utf8'));

const result = runRegressionTests(dataset.keywords, dataset.cross_negatives, dataset.global_negatives);

const report = {
  tested_at: new Date().toISOString(),
  version: 'v5',
  regression: result,
  semantic_evidence_passed: semantic.passed,
  review_workbook_integrity: reviewWb.integrity?.passed,
  negative_risk_unresolved: negRisk.unresolved_count,
  exported_collision_blocking: collision.literal_collisions_after,
  direct_commander_validation: v5Val.status,
  passed:
    result.passed &&
    collision.literal_collisions_after === 0 &&
    semantic.passed &&
    reviewWb.integrity?.passed &&
    negRisk.unresolved_count === 0 &&
    v5Val.status === 'PASS',
};

fs.writeFileSync(path.join(ROOT, 'production/validation/regression-tests-v5.json'), JSON.stringify(report, null, 2));

console.log(JSON.stringify(report, null, 2));
process.exit(report.passed ? 0 : 1);
