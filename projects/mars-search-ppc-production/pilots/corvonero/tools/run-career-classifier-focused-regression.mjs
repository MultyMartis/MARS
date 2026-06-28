#!/usr/bin/env node
/**
 * Focused regression for employment vs service-price "работа" distinction.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { classifyPhraseV2 } from './canary-family-classifier-v2.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../../..');
const FIX = path.join(REPO_ROOT, 'projects/orca/semantic-intelligence/live-model/fixtures');
const context = {
  businessScope: JSON.parse(fs.readFileSync(path.join(FIX, 'business-scope-eval-v1.json'), 'utf8')),
  serviceRegistry: JSON.parse(fs.readFileSync(path.join(FIX, 'service-registry-eval-v1.json'), 'utf8')),
};

const FIXTURES = [
  { phrase: 'сколько стоит работа программиста 1с', family: 'direct_commercial_1c_service', verdict: 'ACCEPT', noCareerTag: true },
  { phrase: 'цена работы специалиста 1с', family: 'direct_commercial_1c_service', verdict: 'ACCEPT', noCareerTag: true },
  { phrase: 'стоимость работ по настройке 1с', family: 'direct_commercial_1c_service', verdict: 'ACCEPT', noCareerTag: true },
  { phrase: 'работа программистом 1с', family: 'careers_training_education', verdict: 'REJECT', careerTag: true },
  { phrase: 'программист 1с стажер', family: 'careers_training_education', verdict: 'REJECT', careerTag: true },
  { phrase: 'вакансия программист 1с', family: 'careers_training_education', verdict: 'REJECT', careerTag: true },
  { phrase: 'зарплата программиста 1с', family: 'careers_training_education', verdict: 'REJECT', careerTag: true },
];

let failed = 0;
for (const fx of FIXTURES) {
  const result = classifyPhraseV2({ phrase_id: 'TEST', phrase: fx.phrase }, context);
  const familyOk = result.primary_family === fx.family;
  const verdictOk = result.expected_verdict === fx.verdict;
  const careerTagOk = fx.noCareerTag
    ? !result.observed_tags.includes('career')
    : fx.careerTag
      ? result.observed_tags.includes('career')
      : true;

  if (!familyOk || !verdictOk || !careerTagOk) {
    failed++;
    console.error('FAIL:', fx.phrase, {
      expected: { family: fx.family, verdict: fx.verdict, noCareerTag: fx.noCareerTag, careerTag: fx.careerTag },
      got: {
        family: result.primary_family,
        verdict: result.expected_verdict,
        tags: result.observed_tags,
      },
    });
  }
}

if (failed > 0) {
  console.error(`Focused regression failed: ${failed}/${FIXTURES.length}`);
  process.exit(1);
}
console.log(JSON.stringify({ pass: true, tested: FIXTURES.length }, null, 2));
