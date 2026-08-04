/**
 * Phase 3E.1 — sm-msg-v2.3 Telegram lead card formatter.
 * Base: Phase 3D.4 formatter-lib (v2.1) + Phase 3D.8 button payload bridge
 * + Phase 3D.8.3 short button labels.
 * Pure ESM module for harness / OPS sync.
 */
import { createRequire } from 'node:module';

const nodeRequire = createRequire(import.meta.url);

export const MESSAGE_FORMAT_VERSION = 'sm-msg-v2.3';

export const LEAD_TYPE_MAP = {
  new: { emoji: '🟢', title: 'Новый лид' },
  repeat: { emoji: '🟡', title: 'Повторный лид' },
  possible: { emoji: '🟠', title: 'Возможный повтор' },
  reprocessed: { emoji: '🔵', title: 'Повторная обработка' },
};

export const LIFECYCLE_MAP = {
  pending: '🕓 Ожидает обработки',
  processed: '✅ Обработан',
  spam: '🚫 Спам',
};

export const QUALITY_MAP = {
  sufficient: 'Данных достаточно',
  ok: 'Данных достаточно',
  needs_clarification: 'Нужны уточнения',
  needs_data: 'Нужны уточнения',
  insufficient: 'Недостаточно данных',
  bad: 'Недостаточно данных',
  unusable: 'Недостаточно данных',
  poor: 'Недостаточно данных',
  test: 'Тестовая заявка',
};

export const SERVICE_MAP = {
  Audit: 'Аудит',
  SEO: 'SEO',
  Direct: 'Директ',
  Site: 'Сайт',
  Other: 'Другое',
  WebsiteDevelopment: 'Разработка сайта',
  WebsiteDevelopmentSEO: 'Разработка сайта + SEO',
  AISearch: 'AI Search / GEO',
  NeedsClarification: 'Требует уточнения',
};

export const MODE_MAP = {
  ai_off: 'Без ИИ',
  template: 'Без ИИ',
  ai_on: 'С ИИ',
  ai: 'С ИИ',
  ai_fallback: 'ИИ не сработал, использован шаблон',
  fallback: 'ИИ не сработал, использован шаблон',
};

export const HISTORY_MAP = {
  same_message: 'Это повторная обработка того же сообщения.',
  phone: 'Ранее уже была заявка с этого телефона.',
  email: 'Ранее уже была заявка с этого email.',
  messenger: 'Ранее уже была заявка из этого мессенджера.',
  site_only: 'Ранее была другая заявка с этого сайта.',
  multi_evidence: 'Найдена предыдущая заявка с совпадающими контактами.',
};

export function escapeHtml(s) {
  return String(s ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

export function dashHtml(s) {
  const v = String(s ?? '').trim();
  return v ? escapeHtml(v) : '—';
}

export function fmtRuDate(v) {
  if (!v) return '';
  const d = new Date(v);
  if (Number.isNaN(d.getTime())) {
    const s = String(v).trim();
    if (/^\d{2}\.\d{2}\.\d{4}/.test(s)) return s;
    return '';
  }
  const pad = (n) => String(n).padStart(2, '0');
  return pad(d.getDate()) + '.' + pad(d.getMonth() + 1) + '.' + d.getFullYear() + ' ' + pad(d.getHours()) + ':' + pad(d.getMinutes());
}

export function computeActionToken(leadId) {
  const s = String(leadId || '');
  try {
    const crypto = nodeRequire('crypto');
    return crypto.createHash('sha256').update(s).digest('hex').slice(0, 12);
  } catch (e) {
    return fnvToken(s);
  }
}

function fnvToken(s) {
  let h1 = 0x811c9dc5 >>> 0;
  for (let i = 0; i < s.length; i++) {
    h1 ^= s.charCodeAt(i);
    h1 = Math.imul(h1, 0x01000193);
  }
  let h2 = 0x9e3779b9 >>> 0;
  for (let i = 0; i < s.length; i++) {
    h2 ^= s.charCodeAt(i);
    h2 = Math.imul(h2, 0x85ebca6b);
    h2 = (h2 << 13) | (h2 >>> 19);
  }
  const hex1 = (h1 >>> 0).toString(16).padStart(8, '0');
  const hex2 = (h2 >>> 0).toString(16).padStart(8, '0');
  return (hex1 + hex2).slice(0, 12);
}

/** Phase 3D.8.3 — short pending button labels. */
export function buildReplyMarkup(token) {
  return {
    inline_keyboard: [[
      { text: '✅ Обработано', callback_data: 'sm:p:' + token },
      { text: '🚫 Спам', callback_data: 'sm:s:' + token },
    ]],
  };
}

export function isMalformedLead(j) {
  if (!j || typeof j !== 'object') return true;
  if (!String(j.lead_id || '').trim()) return true;
  if (String(j.parse_status || '') === 'failed') return true;
  return false;
}

function normalizeManagerStatus(j) {
  const raw = String(j.manager_status || '').trim().toLowerCase();
  return (raw === 'processed' || raw === 'spam') ? raw : 'pending';
}

export function isValidContactValue(value) {
  const v = String(value ?? '').trim();
  if (!v) return false;
  const lower = v.toLowerCase();
  if (['unknown', '44', '#error!', '#value!', '#ref!', '#n/a', 'n/a', 'na', '-', '—', 'null', 'undefined'].includes(lower)) {
    return false;
  }
  if (/#error!|#value!|#ref!|#n\/a/i.test(v)) return false;
  if (/formula\s*parse\s*error/i.test(v)) return false;
  if (/^#\w+!/i.test(v)) return false;
  return true;
}

function contactBlockLines(label, value) {
  const v = String(value ?? '').trim();
  if (!isValidContactValue(v)) return [];
  return [label, '<code>' + escapeHtml(v) + '</code>', ''];
}

function messengerLabel(value) {
  const v = String(value ?? '');
  return (/^@/.test(v) || /t\.me/i.test(v) || /telegram\.me/i.test(v)) ? 'Telegram' : 'Мессенджер';
}

function isProbableOrSyntheticTest(j) {
  return Boolean(
    j.is_probable_test === true
    || j.is_probable_test === 'true'
    || j.__synthetic
    || j.synthetic_fixture
    || j.fixture_id
    || j.marker === 'SYNTHETIC_TEST'
    || String(j.phase_marker || '').includes('PHASE_3'),
  );
}

function looksLikeMessengerAsSite(value) {
  const v = String(value ?? '').trim();
  if (!v) return false;
  if (/t\.me|telegram\.me/i.test(v)) return true;
  if (/^нет\s*сайт/i.test(v)) return true;
  if (/^n\/?a$/i.test(v)) return true;
  return false;
}

/**
 * Site line for v2.3:
 * - provided → website_normalized (never t.me / "нет сайта")
 * - explicitly_absent → "Сайт: отсутствует" when useful
 * - otherwise omit
 */
function siteBlockLines(j) {
  const state = String(j.website_state || '').trim();
  if (state === 'provided') {
    const site = String(j.website_normalized || j.site || '').trim();
    if (!site || looksLikeMessengerAsSite(site) || !isValidContactValue(site)) return [];
    return contactBlockLines('Сайт', site);
  }
  if (state === 'explicitly_absent') {
    const svc = String(j.resolved_service || j.service_machine || j.service || '').trim();
    // Useful when site absence affects triage (audit/SEO/clarify) or client needs a site built.
    const useful = !svc
      || ['Audit', 'SEO', 'NeedsClarification', 'WebsiteDevelopment', 'WebsiteDevelopmentSEO', 'Site', 'Other'].includes(svc);
    if (!useful) return [];
    return ['Сайт: отсутствует', ''];
  }
  return [];
}

function alternativeContactAlreadyShown(alt, phone, email, messenger) {
  const a = String(alt || '').trim().toLowerCase();
  if (!a) return true;
  const pool = [phone, email, messenger].map((x) => String(x || '').trim().toLowerCase()).filter(Boolean);
  return pool.includes(a);
}

function resolveInterestLabel(j) {
  const labeled = String(j.resolved_service_label || j.service_label || '').trim();
  if (labeled) return labeled;
  const key = String(j.resolved_service || j.service_machine || j.service || '').trim();
  if (key && SERVICE_MAP[key]) return SERVICE_MAP[key];
  return '';
}

function resolveQualityLabel(j) {
  const labeled = String(j.lead_quality_label || '').trim();
  if (labeled) return labeled;
  const qk = String(j.lead_quality || j.quality_status || '').trim();
  if (qk && QUALITY_MAP[qk]) return QUALITY_MAP[qk];
  return '';
}

function pushLabeledBlock(lines, title, body) {
  const t = String(title || '').trim();
  const b = String(body || '').trim();
  if (!t || !b) return;
  lines.push(t);
  lines.push(escapeHtml(b));
  lines.push('');
}

function pushInlineField(lines, label, valueHtmlOrText, alreadyEscaped = false) {
  const v = String(valueHtmlOrText ?? '').trim();
  if (!v) return;
  lines.push(label + ': ' + (alreadyEscaped ? v : escapeHtml(v)));
}

/** sm-msg-v2.3 — semantic card; omit empty sections; no IP. */
export function buildCardText(j) {
  const leadType = LEAD_TYPE_MAP[j.duplicate_status] || LEAD_TYPE_MAP.new;
  const managerStatus = normalizeManagerStatus(j);
  const isTest = isProbableOrSyntheticTest(j);

  const clientName = j.client_name || j.client_name_normalized || '';
  const phone = j.phone || j.phone_normalized || '';
  const email = j.email || j.email_normalized || '';
  const messenger = j.messenger || j.telegram_contact_normalized || '';
  const comment = String(j.comment_normalized || '').trim();
  const formOffer = String(j.form_offer || '').trim();
  const pageTitle = String(j.source_page_title || '').trim();
  const missingHuman = String(j.missing_fields || j.missing_information || '')
    .split(/[;,]/)
    .map((s) => s.trim())
    .filter(Boolean)
    .join(', ');
  const nextStep = String(j.manager_recommendation || '').trim();
  const interest = resolveInterestLabel(j);
  const qualityLabel = resolveQualityLabel(j);
  const altValue = String(j.alternative_contact_value || '').trim();
  const altType = String(j.alternative_contact_type || '').trim();

  const lines = [];
  lines.push(leadType.emoji + ' ' + leadType.title);
  lines.push(LIFECYCLE_MAP[managerStatus]);
  if (isTest) {
    lines.push('🧪 Тестовая заявка');
  }
  lines.push('');

  lines.push(...contactBlockLines('Клиент', clientName));
  lines.push(...contactBlockLines('Телефон', phone));
  lines.push(...contactBlockLines('Email', email));
  if (String(messenger).trim()) {
    lines.push(...contactBlockLines(messengerLabel(messenger), messenger));
  }

  lines.push(...siteBlockLines(j));

  if (isValidContactValue(altValue) && !alternativeContactAlreadyShown(altValue, phone, email, messenger)) {
    const altLabel = altType === 'telegram' || altType === 'Telegram'
      ? 'Telegram'
      : (altType ? ('Контакт (' + altType + ')') : 'Доп. контакт');
    lines.push(...contactBlockLines(altLabel, altValue));
  }

  if (interest) {
    pushInlineField(lines, 'Интерес', interest);
  }

  if (comment) {
    pushLabeledBlock(lines, 'Комментарий клиента', comment);
  }

  if (formOffer || pageTitle) {
    lines.push('Контекст формы');
    if (formOffer) lines.push(escapeHtml(formOffer));
    if (pageTitle) lines.push(escapeHtml(pageTitle));
    lines.push('');
  }

  if (qualityLabel) {
    pushInlineField(lines, 'Качество', qualityLabel);
  }

  if (missingHuman) {
    lines.push('');
    lines.push('Не хватает');
    lines.push(escapeHtml(missingHuman));
  }

  if (nextStep) {
    lines.push('');
    lines.push('Следующий шаг');
    lines.push(escapeHtml(nextStep));
    lines.push('');
  } else if (lines.length && lines[lines.length - 1] !== '') {
    lines.push('');
  }

  if (['repeat', 'possible', 'reprocessed'].includes(j.duplicate_status)) {
    const matchType = String(j.duplicate_match_type || '').trim();
    let hist = HISTORY_MAP[matchType] || 'Найдена предыдущая заявка с совпадающими контактами.';
    const prevTs = fmtRuDate(j.previous_contact_at);
    if (prevTs) hist += ' Предыдущее обращение: ' + prevTs + '.';
    lines.push('⚠️ История: ' + hist);
    lines.push('');
  }

  const replyText = String(j.first_reply_text || '').trim();
  const replySource = String(j.first_reply_source || '').trim();
  const replyOmittedForTest = replySource === 'test_omitted'
    || (isTest && !replyText);
  const noContact = j.contact_missing === true
    || j.quality_status === 'bad'
    || j.lead_quality === 'insufficient'
    || replySource === 'none'
    || !replyText;

  if (replyOmittedForTest) {
    // Test-only: skip reply copy block; keep auto-send disclaimer.
    lines.push('Ответ клиенту автоматически не отправляется.');
  } else if (noContact) {
    lines.push('⚠️ Готовый ответ не сформирован: нет контактных данных для связи.');
    lines.push('Ответ клиенту автоматически не отправляется.');
  } else {
    lines.push('✉️ Ответ клиенту — нажмите, чтобы скопировать');
    lines.push('<pre>' + escapeHtml(replyText) + '</pre>');
    lines.push('Ответ клиенту автоматически не отправляется.');
  }

  // Collapse accidental double blank lines; never emit IP / raw address fields.
  return lines.join('\n').replace(/\n{3,}/g, '\n\n').trimEnd();
}

export function formatLeadCard(j) {
  const text = buildCardText(j);
  const leadId = String(j.lead_id || '').trim();
  const managerStatus = normalizeManagerStatus(j);
  const malformed = isMalformedLead(j);
  const token = computeActionToken(leadId);

  const gid = String(j.gmail_message_id || '').trim();
  const attempts = Number(j.delivery_attempt_count || 0);
  const maxAttempts = 5;
  const already = j.telegram_already_delivered === true || String(j.delivery_status || '') === 'delivered';

  const baseFields = {
    message_format_version: MESSAGE_FORMAT_VERSION,
    manager_status: managerStatus,
    telegram_action_token: token,
  };

  function attachMarkupIfActionable(result, skipTelegram) {
    const isDone = managerStatus === 'processed' || managerStatus === 'spam';
    const actionable = Boolean(leadId) && !skipTelegram && !malformed && !isDone;
    if (actionable) {
      result.telegram_reply_markup = buildReplyMarkup(token);
      result.telegram_has_buttons = true;
      result.telegram_callback_processed = 'sm:p:' + token;
      result.telegram_callback_spam = 'sm:s:' + token;
    } else {
      result.telegram_has_buttons = false;
    }
    return result;
  }

  if (already) {
    return attachMarkupIfActionable({
      ...j,
      ...baseFields,
      telegram_text: text,
      telegram_ok: true,
      skip_telegram: true,
      __expect_telegram_send: false,
      disabled_pass_through: true,
      delivery_status: 'delivered',
      telegram_delivered_at: j.telegram_delivered_at || '',
      delivery_attempt_count: attempts,
    }, true);
  }

  if (gid && attempts >= maxAttempts) {
    return attachMarkupIfActionable({
      ...j,
      ...baseFields,
      telegram_text: text,
      telegram_ok: false,
      skip_telegram: true,
      force_telegram_fail: true,
      __expect_telegram_send: false,
      disabled_pass_through: true,
      error_code: 'telegram_retry_exhausted',
      error_stage: 'telegram_send',
      delivery_status: 'exhausted',
      delivery_attempt_count: attempts,
    }, true);
  }

  return attachMarkupIfActionable({
    ...j,
    ...baseFields,
    telegram_text: text,
    telegram_ok: true,
    skip_telegram: false,
    __expect_telegram_send: true,
    disabled_pass_through: false,
    delivery_status: attempts > 0 ? 'retrying' : 'pending',
    delivery_attempt_count: attempts + 1,
  }, false);
}
