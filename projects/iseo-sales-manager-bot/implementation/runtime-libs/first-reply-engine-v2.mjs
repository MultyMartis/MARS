/**
 * First Reply Engine v2.1 — Human Reply Style v1.
 * Deterministic, context-aware, manager-ready drafts for Оля.
 * AI OFF. Never auto-sends to customers. Known-info guards are silent.
 * Versions: first_reply=sm-reply-v2.1, human_reply_style=sm-human-v1.0
 */

export const FIRST_REPLY_VERSION = 'sm-reply-v2.1';
export const HUMAN_REPLY_STYLE_VERSION = 'sm-human-v1.0';
export const FIRST_REPLY_MAX_CHARS = 900;
export const FIRST_REPLY_TARGET_MAX = 700;
export const FIRST_REPLY_MAX_QUESTION_GROUPS = 3;

const PLACEHOLDER_NAMES = new Set([
  'name', 'имя', 'ваше имя', 'фио', 'test', 'тест', 'testing',
  'asdf', 'qwerty', 'xxx', 'n/a', 'na', 'none', 'null', 'undefined',
  '-', '—', '.', '..', '...',
]);

export const FORBIDDEN_PHRASE_PATTERNS = [
  /адрес\s+сайта\s+уже\s+указан/i,
  /повторно\s+присылать\s+(его\s+)?не\s+нужно/i,
  /повторно\s+присылать\s+адрес/i,
  /текущий\s+сайт\s+не\s+указан/i,
  /это\s+ожидаемо\s+для\s+задачи/i,
  /адрес\s+существующего\s+сайта\s+не\s+нужен/i,
  /мы\s+учли\s+ваш\s+комментарий/i,
  /по\s+данным\s+формы/i,
  /система\s+определила/i,
  /поле\s+отсутствует/i,
  /\bwebsite_state\b/i,
  /\bresolved_service\b/i,
  /\bparser\b/i,
  /недостающие\s+поля/i,
  /контакт\s+нормализован/i,
  /сайт\s+\S+\s+уже\s+указан/i,
  /не\s+нужно\s+повторно\s+присылать/i,
];

const PROMISE_PATTERNS = [
  /гарантир/i,
  /в\s+топ[-\s]?1/i,
  /100\s*%/i,
  /обязательно\s+попад[её]те/i,
  /запустим\s+за\s+\d+/i,
  /точн(ая|ые)\s+стоимость/i,
  /бесплатно\s+выведем/i,
];

export function isUsableClientName(raw) {
  const name = String(raw || '').trim();
  if (!name) return false;
  if (name.length < 2) return false;
  if (/^[\d\s\-_.@]+$/.test(name)) return false;
  if (/^[^a-zA-Zа-яА-ЯёЁ]+$/.test(name)) return false;
  if (PLACEHOLDER_NAMES.has(name.toLowerCase())) return false;
  if (/^[=#]/.test(name)) return false;
  if (/^#error/i.test(name)) return false;
  return true;
}

export function buildGreeting(clientName) {
  if (isUsableClientName(clientName)) {
    return `Здравствуйте, ${String(clientName).trim()}!`;
  }
  return 'Здравствуйте!';
}

function asList(v) {
  if (Array.isArray(v)) return v.map((s) => String(s || '').trim()).filter(Boolean);
  return String(v || '').split(/[;,\n]/).map((s) => s.trim()).filter(Boolean);
}

function hasMeaningfulComment(comment) {
  const c = String(comment || '').trim();
  if (!c) return false;
  if (c.length < 8) return false;
  if (/^(seo|audit|аудит|директ|сайт)\.?$/i.test(c)) return false;
  if (/^(в\s*тг|telegram|whatsapp|напишите|перезвоните)\.?$/i.test(c)) return false;
  return true;
}

function isVagueTask(comment, resolvedService) {
  const c = String(comment || '').trim();
  if (!c) return true;
  if (/^(seo|audit|аудит|директ|сайт|хочу сайт|нужно проверить(\s+сайт)?|нужен аудит|нужна проверка|проверить сайт)\.?$/i.test(c)) return true;
  if (/^(нужно|надо)\s+проверить(\s+сайт)?\.?$/i.test(c)) return true;
  if (resolvedService === 'Audit' && c.length < 28 && !/конверси|корзин|трафик|позиц|ошибк|индекс/i.test(c)) return true;
  if (resolvedService === 'SEO' && (c.length < 12 || /^seo\.?$/i.test(c))) return true;
  return !hasMeaningfulComment(c);
}

/**
 * Detect a safe problem/theme class from the customer comment.
 * Deterministic keyword rules only — no AI/NLP.
 */
export function detectMeaningfulTheme(comment, resolvedService) {
  const c = String(comment || '').trim();
  const service = String(resolvedService || '');

  if (/конверси/i.test(c) && /корзин|checkout|оформлен/i.test(c)) return 'conversion_cart';
  if (/конверси/i.test(c)) return 'conversion_cart';
  if (/пада(ет|ют)?\s+трафик|снижен(ие|ия)\s+трафик|трафик\s+(падает|упал|снизил)/i.test(c)) return 'traffic_decline';
  if (/позици|видимост|ранжир|выдач/i.test(c)) return 'rankings_visibility';
  if (/ошибк|не\s+работает|баг|слом|\b404\b|\b500\b/i.test(c)) return 'technical_errors';
  if (/индекс/i.test(c)) return 'indexing';
  if (/редизайн|миграц|переезд/i.test(c)) return 'site_redesign_migration';
  if (/(реклам|директ).{0,40}(нет|не\s+(да|принос))|(нет|не\s+да).{0,40}(заяв|лид|обращ)/i.test(c)) return 'ads_no_leads';
  if (service === 'WebsiteDevelopmentSEO' || (/сайт/i.test(c) && /seo|продвиж/i.test(c))) return 'website_plus_seo';
  if (service === 'WebsiteDevelopment' || /новый\s+сайт|хочу\s+сайт|нужен\s+сайт|разработ/i.test(c)) return 'need_new_website';
  if (/\bai\b|гео|geo|нейросет|chatgpt/i.test(c)) return 'ai_geo_visibility';
  if (!c || isVagueTask(c, service)) return 'vague_service';
  if (hasMeaningfulComment(c)) return 'unclear_request';
  return 'vague_service';
}

export function applyKnownInformationGuard(ctx, candidateQuestions) {
  const suppressed = [];
  const website_state = String(ctx.website_state || '');
  const phone = String(ctx.phone || ctx.phone_normalized || '').trim();
  const email = String(ctx.email || ctx.email_normalized || '').trim();
  const messenger = String(ctx.messenger || ctx.telegram_contact_normalized || ctx.alternative_contact_value || '').trim();
  const altType = String(ctx.alternative_contact_type || '').toLowerCase();
  const comment = String(ctx.comment_normalized || '').trim();
  const resolved = String(ctx.resolved_service || '');
  const regionKnown = /регион|город|москв|спб|питер|росси/i.test(comment);
  const theme = detectMeaningfulTheme(comment, resolved);

  const out = [];
  for (const q of candidateQuestions) {
    const id = q.id || q.code || '';
    const text = String(q.text || q).trim();
    if (!text) continue;

    let suppress = null;
    const asksWebsiteUrl = /пришлите[^\n]{0,60}сайт|укажите[^\n]{0,60}(адрес\s+)?сайт|адрес\s+(вашего\s+)?сайт|url(\s+сайт)?|ссылк[уи]\s+на\s+сайт|подтвердите[^\n]{0,40}адрес сайт/i.test(text);
    if (asksWebsiteUrl && (website_state === 'provided' || website_state === 'explicitly_absent')) {
      suppress = website_state === 'provided' ? 'suppress_ask_website_provided' : 'suppress_ask_website_absent';
    } else if (/пришлите[^\n]{0,40}телефон|укажите[^\n]{0,40}телефон|ваш номер телефона/i.test(text) && phone) {
      suppress = 'suppress_ask_phone_known';
    } else if (/пришлите[^\n]{0,40}e-?mail|укажите[^\n]{0,40}почт|ваш e-?mail/i.test(text) && email) {
      suppress = 'suppress_ask_email_known';
    } else if (/пришлите[^\n]{0,40}telegram|укажите[^\n]{0,40}telegram|ваш username|пришлите[^\n]{0,40}телеграм/i.test(text) && (messenger || altType === 'telegram')) {
      suppress = 'suppress_ask_telegram_known';
    } else if (/что\s+вам\s+требуется|какая\s+услуга\s+нужна|какой\s+сервис\s+нужен/i.test(text)
      && resolved && resolved !== 'NeedsClarification' && resolved !== 'Other') {
      suppress = 'suppress_ask_service_known';
    } else if (/приоритетн(ые|ых)\s+страниц|какой\s+результат\s+аудита|главный\s+результат/i.test(text)
      && theme === 'conversion_cart') {
      suppress = 'suppress_generic_audit_for_cart_theme';
    } else if (/по\s+какому\s+региону/i.test(text) && regionKnown) {
      suppress = 'suppress_ask_region_known';
    }

    if (suppress) {
      suppressed.push(suppress);
      continue;
    }
    out.push({ id: id || `q${out.length + 1}`, text });
  }

  return {
    allowedQuestions: out.slice(0, FIRST_REPLY_MAX_QUESTION_GROUPS),
    suppressedCodes: [...new Set(suppressed)],
  };
}

function formatQuestions(questions, leadIn) {
  if (!questions.length) return [];
  if (questions.length === 1) {
    return ['', questions[0].text];
  }
  const header = leadIn || 'Подскажите, пожалуйста:';
  const lines = ['', header];
  questions.forEach((q, i) => {
    lines.push(`${i + 1}) ${q.text}`);
  });
  return lines;
}

function closingBlock() {
  return ['', 'С уважением,', 'команда i-SEO'];
}

function trimToSafeLength(text) {
  let t = String(text || '').replace(/\n{3,}/g, '\n\n').trim();
  if (t.length <= FIRST_REPLY_MAX_CHARS) return t;
  const closeIdx = t.lastIndexOf('С уважением,');
  if (closeIdx > 200) {
    const head = t.slice(0, Math.min(closeIdx, FIRST_REPLY_MAX_CHARS - 40)).trim();
    t = `${head}\n\nС уважением,\nкоманда i-SEO`;
  }
  if (t.length > FIRST_REPLY_MAX_CHARS) {
    t = `${t.slice(0, FIRST_REPLY_MAX_CHARS - 1).trim()}…`;
  }
  return t;
}

function subjectFor(ctx) {
  const service = String(ctx.resolved_service || '');
  const map = {
    Audit: 'Аудит сайта',
    SEO: 'SEO',
    WebsiteDevelopment: 'Разработка сайта',
    WebsiteDevelopmentSEO: 'Разработка сайта и SEO',
    AISearch: 'AI Search / GEO',
    Direct: 'Контекстная реклама',
    NeedsClarification: 'Уточнение задачи',
    Other: 'Обращение',
  };
  return map[service] || 'Обращение';
}

function siteLabel(ctx) {
  return String(ctx.website_normalized || ctx.site || '').trim();
}

/**
 * Build natural acknowledgement + questions for the case.
 * Never narrates parser/guard internals.
 */
function composeHumanDraft(ctx) {
  const service = String(ctx.resolved_service || '');
  const siteState = String(ctx.website_state || '');
  const site = siteLabel(ctx);
  const comment = String(ctx.comment_normalized || '').trim();
  const altType = String(ctx.alternative_contact_type || '').toLowerCase();
  const theme = detectMeaningfulTheme(comment, service);
  const greeting = buildGreeting(ctx.client_name || ctx.client_name_normalized);
  const questions = [];
  const ack = [];

  // Telegram preference (HITL-safe wording)
  if (altType === 'telegram' || ctx.communication_preference === 'telegram') {
    ack.push('Спасибо за обращение. Учли, что вам удобнее общаться в Telegram.');
    if (service === 'NeedsClarification' || service === 'Other' || !service) {
      questions.push({ id: 'nc_task', text: 'Подскажите, пожалуйста, с какой задачей нужна помощь: аудит сайта, SEO-продвижение, разработка или реклама?' });
    }
  }

  if (service === 'Audit') {
    if (siteState === 'provided' && site) {
      ack.push(`Спасибо за заявку на аудит сайта ${site}.`);
      if (theme === 'conversion_cart') {
        ack.push('Поняли, что проблема связана со снижением конверсии в корзине.');
        questions.push({ id: 'cart_when', text: 'Когда вы заметили снижение?' });
        questions.push({ id: 'cart_changes', text: 'Были ли перед этим изменения на сайте, в рекламе или в процессе оформления заказа?' });
        questions.push({ id: 'cart_analytics', text: 'Есть ли доступ к Метрике или другой аналитике, где видно изменение показателей?' });
      } else if (theme === 'traffic_decline') {
        ack.push('Поняли, что вас беспокоит снижение трафика.');
        questions.push({ id: 'tr_when', text: 'Когда вы заметили падение трафика?' });
        questions.push({ id: 'tr_changes', text: 'Были ли перед этим изменения на сайте или в рекламе?' });
        questions.push({ id: 'tr_analytics', text: 'Есть ли доступ к Метрике или другой аналитике?' });
      } else if (theme === 'rankings_visibility') {
        ack.push('Поняли, что важны позиции и видимость в поиске.');
        questions.push({ id: 'rk_queries', text: 'По каким запросам или разделам заметили изменения?' });
        questions.push({ id: 'rk_when', text: 'Когда это стало заметно?' });
      } else if (theme === 'technical_errors') {
        ack.push('Поняли, что нужно разобраться с техническими проблемами.');
        questions.push({ id: 'te_what', text: 'Какие ошибки или сбои вы замечаете чаще всего?' });
        questions.push({ id: 'te_where', text: 'На каких страницах или этапах это проявляется?' });
      } else if (isVagueTask(comment, service) || theme === 'vague_service') {
        questions.push({
          id: 'audit_focus_natural',
          text: 'Подскажите, пожалуйста, что сейчас беспокоит больше всего: технические ошибки, позиции в поиске, снижение трафика или работа отдельных страниц? Это поможет сделать проверку более полезной именно для вашей задачи.',
        });
      } else {
        ack.push('Поняли вашу задачу по аудиту.');
        questions.push({ id: 'audit_when', text: 'Когда проблема стала заметной?' });
        questions.push({ id: 'audit_analytics', text: 'Есть ли доступ к Метрике или Вебмастеру?' });
      }
    } else {
      ack.push('Спасибо за обращение по аудиту.');
      questions.push({ id: 'audit_site_exists', text: 'Сайт уже существует, или его ещё только предстоит создать?' });
      questions.push({ id: 'audit_goal_alt', text: 'Если сайт есть — пришлите, пожалуйста, его адрес и кратко опишите, что хотите проверить.' });
    }
  } else if (service === 'SEO') {
    if (siteState === 'provided' && site) {
      ack.push(`Спасибо за заявку по SEO для сайта ${site}.`);
      if (!isVagueTask(comment, service) && theme !== 'vague_service') {
        if (theme === 'traffic_decline') ack.push('Поняли, что вас беспокоит снижение трафика.');
        else if (theme === 'rankings_visibility') ack.push('Поняли, что важны позиции в поиске.');
        else ack.push('Поняли вашу задачу по продвижению.');
      }
      if (!/регион|город|москв|спб/i.test(comment)) {
        questions.push({ id: 'seo_region', text: 'По какому региону планируется продвижение?' });
      }
      questions.push({ id: 'seo_priority', text: 'Какие услуги или товары сейчас в приоритете?' });
    } else if (siteState === 'explicitly_absent') {
      ack.push('Спасибо за интерес к SEO.');
      questions.push({ id: 'seo_or_dev', text: 'Нужно сначала создать сайт, а затем заняться SEO, или сайт уже есть под другим адресом?' });
    } else {
      ack.push('Спасибо за интерес к SEO.');
      questions.push({ id: 'seo_site', text: 'Подтвердите, пожалуйста, адрес сайта для SEO.' });
      questions.push({ id: 'seo_region', text: 'По какому региону нужно продвижение?' });
    }
  } else if (service === 'WebsiteDevelopment') {
    if (!ack.length) ack.push('Спасибо за обращение. Поняли, что вам нужен новый сайт.');
    else ack.push('Поняли, что вам нужен новый сайт.');
    questions.push({ id: 'dev_business', text: 'Чем занимается компания и для кого будет сайт?' });
    questions.push({ id: 'dev_features', text: 'Какие задачи он должен решать: представлять услуги, принимать заявки, продавать товары или что-то другое?' });
    questions.push({ id: 'dev_examples', text: 'Есть ли примеры сайтов, которые вам нравятся?' });
  } else if (service === 'WebsiteDevelopmentSEO') {
    if (!ack.length) {
      ack.push('Спасибо за обращение. Поняли задачу: нужно разработать новый сайт и затем продвигать его в поиске.');
    } else {
      ack.push('Поняли задачу: нужно разработать новый сайт и затем продвигать его в поиске.');
    }
    questions.push({ id: 'combo_business', text: 'Чем занимается компания и какие услуги или товары нужно представить?' });
    questions.push({ id: 'combo_features', text: 'Какие функции понадобятся на сайте?' });
    questions.push({ id: 'combo_region', text: 'В каком регионе планируете продвижение?' });
  } else if (service === 'AISearch') {
    if (!ack.length) ack.push('Спасибо за интерес к видимости в AI-ответах и современном поиске.');
    if (siteState === 'provided' && site) {
      questions.push({ id: 'ai_audience', text: 'Какие регионы или аудитории для вас приоритетны?' });
      questions.push({ id: 'ai_focus', text: 'Что важнее сейчас: видимость в AI-ответах, классический поиск или оба направления?' });
    } else {
      questions.push({ id: 'ai_what', text: 'Какой бизнес или сайт нужно продвигать в AI-поиске?' });
      questions.push({ id: 'ai_audience', text: 'Какие регионы или аудитории приоритетны?' });
    }
  } else if (service === 'Direct') {
    if (!ack.length) ack.push('Спасибо за интерес к контекстной рекламе.');
    if (siteState === 'provided' && site) {
      questions.push({ id: 'ppc_products', text: 'Какие услуги или товары нужно рекламировать?' });
      questions.push({ id: 'ppc_region', text: 'По какому региону запускать рекламу?' });
      questions.push({ id: 'ppc_history', text: 'Кампании уже были, или запускаем впервые?' });
    } else {
      questions.push({ id: 'ppc_site', text: 'Есть ли сайт или посадочная страница для рекламы?' });
      questions.push({ id: 'ppc_products', text: 'Какие услуги или товары нужно рекламировать?' });
    }
  } else if (!questions.length) {
    if (!ack.length) ack.push('Спасибо за обращение.');
    questions.push({ id: 'nc_task', text: 'Подскажите, пожалуйста, с какой задачей нужна помощь: аудит сайта, SEO-продвижение, разработка или реклама?' });
  }

  // Deduplicate ack lines and drop empty
  const ackUnique = [...new Set(ack.map((s) => String(s).trim()).filter(Boolean))];
  const leadIn = service === 'WebsiteDevelopment' || service === 'WebsiteDevelopmentSEO'
    ? 'Расскажите, пожалуйста:'
    : 'Подскажите, пожалуйста:';

  return { greeting, ack: ackUnique, questions, theme, leadIn };
}

export function lintFirstReply(text, ctx = {}, meta = {}) {
  const warnings = [];
  const failures = [];
  const value = String(text || '');
  const theme = String(meta.theme || detectMeaningfulTheme(ctx.comment_normalized, ctx.resolved_service));

  if (!value.trim() && meta.requireText !== false) failures.push('empty_reply');

  for (const pattern of FORBIDDEN_PHRASE_PATTERNS) {
    if (pattern.test(value)) failures.push(`forbidden_phrase:${pattern.source.slice(0, 40)}`);
  }

  if (value.length > FIRST_REPLY_MAX_CHARS) failures.push('max_chars_exceeded');
  else if (value.length > FIRST_REPLY_TARGET_MAX) warnings.push('reply_longer_than_target');

  const numbered = value.match(/(?:^|\n)\s*\d+\)/g);
  const groups = numbered ? numbered.length : (value.match(/\?/g) || []).length;
  if (groups > FIRST_REPLY_MAX_QUESTION_GROUPS) failures.push('too_many_question_groups');

  if (value.trim() && !/С уважением,/.test(value)) failures.push('missing_closing');

  for (const re of PROMISE_PATTERNS) {
    if (re.test(value) && !/не\s+обещаем|без\s+гарант/i.test(value)) {
      failures.push('unsupported_promise');
      break;
    }
  }

  if (/напишем\s+вам\s+в\s+telegram/i.test(value)) failures.push('telegram_auto_promise');

  // Duplicate sentence check (naive)
  const sentences = value.split(/\n+/).map((s) => s.trim()).filter((s) => s.length > 20);
  const seen = new Set();
  for (const s of sentences) {
    const key = s.toLowerCase();
    if (seen.has(key)) failures.push('duplicated_sentence');
    seen.add(key);
  }

  if (theme === 'conversion_cart' && value && !/конверси|корзин/i.test(value)) {
    failures.push('cart_theme_not_acknowledged');
  }
  if (theme === 'conversion_cart' && /приоритетн(ые|ых)\s+страниц|какой\s+результат\s+аудита/i.test(value)) {
    failures.push('generic_audit_used_for_cart_theme');
  }

  const siteState = String(ctx.website_state || '');
  if (siteState === 'provided' && /пришлите[^\n]{0,40}сайт|укажите[^\n]{0,40}адрес\s+сайт/i.test(value)) {
    failures.push('asks_known_website');
  }
  if (siteState === 'explicitly_absent' && /пришлите[^\n]{0,40}сайт|адрес\s+существующ/i.test(value)
    && (ctx.resolved_service === 'WebsiteDevelopment' || ctx.resolved_service === 'WebsiteDevelopmentSEO')) {
    failures.push('asks_absent_website');
  }

  if (meta.marker && value.includes(String(meta.marker))) failures.push('internal_marker_in_draft');

  return { ok: failures.length === 0, warnings, failures };
}

export function generateFirstReplyV2(ctx = {}) {
  const warnings = [];
  const isTest = ctx.is_probable_test === true || ctx.is_probable_test === 'true';
  const hasContact = ctx.hasContact !== false && ctx.contact_missing !== true
    && Boolean(
      String(ctx.phone || ctx.phone_normalized || '').trim()
      || String(ctx.email || ctx.email_normalized || '').trim()
      || String(ctx.messenger || ctx.telegram_contact_normalized || '').trim()
      || String(ctx.alternative_contact_value || '').trim()
      || ctx.hasContact === true,
    );

  const theme = detectMeaningfulTheme(ctx.comment_normalized, ctx.resolved_service);

  const base = {
    first_reply_version: FIRST_REPLY_VERSION,
    human_reply_style_version: HUMAN_REPLY_STYLE_VERSION,
    first_reply_mode: 'normal',
    first_reply_subject: subjectFor(ctx),
    first_reply_text: '',
    first_reply_questions: [],
    first_reply_reason_codes: [],
    first_reply_omitted_reason: '',
    first_reply_ready: false,
    first_reply_warnings: [],
    meaningful_theme: theme,
    quality_linter_ok: false,
    quality_linter_failures: [],
    first_reply_source: 'template',
    reply_template_version: FIRST_REPLY_VERSION,
    reply_omitted_reason: '',
  };

  if (isTest) {
    return {
      ...base,
      first_reply_mode: 'test_suppressed',
      first_reply_ready: false,
      first_reply_omitted_reason: 'probable_test',
      first_reply_source: 'test_omitted',
      reply_omitted_reason: 'probable_test',
      first_reply_reason_codes: ['omit_probable_test'],
      quality_linter_ok: true,
    };
  }

  if (!hasContact) {
    return {
      ...base,
      first_reply_mode: 'contact_suppressed',
      first_reply_ready: false,
      first_reply_omitted_reason: 'missing_contact',
      first_reply_source: 'none',
      reply_omitted_reason: 'missing_contact',
      first_reply_reason_codes: ['omit_missing_contact'],
      first_reply_warnings: ['contact_requires_manager_check'],
      quality_linter_ok: true,
    };
  }

  const draft = composeHumanDraft(ctx);
  const { allowedQuestions, suppressedCodes } = applyKnownInformationGuard(ctx, draft.questions);
  const qLimited = allowedQuestions.slice(0, FIRST_REPLY_MAX_QUESTION_GROUPS);
  const lines = [
    draft.greeting,
    '',
    ...draft.ack,
    ...formatQuestions(qLimited, draft.leadIn),
    ...closingBlock(),
  ];
  let text = trimToSafeLength(lines.join('\n'));

  const lint = lintFirstReply(text, ctx, { theme: draft.theme, requireText: true });
  warnings.push(...lint.warnings);

  if (!lint.ok) {
    return {
      ...base,
      first_reply_mode: 'lint_blocked',
      first_reply_text: '',
      first_reply_questions: qLimited.map((q) => q.text),
      first_reply_reason_codes: [...new Set([...suppressedCodes, ...lint.failures.map((f) => `lint:${f}`)])],
      first_reply_omitted_reason: 'quality_linter_failed',
      reply_omitted_reason: 'quality_linter_failed',
      first_reply_ready: false,
      first_reply_warnings: warnings,
      meaningful_theme: draft.theme,
      quality_linter_ok: false,
      quality_linter_failures: lint.failures,
    };
  }

  return {
    ...base,
    first_reply_mode: 'normal',
    first_reply_text: text,
    first_reply_questions: qLimited.map((q) => q.text),
    first_reply_reason_codes: [...new Set(suppressedCodes)],
    first_reply_omitted_reason: '',
    first_reply_ready: true,
    first_reply_warnings: warnings,
    meaningful_theme: draft.theme,
    quality_linter_ok: true,
    quality_linter_failures: [],
    first_reply_source: 'template',
    reply_template_version: FIRST_REPLY_VERSION,
    reply_omitted_reason: '',
  };
}

export function buildFirstReplyDraftV2(ctx) {
  const r = generateFirstReplyV2(ctx);
  return {
    first_reply_text: r.first_reply_text,
    first_reply_source: r.first_reply_source,
    reply_omitted_reason: r.reply_omitted_reason || r.first_reply_omitted_reason,
    first_reply_version: r.first_reply_version,
    human_reply_style_version: r.human_reply_style_version,
    first_reply_mode: r.first_reply_mode,
    first_reply_subject: r.first_reply_subject,
    first_reply_questions: r.first_reply_questions,
    first_reply_reason_codes: r.first_reply_reason_codes,
    first_reply_omitted_reason: r.first_reply_omitted_reason,
    first_reply_ready: r.first_reply_ready,
    first_reply_warnings: r.first_reply_warnings,
    meaningful_theme: r.meaningful_theme,
    quality_linter_ok: r.quality_linter_ok,
    quality_linter_failures: r.quality_linter_failures,
    reply_template_version: r.reply_template_version,
  };
}
