#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { execSync } from 'node:child_process';
import { sha256Json } from '../runs/pilot-assessor-v1.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const PILOT_ROOT = path.resolve(__dirname, '..');
const REPO = path.resolve(PILOT_ROOT, '../../../../../..');

function gitHead() {
  return execSync('git rev-parse --short HEAD', { cwd: REPO, encoding: 'utf8' }).trim();
}

const manifest = JSON.parse(fs.readFileSync(path.join(PILOT_ROOT, 'selection/p0-i-pilot-selection-manifest-v1.json'), 'utf8'));
const lock = JSON.parse(fs.readFileSync(path.join(REPO, 'projects/orca/semantic-intelligence/integration/runtime/config/orca-semantic-contract-runtime-lock-v1.json'), 'utf8'));

const frozenRows = manifest.rows.map((r) => ({
  pilot_run_id: 'p0-i-real-slice-v1',
  pilot_row_id: r.pilot_row_id,
  phrase_id: r.source_query_id,
  raw_query: r.raw_query,
  normalized_query: r.normalized_query,
  provenance: r.provenance,
  intended_sampling_stratum: r.intended_sampling_stratum,
  phrase_origin: r.phrase_origin,
}));

const freeze = {
  freeze_id: 'p0-i-pilot-input-freeze-v1',
  pilot_run_id: 'p0-i-real-slice-v1',
  frozen_at: new Date().toISOString(),
  git_head: gitHead(),
  runtime_commit: gitHead(),
  contract_lock_id: lock.lock_id,
  contract_lock_checksum: sha256Json(lock),
  selection_manifest_checksum: manifest.checksum_sha256,
  selection_script: 'selection/select-pilot-phrases-v1.mjs',
  selection_script_version: 'v1',
  phrase_count: frozenRows.length,
  checksum_sha256: sha256Json({ rows: frozenRows }),
  immutability_note: 'Any phrase change after execution requires P0-I PILOT INPUT VERSION BUMP',
};

const inputDir = path.join(PILOT_ROOT, 'input');
fs.mkdirSync(inputDir, { recursive: true });
fs.writeFileSync(path.join(inputDir, 'p0-i-pilot-input-v1.jsonl'), frozenRows.map((r) => JSON.stringify(r)).join('\n') + '\n', 'utf8');
fs.writeFileSync(path.join(inputDir, 'p0-i-pilot-input-freeze-v1.json'), JSON.stringify(freeze, null, 2) + '\n', 'utf8');

const md = [
  '# P0-I Pilot Input Freeze v1',
  '',
  `**Phrases:** ${freeze.phrase_count}`,
  `**Checksum:** \`${freeze.checksum_sha256}\``,
  `**Git HEAD:** \`${freeze.git_head}\``,
  `**Manifest checksum:** \`${freeze.selection_manifest_checksum}\``,
  '',
  'Immutable after freeze. Version bump required for any phrase change post-execution.',
].join('\n');
fs.writeFileSync(path.join(inputDir, 'P0-I-PILOT-INPUT-FREEZE-v1.md'), md + '\n', 'utf8');

console.log(JSON.stringify({ ok: true, count: freeze.phrase_count, checksum: freeze.checksum_sha256 }, null, 2));
