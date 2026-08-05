/**
 * First Reply Engine v2 — deterministic, context-aware, manager-ready drafts.
 * AI OFF. Never auto-sends to customers. Uses Lead Semantic Model v1 fields.
 * Version: sm-reply-v2.0
 */

export const FIRST_REPLY_VERSION = 'sm-reply-v2.0';
export const FIRST_REPLY_MAX_CHARS = 900;
export const FIRST_REPLY_TARGET_MAX = 700;
export const FIRST_REPLY_MAX_QUESTION_GROUPS = 3;

const PLACEHOLDER_NAMES = new Set([
  'name', 'имя', 'ваше имя', 'фио', 'test', 'тест', 'testing',
  'asdf', 'qwerty', 'xxx', 'n/a', 'na', 'none', 'null', 'undefined',
  '-', '—', '.', '..', '...',
]);

const PROMISE_PATTERNS = [
  /гарантир/i,
  /в\s+топ[-\s]?1/i,
  /100\s*%/i,
  /обязательно\s+попад[её]те/i,
  /запустим\s+за\s+\d+/i,
  /точн(ая|ые)\s+стоимость/i,
  /бесплатно\s+выведем/i,
];

/**
 * Usable client name for greeting (safe, non-placeholder).
 * Probable-test names like "test" are intentionally NOT used for customer drafts
 * because the whole reply is suppressed; this helper still classifies them.
 */
export function isUsableClientName(raw) {
  const name = String(raw || '').trim();
  if (!name) return false;
  if (name.length < 2) return false;
  if (/^[\d\s\-_.@]+$/.test(name)) return false;
  if (/^[^a-zA-Zа-яА-ЯёЁ]+$/.test(name)) return false;
  if (PLACEHOLDER_NAMES.has(name.toLowerCase())) return false;
  // Form garbage / spreadsheet formulas
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
  return String(v || '')
    .split(/[;,\n]/)
    .map((s) => s.trim())
    .filter(Boolean);
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
  if (/^(seo|audit|аудит|директ|сайт|хочу сайт)\.?$/i.test(c)) return true;
  if (resolvedService === 'Audit' && c.length < 20) return true;
  if (resolvedService === 'SEO' && (c.length < 12 || /^seo\.?$/i.test(c))) return true;
  return !hasMeaningfulComment(c);
}

/**
 * Known-information guard — suppress questions for data already present.
 * Returns { allowedQuestions, suppressedCodes }.
 */
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
    } else if (/что\s+вам\s+требуется/i.test(text) && hasMeaningfulComment(comment)) {
      suppress = 'suppress_ask_generic_task_known';
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

function formatQuestions(questions) {
  if (!questions.length) return [];
  if (questions.length === 1) {
    return ['', questions[0].text];
  }
  const lines = ['', 'Уточните, пожалуйста:'];
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
  // Prefer cutting before closing if possible
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

function assertNoUnsupportedPromises(text, warnings) {
  for (const re of PROMISE_PATTERNS) {
    if (re.test(text)) warnings.push('unsupported_promise_detected');
  }
}

/**
 * Service-specific candidate question sets (pre-guard).
 */
function candidateQuestionsFor(ctx) {
  const {
    resolved_service: service,
    website_state: siteState,
    comment_normalized: comment,
    secondary_service: secondary,
  } = ctx;
  const vague = isVagueTask(comment, service);
  const meaningful = hasMeaningfulComment(comment);
  const qs = [];

  if (service === 'Audit') {
    if (siteState === 'provided') {
      if (vague) {
        qs.push({ id: 'audit_focus', text: 'Что для вас сейчас важнее всего проверить: техническое состояние, видимость в поиске, трафик, конверсию или конкретную проблему на сайте?' });
      } else {
        qs.push({ id: 'audit_detail', text: 'Есть ли приоритетные страницы или разделы, на которых стоит сфокусировать аудит?' });
        if (!/регион|город/i.test(comment)) {
          qs.push({ id: 'audit_goal', text: 'Какой результат аудита для вас главный?' });
        }
      }
    } else if (siteState === 'explicitly_absent' || siteState === 'missing' || siteState === 'invalid_or_placeholder') {
      qs.push({ id: 'audit_site_exists', text: 'Сайт уже существует, или его ещё только предстоит создать?' });
      qs.push({ id: 'audit_goal_alt', text: 'Если сайт есть — пришлите, пожалуйста, его адрес и кратко опишите, что хотите проверить.' });
    }
    return qs;
  }

  if (service === 'SEO') {
    if (siteState === 'provided') {
      if (vague) {
        qs.push({ id: 'seo_region', text: 'По какому региону нужно продвижение?' });
        qs.push({ id: 'seo_priority', text: 'Какие услуги или товары сейчас в приоритете?' });
      } else {
        if (!/регион|город|москв|спб/i.test(comment)) {
          qs.push({ id: 'seo_region', text: 'По какому региону нужно продвижение?' });
        }
        qs.push({ id: 'seo_history', text: 'Продвижение уже велось раньше, или начинаем с нуля?' });
        qs.push({ id: 'seo_goal', text: 'Какая главная цель: заявки, трафик или видимость?' });
      }
    } else if (siteState === 'explicitly_absent') {
      qs.push({ id: 'seo_or_dev', text: 'Нужно сначала создать сайт, а затем заняться SEO, или сайт уже есть под другим адресом?' });
    } else {
      qs.push({ id: 'seo_site', text: 'Подтвердите, пожалуйста, адрес сайта для SEO.' });
      qs.push({ id: 'seo_region', text: 'По какому региону нужно продвижение?' });
    }
    return qs;
  }

  if (service === 'WebsiteDevelopment') {
    qs.push({ id: 'dev_business', text: 'Чем занимается бизнес и какая основная аудитория?' });
    qs.push({ id: 'dev_features', text: 'Какой тип сайта и какие функции нужны в первую очередь?' });
    qs.push({ id: 'dev_examples', text: 'Есть ли примеры сайтов, которые вам нравятся?' });
    return qs;
  }

  if (service === 'WebsiteDevelopmentSEO' || (service === 'WebsiteDevelopment' && secondary === 'SEO')) {
    qs.push({ id: 'combo_business', text: 'Чем занимается бизнес и какие услуги/товары нужно представить на сайте?' });
    qs.push({ id: 'combo_features', text: 'Какие функции сайта обязательны на старте?' });
    qs.push({ id: 'combo_region', text: 'По какому региону планируете продвижение после запуска?' });
    return qs;
  }

  if (service === 'AISearch') {
    if (siteState === 'provided') {
      qs.push({ id: 'ai_audience', text: 'Какие регионы или аудитории для вас приоритетны?' });
      qs.push({ id: 'ai_focus', text: 'Что важнее сейчас: видимость в AI-ответах, классический поиск или оба направления?' });
    } else {
      qs.push({ id: 'ai_what', text: 'Какой бизнес или сайт нужно продвигать в AI-поиске?' });
      qs.push({ id: 'ai_audience', text: 'Какие регионы или аудитории приоритетны?' });
    }
    return qs;
  }

  if (service === 'Direct') {
    if (siteState === 'provided') {
      qs.push({ id: 'ppc_products', text: 'Какие услуги или товары нужно рекламировать?' });
      qs.push({ id: 'ppc_region', text: 'По какому региону запускать рекламу?' });
      qs.push({ id: 'ppc_history', text: 'Кампании уже были, или запускаем впервые?' });
    } else {
      qs.push({ id: 'ppc_site', text: 'Есть ли сайт или посадочная страница для рекламы?' });
      qs.push({ id: 'ppc_products', text: 'Какие услуги или товары нужно рекламировать?' });
      qs.push({ id: 'ppc_region', text: 'По какому региону запускать рекламу?' });
    }
    return qs;
  }

  if (service === 'NeedsClarification' || service === 'Other') {
    if (ctx.alternative_contact_type || ctx.communication_preference === 'telegram') {
      qs.push({ id: 'nc_task', text: 'Какая задача для вас сейчас главная: аудит, SEO, разработка сайта или реклама?' });
    } else if (meaningful) {
      qs.push({ id: 'nc_confirm', text: 'Верно ли мы понимаем задачу? Если нужно — уточните один главный приоритет.' });
    } else {
      qs.push({ id: 'nc_task', text: 'Кратко напишите, какая задача для вас сейчас главная.' });
    }
    return qs;
  }

  qs.push({ id: 'generic_task', text: 'Кратко опишите, какая задача для вас сейчас главная.' });
  return qs;
}

function acknowledgeLines(ctx) {
  const service = String(ctx.resolved_service || '');
  const siteState = String(ctx.website_state || '');
  const site = String(ctx.website_normalized || '').trim();
  const comment = String(ctx.comment_normalized || '').trim();
  const altType = String(ctx.alternative_contact_type || '').toLowerCase();
  const lines = [];

  if (service === 'Audit') {
    if (siteState === 'provided' && site) {
      lines.push(`Спасибо за заявку на аудит сайта ${site}.`);
      if (hasMeaningfulComment(comment) && !isVagueTask(comment, service)) {
        lines.push('Мы учли ваш комментарий и уточним детали, чтобы сфокусировать проверку.');
      }
    } else {
      lines.push('Спасибо за обращение по аудиту.');
      lines.push('Для аудита обычно нужен адрес существующего сайта — без него полноценную проверку начать нельзя.');
    }
    return lines;
  }

  if (service === 'SEO') {
    if (siteState === 'provided' && site) {
      lines.push(`Спасибо за заявку по SEO для сайта ${site}.`);
      lines.push('Адрес сайта уже указан — повторно присылать его не нужно.');
      if (/^seo\.?$/i.test(comment) || isVagueTask(comment, service)) {
        lines.push('Поняли, что интересует продвижение в поиске.');
      } else if (hasMeaningfulComment(comment)) {
        lines.push('Мы учли ваш комментарий и подготовим уточняющие вопросы по задаче.');
      }
    } else if (siteState === 'explicitly_absent') {
      lines.push('Спасибо за интерес к SEO.');
      lines.push('Вы указали, что сайта сейчас нет — уточним, нужен ли сначала новый сайт.');
    } else {
      lines.push('Спасибо за интерес к SEO.');
    }
    return lines;
  }

  if (service === 'WebsiteDevelopment') {
    lines.push('Спасибо за обращение.');
    lines.push('Поняли, что вам требуется новый сайт.');
    if (siteState === 'explicitly_absent') {
      lines.push('Текущий сайт не указан — это ожидаемо для задачи на разработку.');
    }
    return lines;
  }

  if (service === 'WebsiteDevelopmentSEO') {
    lines.push('Спасибо за обращение.');
    lines.push('Поняли задачу: сначала создать сайт, подготовить его к продвижению, а затем начать SEO.');
    if (siteState === 'explicitly_absent') {
      lines.push('Текущий сайт отсутствует — адрес существующего сайта не нужен.');
    }
    return lines;
  }

  if (service === 'AISearch') {
    lines.push('Спасибо за интерес к видимости в AI-ответах и современном поиске.');
    if (siteState === 'provided' && site) {
      lines.push(`Сайт ${site} уже указан.`);
    }
    lines.push('Мы не обещаем автоматическое появление в ответах нейросетей — обсудим реалистичный план.');
    return lines;
  }

  if (service === 'Direct') {
    lines.push('Спасибо за интерес к контекстной рекламе.');
    if (siteState === 'provided' && site) {
      lines.push(`Сайт ${site} уже указан — повторно присылать адрес не нужно.`);
    }
    return lines;
  }

  if (altType === 'telegram' || ctx.communication_preference === 'telegram') {
    lines.push('Спасибо, заявка получена.');
    lines.push('Учли, что вам удобнее общаться в Telegram.');
    return lines;
  }

  if (hasMeaningfulComment(comment)) {
    lines.push('Спасибо, ваша заявка получена.');
    lines.push('Мы учли ваш комментарий и уточним один главный приоритет.');
    return lines;
  }

  lines.push('Спасибо, ваша заявка получена.');
  return lines;
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

/**
 * Generate First Reply v2 draft from Lead Semantic Model fields.
 */
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

  const base = {
    first_reply_version: FIRST_REPLY_VERSION,
    first_reply_mode: 'normal',
    first_reply_subject: subjectFor(ctx),
    first_reply_text: '',
    first_reply_questions: [],
    first_reply_reason_codes: [],
    first_reply_omitted_reason: '',
    first_reply_ready: false,
    first_reply_warnings: [],
    // Compat with sm-reply-v1 / processor
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
    };
  }

  const greeting = buildGreeting(ctx.client_name || ctx.client_name_normalized);
  const ack = acknowledgeLines(ctx);
  const candidates = candidateQuestionsFor(ctx);
  const { allowedQuestions, suppressedCodes } = applyKnownInformationGuard(ctx, candidates);

  // Extra hard strip: never ask for known site URL
  const siteState = String(ctx.website_state || '');
  if (siteState === 'provided' || siteState === 'explicitly_absent') {
    for (let i = allowedQuestions.length - 1; i >= 0; i -= 1) {
      if (/адрес\s+сайт|пришлите.*сайт|url/i.test(allowedQuestions[i].text) && siteState === 'provided') {
        suppressedCodes.push('suppress_ask_website_provided');
        allowedQuestions.splice(i, 1);
      }
      if (/адрес\s+существующ|пришлите.*сайт/i.test(allowedQuestions[i]?.text || '') && siteState === 'explicitly_absent') {
        // Keep "does site exist" for Audit missing-site, but not "send current URL" for development
        if (ctx.resolved_service === 'WebsiteDevelopment' || ctx.resolved_service === 'WebsiteDevelopmentSEO') {
          suppressedCodes.push('suppress_ask_website_absent');
          allowedQuestions.splice(i, 1);
        }
      }
    }
  }

  const qLimited = allowedQuestions.slice(0, FIRST_REPLY_MAX_QUESTION_GROUPS);
  const lines = [greeting, '', ...ack, ...formatQuestions(qLimited), ...closingBlock()];
  let text = trimToSafeLength(lines.join('\n'));

  // Safety scrub residual known-info asks
  if (siteState === 'provided' || siteState === 'explicitly_absent') {
    text = text
      .replace(/Пришлите,?\s*пожалуйста,?\s*адрес сайта[^.]*\./gi, '')
      .replace(/Укажите адрес сайта[^.]*\./gi, '')
      .replace(/повторно присылать адрес не нужно\.[^\n]*пришлите[^\n]*сайт[^\n]*/gi, (m) => m.split('.')[0] + '.')
      .replace(/\n{3,}/g, '\n\n')
      .trim();
  }

  assertNoUnsupportedPromises(text, warnings);

  if (text.length > FIRST_REPLY_TARGET_MAX) {
    warnings.push('reply_longer_than_target');
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
    first_reply_source: 'template',
    reply_template_version: FIRST_REPLY_VERSION,
    reply_omitted_reason: '',
  };
}

/** Compatibility wrapper used by parse-lead-lib / processor. */
export function buildFirstReplyDraftV2(ctx) {
  const r = generateFirstReplyV2(ctx);
  return {
    first_reply_text: r.first_reply_text,
    first_reply_source: r.first_reply_source,
    reply_omitted_reason: r.reply_omitted_reason || r.first_reply_omitted_reason,
    first_reply_version: r.first_reply_version,
    first_reply_mode: r.first_reply_mode,
    first_reply_subject: r.first_reply_subject,
    first_reply_questions: r.first_reply_questions,
    first_reply_reason_codes: r.first_reply_reason_codes,
    first_reply_omitted_reason: r.first_reply_omitted_reason,
    first_reply_ready: r.first_reply_ready,
    first_reply_warnings: r.first_reply_warnings,
    reply_template_version: r.reply_template_version,
  };
}
