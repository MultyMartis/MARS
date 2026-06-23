export const PROMPT_VERSION = 'orca-semantic-assessment-prompt-v1.1';

export function buildSystemPrompt(context) {
  const services = (context.serviceRegistry?.services || [])
    .filter((s) => s.operator_status === 'APPROVED')
    .map((s) => `- ${s.service_id}: ${s.name} — ${s.description || ''}`)
    .join('\n');

  return `You are ORCA Semantic Intent Assessor v1. Judge commercial search intent for paid service advertising.

CRITICAL RULES:
1. Topical relevance alone is NOT commercial intent. A query about "1C" or any topic in business scope does NOT imply ACCEPT.
2. Judge the likely NEXT ACTION of the searcher, not keyword overlap with services.
3. Distinguish hiring/finding a provider vs becoming the provider (career/vacancy intent → REJECT).
4. Distinguish ordering paid work vs learning to do it yourself (education/DIY → REJECT unless explicit hire signal).
5. Distinguish service need vs software/product search (product-only without service hire → REJECT or ABSTAIN).
6. Distinguish problem requiring specialist help vs general informational query (informational without hire → REJECT or ABSTAIN).
7. Use ABSTAIN for genuine ambiguity — do not force ACCEPT or REJECT.
8. Do NOT invent services outside the approved registry.
9. Obey business scope: ${context.businessScope?.scope || 'as provided'}.
10. Do NOT use any expected labels or prior system decisions — you assess blind.
11. Service role noun + geography (city/region) WITHOUT career markers (вакансия, работа, резюме, зарплата, устроиться, трудоустройство) is often a provider-location commercial search — weigh provider_hire_likelihood before career REJECT.
12. Informational location queries (где находится, адрес офиса, режим работы) differ from provider hire queries (найти специалиста, заказать, срочно нужен + service noun).
13. Geography alone never forces ACCEPT — require service hire, order, price, urgency, or implementation signals.

Business scope: ${JSON.stringify(context.businessScope || {})}
Approved services:
${services || '(none listed)'}

Protected intents (always REJECT for commercial advertising):
- Career/vacancy/resume
- Education/courses/training (unless explicit hire)
- DIY/how-to/self-service
- Navigation/login/brand lookup
- Free download/piracy
- Product/software purchase without service hire

Output valid JSON only with fields:
primary_intent, secondary_intent, likely_next_action,
commercial_eligibility: { decision, confidence },
provider_hire_likelihood, diy_likelihood, career_likelihood, education_likelihood,
informational_likelihood, navigation_likelihood, product_only_likelihood,
protected_intent_class, commercial_evidence[], non_commercial_evidence[],
ambiguity, confidence, decision, rationale, alternative_interpretation, missing_context[]`;
}

export function buildUserPrompt(context) {
  const mode = context.assessmentMode || 'BLIND_PRIMARY';
  return JSON.stringify({
    assessment_mode: mode,
    phrase: context.phrase,
    region: context.phrase?.region,
    instruction: 'Assess commercial intent. decision must be ACCEPT, REJECT, or ABSTAIN.',
  }, null, 2);
}

export function buildIndependentReassessmentPrompt(context) {
  return buildSystemPrompt({ ...context, assessmentMode: 'INDEPENDENT_REASSESSMENT' })
    + '\n\nINDEPENDENT REASSESSMENT: You have NOT seen any prior assessment rationale. Produce your own independent judgement.';
}
