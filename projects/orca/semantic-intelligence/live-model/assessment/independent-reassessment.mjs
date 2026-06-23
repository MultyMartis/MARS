/**
 * Independent second assessment — must not see first model decision/rationale.
 */
import { assessSemanticIntent, assertBlindInputSeparation } from '../adapters/model-adapter-interface.mjs';
import { buildIndependentReassessmentPrompt, PROMPT_VERSION } from '../contracts/prompt-contract.mjs';

export const INDEPENDENCE_LEVELS = {
  DIFFERENT_PROVIDER: 'DIFFERENT_PROVIDER',
  DIFFERENT_MODEL: 'DIFFERENT_MODEL',
  SAME_MODEL_INDEPENDENT_CONTEXT: 'SAME_MODEL — INDEPENDENT CONTEXT',
  RULE_ONLY_SUPPORT: 'RULE-ONLY SUPPORT',
  NOT_INDEPENDENT: 'NOT INDEPENDENT',
};

export async function runIndependentReassessment(params) {
  const {
    phrase,
    businessScope,
    serviceRegistry,
    taxonomy,
    commercialPolicy,
    protectedIntentPolicy,
    primaryAdapter,
    secondaryAdapter = null,
    hardRuleEvidence = null,
  } = params;

  const forbidden = {
    primary_decision: params.primaryDecision,
    primary_rationale: params.primaryRationale,
    expected_label: params.expectedLabel,
  };
  const separation = assertBlindInputSeparation(forbidden);
  if (!separation.blind) {
    return { ok: false, blocker: 'REASSESSMENT_LEAKAGE', leaks: separation.leaks };
  }

  let adapter = secondaryAdapter;
  let independenceLevel = INDEPENDENCE_LEVELS.NOT_INDEPENDENT;

  if (secondaryAdapter && primaryAdapter) {
    if (secondaryAdapter.provider !== primaryAdapter.provider) {
      independenceLevel = INDEPENDENCE_LEVELS.DIFFERENT_PROVIDER;
    } else if (secondaryAdapter.modelId !== primaryAdapter.modelId) {
      independenceLevel = INDEPENDENCE_LEVELS.DIFFERENT_MODEL;
    } else {
      independenceLevel = INDEPENDENCE_LEVELS.SAME_MODEL_INDEPENDENT_CONTEXT;
    }
  } else if (primaryAdapter && !secondaryAdapter) {
    adapter = createIndependentContextAdapter(primaryAdapter);
    independenceLevel = INDEPENDENCE_LEVELS.SAME_MODEL_INDEPENDENT_CONTEXT;
  } else if (!adapter && hardRuleEvidence) {
    return {
      ok: true,
      output: ruleOnlySupportAssessment(hardRuleEvidence),
      independence_level: INDEPENDENCE_LEVELS.RULE_ONLY_SUPPORT,
      assessment_role: 'PRIMARY_B',
      note: 'Deterministic rules as evidence only — not independent semantic judge',
    };
  }

  if (!adapter) {
    return { ok: false, blocker: 'NO_INDEPENDENT_ASSESSOR', errors: ['secondary adapter unavailable'] };
  }

  const result = await assessSemanticIntent({
    phrase,
    businessScope,
    serviceRegistry,
    taxonomy,
    commercialPolicy,
    protectedIntentPolicy,
    assessmentMode: 'INDEPENDENT_REASSESSMENT',
    adapter,
  });

  if (!result.ok) return result;

  result.output.blind_assessment = true;
  result.independence_level = independenceLevel;
  result.assessment_role = 'PRIMARY_B';

  return result;
}

function createIndependentContextAdapter(baseAdapter) {
  return {
    ...baseAdapter,
    async assess(context) {
      const independentContext = {
        ...context,
        assessmentMode: 'INDEPENDENT_REASSESSMENT',
        _independent_prompt: buildIndependentReassessmentPrompt(context),
      };
      return baseAdapter.assess(independentContext);
    },
  };
}

function ruleOnlySupportAssessment(hardRuleEvidence) {
  const blocked = hardRuleEvidence?.blocked;
  return {
    primary_intent: 'RULE_EVIDENCE_ONLY',
    decision: blocked ? 'REJECT' : 'ABSTAIN',
    commercial_eligibility: { decision: blocked ? 'REJECT' : 'ABSTAIN', confidence: 0.5 },
    confidence: 0.5,
    rationale: 'Rule-only support evidence — not semantic authority',
    blind_assessment: true,
    commercial_evidence: [],
    non_commercial_evidence: hardRuleEvidence?.evidence || [],
    model_metadata: { provider: 'rule-only', prompt_version: PROMPT_VERSION },
  };
}

export function assessmentsAgree(a, b) {
  if (!a?.decision || !b?.decision) return false;
  return a.decision === b.decision;
}
