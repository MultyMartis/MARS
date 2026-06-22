#!/usr/bin/env node
/**
 * MIG Search PPC Evidence — Fixture Test Suite (Wave 2)
 */
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import { fileURLToPath } from 'node:url';
import { registerSource } from '../runtime/lib/source-registry.mjs';
import { intakeCorpus } from '../runtime/lib/corpus-intake.mjs';
import { normalizeCorpus, detectSemanticRewriting } from '../runtime/lib/canonical-registry.mjs';
import { validateBusinessHoursWindow } from '../runtime/lib/business-hours.mjs';
import { runPaidSerpSession, parsePaidSerpCapture } from '../runtime/lib/paid-serp-runtime.mjs';
import { buildAdvertiserRegistry, assessAdvertiserMerge } from '../runtime/lib/competitor-registry.mjs';
import { captureLandingEvidence } from '../runtime/lib/landing-evidence.mjs';
import { buildEvidenceManifest } from '../runtime/lib/evidence-manifest.mjs';
import { buildDegradedRecord, assessFreshness } from '../runtime/lib/freshness.mjs';
import { loadJson, writeJson, nowIso } from '../runtime/lib/utils.mjs';
import { authorizeEvidenceCommand } from '../runtime/lib/gate.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const FIX = path.join(__dirname, '../fixtures');
const REPO = path.resolve(__dirname, '../../../..');
const MANIFEST = path.join(REPO, 'projects/mars-search-ppc-production/runtime/fixtures/example-valid-manifest-v2.json');
const CORVONERO = path.join(REPO, 'projects/orca/projects/corvonero-direct-v2-clean-room/state/project-ppc-state-manifest-v1.json');

const results = [];

function record(id, name, fn) {
  try {
    const r = fn();
    results.push({ id, name, pass: !!r.pass, ...r });
  } catch (e) {
    results.push({ id, name, pass: false, error: e.message });
  }
}

const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'sppc-w2-'));

record(1, 'valid source registration', () => {
  const reg = path.join(tmp, 'registry-1.json');
  const src = loadJson(path.join(FIX, 'source-valid.json'));
  src.source_path = path.join(REPO, src.source_path);
  const r = registerSource({ registryPath: reg, record: src });
  return { pass: r.ok };
});

record(2, 'source missing collection date blocked', () => {
  const reg = path.join(tmp, 'registry-2.json');
  const r = registerSource({ registryPath: reg, record: loadJson(path.join(FIX, 'source-missing-date.json')) });
  return { pass: !r.ok && /missing collection date/i.test(r.message || '') };
});

record(3, 'corpus count reconciliation pass', () => {
  const src = loadJson(path.join(FIX, 'source-valid.json'));
  src.source_path = path.join(REPO, src.source_path);
  const r = intakeCorpus({ sources: [src], outputDir: path.join(tmp, 'corpus-pass') });
  return { pass: r.ok && r.report.counts_reconcile };
});

record(4, 'corpus count mismatch blocked', () => {
  const bad = {
    source_id: 'bad',
    source_path: path.join(REPO, 'projects/mig/search-ppc-evidence/fixtures/corpus/keywords-mismatch.csv'),
    raw_row_count: 99,
  };
  const r = intakeCorpus({ sources: [bad], outputDir: path.join(tmp, 'corpus-fail') });
  return { pass: !r.ok };
});

record(5, 'duplicate aggregation preserving provenance', () => {
  const rows = {
    rows: [
      { raw_phrase: 'тест фраза', source_id: 'a', source_row: 1, frequency: 10 },
      { raw_phrase: 'тест фраза', source_id: 'b', source_row: 2, frequency: 20 },
    ],
  };
  const corpusPath = path.join(tmp, 'dup-corpus.json');
  writeJson(corpusPath, rows);
  const r = normalizeCorpus({ corpusPath, outputDir: path.join(tmp, 'dup-out'), region: 'msk' });
  const reg = loadJson(r.registry_path);
  return { pass: r.ok && reg.entries[0].source_ids.length === 2 };
});

record(6, 'semantic rewriting detection', () => {
  const d = detectSemanticRewriting('купить станок чпу', 'станок чпу');
  return { pass: d.rewritten && d.removed_modifiers.includes('купить') };
});

record(7, 'paid SERP within approved window', () => {
  const s = loadJson(path.join(FIX, 'paid-serp/session-within-window.json'));
  const r = validateBusinessHoursWindow({
    projectTimezone: s.timezone,
    currentTimestamp: s.current_timestamp,
    observationWindows: s.allowed_local_collection_windows,
    weekdayPolicy: s.weekday_policy,
  });
  return { pass: r.allowed && r.status === 'WITHIN APPROVED BUSINESS-HOURS WINDOW' };
});

record(8, 'paid SERP outside window blocked', () => {
  const s = loadJson(path.join(FIX, 'paid-serp/session-outside-window.json'));
  const r = validateBusinessHoursWindow({
    projectTimezone: s.timezone,
    currentTimestamp: s.current_timestamp,
    observationWindows: s.allowed_local_collection_windows,
  });
  return { pass: !r.allowed && r.status === 'OUTSIDE APPROVED WINDOW' };
});

record(9, 'timezone missing blocked', () => {
  const r = validateBusinessHoursWindow({ projectTimezone: null, observationWindows: [{ start: '09:00', end: '18:00' }] });
  return { pass: !r.allowed && r.status === 'TIMEZONE UNRESOLVED' };
});

record(10, 'CAPTCHA partial session degraded', () => {
  const serp = loadJson(path.join(FIX, 'paid-serp/captcha-partial.json'));
  const p = parsePaidSerpCapture(serp, { sessionId: 't', projectId: 'p', queryId: 'q' });
  return { pass: p.degraded && p.observation_state === 'CAPTCHA' };
});

record(11, 'no ads observed explicit state', () => {
  const serp = loadJson(path.join(FIX, 'paid-serp/no-ads.json'));
  const p = parsePaidSerpCapture(serp, { sessionId: 't', projectId: 'p', queryId: 'q' });
  return { pass: p.observation_state === 'NO ADS OBSERVED' && p.no_ads_scope?.note };
});

record(12, 'ads observed structured evidence', () => {
  const serp = loadJson(path.join(FIX, 'paid-serp/ads-observed.json'));
  const p = parsePaidSerpCapture(serp, { sessionId: 't', projectId: 'p', queryId: 'q' });
  return { pass: p.ads.length >= 2 && p.ads[0].headline && p.organic_kept_separate };
});

record(13, 'advertiser deduplication safe case', () => {
  const serp = loadJson(path.join(FIX, 'paid-serp/ads-observed.json'));
  const p = parsePaidSerpCapture(serp, { sessionId: 't', projectId: 'p', queryId: 'q' });
  const reg = buildAdvertiserRegistry([p]);
  return { pass: reg.advertisers.length >= 1 && reg.domains.length >= 1 };
});

record(14, 'advertiser ambiguous merge unresolved', () => {
  const rel = assessAdvertiserMerge('Brand A', 'Brand A', 'a.ru', 'b.ru');
  return { pass: rel === 'unresolved' };
});

record(15, 'landing evidence partial', () => {
  const r = captureLandingEvidence({ destinationUrl: 'https://example.ru', pageData: { final_url: 'https://example.ru' } });
  return { pass: r.ok && r.state === 'PARTIAL' };
});

record(16, 'degraded collection without approval', () => {
  const d = buildDegradedRecord({
    completedQueries: ['q1'],
    incompleteQueries: ['q2'],
    reason: 'CAPTCHA',
    evidence: {},
    impact: 'partial',
    retryRecommendation: 'retry later',
    operatorApprovalRequired: true,
  });
  return { pass: d.operator_approval_required === true };
});

record(17, 'evidence pack partial readiness', () => {
  const r = buildEvidenceManifest({
    projectId: 'T',
    manifestPath: MANIFEST,
    sourceRegistry: { sources: [{ source_id: 'x' }], updated_at: nowIso() },
    rawCorpus: { final_raw_corpus_count: 0 },
    canonicalRegistry: null,
    paidSerpSessions: [],
    competitorPack: null,
    orcaSemanticArtifacts: {},
    freshnessPolicy: {},
  });
  return { pass: ['MIG EVIDENCE PARTIAL', 'MIG EVIDENCE BLOCKED'].includes(r.readiness) };
});

record(18, 'stale evidence detection', () => {
  const old = new Date();
  old.setDate(old.getDate() - 30);
  const f = assessFreshness({
    paidSerpSessions: [{ generated_at: old.toISOString() }],
    policy: { paid_serp: { valid_through_days: 7 } },
  });
  return { pass: f.any_stale };
});

record(19, 'synthetic source cannot be production authority', () => {
  const reg = path.join(tmp, 'registry-syn.json');
  const r = registerSource({
    registryPath: reg,
    record: {
      source_id: 'syn',
      project_id: 'T',
      source_class: 'SYNTHETIC / TEST',
      source_title: 't',
      source_path: '/x',
      collection_start: '2026-01-01',
      collection_end: '2026-01-01',
      imported_at: '2026-01-01',
      region: 'r',
      timezone: 'UTC',
      collection_method: 'test',
      tool_runtime_version: 'v1',
      operator_tool: 'test',
      raw_row_count: 1,
      content_checksum: 'x',
      limitations: [],
      use_authority: 'production',
      status: 'REGISTERED',
      related_lifecycle_stage: 'SPPC-02',
    },
  });
  return { pass: !r.ok };
});

record(20, 'frozen project collection blocked via gate', () => {
  const auth = authorizeEvidenceCommand({
    manifestPath: CORVONERO,
    cliCommand: 'paid-serp:run',
  });
  return { pass: !auth.allowed };
});

const passed = results.filter((r) => r.pass).length;
const report = { suite: 'wave2-fixtures', passed, failed: results.length - passed, total: results.length, results };
writeJson(path.join(__dirname, '../reports/fixture-test-results-v1.json'), report);

for (const r of results) {
  console.log(`  [${r.pass ? 'PASS' : 'FAIL'}] #${r.id} ${r.name}`);
}
console.log(`Fixture tests: ${passed}/${results.length} passed`);
process.exit(passed === results.length ? 0 : 1);
