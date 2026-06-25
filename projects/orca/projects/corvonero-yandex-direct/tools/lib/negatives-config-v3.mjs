/**
 * Negative keyword architecture v3 — safe layers with collision-aware filtering.
 */
import {
  GLOBAL_NEGATIVES_V2,
  DIRECTION_NEGATIVES_V2,
  GROUP_CROSS_NEGATIVES_V2,
  PHRASE_INLINE_NEGATIVES_V2,
  formatNegativesForCommander,
  mergeNegatives,
  buildCrossNegativeRecords,
  buildGlobalNegativeRegistry,
  buildDirectionNegativeRegistry,
} from './negatives-config-v2.mjs';
import { filterSafeNegatives } from './collision-engine-v3.mjs';

/** v3 global — remove bare «бесплатно» (blocks valid commercial qualifiers); keep phrase forms */
export const GLOBAL_NEGATIVES_V3 = GLOBAL_NEGATIVES_V2.filter(
  (t) => !['бесплатно', 'тест', 'видео'].includes(t)
);

/** Per-group manual removals — known regression stems before auto-filter */
const MANUAL_CROSS_REMOVALS = {
  'CORV-G05-02': ['сайт'],
  'CORV-G07-03': ['не работает'],
  'CORV-G03-05': ['печатная форма'],
  'CORV-G05-03': ['синхрон'],
  'CORV-G05-04': ['синхрон'],
  'CORV-G05-05': ['синхрон'],
  'CORV-G03-03': ['как сделать', 'как изменить', 'как настроить'],
  'CORV-G03-04': ['как сделать', 'как изменить', 'как настроить'],
};

/** Build base cross-negatives from v2 with manual stem fixes */
function buildBaseCrossNegatives() {
  const out = {};
  for (const [gid, tokens] of Object.entries(GROUP_CROSS_NEGATIVES_V2)) {
    const remove = new Set((MANUAL_CROSS_REMOVALS[gid] || []).map((t) => t.toLowerCase()));
    out[gid] = tokens.filter((t) => !remove.has(t.toLowerCase()));
  }
  return out;
}

export const BASE_CROSS_NEGATIVES_V3 = buildBaseCrossNegatives();

/** Minimal inline negatives — only protect valid commercial head terms */
export const PHRASE_INLINE_NEGATIVES_V3 = {
  'CORV-G01-01': ['вакансия', 'обучение', 'курсы', 'резюме', 'как стать'],
  'CORV-G01-05': ['вакансия'],
  'CORV-G07-01': ['вакансия'],
};

export const DIRECTION_NEGATIVES_V3 = Object.fromEntries(
  Object.entries(DIRECTION_NEGATIVES_V2).map(([cid, tokens]) => [
    cid,
    tokens.filter((t) => {
      if (t === 'тс пиот' && (cid === 'CORV-C03' || cid === 'CORV-C05')) return false;
      if (t === 'честный знак' && cid === 'CORV-C08') return false;
      return true;
    }),
  ])
);

/**
 * Build collision-safe group negatives for export.
 * @param {string} groupId
 * @param {object[]} groupKeywords final keywords in group
 * @param {string} campaignId
 */
export function buildSafeGroupNegatives(groupId, groupKeywords, campaignId) {
  const rawCross = BASE_CROSS_NEGATIVES_V3[groupId] || [];
  const rawDir = DIRECTION_NEGATIVES_V3[campaignId] || [];

  const crossFiltered = filterSafeNegatives(rawCross, groupKeywords, {
    level: 'group_cross',
    group_id: groupId,
  });
  const dirFiltered = filterSafeNegatives(rawDir, groupKeywords, {
    level: 'direction',
    group_id: groupId,
  });

  const merged = mergeNegatives(crossFiltered.safe, dirFiltered.safe);
  return {
    group_negatives: merged,
    group_negatives_commander: formatNegativesForCommander(merged),
    cross_negatives: crossFiltered.safe,
    direction_negatives_applied: dirFiltered.safe,
    removed_negatives: [...crossFiltered.removed, ...dirFiltered.removed],
  };
}

/**
 * Build full safe cross-negative map for all active groups.
 */
export function buildSafeCrossNegativeMap(activeGroups, finalKeywords) {
  const map = {};
  const removalLog = [];

  for (const g of activeGroups) {
    const kws = finalKeywords.filter((k) => k.group_id === g.id);
    const raw = BASE_CROSS_NEGATIVES_V3[g.id] || [];
    const { safe, removed } = filterSafeNegatives(raw, kws, { level: 'group_cross', group_id: g.id });
    map[g.id] = safe;
    if (removed.length) {
      removalLog.push({ group_id: g.id, removed });
    }
  }

  return { map, removalLog };
}

export {
  formatNegativesForCommander,
  mergeNegatives,
  buildCrossNegativeRecords,
  buildGlobalNegativeRegistry,
  buildDirectionNegativeRegistry,
};

export function buildGlobalNegativeRegistryV3() {
  return GLOBAL_NEGATIVES_V3.map((phrase) => ({
    phrase,
    level: 'global',
    source: 'wordstat_evidence_v3_review',
    reason: 'common_noise_all_directions',
    risk: phrase.length <= 4 ? 'medium' : 'low',
    approved_status: 'approved',
  }));
}

export function buildDirectionNegativeRegistryV3() {
  const out = [];
  for (const [cid, tokens] of Object.entries(DIRECTION_NEGATIVES_V3)) {
    for (const phrase of tokens) {
      out.push({
        phrase,
        level: 'direction',
        campaign_id: cid,
        source: 'direction_isolation_v3',
        reason: 'logical_campaign_separation_emulated',
        risk: 'medium',
        approved_status: 'approved',
      });
    }
  }
  return out;
}

export function buildFinalNegativeRegistryV3(crossMap, inlineMap) {
  const out = [
    ...buildGlobalNegativeRegistryV3(),
    ...buildDirectionNegativeRegistryV3(),
  ];

  for (const [gid, tokens] of Object.entries(crossMap)) {
    for (const token of tokens) {
      out.push({
        level: 'group',
        group_id: gid,
        phrase: token,
        source: 'conflict-negative-matrix-v3',
        reason: 'sibling_discriminator_safe',
        cross_risk: 'low',
        approved_status: 'approved',
      });
    }
  }

  for (const [gid, tokens] of Object.entries(inlineMap)) {
    for (const token of tokens) {
      out.push({
        level: 'phrase_inline',
        group_id: gid,
        phrase: token,
        source: 'phrase_inline_v3_minimal',
        reason: 'head_term_protection_only',
        cross_risk: 'low',
        approved_status: 'approved',
      });
    }
  }

  return out;
}
