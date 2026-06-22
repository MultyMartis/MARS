#!/usr/bin/env node
/**
 * P0-I pilot phrase assessor v1 — heuristic tri-state candidate generator.
 * NOT semantic authority; produces assessor fixture input for integration runtime.
 */
import crypto from 'node:crypto';

const CAREER = [/ваканс/, /резюме/, /зарплат/, /стажиров/, /трудоустрой/, /hh\.ru/, /headhunter/, /ищу\s+работ/, /работа\s+программист/];
const EDU = [/обучени/, /курс(?!с)/, /урок/, /школ[аы]/, /сертификат/, /экзамен/, /учебник/, /тренинг/, /репетитор/];
const DOWNLOAD = [/скачать/, /торрент/, /бесплатн.*скач/, /crack/, /кряк/, /демо\s*верси/];
const LOGIN = [/личн.*кабинет/, /\bвход\b/, /авторизац/, /\blogin\b/];
const NAV = [/corvonero/, /корво\s*неро/, /1с\.ру/, /официальн.*сайт.*1с/];
const DIY = [/своими\s+руками/, /как\s+сделать\s+сам/, /самостоятельно\s+(настро|установ|внедр|сделать)/, /инструкци[яи]\s+как/];
const INFO = [/что\s+такое/, /форум/, /wiki/, /википед/, /справк[аи]/, /документаци/];
const REG = [/закон.*маркиров/, /требовани.*маркиров/, /норматив.*маркиров/, /приказ.*маркиров/];
const COMMERCIAL_HIRE = [/заказать/, /услуг[аи]/, /на\s+аутсорс/, /под\s+ключ/, /найти\s+программист/, /нужен\s+программист/, /ищу\s+программист/, /консультаци/, /аудит\s+1с/, /стоимость/, /цена/, /прайс/, /сколько\s+стоит/, /контакт/];
const IMPL = [/внедрен/, /настройк/, /установк/, /миграци/, /переход\s+на\s+1с/];
const MOD_INT = [/доработ/, /интеграц/, /обмен\s+с/, /синхронизац/, /доработать/];
const SUPPORT = [/не\s+работ/, /ошибк/, /завис/, /не\s+запуск/, /не\s+открыв/, /вылетает/, /сломал/, /восстанов/, /починить/, /исправить/];
const PRODUCT_CFG = [/1с\s*:\s*/, /управлени[ея]\s+торговл/, /управлени[ея]\s+нашей\s+фирм/, /комплексн.*автоматизац/, /бухгалтери[яи]\s+предприят/, /1с\s+розниц/, /\bут\b/, /\bунф\b/, /\bбп\b/, /\bка\b/];

export function normalizePhrase(raw) {
  let t = String(raw ?? '').trim().toLowerCase().replace(/ё/g, 'е');
  t = t.replace(/["«»""'']/g, '');
  t = t.replace(/[.,;:!?…]+/g, ' ').replace(/\s+/g, ' ').trim();
  const tokens = t ? t.split(' ') : [];
  const malformed = !t || t.length < 2 || /^[\d\s+\-!|()]+$/.test(t);
  const shortHead = tokens.length <= 2 && t.length <= 15;
  return { normalized: t, tokens, malformed, shortHead };
}

function signal(id, strength, span) {
  return { signal_id: id, strength, evidence_span: span, conflict_flag: false };
}

export function assessPhrase(rawQuery, normalizedQuery) {
  const norm = normalizePhrase(normalizedQuery || rawQuery);
  const p = norm.normalized;
  const ambiguityTypes = [];
  let severity = 'LOW';
  const competing = [];
  const unresolved = [];
  const signals = [];
  let primaryIntent = 'UNKNOWN';
  let likelyGoal = 'UNKNOWN';
  let literal = 'Не оценено автоматически';
  let decision = 'ABSTAIN';
  let reasonCode = 'NOT_ASSESSED';
  let supporting = [];
  let opposing = [];
  let confidence = 0.5;
  let reviewerRequired = true;
  let risk = 'LOW';
  let protectedStrataConflict = false;
  let assessorDisagreement = false;

  if (norm.malformed) {
    ambiguityTypes.push('MALFORMED');
    severity = 'HIGH';
    return buildAssessor({
      primaryIntent: 'MALFORMED', likelyGoal: 'UNKNOWN', literal: 'Некорректная фраза',
      signals, ambiguityTypes, severity, competing, unresolved,
      decision: 'REJECT', reasonCode: 'MALFORMED_QUERY', supporting: [], opposing: [p],
      confidence: 0.85, reviewerRequired: false, risk: 'LOW',
    });
  }

  if (norm.shortHead) {
    ambiguityTypes.push('SHORT_HEAD_TERM');
    severity = 'HIGH';
    unresolved.push('Короткая фраза — недостаточно контекста');
  }

  const isCareer = CAREER.some((r) => r.test(p));
  const isEdu = EDU.some((r) => r.test(p)) && !COMMERCIAL_HIRE.some((r) => r.test(p));
  const isDiy = DIY.some((r) => r.test(p));
  const isDownload = DOWNLOAD.some((r) => r.test(p));
  const isLogin = LOGIN.some((r) => r.test(p));
  const isNav = NAV.some((r) => r.test(p));
  const isInfo = INFO.some((r) => r.test(p)) && !/(1с|маркиров)/.test(p);
  const isReg = REG.some((r) => r.test(p)) && !/(настрой|внедр|услуг|программист)/.test(p);
  const isSupport = SUPPORT.some((r) => r.test(p));
  const isProduct = PRODUCT_CFG.some((r) => r.test(p)) && !/(программист|услуг|настрой|внедр|доработ|сопровожд)/.test(p);
  const isHire = COMMERCIAL_HIRE.some((r) => r.test(p)) || /программист|специалист|разработчик|внедрен|настройк|доработ|сопровожд|обслужив|интеграц|аудит|консультац/.test(p);
  const in1c = /(1с|1c|маркиров|честн|битрикс)/i.test(p);

  if (isCareer) {
    primaryIntent = 'CAREER_EMPLOYMENT';
    likelyGoal = 'FIND_EMPLOYMENT';
    literal = 'Поиск работы или вакансий';
    signals.push(signal('CAREER_INTENT', 'EXPLICIT', p.match(/ваканс|работа|резюме/)?.[0] || 'career'));
    if (isHire) { ambiguityTypes.push('CAREER_VS_PROVIDER'); severity = 'HIGH'; protectedStrataConflict = true; }
    decision = 'REJECT';
    reasonCode = 'PROTECTED_CAREER_STRATUM';
    opposing = ['career_pattern'];
    confidence = 0.88;
    reviewerRequired = protectedStrataConflict;
    return buildAssessor({ primaryIntent, likelyGoal, literal, signals, ambiguityTypes, severity, competing, unresolved, decision, reasonCode, supporting, opposing, confidence, reviewerRequired, risk });
  }

  if (isEdu) {
    primaryIntent = 'EDUCATION';
    likelyGoal = 'LEARN_SKILL';
    literal = 'Обучение или курсы';
    signals.push(signal('EDUCATION_INTENT', 'EXPLICIT', 'обучение'));
    decision = 'REJECT';
    reasonCode = 'PROTECTED_EDUCATION_STRATUM';
    opposing = ['education_pattern'];
    confidence = 0.86;
    reviewerRequired = false;
    return buildAssessor({ primaryIntent, likelyGoal, literal, signals, ambiguityTypes, severity, competing, unresolved, decision, reasonCode, supporting, opposing, confidence, reviewerRequired, risk });
  }

  if (isDiy) {
    primaryIntent = 'DIY_HOW_TO';
    likelyGoal = 'SELF_SERVICE';
    literal = 'Самостоятельное выполнение';
    signals.push(signal('DIY_INTENT', 'EXPLICIT', 'diy'));
    ambiguityTypes.push('PROVIDER_VS_DIY');
    severity = isHire ? 'HIGH' : 'MEDIUM';
    if (isHire) protectedStrataConflict = true;
    decision = protectedStrataConflict ? 'ABSTAIN' : 'REJECT';
    reasonCode = protectedStrataConflict ? 'PROVIDER_DIY_CONFLICT' : 'PROTECTED_DIY_STRATUM';
    opposing = ['diy_pattern'];
    confidence = 0.8;
    reviewerRequired = true;
    return buildAssessor({ primaryIntent, likelyGoal, literal, signals, ambiguityTypes, severity, competing, unresolved, decision, reasonCode, supporting, opposing, confidence, reviewerRequired, risk });
  }

  if (isDownload) {
    primaryIntent = 'DOWNLOAD_FREE';
    decision = 'REJECT';
    reasonCode = 'PROTECTED_DOWNLOAD_STRATUM';
    literal = 'Скачивание или бесплатные материалы';
    opposing = ['download_pattern'];
    confidence = 0.9;
    reviewerRequired = false;
    return buildAssessor({ primaryIntent, likelyGoal: 'OBTAIN_FREE', literal, signals, ambiguityTypes, severity, competing, unresolved, decision, reasonCode, supporting, opposing, confidence, reviewerRequired, risk });
  }

  if (isLogin || isNav) {
    primaryIntent = isLogin ? 'LOGIN_ACCOUNT' : 'NAVIGATIONAL';
    decision = 'REJECT';
    reasonCode = 'PROTECTED_NAVIGATIONAL_STRATUM';
    literal = isLogin ? 'Вход в кабинет' : 'Навигационный запрос';
    opposing = ['nav_pattern'];
    confidence = 0.88;
    reviewerRequired = false;
    return buildAssessor({ primaryIntent, likelyGoal: 'NAVIGATE', literal, signals, ambiguityTypes, severity, competing, unresolved, decision, reasonCode, supporting, opposing, confidence, reviewerRequired, risk });
  }

  if (isInfo) {
    primaryIntent = 'INFORMATIONAL';
    decision = 'REJECT';
    reasonCode = 'PROTECTED_INFORMATIONAL_STRATUM';
    literal = 'Справочная информация';
    opposing = ['informational_pattern'];
    confidence = 0.75;
    reviewerRequired = false;
    return buildAssessor({ primaryIntent, likelyGoal: 'LEARN_TOPIC', literal, signals, ambiguityTypes, severity, competing, unresolved, decision, reasonCode, supporting, opposing, confidence, reviewerRequired, risk });
  }

  if (isReg) {
    primaryIntent = 'REGULATORY';
    ambiguityTypes.push('REGULATORY_VS_SERVICE');
    severity = 'MEDIUM';
    literal = 'Нормативные требования';
    if (isHire) {
      signals.push(signal('PROVIDER_HIRE', 'MEDIUM', 'service'));
      decision = 'ABSTAIN';
      reasonCode = 'REGULATORY_SERVICE_AMBIGUITY';
      reviewerRequired = true;
    } else {
      decision = 'REJECT';
      reasonCode = 'PROTECTED_REGULATORY_STRATUM';
      reviewerRequired = false;
    }
    confidence = 0.7;
    return buildAssessor({ primaryIntent, likelyGoal: 'UNDERSTAND_REGULATION', literal, signals, ambiguityTypes, severity, competing, unresolved, decision, reasonCode, supporting, opposing, confidence, reviewerRequired, risk });
  }

  if (isSupport) {
    primaryIntent = 'SUPPORT_SEEKING';
    ambiguityTypes.push('INTENT', 'PROVIDER_VS_DIY');
    severity = 'HIGH';
    unresolved.push('Проблемный запрос — услуга или самостоятельное решение?');
    literal = 'Проблема с работой системы';
    signals.push(signal('PROBLEM_QUERY', 'STRONG', p.match(/не\s+работ|ошибк|завис/)?.[0] || 'problem'));
    if (isHire) signals.push(signal('PROVIDER_HIRE', 'MEDIUM', 'hire'));
    decision = 'ABSTAIN';
    reasonCode = 'PROBLEM_QUERY_AMBIGUITY';
    confidence = 0.55;
    reviewerRequired = true;
    risk = 'MEDIUM';
    return buildAssessor({ primaryIntent, likelyGoal: 'RESOLVE_PROBLEM', literal, signals, ambiguityTypes, severity, competing, unresolved, decision, reasonCode, supporting, opposing, confidence, reviewerRequired, risk });
  }

  if (isProduct) {
    primaryIntent = 'COMMERCIAL_PRODUCT';
    ambiguityTypes.push('PRODUCT_VS_SERVICE');
    severity = 'HIGH';
    literal = 'Конфигурация или модуль 1С';
    signals.push(signal('PRODUCT_MODULE', 'STRONG', 'product'));
    if (isHire) {
      signals.push(signal('PROVIDER_HIRE', 'MEDIUM', 'hire'));
      decision = 'ABSTAIN';
      reasonCode = 'PRODUCT_SERVICE_AMBIGUITY';
    } else {
      decision = 'ABSTAIN';
      reasonCode = 'PRODUCT_WITHOUT_HIRE_SIGNAL';
    }
    confidence = 0.6;
    reviewerRequired = true;
    return buildAssessor({ primaryIntent, likelyGoal: 'ACQUIRE_PRODUCT', literal, signals, ambiguityTypes, severity, competing, unresolved, decision, reasonCode, supporting, opposing, confidence, reviewerRequired, risk });
  }

  if (in1c && isHire) {
    primaryIntent = 'HIRE_SERVICE';
    likelyGoal = 'HIRE_PROVIDER';
    literal = 'Запрос коммерческой услуги вокруг 1С';
    const hireSpan = p.match(/заказать|услуг|под ключ|программист|внедр|настройк|доработ|сопровожд|стоимость|цена|контакт/)?.[0] || 'commercial';
    signals.push(signal('PROVIDER_HIRE', COMMERCIAL_HIRE.some((r) => r.test(p)) ? 'EXPLICIT' : 'STRONG', hireSpan));
    if (IMPL.some((r) => r.test(p))) signals.push(signal('IMPLICATION_SERVICE', 'MEDIUM', 'implementation'));
    decision = norm.shortHead ? 'ABSTAIN' : 'ACCEPT';
    reasonCode = norm.shortHead ? 'SHORT_HEAD_COMMERCIAL' : 'EXPLICIT_PROVIDER_REQUEST';
    supporting = [hireSpan];
    confidence = norm.shortHead ? 0.45 : 0.82;
    reviewerRequired = norm.shortHead;
    risk = norm.shortHead ? 'MEDIUM' : 'LOW';
    return buildAssessor({ primaryIntent, likelyGoal, literal, signals, ambiguityTypes, severity, competing, unresolved, decision, reasonCode, supporting, opposing, confidence, reviewerRequired, risk });
  }

  if (in1c) {
    primaryIntent = 'COMMERCIAL_TOPIC';
    ambiguityTypes.push('INTENT');
    severity = norm.shortHead ? 'HIGH' : 'MEDIUM';
    literal = 'Тематический запрос 1С без явного найма';
    decision = 'ABSTAIN';
    reasonCode = 'TOPIC_ONLY_INSUFFICIENT_EVIDENCE';
    confidence = 0.4;
    reviewerRequired = true;
    risk = 'MEDIUM';
    return buildAssessor({ primaryIntent, likelyGoal: 'UNKNOWN', literal, signals, ambiguityTypes, severity, competing, unresolved, decision, reasonCode, supporting, opposing, confidence, reviewerRequired, risk });
  }

  if (norm.shortHead) {
    decision = 'ABSTAIN';
    reasonCode = 'SHORT_HEAD_UNKNOWN';
    reviewerRequired = true;
    risk = 'MEDIUM';
    return buildAssessor({ primaryIntent, likelyGoal, literal: 'Короткая неоднозначная фраза', signals, ambiguityTypes, severity: 'HIGH', competing, unresolved, decision, reasonCode, supporting, opposing, confidence: 0.35, reviewerRequired, risk });
  }

  decision = 'REJECT';
  reasonCode = 'OUT_OF_SCOPE_OR_UNKNOWN';
  primaryIntent = 'UNKNOWN';
  literal = 'Не относится к scope или недостаточно сигналов';
  confidence = 0.65;
  reviewerRequired = false;
  return buildAssessor({ primaryIntent, likelyGoal, literal, signals, ambiguityTypes, severity, competing, unresolved, decision, reasonCode, supporting, opposing, confidence, reviewerRequired, risk });
}

function buildAssessor(ctx) {
  return {
    assessor: {
      primary_intent: ctx.primaryIntent,
      likely_user_goal: ctx.likelyGoal,
      literal_interpretation: ctx.literal,
      signals: ctx.signals,
      ambiguity: {
        types: ctx.ambiguityTypes.length ? ctx.ambiguityTypes : ['NONE'],
        severity: ctx.severity,
        competing_interpretations: ctx.competing,
        unresolved_questions: ctx.unresolved,
      },
      risk: { overall_risk: ctx.risk, dimensions: {}, blocking_conditions: [] },
      commercial_eligibility: {
        decision: ctx.decision,
        reason_code: ctx.reasonCode,
        supporting_evidence: ctx.supporting,
        opposing_evidence: ctx.opposing,
        confidence: ctx.confidence,
        reviewer_required: ctx.reviewerRequired,
      },
    },
    protected_strata_conflict: ctx.protectedStrataConflict || false,
    assessor_disagreement: ctx.assessorDisagreement || false,
  };
}

export function classifyStratum(rawQuery) {
  const norm = normalizePhrase(rawQuery);
  const p = norm.normalized;
  if (norm.malformed) return 'ambiguous_malformed_noise';
  if (norm.shortHead) return 'ambiguous_short_head';
  if (CAREER.some((r) => r.test(p))) return 'protected_career';
  if (EDU.some((r) => r.test(p)) && !COMMERCIAL_HIRE.some((r) => r.test(p))) return 'protected_education';
  if (DIY.some((r) => r.test(p)) || /самостоятельно/.test(p)) return 'protected_diy_howto';
  if (DOWNLOAD.some((r) => r.test(p))) return 'protected_documentation_download_free';
  if (LOGIN.some((r) => r.test(p)) || NAV.some((r) => r.test(p))) return 'protected_navigational_login';
  if (REG.some((r) => r.test(p)) && !/(настрой|внедр|услуг|программист)/.test(p)) return 'protected_regulatory';
  if (INFO.some((r) => r.test(p)) && !/(1с|маркиров)/.test(p)) return 'protected_documentation_download_free';
  if (/стоимость|цена|прайс|сколько\s+стоит|контакт|тариф/.test(p)) return 'commercial_quote_price_contact';
  if (SUPPORT.some((r) => r.test(p))) {
    return /(программист|услуг|внедр|настройк|починить|восстанов)/.test(p)
      ? 'commercial_support_recovery'
      : 'ambiguous_problem_query';
  }
  if (MOD_INT.some((r) => r.test(p))) return 'commercial_modification_integration';
  if (IMPL.some((r) => r.test(p))) return 'commercial_implementation_configuration';
  if (COMMERCIAL_HIRE.some((r) => r.test(p)) || /программист|специалист|разработчик/.test(p)) {
    if (CAREER.some((r) => r.test(p))) return 'ambiguous_career_vs_provider';
    if (DIY.some((r) => r.test(p)) || /самостоятельно/.test(p)) return 'ambiguous_provider_vs_diy';
    return 'commercial_explicit_service_request';
  }
  if (PRODUCT_CFG.some((r) => r.test(p))) return 'ambiguous_product_vs_service';
  if (/(1с|1c)/i.test(p)) {
    if (SUPPORT.some((r) => r.test(p))) return 'ambiguous_support_vs_info';
    return 'ambiguous_product_vs_service';
  }
  return 'ambiguous_unknown';
}

export function sha256FileContent(content) {
  return crypto.createHash('sha256').update(content).digest('hex').toUpperCase();
}

export function sha256Json(obj) {
  return crypto.createHash('sha256').update(JSON.stringify(obj)).digest('hex').toUpperCase();
}

export function seededShuffle(arr, seed) {
  const a = [...arr];
  let s = crypto.createHash('sha256').update(String(seed)).digest().readUInt32BE(0);
  for (let i = a.length - 1; i > 0; i--) {
    s = (s * 1664525 + 1013904223) >>> 0;
    const j = s % (i + 1);
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}
