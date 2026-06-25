/**
 * ORCA semantic evidence review v5 — phrase-specific decisions, honest review states.
 * No template-only approvals; group fit is a separate gate from commerciality.
 */
import { GROUPS } from './groups-config.mjs';
import { GROUP_COMMERCIAL_SERVICE } from './semantic-human-review-v4.mjs';
import { normPhrase, stripInlineNegatives } from './keyword-classifier-v2.mjs';

export { GROUP_COMMERCIAL_SERVICE };

export const REVIEW_STATUSES = [
  'SEMANTICALLY REVIEWED',
  'RULE-SCREENED',
  'NEEDS CONTENT REVIEW',
  'OPERATOR HOLD',
];

export const FINAL_DECISIONS = [
  'ACTIVE COMMERCIAL',
  'ACTIVE NARROW',
  'CONTROLLED TEST',
  'REASSIGN GROUP',
  'EXCLUDE INFORMATIONAL',
  'EXCLUDE REGULATORY',
  'EXCLUDE DIY',
  'EXCLUDE EMPLOYMENT',
  'EXCLUDE EDUCATIONAL',
  'EXCLUDE TRAINING',
  'EXCLUDE DOWNLOAD',
  'EXCLUDE IRRELEVANT',
  'EXCLUDE DUPLICATE',
  'EXCLUDE TYPO',
  'HOLD AMBIGUOUS',
];

const GROUP_BY_ID = Object.fromEntries(GROUPS.map((g) => [g.id, g]));
const LANDING_BY_GROUP = Object.fromEntries(GROUPS.map((g) => [g.id, g.url]));

const PROHIBITED_REASONS = new Set([
  'clear_commercial_service_intent',
  'commercial_service_intent',
  'commercial query for group',
  'matches group',
  'yes',
]);

const OPERATOR_EXCLUDE_PATTERNS = [
  { re: /^как (подключить|установить|настроить|изменить|сделать|включить)/, decision: 'EXCLUDE DIY', reason: 'how_to_prefix_seeking_self_service' },
  { re: /инструкц|документац|руководств|пошагов/, decision: 'EXCLUDE INFORMATIONAL', reason: 'documentation_or_instruction_seek' },
  { re: /личный кабинет/, decision: 'EXCLUDE INFORMATIONAL', reason: 'personal_cabinet_access_not_service' },
  { re: /(с какого|когда начн|обязательн|подлеж|попадают под|без маркиров)/, decision: 'EXCLUDE REGULATORY', reason: 'regulatory_timeline_or_scope_research' },
  { re: /час[аы]? работы|ваканс|резюме|зарплат/, decision: 'EXCLUDE EMPLOYMENT', reason: 'employment_or_labor_market' },
  { re: /образован|высшее образование|без образования|без высшего/, decision: 'EXCLUDE EDUCATIONAL', reason: 'education_qualification_research_not_service_hire' },
  { re: /^(1с )?программист.*(образован|высшее|без образования)/, decision: 'EXCLUDE EDUCATIONAL', reason: 'programmer_education_requirements_not_service' },
  { re: /^образование программист/, decision: 'EXCLUDE EDUCATIONAL', reason: 'education_path_for_programmers_not_service' },
  { re: /скачать|торрент|кряк/, decision: 'EXCLUDE DOWNLOAD', reason: 'download_or_piracy' },
  { re: /обучен|курс|урок|экзамен/, decision: 'EXCLUDE TRAINING', reason: 'training_course_intent' },
  { re: /^вопрос программист/, decision: 'EXCLUDE INFORMATIONAL', reason: 'qa_forum_style_not_hire_intent' },
  { re: /^маркировка лекарств (препаратов|средств)$/, decision: 'EXCLUDE REGULATORY', reason: 'generic_pharma_listing_not_1c_service' },
  { re: /маркировка лекарств аптека$/, decision: 'CONTROLLED TEST', reason: 'pharmacy_retail_context_needs_narrow_ad_match' },
  { re: /тс пиот.*розница.*\d(\.\d)?$/, decision: 'CONTROLLED TEST', reason: 'retail_config_version_specific_ts_piot_setup' },
  { re: /тс пиот и 1с розница/, decision: 'CONTROLLED TEST', reason: 'retail_config_integration_ambiguous' },
  { re: /тс пиот честный знак 1с/, decision: 'CONTROLLED TEST', reason: 'ts_piot_and_marking_cross_domain' },
];

/** Stale v3 group_id overrides — reassignment before commercial gate */
const FORCED_REASSIGN = [
  { re: /маркиров.*(производств|ввод в оборот)/, to: 'CORV-G06-01', from: ['CORV-G06-06', 'CORV-G06-05', 'CORV-G06-07'] },
  { re: /тс пиот.*розница/, to: 'CORV-G08-01', from: ['CORV-G08-02', 'CORV-G05-03', 'CORV-G03-06'] },
  { re: /тс пиот.*розница.*\d/, to: 'CORV-G08-01', from: ['CORV-G08-02'] },
  { re: /внешн.*печатн.*форм/, to: 'CORV-G03-05', from: ['CORV-G03-03', 'CORV-G03-04'] },
  { re: /рмк|рабоч.*мест.*кассир/, to: 'CORV-G03-06', from: ['CORV-G05-03'] },
];

function literalInterpretation(p) {
  const tokens = p.split(/\s+/).slice(0, 8).join(' ');
  return `Дословно: запрос «${tokens}» в контексте 1С/учётных систем.`;
}

function inferUserNeed(p, groupId) {
  if (/не работает|ошибк|сбой/.test(p)) return `Срочная помощь при сбое — «${p.slice(0, 60)}»`;
  if (/настрой|подключ|интеграц/.test(p)) return `Заказ настройки/подключения — «${p.slice(0, 60)}»`;
  if (/доработ|изменить|печатн|отчет/.test(p)) return `Заказ доработки конфигурации — «${p.slice(0, 60)}»`;
  if (/маркиров|честный знак/.test(p)) return `Подключение маркировки в 1С — «${p.slice(0, 60)}»`;
  if (/тс пиот/.test(p)) return `Настройка/интеграция ТС ПИОТ — «${p.slice(0, 60)}»`;
  if (/программист|услуг/.test(p)) return `Поиск специалиста 1С — «${p.slice(0, 60)}»`;
  return `Коммерческая задача по теме группы ${groupId} — «${p.slice(0, 60)}»`;
}

function inferAlternative(p) {
  if (/^как /.test(p)) return 'Самостоятельное выполнение по инструкции';
  if (/с какого|когда|обязательн/.test(p)) return 'Уточнение нормативных сроков без заказа услуги';
  if (/вопрос /.test(p)) return 'Получение ответа на форуме/Q&A';
  if (/аптека/.test(p) && /маркиров/.test(p)) return 'Розничная аптека ищет нормативную информацию';
  if (/розница.*\d/.test(p)) return 'Поиск версии конфигурации или документации';
  return 'Информационный или смешанный интент без явного заказа услуги';
}

function findMatchingGroups(kw) {
  const np = normPhrase(kw.normalized_phrase || kw.source_phrase);
  const fake = { ...kw, normalized_phrase: np };
  return GROUPS.filter((g) => g.filter(fake)).sort((a, b) => b.priority - a.priority);
}

function hasWaterToken(p) {
  return /(?:^|\s)вод(?:а|ы)?(?:\s|$)|маркиров(?:ка|ки|ку)?\s+вод|вода\s+маркиров/.test(p);
}

function scoreGroupFit(p, groupId) {
  const g = GROUP_BY_ID[groupId];
  if (!g) return { score: 0, reason: 'unknown_group' };

  let score = 50;
  const reasons = [];

  if (groupId === 'CORV-G06-06' && hasWaterToken(p)) {
    score += 40;
    reasons.push('explicit_water_token');
  } else if (groupId === 'CORV-G06-06' && !hasWaterToken(p)) {
    score -= 35;
    reasons.push('water_group_without_water_token');
  }

  if (/производств|ввод в оборот|в оборот/.test(p) && (groupId === 'CORV-G06-01' || groupId === 'CORV-G06-02')) {
    score += 35;
    reasons.push('general_marking_circulation_or_production');
  }

  if (/лекарств/.test(p) && groupId === 'CORV-G06-08') {
    score += 30;
    reasons.push('pharma_marking_group');
  }

  if (/тс пиот/.test(p) && groupId.startsWith('CORV-G08')) {
    score += 25;
    reasons.push('ts_piot_specialist_group');
  }
  if (/тс пиот.*розница/.test(p) && groupId === 'CORV-G08-01') {
    score += 20;
    reasons.push('retail_ts_piot_setup_not_pure_integration');
  }
  if (/тс пиот.*розница/.test(p) && groupId === 'CORV-G08-02' && !/интеграц|модуль|связ/.test(p)) {
    score -= 25;
    reasons.push('integration_group_for_setup_phrase');
  }

  if (/внешн.*печатн|внешн.*отчет|внешн.*обработ/.test(p) && groupId === 'CORV-G03-05') {
    score += 35;
    reasons.push('external_forms_group');
  }
  if (/внешн.*печатн/.test(p) && groupId === 'CORV-G03-03') {
    score -= 20;
    reasons.push('generic_print_forms_not_external');
  }

  if (/рмк|кассир/.test(p) && groupId === 'CORV-G03-06') {
    score += 30;
    reasons.push('rmk_group');
  }
  if (/синхрон|обмен/.test(p) && !/не работ/.test(p) && (groupId === 'CORV-G05-04' || groupId === 'CORV-G05-05')) {
    score += 25;
    reasons.push('sync_exchange_group');
  }
  if (/битрикс/.test(p) && groupId === 'CORV-G05-02') {
    score += 40;
    reasons.push('bitrix_integration_group');
  }
  if (/сайт/.test(p) && !/битрикс/.test(p) && groupId === 'CORV-G05-01') {
    score += 35;
    reasons.push('website_integration_group');
  }

  if (g.filter({ normalized_phrase: p, cluster: kwCluster(p) })) {
    score += 15;
    reasons.push('group_filter_match');
  }

  return { score: Math.max(0, Math.min(100, score)), reason: reasons.join('; ') || 'baseline_fit' };
}

function kwCluster(p) {
  if (/тс пиот/.test(p)) return 'D_ts_piot';
  if (/маркиров|честный знак/.test(p)) return 'D_labeling';
  if (/интеграц|синхрон|обмен/.test(p)) return 'C_integrations';
  if (/доработ/.test(p)) return 'A_modification';
  if (/отчет/.test(p)) return 'B_reports';
  if (/печатн/.test(p)) return 'B_forms';
  return 'A_broad_commercial';
}

function buildPhraseReason(p, decision, groupId, extra = {}) {
  const svc = GROUP_COMMERCIAL_SERVICE[groupId] || GROUP_BY_ID[groupId]?.name || groupId;
  if (decision.startsWith('EXCLUDE')) {
    return `${decision}: «${p}» — ${extra.rule || extra.alt || inferAlternative(p)}; не соответствует платной услуге «${svc}».`;
  }
  if (decision === 'CONTROLLED TEST') {
    return `CONTROLLED TEST: «${p}» — смешанный интент; риск: ${extra.risk || inferAlternative(p)}; услуга: ${svc}.`;
  }
  if (decision === 'REASSIGN GROUP') {
    return `REASSIGN: «${p}» из ${extra.from} в ${extra.to} — ${extra.reassign_reason}.`;
  }
  return `ACTIVE: «${p}» — заказ услуги «${svc}»; ключевые сигналы: ${extra.signals || p.split(/\s+/).slice(0, 5).join(', ')}.`;
}

function isTemplateReason(reason) {
  if (!reason) return true;
  if (PROHIBITED_REASONS.has(reason)) return true;
  if (/^Коммерческий запрос по услуге группы CORV/.test(reason)) return true;
  return false;
}

function evaluateAdLanding(p, groupId, decision) {
  if (!decision.startsWith('ACTIVE') && decision !== 'CONTROLLED TEST') {
    return { ad: 'n/a', landing: 'n/a' };
  }
  const g = GROUP_BY_ID[groupId];
  const landing = LANDING_BY_GROUP[groupId];
  let adFit = 'partial';
  let landingFit = 'partial';

  if (groupId === 'CORV-G06-06' && !hasWaterToken(p)) adFit = 'mismatch';
  else if (groupId === 'CORV-G08-02' && /розница.*\d/.test(p) && !/интеграц/.test(p)) adFit = 'mismatch';
  else if (/1с|настрой|доработ|маркиров|интеграц|программист/.test(p)) adFit = 'match';

  if (landing && adFit !== 'mismatch') landingFit = 'planned_url_match';
  if (adFit === 'mismatch') landingFit = 'wrong_service_page';

  return { ad: adFit, landing: landingFit, group_name: g?.name };
}

function resolveGroup(kw) {
  const p = normPhrase(stripInlineNegatives(kw.source_phrase || kw.ad_phrase || kw.normalized_phrase));
  let groupId = kw.group_id;
  let reassigned = false;
  let reassignMeta = null;

  for (const rule of FORCED_REASSIGN) {
    if (rule.re.test(p) && rule.from.includes(groupId)) {
      reassignMeta = { from: groupId, to: rule.to, reassign_reason: `pattern ${rule.re.source} → general owner ${rule.to}` };
      groupId = rule.to;
      reassigned = true;
      break;
    }
  }

  const matches = findMatchingGroups({ ...kw, normalized_phrase: p, group_id: groupId });
  const best = matches[0];
  if (best && best.id !== groupId && !reassigned) {
    const curScore = scoreGroupFit(p, groupId).score;
    const bestScore = scoreGroupFit(p, best.id).score;
    if (bestScore > curScore + 10) {
      reassignMeta = {
        from: groupId,
        to: best.id,
        reassign_reason: `filter_priority ${best.priority} vs current score ${curScore}→${bestScore}`,
      };
      groupId = best.id;
      reassigned = true;
    }
  }

  return { p, groupId, reassigned, reassignMeta, matches: matches.map((g) => g.id).slice(0, 5) };
}

export function reviewKeywordEvidenceV5(kw, opts = {}) {
  const raw = kw.source_phrase || kw.ad_phrase || kw.normalized_phrase || '';
  const positive = stripInlineNegatives(raw);
  const { p, groupId, reassigned, reassignMeta, matches } = resolveGroup({ ...kw, source_phrase: positive });

  let decision = 'ACTIVE COMMERCIAL';
  let commercialConfidence = 'HIGH';
  let reviewStatus = 'SEMANTICALLY REVIEWED';
  let reviewerMethod = 'phrase_contextual_v5';
  let ruleHit = null;

  for (const pat of OPERATOR_EXCLUDE_PATTERNS) {
    if (pat.re.test(p)) {
      decision = pat.decision;
      commercialConfidence = pat.decision === 'CONTROLLED TEST' ? 'MEDIUM' : 'LOW';
      ruleHit = pat;
      break;
    }
  }

  if (!ruleHit) {
    if (/^как /.test(p)) {
      decision = 'EXCLUDE DIY';
      commercialConfidence = 'LOW';
    } else if (kw.intent_class === 'informational') {
      decision = 'EXCLUDE INFORMATIONAL';
      commercialConfidence = 'LOW';
    } else if (kw.intent_class === 'regulatory') {
      decision = 'EXCLUDE REGULATORY';
      commercialConfidence = 'LOW';
    } else if (kw.commercial_relevance === 'low') {
      decision = 'HOLD AMBIGUOUS';
      commercialConfidence = 'LOW';
      reviewStatus = 'NEEDS CONTENT REVIEW';
    } else if (kw.commercial_relevance === 'medium' || kw.intent_class === 'commercial-mixed') {
      decision = 'CONTROLLED TEST';
      commercialConfidence = 'MEDIUM';
    } else if (/версия|8\.3|7\.7|3\.0/.test(p) && !/доработ|обновлен|ошибк|не работает|тс пиот/.test(p)) {
      decision = 'CONTROLLED TEST';
      commercialConfidence = 'MEDIUM';
    }
  }

  if (reassigned && isActiveDecision({ decision })) {
    decision = 'REASSIGN GROUP';
  }

  const groupFit = scoreGroupFit(p, groupId);
  if (groupFit.score < 40 && isActiveDecision({ decision: decision === 'REASSIGN GROUP' ? 'ACTIVE COMMERCIAL' : decision })) {
    if (decision === 'ACTIVE COMMERCIAL') {
      decision = groupFit.score < 25 ? 'HOLD AMBIGUOUS' : 'CONTROLLED TEST';
      commercialConfidence = 'MEDIUM';
      reviewStatus = 'NEEDS CONTENT REVIEW';
    }
  }

  if (commercialConfidence === 'LOW' && decision === 'ACTIVE COMMERCIAL') {
    decision = 'CONTROLLED TEST';
    commercialConfidence = 'MEDIUM';
  }

  const fit = evaluateAdLanding(p, reassignMeta?.to || groupId, decision === 'REASSIGN GROUP' ? 'ACTIVE COMMERCIAL' : decision);
  if (fit.ad === 'mismatch' && decision === 'ACTIVE COMMERCIAL') {
    decision = 'CONTROLLED TEST';
    commercialConfidence = 'MEDIUM';
  }

  const finalGroup = reassignMeta?.to || groupId;
  const reason = buildPhraseReason(p, decision, finalGroup, {
    rule: ruleHit?.reason,
    from: reassignMeta?.from,
    to: reassignMeta?.to,
    reassign_reason: reassignMeta?.reassign_reason,
    risk: inferAlternative(p),
    signals: p.split(/\s+/).filter((w) => w.length > 2).slice(0, 6).join(', '),
  });

  if (isTemplateReason(reason)) reviewStatus = 'RULE-SCREENED';
  else if (decision === 'HOLD AMBIGUOUS') reviewStatus = 'NEEDS CONTENT REVIEW';

  const hireEvidence =
    /услуг|заказ|специалист|аутсорс|доработ|настрой|подключ|не работает|ошибк|программист/.test(p) &&
    !decision.startsWith('EXCLUDE');

  return {
    keyword_id: kw.keyword_id,
    raw_phrase: raw,
    positive_phrase: positive,
    normalized_phrase: p,
    current_group: kw.group_id,
    assigned_group: finalGroup,
    group_reassigned: reassigned,
    reassign_meta: reassignMeta,
    candidate_groups: matches,
    literal_interpretation: literalInterpretation(p),
    likely_user_need: inferUserNeed(p, finalGroup),
    hire_intent_evidence: hireEvidence,
    paid_service_implied: GROUP_COMMERCIAL_SERVICE[finalGroup] || '',
    alternative_interpretation: inferAlternative(p),
    commercial_confidence: commercialConfidence,
    group_fit_confidence: groupFit.score >= 70 ? 'HIGH' : groupFit.score >= 45 ? 'MEDIUM' : 'LOW',
    group_fit_score: groupFit.score,
    group_fit_reason: groupFit.reason,
    ad_fit_result: fit.ad,
    landing_fit_result: fit.landing,
    final_decision: decision,
    phrase_specific_reason: reason,
    reviewer_method: reviewerMethod,
    review_status: reviewStatus,
    reviewed_at: opts.reviewed_at || new Date().toISOString(),
  };
}

export function isActiveDecision(review) {
  const d = review.final_decision || review.decision;
  return (
    d === 'ACTIVE COMMERCIAL' ||
    d === 'ACTIVE NARROW' ||
    d === 'CONTROLLED TEST' ||
    d === 'REASSIGN GROUP'
  );
}

export function buildSemanticEvidenceRegistry(keywords, opts = {}) {
  const reviews = keywords.map((kw) => reviewKeywordEvidenceV5(kw, opts));
  return {
    registry_id: 'corv-semantic-evidence-review-v5',
    generated_at: new Date().toISOString(),
    review_method: 'phrase_specific_evidence_v5 — no template-only approvals',
    total_reviewed: reviews.length,
    stats: {
      semantically_reviewed: reviews.filter((r) => r.review_status === 'SEMANTICALLY REVIEWED').length,
      rule_screened: reviews.filter((r) => r.review_status === 'RULE-SCREENED').length,
      needs_content: reviews.filter((r) => r.review_status === 'NEEDS CONTENT REVIEW').length,
      active_commercial: reviews.filter((r) => r.final_decision === 'ACTIVE COMMERCIAL').length,
      controlled_test: reviews.filter((r) => r.final_decision === 'CONTROLLED TEST').length,
      reassigned: reviews.filter((r) => r.group_reassigned).length,
      excluded: reviews.filter((r) => r.final_decision.startsWith('EXCLUDE') || r.final_decision === 'HOLD AMBIGUOUS').length,
    },
    reviews,
  };
}

export function reviewsToMarkdown(registry) {
  const s = registry.stats;
  const lines = [
    '# Semantic Evidence Review — Корво Неро v5',
    '',
    `**Reviewed:** ${registry.total_reviewed} · **Semantically reviewed:** ${s.semantically_reviewed} · **Active:** ${s.active_commercial} · **Controlled test:** ${s.controlled_test} · **Excluded/Hold:** ${s.excluded} · **Reassigned:** ${s.reassigned}`,
    '',
    '## Method',
    '',
    'Each phrase has phrase-specific reason, group-fit score, and honest review_status. Template-only reasons prohibited.',
    '',
  ];
  const excluded = registry.reviews.filter((r) => r.final_decision.startsWith('EXCLUDE') || r.final_decision === 'HOLD AMBIGUOUS');
  lines.push('## Exclusions (sample)', '');
  for (const r of excluded.slice(0, 40)) {
    lines.push(`- \`${r.positive_phrase}\` → **${r.final_decision}** — ${r.phrase_specific_reason.slice(0, 120)}`);
  }
  lines.push('', '## Reassignments', '');
  for (const r of registry.reviews.filter((x) => x.group_reassigned).slice(0, 30)) {
    lines.push(`- \`${r.positive_phrase}\` ${r.current_group} → ${r.assigned_group}`);
  }
  return lines.join('\n');
}
