#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { adjudicateSemanticIntent } from '../adjudication/semantic-adjudicator.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const FIX = path.join(__dirname, '../supplementary/regression/under-admission-regression-v1.json');

let passed = 0;
let failed = 0;

function assert(name, cond) {
  if (cond) { passed++; console.log(`  [PASS] ${name}`); }
  else { failed++; console.log(`  [FAIL] ${name}`); }
}

// Adjudicator unit: geo-commercial disagreement resolution
const geoCommercial = adjudicateSemanticIntent({
  assessmentA: {
    decision: 'ACCEPT',
    confidence: 0.85,
    provider_hire_likelihood: 0.8,
    career_likelihood: 0.2,
    commercial_evidence: ['service_role_plus_geo'],
    rationale: 'Provider hire in Moscow for 1C specialist',
  },
  assessmentB: {
    decision: 'REJECT',
    confidence: 0.7,
    career_likelihood: 0.6,
    rationale: 'Could be job search',
  },
  hardRuleEvidence: { blocked: false },
  serviceRegistry: { services: [] },
});
assert('geo commercial disagreement resolves to ACCEPT', geoCommercial.final_decision === 'ACCEPT');

// Career marker should block geo resolution
const careerGeo = adjudicateSemanticIntent({
  assessmentA: {
    decision: 'ACCEPT', confidence: 0.8, provider_hire_likelihood: 0.7, career_likelihood: 0.3,
    commercial_evidence: ['x'], rationale: 'hire',
  },
  assessmentB: {
    decision: 'REJECT', confidence: 0.8, career_likelihood: 0.9,
    rationale: 'вакансия программист 1с москва',
  },
  hardRuleEvidence: { blocked: false },
  serviceRegistry: { services: [] },
});
assert('career markers keep REJECT on disagreement', careerGeo.final_decision === 'REJECT');

// Geography alone — no commercial evidence
const geoOnly = adjudicateSemanticIntent({
  assessmentA: { decision: 'ACCEPT', confidence: 0.6, commercial_evidence: [], rationale: 'москва' },
  assessmentB: { decision: 'REJECT', confidence: 0.7, rationale: 'navigation' },
  hardRuleEvidence: { blocked: false },
  serviceRegistry: { services: [] },
});
assert('no commercial evidence — reject wins', geoOnly.final_decision === 'REJECT');

const fixture = JSON.parse(fs.readFileSync(FIX, 'utf8'));
assert('fixture lists 4 false reject ids', fixture.false_reject_cases.length === 4);
assert('adversarial geography negatives present', fixture.adversarial_geography_negatives.length >= 4);

console.log(`Under-admission regression: ${passed}/${passed + failed}`);
process.exit(failed ? 1 : 0);
