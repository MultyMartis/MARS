/**
 * ORCA collision engine v3 — keyword vs negative QA with regression tests.
 * Reusable across ORCA PPC projects.
 */

export const HIGH_RISK_STEMS = [
  'синхрон',
  'настрой',
  'создан',
  'конфигурац',
  'обновлен',
  'разов',
  'не работает',
  'печатная форма',
  'сайт',
  'обмен',
  'ошибк',
  'интеграц',
  'маркиров',
  'программист',
  'доработк',
];

/** Known failure classes from prior Corvonero cycles — generalized patterns. */
export const REGRESSION_CASES = [
  {
    id: 'REG-01',
    group_id: 'CORV-G05-02',
    forbidden_negative: 'сайт',
    description: 'Bitrix/site phrases must not be blocked by bare «сайт» in owner group',
    test: (gid, neg, keywords) =>
      gid === 'CORV-G05-02' &&
      normPhrase(neg) === 'сайт' &&
      keywords.some((k) => /сайт/.test(normPhrase(k.ad_phrase || k.normalized_phrase || k.source_phrase))),
  },
  {
    id: 'REG-02',
    group_id: 'CORV-G07-03',
    forbidden_negative: 'не работает',
    description: 'Exchange-failure group must not minus core symptom «не работает»',
    test: (gid, neg, keywords) =>
      gid === 'CORV-G07-03' &&
      normPhrase(neg) === 'не работает' &&
      keywords.some((k) => /не работает/.test(normPhrase(k.ad_phrase || k.normalized_phrase || k.source_phrase))),
  },
  {
    id: 'REG-03',
    group_id: 'CORV-G03-05',
    forbidden_negative: 'печатная форма',
    description: 'External print-form group must not minus «печатная форма»',
    test: (gid, neg, keywords) =>
      gid === 'CORV-G03-05' &&
      normPhrase(neg) === 'печатная форма' &&
      keywords.some((k) => /печатн.*форм|внешн.*печатн/.test(normPhrase(k.ad_phrase || k.normalized_phrase || k.source_phrase))),
  },
  {
    id: 'REG-04',
    group_id: 'CORV-G05-03',
    forbidden_negative: 'синхрон',
    description: 'Cash-register sync group must not minus stem «синхрон»',
    test: (gid, neg, keywords) =>
      gid === 'CORV-G05-03' &&
      /^синхрон/.test(normPhrase(neg)) &&
      keywords.some((k) => /синхрон/.test(normPhrase(k.ad_phrase || k.normalized_phrase || k.source_phrase))),
  },
  {
    id: 'REG-05',
    level: 'global',
    description: 'No active phrase blocked by global negative in owner campaign',
    test: (level, neg, keywords, hits) => level === 'global' && hits.length > 0,
  },
  {
    id: 'REG-06',
    description: 'Informational phrase must not survive via long inline-minus tail alone',
    test: (kw) => {
      const base = stripInlineNegatives(kw.ad_phrase || kw.source_phrase || '');
      const inlineCount = (kw.phrase_negatives || []).length;
      return (
        inlineCount >= 3 &&
        (/^как (сделать|настроить|изменить)/.test(base) ||
          /подлеж.*маркиров|какие.*маркиров/.test(base))
      );
    },
  },
];

export function normPhrase(s) {
  return String(s || '')
    .toLowerCase()
    .replace(/ё/g, 'е')
    .replace(/\s+/g, ' ')
    .trim();
}

export function stripInlineNegatives(phrase) {
  return normPhrase(String(phrase || '').replace(/\s+-[\wа-яё]+/gi, ''));
}

/**
 * Test whether a negative blocks a keyword phrase.
 * @param {string} keywordPhrase
 * @param {string} negativeToken
 * @param {{ substringMode?: boolean }} opts
 */
export function testCollision(keywordPhrase, negativeToken, opts = {}) {
  const p = stripInlineNegatives(keywordPhrase);
  const neg = normPhrase(negativeToken).replace(/^-/, '');
  if (!neg || !p) return false;

  if (neg.includes(' ')) {
    return p.includes(neg);
  }

  const words = p.split(/\s+/);
  if (words.includes(neg)) return true;
  if (p.includes(` ${neg} `) || p.startsWith(`${neg} `) || p.endsWith(` ${neg}`)) return true;

  if (opts.substringMode !== false) {
    for (const w of words) {
      if (w.startsWith(neg) || w.includes(neg)) return true;
    }
    if (p.includes(neg)) return true;
  }

  return false;
}

export function isHighRiskStem(token) {
  const t = normPhrase(token);
  return HIGH_RISK_STEMS.some((stem) => t === stem || t.startsWith(stem) || stem.startsWith(t));
}

/**
 * Remove negatives that collide with keywords in the same group.
 */
export function filterSafeNegatives(negatives, keywords, context = {}) {
  const removed = [];
  const safe = [];

  for (const neg of negatives || []) {
    const token = normPhrase(neg);
    const hits = (keywords || []).filter((k) =>
      testCollision(k.ad_phrase || k.source_phrase || k.normalized_phrase, token)
    );

    if (hits.length) {
      removed.push({
        negative: token,
        level: context.level || 'group',
        group_id: context.group_id,
        colliding_keywords: hits.map((k) => k.ad_phrase || k.source_phrase || k.normalized_phrase),
        reason: 'blocks_own_group_keyword',
      });
      continue;
    }

    let regressionHit = false;
    for (const reg of REGRESSION_CASES) {
      if (!reg.test || reg.level || reg.id === 'REG-06') continue;
      if (reg.test(context.group_id, token, keywords)) {
        removed.push({
          negative: token,
          level: context.level || 'group',
          group_id: context.group_id,
          regression_id: reg.id,
          reason: reg.description,
        });
        regressionHit = true;
        break;
      }
    }
    if (regressionHit) continue;

    safe.push(token);
  }

  return { safe: [...new Set(safe)], removed };
}

/**
 * Full collision audit across all levels for export keywords.
 */
export function runCollisionAudit(finalKeywords, negativesConfig) {
  const {
    globalNegatives = [],
    directionNegatives = {},
    groupCrossNegatives = {},
    phraseInlineNegatives = {},
    groups = [],
  } = negativesConfig;

  const records = [];
  let pairsTested = 0;

  const addRecord = (kw, neg, level, result, extra = {}) => {
    pairsTested++;
    records.push({
      keyword_id: kw.keyword_id,
      keyword: kw.ad_phrase || kw.source_phrase,
      positive_base: stripInlineNegatives(kw.ad_phrase || kw.source_phrase),
      group_id: kw.group_id,
      negative: neg,
      negative_level: level,
      collision: result.collision,
      risk_type: result.risk_type,
      correction: result.correction || '',
      stem_warning: isHighRiskStem(neg),
      ...extra,
    });
  };

  for (const kw of finalKeywords) {
    const g = groups.find((x) => x.id === kw.group_id);
    const dirId = g?.campaign || kw.campaign_id;

    for (const neg of globalNegatives) {
      const hit = testCollision(kw.ad_phrase || kw.source_phrase, neg);
      addRecord(kw, neg, 'global', {
        collision: hit,
        risk_type: hit ? 'BLOCKING' : 'OK',
        correction: hit ? 'remove_global_or_exclude_keyword' : '',
      });
    }

    for (const neg of directionNegatives[dirId] || []) {
      const hit = testCollision(kw.ad_phrase || kw.source_phrase, neg);
      addRecord(kw, neg, 'direction', {
        collision: hit,
        risk_type: hit ? 'BLOCKING' : 'OK',
        correction: hit ? 'remove_from_direction_or_reassign_keyword' : '',
      });
    }

    for (const neg of groupCrossNegatives[kw.group_id] || []) {
      const hit = testCollision(kw.ad_phrase || kw.source_phrase, neg);
      addRecord(kw, neg, 'group_cross', {
        collision: hit,
        risk_type: hit ? 'BLOCKING' : isHighRiskStem(neg) ? 'STEM_RISK' : 'OK',
        correction: hit ? 'remove_cross_negative_from_owner_group' : '',
      });
    }

    for (const neg of phraseInlineNegatives[kw.group_id] || []) {
      const hit = testCollision(stripInlineNegatives(kw.ad_phrase), neg);
      addRecord(kw, neg, 'phrase_inline', {
        collision: hit,
        risk_type: hit ? 'BLOCKING' : 'OK',
        correction: hit ? 'remove_inline_or_exclude_phrase' : '',
      });
    }
  }

  const blocking = records.filter((r) => r.collision && r.risk_type === 'BLOCKING');
  const stemWarnings = records.filter((r) => !r.collision && r.stem_warning);
  const inlineRegressions = finalKeywords.filter((kw) =>
    REGRESSION_CASES.filter((r) => r.id === 'REG-06').some((r) => r.test(kw))
  );

  return {
    pairs_tested: pairsTested,
    collisions_before_correction: blocking.length,
    blocking_records: blocking,
    stem_warnings: stemWarnings.length,
    stem_warning_records: stemWarnings.slice(0, 100),
    inline_regression_phrases: inlineRegressions.map((k) => k.ad_phrase),
    records,
  };
}

/**
 * Audit using exported per-group negatives (ground truth for Commander).
 */
export function runExportedCollisionAudit(finalKeywords, groupsPayload, globalNegatives, phraseInlineNegatives) {
  const records = [];
  let pairsTested = 0;

  for (const kw of finalKeywords) {
    const group = groupsPayload.find((g) => g.group_id === kw.group_id);
    const groupNegs = group?.group_negatives || [];

    for (const neg of globalNegatives) {
      pairsTested++;
      const hit = testCollision(kw.ad_phrase || kw.source_phrase, neg);
      records.push({
        keyword_id: kw.keyword_id,
        keyword: kw.ad_phrase,
        group_id: kw.group_id,
        negative: neg,
        negative_level: 'global',
        collision: hit,
        risk_type: hit ? 'BLOCKING' : 'OK',
      });
    }

    for (const neg of groupNegs) {
      pairsTested++;
      const hit = testCollision(kw.ad_phrase || kw.source_phrase, neg);
      records.push({
        keyword_id: kw.keyword_id,
        keyword: kw.ad_phrase,
        group_id: kw.group_id,
        negative: neg,
        negative_level: 'group_export',
        collision: hit,
        risk_type: hit ? 'BLOCKING' : isHighRiskStem(neg) ? 'STEM_RISK' : 'OK',
      });
    }

    for (const neg of phraseInlineNegatives[kw.group_id] || []) {
      pairsTested++;
      const hit = testCollision(stripInlineNegatives(kw.ad_phrase), neg);
      records.push({
        keyword_id: kw.keyword_id,
        keyword: kw.ad_phrase,
        group_id: kw.group_id,
        negative: neg,
        negative_level: 'phrase_inline',
        collision: hit,
        risk_type: hit ? 'BLOCKING' : 'OK',
      });
    }
  }

  const blocking = records.filter((r) => r.collision && r.risk_type === 'BLOCKING');
  return { pairs_tested: pairsTested, blocking_records: blocking, records };
}

export function runRegressionTests(finalKeywords, groupCrossNegatives, globalNegatives) {
  const failures = [];

  for (const reg of REGRESSION_CASES) {
    if (reg.id === 'REG-05') {
      for (const kw of finalKeywords) {
        for (const g of globalNegatives) {
          if (testCollision(kw.ad_phrase || kw.source_phrase, g)) {
            failures.push({
              regression_id: reg.id,
              group_id: kw.group_id,
              keyword: kw.ad_phrase,
              negative: g,
              description: reg.description,
            });
          }
        }
      }
      continue;
    }

    if (reg.id === 'REG-06') {
      for (const kw of finalKeywords) {
        if (reg.test(kw)) {
          failures.push({
            regression_id: reg.id,
            group_id: kw.group_id,
            keyword: kw.ad_phrase,
            description: reg.description,
          });
        }
      }
      continue;
    }

    const gid = reg.group_id;
    const tokens = groupCrossNegatives[gid] || [];
    const kws = finalKeywords.filter((k) => k.group_id === gid);
    for (const neg of tokens) {
      if (reg.test(gid, neg, kws)) {
        failures.push({
          regression_id: reg.id,
          group_id: gid,
          negative: neg,
          description: reg.description,
          sample_keywords: kws.filter((k) => testCollision(k.ad_phrase, neg)).slice(0, 3).map((k) => k.ad_phrase),
        });
      }
    }
  }

  return { passed: failures.length === 0, failures };
}
