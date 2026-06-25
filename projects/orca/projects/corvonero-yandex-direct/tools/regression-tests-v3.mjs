#!/usr/bin/env node
/**
 * ORCA Corvonero regression tests v3 — reusable negative/semantic failure classes.
 * Run: node tools/regression-tests-v3.mjs
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { runRegressionTests } from './lib/collision-engine-v3.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, '..');

const dataset = JSON.parse(
  fs.readFileSync(path.join(ROOT, 'production/direct-commander-production-dataset-v3.json'), 'utf8')
);

const result = runRegressionTests(
  dataset.keywords,
  dataset.cross_negatives,
  dataset.global_negatives
);

const collision = JSON.parse(
  fs.readFileSync(path.join(ROOT, 'production/validation/negative-collision-validation-v3.json'), 'utf8')
);

const report = {
  tested_at: new Date().toISOString(),
  regression: result,
  exported_collision_blocking: collision.collisions_after_correction,
  passed: result.passed && collision.collisions_after_correction === 0,
};

fs.writeFileSync(path.join(ROOT, 'production/validation/regression-tests-v3.json'), JSON.stringify(report, null, 2));

console.log(JSON.stringify(report, null, 2));
process.exit(report.passed ? 0 : 1);
