#!/usr/bin/env node
/** Repair checkpoint after partial resume batch. */
import fs from 'node:fs';

const STORAGE = 'C:/MARS Phenix/AI MARS STORAGE/mig/corvonero/semantic-runs/corv-semantic-v2-20260626-004';
const cpPath = `${STORAGE}/checkpoints/checkpoint-phase4-v1.json`;
const regPath = `${STORAGE}/checkpoints/phase4-semantic-registry-v1.json`;
const cp = JSON.parse(fs.readFileSync(cpPath, 'utf8'));
const reg = JSON.parse(fs.readFileSync(regPath, 'utf8'));

const batch8 = JSON.parse(fs.readFileSync(`${STORAGE}/batches/phase4-batch-008/batch-completion-receipt-v1.json`, 'utf8'));

cp.cumulative_cost_usd = batch8.cumulative_cost_usd;
cp.unique_assessed_total = reg.results.length;
cp.production_newly_processed = reg.results.filter((r) => r.production_source === 'PHASE_4_NEW').length;
cp.missing = 2368 - cp.unique_assessed_total;
cp.lifecycle_state = 'PHASE_4_RESUME_AUTHORIZED';
cp.stop_reason = null;
cp.last_batch_id = 'phase4-batch-008';
if (!cp.batch_receipts.includes('phase4-batch-008')) cp.batch_receipts.push('phase4-batch-008');

fs.writeFileSync(cpPath, JSON.stringify(cp, null, 2));

const quarantinePath = `${STORAGE}/quarantine/CR2-PHR-00799.json`;
if (fs.existsSync(quarantinePath)) fs.unlinkSync(quarantinePath);

console.log(JSON.stringify({
  unique: cp.unique_assessed_total,
  missing: cp.missing,
  cost: cp.cumulative_cost_usd,
  batches: cp.batch_receipts.length,
  quarantine_cleared: true,
}, null, 2));
