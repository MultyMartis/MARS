import fs from 'node:fs';
import { readJson, resolveRepo, stablePhraseId, BLOCKERS } from './lib.mjs';

export function loadProductionInputs(manifest) {
  const artifacts = manifest.artifact_registry || {};
  const corpusPath = resolveRepo(artifacts.canonical_phrase_registry?.path
    || artifacts.full_semantic_corpus_intake?.path);
  const scopePath = resolveRepo(artifacts.business_scope_operator_authority?.path);
  const servicePath = resolveRepo(artifacts.service_registry?.path);

  if (!fs.existsSync(corpusPath)) {
    throw new Error(`canonical registry not found: ${corpusPath}`);
  }

  const corpus = readJson(corpusPath);
  const phrases = corpus.phrases || corpus.records || corpus.entries || [];
  const expectedCount = manifest.source_registry?.expected_row_count
    || artifacts.canonical_phrase_registry?.registered_row_count
    || phrases.length;

  if (phrases.length !== expectedCount) {
    throw new Error(`${BLOCKERS.COUNT_MISMATCH}: expected ${expectedCount}, got ${phrases.length}`);
  }

  const businessScope = fs.existsSync(scopePath) ? readJson(scopePath) : {};
  let serviceRegistry = null;
  if (servicePath && fs.existsSync(servicePath)) {
    serviceRegistry = readJson(servicePath);
  }

  const normalized = phrases.map((p, i) => normalizePhraseEntry(p, i));

  return {
    corpus,
    phrases: normalized,
    expectedCount,
    businessScope,
    serviceRegistry,
    serviceRegistryPath: servicePath,
    corpusPath,
  };
}

function normalizePhraseEntry(p, index) {
  const raw = p.raw_query || p.phrase || p.query || String(p);
  const normalized = p.normalized_query || raw.toLowerCase().trim();
  return {
    phrase_id: p.phrase_id || p.id || stablePhraseId(normalized, p.source_id || 'corpus'),
    raw_query: raw,
    normalized_query: normalized,
    source_ids: p.source_ids || [p.source_id || 'unknown'],
    frequencies: p.frequencies || { total: p.frequency || p.freq || null },
    region: p.region || null,
    collection_period: p.collection_period || null,
    source_metadata: p.source_metadata || {},
    index,
  };
}

export function loadCorpusFromFixture(fixturePath) {
  const data = readJson(fixturePath);
  const phrases = (data.phrases || []).map((p, i) => normalizePhraseEntry(p, i));
  return {
    corpus: data,
    phrases,
    expectedCount: data.expected_count || phrases.length,
    businessScope: data.business_scope || {},
    serviceRegistry: data.service_registry || null,
  };
}
