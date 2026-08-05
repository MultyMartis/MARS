/**
 * Approved Template Renderer v1 — INTLSEO first-contact templates.
 * Customer copy and manager guidance are always separated.
 * Sender name is snapshot-literal; AI must not rewrite it.
 */

import {
  DEFAULT_REPLY_COMPANY_NAME,
  introSentence,
  missingSenderNameWarning,
  resolveRecipientReplyProfile,
  RECIPIENT_PERSONALIZATION_VERSION,
} from './reply-profile-lib.mjs';
import {
  TEMPLATE_IDS,
  REPLY_STANDARD_VERSION,
  REPLY_TEMPLATE_VERSION,
  REPLY_POLICY_VERSION,
  routeApprovedTemplate,
} from './approved-template-router-v1.mjs';

export const MANAGER_ASSIST_VERSION = 'iseo-manager-assist-v1.0';
export const GENERATION_MODE = Object.freeze({
  DETERMINISTIC_TEMPLATE: 'DETERMINISTIC_TEMPLATE',
  AI_ASSISTED_TEMPLATE: 'AI_ASSISTED_TEMPLATE',
});

const FORBIDDEN_CLIENT_RE = [
  /гарантир/i,
  /в\s+топ[-\s]?1/i,
  /100\s*%/,
  /тариф/i,
  /стоимост[ьи].{0,20}\d/i,
  /за\s+\d+\s*(день|дня|дней|недел|месяц)/i,
  /мы\s+изучили\s+сайт/i,
  /мы\s+проверили\s+сайт/i,
  /telegram_user_id|chat_id|@\w{4,}/i,
  /SYNTHETIC_TEST|PHASE_3/i,
  /T1_EXISTING_SITE|routing_confidence|traffic_decline/i,
];

function joinBlocks(blocks) {
  return blocks.filter((b) => b !== null && b !== undefined && String(b).length).join('\n\n').replace(/\n{3,}/g, '\n\n').trim();
}

function humanTemplateLabel(id) {
  switch (id) {
    case TEMPLATE_IDS.T1: return '№1 — сайт указан, SEO/рост';
    case TEMPLATE_IDS.T2: return '№2 — сайт не указан';
    case TEMPLATE_IDS.T3: return '№3 — описана задача';
    case TEMPLATE_IDS.T4: return '№4 — новый сайт / разработка';
    case TEMPLATE_IDS.T5: return '№5 — спецпроект';
    default: return 'стандартный';
  }
}

function humanGoal(id) {
  switch (id) {
    case TEMPLATE_IDS.T1:
    case TEMPLATE_IDS.T3:
      return 'проверить актуальность и получить согласие на аудит';
    case TEMPLATE_IDS.T2:
      return 'уточнить, есть ли сайт, или подтвердить, что его нужно сделать';
    case TEMPLATE_IDS.T4:
      return 'уточнить стадию сайта и предложить разработку с SEO-структурой';
    case TEMPLATE_IDS.T5:
      return 'получить материалы для предварительной оценки';
    default:
      return 'уточнить следующий шаг';
  }
}

function humanNext(id) {
  switch (id) {
    case TEMPLATE_IDS.T1:
    case TEMPLATE_IDS.T3:
      return 'договориться о подготовке аудита и видеосозвоне';
    case TEMPLATE_IDS.T2:
      return 'после ответа предложить аудит или разработку сайта';
    case TEMPLATE_IDS.T4:
      return 'согласовать старт разработки и дальнейшее продвижение';
    case TEMPLATE_IDS.T5:
      return 'после изучения материалов вернуться с форматом и ориентиром по стоимости';
    default:
      return 'продолжить диалог по ответу клиента';
  }
}

export function buildDeterministicManagerGuidance(route, opts = {}) {
  const id = route.selected_template_id;
  const lines = [
    '💡 Подсказка менеджеру',
    `Тип заявки: ${opts.request_type_label || humanTemplateLabel(id)}`,
    `Выбран шаблон: ${humanTemplateLabel(id)}`,
    `Цель: ${humanGoal(id)}`,
    'Не обещать позиции, сроки или гарантированный рост',
    `После ответа клиента: ${humanNext(id)}`,
  ];
  if (route.deterministic_task_summary) {
    lines.splice(4, 0, `Кратко по задаче: ${route.deterministic_task_summary}`);
  }
  if (opts.ai_confidence != null && opts.generation_mode === GENERATION_MODE.AI_ASSISTED_TEMPLATE) {
    lines.push(`Уверенность ИИ-подсказки: ${opts.ai_confidence}`);
  }
  if (opts.extra_lines && Array.isArray(opts.extra_lines)) {
    for (const x of opts.extra_lines.slice(0, 3)) {
      if (x) lines.push(String(x));
    }
  }
  // Cap to ~4 most important body lines after header for Telegram safety (+ header)
  return lines.slice(0, 7).join('\n');
}

function renderT1(senderName, company, website, geoAi) {
  const geo = geoAi ? ', в том числе по GEO/AI-продвижению' : '';
  return joinBlocks([
    'Добрый день!',
    `${introSentence(senderName, company)} Вы оставляли заявку по сайту ${website}.`,
    'Подскажите, пожалуйста, заявка сейчас актуальна?',
    `Если да — посмотрим сайт и подготовим аудит, чтобы понять текущую ситуацию и точки роста${geo}.`,
    'Аудит разбираем на созвоне с командой в формате видео-презентации: показываем, что сейчас мешает заявкам и что нужно сделать. После — передаём все материалы.',
    'Делаем аудит?',
  ]);
}

function renderT2(senderName, company) {
  return joinBlocks([
    'Добрый день!',
    `${introSentence(senderName, company)} Вы оставляли заявку у нас на сайте.`,
    'Подскажите, пожалуйста:\n— у вас уже есть сайт или его нужно сделать?',
    'Если сайт есть — пришлите ссылку.',
    'Если нет — можем сначала сделать сайт, а затем запустить SEO и/или рекламу.',
    'После этого предложим оптимальный вариант.',
  ]);
}

function renderT3(senderName, company, taskSummary) {
  return joinBlocks([
    'Добрый день!',
    introSentence(senderName, company),
    'Спасибо за подробное описание задачи.',
    `Понял, что ваша цель — ${taskSummary}.`,
    'Предлагаю начать с аудита. Посмотрим сайт, подготовим рекомендации и покажем, какие работы дадут наибольший эффект.',
    'Аудит разбираем на созвоне с командой в формате видео-презентации: показываем текущую ситуацию, точки роста и дальнейший план работ. После — передаём все материалы.',
    'Делаем аудит?',
  ]);
}

function renderT4(senderName, company, developmentStage) {
  const blocks = ['Добрый день!', introSentence(senderName, company)];
  if (developmentStage === 'confirmed_absent') {
    blocks.push('Понял, что сайт ещё нужно сделать.');
  } else {
    blocks.push('Подскажите, пожалуйста:\n— сайт уже есть или его нужно сделать?');
  }
  blocks.push('Если сайт ещё не готов — можем сразу сделать его с правильной структурой под SEO и дальнейшее продвижение в поиске и AI-ответах.');
  blocks.push('После этого предложим оптимальный вариант запуска.');
  return joinBlocks(blocks);
}

function renderT5(senderName, company) {
  return joinBlocks([
    'Добрый день!',
    introSentence(senderName, company),
    'Спасибо за подробное описание задачи.',
    'Нам нужно сначала изучить материалы и понять объём работ.',
    'После этого сможем сказать, готовы ли взяться за проект, в каком формате и сориентировать по стоимости.',
    'Если удобно, пришлите материалы, после изучения вернёмся с ответом.',
  ]);
}

export function validateCustomerReply(text, ctx = {}) {
  const warnings = [];
  const t = String(text || '');
  if (!t) return { ok: false, reason: 'empty', warnings };
  if (!t.startsWith('Добрый день!')) {
    return { ok: false, reason: 'missing_greeting', warnings };
  }
  const sender = String(ctx.reply_sender_name || '').trim();
  const company = String(ctx.reply_company_name || DEFAULT_REPLY_COMPANY_NAME).trim();
  const expectedIntro = introSentence(sender, company);
  if (sender && !t.includes(expectedIntro)) {
    return { ok: false, reason: 'sender_sentence_mismatch', warnings };
  }
  if (!t.includes('INTLSEO') && !t.includes(company)) {
    return { ok: false, reason: 'missing_company', warnings };
  }
  for (const re of FORBIDDEN_CLIENT_RE) {
    if (re.test(t)) {
      warnings.push(`forbidden:${re}`);
      return { ok: false, reason: 'forbidden_content', warnings };
    }
  }
  if (t.length > 1200) {
    return { ok: false, reason: 'too_long', warnings };
  }
  const id = ctx.selected_template_id;
  if (id === TEMPLATE_IDS.T1 || id === TEMPLATE_IDS.T3) {
    if (!/Делаем аудит\?/.test(t)) return { ok: false, reason: 'missing_cta_audit', warnings };
    if (!/видео-презентац/i.test(t)) return { ok: false, reason: 'missing_video_presentation', warnings };
    if (!/передаём все материалы/i.test(t)) return { ok: false, reason: 'missing_materials_handoff', warnings };
  }
  if (id === TEMPLATE_IDS.T2 && !/пришлите ссылку/i.test(t)) {
    return { ok: false, reason: 'missing_cta_t2', warnings };
  }
  if (id === TEMPLATE_IDS.T5 && /Делаем аудит\?/.test(t)) {
    return { ok: false, reason: 'audit_cta_on_special_project', warnings };
  }
  if (id === TEMPLATE_IDS.T4 && /Делаем аудит\?/.test(t)) {
    return { ok: false, reason: 'audit_cta_on_new_site', warnings };
  }
  if (/💡 Подсказка менеджеру/.test(t)) {
    return { ok: false, reason: 'guidance_leaked_into_client_copy', warnings };
  }
  // Never show nickname Мопс in client copy
  if (/(^|[^\wа-яё])Мопс([^\wа-яё]|$)/i.test(t)) {
    return { ok: false, reason: 'nickname_leak', warnings };
  }
  return { ok: true, reason: 'ok', warnings };
}

function renderBody(route, senderName, company, aiFields = {}) {
  const id = route.selected_template_id;
  if (id === TEMPLATE_IDS.T1) {
    return renderT1(senderName, company, route.website_for_reply || 'сайта', route.geo_ai_clause_enabled);
  }
  if (id === TEMPLATE_IDS.T2) return renderT2(senderName, company);
  if (id === TEMPLATE_IDS.T3) {
    const summary = String(aiFields.task_summary || route.deterministic_task_summary || '').trim();
    if (!summary) return null;
    return renderT3(senderName, company, summary);
  }
  if (id === TEMPLATE_IDS.T4) return renderT4(senderName, company, route.development_stage_state);
  if (id === TEMPLATE_IDS.T5) return renderT5(senderName, company);
  return renderT2(senderName, company);
}

/**
 * Render personalized recipient reply.
 */
export function renderApprovedReply({
  leadContext = {},
  route = null,
  recipientProfileRow = {},
  generationMode = GENERATION_MODE.DETERMINISTIC_TEMPLATE,
  aiFields = null,
  generatedAt = null,
} = {}) {
  const routing = route || routeApprovedTemplate(leadContext);
  const profile = resolveRecipientReplyProfile(recipientProfileRow);
  const mode = generationMode === GENERATION_MODE.AI_ASSISTED_TEMPLATE
    ? GENERATION_MODE.AI_ASSISTED_TEMPLATE
    : GENERATION_MODE.DETERMINISTIC_TEMPLATE;
  const now = generatedAt || new Date().toISOString();

  const baseMeta = {
    template_id: routing.selected_template_id,
    template_version: REPLY_TEMPLATE_VERSION,
    policy_version: REPLY_POLICY_VERSION,
    standard_version: REPLY_STANDARD_VERSION,
    assist_version: MANAGER_ASSIST_VERSION,
    recipient_personalization_version: RECIPIENT_PERSONALIZATION_VERSION,
    generation_mode: mode,
    generated_at: now,
    selected_template_reason: routing.selected_template_reason,
    geo_ai_clause_enabled: routing.geo_ai_clause_enabled,
    deterministic_task_summary: routing.deterministic_task_summary,
    reply_sender_name_snapshot: profile.reply_sender_name,
    company_name_snapshot: profile.reply_company_name || DEFAULT_REPLY_COMPANY_NAME,
    copy_block_available: false,
    customer_reply_text: '',
    manager_guidance: '',
    recipient_reply_state: profile.recipient_reply_state,
    validation_result: 'blocked',
    validation_warnings: [],
  };

  if (!profile.personalization_ready) {
    return {
      ...baseMeta,
      manager_guidance: [
        missingSenderNameWarning(),
        '',
        buildDeterministicManagerGuidance(routing, { generation_mode: mode }),
      ].join('\n'),
      recipient_reply_state: 'blocked_missing_sender_name',
      validation_result: 'blocked_missing_sender_name',
    };
  }

  const acceptedAi = (mode === GENERATION_MODE.AI_ASSISTED_TEMPLATE && aiFields && aiFields.accepted)
    ? aiFields
    : null;

  let text = renderBody(routing, profile.reply_sender_name, profile.reply_company_name, {
    task_summary: acceptedAi?.task_summary || routing.deterministic_task_summary,
  });

  if (!text) {
    // Safe fallback: T1 if site else T2
    const fallbackRoute = {
      ...routing,
      selected_template_id: routing.website_for_reply ? TEMPLATE_IDS.T1 : TEMPLATE_IDS.T2,
      deterministic_task_summary: '',
    };
    text = renderBody(fallbackRoute, profile.reply_sender_name, profile.reply_company_name, {});
  }

  let validation = validateCustomerReply(text, {
    reply_sender_name: profile.reply_sender_name,
    reply_company_name: profile.reply_company_name,
    selected_template_id: routing.selected_template_id,
  });

  if (!validation.ok) {
    // One deterministic regeneration attempt via T2/T1 safe path
    const safeRoute = {
      ...routing,
      selected_template_id: routing.website_for_reply ? TEMPLATE_IDS.T1 : TEMPLATE_IDS.T2,
      geo_ai_clause_enabled: false,
      deterministic_task_summary: '',
    };
    text = renderBody(safeRoute, profile.reply_sender_name, profile.reply_company_name, {});
    validation = validateCustomerReply(text, {
      reply_sender_name: profile.reply_sender_name,
      reply_company_name: profile.reply_company_name,
      selected_template_id: safeRoute.selected_template_id,
    });
    if (!validation.ok) {
      return {
        ...baseMeta,
        manager_guidance: [
          '⚠️ Не удалось подготовить корректный черновик ответа.',
          '',
          buildDeterministicManagerGuidance(routing, { generation_mode: mode }),
        ].join('\n'),
        recipient_reply_state: 'blocked_validation_failed',
        validation_result: validation.reason,
        validation_warnings: validation.warnings,
      };
    }
  }

  const guidanceExtra = [];
  if (acceptedAi?.manager_note) guidanceExtra.push(String(acceptedAi.manager_note).slice(0, 240));
  if (acceptedAi?.follow_up_after_positive_reply) {
    guidanceExtra.push(`Далее: ${String(acceptedAi.follow_up_after_positive_reply).slice(0, 160)}`);
  }

  const manager_guidance = buildDeterministicManagerGuidance(routing, {
    generation_mode: mode,
    ai_confidence: acceptedAi?.confidence,
    extra_lines: guidanceExtra,
  });

  return {
    ...baseMeta,
    customer_reply_text: text,
    manager_guidance,
    copy_block_available: true,
    recipient_reply_state: 'ready',
    validation_result: 'pass',
    validation_warnings: validation.warnings,
  };
}

/**
 * Shared LEADS metadata (no personalized name).
 */
export function buildSharedReplyMetadata(route, generationMode = GENERATION_MODE.DETERMINISTIC_TEMPLATE) {
  return {
    selected_template_id: route.selected_template_id,
    selected_template_reason: route.selected_template_reason,
    reply_standard_version: REPLY_STANDARD_VERSION,
    reply_template_version: REPLY_TEMPLATE_VERSION,
    reply_policy_version: REPLY_POLICY_VERSION,
    reply_generation_mode: generationMode,
    deterministic_task_summary: route.deterministic_task_summary || '',
    geo_ai_clause_enabled: !!route.geo_ai_clause_enabled,
    reply_base_state: 'routed',
    reply_validation_state: 'pending_recipient_render',
    manager_assist_version: MANAGER_ASSIST_VERSION,
    // Keep legacy stamp for rollback history only
    first_reply_version_legacy: 'sm-reply-v2.1',
  };
}
