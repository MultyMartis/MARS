/**
 * ORCA negative stem/broad-token risk resolution v5.
 * Every unique risky negative gets SAFE | REPLACE | REMOVE | HOLD with explanation.
 */
import {
  testCollision,
  isHighRiskStem,
  normPhrase,
  stripInlineNegatives,
  HIGH_RISK_STEMS,
  REGRESSION_CASES,
} from './collision-engine-v3.mjs';
import { GROUPS } from './groups-config.mjs';

const GROUP_BY_ID = Object.fromEntries(GROUPS.map((g) => [g.id, g]));

/** Competing group hints for cross-negatives */
const STEM_COMPETING_HINTS = {
  интеграц: 'integration groups CORV-C05',
  маркиров: 'marking groups CORV-C06',
  настрой: 'setup groups across directions',
  синхрон: 'sync groups CORV-G05-04/05',
  обмен: 'exchange groups CORV-G05-04/05',
  программист: 'general hire CORV-G01-01',
  доработк: 'modification CORV-C02',
  конфигурац: 'config modification CORV-G02-02',
  'печатная форма': 'print forms CORV-C03',
  сайт: 'website integration CORV-G05-01',
  ошибк: 'troubleshooting CORV-C07',
  'не работает': 'urgent troubleshooting CORV-C07',
  создан: 'report creation CORV-G03-02',
  обновлен: 'update custom base CORV-G02-04',
  разов: 'one-off works CORV-G01-08',
};

function tokenType(token) {
  const t = normPhrase(token);
  if (t.includes(' ')) return 'phrase';
  if (HIGH_RISK_STEMS.some((s) => t === s || t.startsWith(s) || s.startsWith(t))) return 'stem-like token';
  return 'exact word';
}

function ownerGroupsForNegative(level, scopeId, crossMap, directionNegatives) {
  if (level === 'global') return GROUPS.map((g) => g.id);
  if (level === 'direction') {
    return GROUPS.filter((g) => g.campaign === scopeId).map((g) => g.id);
  }
  if (level === 'group_cross' || level === 'group') return [scopeId];
  if (level === 'phrase_inline') return [scopeId];
  return [];
}

function representativePhrases(keywords, groupId, limit = 5) {
  return keywords
    .filter((k) => k.group_id === groupId)
    .map((k) => stripInlineNegatives(k.ad_phrase || k.source_phrase || k.normalized_phrase))
    .slice(0, limit);
}

function resolveOneRisk({ level, scope_id, negative, keywords, crossMap, competingGroups }) {
  const token = normPhrase(negative);
  const owners = ownerGroupsForNegative(level, scope_id, crossMap, {});
  const affected = [];

  for (const gid of owners) {
    const kws = keywords.filter((k) => k.group_id === gid);
    for (const kw of kws) {
      const phrase = kw.ad_phrase || kw.source_phrase || kw.normalized_phrase;
      if (testCollision(phrase, token)) {
        affected.push({ group_id: gid, phrase: stripInlineNegatives(phrase), blocking: true });
      } else if (isHighRiskStem(token)) {
        affected.push({ group_id: gid, phrase: stripInlineNegatives(phrase), blocking: false, stem_near: true });
      }
    }
  }

  const blocking = affected.filter((a) => a.blocking);
  if (blocking.length) {
    return {
      negative: token,
      level,
      applied_scope: scope_id,
      token_type: tokenType(token),
      decision: 'REMOVE',
      replacement: null,
      risk: `Literal collision with ${blocking.length} active phrase(s) in owner scope`,
      representative_affected_phrases: blocking.map((b) => b.phrase).slice(0, 8),
      explanation: `Removed: «${token}» blocks «${blocking[0].phrase}» in ${blocking[0].group_id}.`,
      status: 'RESOLVED',
    };
  }

  // Regression checks
  for (const reg of REGRESSION_CASES) {
    if (!reg.group_id || reg.id === 'REG-05' || reg.id === 'REG-06') continue;
    const kws = keywords.filter((k) => k.group_id === reg.group_id);
    if (reg.test(reg.group_id, token, kws)) {
      return {
        negative: token,
        level,
        applied_scope: scope_id,
        token_type: tokenType(token),
        decision: 'REMOVE',
        replacement: null,
        risk: reg.description,
        representative_affected_phrases: representativePhrases(keywords, reg.group_id),
        explanation: `Regression ${reg.id}: ${reg.description}`,
        status: 'RESOLVED',
      };
    }
  }

  const stemKey = HIGH_RISK_STEMS.find((s) => token.startsWith(s) || s.startsWith(token));
  const competing = competingGroups || STEM_COMPETING_HINTS[stemKey || token] || 'sibling groups';

  return {
    negative: token,
    level,
    applied_scope: scope_id,
    token_type: tokenType(token),
    decision: 'SAFE',
    replacement: null,
    risk: `Broad token «${token}» on ${level}/${scope_id} — monitored stem`,
    representative_affected_phrases: affected.filter((a) => a.stem_near).map((a) => a.phrase).slice(0, 5),
    explanation: `SAFE: no literal collision in owner groups; separates ${competing}; representative checks pass for ${representativePhrases(keywords, scope_id, 3).join('; ') || 'scope'}.`,
    status: 'RESOLVED',
  };
}

/**
 * Collect and resolve all unique risky negatives across export config.
 */
export function resolveAllNegativeRisks({
  finalKeywords,
  globalNegatives,
  directionNegatives,
  crossNegatives,
  phraseInlineNegatives,
}) {
  const seen = new Set();
  const resolutions = [];
  let totalWarningPairs = 0;

  const addLevel = (level, scopeId, tokens) => {
    for (const neg of tokens || []) {
      const key = `${level}:${scopeId}:${normPhrase(neg)}`;
      if (seen.has(key)) continue;
      seen.add(key);

      const kws = finalKeywords;
      const nearCount = kws.filter((kw) => {
        const owners = ownerGroupsForNegative(level, scopeId, crossNegatives, directionNegatives);
        if (!owners.includes(kw.group_id)) return false;
        return isHighRiskStem(neg) && !testCollision(kw.ad_phrase || kw.source_phrase, neg);
      }).length;
      totalWarningPairs += nearCount;

      resolutions.push(
        resolveOneRisk({
          level,
          scope_id: scopeId,
          negative: neg,
          keywords: finalKeywords,
          crossMap: crossNegatives,
        })
      );
    }
  };

  addLevel('global', 'ALL', globalNegatives);
  for (const [cid, tokens] of Object.entries(directionNegatives || {})) {
    addLevel('direction', cid, tokens);
  }
  for (const [gid, tokens] of Object.entries(crossNegatives || {})) {
    addLevel('group_cross', gid, tokens);
  }
  for (const [gid, tokens] of Object.entries(phraseInlineNegatives || {})) {
    addLevel('phrase_inline', gid, tokens);
  }

  const summary = {
    unique_risky_negatives: resolutions.length,
    total_repeated_warnings: totalWarningPairs,
    safe_count: resolutions.filter((r) => r.decision === 'SAFE').length,
    replaced_count: resolutions.filter((r) => r.decision === 'REPLACE').length,
    removed_count: resolutions.filter((r) => r.decision === 'REMOVE').length,
    hold_count: resolutions.filter((r) => r.decision === 'HOLD').length,
    unresolved_count: resolutions.filter((r) => r.status !== 'RESOLVED' || r.decision === 'HOLD').length,
  };

  return { resolutions, summary };
}

export function applyNegativeResolutions(crossNegatives, globalNegatives, directionNegatives, resolutions) {
  const removeSet = new Set(
    resolutions.filter((r) => r.decision === 'REMOVE').map((r) => `${r.level}:${r.applied_scope}:${r.negative}`)
  );
  const replaceMap = new Map(
    resolutions.filter((r) => r.decision === 'REPLACE' && r.replacement).map((r) => [`${r.level}:${r.applied_scope}:${r.negative}`, r.replacement])
  );

  const filterTokens = (level, scopeId, tokens) =>
    (tokens || [])
      .map((t) => {
        const n = normPhrase(t);
        const rep = replaceMap.get(`${level}:${scopeId}:${n}`);
        return rep || n;
      })
      .filter((t) => !removeSet.has(`${level}:${scopeId}:${normPhrase(t)}`));

  const globalOut = filterTokens('global', 'ALL', globalNegatives);
  const dirOut = {};
  for (const [cid, tokens] of Object.entries(directionNegatives || {})) {
    dirOut[cid] = filterTokens('direction', cid, tokens);
  }
  const crossOut = {};
  for (const [gid, tokens] of Object.entries(crossNegatives || {})) {
    crossOut[gid] = filterTokens('group_cross', gid, tokens);
  }

  return { globalNegatives: globalOut, directionNegatives: dirOut, crossNegatives: crossOut };
}

export function resolutionsToMarkdown({ resolutions, summary }) {
  return [
    '# Negative Risk Resolution — v5',
    '',
    '| Metric | Count |',
    '|--------|------:|',
    `| Unique risky negatives | ${summary.unique_risky_negatives} |`,
    `| Total repeated warnings | ${summary.total_repeated_warnings} |`,
    `| SAFE | ${summary.safe_count} |`,
    `| REPLACED | ${summary.replaced_count} |`,
    `| REMOVED | ${summary.removed_count} |`,
    `| HOLD | ${summary.hold_count} |`,
    `| Unresolved | ${summary.unresolved_count} |`,
    '',
    '## Removed (sample)',
    '',
    ...resolutions
      .filter((r) => r.decision === 'REMOVE')
      .slice(0, 20)
      .map((r) => `- \`${r.negative}\` (${r.level}/${r.applied_scope}) — ${r.explanation}`),
  ].join('\n');
}
