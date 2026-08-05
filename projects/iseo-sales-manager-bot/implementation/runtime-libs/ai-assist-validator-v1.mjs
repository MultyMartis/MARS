/**
 * AI Assist Validator v1 — constrained structured fields only.
 * Template, CTA, sender name, company remain immutable outside AI.
 * On rejection → deterministic fallback (never block lead delivery).
 */

import { GENERATION_MODE } from './approved-template-renderer-v1.mjs';
import { DEFAULT_REPLY_COMPANY_NAME } from './reply-profile-lib.mjs';

export const AI_ASSIST_SCHEMA_VERSION = 'iseo-ai-assist-schema-v1.0';
export const AI_TASK_SUMMARY_MAX = 120;
export const AI_MANAGER_NOTE_MAX = 400;
export const AI_FOLLOWUP_MAX = 200;

const GUARANTEE_RE = /гарантир|в\s+топ|100\s*%|обязательно\s+попад/i;
const PRICE_RE = /тариф|стоимост|руб\.|₽|\bUSD\b|\bEUR\b|\d[\d\s]{2,}\s*(руб|₽)/i;
const DEADLINE_RE = /за\s+\d+\s*(день|дня|дней|недел|месяц)|в\s+течение\s+\d+/i;
const REVIEWED_RE = /мы\s+(изучили|проверили|проанализировали)\s+сайт|аудит\s+уже\s+готов/i;
const HTML_RE = /<\/?[a-z][\s\S]*>/i;
const AI_INJECTION_RE = /ignore\s+(all\s+)?previous|system\s+prompt|<\/?(system|assistant)>/i;

export function buildAiAssistSystemPrompt({ templateId, senderNameLocked = true } = {}) {
  return [
    'Ты помощник менеджера INTLSEO. Шаблон первого ответа уже выбран и НЕ может быть заменён.',
    `selected_template_id=${templateId || 'LOCKED'}`,
    'Нельзя менять текст шаблона, CTA, имя отправителя и название компании.',
    'Верни ТОЛЬКО валидный JSON со полями: task_summary, manager_note, follow_up_after_positive_reply, risk_flags, confidence.',
    'task_summary — одна короткая фраза на русском без обещаний (макс. 1 предложение).',
    'manager_note — несколько кратких строк подсказки менеджеру, не клиенту.',
    'Не выдумывай факты о сайте, доступы к аналитике, цены, сроки, гарантии.',
    'Не включай телефон, email или другие контакты клиента.',
    senderNameLocked ? 'Имя отправителя задаётся вне модели и неизменяемо.' : '',
    'Компания всегда INTLSEO.',
  ].filter(Boolean).join('\n');
}

export function buildAiAssistUserPayload(leadContext = {}, route = {}) {
  // Sanitized minimum context — no phone/email/PII
  return {
    selected_template_id: route.selected_template_id,
    website_state: String(leadContext.website_state || ''),
    website_present: Boolean(route.website_for_reply),
    resolved_service: String(leadContext.resolved_service || leadContext.service || ''),
    comment_excerpt: String(leadContext.comment_normalized || leadContext.client_comment || '')
      .replace(/[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}/gi, '[email]')
      .replace(/\+?\d[\d\s\-()]{6,}\d/g, '[phone]')
      .slice(0, 400),
    meaningful_task_theme: route.meaningful_task_theme || '',
    deterministic_task_summary: route.deterministic_task_summary || '',
  };
}

function asString(v) {
  return String(v ?? '').trim();
}

function parseJsonLoose(raw) {
  if (raw && typeof raw === 'object' && !Array.isArray(raw)) return { ok: true, value: raw };
  let s = asString(raw);
  if (!s) return { ok: false, reason: 'empty' };
  // Strip markdown fences if present
  s = s.replace(/^```(?:json)?\s*/i, '').replace(/\s*```$/i, '').trim();
  try {
    return { ok: true, value: JSON.parse(s) };
  } catch {
    return { ok: false, reason: 'invalid_json' };
  }
}

/**
 * Validate AI structured output. Returns accepted fields or rejection.
 */
export function validateAiAssistOutput(raw, ctx = {}) {
  const warnings = [];
  const parsed = parseJsonLoose(raw);
  if (!parsed.ok) {
    return { accepted: false, reason: parsed.reason, warnings, fields: null };
  }
  const obj = parsed.value || {};
  const task_summary = asString(obj.task_summary);
  const manager_note = asString(obj.manager_note);
  const follow_up_after_positive_reply = asString(obj.follow_up_after_positive_reply);
  const risk_flags = Array.isArray(obj.risk_flags)
    ? obj.risk_flags.map((x) => asString(x)).filter(Boolean).slice(0, 5)
    : [];
  let confidence = obj.confidence;
  if (typeof confidence === 'string' && confidence) confidence = Number(confidence);
  if (typeof confidence !== 'number' || !Number.isFinite(confidence)) confidence = null;

  const blob = [task_summary, manager_note, follow_up_after_positive_reply, risk_flags.join(' ')].join('\n');

  if (HTML_RE.test(blob)) return { accepted: false, reason: 'contains_html', warnings, fields: null };
  if (AI_INJECTION_RE.test(blob)) return { accepted: false, reason: 'injection_artifact', warnings, fields: null };
  if (GUARANTEE_RE.test(blob)) return { accepted: false, reason: 'guarantee_language', warnings, fields: null };
  if (PRICE_RE.test(blob)) return { accepted: false, reason: 'price_language', warnings, fields: null };
  if (DEADLINE_RE.test(blob)) return { accepted: false, reason: 'deadline_language', warnings, fields: null };
  if (REVIEWED_RE.test(blob)) return { accepted: false, reason: 'unsupported_site_review_claim', warnings, fields: null };

  const lockedSender = asString(ctx.reply_sender_name);
  if (lockedSender) {
    // Reject if AI invents a different person name sentence
    if (/меня зовут\s+\S+/i.test(blob) && !new RegExp(`меня зовут\\s+${lockedSender.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}`, 'i').test(blob)) {
      return { accepted: false, reason: 'sender_name_changed', warnings, fields: null };
    }
  }
  if (/intlseo/i.test(blob) === false && /компания\s+\S+/i.test(blob) && !new RegExp(DEFAULT_REPLY_COMPANY_NAME, 'i').test(blob)) {
    // company rename attempt inside notes
    warnings.push('company_mention_checked');
  }
  if (/компания\s+(?!INTLSEO)\S+/i.test(blob)) {
    return { accepted: false, reason: 'company_changed', warnings, fields: null };
  }

  if (task_summary.length > AI_TASK_SUMMARY_MAX) {
    return { accepted: false, reason: 'task_summary_too_long', warnings, fields: null };
  }
  if (manager_note.length > AI_MANAGER_NOTE_MAX) {
    return { accepted: false, reason: 'manager_note_too_long', warnings, fields: null };
  }
  if (follow_up_after_positive_reply.length > AI_FOLLOWUP_MAX) {
    return { accepted: false, reason: 'followup_too_long', warnings, fields: null };
  }

  // Full unrestricted client message is forbidden
  if (/добрый день!/i.test(blob) || /делаем аудит\?/i.test(blob)) {
    return { accepted: false, reason: 'full_client_message_forbidden', warnings, fields: null };
  }

  if (!task_summary && !manager_note) {
    return { accepted: false, reason: 'no_usable_fields', warnings, fields: null };
  }

  return {
    accepted: true,
    reason: 'ok',
    warnings,
    fields: {
      task_summary,
      manager_note,
      follow_up_after_positive_reply,
      risk_flags,
      confidence,
      schema_version: AI_ASSIST_SCHEMA_VERSION,
    },
  };
}

/**
 * Decide generation mode from config. Production default remains AI OFF.
 */
export function resolveGenerationMode(config = {}) {
  if (config.ai_enabled === true || config.ai_enabled === 'true') {
    return GENERATION_MODE.AI_ASSISTED_TEMPLATE;
  }
  return GENERATION_MODE.DETERMINISTIC_TEMPLATE;
}

/**
 * Apply AI assist with deterministic fallback.
 */
export function applyAiAssistOrFallback(rawAi, ctx = {}) {
  const validated = validateAiAssistOutput(rawAi, ctx);
  if (!validated.accepted) {
    return {
      generation_mode: GENERATION_MODE.DETERMINISTIC_TEMPLATE,
      ai_status: 'fallback',
      fallback_used: true,
      validation_warning: validated.reason,
      fields: {
        accepted: false,
        task_summary: '',
        manager_note: '',
        follow_up_after_positive_reply: '',
        risk_flags: [],
        confidence: null,
      },
    };
  }
  return {
    generation_mode: GENERATION_MODE.AI_ASSISTED_TEMPLATE,
    ai_status: 'ok',
    fallback_used: false,
    validation_warning: '',
    fields: { accepted: true, ...validated.fields },
  };
}
