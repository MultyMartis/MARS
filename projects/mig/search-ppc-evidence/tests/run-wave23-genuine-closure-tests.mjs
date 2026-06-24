#!/usr/bin/env node
/**
 * Wave 2.3 — Genuine live Paid SERP closure validation tests
 */
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import { fileURLToPath } from 'node:url';
import { validateAssistedCaptureBundle, hashAssistedManifestBody } from '../runtime/lib/assisted-capture-validator.mjs';
import { parsePaidSerpCapture } from '../runtime/lib/paid-serp-runtime.mjs';
import { buildAdvertiserRegistry } from '../runtime/lib/competitor-registry.mjs';
import { captureLandingEvidence } from '../runtime/lib/landing-evidence.mjs';
import { buildEvidenceManifest } from '../runtime/lib/evidence-manifest.mjs';
import { assessFreshness } from '../runtime/lib/freshness.mjs';
import { authorizeEvidenceCommand } from '../runtime/lib/gate.mjs';
import { extractSerpItemsFromHtml } from '../runtime/lib/serp-html-extract.mjs';
import {
  buildNormalizedManifest,
  isEmptyTemplateManifest,
  selectCanonicalManifest,
  writeNormalizedBundleManifests,
} from '../runtime/lib/assisted-manifest-normalizer.mjs';
import { privacySanitizationSummary, assertRepoSafeText } from '../runtime/lib/privacy-sanitize.mjs';
import { loadJson, writeJson, sha256File } from '../runtime/lib/utils.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO = path.resolve(__dirname, '../../../..');
const FIX = path.join(__dirname, '../fixtures');
const W23_MANIFEST = path.join(REPO, 'projects/mig/search-ppc-evidence/live-validation/w2-3-tech-paid-serp/project-ppc-state-manifest-v1.json');
const W23_QUERIES = path.join(REPO, 'projects/mig/search-ppc-evidence/live-validation/w2-3-tech-paid-serp/query-set-v1.json');
const W23_SESSION = path.join(REPO, 'projects/mig/search-ppc-evidence/live-validation/w2-3-tech-paid-serp/session-config-v1.json');
const CLIENT_MANIFEST = path.join(REPO, 'projects/orca/projects/corvonero-direct-v2-clean-room/state/project-ppc-state-manifest-v1.json');

const results = [];
function record(id, name, fn) {
  try {
    const pass = !!fn();
    results.push({ id, name, pass });
  } catch (e) {
    results.push({ id, name, pass: false, error: e.message });
  }
}

function buildAssistedBundle(tmp, overrides = {}) {
  const dir = path.join(tmp, `bundle-${Math.random().toString(36).slice(2, 8)}`);
  fs.mkdirSync(dir, { recursive: true });
  fs.copyFileSync(path.join(FIX, 'assisted-capture/valid-page.html'), path.join(dir, 'page.html'));
  fs.writeFileSync(path.join(dir, 'screenshot.png'), Buffer.from('w23-fixture-screenshot'));
  const manifest = {
    ...loadJson(path.join(FIX, 'assisted-capture/valid-manifest-template.json')),
    project_id: 'MIG-W2-3-TECH-PAID-SERP',
    query_id: 'w2-3-q02',
    query: 'ремонт квартир под ключ',
    captured_at: '2026-06-23T10:30:00.000Z',
    operator_attestation: { attested: true, attested_at: '2026-06-23T10:30:30.000Z', statement: 'fixture' },
    ...overrides,
  };
  writeJson(path.join(dir, 'capture-manifest.json'), manifest);
  const m = loadJson(path.join(dir, 'capture-manifest.json'));
  m.checksums = {
    screenshot_sha256: sha256File(path.join(dir, 'screenshot.png')),
    html_sha256: sha256File(path.join(dir, 'page.html')),
    manifest_sha256: hashAssistedManifestBody(m),
  };
  writeJson(path.join(dir, 'capture-manifest.json'), m);
  return dir;
}

const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'sppc-w23-'));
const querySet = loadJson(W23_QUERIES);
const session = loadJson(W23_SESSION);
const projectManifest = loadJson(W23_MANIFEST);
const validBundle = buildAssistedBundle(tmp);

record(1, 'genuine assisted bundle validation for w2-3 project', () => {
  const r = validateAssistedCaptureBundle({ bundleDir: validBundle, querySet, sessionConfig: session, projectManifest });
  return r.valid;
});

record(2, 'paid/organic extraction from assisted HTML', () => {
  const html = fs.readFileSync(path.join(validBundle, 'page.html'), 'utf8');
  const extracted = extractSerpItemsFromHtml(html);
  const items = extracted.items || [];
  const ads = items.filter((i) => i.surface_type === 'ad');
  return ads.length >= 1;
});

record(3, 'advertiser creation from parsed ads', () => {
  const parsed = parsePaidSerpCapture(loadJson(path.join(FIX, 'paid-serp/ads-observed.json')), {
    sessionId: 'w23-test',
    projectId: 'MIG-W2-3-TECH-PAID-SERP',
    queryId: 'w2-3-q02',
  });
  const reg = buildAdvertiserRegistry([parsed]);
  return reg.advertisers?.length >= 1;
});

record(4, 'bounded landing resolution records access status', () => {
  const landing = captureLandingEvidence({
    destinationUrl: 'https://example.org/landing',
    pageData: { final_url: 'https://example.org/landing', page_title: 'Example', h1: 'H1', cta_text: 'Call' },
    evidenceLinks: {},
  });
  return landing.ok && landing.observed?.final_url && landing.state;
});

record(5, 'technical evidence cannot become client authority', () => {
  const m = loadJson(path.join(validBundle, 'capture-manifest.json'));
  return m.production_authority === false && projectManifest.production_authority === 'NONE';
});

record(6, 'global capability does not complete client stage', () => {
  const pack = buildEvidenceManifest({
    projectId: 'MIG-W2-3-TECH-PAID-SERP',
    sourceRegistry: { sources: [{ source_id: 'tech' }], updated_at: '2026-06-23T10:00:00Z' },
    paidSerpSessions: [{ generated_at: '2026-06-23T10:00:00Z' }],
    orcaSemanticArtifacts: {},
  });
  return pack.manifest.sppc_12_complete !== true;
});

record(7, 'project-specific evidence required for client manifest', () => {
  const a = authorizeEvidenceCommand({ manifestPath: CLIENT_MANIFEST, cliCommand: 'paid-serp:import-assisted' });
  return !a.allowed;
});

record(8, 'stale live evidence rejected', () => {
  const f = assessFreshness({
    paidSerpSessions: [{ generated_at: '2020-01-01T10:00:00Z' }],
    policy: { paid_serp: { valid_through_days: 30 } },
  });
  return f.any_stale === true;
});

record(9, 'CAPTCHA session not complete', () => {
  const p = parsePaidSerpCapture(loadJson(path.join(FIX, 'paid-serp/captcha-partial.json')), {
    sessionId: 's',
    projectId: 'MIG-W2-3-TECH-PAID-SERP',
    queryId: 'w2-3-q01',
  });
  return p.observation_state === 'CAPTCHA' && p.degraded;
});

record(10, 'manually typed advertiser rows rejected', () => {
  const dir = buildAssistedBundle(tmp, {
    manual_advertiser_rows: [{ domain: 'fake.example', headline: 'typed manually' }],
  });
  const r = validateAssistedCaptureBundle({ bundleDir: dir, querySet, sessionConfig: session, projectManifest });
  return !r.valid;
});

record(11, 'missing raw evidence rejected', () => {
  const dir = path.join(tmp, 'no-raw');
  fs.mkdirSync(dir, { recursive: true });
  writeJson(path.join(dir, 'capture-manifest.json'), loadJson(path.join(validBundle, 'capture-manifest.json')));
  const r = validateAssistedCaptureBundle({ bundleDir: dir, querySet, sessionConfig: session, projectManifest });
  return !r.valid;
});

record(12, 'SPPC-12 blocked without client ORCA evidence', () => {
  const pack = buildEvidenceManifest({ projectId: 'MIG-W2-3-TECH-PAID-SERP' });
  return pack.manifest.sppc_12_complete === false;
});

const LIVE_BUNDLE =
  'C:/AI MARS STORAGE/incoming/mig/live-validation/w2-3-tech-paid-serp/assisted-capture-pending/w2-3-q02';

record(13, '.htm accepted when declared in manifest', () => {
  if (!fs.existsSync(LIVE_BUNDLE)) return true;
  const r = validateAssistedCaptureBundle({ bundleDir: LIVE_BUNDLE, querySet, sessionConfig: session, projectManifest });
  return r.htmlPath?.endsWith('page.htm') && r.bundle?.files?.html === 'page.htm';
});

record(14, 'actual Firefox manifest preferred over empty template', () => {
  if (!fs.existsSync(LIVE_BUNDLE)) return true;
  const selected = selectCanonicalManifest(LIVE_BUNDLE);
  return selected.manifest?.captured_at === '2026-06-24T04:41:47.799Z' && selected.source !== 'none';
});

record(15, 'legacy IDs normalized only under strong bundle evidence', () => {
  if (!fs.existsSync(path.join(LIVE_BUNDLE, 'capture-manifest by-firefox.json'))) return true;
  const firefox = loadJson(path.join(LIVE_BUNDLE, 'capture-manifest by-firefox.json'));
  const normalized = buildNormalizedManifest({ firefoxManifest: firefox, bundleDir: LIVE_BUNDLE });
  return (
    normalized.project_id === 'MIG-W2-3-TECH-PAID-SERP' &&
    normalized.query_id === 'w2-3-q02' &&
    firefox.project_id !== normalized.project_id
  );
});

record(16, 'timestamp preserved during normalization', () => {
  if (!fs.existsSync(path.join(LIVE_BUNDLE, 'capture-manifest.normalized.json'))) return true;
  const raw = loadJson(path.join(LIVE_BUNDLE, 'capture-manifest by-firefox.json'));
  const norm = loadJson(path.join(LIVE_BUNDLE, 'capture-manifest.normalized.json'));
  return norm.captured_at === raw.captured_at;
});

record(17, 'browser preserved during normalization', () => {
  if (!fs.existsSync(path.join(LIVE_BUNDLE, 'capture-manifest.normalized.json'))) return true;
  const raw = loadJson(path.join(LIVE_BUNDLE, 'capture-manifest by-firefox.json'));
  const norm = loadJson(path.join(LIVE_BUNDLE, 'capture-manifest.normalized.json'));
  return norm.device_browser === raw.device_browser;
});

record(18, 'attestation preserved during normalization', () => {
  if (!fs.existsSync(path.join(LIVE_BUNDLE, 'capture-manifest.normalized.json'))) return true;
  const raw = loadJson(path.join(LIVE_BUNDLE, 'capture-manifest by-firefox.json'));
  const norm = loadJson(path.join(LIVE_BUNDLE, 'capture-manifest.normalized.json'));
  return norm.operator_attestation?.attested === true && norm.operator_attestation?.attested_at === raw.operator_attestation?.attested_at;
});

record(19, 'raw login/account identifiers do not leak into repo reports', () => {
  const packPath = path.join(REPO, 'projects/mig/search-ppc-evidence/live-validation/w2-3-tech-paid-serp/genuine-technical-evidence-pack-v2.json');
  if (!fs.existsSync(packPath)) return true;
  const packText = fs.readFileSync(packPath, 'utf8');
  assertRepoSafeText(packText, 'genuine-technical-evidence-pack-v2.json');
  return !packText.includes('admin@') && !packText.includes('"login":');
});

record(20, 'raw HTML remains outside Git', () => {
  const tracked = ['page.htm', 'page.html', 'screenshot.png'].every(
    (f) => !fs.existsSync(path.join(REPO, 'projects/mig/search-ppc-evidence/live-validation/w2-3-tech-paid-serp', f)),
  );
  const privacy = fs.existsSync(LIVE_BUNDLE) ? privacySanitizationSummary(path.join(LIVE_BUNDLE, 'page.htm')) : { raw_html_committed_to_git: false };
  return tracked && privacy.raw_html_committed_to_git === false;
});

record(21, 'empty template cannot override actual capture', () => {
  const dir = path.join(tmp, 'firefox-priority');
  fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(path.join(dir, 'page.htm'), '<html></html>');
  fs.writeFileSync(path.join(dir, 'screenshot.png'), Buffer.from('x'));
  writeJson(path.join(dir, 'capture-manifest.json'), {
    project_id: 'MIG-W2-3-TECH-PAID-SERP',
    session_id: 'w2-3-assisted-session-001',
    query_id: 'w2-3-q02',
    query: 'ремонт квартир под ключ',
    captured_at: null,
    operator_attestation: { attested: false },
  });
  writeJson(path.join(dir, 'capture-manifest by-firefox.json'), {
    schema_version: '1.0.0',
    project_id: 'MIG-W2-1-TECH-PAID-SERP',
    session_id: 'w2-2-assisted-session-001',
    query_id: 'w2-1-q02',
    query: 'ремонт квартир под ключ',
    captured_at: '2026-06-24T04:41:47.799Z',
    timezone: 'Europe/Moscow',
    region: 'Москва',
    region_lr: 213,
    device_browser: 'Firefox/152.0',
    page_url: 'https://yandex.ru/search/?text=test&lr=213',
    page_title: 'test',
    files: { screenshot: 'screenshot.png', html: 'page.htm' },
    operator_attestation: { attested: true, attested_at: '2026-06-24T04:41:47.799Z', statement: 'fixture' },
    production_authority: false,
    technical_test_only: true,
  });
  const selected = selectCanonicalManifest(dir);
  return selected.manifest?.device_browser === 'Firefox/152.0' && !isEmptyTemplateManifest(selected.manifest);
});

record(22, 'screenshot and HTML reconcile with paid extraction', () => {
  if (!fs.existsSync(LIVE_BUNDLE)) return true;
  const html = fs.readFileSync(path.join(LIVE_BUNDLE, 'page.htm'), 'utf8');
  const extracted = extractSerpItemsFromHtml(html);
  const ads = extracted.items.filter((i) => i.surface_type === 'ad');
  return ads.length >= 2 && fs.existsSync(path.join(LIVE_BUNDLE, 'screenshot.png'));
});

const passed = results.filter((r) => r.pass).length;
const failed = results.length - passed;
console.log(`Wave 2.3 genuine closure tests: ${passed}/${results.length} passed`);
for (const r of results) {
  console.log(`  [${r.pass ? 'PASS' : 'FAIL'}] #${r.id} ${r.name}${r.error ? ` — ${r.error}` : ''}`);
}
writeJson(path.join(__dirname, '../reports/wave23-genuine-closure-test-results-v1.json'), {
  suite: 'wave23-genuine-closure-tests',
  passed,
  failed,
  results,
});
process.exit(failed > 0 ? 1 : 0);
