const PROTECTED_NEGATIVES = [
  { pattern: /ваканс|резюме|работа программист/i, term: 'вакансии', class: 'protected_career', risk: 'low' },
  { pattern: /скачать|бесплатно|торрент/i, term: 'скачать бесплатно', class: 'protected_download', risk: 'low' },
  { pattern: /курс|обучение|урок/i, term: 'курсы', class: 'protected_education', risk: 'medium' },
  { pattern: /своими руками|самостоятельно/i, term: 'своими руками', class: 'protected_diy', risk: 'medium' },
];

export function buildNegativeIntelligence(records, clusters, ownershipMap) {
  const global = [];
  const campaign = [];
  const group = [];
  const cross = [];
  const watchlist = [];

  for (const neg of PROTECTED_NEGATIVES) {
    global.push({
      negative_id: `NEG-G-${neg.class}`,
      term: neg.term,
      match_type: 'phrase',
      class: neg.class,
      exclusion_type: 'definite_exclusion',
      rationale: `Protected intent stratum: ${neg.class}`,
      risk: neg.risk,
      source_evidence: 'protected_intent_policy',
    });
  }

  for (const c of clusters) {
    const otherServices = new Set(clusters.filter((x) => x.cluster_id !== c.cluster_id).map((x) => x.service_owner));
    for (const svc of otherServices) {
      if (svc !== c.service_owner) {
        cross.push({
          negative_id: `NEG-X-${c.cluster_id}-${svc}`,
          term: null,
          cluster_id: c.cluster_id,
          blocks_service: svc,
          exclusion_type: 'cross_separation',
          rationale: `Separate cluster service ${svc} from ${c.service_owner}`,
          risk: 'medium',
        });
      }
    }
  }

  for (const rec of records) {
    if (rec.adjudication_result?.outcome === 'FINAL REJECT' && rec.protected_intent_class) {
      watchlist.push({
        negative_id: `NEG-W-${rec.phrase_id}`,
        term: rec.raw_query,
        class: rec.protected_intent_class,
        exclusion_type: 'observation_only',
        affected_phrase_ids: [rec.phrase_id],
        rationale: 'Rejected protected intent — observation',
        risk: 'low',
      });
    }
  }

  const unsafeBroad = global.filter((n) => n.term && n.term.length < 4);
  for (const u of unsafeBroad) {
    u.exclusion_type = 'unsafe_broad_negative';
    u.risk = 'high';
  }

  return {
    global_negatives: global,
    campaign_level_candidates: campaign,
    group_level_candidates: group,
    cross_negatives: cross,
    protected_intent_negatives: global.filter((g) => g.class?.startsWith('protected_')),
    observation_watchlist: watchlist,
    generated_at: new Date().toISOString(),
  };
}
