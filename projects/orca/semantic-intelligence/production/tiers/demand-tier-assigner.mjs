const TIER_ORDER = ['T1', 'T2', 'T3', 'T4', 'T5'];

export function assignDemandTier(record) {
  if (record.adjudication_result?.outcome !== 'FINAL ACCEPT' && record.final_authority !== 'FINAL ACCEPT') {
    return null;
  }
  const primary = record.primary_assessment || record;
  const reason = primary.reason_code || '';
  const signals = primary.signals || [];

  if (/EXPLICIT_PROVIDER|QUOTE|PRICE|CONTACT|ORDER/i.test(reason)) return 'T1';
  if (signals.some((s) => s.signal_id === 'PROVIDER_HIRE' && ['EXPLICIT', 'STRONG'].includes(s.strength))) return 'T1';
  if (/PROBLEM_QUERY|SUPPORT/i.test(reason) || primary.primary_intent === 'SUPPORT_SEEKING') return 'T2';
  if (/IMPLICATION|MODIFICATION|IMPLEMENTATION/i.test(reason)) return 'T3';
  if (primary.provider_hire_likelihood >= 0.5 && primary.confidence >= 0.7) return 'T3';
  if (primary.commercial_evidence?.length && primary.confidence >= 0.55) return 'T4';
  if (primary.decision === 'ACCEPT') return 'T5';
  return null;
}

export function blockFrequencyOnlyTiering(tier, phrase) {
  const freq = phrase.frequency || phrase.frequencies?.total || 0;
  if (freq > 1000 && tier === 'T1' && !phrase.commercial_evidence?.length) {
    return { blocked: true, reason: 'frequency_only_tiering_blocked' };
  }
  return { blocked: false };
}

export { TIER_ORDER };
