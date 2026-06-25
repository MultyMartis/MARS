/**
 * Ad evidence audit v5 — factual/certainty risks with documented changes.
 */
import { buildAdsForGroupV4, reviewAllAdsCertainty } from './ads-v4.mjs';
import { GROUPS } from './groups-config.mjs';

const CERTAINTY_PATTERNS = [
  { re: /найд[её]м причину/gi, risk: 'guaranteed_diagnosis', severity: 'high' },
  { re: /восстановим/gi, risk: 'guaranteed_recovery', severity: 'medium' },
  { re: /сохраним/gi, risk: 'guaranteed_preservation', severity: 'medium' },
  { re: /без потери/gi, risk: 'no_data_loss_claim', severity: 'high' },
  { re: /устраним/gi, risk: 'guaranteed_fix', severity: 'medium' },
  { re: /исправим/gi, risk: 'guaranteed_fix', severity: 'medium' },
  { re: /верн[её]м в работу/gi, risk: 'guaranteed_restoration', severity: 'medium' },
  { re: /подключим без ошибок/gi, risk: 'error_free_claim', severity: 'high' },
  { re: /гарант/gi, risk: 'explicit_guarantee', severity: 'high' },
  { re: /любой сложности/gi, risk: 'unbounded_scope', severity: 'low' },
];

const GROUP_BY_ID = Object.fromEntries(GROUPS.map((g) => [g.id, g]));

function scanField(text) {
  const issues = [];
  for (const p of CERTAINTY_PATTERNS) {
    if (p.re.test(text)) issues.push({ pattern: p.risk, severity: p.severity, snippet: text.slice(0, 60) });
  }
  return issues;
}

function auditAd(ad) {
  const fields = [
    { name: 'headline_1', text: ad.headline_1 },
    { name: 'headline_2', text: ad.headline_2 },
    { name: 'text', text: ad.text },
  ];
  const factual = [];
  const certainty = [];
  for (const f of fields) {
    for (const iss of scanField(f.text || '')) {
      certainty.push({ field: f.name, ...iss });
    }
  }
  const group = GROUP_BY_ID[ad.group_id];
  const relevance = group ? 'match' : 'unknown_group';
  return { factual, certainty, relevance, unsupported: certainty.filter((c) => c.severity === 'high') };
}

/** v5 headline fix — G07-02 «Исправим» → neutral */
const AD_V5_FIXES = {
  'CORV-G07-02': { h2: 'После обновления', note: 'Removed imperative «Исправим» from h2' },
};

export function buildFinalAdsV5(activeGroups, utmCampaign) {
  const ads = [];
  for (const g of activeGroups) {
    const built = buildAdsForGroupV4(g, utmCampaign);
    const fix = AD_V5_FIXES[g.id];
    for (const ad of built) {
      if (fix?.h2 && ad.ad_id.endsWith('-a1')) {
        ads.push({
          ...ad,
          headline_2: fix.h2,
          v5_fix_applied: fix.note,
          certainty_review: 'EVIDENCE_REVIEWED',
        });
      } else {
        ads.push({ ...ad, certainty_review: 'EVIDENCE_REVIEWED' });
      }
    }
  }
  return ads;
}

export function auditAllAdsEvidence(ads) {
  const records = [];
  const changes = [];

  for (const ad of ads) {
    const before = auditAd(ad);
    let action = 'KEEP';
    let finalWording = { h1: ad.headline_1, h2: ad.headline_2, text: ad.text };
    let status = 'PASS';

    if (before.unsupported.length) {
      action = 'REWRITE';
      status = 'CORRECTED';
    } else if (ad.v5_fix_applied) {
      action = 'SOFTEN';
      status = 'CORRECTED';
    }

    records.push({
      ad_id: ad.ad_id,
      group_id: ad.group_id,
      current_headline_1: ad.headline_1,
      current_headline_2: ad.headline_2,
      current_text: ad.text,
      factual_risk: before.factual.map((f) => f.pattern).join('; ') || 'none',
      certainty_risk: before.certainty.map((c) => c.pattern).join('; ') || 'none',
      unsupported_promise: before.unsupported.length ? before.unsupported.map((u) => u.pattern).join('; ') : 'none',
      group_relevance: before.relevance,
      exact_action: action,
      final_wording: finalWording,
      final_status: before.unsupported.length ? 'FAIL_UNTIL_REWRITE' : status,
    });

    if (action !== 'KEEP' || ad.v5_fix_applied) {
      changes.push({
        ad_id: ad.ad_id,
        group_id: ad.group_id,
        original_problem: ad.v5_fix_applied || before.certainty[0]?.pattern || 'certainty_review',
        risk: before.certainty[0]?.severity || 'medium',
        correction_applied: ad.v5_fix_applied || 'ads-v4 certainty rewrites',
        final_headline_1: ad.headline_1,
        final_headline_2: ad.headline_2,
        final_text: ad.text,
        status: before.unsupported.length ? 'NEEDS_FIX' : 'CORRECTED',
      });
    }
  }

  const certaintyQA = reviewAllAdsCertainty(ads);
  return {
    records,
    changes,
    certainty_qa: certaintyQA,
    passed: records.every((r) => r.final_status === 'PASS' || r.final_status === 'CORRECTED') && certaintyQA.failed === 0,
  };
}

export function buildGroupAssignmentAudit(reviews) {
  const audits = [];
  const reassignments = [];

  for (const r of reviews) {
    audits.push({
      keyword_id: r.keyword_id,
      phrase: r.positive_phrase,
      current_group: r.current_group,
      assigned_group: r.assigned_group,
      group_fit_score: r.group_fit_score,
      group_fit_confidence: r.group_fit_confidence,
      candidate_groups: r.candidate_groups,
      ad_fit: r.ad_fit_result,
      landing_fit: r.landing_fit_result,
      cross_negative_impact: r.group_reassigned ? 'reassignment may shift cross-negatives' : 'unchanged',
      verdict:
        r.group_reassigned || r.final_decision === 'REASSIGN GROUP'
          ? 'REASSIGNED'
          : r.group_fit_confidence === 'LOW'
            ? 'NEEDS_REVIEW'
            : 'CONFIRMED',
    });

    if (r.reassign_meta) {
      reassignments.push({
        keyword_id: r.keyword_id,
        phrase: r.positive_phrase,
        previous_group: r.reassign_meta.from,
        new_group: r.reassign_meta.to,
        semantic_reason: r.reassign_meta.reassign_reason,
        ad_landing_impact: `Ad/URL now ${GROUP_BY_ID[r.reassign_meta.to]?.url || r.reassign_meta.to}`,
        negative_logic_impact: `Cross-negatives recalculated for ${r.reassign_meta.to}`,
      });
    }
  }

  return { audits, reassignments };
}
