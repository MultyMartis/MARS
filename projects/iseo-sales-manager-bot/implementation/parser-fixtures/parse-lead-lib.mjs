/**
 * Phase 3E.1/3E.2 — sm-parser-v3.3 + Lead Semantic Model v1 (pure module).
 * First Reply Engine v2 (sm-reply-v2.0) for manager drafts.
 * Local harness + n8n SYNC target. No $input — import-only.
 * AI OFF. Deterministic extraction / intent / reply facts only.
 */

import {
  buildFirstReplyDraftV2,
  FIRST_REPLY_VERSION,
} from '../runtime-libs/first-reply-engine-v2.mjs';

export const PARSER_VERSION = 'sm-parser-v3.3';
export const SEMANTIC_MODEL_VERSION = 'lead-semantic-v1';
export const MESSAGE_FORMAT_VERSION_DEFAULT = 'sm-msg-v2.4';
export { FIRST_REPLY_VERSION };

const INVALID = new Set([
  '44', '#error!', 'unknown', 'telegram', 'whatsapp', 'viber',
  'телефон', 'email', 'e-mail', 'почта', 'сайт', 'n/a', 'na', '-', '—', '–',
  'null', 'undefined', 'phone', 'messenger', 'contact', 'контакт', 'нет', 'no',
  'имя', 'name',
]);

const NAME_PLACEHOLDERS = new Set(['имя', 'name', 'n/a', 'na', '-', '—', '–', 'null', 'undefined']);

const SITE_PLACEHOLDERS = new Set([
  'нет', 'отсутствует', '—', '–', '-', 'не указан', 'потом', 'не знаю', 'unknown',
  '123', 'n/a', 'na', 'null', 'undefined', '#error!',
]);

/** Explicit no-site / need-a-site phrases (website_state=explicitly_absent). */
const EXPLICIT_ABSENT_RE = [
  /нет\s+сайта/i,
  /сайта\s+нет/i,
  /нету\s+сайта/i,
  /нет\s+адреса/i,
  /нету\s+адреса/i,
  /пока\s+нет\s+сайта/i,
  /сайта\s+пока\s+нет/i,
  /сайт\s+ещ[её]\s+не\s+сделали/i,
  /сайт\s+ещ[её]\s+не\s+готов/i,
  /сайта\s+ещ[её]\s+нет/i,
  /нужен\s+сайт/i,
  /хочу\s+сайт/i,
  /нет\s+своего\s+сайта/i,
  /своего\s+сайта\s+нет/i,
];

export const LABEL_DEFS = [
  { key: 'name', re: /(?:От\s*кого|Имя)\s*[:：]/gi },
  { key: 'contact_method', re: /Способ\s*связи\s*[:：]/gi },
  { key: 'contact', re: /Контакт\s*[:：]/gi },
  { key: 'phone_direct', re: /Телефон\s*[:：]/gi },
  { key: 'email_direct', re: /(?:E[\u2011\u2010\-]?mail|Email|Почта)\s*[:：]/gi },
  { key: 'site', re: /(?:Адрес\s*сайта|Сайт)\s*[:：]/gi },
  { key: 'comment', re: /(?:Комментарий|Сообщение)\s*[:：]/gi },
  { key: 'page', re: /Отправлено\s+со\s+страницы\s*[:：]?/gi },
  { key: 'ip', re: /\bIP\s*[:：]/gi },
];

const BOUNDARY_DEFS = [
  { key: '__audit_title', re: /Заявка\s+на\s+бесплатный\s+аудит/gi },
  { key: '__forward', re: /^-{2,}\s*Forwarded\s*-{2,}/gim },
  { key: '__footer', re: /^-{2,}\s*Original\s+Message\s*-{2,}/gim },
];

const COMM_PREF_ONLY = [
  /^в\s*тг\.?$/i,
  /^пишите\s+в\s*тг\.?$/i,
  /^связь\s+в\s*телеграм\.?$/i,
  /^пишите\s+в\s*telegram\.?$/i,
  /^звонить\.?$/i,
  /^лучше\s+whatsapp\.?$/i,
  /^лучше\s+ватсап\.?$/i,
  /^по\s*телефону\.?$/i,
  /^whatsapp\.?$/i,
  /^telegram\.?$/i,
  /^телеграм\.?$/i,
];

const SERVICE_TAXONOMY = {
  Audit: { machine: 'Audit', label: 'Аудит' },
  SEO: { machine: 'SEO', label: 'SEO' },
  WebsiteDevelopment: { machine: 'WebsiteDevelopment', label: 'Разработка сайта' },
  WebsiteDevelopmentSEO: { machine: 'WebsiteDevelopmentSEO', label: 'Разработка сайта + SEO' },
  AISearch: { machine: 'AISearch', label: 'AI Search / GEO' },
  Direct: { machine: 'Direct', label: 'Яндекс Директ / PPC' },
  Other: { machine: 'Other', label: 'Другое' },
  NeedsClarification: { machine: 'NeedsClarification', label: 'Требует уточнения' },
};

/** Compat map for older processor/service fields. */
export const SERVICE_COMPAT = {
  Audit: 'Audit',
  SEO: 'SEO',
  WebsiteDevelopment: 'Site',
  WebsiteDevelopmentSEO: 'Site',
  AISearch: 'Other',
  Direct: 'Direct',
  Other: 'Other',
  NeedsClarification: 'Other',
};

export function normalizeSpaces(raw) {
  return String(raw ?? '')
    .replace(/\u00a0/g, ' ')
    .replace(/[\u2007\u202F\u2009\u200A]/g, ' ')
    .replace(/\r\n/g, '\n')
    .replace(/\r/g, '\n');
}

function isInvalidToken(v) {
  const s = String(v || '').trim().toLowerCase();
  return !s || INVALID.has(s);
}

function isNamePlaceholder(v) {
  const s = String(v || '').trim().toLowerCase();
  return !s || NAME_PLACEHOLDERS.has(s);
}

function isSitePlaceholder(raw) {
  const s = String(raw || '').trim().toLowerCase();
  return !s || SITE_PLACEHOLDERS.has(s);
}

export function htmlToPlainText(html) {
  let s = String(html ?? '');
  if (!/<[a-z][\s\S]*>/i.test(s)) return normalizeSpaces(s);
  s = s.replace(/<\s*br\s*\/?\s*>/gi, '\n');
  s = s.replace(/<\/\s*(p|div|tr|li|h[1-6])\s*>/gi, '\n');
  s = s.replace(/<\s*(p|div|tr|li|h[1-6])[^>]*>/gi, '\n');
  s = s.replace(/<\/\s*td\s*>/gi, '\t');
  s = s.replace(/<\s*td[^>]*>/gi, ' ');
  // Prefer href for links that wrap empty/short anchors
  s = s.replace(/<a[^>]+href=["']([^"']+)["'][^>]*>([\s\S]*?)<\/a>/gi, (_, href, text) => {
    const t = String(text).replace(/<[^>]+>/g, '').trim();
    if (t && t.length >= 3) return t;
    return href;
  });
  s = s.replace(/<[^>]+>/g, ' ');
  s = s.replace(/&nbsp;/gi, ' ').replace(/&amp;/gi, '&').replace(/&lt;/gi, '<').replace(/&gt;/gi, '>')
    .replace(/&quot;/gi, '"').replace(/&#39;/gi, "'");
  return normalizeSpaces(s);
}

export function extractLabeledFields(raw) {
  const text = normalizeSpaces(raw);
  const hits = [];
  for (const def of LABEL_DEFS) {
    const re = new RegExp(def.re.source, def.re.flags);
    let m;
    while ((m = re.exec(text)) !== null) {
      hits.push({ key: def.key, start: m.index, end: m.index + m[0].length, boundary: false });
      if (!re.global) break;
    }
  }
  for (const def of BOUNDARY_DEFS) {
    const re = new RegExp(def.re.source, def.re.flags);
    let m;
    while ((m = re.exec(text)) !== null) {
      hits.push({ key: def.key, start: m.index, end: m.index + m[0].length, boundary: true });
    }
  }
  hits.sort((a, b) => a.start - b.start || a.end - b.end);

  const fields = {};
  for (let i = 0; i < hits.length; i++) {
    const h = hits[i];
    if (h.boundary) continue;
    if (fields[h.key] != null) continue;
    const valueEnd = i + 1 < hits.length ? hits[i + 1].start : text.length;
    let val = text.slice(h.end, valueEnd).trim();
    val = val.replace(/^[\s:：\-–—|]+/, '').replace(/\s+/g, ' ').trim();
    for (const def of LABEL_DEFS) {
      const probe = new RegExp(def.re.source, 'i');
      if (probe.test(val)) {
        const cut = val.search(probe);
        if (cut > 0) val = val.slice(0, cut).trim();
      }
    }
    // Strip form-title bleed but keep as separate form_offer elsewhere
    val = val.replace(/\s*Заявка\s+на\s+бесплатный\s+аудит\s*/gi, ' ').replace(/\s+/g, ' ').trim();
    // Prevent partial "Отправлено со" leakage into comment
    if (h.key === 'comment') {
      val = val.replace(/\s*Отправлено\s+со\s*(страницы)?\s*$/i, '').trim();
    }
    fields[h.key] = val;
  }
  return { fields, text, hits };
}

export function digits(p) {
  return String(p || '').replace(/\D/g, '');
}

export function looksLikePhone(p) {
  if (isInvalidToken(p)) return false;
  const d = digits(p);
  if (!d || d.length < 10 || d.length > 15) return false;
  if (INVALID.has(d)) return false;
  return true;
}

export function looksLikeEmail(e) {
  const v = String(e || '').trim().toLowerCase();
  if (!v || isInvalidToken(v) || v.length > 254) return false;
  return /^[^\s@]+@[^\s@]+\.[^\s@]{2,24}$/.test(v);
}

function normalizeMessengerDisplay(raw) {
  let v = String(raw || '').trim();
  if (!v) return '';
  if (/^@[a-zA-Z0-9_]{4,32}$/.test(v)) return v;
  if (/^t\.me\//i.test(v)) return v.replace(/\s+/g, '');
  if (/^telegram\.me\//i.test(v)) return v.replace(/\s+/g, '');
  if (/^https?:\/\/(t\.me|telegram\.me)\//i.test(v)) return v.replace(/\s+/g, '');
  if (/^https?:\/\/(wa\.me|api\.whatsapp\.com)\//i.test(v)) return v.replace(/\s+/g, '');
  if (/^(wa\.me|api\.whatsapp\.com)\//i.test(v)) return v.replace(/\s+/g, '');
  return v.replace(/\s+/g, ' ').trim();
}

export function classifyMessengerUrl(raw) {
  const v = String(raw || '').trim();
  if (!v || isInvalidToken(v)) return null;
  const lower = v.toLowerCase();
  if (/^@[a-zA-Z0-9_]{4,32}$/.test(v)
    || /^(https?:\/\/)?(t\.me|telegram\.me)\//i.test(v)
    || /^t\.me\//i.test(v)
    || /^telegram\.me\//i.test(v)) {
    return { channel: 'telegram', value: normalizeMessengerDisplay(v) };
  }
  if (/^(https?:\/\/)?(wa\.me|api\.whatsapp\.com)\//i.test(v)
    || /^wa\.me\//i.test(v)
    || /^api\.whatsapp\.com\//i.test(v)) {
    return { channel: 'whatsapp', value: normalizeMessengerDisplay(v) };
  }
  if (lower === 'telegram' || lower === 'телеграм') {
    return { channel: 'telegram', value: '' };
  }
  if (lower === 'whatsapp' || lower === 'ватсап' || lower === 'вацап') {
    return { channel: 'whatsapp', value: '' };
  }
  return null;
}

export function looksLikeMessenger(m) {
  return classifyMessengerUrl(m) != null;
}

export function normalizePhoneDisplay(raw) {
  const src = String(raw || '').trim();
  if (!looksLikePhone(src)) return '';
  return src.replace(/\s+/g, ' ').trim();
}

export function looksLikePlausibleSite(raw) {
  let s = String(raw || '').trim();
  if (!s || isSitePlaceholder(s) || isInvalidToken(s)) return false;
  if (classifyMessengerUrl(s)) return false;
  s = s.replace(/^[\s"'«»(<[{]+/, '').replace(/[\s"'«».,;:!?)\]}>]+$/g, '').trim();
  if (!s || isSitePlaceholder(s)) return false;
  // Reject obvious system/service hosts
  if (/(^|\.)(googleapis|googleusercontent|gstatic|mail\.google|n8n\.|localhost)\b/i.test(s)) return false;
  if (/^https?:\/\//i.test(s)) return true;
  if (/^www\./i.test(s)) return true;
  if (/^[a-z0-9][\w.-]*\.[a-z0-9][\w.-]*(?:\/\S*)?$/i.test(s)) return true;
  return false;
}

export function normalizeSite(raw) {
  let s = String(raw || '').trim();
  if (!looksLikePlausibleSite(s)) return '';
  s = s.replace(/^[\s"'«»(<[{]+/, '').replace(/[\s"'«».,;:!?)\]}>]+$/g, '').trim();
  s = s.replace(/\s+/g, '');
  // Lowercase host only; keep path case
  try {
    if (/^https?:\/\//i.test(s)) {
      const u = new URL(s);
      u.hostname = u.hostname.toLowerCase();
      return u.toString().replace(/\/$/, '') === (u.origin + u.pathname.replace(/\/$/, '') + u.search + u.hash)
        ? u.toString().replace(/\/$/, '') || u.origin
        : u.toString();
    }
  } catch {
    // fall through
  }
  if (/^www\./i.test(s)) return s.toLowerCase();
  const slash = s.indexOf('/');
  if (slash === -1) return s.toLowerCase();
  return s.slice(0, slash).toLowerCase() + s.slice(slash);
}

export function isExplicitAbsentPhrase(raw) {
  const s = String(raw || '').trim();
  if (!s) return false;
  return EXPLICIT_ABSENT_RE.some((re) => re.test(s));
}

/**
 * Website state model with required precedence:
 * provided > explicitly_absent > alternative_contact > invalid_or_placeholder > missing
 */
export function classifyWebsiteField(siteRaw, commentRaw = '') {
  const raw = String(siteRaw || '').trim();
  const warnings = [];
  const comment = String(commentRaw || '').trim();

  if (raw && looksLikePlausibleSite(raw)) {
    return {
      website_raw: raw,
      website_normalized: normalizeSite(raw),
      website_state: 'provided',
      alternative_contact_type: '',
      alternative_contact_value: '',
      warnings,
    };
  }

  const absentFromSite = raw && isExplicitAbsentPhrase(raw);
  const absentFromComment = !raw && isExplicitAbsentPhrase(comment);
  // "хочу сайт" / "нужен сайт" in comment with empty site = explicitly_absent
  if (absentFromSite || absentFromComment || (raw && isExplicitAbsentPhrase(raw))) {
    return {
      website_raw: raw,
      website_normalized: '',
      website_state: 'explicitly_absent',
      alternative_contact_type: '',
      alternative_contact_value: '',
      warnings,
    };
  }
  // Also: empty site + comment expresses need-for-site
  if (!raw && /(?:хочу|нужен|нужна|сделать|создать)\s+сайт/i.test(comment)) {
    return {
      website_raw: '',
      website_normalized: '',
      website_state: 'explicitly_absent',
      alternative_contact_type: '',
      alternative_contact_value: '',
      warnings,
    };
  }

  const alt = classifyMessengerUrl(raw);
  if (raw && alt) {
    warnings.push('site_field_was_messenger');
    return {
      website_raw: raw,
      website_normalized: '',
      website_state: 'alternative_contact',
      alternative_contact_type: alt.channel,
      alternative_contact_value: alt.value || raw,
      warnings,
    };
  }

  if (raw && (isSitePlaceholder(raw) || isInvalidToken(raw) || /^(test|тест)$/i.test(raw) || !looksLikePlausibleSite(raw))) {
    if (raw) warnings.push('site_invalid_or_placeholder');
    return {
      website_raw: raw,
      website_normalized: '',
      website_state: raw ? 'invalid_or_placeholder' : 'missing',
      alternative_contact_type: '',
      alternative_contact_value: '',
      warnings,
    };
  }

  return {
    website_raw: raw,
    website_normalized: '',
    website_state: 'missing',
    alternative_contact_type: '',
    alternative_contact_value: '',
    warnings,
  };
}

/** Strict recovery of a site from comment only (not sender/source/i-SEO). */
export function recoverSiteFromComment(comment) {
  const c = String(comment || '');
  const m = c.match(/(?:https?:\/\/)?(?:www\.)?[a-z0-9][\w.-]*\.[a-z]{2,24}(?:\/[\w./?#&=%-]*)?/i);
  if (!m) return null;
  const candidate = m[0];
  if (classifyMessengerUrl(candidate)) return null;
  if (/i-?seo\.(ru|example)/i.test(candidate)) return null;
  if (!looksLikePlausibleSite(candidate)) return null;
  return {
    website_raw: candidate,
    website_normalized: normalizeSite(candidate),
    website_state: 'provided',
    recovery_source: 'comment',
  };
}

export function inferCommPreference(text) {
  const t = String(text || '').trim().toLowerCase();
  if (!t) return null;
  if (/^(в\s*тг|пишите\s+в\s*тг|связь\s+в\s*телеграм|пишите\s+в\s*telegram|telegram|телеграм)/.test(t)) {
    return 'telegram';
  }
  if (/^(звонить|по\s*телефону|лучше\s+звонить)/.test(t)) return 'phone';
  if (/^(лучше\s+whatsapp|whatsapp|ватсап|вацап)/.test(t)) return 'whatsapp';
  if (/^(по\s*email|пишите\s+на\s*почту|email|почта)/.test(t)) return 'email';
  return null;
}

export function isCommPreferenceOnly(text) {
  const t = String(text || '').trim();
  if (!t) return false;
  if (COMM_PREF_ONLY.some((re) => re.test(t))) return true;
  return inferCommPreference(t) != null && t.length <= 48;
}

export function normalizeSourcePage(page) {
  let s = String(page || '').trim();
  if (!s) return '';
  s = s.replace(/[\s|—–\-]+$/g, '').trim();
  s = s.replace(/\s*[|—–\-]\s*i[\-\.]?seo\.(ru|example)(\/.*)?$/i, '').trim();
  s = s.replace(/\s*[|—–\-]\s*https?:\/\/[^\s|—–\-]+$/i, '').trim();
  s = s.replace(/[\s|—–\-]+$/g, '').trim();
  const bareUrlOnly = /^https?:\/\/\S+$/i.test(s) && !/\s/.test(s.trim());
  if (bareUrlOnly) return s;
  if (/seo/i.test(s) && /(ai|нейросет|нейро)/i.test(s)) {
    if (/продвижен/i.test(s)) return 'SEO-продвижение в AI и нейросетях';
  }
  return s;
}

export function classifySourceTopic(page, subject = '', formOffer = '') {
  const blob = [page, subject, formOffer].join(' ').toLowerCase();
  if (/иностран|foreign|зарубеж/.test(blob)) return 'foreign_seo';
  if (/бесплатн.*аудит|free\s*audit|\/audit/.test(blob)) return 'free_audit';
  if (/москв/.test(blob) && /seo|продвиж/.test(blob)) return 'moscow_seo';
  if (/ai\s*search|гео|geo|нейросет|ai\s*visibility/.test(blob)) return 'ai_search';
  if (/нов(ый|ого)\s+сайт|new.?site/.test(blob) && /seo|продвиж/.test(blob)) return 'new_site_seo';
  if (/директ|контекст|ppc|яндекс\s*директ/.test(blob)) return 'contextual_ads';
  if (/разработк|создани[ея]\s+сайт|website\s*dev/.test(blob)) return 'website_development';
  if (/seo|продвиж/.test(blob)) return 'seo';
  if (/аудит|audit/.test(blob)) return 'audit';
  return '';
}

function inferContactMethodFromSignals({ methodRaw, contact, phone, email, messenger, commentPref }) {
  const method = String(methodRaw || '').trim().toLowerCase();
  if (/telegram|телеграм/i.test(method)) return 'telegram';
  if (/whats\s*app|ватсап|вацап/i.test(method)) return 'whatsapp';
  if (/телефон|phone|звон/i.test(method)) return 'phone';
  if (/e[\u2011\u2010\-]?mail|email|почта|mail/i.test(method)) return 'email';

  if (messenger) {
    const cls = classifyMessengerUrl(messenger);
    if (cls?.channel === 'telegram') return 'telegram';
    if (cls?.channel === 'whatsapp') return 'whatsapp';
    return 'messenger';
  }
  if (commentPref === 'telegram') return 'telegram';
  if (commentPref === 'whatsapp') return 'whatsapp';
  if (commentPref === 'phone' && phone) return 'phone';
  if (commentPref === 'email' && email) return 'email';
  if (phone && !email && !messenger) return 'phone';
  if (email && !phone && !messenger) return 'email';
  return 'unknown';
}

export function interpretContactMethod(methodRaw, contactRaw, extras = {}) {
  const method = String(methodRaw || '').trim().toLowerCase();
  const contact = String(contactRaw || '').trim();
  let phone = String(extras.phone_direct || '').trim();
  let email = String(extras.email_direct || '').trim();
  let messenger = String(extras.messenger_extra || '').trim();

  const methodPhone = /телефон|phone|звон/i.test(method);
  const methodEmail = /e[\u2011\u2010\-]?mail|email|почта|mail/i.test(method);
  const methodTg = /telegram|телеграм/i.test(method);
  const methodWa = /whats\s*app|ватсап|вацап/i.test(method);

  if (methodPhone) {
    if (looksLikePhone(contact)) phone = phone || contact;
  } else if (methodEmail) {
    if (looksLikeEmail(contact)) email = email || contact;
    else if (looksLikeEmail(contact.replace(/\s+/g, ''))) email = email || contact.replace(/\s+/g, '');
  } else if (methodTg) {
    const cls = classifyMessengerUrl(contact);
    if (cls) messenger = messenger || cls.value || contact;
    else if (/^[a-zA-Z0-9_]{5,32}$/.test(contact)) messenger = messenger || ('@' + contact.replace(/^@/, ''));
    else if (looksLikePhone(contact)) phone = phone || contact;
  } else if (methodWa) {
    const cls = classifyMessengerUrl(contact);
    if (cls) messenger = messenger || cls.value || contact;
    else if (looksLikePhone(contact)) phone = phone || contact;
    else if (contact) messenger = messenger || contact;
  } else if (contact) {
    if (looksLikePhone(contact)) phone = phone || contact;
    else if (looksLikeEmail(contact)) email = email || contact;
    else {
      const cls = classifyMessengerUrl(contact);
      if (cls) messenger = messenger || cls.value || contact;
      else if (/^@[a-zA-Z0-9_]{4,32}$/.test(contact)) messenger = messenger || contact;
    }
  }

  if (phone && !looksLikePhone(phone)) phone = '';
  if (email && !looksLikeEmail(email)) email = '';
  if (messenger && isInvalidToken(messenger) && !classifyMessengerUrl(messenger)) messenger = '';

  const contact_method = inferContactMethodFromSignals({
    methodRaw: method,
    contact,
    phone,
    email,
    messenger,
    commentPref: extras.comment_preference || null,
  });

  return {
    contact_method,
    phone: normalizePhoneDisplay(phone),
    email: email ? email.toLowerCase() : '',
    messenger: String(messenger || '').trim(),
  };
}

export function detectAuditForm(raw) {
  return /Заявка\s+на\s+бесплатный\s+аудит/i.test(String(raw || ''));
}

export function detectFormOffer(raw, subject = '') {
  if (detectAuditForm(raw) || /бесплатн.*аудит/i.test(subject)) return 'Бесплатный аудит';
  if (/яндекс\s*директ|контекстн/i.test(raw + ' ' + subject)) return 'Яндекс Директ';
  if (/создани[ея]\s+сайт|разработк/i.test(raw + ' ' + subject)) return 'Разработка сайта';
  return '';
}

export function stripLabeledPayload(raw) {
  const text = normalizeSpaces(raw);
  const { fields } = extractLabeledFields(text);
  let residual = text;
  const labelUnion = LABEL_DEFS.map((d) => d.re.source).join('|');
  residual = residual.replace(new RegExp('(?:' + labelUnion + ')\\s*[^]*?(?=(?:' + labelUnion + ')|$)', 'gi'), ' ');
  residual = residual.replace(/\s+/g, ' ').trim();
  return { fields, residual };
}

export function classifyProbableTest({ name, comment, site, phone, email, marker, phase_marker }) {
  const reasons = [];
  const n = String(name || '');
  const c = String(comment || '');
  const s = String(site || '');
  // Word-ish boundaries: avoid false positives inside «проверить», «протестировать» stems where «тест» is not a standalone token.
  const hasRuTestToken = (text) => /(^|[^\p{L}])тест(?:овая|овый|овое|овые|ов|ик|ирование|ируем|ировать)?([^\p{L}]|$)/iu.test(text);
  if (/\btest\b/i.test(n) || hasRuTestToken(n)) reasons.push('name_test');
  if (/тест\s*бота/i.test(c) || /\btest\b/i.test(c) || hasRuTestToken(c)) reasons.push('comment_test');
  if (/synthetic|parser|stabilization|phase\s*3/i.test(c)) reasons.push('comment_internal');
  if (/\.(test|example)(\b|\/|$)/i.test(s)) reasons.push('synthetic_domain');
  {
    const markerBlob = String(marker || '') + ' ' + String(phase_marker || '');
    // Phase 3E.2.1 human-copy acceptance markers must produce customer drafts.
    // Keep suppression for explicit TEST / PROBABLE_TEST markers (fixture H).
    const humanAcceptance = /PHASE_3E2_1_[BCDG]_[A-Z0-9_]+_HUMAN\b/i.test(markerBlob)
      && !(/_TEST_|PROBABLE_TEST/i.test(markerBlob));
    if (!humanAcceptance && /SYNTHETIC_TEST|PHASE_3E1|PHASE_3E2|PHASE_3D/i.test(markerBlob)) {
      reasons.push('phase_marker');
    }
  }
  if (/900\s*111\s*22\s*33|lead\.test@example\.com/i.test([phone, email].join(' '))) {
    reasons.push('synthetic_contact');
  }
  return { is_probable_test: reasons.length > 0, test_reason_codes: reasons };
}

/**
 * Intent precedence:
 * 1 explicit comment → 2 structured fields → 3 form selection → 4 source page → 5 subject/form title
 */
export function resolveIntent({
  comment_normalized,
  website_state,
  form_offer,
  source_topic,
  email_subject,
  communication_preference,
  is_probable_test,
}) {
  const comment = String(comment_normalized || '').trim();
  const lower = comment.toLowerCase();
  let resolved_service = 'NeedsClarification';
  let secondary_service = '';
  let explicit_client_intent = '';
  let intent_evidence_source = 'none';
  let intent_conflict = false;
  let parser_confidence = 'medium';

  const wantsSite = /(?:хочу|нужен|нужна).{0,24}сайт|(?:сделать|создать|разработ)\w*.{0,16}сайт|сайт\s+(?:под\s+ключ|с\s+нуля)/i.test(comment);
  const wantsSeo = /\bseo\b|продвиж|продвиг|поисков/i.test(lower);
  const wantsAudit = /аудит|audit|провер/i.test(lower);
  const wantsDirect = /директ|контекст|\bppc\b|реклам/i.test(lower);
  const wantsAi = /ai\s*search|гео\b|geo\b|нейросет|ai\s*visibility/i.test(lower);
  const siteThenSeo = /сайт.{0,60}(?:потом|затем|после).{0,40}(?:продвиж|продвиг|seo)/i.test(comment)
    || /сделать\s+сайт.{0,60}(?:продвиж|продвиг|seo)/i.test(comment)
    || /сайт.{0,40}и\s+(?:потом\s+)?(?:его\s+)?(?:продвиж|продвиг)/i.test(comment);

  if (comment && !isCommPreferenceOnly(comment)) {
    explicit_client_intent = comment.slice(0, 280);
    intent_evidence_source = 'client_comment';
    parser_confidence = 'high';
    if (siteThenSeo || (wantsSite && wantsSeo)) {
      resolved_service = 'WebsiteDevelopmentSEO';
    } else if (wantsSite) {
      resolved_service = 'WebsiteDevelopment';
    } else if (wantsAi) {
      resolved_service = 'AISearch';
    } else if (wantsDirect) {
      resolved_service = 'Direct';
    } else if (wantsSeo && !wantsAudit) {
      resolved_service = website_state === 'provided' ? 'SEO' : 'NeedsClarification';
    } else if (wantsAudit) {
      resolved_service = 'Audit';
    } else if (/^seo\.?$/i.test(comment.trim()) && website_state === 'provided') {
      resolved_service = 'SEO';
      parser_confidence = 'medium';
    } else {
      resolved_service = 'NeedsClarification';
      parser_confidence = 'low';
    }
  } else if (form_offer) {
    intent_evidence_source = 'form_offer';
    if (/аудит/i.test(form_offer)) resolved_service = 'Audit';
    else if (/директ/i.test(form_offer)) resolved_service = 'Direct';
    else if (/сайт/i.test(form_offer)) resolved_service = 'WebsiteDevelopment';
    else resolved_service = 'NeedsClarification';
    parser_confidence = 'low';
  } else if (source_topic) {
    intent_evidence_source = 'source_page';
    const map = {
      free_audit: 'Audit',
      audit: 'Audit',
      seo: 'SEO',
      moscow_seo: 'SEO',
      foreign_seo: 'SEO',
      new_site_seo: 'WebsiteDevelopmentSEO',
      website_development: 'WebsiteDevelopment',
      ai_search: 'AISearch',
      contextual_ads: 'Direct',
    };
    resolved_service = map[source_topic] || 'NeedsClarification';
    parser_confidence = 'low';
  } else if (/аудит/i.test(email_subject || '')) {
    intent_evidence_source = 'email_subject';
    resolved_service = 'Audit';
    parser_confidence = 'low';
  }

  // Weak form title must not override strong comment (already handled by order).
  // Flag conflict when form says Audit but comment wants development.
  if (intent_evidence_source === 'client_comment'
    && /аудит/i.test(form_offer || '')
    && (resolved_service === 'WebsiteDevelopment' || resolved_service === 'WebsiteDevelopmentSEO')) {
    intent_conflict = true;
  }

  if (communication_preference && resolved_service === 'NeedsClarification' && !comment) {
    explicit_client_intent = '';
  }

  if (is_probable_test && (!comment || /тест/i.test(comment))) {
    // Keep form context but mark clarification/test — do not invent business task
    if (!explicit_client_intent || /тест/i.test(explicit_client_intent)) {
      if (/аудит/i.test(form_offer || '') || source_topic === 'free_audit') {
        // retain Audit as form context but confidence low
        if (resolved_service === 'NeedsClarification') resolved_service = 'Audit';
      }
    }
  }

  const tax = SERVICE_TAXONOMY[resolved_service] || SERVICE_TAXONOMY.NeedsClarification;
  return {
    explicit_client_intent,
    resolved_service: tax.machine,
    resolved_service_label: tax.label,
    secondary_service,
    intent_evidence_source,
    intent_conflict,
    parser_confidence,
    service_compat: SERVICE_COMPAT[tax.machine] || 'Other',
  };
}

export function buildRequestSummary({ resolved_service, website_state, comment_normalized, communication_preference }) {
  const svc = resolved_service;
  if (svc === 'WebsiteDevelopmentSEO') return 'Нужен новый сайт с последующим SEO-продвижением.';
  if (svc === 'WebsiteDevelopment') return 'Нужен новый сайт.';
  if (svc === 'SEO' && website_state === 'provided') return 'Требуется SEO-продвижение существующего сайта.';
  if (svc === 'SEO') return 'Требуется SEO-продвижение; нужны уточнения.';
  if (svc === 'Audit' && website_state === 'provided' && comment_normalized && !isCommPreferenceOnly(comment_normalized) && comment_normalized.length > 20) {
    return 'Запрошен аудит сайта с описанной задачей.';
  }
  if (svc === 'Audit') return 'Запрошен аудит сайта; конкретная задача не указана.';
  if (svc === 'AISearch') return 'Интерес к AI Search / GEO / видимости в нейросетях.';
  if (svc === 'Direct') return 'Интерес к контекстной рекламе / Яндекс Директ.';
  if (communication_preference === 'telegram') return 'Контакт через Telegram; задача требует уточнения.';
  if (svc === 'NeedsClarification') return 'Задача требует уточнения.';
  return 'Заявка получена; требуется уточнение задачи.';
}

export function assessLeadQuality({
  hasContact,
  website_state,
  resolved_service,
  comment_normalized,
  is_probable_test,
  parse_status,
  name,
}) {
  if (is_probable_test) {
    return { lead_quality: 'test', lead_quality_label: 'Тестовая заявка', quality_status: 'ok' };
  }
  if (!hasContact || parse_status === 'failed') {
    return { lead_quality: 'insufficient', lead_quality_label: 'Недостаточно данных', quality_status: 'bad' };
  }
  const meaningfulComment = comment_normalized && !isCommPreferenceOnly(comment_normalized) && comment_normalized.length >= 3;
  const siteOkForSvc = (
    resolved_service === 'WebsiteDevelopment'
    || resolved_service === 'WebsiteDevelopmentSEO'
  )
    ? (website_state === 'explicitly_absent' || website_state === 'provided' || website_state === 'missing')
    : (website_state === 'provided' || website_state === 'explicitly_absent');

  const taskClear = resolved_service !== 'NeedsClarification' && (
    meaningfulComment
    || resolved_service === 'WebsiteDevelopment'
    || resolved_service === 'WebsiteDevelopmentSEO'
  );

  // Website development with no site can still be data-sufficient
  if (hasContact && taskClear && (
    website_state === 'provided'
    || ((resolved_service === 'WebsiteDevelopment' || resolved_service === 'WebsiteDevelopmentSEO')
      && (website_state === 'explicitly_absent' || website_state === 'missing'))
  )) {
    return { lead_quality: 'sufficient', lead_quality_label: 'Данных достаточно', quality_status: 'ok' };
  }

  if (hasContact && (!taskClear || !siteOkForSvc || !name)) {
    return { lead_quality: 'needs_clarification', lead_quality_label: 'Нужны уточнения', quality_status: 'needs_data' };
  }

  return { lead_quality: 'needs_clarification', lead_quality_label: 'Нужны уточнения', quality_status: 'needs_data' };
}

export function computeMissingInformation({
  resolved_service,
  website_state,
  hasContact,
  name,
  comment_normalized,
}) {
  // Human-readable manager labels (not machine reason codes).
  // Service-level intent already known must NOT be labeled as a missing "задача".
  const missing = [];
  if (!hasContact) missing.push('контакт');
  if (!name) missing.push('имя');

  const comment = String(comment_normalized || '').trim();
  const needsExistingSite = ['Audit', 'SEO'].includes(resolved_service);
  if (needsExistingSite && website_state !== 'provided') {
    if (website_state !== 'explicitly_absent') missing.push('сайт');
  }

  if (resolved_service === 'WebsiteDevelopment' || resolved_service === 'WebsiteDevelopmentSEO') {
    if (!comment || comment.length < 12) {
      missing.push('тип бизнеса');
      missing.push('функциональность');
    } else {
      if (!/бизнес|ниша|отрасл|магазин|услуг|компани/i.test(comment)) missing.push('тип бизнеса');
      if (!/функц|каталог|форм|оплат|интегр/i.test(comment)) missing.push('функциональность');
    }
    if (resolved_service === 'WebsiteDevelopmentSEO') {
      if (!/регион|город|москв|росси|цель/i.test(comment || '')) missing.push('регион продвижения');
    }
  } else if (resolved_service === 'SEO') {
    if (!/регион|город|москв|спб|росси/i.test(comment)) missing.push('регион');
    if (!comment || comment.length < 12 || /^seo\.?$/i.test(comment)) missing.push('приоритеты продвижения');
  } else if (resolved_service === 'Audit') {
    // "нужен аудит" / short audit intent = service known; only focus details may be missing
    if (!comment || /^(аудит|нужен аудит|нужна проверка|нужно проверить(\s+сайт)?)\.?$/i.test(comment) || comment.length < 20) {
      if (!/конверси|корзин|трафик|позиц|ошибк|индекс|технич/i.test(comment)) {
        missing.push('фокус аудита');
      }
    }
  } else if (resolved_service === 'NeedsClarification' || resolved_service === 'Other') {
    if (!comment || isCommPreferenceOnly(comment)) missing.push('задача');
  } else if (!resolved_service && (!comment || isCommPreferenceOnly(comment))) {
    missing.push('задача');
  }

  return missing.filter((m, i, arr) => arr.indexOf(m) === i);
}

/**
 * First Reply Engine v2 entry (compat wrapper).
 * Keeps historical function name used by processor / harness / n8n SYNC.
 */
export function buildFirstReplyDraft(ctx) {
  return buildFirstReplyDraftV2({
    ...ctx,
    client_name: ctx.client_name || ctx.client_name_normalized || '',
    phone: ctx.phone || ctx.phone_normalized || '',
    email: ctx.email || ctx.email_normalized || '',
    messenger: ctx.messenger || ctx.telegram_contact_normalized || '',
  });
}

export function parseLeadItem(j = {}) {
  const now = new Date().toISOString();
  const isSynth = Boolean(j.synthetic_fixture || j.fixture_id || j.__synthetic);

  const subject = String(j.email_subject || j.subject || '').trim();
  const sender = String(j.sender_email || j.from || '').trim();
  const thread = String(j.gmail_thread_id || j.threadId || '').trim();
  const received = String(j.received_at || '').trim();

  let gmail_message_id = String(j.gmail_message_id || j.id || j.messageId || '').trim();
  if (!gmail_message_id) {
    if (isSynth) gmail_message_id = 'msg_synth_' + String(j.fixture_id || 'X');
    else {
      const raw = [thread, received, sender, subject, String(j.request_text || j.snippet || '').slice(0, 120)]
        .map((p) => String(p ?? '').trim().toLowerCase()).join('|');
      let h1 = 0x811c9dc5;
      for (let i = 0; i < raw.length; i++) { h1 ^= raw.charCodeAt(i); h1 = Math.imul(h1, 0x01000193); }
      let h2 = 5381;
      for (let i = 0; i < raw.length; i++) h2 = ((h2 << 5) + h2) ^ raw.charCodeAt(i);
      gmail_message_id = 'msg_' + ((h1 >>> 0).toString(16).padStart(8, '0')) + ((h2 >>> 0).toString(16).padStart(8, '0'));
    }
  }
  const lead_id = String(j.lead_id || ('lead_' + gmail_message_id));

  const rawBodyInput = String(j.request_text || j.text || j.textPlain || j.html || j.snippet || j.body || j.raw_text || '');
  const usedHtml = /<[a-z][\s\S]*>/i.test(rawBodyInput) && !j.textPlain;
  const normalizedBody = usedHtml ? htmlToPlainText(rawBodyInput) : normalizeSpaces(rawBodyInput);
  const extraction_path = usedHtml ? 'html_structure' : 'normalized_text';
  const { fields } = extractLabeledFields(normalizedBody);

  // RAW name preservation: never destroy "test"
  const client_name_raw = String(fields.name || j.parsed_name || j.client_name || j.name || '').trim();
  const client_name_normalized = isNamePlaceholder(client_name_raw) ? '' : client_name_raw;

  const contact_method_raw = String(fields.contact_method || '').trim();
  const contact_raw = String(fields.contact || '').trim();
  const comment_raw_full = String(fields.comment || '').trim();
  let comment_raw = comment_raw_full.replace(/\s*Отправлено\s+со\s*(страницы)?\s*$/i, '').trim();
  comment_raw = comment_raw.replace(/\s*IP\s*[:：].*$/i, '').trim();
  const comment_normalized = comment_raw.replace(/\s+/g, ' ').trim();

  let website = classifyWebsiteField(fields.site || '', comment_normalized);
  // Cross-field recovery only when missing/invalid
  if ((website.website_state === 'missing' || website.website_state === 'invalid_or_placeholder') && comment_normalized) {
    const recovered = recoverSiteFromComment(comment_normalized);
    if (recovered) {
      website = {
        website_raw: website.website_raw || recovered.website_raw,
        website_normalized: recovered.website_normalized,
        website_state: 'provided',
        alternative_contact_type: '',
        alternative_contact_value: '',
        warnings: [...(website.warnings || []), 'site_recovered_from_comment'],
      };
      // Remove recovered URL from normalized comment display (keep raw)
      // do not mutate comment_raw
    }
  }

  // Explicit absent phrases that look like site values
  if (website.website_state === 'invalid_or_placeholder' && isExplicitAbsentPhrase(website.website_raw)) {
    website.website_state = 'explicitly_absent';
    website.website_normalized = '';
  }

  const commentPref = isCommPreferenceOnly(comment_normalized) ? inferCommPreference(comment_normalized) : null;
  const interpreted = interpretContactMethod(contact_method_raw, contact_raw, {
    phone_direct: fields.phone_direct,
    email_direct: fields.email_direct,
    messenger_extra: website.website_state === 'alternative_contact' ? website.alternative_contact_value : '',
    comment_preference: commentPref,
  });

  // Pull telegram username from comment if present
  let telegram_from_comment = '';
  const tgInComment = comment_normalized.match(/@[a-zA-Z0-9_]{4,32}/);
  if (tgInComment) telegram_from_comment = tgInComment[0];

  const phone_normalized = String(j.parsed_phone || j.phone || interpreted.phone || '').trim();
  const email_normalized = String(j.parsed_email || j.email || interpreted.email || '').trim();
  let telegram_contact_normalized = String(j.parsed_messenger || j.messenger || interpreted.messenger || '').trim();
  if (!telegram_contact_normalized && website.alternative_contact_type === 'telegram') {
    telegram_contact_normalized = website.alternative_contact_value;
  }
  if (!telegram_contact_normalized && telegram_from_comment) {
    telegram_contact_normalized = telegram_from_comment;
  }

  let contact_method = interpreted.contact_method;
  if (contact_method === 'unknown' && commentPref) contact_method = commentPref;
  if (contact_method === 'unknown' && website.alternative_contact_type) contact_method = website.alternative_contact_type;

  const form_offer_raw = detectFormOffer(normalizedBody, subject) || String(j.form_name || '').trim();
  const form_offer = form_offer_raw;
  const form_name = form_offer || String(j.form_name || '').trim();

  const pageRaw = String(fields.page || '').trim();
  const source_page_title = normalizeSourcePage(pageRaw);
  const source_page_url = /^https?:\/\//i.test(pageRaw) ? pageRaw.split(/\s+/)[0] : '';
  const source_topic = classifySourceTopic(source_page_title, subject, form_offer);

  const testInfo = classifyProbableTest({
    name: client_name_normalized || client_name_raw,
    comment: comment_normalized,
    site: website.website_normalized || website.website_raw,
    phone: phone_normalized,
    email: email_normalized,
    marker: j.marker,
    phase_marker: j.phase_marker,
  });

  const intent = resolveIntent({
    comment_normalized,
    website_state: website.website_state,
    form_offer,
    source_topic,
    email_subject: subject,
    communication_preference: commentPref || '',
    is_probable_test: testInfo.is_probable_test,
  });

  const request_summary = buildRequestSummary({
    resolved_service: intent.resolved_service,
    website_state: website.website_state,
    comment_normalized,
    communication_preference: commentPref || '',
  });

  // Compat request_text: real comment only (do NOT concatenate form offer)
  let request_text = comment_normalized;
  let request_insufficient = false;
  if (commentPref && !comment_normalized) request_insufficient = true;
  if (commentPref && isCommPreferenceOnly(comment_normalized)) {
    request_insufficient = true;
    request_text = '';
  }
  if (!request_text && !commentPref) {
    const { residual } = stripLabeledPayload(normalizedBody);
    const cleaned = residual.replace(/Заявка\s+на\s+бесплатный\s+аудит/gi, ' ').replace(/\s+/g, ' ').trim();
    if (cleaned && cleaned.length > 12) request_text = cleaned;
  }
  if (!request_text || request_text.length < 3) request_insufficient = true;
  request_text = String(request_text || '').slice(0, 4000);

  const hasContact = Boolean(phone_normalized || email_normalized || telegram_contact_normalized);
  const parse_status = hasContact || request_text || comment_normalized
    ? ((client_name_normalized || client_name_raw || website.website_normalized || comment_normalized) ? 'ok' : 'partial')
    : 'failed';

  const quality = assessLeadQuality({
    hasContact,
    website_state: website.website_state,
    resolved_service: intent.resolved_service,
    comment_normalized,
    is_probable_test: testInfo.is_probable_test,
    parse_status,
    name: client_name_normalized || client_name_raw,
  });

  const missing_information = computeMissingInformation({
    resolved_service: intent.resolved_service,
    website_state: website.website_state,
    hasContact,
    name: client_name_normalized || client_name_raw,
    comment_normalized,
  });

  const reply = buildFirstReplyDraft({
    client_name: client_name_normalized || client_name_raw,
    client_name_normalized: client_name_normalized || client_name_raw,
    website_state: website.website_state,
    website_normalized: website.website_normalized,
    resolved_service: intent.resolved_service,
    secondary_service: intent.secondary_service,
    comment_normalized,
    missing_information,
    hasContact,
    is_probable_test: testInfo.is_probable_test,
    alternative_contact_type: website.alternative_contact_type,
    alternative_contact_value: website.alternative_contact_value,
    communication_preference: commentPref || '',
    phone: phone_normalized,
    email: email_normalized,
    messenger: telegram_contact_normalized,
    explicit_client_intent: intent.explicit_client_intent,
    source_topic,
  });

  const warnings = [
    ...(website.warnings || []),
  ];
  if (fields.contact && !hasContact) warnings.push('contact_unrecognized');
  if (commentPref) warnings.push('comment_is_preference_only');
  if (intent.intent_conflict) warnings.push('intent_conflict_form_vs_comment');
  if (extraction_path === 'html_structure') warnings.push('html_extraction');

  // Compat aliases used by existing processor/sheets
  const parsed_name = client_name_normalized || client_name_raw;
  const parsed_site = website.website_state === 'provided' ? website.website_normalized : '';
  const parsed_messenger = telegram_contact_normalized;
  const parsed_phone = phone_normalized;
  const parsed_email = email_normalized;

  return {
    ...j,
    lead_id,
    gmail_message_id,
    gmail_thread_id: thread,
    received_at: j.received_at || now,
    source: j.source || (isSynth ? 'synthetic' : 'gmail'),
    email_subject: subject,
    sender_email: sender,
    request_page: j.request_page || source_page_title || '',
    form_name,
    form_offer,
    form_offer_raw,
    utm_source: j.utm_source || '',
    utm_medium: j.utm_medium || '',
    utm_campaign: j.utm_campaign || '',
    utm_term: j.utm_term || '',
    utm_content: j.utm_content || '',

    // Semantic raw/normalized
    client_name_raw,
    client_name_normalized: client_name_normalized || client_name_raw,
    contact_method_raw,
    contact_method_normalized: contact_method,
    contact_raw,
    phone_normalized,
    email_normalized,
    telegram_contact_normalized,
    website_raw: website.website_raw,
    website_normalized: website.website_normalized,
    website_state: website.website_state,
    alternative_contact_type: website.alternative_contact_type,
    alternative_contact_value: website.alternative_contact_value,
    comment_raw,
    comment_normalized,
    source_page_title,
    source_page_url,
    source_topic,
    explicit_client_intent: intent.explicit_client_intent,
    resolved_service: intent.resolved_service,
    resolved_service_label: intent.resolved_service_label,
    secondary_service: intent.secondary_service,
    request_summary,
    lead_quality: quality.lead_quality,
    lead_quality_label: quality.lead_quality_label,
    is_probable_test: testInfo.is_probable_test,
    test_reason_codes: testInfo.test_reason_codes.join(','),
    parser_confidence: intent.parser_confidence,
    missing_information: missing_information.join(', '),
    intent_evidence_source: intent.intent_evidence_source,
    intent_conflict: intent.intent_conflict,
    extraction_path,
    semantic_model_version: SEMANTIC_MODEL_VERSION,

    // Compat fields
    parsed_name,
    parsed_phone,
    parsed_email,
    parsed_messenger,
    parsed_site,
    contact_method,
    communication_preference: commentPref || '',
    request_insufficient,
    request_text,
    service: intent.service_compat,
    service_machine: intent.resolved_service,
    service_label: intent.resolved_service_label,
    summary: request_summary,
    quality_status: quality.quality_status,
    missing_fields: missing_information.join(', '),
    first_reply_text: reply.first_reply_text,
    first_reply_source: reply.first_reply_source,
    first_reply_version: reply.first_reply_version || FIRST_REPLY_VERSION,
    first_reply_mode: reply.first_reply_mode || '',
    first_reply_subject: reply.first_reply_subject || '',
    first_reply_questions: Array.isArray(reply.first_reply_questions) ? reply.first_reply_questions.join(' | ') : (reply.first_reply_questions || ''),
    first_reply_reason_codes: Array.isArray(reply.first_reply_reason_codes) ? reply.first_reply_reason_codes.join(',') : (reply.first_reply_reason_codes || ''),
    first_reply_omitted_reason: reply.first_reply_omitted_reason || reply.reply_omitted_reason || '',
    first_reply_ready: reply.first_reply_ready === true,
    first_reply_warnings: Array.isArray(reply.first_reply_warnings) ? reply.first_reply_warnings.join(',') : (reply.first_reply_warnings || ''),
    reply_template_version: reply.reply_template_version || FIRST_REPLY_VERSION,
    client_name: parsed_name,
    phone: parsed_phone,
    email: parsed_email,
    messenger: parsed_messenger,
    site: parsed_site,

    calc_detected: String(j.calc_detected || 'false'),
    calc_data: j.calc_data || '',
    ip: j.ip || fields.ip || '',
    parser_version: PARSER_VERSION,
    parse_status,
    parse_warnings: warnings.filter(Boolean).join(',') || j.parse_warnings || '',
    parser_warnings: warnings.filter(Boolean).join(','),
    workflow_version: 'operational.dev.phase3e1',
    message_format_version: j.message_format_version || MESSAGE_FORMAT_VERSION_DEFAULT,
    raw_logged_at: now,
    raw_text: String(j.raw_text || normalizedBody).slice(0, 8000),
    __synthetic: isSynth,
    fixture_id: j.fixture_id || null,
    marker: j.marker || (isSynth ? 'SYNTHETIC_TEST' : ''),
    phase_marker: j.phase_marker || (isSynth ? 'PHASE_3E1' : ''),
    exclude_from_prod_stats: testInfo.is_probable_test || isSynth,
  };
}
