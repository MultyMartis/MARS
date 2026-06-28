#!/usr/bin/env node
/**
 * Focused regression suite for canary-family-classifier-v2.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { classifyPhraseV2, EXPECTATION_STATUS } from './canary-family-classifier-v2.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../../..');
const FIX = path.join(REPO_ROOT, 'projects/orca/semantic-intelligence/live-model/fixtures');
const context = {
  businessScope: JSON.parse(fs.readFileSync(path.join(FIX, 'business-scope-eval-v1.json'), 'utf8')),
  serviceRegistry: JSON.parse(fs.readFileSync(path.join(FIX, 'service-registry-eval-v1.json'), 'utf8')),
};

const FIXTURES = [
  { phrase: 'собеседование 1с программиста', family: 'careers_training_education', verdict: 'REJECT' },
  { phrase: 'работа программистом 1с', family: 'careers_training_education', verdict: 'REJECT' },
  { phrase: 'зарплата программиста 1с', family: 'careers_training_education', verdict: 'REJECT' },
  { phrase: 'вакансии программист 1с', family: 'careers_training_education', verdict: 'REJECT' },
  { phrase: 'как стать программистом 1с', family: 'careers_training_education', verdict: 'REJECT' },
  { phrase: 'курсы программиста 1с', family: 'careers_training_education', verdict: 'REJECT' },
  { phrase: 'обучение разработке 1с', family: 'careers_training_education', verdict: 'REJECT' },
  { phrase: 'сертификация 1с программиста', family: 'careers_training_education', verdict: 'REJECT', allowReview: true },
  { phrase: 'что делает программист 1с', family: 'informational_self_service', verdict: 'REJECT' },
  { phrase: 'как работает интеграция 1с', family: 'integrations', verdict: null, allowReview: true },
  { phrase: 'инструкция по обновлению 1с', family: 'informational_self_service', verdict: 'REJECT' },
  { phrase: 'нужен программист 1с', family: 'direct_commercial_1c_service', verdict: 'ACCEPT' },
  { phrase: 'заказать доработку 1с', family: 'direct_commercial_1c_service', verdict: 'ACCEPT' },
  { phrase: 'стоимость сопровождения 1с', family: 'direct_commercial_1c_service', verdict: 'ACCEPT' },
  { phrase: 'исправить ошибку 1с специалист', family: 'direct_commercial_1c_service', verdict: 'ACCEPT' },
  { phrase: 'программист 1с', family: 'ambiguous_mixed_intent', verdict: null, allowReview: true },
  { phrase: 'обновление 1с', family: 'ambiguous_mixed_intent', verdict: null, allowReview: true },
  { phrase: 'купить 1с с настройкой', family: 'ambiguous_mixed_intent', verdict: null, allowReview: true },
  { phrase: 'что делать если 1с не работает', family: 'problem_troubleshooting', verdict: 'ABSTAIN', allowReview: false },
];

let failed = 0;
for (const fx of FIXTURES) {
  const result = classifyPhraseV2({ phrase_id: 'TEST', phrase: fx.phrase }, context);
  const familyOk = fx.family === null || result.primary_family === fx.family;
  const verdictOk = fx.verdict === null
    ? (fx.allowReview ? result.review_required || result.expectation_status === EXPECTATION_STATUS.REVIEW_REQUIRED : result.expected_verdict === null)
    : result.expected_verdict === fx.verdict;
  const careerEducationReject = !result.observed_tags.includes('career') || result.expected_verdict !== 'ACCEPT';
  const educationReject = !result.observed_tags.includes('education') || result.expected_verdict !== 'ACCEPT';

  if (!familyOk || !verdictOk || !careerEducationReject || !educationReject) {
    failed++;
    console.error('FAIL:', fx.phrase, {
      expected: { family: fx.family, verdict: fx.verdict },
      got: {
        family: result.primary_family,
        verdict: result.expected_verdict,
        status: result.expectation_status,
        tags: result.observed_tags,
      },
    });
  }
}

if (failed > 0) {
  console.error(`Regression failed: ${failed}/${FIXTURES.length}`);
  process.exit(1);
}
console.log(JSON.stringify({ pass: true, tested: FIXTURES.length }, null, 2));
