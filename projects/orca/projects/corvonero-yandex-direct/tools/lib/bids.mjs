export const TIER_RANGES = {
  T1: { min: 450, max: 550 },
  T2: { min: 350, max: 450 },
  T3: { min: 250, max: 350 },
  T4: { min: 180, max: 250 },
};

/**
 * Deterministic bid assignment per Corvonero bidding-model-v1.
 * @param {string} tier
 * @param {number} rank 1-based priority rank in group
 * @param {number} total keywords in group
 * @param {{ commercial?: number, specificity?: number, noiseRisk?: number, urgency?: number }} factors
 */
export function assignBid(tier, rank, total, factors = {}) {
  const range = TIER_RANGES[tier] || TIER_RANGES.T3;
  const spread = Math.min(90, Math.max(10, range.max - range.min));
  const step = total <= 1 ? 0 : Math.max(15, Math.min(25, Math.floor(spread / (total - 1))));

  let bid = range.max - (rank - 1) * step;

  // Factor adjustments (bounded ±30)
  const adj =
    (factors.commercial || 0) * 8 +
    (factors.specificity || 0) * 6 -
    (factors.noiseRisk || 0) * 10 +
    (factors.urgency || 0) * 12;

  bid = Math.round(bid + Math.max(-30, Math.min(30, adj)));
  bid = Math.max(range.min, Math.min(range.max, bid));

  const rationale = [];
  if (rank === 1) rationale.push('PRIMARY');
  if (factors.commercial >= 0.7) rationale.push('HIGH_COMMERCIAL');
  if (factors.noiseRisk >= 0.5) rationale.push('NOISE_CONTROL');
  if (factors.urgency >= 0.5) rationale.push('URGENCY');
  if (factors.specificity >= 0.6) rationale.push('SPECIFIC_INTENT');

  return { tier, final_bid: bid, rationale_code: rationale.join('|') || 'TIER_DEFAULT', factors };
}

export function scoreKeywordFactors(kw, group) {
  const phrase = kw.normalized_phrase || '';
  let commercial = 0.5;
  if (kw.intent_class === 'direct-commercial') commercial = 0.85;
  if (kw.intent_class === 'commercial-mixed') commercial = 0.65;
  if (kw.intent_class === 'troubleshooting') commercial = 0.75;
  if (/услуг|заказ|под ключ|специалист|на аутсорсе|для организац|для бизнес/.test(phrase)) commercial += 0.1;

  let specificity = 0.4;
  if (group.priority >= 80) specificity = 0.8;
  else if (group.priority >= 60) specificity = 0.6;
  if (phrase.split(/\s+/).length >= 4) specificity += 0.1;

  let noiseRisk = 0.2;
  const nc = kw.noise_classes || [];
  if (nc.includes('job-seeking')) noiseRisk += 0.4;
  if (nc.includes('informational')) noiseRisk += 0.3;
  if (nc.includes('training')) noiseRisk += 0.3;

  let urgency = 0;
  if (group.campaign === 'CORV-C07') urgency = 0.7;
  if (/срочн|не работает|ошибк|восстанов/.test(phrase)) urgency = 0.8;

  return {
    commercial: Math.min(1, commercial),
    specificity: Math.min(1, specificity),
    noiseRisk: Math.min(1, noiseRisk),
    urgency: Math.min(1, urgency),
  };
}
