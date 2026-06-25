#!/usr/bin/env node
/** Wave 3.1F geo false-reject closed regression — 16 V1 known failures. */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { adjudicateSemanticIntent } from '../adjudication/semantic-adjudicator.mjs';
import { applyHardRules } from '../../production/assessors/hard-rules.mjs';
import { extractServiceIntentEvidence } from '../evidence/service-intent-evidence.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ANALYSIS = path.join(__dirname, '../supplementary/regression/geo-commercial-error-analysis-v1.json');
const OUT = path.join(__dirname, '../reports', `geo-false-reject-regression-${Date.now()}`);

const FALSE_REJECT_PHRASES = [
  { id: 'CFM-GEO-PRV-06', q: 'программист bitrix москва' },
  { id: 'CFM-GEO-PRV-08', q: 'программист bitrix новосибирск' },
  { id: 'CFM-GEO-PRV-09', q: 'программист bitrix казань' },
  { id: 'CFM-GEO-PRV-13', q: 'программист bitrix новосибирск' },
  { id: 'CFM-GEO-ORD-01', q: 'цена настройки sap москва' },
  { id: 'CFM-GEO-ORD-02', q: 'цена настройки sap санкт-петербург' },
  { id: 'CFM-GEO-ORD-03', q: 'цена настройки sap нижний новгород' },
  { id: 'CFM-GEO-ORD-04', q: 'цена настройки sap москва' },
  { id: 'CFM-GEO-ORD-05', q: 'цена настройки sap санкт-петербург' },
  { id: 'CFM-GEO-ORD-06', q: 'цена настройки sap нижний новгород' },
  { id: 'CFM-GEO-ORD-07', q: 'цена настройки sap москва' },
  { id: 'CFM-GEO-ORD-08', q: 'цена настройки sap санкт-петербург' },
  { id: 'CFM-GEO-ORD-09', q: 'цена настройки sap нижний новгород' },
  { id: 'CFM-GEO-ORD-10', q: 'цена настройки sap москва' },
  { id: 'CFM-GEO-ORD-11', q: 'цена настройки sap санкт-петербург' },
  { id: 'CFM-GEO-ORD-12', q: 'цена настройки sap нижний новгород' },
];

function simulatePreRepairAdj(phrase, structured) {
  return adjudicateSemanticIntent({
    assessmentA: { decision: 'REJECT', confidence: 0.9, career_likelihood: 0.3, provider_hire_likelihood: 0.3, commercial_evidence: [], rationale: 'out of scope product' },
    assessmentB: { decision: 'REJECT', confidence: 0.85, career_likelihood: 0.2, provider_hire_likelihood: 0.25, commercial_evidence: [], rationale: 'not in registry' },
    hardRuleEvidence: { blocked: false },
    serviceRegistry: { services: [{ service_id: 'svc-hire', name: '1C' }] },
    phrase: { raw_query: phrase, normalized_query: phrase.toLowerCase() },
    structuredEvidence: null,
  });
}

const results = [];
for (const c of FALSE_REJECT_PHRASES) {
  const phrase = { raw_query: c.q, normalized_query: c.q.toLowerCase() };
  const structured = extractServiceIntentEvidence(phrase);
  const hardRules = applyHardRules(phrase, { decision: 'REJECT' });
  const adj = adjudicateSemanticIntent({
    assessmentA: { decision: 'REJECT', confidence: 0.9, career_likelihood: 0.2, provider_hire_likelihood: 0.3, commercial_evidence: [], rationale: 'scope' },
    assessmentB: { decision: 'REJECT', confidence: 0.85, career_likelihood: 0.15, provider_hire_likelihood: 0.25, commercial_evidence: [], rationale: 'registry' },
    hardRuleEvidence: hardRules,
    serviceRegistry: { services: [{ service_id: 'svc-hire', name: '1C' }] },
    phrase,
    structuredEvidence: structured,
  });
  results.push({
    record_id: c.id,
    phrase: c.q,
    expected: 'ACCEPT',
    final: adj.final_decision,
    scope_fit: adj.scope_fit,
    ownership: adj.ownership,
    strong_commercial_geo: structured.strong_commercial_geo,
    fixed: adj.final_decision === 'ACCEPT',
  });
}

const fixed = results.filter((r) => r.fixed).length;
const summary = {
  total: results.length,
  fixed_count: fixed,
  remaining_false_reject: results.length - fixed,
  results,
  analysis_source: ANALYSIS,
};
fs.mkdirSync(OUT, { recursive: true });
fs.writeFileSync(path.join(OUT, 'geo-false-reject-regression-v1.json'), JSON.stringify(summary, null, 2));
console.log(`Geo false-reject regression: ${fixed}/${results.length} fixed`);
process.exit(fixed === results.length ? 0 : 1);
