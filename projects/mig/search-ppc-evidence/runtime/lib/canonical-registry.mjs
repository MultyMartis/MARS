import path from 'node:path';
import { loadJson, writeJson, normalizeQuery, stablePhraseId, sha256Text, nowIso } from './utils.mjs';

const PROHIBITED_OPS = ['semantic_rewrite', 'modifier_removal_untraced', 'intent_merge_untraced', 'frequency_invention'];

export function normalizeCorpus({ corpusPath, outputDir, region, collectionPeriod }) {
  const corpus = loadJson(corpusPath);
  const entries = [];
  const duplicateGroups = new Map();
  const violations = [];

  for (const row of corpus.rows || []) {
    const raw = row.raw_phrase;
    const normalized = normalizeQuery(raw);
    const phraseId = stablePhraseId(normalized, region || '');
    const normKey = `${normalized}|${region || ''}`;

    if (row.normalization_operations?.some((op) => PROHIBITED_OPS.includes(op))) {
      violations.push({ phrase: raw, issue: 'prohibited normalization operation' });
    }
    if (row.frequency != null && row.frequency_invented === true) {
      violations.push({ phrase: raw, issue: 'invented frequency' });
    }

    if (!duplicateGroups.has(normKey)) {
      duplicateGroups.set(normKey, []);
    }
    duplicateGroups.get(normKey).push(row);

    entries.push({
      phrase_id: phraseId,
      raw_query: raw,
      normalized_query: normalized,
      source_ids: [row.source_id],
      source_row_references: [`${row.source_id}:${row.source_row}`],
      frequency: row.frequency ?? null,
      frequency_type: row.frequency != null ? 'source_provided' : 'missing',
      region: region || null,
      collection_period: collectionPeriod || null,
      duplicate_group: normKey,
      normalization_operations: ['nfc_lowercase_collapse_whitespace'],
      exclusion_status: row.excluded ? 'excluded' : 'included',
      exclusion_reason: row.exclusion_reason || null,
      checksum: sha256Text(`${raw}|${normalized}|${row.frequency}`),
    });
  }

  if (violations.length) {
    return { ok: false, blockers: violations.map((v) => `semantic violation: ${v.phrase}`), violations };
  }

  const merged = [];
  const seen = new Map();
  for (const e of entries) {
    if (seen.has(e.duplicate_group)) {
      const existing = seen.get(e.duplicate_group);
      existing.source_ids = [...new Set([...existing.source_ids, ...e.source_ids])];
      existing.source_row_references = [...existing.source_row_references, ...e.source_row_references];
      if (e.frequency != null && existing.frequency == null) existing.frequency = e.frequency;
      continue;
    }
    seen.set(e.duplicate_group, e);
    merged.push(e);
  }

  const registry = {
    schema_version: '1.0.0',
    generated_at: nowIso(),
    entry_count: merged.length,
    entries: merged,
    checksum: sha256Text(JSON.stringify(merged)),
  };

  writeJson(path.join(outputDir, 'canonical-registry.json'), registry);
  return { ok: true, registry_path: path.join(outputDir, 'canonical-registry.json'), entry_count: merged.length };
}

export function detectSemanticRewriting(before, after) {
  const b = normalizeQuery(before);
  const a = normalizeQuery(after);
  if (b === a) return { rewritten: false };
  const tokensB = new Set(b.split(' '));
  const tokensA = new Set(a.split(' '));
  const removed = [...tokensB].filter((t) => !tokensA.has(t));
  const added = [...tokensA].filter((t) => !tokensB.has(t));
  return {
    rewritten: removed.length > 0 || added.length > 0,
    removed_modifiers: removed,
    added_tokens: added,
  };
}
