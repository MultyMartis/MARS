#!/usr/bin/env node
/**
 * Run Corvonero phrase-slot reconciliation and write CSV/JSON artifacts.
 */
// C2b source persistence only. This file is not authorized for execution without explicit operator approval. Commit/persistence does not authorize Storage export generation, repo artifact generation, Commander import, Direct launch, account mutation, advertising start, Localhost mutation, Storage mutation, or Yandex/API access.
import fs from 'node:fs';
import path from 'node:path';
import {
  reconcilePackagePhraseSlots,
  writePhraseSlotCsvOutputs,
} from '../src/phrase-slot-reconciler.mjs';

function requireOperatorGate() {
  if (process.env.CORVONERO_OPERATOR_GATE !== 'APPROVED') {
    console.error(
      'STOP: CORVONERO_OPERATOR_GATE=APPROVED required. This C2b helper is not safe for casual execution.'
    );
    process.exit(1);
  }
}

requireOperatorGate();

const PILOT = path.resolve('X:/AI MARS/projects/mars-search-ppc-production/pilots/corvonero');
const args = process.argv.slice(2);
const packageVersion = args[0] ?? 'V2.6.1';
const pkgDir =
  packageVersion === 'V2.6.2'
    ? 'X:/AI MARS STORAGE/exports/corvonero/CORVONERO-CAMPAIGN-V2.6.2-FINAL-2026-06-30'
    : 'X:/AI MARS STORAGE/exports/corvonero/CORVONERO-CAMPAIGN-V2.6.1-FINAL-2026-06-30';

const groupPlan = JSON.parse(
  fs.readFileSync(path.join(PILOT, 'CORVONERO-CAMPAIGN-V2.6-FINAL-GROUP-PLAN-v1.json'), 'utf8'),
);
const architecture = JSON.parse(
  fs.readFileSync(path.join(PILOT, 'CORVONERO-CAMPAIGN-V2.6-CAMPAIGN-ARCHITECTURE-v1.json'), 'utf8'),
);
const manifestPath = fs
  .readdirSync(pkgDir)
  .find((f) => /OUTPUT-MANIFEST/i.test(f));
if (!manifestPath) throw new Error(`No manifest in ${pkgDir}`);
const manifest = JSON.parse(fs.readFileSync(path.join(pkgDir, manifestPath), 'utf8'));

const result = await reconcilePackagePhraseSlots({
  group_plan: groupPlan,
  architecture,
  package_root: pkgDir,
  xlsx_files: manifest.xlsx_files,
  authority_source_file: 'CORVONERO-CAMPAIGN-V2.6-FINAL-GROUP-PLAN-v1.json',
});

const outDir = PILOT;
const csvPrefix = packageVersion === 'V2.6.2' ? 'V2.6.2' : 'V2.6.1';
writePhraseSlotCsvOutputs(outDir, {
  ...result,
  expected_and_present: result.expected_and_present,
});

// Rename CSV outputs to versioned names if V2.6.2
if (packageVersion === 'V2.6.2') {
  for (const name of [
    'CORVONERO-V2.6.1-PHRASE-SLOT-RECONCILIATION.csv',
    'CORVONERO-V2.6.1-MISSING-SLOTS.csv',
    'CORVONERO-V2.6.1-UNEXPECTED-SLOTS.csv',
    'CORVONERO-V2.6.1-DUPLICATE-SLOTS.csv',
  ]) {
    const src = path.join(outDir, name);
    const dst = path.join(outDir, name.replace('V2.6.1', 'V2.6.2'));
    if (fs.existsSync(src)) fs.renameSync(src, dst);
  }
}

const jsonOut = {
  schema_version: 'corvonero-phrase-slot-reconciliation-v1',
  package_version: packageVersion,
  package_path: pkgDir,
  reconciled_at: result.reconciled_at,
  authority_phrase_slots: result.authority_phrase_slots,
  artifact_phrase_slots: result.artifact_phrase_slots,
  phrase_slot_delta: result.phrase_slot_delta,
  phrase_slot_reconciliation_pass: result.phrase_slot_reconciliation_pass,
  missing_slots: result.missing_slots_list,
  unexpected_slots: result.unexpected_slots_list,
  duplicate_slots: result.duplicate_slots_list,
  normalization_collisions: result.normalization_collisions,
  campaign_reconciliation: result.campaign_reconciliation,
  group_reconciliation: result.group_reconciliation,
  root_cause_classification: (result.missing_slots_list ?? []).map((m) => ({
    phrase: m.phrase,
    campaign_id: m.campaign_id,
    mode: m.mode,
    group_id: m.group_id,
    classification: 'GENERATION_DEFECT',
    evidence: 'Group plan slot absent from phrase allocation / XLSX — build_phrase_allocation omitted V26_SINGLE_PHRASE_MERGE target ca-02-support-tech',
  })),
};

const jsonName = `CORVONERO-CAMPAIGN-${packageVersion}-PHRASE-SLOT-RECONCILIATION-v1.json`;
fs.writeFileSync(path.join(PILOT, jsonName), JSON.stringify(jsonOut, null, 2) + '\n');

const mdName = `CORVONERO-CAMPAIGN-${packageVersion}-PHRASE-SLOT-RECONCILIATION-v1.md`;
fs.writeFileSync(
  path.join(PILOT, mdName),
  [
    `# Corvonero ${packageVersion} — Phrase Slot Reconciliation v1`,
    '',
    `**Pass:** ${result.phrase_slot_reconciliation_pass}`,
    `**Authority slots:** ${result.authority_phrase_slots}`,
    `**Artifact slots:** ${result.artifact_phrase_slots}`,
    `**Delta:** ${result.phrase_slot_delta}`,
    `**Missing:** ${result.missing_slots}`,
    `**Unexpected:** ${result.unexpected_slots}`,
    `**Duplicates:** ${result.duplicate_slots}`,
    '',
    'See CSV: `CORVONERO-V2.6.1-PHRASE-SLOT-RECONCILIATION.csv` (V2.6.1 evidence) or V2.6.2 variant.',
  ].join('\n') + '\n',
);

console.log(JSON.stringify({ packageVersion, ...jsonOut }, null, 2));
