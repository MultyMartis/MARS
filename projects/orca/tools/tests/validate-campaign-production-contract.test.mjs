#!/usr/bin/env node

/**

 * Regression tests for ORCA Campaign Production Contract validator.

 */

import fs from 'node:fs';

import path from 'node:path';

import { fileURLToPath } from 'node:url';

import { validateCampaignProductionContract } from '../validate-campaign-production-contract.mjs';



const __dirname = path.dirname(fileURLToPath(import.meta.url));

const FIXTURES = path.join(__dirname, '..', 'fixtures', 'campaign-contract');



function load(name) {

  return JSON.parse(fs.readFileSync(path.join(FIXTURES, name), 'utf8'));

}



function runFixture(fixture, meta = {}) {

  return validateCampaignProductionContract({

    operator_service_scope: fixture.operator_service_scope,

    protected_seed_registry: fixture.protected_seed_registry,

    production_dataset: fixture.production_dataset,

    controlled_test_registry: fixture.controlled_test_registry,

    ad_registry: fixture.ad_registry,
    group_registry: fixture.group_registry || { groups: [] },
    collision_validation: fixture.collision_validation,

    negative_validation: fixture.negative_validation,

    project_meta: meta,

  });

}



let failed = 0;



function assert(cond, msg) {

  if (!cond) {

    console.error('FAIL:', msg);

    failed++;

  } else {

    console.log('OK:', msg);

  }

}



const triumph = load('triumph-success-minimal-v1.json');

const triumphResult = runFixture(triumph);

assert(triumphResult.gate_decision.startsWith('PASS'), 'Triumph minimal fixture should PASS');

assert(triumphResult.summary.critical_violations === 0, 'Triumph minimal: zero critical');



const corvFail = load('corvonero-v6-failure-patterns-v1.json');

const corvResult = runFixture(corvFail);

assert(corvResult.gate_decision.startsWith('BLOCKED'), 'Corvonero v6 failure fixture should BLOCK');

assert(corvResult.summary.critical_violations > 0, 'Corvonero v6 failure: has critical violations');



const seedLoss = JSON.parse(JSON.stringify(corvFail));

seedLoss.production_dataset.groups[0].viability_status = 'ACTIVE';

seedLoss.production_dataset.groups[0].export_to_xlsx = true;

seedLoss.production_dataset.keywords = [];

const seedLossResult = runFixture(seedLoss);

assert(seedLossResult.summary.critical_violations >= 2, 'Seed loss + empty group triggers critical');



const staleHold = load('authority-stale-hold-v1.json');

const staleHoldResult = runFixture(staleHold);

assert(

  staleHoldResult.gate_decision === 'BLOCKED — OPERATOR SCOPE AUTHORITY STILL INCONSISTENT',

  'Stale HOLD authority with ACTIVE production blocks export'

);

assert(staleHoldResult.summary.authority_drift_violations >= 1, 'Stale HOLD: authority drift detected');



const activeMissing = load('authority-active-missing-production-v1.json');

const activeMissingResult = runFixture(activeMissing);

assert(

  activeMissingResult.gate_decision.includes('BLOCKED'),

  'ACTIVE authority with missing production blocks'

);

assert(activeMissingResult.summary.critical_violations >= 1, 'Missing production group is critical');



const matched = load('authority-matched-v1.json');

const matchedResult = runFixture(matched, { authority_synchronized: true });

assert(

  matchedResult.gate_decision.includes('AUTHORITY SYNCHRONIZED'),

  'Matched authority with sync flag uses synchronized PASS message'

);

assert(matchedResult.summary.authority_drift_violations === 0, 'Matched authority: zero drift');



const narrowOptional = load('authority-narrow-optional-v1.json');

const narrowResult = runFixture(narrowOptional);

assert(narrowResult.gate_decision.startsWith('PASS'), 'MAY BE NARROW optional service PASS');

assert(narrowResult.summary.authority_drift_violations === 0, 'Narrow optional: zero drift');



const unauthorized = load('unauthorized-production-service-v1.json');

const unauthorizedResult = runFixture(unauthorized);

assert(

  unauthorizedResult.gate_decision === 'BLOCKED — OPERATOR SCOPE AUTHORITY STILL INCONSISTENT',

  'Unauthorized production group blocks export'

);

assert(

  unauthorizedResult.authority_drift_violations.some((v) => v.invariant_id === 'INV-SCOPE-03'),

  'Unauthorized group triggers INV-SCOPE-03'

);



console.log(failed ? `\n${failed} test(s) failed` : '\nAll contract validator regression tests passed');

process.exit(failed ? 1 : 0);

