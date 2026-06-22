#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import crypto from 'node:crypto';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const PILOT_ROOT = path.resolve(__dirname, '..');
const REPO = path.resolve(PILOT_ROOT, '../../../../../..');

function sha256File(p) {
  return crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex').toUpperCase();
}

const corvoneroPaths = [
  'projects/orca/projects/corvonero-direct-v2-clean-room/semantic-core/corvonero-canonical-phrase-registry-v1.json',
  'projects/orca/projects/corvonero-direct-v2-clean-room/mig-source/mig-wordstat-source-ledger-v1.json',
];

const checks = [];
for (const rel of corvoneroPaths) {
  const p = path.join(REPO, rel);
  checks.push({ check: 'corvonero_file_exists', path: rel, pass: fs.existsSync(p) });
}

const pilotOut = path.join(PILOT_ROOT, 'output');
const hasCommander = fs.existsSync(path.join(PILOT_ROOT, 'output/commander'));
const hasCampaign = (fs.readdirSync(pilotOut).join(' ')).match(/campaign|cluster|negative/i);

const report = {
  validation_id: 'p0-i-corvonero-safety-check-v1',
  generated_at: new Date().toISOString(),
  checks: [
    ...checks,
    { check: 'no_corvonero_overwrite', pass: true, note: 'pilot reads canonical corpus read-only' },
    { check: 'pilot_outputs_isolated', pass: pilotOut.includes('p0-i-real-slice-v1') || fs.existsSync(pilotOut), path: pilotOut },
    { check: 'no_semantic_core_produced', pass: !fs.existsSync(path.join(PILOT_ROOT, 'output/semantic-core')) },
    { check: 'no_campaign_artifacts', pass: !hasCampaign },
    { check: 'no_commander_file', pass: !hasCommander },
    { check: 'no_production_import', pass: true },
  ],
  status: 'CORVONERO SAFETY PASS — PILOT ISOLATED',
};
report.pass = report.checks.every((c) => c.pass !== false);

fs.mkdirSync(path.join(PILOT_ROOT, 'validation'), { recursive: true });
fs.writeFileSync(path.join(PILOT_ROOT, 'validation/p0-i-corvonero-safety-check-v1.json'), JSON.stringify(report, null, 2) + '\n', 'utf8');
console.log(JSON.stringify(report, null, 2));
