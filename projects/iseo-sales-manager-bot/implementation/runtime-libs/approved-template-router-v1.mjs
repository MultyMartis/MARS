/**
 * Approved Template Router v1 — INTLSEO first-contact standard.
 * Versions: reply_standard=iseo-first-contact-v1.0, reply_template=iseo-template-set-v1.0,
 *           reply_policy=iseo-sales-policy-v1.0
 * Precedence: T5 > T4 > T3 > T1 > T2 > safe fallback T2.
 */

export const REPLY_STANDARD_VERSION = 'iseo-first-contact-v1.0';
export const REPLY_TEMPLATE_VERSION = 'iseo-template-set-v1.0';
export const REPLY_POLICY_VERSION = 'iseo-sales-policy-v1.0';

export const TEMPLATE_IDS = Object.freeze({
  T1: 'T1_EXISTING_SITE_GROWTH',
  T2: 'T2_SITE_MISSING',
  T3: 'T3_MEANINGFUL_TASK',
  T4: 'T4_NEW_SITE_DEVELOPMENT',
  T5: 'T5_SPECIAL_PROJECT',
});

export const CTA_TYPES = Object.freeze({
  AUDIT_AGREEMENT: 'audit_agreement',
  OBTAIN_SITE_OR_CONFIRM_NONE: 'obtain_site_or_confirm_none',
  CLARIFY_DEV_STAGE: 'clarify_development_stage',
  OBTAIN_MATERIALS: 'obtain_materials',
});

/** Controlled theme → task_summary dictionary (AI OFF). */
export const TASK_SUMMARY_BY_THEME = Object.freeze({
  traffic_decline: 'разобраться, почему снизился поисковый трафик',
  conversion_low: 'увеличить конверсию сайта',
  growth_stalled: 'понять причины остановки роста и определить дальнейшие точки роста',
  seo_needed: 'запустить или усилить SEO-продвижение сайта',
  geo_ai_visibility: 'усилить видимость сайта в поиске и AI-ответах',
  brand_visibility: 'повысить видимость бренда в поиске',
  positions_decline: 'разобраться в причинах снижения позиций',
  leads_decline: 'понять, почему снизилось количество заявок из поиска',
  technical_site_problem: 'разобраться с техническими проблемами сайта',
  general_promotion: 'усилить продвижение сайта',
});

const SPECIAL_PROJECT_RE = /(?:^|[^\wа-яё])(?:суд(?:ебн|а|у|ом|ы)?|исков(?:ое|ые|ый)?|экспертн(?:ое|ый|ая)|заключен(?:ие|ия)|репутац(?:ия|ии|ионн)|юридич(?:еск|еский)|правов(?:ой|ые|ая)|арбитраж|компромат)(?=[^\wа-яё]|$)|больш(?:ой|ие)\s+объ[её]м\s+материал|пакет\s+документ|материалы\s+для\s+изучен/i;
const NEW_SITE_RE = /сайт\s+(ещ[её]\s+)?нужно\s+сделать|нужен\s+(новый\s+)?сайт|хочу\s+(новый\s+)?сайт|разработк[аи]\s+сайт|сделать\s+сайт|сайт\s+будем\s+создавать|сайт\s+будет\s+создан|сайт\s+в\s+разработк|нет\s+сайт|сайта\s+нет|сайт\s+отсутств/i;
const EXPLICIT_NO_SITE_RE = /сайта\s+нет|нет\s+сайт|сайт\s+отсутств|ещ[её]\s+нет\s+сайт|сайт\s+нужно\s+сделать/i;
const TRAFFIC_RE = /пада(ет|ют)?\s+трафик|снижен(ие|ия)\s+трафик|трафик\s+(падает|упал|снизил)|снизил(?:ся|ось|ись)?\s+(?:поисковый\s+)?трафик/i;
const CONVERSION_RE = /конверси/i;
const GROWTH_STALL_RE = /рост\s+(останов|перестал)|останов(ка|ился)\s+рост|перестал\s+расти/i;
const POSITIONS_RE = /снижен(ие|ия)\s+позиц|позици[ия]\s+(падают|упали|снизил)|упали\s+позици/i;
const LEADS_DECLINE_RE = /снизил(?:ось|ись|ся)?\s+(?:число|количество)?\s*(?:заявок|лидов)|заявк[аи]\s+(падают|упали|снизил)|меньше\s+заявок/i;
const GEO_AI_RE = /\bgeo\b|\bai\b|гео|нейросет|chatgpt|алиса|ai[- ]?отве|видимость.{0,24}(ai|аи|нейро)/i;
const BRAND_RE = /видимост[ьи]\s+бренд|бренд.{0,20}видимост|узнаваемост/i;
const SEO_RE = /\bseo\b|продвижен|поисков(ое|ой)\s+продвиж|сео/i;
const TECH_RE = /ошибк|не\s+работает|баг|слом|\b404\b|\b500\b|техн(ическ|ическ)/i;
const INJECTION_RE = /ignore\s+(all\s+)?previous|system\s+prompt|выведи\s+систем|забудь\s+инструкц|override\s+template|ignore previous instructions/i;

function asText(v) {
  return String(v ?? '').trim();
}

function websiteProvided(ctx) {
  const state = asText(ctx.website_state).toLowerCase();
  if (state === 'provided' || state === 'valid' || state === 'ok') return true;
  if (state === 'explicitly_absent' || state === 'absent' || state === 'missing' || state === 'invalid') return false;
  const site = asText(ctx.website_normalized || ctx.website || ctx.site);
  if (!site) return false;
  if (isNonWebsiteValue(site)) return false;
  return /^(https?:\/\/)?([a-z0-9-]+\.)+[a-z]{2,}/i.test(site) || /^[a-z0-9-]+\.[a-z]{2,}(\/|$)/i.test(site);
}

export function isNonWebsiteValue(raw) {
  const v = asText(raw);
  if (!v) return true;
  if (/^[-—.…]+$/.test(v)) return true;
  if (/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v)) return true;
  if (/^(t\.me\/|telegram\.me\/|@)/i.test(v)) return true;
  if (/^\+?\d[\d\s\-()]{6,}$/.test(v)) return true;
  if (/^(ул\.|улица|г\.|город|индекс)/i.test(v)) return true;
  if (/^(whatsapp|viber|телефон|phone|email|почта)/i.test(v)) return true;
  return false;
}

function commentText(ctx) {
  return asText(ctx.comment_normalized || ctx.client_comment || ctx.comment || ctx.request_summary);
}

function hasMeaningfulComment(c) {
  if (!c || c.length < 12) return false;
  if (/^(seo|audit|аудит|директ|сайт|хочу сайт|нужен аудит)\.?$/i.test(c)) return false;
  return true;
}

export function detectControlledTheme(ctx) {
  const c = commentText(ctx);
  const service = asText(ctx.resolved_service || ctx.service);
  if (TRAFFIC_RE.test(c)) return 'traffic_decline';
  if (CONVERSION_RE.test(c)) return 'conversion_low';
  if (GROWTH_STALL_RE.test(c)) return 'growth_stalled';
  if (POSITIONS_RE.test(c)) return 'positions_decline';
  if (LEADS_DECLINE_RE.test(c)) return 'leads_decline';
  if (GEO_AI_RE.test(c) || /Alice|Алиса/i.test(c)) return 'geo_ai_visibility';
  if (BRAND_RE.test(c)) return 'brand_visibility';
  if (TECH_RE.test(c)) return 'technical_site_problem';
  if (SEO_RE.test(c) || /SEO/i.test(service)) return 'seo_needed';
  if (hasMeaningfulComment(c) && /продвиж|трафик|видимост|заявк|рост/i.test(c)) return 'general_promotion';
  return '';
}

export function buildDeterministicTaskSummary(theme) {
  const t = asText(theme);
  return TASK_SUMMARY_BY_THEME[t] || '';
}

export function shouldEnableGeoAiClause(ctx, templateId) {
  if (templateId !== TEMPLATE_IDS.T1) return false;
  const c = commentText(ctx);
  const blobs = [
    asText(ctx.resolved_service || ctx.service),
    asText(ctx.source_topic),
    asText(ctx.form_topic),
    asText(ctx.explicit_client_intent || ctx.resolved_semantic_intent || ctx.intent),
    c,
  ].join('\n');
  if (GEO_AI_RE.test(blobs)) return true;
  return false;
}

function isSpecialProject(ctx) {
  const c = commentText(ctx);
  if (SPECIAL_PROJECT_RE.test(c)) return true;
  if (parseBool(ctx.special_project_flag)) return true;
  const service = asText(ctx.resolved_service);
  if (/Special|Legal|Expert|Court/i.test(service)) return true;
  return false;
}

function isNewSiteDevelopment(ctx) {
  const c = commentText(ctx);
  const service = asText(ctx.resolved_service || ctx.service);
  const state = asText(ctx.website_state).toLowerCase();
  if (state === 'explicitly_absent') return true;
  if (/WebsiteDevelopment/i.test(service)) return true;
  if (NEW_SITE_RE.test(c)) return true;
  const site = asText(ctx.website_normalized || ctx.website || ctx.site);
  if (site && /^(example\.|test\.|placeholder|заглушка)/i.test(site)) return true;
  return false;
}

function parseBool(v) {
  return v === true || v === 'true' || v === 1 || v === '1';
}

function websiteForReply(ctx) {
  if (!websiteProvided(ctx)) return '';
  let site = asText(ctx.website_normalized || ctx.website || ctx.site);
  site = site.replace(/^https?:\/\//i, '').replace(/\/$/, '');
  if (isNonWebsiteValue(site)) return '';
  return site;
}

/**
 * Route one semantic lead context to an approved template.
 */
export function routeApprovedTemplate(ctx = {}) {
  const warnings = [];
  const c = commentText(ctx);
  if (INJECTION_RE.test(c)) {
    warnings.push('prompt_injection_ignored');
  }

  const special = isSpecialProject(ctx);
  const development = isNewSiteDevelopment(ctx);
  const theme = detectControlledTheme(ctx);
  const taskSummary = buildDeterministicTaskSummary(theme);
  const siteOk = websiteProvided(ctx);
  const siteRaw = asText(ctx.website || ctx.site || ctx.website_raw);
  const siteMissing = !siteOk;
  const developmentStage = EXPLICIT_NO_SITE_RE.test(c) || asText(ctx.website_state).toLowerCase() === 'explicitly_absent'
    ? 'confirmed_absent'
    : (development ? 'development_requested' : (siteOk ? 'existing' : 'unknown'));

  let selected_template_id = TEMPLATE_IDS.T2;
  let selected_template_reason = 'fallback_site_missing_or_ambiguous';
  let selected_cta_type = CTA_TYPES.OBTAIN_SITE_OR_CONFIRM_NONE;
  let routing_confidence = 0.55;

  // Precedence 1: T5
  if (special) {
    selected_template_id = TEMPLATE_IDS.T5;
    selected_template_reason = 'special_or_legal_or_materials_project';
    selected_cta_type = CTA_TYPES.OBTAIN_MATERIALS;
    routing_confidence = 0.92;
  } else if (development && (!siteOk || developmentStage !== 'existing')) {
    // Precedence 2: T4 (over T2)
    selected_template_id = TEMPLATE_IDS.T4;
    selected_template_reason = 'new_site_or_development';
    selected_cta_type = CTA_TYPES.CLARIFY_DEV_STAGE;
    routing_confidence = 0.9;
  } else if (theme && taskSummary && hasMeaningfulComment(c) && !/^vague/i.test(theme)) {
    // Precedence 3: T3 meaningful task (over T1 even with site)
    selected_template_id = TEMPLATE_IDS.T3;
    selected_template_reason = 'meaningful_described_task';
    selected_cta_type = CTA_TYPES.AUDIT_AGREEMENT;
    routing_confidence = 0.88;
  } else if (siteOk) {
    // Precedence 4: T1
    selected_template_id = TEMPLATE_IDS.T1;
    selected_template_reason = 'valid_site_seo_geo_ai_or_growth';
    selected_cta_type = CTA_TYPES.AUDIT_AGREEMENT;
    routing_confidence = 0.86;
  } else if (siteMissing || isNonWebsiteValue(siteRaw)) {
    // Precedence 5: T2
    selected_template_id = TEMPLATE_IDS.T2;
    selected_template_reason = isNonWebsiteValue(siteRaw) && siteRaw
      ? 'website_field_non_website_value'
      : 'website_missing';
    selected_cta_type = CTA_TYPES.OBTAIN_SITE_OR_CONFIRM_NONE;
    routing_confidence = 0.84;
  } else {
    selected_template_id = TEMPLATE_IDS.T2;
    selected_template_reason = 'ambiguous_safe_fallback_t2';
    selected_cta_type = CTA_TYPES.OBTAIN_SITE_OR_CONFIRM_NONE;
    routing_confidence = 0.5;
    warnings.push('ambiguous_routing');
  }

  // If T3 theme empty but meaningful comment without controlled summary → prefer T1 when site exists
  if (selected_template_id === TEMPLATE_IDS.T3 && !taskSummary) {
    if (siteOk) {
      selected_template_id = TEMPLATE_IDS.T1;
      selected_template_reason = 'meaningful_comment_without_safe_summary_use_t1';
      selected_cta_type = CTA_TYPES.AUDIT_AGREEMENT;
      warnings.push('task_summary_unavailable_routed_t1');
      routing_confidence = 0.7;
    } else {
      selected_template_id = TEMPLATE_IDS.T2;
      selected_template_reason = 'meaningful_comment_without_summary_or_site';
      selected_cta_type = CTA_TYPES.OBTAIN_SITE_OR_CONFIRM_NONE;
      warnings.push('review_required_no_safe_summary');
      routing_confidence = 0.6;
    }
  }

  const geo_ai_clause_enabled = shouldEnableGeoAiClause(ctx, selected_template_id);
  const website_for_reply = selected_template_id === TEMPLATE_IDS.T1 ? websiteForReply(ctx) : '';

  return {
    selected_template_id,
    selected_template_reason,
    selected_cta_type,
    meaningful_task_theme: theme || '',
    geo_ai_clause_enabled,
    website_for_reply,
    deterministic_task_summary: selected_template_id === TEMPLATE_IDS.T3 ? taskSummary : '',
    special_project_flag: special,
    development_stage_state: developmentStage,
    routing_confidence,
    routing_warnings: warnings,
    reply_standard_version: REPLY_STANDARD_VERSION,
    reply_template_version: REPLY_TEMPLATE_VERSION,
    reply_policy_version: REPLY_POLICY_VERSION,
  };
}
