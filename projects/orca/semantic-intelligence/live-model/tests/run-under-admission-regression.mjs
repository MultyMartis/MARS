#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { adjudicateSemanticIntent } from '../adjudication/semantic-adjudicator.mjs';
import { applyHardRules } from '../../production/assessors/hard-rules.mjs';
import { extractServiceIntentEvidence } from '../evidence/service-intent-evidence.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const FIX = path.join(__dirname, '../supplementary/regression/under-admission-regression-v1.json');
const PSFIX = path.join(__dirname, '../supplementary/regression/product-service-regression-v1.json');

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

// Product/service adjudicator: boxed delivery false accept resolved
const productBox = adjudicateSemanticIntent({
  assessmentA: {
    decision: 'ACCEPT', confidence: 0.9, product_only_likelihood: 0.85, provider_hire_likelihood: 0.3,
    commercial_evidence: ['topic match'], rationale: 'коробочная поставка 1с бухгалтерия',
  },
  assessmentB: {
    decision: 'REJECT', confidence: 0.85, product_only_likelihood: 0.9,
    rationale: 'product license purchase not service hire',
  },
  hardRuleEvidence: { blocked: false },
  serviceRegistry: { services: [] },
});
assert('product boxed delivery disagreement resolves to REJECT', productBox.final_decision === 'REJECT');

// Service contrast must not be blocked
const servicePair = adjudicateSemanticIntent({
  assessmentA: {
    decision: 'ACCEPT', confidence: 0.9, provider_hire_likelihood: 0.85, product_only_likelihood: 0.1,
    commercial_evidence: ['implementation under key'], rationale: 'внедрение 1с под ключ',
  },
  assessmentB: { decision: 'ACCEPT', confidence: 0.88, provider_hire_likelihood: 0.9, commercial_evidence: ['service'] },
  hardRuleEvidence: { blocked: false },
  serviceRegistry: { services: [] },
});
assert('service contrast stays ACCEPT', servicePair.final_decision === 'ACCEPT');

// Hard rule: product acquisition blocks ACCEPT
const hardProduct = applyHardRules(
  { raw_query: 'купить коробочную 1с', normalized_query: 'купить коробочную 1с' },
  { decision: 'ACCEPT' },
);
assert('hard rule blocks product-only ACCEPT', hardProduct.blocked && hardProduct.override_decision === 'REJECT');

// Hard rule: service bundled passes
const hardService = applyHardRules(
  { raw_query: 'поставка и внедрение 1с', normalized_query: 'поставка и внедрение 1с' },
  { decision: 'ACCEPT' },
);
assert('hard rule allows service bundled supply', !hardService.blocked);

const psFixture = JSON.parse(fs.readFileSync(PSFIX, 'utf8'));
assert('product regression minimal pairs count', psFixture.minimal_pairs.length === 8);
assert('boxed regression ids tracked', psFixture.boxed_delivery_regression_ids.length === 2);

// Wave 3.1F: structured geo commercial override on agree-REJECT
const structuredGeo = adjudicateSemanticIntent({
  assessmentA: { decision: 'REJECT', confidence: 0.9, commercial_evidence: [], rationale: 'sap not in registry' },
  assessmentB: { decision: 'REJECT', confidence: 0.85, commercial_evidence: [], rationale: 'out of scope' },
  hardRuleEvidence: { blocked: false },
  serviceRegistry: { services: [{ service_id: 'svc-hire', name: '1C' }] },
  phrase: { raw_query: 'цена настройки sap москва', normalized_query: 'цена настройки sap москва' },
});
assert('price+service+geo agree-REJECT overridden to ACCEPT', structuredGeo.final_decision === 'ACCEPT');
assert('out-of-scope commercial has scope_fit OUT_OF_SCOPE', structuredGeo.scope_fit === 'OUT_OF_SCOPE');

// Bare error abstain
const bareError = applyHardRules(
  { raw_query: 'ошибка 0x80004005 1с', normalized_query: 'ошибка 0x80004005 1с' },
  { decision: 'REJECT' },
);
assert('bare error hard rule forces ABSTAIN not REJECT', bareError.override_decision === 'ABSTAIN');

const bareAdj = adjudicateSemanticIntent({
  assessmentA: { decision: 'REJECT', confidence: 0.7, rationale: 'error' },
  assessmentB: null,
  hardRuleEvidence: bareError,
  serviceRegistry: { services: [] },
  phrase: { raw_query: 'ошибка 0x80004005 1с', normalized_query: 'ошибка 0x80004005 1с' },
});
assert('bare error adjudicator yields ABSTAIN', bareAdj.final_decision === 'ABSTAIN');

// Provider noun + geo
const prvEvidence = extractServiceIntentEvidence({ raw_query: 'программист bitrix москва', normalized_query: 'программист bitrix москва' });
assert('provider+geo strong commercial evidence', prvEvidence.strong_commercial_geo === true);

// Wave 3.1F repair: product version update blocks ACCEPT
const sapUpdateHard = applyHardRules(
  { raw_query: 'обновление sap business one до новой версии', normalized_query: 'обновление sap business one до новой версии' },
  { decision: 'ACCEPT' },
  { businessScope: { scope: '1c_services' }, serviceRegistry: { services: [] } },
);
assert('product version update hard rule blocks ACCEPT', sapUpdateHard.blocked && sapUpdateHard.override_decision === 'REJECT');

const sapUpdateAdj = adjudicateSemanticIntent({
  assessmentA: { decision: 'ACCEPT', confidence: 0.78, commercial_evidence: ['update service'], rationale: 'update request' },
  assessmentB: { decision: 'ACCEPT', confidence: 0.76, commercial_evidence: ['update'], rationale: 'version update' },
  hardRuleEvidence: sapUpdateHard,
  serviceRegistry: { services: [{ service_id: 'svc-hire', name: '1C' }] },
  phrase: { raw_query: 'обновление sap business one до новой версии', normalized_query: 'обновление sap business one до новой версии' },
});
assert('product version update adjudicator yields REJECT', sapUpdateAdj.final_decision === 'REJECT');

// Wave 3.1F repair: ambiguous DIY problem → ABSTAIN not REJECT
const diyErrorHard = applyHardRules(
  { raw_query: 'как исправить ошибку 0x80004005 1с', normalized_query: 'как исправить ошибку 0x80004005 1с' },
  { decision: 'REJECT' },
);
assert('ambiguous DIY error hard rule forces ABSTAIN', diyErrorHard.override_decision === 'ABSTAIN');

const diyErrorAdj = adjudicateSemanticIntent({
  assessmentA: { decision: 'REJECT', confidence: 0.7, rationale: 'diy how-to' },
  assessmentB: null,
  hardRuleEvidence: diyErrorHard,
  serviceRegistry: { services: [] },
  phrase: { raw_query: 'как исправить ошибку 0x80004005 1с', normalized_query: 'как исправить ошибку 0x80004005 1с' },
});
assert('ambiguous DIY error adjudicator yields ABSTAIN', diyErrorAdj.final_decision === 'ABSTAIN');

// Wave 3.1F repair v2: generic ERP platform family → ABSTAIN
const genericErpHard = applyHardRules(
  { raw_query: 'обновление erp до новой версии', normalized_query: 'обновление erp до новой версии' },
  { decision: 'REJECT' },
  { businessScope: { scope: '1c_services' }, serviceRegistry: { services: [] } },
);
assert('generic ERP hard rule forces ABSTAIN', genericErpHard.override_decision === 'ABSTAIN');

const genericErpAdj = adjudicateSemanticIntent({
  assessmentA: { decision: 'REJECT', confidence: 0.7, rationale: 'erp update' },
  assessmentB: null,
  hardRuleEvidence: genericErpHard,
  serviceRegistry: { services: [] },
  businessScope: { scope: '1c_services' },
  phrase: { raw_query: 'обновление erp до новой версии', normalized_query: 'обновление erp до новой версии' },
});
assert('generic ERP adjudicator yields ABSTAIN', genericErpAdj.final_decision === 'ABSTAIN');

// Service update with specialist remains admissible
const svcUpdateEvidence = extractServiceIntentEvidence({ raw_query: 'специалист обновить конфигурацию 1с', normalized_query: 'специалист обновить конфигурацию 1с' });
assert('service update with specialist has service scope', svcUpdateEvidence.service_update_intent || svcUpdateEvidence.provider_noun_detected);

console.log(`Under-admission regression: ${passed}/${passed + failed}`);
process.exit(failed ? 1 : 0);
