#!/usr/bin/env node
/**
 * P0-I pilot phrase selection v1 — stratified sampling from Corvonero canonical corpus.
 * Does NOT use old semantic decisions as truth.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { classifyStratum, seededShuffle, sha256Json } from '../runs/pilot-assessor-v1.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const PILOT_ROOT = path.resolve(__dirname, '..');
const REPO = path.resolve(PILOT_ROOT, '../../../../../..');

const CANONICAL = path.join(REPO, 'projects/orca/projects/corvonero-direct-v2-clean-room/semantic-core/corvonero-canonical-phrase-registry-v1.json');
const LEDGER = path.join(REPO, 'projects/orca/projects/corvonero-direct-v2-clean-room/mig-source/mig-wordstat-source-ledger-v1.json');
const FIXTURE_DIR = path.join(REPO, 'projects/orca/semantic-intelligence/integration/runtime/fixtures/integration');

const TARGET = 200;
const SEED = 'p0-i-real-slice-v1-20260622';

const FALLBACKS = {
  commercial_support_recovery: ['ambiguous_problem_query', 'commercial_explicit_service_request'],
  commercial_quote_price_contact: ['commercial_explicit_service_request'],
  protected_diy_howto: ['ambiguous_provider_vs_diy', 'protected_education'],
  protected_regulatory: ['ambiguous_unknown', 'ambiguous_product_vs_service'],
  protected_navigational_login: ['protected_documentation_download_free', 'ambiguous_unknown'],
  ambiguous_short_head: ['ambiguous_unknown', 'ambiguous_product_vs_service'],
  ambiguous_support_vs_info: ['ambiguous_problem_query', 'ambiguous_product_vs_service'],
  ambiguous_career_vs_provider: ['protected_career', 'commercial_explicit_service_request'],
  ambiguous_provider_vs_diy: ['protected_diy_howto', 'commercial_explicit_service_request'],
  ambiguous_malformed_noise: ['ambiguous_unknown'],
};

const QUOTAS = {
  commercial_explicit_service_request: 18,
  commercial_implementation_configuration: 18,
  commercial_modification_integration: 18,
  commercial_support_recovery: 18,
  commercial_quote_price_contact: 18,
  protected_career: 10,
  protected_education: 10,
  protected_diy_howto: 10,
  protected_regulatory: 10,
  protected_navigational_login: 10,
  protected_documentation_download_free: 10,
  ambiguous_short_head: 8,
  ambiguous_problem_query: 8,
  ambiguous_product_vs_service: 8,
  ambiguous_support_vs_info: 4,
  ambiguous_career_vs_provider: 4,
  ambiguous_provider_vs_diy: 4,
  ambiguous_malformed_noise: 4,
  ambiguous_unknown: 10,
};

function readJson(p) {
  return JSON.parse(fs.readFileSync(p, 'utf8'));
}

function ledgerByRowId(ledger) {
  const m = new Map();
  for (const row of ledger.rows) m.set(row.ledger_row_id, row);
  return m;
}

function buildPools(phrases) {
  const pools = Object.fromEntries(Object.keys(QUOTAS).map((k) => [k, []]));
  for (const ph of phrases) {
    const stratum = classifyStratum(ph.normalized_phrase || ph.phrase);
    if (pools[stratum]) pools[stratum].push(ph);
    else pools.ambiguous_unknown.push(ph);
  }
  return pools;
}

function pickFromPool(pool, n, usedPhrases, seedKey) {
  const available = pool.filter((p) => !usedPhrases.has(p.normalized_phrase));
  const shuffled = seededShuffle(available, `${SEED}:${seedKey}`);
  return shuffled.slice(0, n);
}

function loadSyntheticFixtures() {
  const out = [];
  for (const sub of ['positive', 'negative']) {
    const dir = path.join(FIXTURE_DIR, sub);
    if (!fs.existsSync(dir)) continue;
    for (const f of fs.readdirSync(dir).filter((x) => x.endsWith('.json'))) {
      const fx = readJson(path.join(dir, f));
      const inp = fx.input || fx;
      if (!inp.raw_query) continue;
      out.push({
        phrase_id: `SYN-${f.replace('.json', '')}`,
        phrase: inp.raw_query,
        normalized_phrase: inp.normalized_query || inp.raw_query,
        source_variants: [inp.raw_query],
        source_row_ids: [],
        combined_frequency: null,
        provenance: [`integration-fixture:${f}`],
        synthetic: true,
        fixture_id: fx.fixture_id,
      });
    }
  }
  return out;
}

function main() {
  const canonical = readJson(CANONICAL);
  const ledger = readJson(LEDGER);
  const ledgerMap = ledgerByRowId(ledger);
  const pools = buildPools(canonical.phrases);
  const used = new Set();
  const selected = [];
  let rowNum = 0;

  for (const [stratum, quota] of Object.entries(QUOTAS)) {
    let picks = pickFromPool(pools[stratum] || [], quota, used, stratum);
    if (picks.length < quota) {
      for (const fb of FALLBACKS[stratum] || []) {
        if (picks.length >= quota) break;
        const more = pickFromPool(pools[fb] || [], quota - picks.length, used, `${stratum}:${fb}`);
        picks = picks.concat(more);
      }
    }
    for (const ph of picks) {
      used.add(ph.normalized_phrase);
      const rowId = ph.source_row_ids?.[0];
      const led = rowId ? ledgerMap.get(rowId) : null;
      rowNum++;
      selected.push({
        pilot_row_id: `P0I-${String(rowNum).padStart(5, '0')}`,
        source_query_id: ph.phrase_id,
        raw_query: ph.phrase,
        normalized_query: ph.normalized_phrase,
        source_path: 'projects/orca/projects/corvonero-direct-v2-clean-room/semantic-core/corvonero-canonical-phrase-registry-v1.json',
        source_row_reference: ph.phrase_id,
        provenance: {
          status: 'COMPLETE',
          source_type: 'corvonero-canonical-corpus',
          ledger_row_id: rowId || null,
          mig_provenance: ph.provenance?.[0] || null,
          source_file: led?.source_file || null,
          source_sheet: led?.source_sheet || null,
          source_row: led?.source_row || null,
        },
        frequency_evidence: {
          combined_frequency: ph.combined_frequency ?? null,
          max_frequency: ph.max_frequency ?? null,
        },
        intended_sampling_stratum: stratum,
        phrase_origin: 'natural',
        selection_reason: `stratified_quota:${stratum}`,
        leakage_group: `corvonero-v1-canonical:${ph.phrase_id}`,
      });
    }
  }

  // Final fill to TARGET from any unused canonical phrases
  if (selected.length < TARGET) {
    const remaining = seededShuffle(
      canonical.phrases.filter((p) => !used.has(p.normalized_phrase)),
      `${SEED}:fill`,
    );
    for (const ph of remaining) {
      if (selected.length >= TARGET) break;
      used.add(ph.normalized_phrase);
      const rowId = ph.source_row_ids?.[0];
      const led = rowId ? ledgerMap.get(rowId) : null;
      rowNum++;
      const stratum = classifyStratum(ph.normalized_phrase);
      selected.push({
        pilot_row_id: `P0I-${String(rowNum).padStart(5, '0')}`,
        source_query_id: ph.phrase_id,
        raw_query: ph.phrase,
        normalized_query: ph.normalized_phrase,
        source_path: 'projects/orca/projects/corvonero-direct-v2-clean-room/semantic-core/corvonero-canonical-phrase-registry-v1.json',
        source_row_reference: ph.phrase_id,
        provenance: {
          status: 'COMPLETE',
          source_type: 'corvonero-canonical-corpus',
          ledger_row_id: rowId || null,
          mig_provenance: ph.provenance?.[0] || null,
          source_file: led?.source_file || null,
          source_sheet: led?.source_sheet || null,
          source_row: led?.source_row || null,
        },
        frequency_evidence: {
          combined_frequency: ph.combined_frequency ?? null,
          max_frequency: ph.max_frequency ?? null,
        },
        intended_sampling_stratum: stratum,
        phrase_origin: 'natural',
        selection_reason: 'quota_backfill:general_pool',
        leakage_group: `corvonero-v1-canonical:${ph.phrase_id}`,
      });
    }
  }

  // Supplement if still under target from synthetic fixtures
  if (selected.length < TARGET) {
    const synthetics = loadSyntheticFixtures();
    for (const ph of seededShuffle(synthetics, SEED)) {
      if (selected.length >= TARGET) break;
      if (used.has(ph.normalized_phrase)) continue;
      used.add(ph.normalized_phrase);
      rowNum++;
      selected.push({
        pilot_row_id: `P0I-${String(rowNum).padStart(5, '0')}`,
        source_query_id: ph.phrase_id,
        raw_query: ph.phrase,
        normalized_query: ph.normalized_phrase,
        source_path: `integration/runtime/fixtures/integration`,
        source_row_reference: ph.fixture_id,
        provenance: { status: 'COMPLETE', source_type: 'integration-fixture', references: ph.provenance },
        frequency_evidence: null,
        intended_sampling_stratum: classifyStratum(ph.normalized_phrase),
        phrase_origin: 'synthetic',
        selection_reason: 'supplementary_fixture_coverage',
        leakage_group: `fixture:${ph.fixture_id}`,
      });
    }
  }

  const manifest = {
    manifest_id: 'p0-i-pilot-selection-manifest-v1',
    pilot_run_id: 'p0-i-real-slice-v1',
    generated_at: new Date().toISOString(),
    selection_seed: SEED,
    target_count: TARGET,
    actual_count: selected.length,
    unique_phrases: new Set(selected.map((r) => r.normalized_query)).size,
    checksum_sha256: null,
    rows: selected,
  };
  manifest.checksum_sha256 = sha256Json({ rows: selected });

  const selDir = path.join(PILOT_ROOT, 'selection');
  fs.mkdirSync(selDir, { recursive: true });
  fs.writeFileSync(path.join(selDir, 'p0-i-pilot-selection-manifest-v1.json'), JSON.stringify(manifest, null, 2) + '\n', 'utf8');

  const strataCounts = {};
  for (const r of selected) strataCounts[r.intended_sampling_stratum] = (strataCounts[r.intended_sampling_stratum] || 0) + 1;

  const md = [
    '# P0-I Pilot Selection Manifest v1',
    '',
    `**Pilot run:** p0-i-real-slice-v1`,
    `**Selected:** ${selected.length} phrases`,
    `**Unique:** ${manifest.unique_phrases}`,
    `**Checksum:** \`${manifest.checksum_sha256}\``,
    `**Seed:** \`${SEED}\``,
    '',
    '## Stratum distribution',
    '',
    ...Object.entries(strataCounts).sort((a, b) => b[1] - a[1]).map(([k, v]) => `- ${k}: ${v}`),
    '',
    '## Forbidden fields',
    '',
    'No primary intent truth, eligibility truth, expected decision, or gold labels.',
  ].join('\n');
  fs.writeFileSync(path.join(selDir, 'P0-I-PILOT-SELECTION-MANIFEST-v1.md'), md + '\n', 'utf8');

  console.log(JSON.stringify({
    ok: selected.length >= 180 && selected.length <= 220,
    count: selected.length,
    unique: manifest.unique_phrases,
    checksum: manifest.checksum_sha256,
    manifest: path.join(selDir, 'p0-i-pilot-selection-manifest-v1.json'),
  }, null, 2));
}

main();
