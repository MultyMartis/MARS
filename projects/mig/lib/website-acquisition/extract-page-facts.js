"use strict";

const { loadRules, extractDomain } = require("./build-url-plan");

function decodeEntities(text) {
  return text
    .replace(/&nbsp;/gi, " ")
    .replace(/&amp;/gi, "&")
    .replace(/&lt;/gi, "<")
    .replace(/&gt;/gi, ">")
    .replace(/&quot;/gi, '"')
    .replace(/&#39;/gi, "'");
}

function stripTags(html) {
  return decodeEntities(html.replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim());
}

function matchAll(regex, text) {
  const results = [];
  const flags = regex.global ? regex : new RegExp(regex.source, regex.flags.includes("g") ? regex.flags : `${regex.flags}g`);
  let match = flags.exec(text);
  while (match) {
    results.push(match);
    match = flags.exec(text);
  }
  return results;
}

function uniqueStrings(values, limit) {
  const seen = new Set();
  const out = [];
  for (const value of values) {
    const normalized = value.replace(/\s+/g, " ").trim();
    if (!normalized || seen.has(normalized.toLowerCase())) {
      continue;
    }
    seen.add(normalized.toLowerCase());
    out.push(normalized);
    if (limit && out.length >= limit) {
      break;
    }
  }
  return out;
}

function extractTitle(html) {
  const match = html.match(/<title[^>]*>([\s\S]*?)<\/title>/i);
  return match ? stripTags(match[1]) : null;
}

function extractMetaDescription(html) {
  const match = html.match(
    /<meta[^>]+name=["']description["'][^>]+content=["']([^"']*)["'][^>]*>/i
  ) || html.match(
    /<meta[^>]+content=["']([^"']*)["'][^>]+name=["']description["'][^>]*>/i
  );
  return match ? decodeEntities(match[1].trim()) : null;
}

function extractLang(html) {
  const match = html.match(/<html[^>]+lang=["']([^"']+)["']/i);
  return match ? match[1].trim() : null;
}

function extractCanonical(html, baseUrl) {
  const match = html.match(/<link[^>]+rel=["']canonical["'][^>]+href=["']([^"']+)["']/i);
  if (!match) {
    return null;
  }
  try {
    return new URL(match[1], baseUrl).href;
  } catch {
    return match[1];
  }
}

function extractHeadings(html, cap = 50) {
  const headings = [];
  const regex = /<h([1-3])[^>]*>([\s\S]*?)<\/h\1>/gi;
  let match = regex.exec(html);
  let order = 0;
  while (match && headings.length < cap) {
    const text = stripTags(match[2]);
    if (text) {
      headings.push({
        level: Number(match[1]),
        text,
        order,
      });
      order += 1;
    }
    match = regex.exec(html);
  }
  return headings;
}

function extractPhones(html) {
  const phones = [];
  const telMatches = matchAll(/href=["']tel:([^"']+)["']/gi, html);
  for (const m of telMatches) {
    phones.push(m[1].trim());
  }
  const textMatches = matchAll(
    /(?:\+7|8)[\s(-]*\d{3}[\s)-]*\d{3}[\s-]*\d{2}[\s-]*\d{2}/g,
    stripTags(html)
  );
  for (const m of textMatches) {
    phones.push(m[0].trim());
  }
  return uniqueStrings(phones, 20);
}

function extractEmails(html) {
  const emails = [];
  const mailtoMatches = matchAll(/href=["']mailto:([^"'?]+)["']/gi, html);
  for (const m of mailtoMatches) {
    emails.push(m[1].trim());
  }
  const textMatches = matchAll(
    /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/g,
    stripTags(html)
  );
  for (const m of textMatches) {
    emails.push(m[0].trim());
  }
  return uniqueStrings(emails, 20);
}

function extractMessengers(html) {
  const messengers = [];
  const patterns = [
    { type: "telegram", regex: /https?:\/\/t\.me\/([a-zA-Z0-9_]+)/gi },
    { type: "whatsapp", regex: /https?:\/\/wa\.me\/(\d+)/gi },
    { type: "viber", regex: /viber:\/\/chat\?number=(%2B?\d+)/gi },
  ];
  for (const { type, regex } of patterns) {
    const matches = matchAll(regex, html);
    for (const m of matches) {
      messengers.push({ type, handle: m[1] });
    }
  }
  return messengers;
}

function extractAddresses(html) {
  const addresses = [];
  const addressBlocks = matchAll(/<address[^>]*>([\s\S]*?)<\/address>/gi, html);
  for (const m of addressBlocks) {
    const text = stripTags(m[1]);
    if (text) {
      addresses.push(text);
    }
  }
  return uniqueStrings(addresses, 10);
}

function extractOffers(headings) {
  return headings
    .filter((h) => h.level <= 2)
    .map((h) => ({ text: h.text, context: `h${h.level}` }));
}

function extractPricingSignals(html, rules) {
  const text = stripTags(html);
  const lines = text.split(/(?<=[.!?])\s+/);
  const patterns = (rules.pricing_patterns || []).map((p) => new RegExp(p, "i"));
  const signals = [];

  for (const line of lines) {
    if (!line || line.length > 240) {
      continue;
    }
    if (patterns.some((re) => re.test(line))) {
      let currencyHint = null;
      if (/₽|руб/i.test(line)) {
        currencyHint = "RUB";
      } else if (/\$/.test(line)) {
        currencyHint = "USD";
      } else if (/€/.test(line)) {
        currencyHint = "EUR";
      }
      signals.push({ text: line.trim(), currency_hint: currencyHint, context: null });
    }
  }
  return signals.slice(0, 30);
}

function extractCtaElements(html, baseUrl, rules) {
  const ctas = [];
  const patterns = (rules.cta_button_patterns || []).map((p) => new RegExp(p, "i"));

  const anchorRegex = /<a[^>]+href=["']([^"']+)["'][^>]*>([\s\S]*?)<\/a>/gi;
  let match = anchorRegex.exec(html);
  while (match) {
    const text = stripTags(match[2]);
    if (text && patterns.some((re) => re.test(text))) {
      let href = match[1];
      try {
        href = new URL(href, baseUrl).href;
      } catch {
        /* keep raw */
      }
      ctas.push({ text, href, element_type: "link", position_hint: "unknown" });
    }
    match = anchorRegex.exec(html);
  }

  const buttonRegex = /<button[^>]*>([\s\S]*?)<\/button>/gi;
  match = buttonRegex.exec(html);
  while (match) {
    const text = stripTags(match[1]);
    if (text && patterns.some((re) => re.test(text))) {
      ctas.push({ text, href: null, element_type: "button", position_hint: "unknown" });
    }
    match = buttonRegex.exec(html);
  }

  return ctas.slice(0, 40);
}

function extractForms(html) {
  const forms = [];
  const formRegex = /<form\b([^>]*)>([\s\S]*?)<\/form>/gi;
  let match = formRegex.exec(html);
  while (match) {
    const attrs = match[1];
    const body = match[2];
    const idMatch = attrs.match(/\bid=["']([^"']+)["']/i);
    const actionMatch = attrs.match(/\baction=["']([^"']*)["']/i);
    const methodMatch = attrs.match(/\bmethod=["']([^"']*)["']/i);

    const fields = [];
    const inputRegex = /<(?:input|textarea|select)\b([^>]*)\/?>/gi;
    let inputMatch = inputRegex.exec(body);
    while (inputMatch) {
      const inputAttrs = inputMatch[1];
      const nameMatch = inputAttrs.match(/\bname=["']([^"']+)["']/i);
      const typeMatch = inputAttrs.match(/\btype=["']([^"']+)["']/i);
      const placeholderMatch = inputAttrs.match(/\bplaceholder=["']([^"']+)["']/i);
      const required = /\brequired\b/i.test(inputAttrs);
      const labelMatch = body.match(
        new RegExp(`<label[^>]*for=["']${nameMatch ? nameMatch[1] : "____"}["'][^>]*>([\\s\\S]*?)<\\/label>`, "i")
      );
      fields.push({
        name: nameMatch ? nameMatch[1] : null,
        type: typeMatch ? typeMatch[1] : "text",
        label: labelMatch ? stripTags(labelMatch[1]) : placeholderMatch ? placeholderMatch[1] : null,
        required,
      });
      inputMatch = inputRegex.exec(body);
    }

    forms.push({
      form_id: idMatch ? idMatch[1] : null,
      action: actionMatch ? actionMatch[1] : null,
      method: methodMatch ? methodMatch[1].toLowerCase() : "get",
      fields,
      visible_purpose: null,
    });
    match = formRegex.exec(html);
  }
  return forms;
}

function extractLinks(html, baseUrl, cap = 200) {
  const internal = [];
  const external = [];
  const baseDomain = extractDomain(baseUrl);
  const seen = new Set();

  const anchorRegex = /<a[^>]+href=["']([^"']+)["'][^>]*>([\s\S]*?)<\/a>/gi;
  let match = anchorRegex.exec(html);
  while (match && internal.length + external.length < cap * 2) {
    const hrefRaw = match[1].trim();
    if (!hrefRaw || hrefRaw.startsWith("#") || hrefRaw.startsWith("javascript:")) {
      match = anchorRegex.exec(html);
      continue;
    }
    let href;
    try {
      href = new URL(hrefRaw, baseUrl).href;
    } catch {
      match = anchorRegex.exec(html);
      continue;
    }
    if (seen.has(href)) {
      match = anchorRegex.exec(html);
      continue;
    }
    seen.add(href);
    const text = stripTags(match[2]) || href;
    const linkDomain = extractDomain(href);
    const item = { href, text };
    if (linkDomain && baseDomain && linkDomain === baseDomain) {
      if (internal.length < cap) {
        internal.push(item);
      }
    } else if (external.length < cap) {
      external.push(item);
    }
    match = anchorRegex.exec(html);
  }

  return { internal, external };
}

function extractTrustSignals(html, rules) {
  const text = stripTags(html);
  const patterns = rules.trust_phrase_patterns || [];
  const signals = [];
  const lines = text.split(/\s{2,}|\n/).map((l) => l.trim()).filter(Boolean);

  for (const line of lines) {
    if (line.length > 200) {
      continue;
    }
    const lower = line.toLowerCase();
    if (patterns.some((phrase) => lower.includes(phrase.toLowerCase()))) {
      signals.push({ text: line, context: null });
    }
  }
  return signals.slice(0, 30);
}

function detectRenderStatus(html) {
  const stripped = stripTags(html);
  const bodyMatch = html.match(/<body[^>]*>([\s\S]*?)<\/body>/i);
  const body = bodyMatch ? bodyMatch[1] : html;

  if (
    /<div[^>]+id=["'](root|app|__next)["']/i.test(body) &&
    stripped.length < 400
  ) {
    return "js_shell";
  }
  if (!stripped || stripped.length < 80) {
    return "static_empty";
  }
  return "static_ok";
}

function emptyContacts() {
  return { phones: [], emails: [], addresses: [], messengers: [] };
}

/**
 * Extract observable page facts from HTML (deterministic, no AI).
 */
function extractPageFacts(html, baseUrl, options = {}) {
  const MAX_HTML_CHARS = options.max_html_chars ?? 350000;
  if (html && html.length > MAX_HTML_CHARS) {
    html = html.slice(0, MAX_HTML_CHARS);
  }
  const rules = options.rules || loadRules(options.rulesPath);
  const renderStatus = detectRenderStatus(html);
  const headings = extractHeadings(html, rules.heading_cap || 50);

  if (renderStatus === "js_shell") {
    return {
      title: extractTitle(html),
      meta_description: extractMetaDescription(html),
      canonical_url: extractCanonical(html, baseUrl),
      lang: extractLang(html),
      headings,
      contacts: emptyContacts(),
      offers: [],
      pricing_signals: [],
      cta_elements: [],
      forms: [],
      links: { internal: [], external: [] },
      trust_signals_visible: [],
      visible_text_excerpt: stripTags(html).slice(0, 500) || null,
      render_status: renderStatus,
      acquisition_status: "render_required",
    };
  }

  const contacts = {
    phones: extractPhones(html),
    emails: extractEmails(html),
    addresses: extractAddresses(html),
    messengers: extractMessengers(html),
  };

  return {
    title: extractTitle(html),
    meta_description: extractMetaDescription(html),
    canonical_url: extractCanonical(html, baseUrl),
    lang: extractLang(html),
    headings,
    contacts,
    offers: extractOffers(headings),
    pricing_signals: extractPricingSignals(html, rules),
    cta_elements: extractCtaElements(html, baseUrl, rules),
    forms: extractForms(html),
    links: extractLinks(html, baseUrl, rules.links_cap_per_kind || 200),
    trust_signals_visible: extractTrustSignals(html, rules),
    visible_text_excerpt: stripTags(html).slice(0, 500) || null,
    render_status: renderStatus,
    acquisition_status: renderStatus === "static_empty" ? "empty" : "success",
  };
}

module.exports = {
  extractPageFacts,
  detectRenderStatus,
  stripTags,
  extractLinks,
};
