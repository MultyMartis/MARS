/**
 * Campaign architecture validation — warnings vs hard fails documented per check.
 */

export const CHECK_SEVERITY = Object.freeze({
  HARD_FAIL: 'HARD_FAIL',
  WARNING: 'WARNING',
  OPERATOR_REVIEW: 'OPERATOR_REVIEW',
});

const DEFAULT_MAX_GROUP_SIZE = 30;
const DEFAULT_MIN_GROUP_SIZE = 1;

/**
 * @param {object} input — { groups: [{ group_id, campaign, phrase_count, commercial_intent, group_name }] }
 * @param {object} [options]
 */
export function validateCampaignArchitecture(input, options = {}) {
  const violations = [];
  const maxSize = options.max_group_size ?? DEFAULT_MAX_GROUP_SIZE;
  const minSize = options.min_group_size ?? DEFAULT_MIN_GROUP_SIZE;
  const groups = input.groups ?? [];

  const byKey = new Map();
  for (const g of groups) {
    const key = `${g.campaign}::${g.group_id}`;
    if (byKey.has(key)) {
      violations.push({
        code: 'DUPLICATE_GROUP',
        severity: CHECK_SEVERITY.HARD_FAIL,
        message: `Duplicate group ${g.group_id} in ${g.campaign}`,
      });
    }
    byKey.set(key, g);

    const count = g.phrase_count ?? (g.phrase_list ? String(g.phrase_list).split(';').length : 0);
    if (count > maxSize) {
      violations.push({
        code: 'GROUP_ABOVE_MAXIMUM',
        severity: CHECK_SEVERITY.WARNING,
        message: `Group ${g.group_id} has ${count} phrases (max ${maxSize})`,
      });
    }
    if (count < minSize) {
      violations.push({
        code: 'GROUP_BELOW_MINIMUM',
        severity: CHECK_SEVERITY.HARD_FAIL,
        message: `Group ${g.group_id} has no phrases`,
      });
    }
    if (count === 1 && !g.single_phrase_justification) {
      violations.push({
        code: 'ONE_PHRASE_WITHOUT_JUSTIFICATION',
        severity: CHECK_SEVERITY.OPERATOR_REVIEW,
        message: `Group ${g.group_id} has single phrase without justification`,
      });
    }
  }

  const intentByGroup = new Map();
  for (const g of groups) {
    const intents = new Set(String(g.commercial_intent ?? '').split(/[,;]/).map((s) => s.trim()).filter(Boolean));
    if (intents.size > 1) {
      violations.push({
        code: 'MIXED_INTENT_GROUP',
        severity: CHECK_SEVERITY.HARD_FAIL,
        message: `Group ${g.group_id} mixes intents: ${[...intents].join(', ')}`,
      });
    }
    intentByGroup.set(g.group_id, intents);
  }

  const phraseOwners = new Map();
  for (const g of groups) {
    const phrases = String(g.phrase_list ?? '').split(';').map((s) => s.trim().toLowerCase()).filter(Boolean);
    for (const ph of phrases) {
      if (phraseOwners.has(ph)) {
        violations.push({
          code: 'OVERLAPPING_DUPLICATE_PHRASE',
          severity: CHECK_SEVERITY.HARD_FAIL,
          message: `Phrase "${ph}" in ${g.group_id} and ${phraseOwners.get(ph)}`,
        });
      } else {
        phraseOwners.set(ph, g.group_id);
      }
    }
  }

  const serviceFamilies = new Set(groups.map((g) => g.service ?? g.commercial_intent).filter(Boolean));
  if (serviceFamilies.size > 1 && options.require_single_service_family) {
    violations.push({
      code: 'SERVICE_FAMILY_INCONSISTENCY',
      severity: CHECK_SEVERITY.WARNING,
      message: `Multiple service families in scope: ${[...serviceFamilies].join(', ')}`,
    });
  }

  const hardFails = violations.filter((v) => v.severity === CHECK_SEVERITY.HARD_FAIL);
  return {
    status: hardFails.length === 0 ? 'PASS' : 'FAIL',
    violation_count: violations.length,
    violations,
  };
}

/**
 * @param {object[]} ads — [{ group_id, headline_1, text }]
 * @param {string} forbiddenGeneric
 */
export function detectGenericAdReuse(ads, forbiddenGeneric) {
  const violations = [];
  const textCounts = new Map();
  for (const ad of ads) {
    const text = String(ad.text ?? ad.ad_text ?? '').trim();
    if (!text) continue;
    textCounts.set(text, (textCounts.get(text) ?? 0) + 1);
    if (forbiddenGeneric && text === forbiddenGeneric) {
      violations.push({
        code: 'FORBIDDEN_GENERIC_AD',
        severity: CHECK_SEVERITY.HARD_FAIL,
        message: `Forbidden generic ad on group ${ad.group_id}`,
      });
    }
  }
  for (const [text, count] of textCounts) {
    if (count > 3) {
      violations.push({
        code: 'GENERIC_AD_REUSE_THRESHOLD',
        severity: CHECK_SEVERITY.WARNING,
        message: `Ad text reused ${count} times: "${text.slice(0, 60)}..."`,
      });
    }
  }
  return violations;
}
