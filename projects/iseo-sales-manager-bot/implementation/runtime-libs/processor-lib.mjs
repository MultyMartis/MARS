/**
 * Phase 3E.2 — deterministic lead processor (semantic pass-through + First Reply v2).
 * Prefer Parser 3.3 semantic fields when present; AI OFF template replies only.
 */

import { isCommPreferenceOnly, SERVICE_COMPAT, buildFirstReplyDraft, assessLeadQuality, computeMissingInformation } from '../parser-fixtures/parse-lead-lib.mjs';
import { FIRST_REPLY_VERSION } from './first-reply-engine-v2.mjs';

export function isCommPreferenceText(text) {
  return isCommPreferenceOnly(text);
}

const INVALID_CONTACT = new Set([
  '44', '#error!', 'unknown', 'telegram', 'whatsapp', 'viber',
  'телефон', 'email', 'сайт', 'n/a', 'na', '-', '—', 'null', 'undefined',
  'phone', 'messenger', 'contact',
]);

function digits(p) { return String(p || '').replace(/\D/g, ''); }

function validPhone(p) {
  const raw = String(p || '').trim();
  if (!raw) return false;
  if (INVALID_CONTACT.has(raw.toLowerCase())) return false;
  const d = digits(raw);
  if (!d || d.length < 10 || d.length > 15) return false;
  if (INVALID_CONTACT.has(d)) return false;
  return true;
}

function validEmail(e) {
  const v = String(e || '').trim().toLowerCase();
  if (!v || INVALID_CONTACT.has(v) || v.length > 254) return false;
  return /^[^\s@]+@[^\s@]+\.[^\s@]{2,24}$/.test(v);
}

function validMessenger(m) {
  const v = String(m || '').trim();
  if (!v) return false;
  const low = v.toLowerCase();
  if (INVALID_CONTACT.has(low)) return false;
  if (/^@[a-zA-Z0-9_]{4,32}$/.test(v)) return true;
  if (/^(t\.me\/|telegram\.me\/|https?:\/\/(t\.me|telegram\.me)\/)[a-zA-Z0-9_]{4,}/i.test(v)) return true;
  if (/^(wa\.me\/|api\.whatsapp\.com\/|https?:\/\/(wa\.me|api\.whatsapp\.com)\/)/i.test(v)) return true;
  if (/^[a-zA-Z0-9_]{5,32}$/.test(v)) return true;
  return false;
}

export function processLeadDeterministic(j = {}) {
  const cfg = j.config || {};

  const name = String(j.client_name_normalized || j.client_name || j.parsed_name || '').trim();
  const phoneRaw = String(j.phone_normalized || j.parsed_phone || j.phone || '').trim();
  const emailRaw = String(j.email_normalized || j.parsed_email || j.email || '').trim();
  const messengerRaw = String(j.telegram_contact_normalized || j.parsed_messenger || j.messenger || '').trim();
  const website_state = String(j.website_state || '').trim() || (j.parsed_site ? 'provided' : 'missing');
  const website_normalized = String(j.website_normalized || j.parsed_site || j.site || '').trim();
  const comment_normalized = String(j.comment_normalized || '').trim();
  const resolved_service = String(j.resolved_service || j.service_machine || '').trim();
  const is_probable_test = j.is_probable_test === true || j.is_probable_test === 'true';

  const phone = validPhone(phoneRaw) ? phoneRaw : '';
  const email = validEmail(emailRaw) ? emailRaw : '';
  const messenger = validMessenger(messengerRaw) ? messengerRaw : '';
  const altValue = String(j.alternative_contact_value || '').trim();
  const contact_missing = !(phone || email || messenger || validMessenger(altValue));
  const hasContact = !contact_missing;
  const contact_method = String(j.contact_method_normalized || j.contact_method || '').trim() || 'unknown';

  const contacts = [phone, email, messenger].filter(Boolean);
  const primary_contact = phone || email || messenger || altValue || '';
  let contact_type = 'unknown';
  if (contacts.length > 1) contact_type = 'mixed';
  else if (phone) contact_type = 'phone';
  else if (email) contact_type = 'email';
  else if (messenger || altValue) contact_type = 'messenger';

  let service_machine = resolved_service || 'NeedsClarification';
  let service_label = String(j.resolved_service_label || j.service_label || '').trim();
  let service = String(j.service || SERVICE_COMPAT[service_machine] || 'Other');

  let quality_status = String(j.quality_status || '').trim();
  let lead_quality = String(j.lead_quality || '').trim();
  let lead_quality_label = String(j.lead_quality_label || '').trim();
  let missing_fields = String(j.missing_information || j.missing_fields || '').trim();
  let summary = String(j.request_summary || j.summary || '').trim();
  let first_reply_text = String(j.first_reply_text || '');
  let first_reply_source = String(j.first_reply_source || '');
  let first_reply_version = String(j.first_reply_version || '').trim();
  let first_reply_mode = String(j.first_reply_mode || '').trim();
  let first_reply_subject = String(j.first_reply_subject || '').trim();
  let first_reply_questions = j.first_reply_questions || '';
  let first_reply_reason_codes = String(j.first_reply_reason_codes || '').trim();
  let first_reply_omitted_reason = String(j.first_reply_omitted_reason || '').trim();
  let first_reply_ready = j.first_reply_ready === true;
  let first_reply_warnings = String(j.first_reply_warnings || '').trim();

  if (!lead_quality) {
    const q = assessLeadQuality({
      hasContact,
      website_state,
      resolved_service: service_machine,
      comment_normalized,
      is_probable_test,
      parse_status: j.parse_status,
      name,
    });
    lead_quality = q.lead_quality;
    lead_quality_label = q.lead_quality_label;
    quality_status = q.quality_status;
  }

  if (!missing_fields) {
    missing_fields = computeMissingInformation({
      resolved_service: service_machine,
      website_state,
      hasContact,
      name,
      comment_normalized,
    }).join(', ');
  }

  const existingVersion = String(j.first_reply_version || '').trim();
  const legacyReply = !existingVersion || /^sm-reply-v1/i.test(existingVersion);
  const shouldBuild = legacyReply
    || (!first_reply_text && first_reply_source !== 'none' && first_reply_source !== 'test_omitted');

  if (shouldBuild) {
    const reply = buildFirstReplyDraft({
      client_name: name,
      client_name_normalized: name,
      website_state,
      website_normalized,
      resolved_service: service_machine,
      secondary_service: j.secondary_service || '',
      comment_normalized,
      missing_information: missing_fields,
      hasContact,
      is_probable_test,
      alternative_contact_type: j.alternative_contact_type || '',
      alternative_contact_value: altValue,
      communication_preference: j.communication_preference || '',
      phone,
      email,
      messenger: messenger || altValue,
      explicit_client_intent: j.explicit_client_intent || '',
      source_topic: j.source_topic || '',
    });
    first_reply_text = reply.first_reply_text;
    first_reply_source = reply.first_reply_source;
    first_reply_version = reply.first_reply_version || FIRST_REPLY_VERSION;
    first_reply_mode = reply.first_reply_mode || '';
    first_reply_subject = reply.first_reply_subject || '';
    first_reply_questions = Array.isArray(reply.first_reply_questions)
      ? reply.first_reply_questions.join(' | ')
      : (reply.first_reply_questions || '');
    first_reply_reason_codes = Array.isArray(reply.first_reply_reason_codes)
      ? reply.first_reply_reason_codes.join(',')
      : (reply.first_reply_reason_codes || '');
    first_reply_omitted_reason = reply.first_reply_omitted_reason || reply.reply_omitted_reason || '';
    first_reply_ready = reply.first_reply_ready === true;
    first_reply_warnings = Array.isArray(reply.first_reply_warnings)
      ? reply.first_reply_warnings.join(',')
      : (reply.first_reply_warnings || '');
  } else {
    first_reply_version = existingVersion || FIRST_REPLY_VERSION;
    first_reply_ready = j.first_reply_ready === true || Boolean(first_reply_text);
  }

  if (contact_missing) {
    quality_status = 'bad';
    lead_quality = 'insufficient';
    lead_quality_label = 'Недостаточно данных';
    first_reply_text = '';
    first_reply_source = 'none';
    first_reply_mode = 'contact_suppressed';
    first_reply_ready = false;
    first_reply_omitted_reason = 'missing_contact';
    first_reply_version = first_reply_version || FIRST_REPLY_VERSION;
  }

  if (is_probable_test) {
    first_reply_text = '';
    first_reply_source = 'test_omitted';
    first_reply_mode = 'test_suppressed';
    first_reply_ready = false;
    first_reply_omitted_reason = 'probable_test';
    first_reply_version = first_reply_version || FIRST_REPLY_VERSION;
  }

  let priority = 'normal';
  const text = comment_normalized || String(j.request_text || '');
  if (/срочно|urgent|asap|критич/i.test(text) || (service_machine === 'Audit' && website_state === 'provided')) priority = 'high';
  if (quality_status === 'bad' || is_probable_test) priority = 'low';

  let manager_recommendation;
  if (contact_missing) {
    manager_recommendation = 'Контактные данные требуют проверки.';
  } else if (is_probable_test) {
    manager_recommendation = 'Тестовая заявка — не учитывать в боевой статистике.';
  } else if (service_machine === 'WebsiteDevelopment' || service_machine === 'WebsiteDevelopmentSEO') {
    manager_recommendation = 'Уточнить требования к сайту и связаться с клиентом.';
  } else if (missing_fields) {
    manager_recommendation = 'Уточнить: ' + missing_fields + '.';
  } else if (service_machine === 'Audit') {
    manager_recommendation = 'Связаться с клиентом и уточнить детали аудита.';
  } else if (service_machine === 'SEO') {
    manager_recommendation = 'Связаться с клиентом и уточнить задачи по продвижению.';
  } else {
    manager_recommendation = 'Связаться с клиентом и уточнить задачу.';
  }

  const clarification_questions = missing_fields
    ? String(missing_fields).split(',').map((s) => s.trim()).filter(Boolean)
      .map((m, i) => ((i + 1) + ') Уточнить: ' + m)).join('\n')
    : '';

  const site = website_state === 'provided' ? website_normalized : '';

  return {
    ...j,
    client_name: name,
    primary_contact,
    contact_type,
    contact_missing,
    phone,
    email,
    messenger,
    site,
    website_state,
    website_normalized,
    website_raw: j.website_raw || '',
    alternative_contact_type: j.alternative_contact_type || '',
    alternative_contact_value: altValue,
    comment_raw: j.comment_raw || '',
    comment_normalized,
    form_offer: j.form_offer || j.form_name || '',
    source_page_title: j.source_page_title || j.request_page || '',
    source_topic: j.source_topic || '',
    resolved_service: service_machine,
    resolved_service_label: service_label,
    secondary_service: j.secondary_service || '',
    service,
    service_machine,
    service_label,
    summary,
    request_summary: summary,
    priority,
    quality_status,
    lead_quality,
    lead_quality_label,
    quality_comment: [
      website_state ? ('website_state=' + website_state) : '',
      service_machine ? ('resolved_service=' + service_machine) : '',
      lead_quality ? ('lead_quality=' + lead_quality) : '',
      first_reply_version ? ('first_reply_version=' + first_reply_version) : '',
      j.form_offer ? ('form_offer=' + String(j.form_offer).slice(0, 80)) : '',
      is_probable_test ? 'is_probable_test=true' : '',
    ].filter(Boolean).join('; '),
    missing_fields,
    missing_information: missing_fields,
    clarification_questions,
    manager_recommendation,
    first_reply_text,
    first_reply_source,
    first_reply_version: first_reply_version || FIRST_REPLY_VERSION,
    first_reply_mode,
    first_reply_subject,
    first_reply_questions,
    first_reply_reason_codes,
    first_reply_omitted_reason,
    first_reply_ready,
    first_reply_warnings,
    is_probable_test,
    exclude_from_prod_stats: j.exclude_from_prod_stats === true || is_probable_test || Boolean(j.__synthetic),
    processing_mode: 'ai_off',
    ai_status: 'skipped',
    fallback_used: false,
    ai_enabled: Boolean(cfg.ai_enabled),
    message_format_version: cfg.message_format_version || j.message_format_version || 'sm-msg-v2.4',
    manager_status: j.manager_status || 'pending',
    reply_template_version: cfg.reply_template_version || first_reply_version || FIRST_REPLY_VERSION,
    parser_version: cfg.parser_version || j.parser_version || 'sm-parser-v3.3',
    semantic_model_version: j.semantic_model_version || 'lead-semantic-v1',
  };
}
