#!/usr/bin/env node
/**
 * Read-only HTTP audit of corvonero.ru and lk.corvonero.ru
 * No form submission, no login. Evidence for Phase 6.1 LP audit.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const PILOT = path.resolve(__dirname, '..');
const AUDIT_TS = new Date().toISOString();

const SEEDS = [
  { site_id: 'corvonero.ru', base: 'https://corvonero.ru' },
  { site_id: 'lk.corvonero.ru', base: 'https://lk.corvonero.ru' },
];

/** Known paths from sitemap / prior probe — read-only fetch only */
const KNOWN_PATHS = {
  'lk.corvonero.ru': ['/', '/products', '/products/nothing', '/personal'],
  'corvonero.ru': ['/'],
};

const MAX_PAGES_PER_SITE = 80;
const FETCH_TIMEOUT_MS = 15000;

function stripTags(html) {
  return html
    .replace(/<script[\s\S]*?<\/script>/gi, ' ')
    .replace(/<style[\s\S]*?<\/style>/gi, ' ')
    .replace(/<[^>]+>/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

function extractMeta(html, name) {
  const re = new RegExp(
    `<meta[^>]+(?:name|property)=["']${name}["'][^>]+content=["']([^"']*)["']`,
    'i'
  );
  const m = html.match(re);
  if (m) return m[1].trim();
  const re2 = new RegExp(
    `<meta[^>]+content=["']([^"']*)["'][^>]+(?:name|property)=["']${name}["']`,
    'i'
  );
  const m2 = html.match(re2);
  return m2 ? m2[1].trim() : null;
}

function extractTitle(html) {
  const m = html.match(/<title[^>]*>([\s\S]*?)<\/title>/i);
  return m ? m[1].replace(/\s+/g, ' ').trim() : null;
}

function extractH1(html) {
  const m = html.match(/<h1[^>]*>([\s\S]*?)<\/h1>/i);
  return m ? stripTags(m[1]).slice(0, 500) : null;
}

function extractLinks(html, baseUrl) {
  const links = new Set();
  const re = /<a[^>]+href=["']([^"'#]+)["']/gi;
  let m;
  while ((m = re.exec(html))) {
    try {
      const u = new URL(m[1], baseUrl);
      if (u.protocol !== 'http:' && u.protocol !== 'https:') continue;
      u.hash = '';
      links.add(u.href.replace(/\/$/, '') || u.href);
    } catch {
      /* skip invalid */
    }
  }
  return [...links];
}

function detectFeatures(text, html) {
  const lower = text.toLowerCase();
  const hasForm = /<form[\s>]/i.test(html);
  const hasTel = /tel:|тел\.|телефон|\+7[\s(]?\d/i.test(text + html);
  const hasEmail = /mailto:|@[a-z0-9.-]+\.[a-z]{2,}/i.test(text + html);
  const hasCallback = /обратн|заявк|консультац|заказать|оставить/i.test(lower);
  const geoNovosibirsk = /новосибирск/i.test(lower);
  const geoRussia = /росси|удалён|удален|remote|online/i.test(lower);
  return {
    contact_form: hasForm,
    phone_visible: hasTel,
    email_visible: hasEmail,
    commercial_cta: hasCallback,
    geography_novosibirsk: geoNovosibirsk,
    geography_russia_wide: geoRussia,
  };
}

function inferServices(text) {
  const lower = text.toLowerCase();
  const services = [];
  const map = [
    ['programmer', /программист|специалист\s+1с|разработчик\s+1с|1с\s+программист/],
    ['support', /сопровожден|абонентск|техподдерж|обслуживан|its|итс/],
    ['modification', /доработк|разработк|конфигурац|внедрен/],
    ['integration', /интеграц|битрикс|bitrix|api|обмен\s+данн/],
    ['marking', /маркировк|честный\s+знак|честный\s+знак|гис\s+мт|пиот|crpt/],
    ['reports', /отч[её]т|обработк|печатн\s+форм/],
    ['troubleshooting', /не\s+работает|ошибк|восстановлен|аварийн/],
  ];
  for (const [id, re] of map) {
    if (re.test(lower)) services.push(id);
  }
  return services;
}

function inferAudience(text) {
  const lower = text.toLowerCase();
  if (/бухгалтер|уч[её]т|бух/i.test(lower)) return 'accounting_and_finance';
  if (/производств|склад|логистик/i.test(lower)) return 'operations';
  if (/розниц|магазин|торговл/i.test(lower)) return 'retail';
  if (/общепит|ресторан|кафе/i.test(lower)) return 'horeca';
  return 'business_general';
}

function inferTrust(text) {
  const lower = text.toLowerCase();
  const evidence = [];
  if (/официальн|партн[её]р|1с:франч|франчиз/i.test(lower)) evidence.push('official_partner_claim');
  if (/опыт|лет\s+на\s+рынке|\d+\s+лет/i.test(lower)) evidence.push('experience_claim');
  if (/клиент|кейс|отзыв/i.test(lower)) evidence.push('clients_or_cases');
  if (/сертифик|аттест/i.test(lower)) evidence.push('certification_claim');
  return evidence;
}

async function fetchPage(url) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), FETCH_TIMEOUT_MS);
  try {
    const res = await fetch(url, {
      signal: controller.signal,
      headers: { 'User-Agent': 'MARS-Corvonero-Phase6.1-ReadOnly-Audit/1.0' },
      redirect: 'follow',
    });
    const html = await res.text();
    return { status: res.status, finalUrl: res.url, html };
  } catch (err) {
    return { status: 0, finalUrl: url, error: String(err.message || err), html: '' };
  } finally {
    clearTimeout(timer);
  }
}

async function crawlSite({ site_id, base }) {
  const baseHost = new URL(base).hostname;
  const queue = [
    base.replace(/\/$/, ''),
    ...(KNOWN_PATHS[site_id] || []).map((p) => new URL(p, base).href.replace(/\/$/, '') || new URL(p, base).href),
  ];
  const seen = new Set();
  const pages = [];

  while (queue.length && pages.length < MAX_PAGES_PER_SITE) {
    const url = queue.shift();
    const norm = url.replace(/\/$/, '') || url;
    if (seen.has(norm)) continue;
    seen.add(norm);

    const { status, finalUrl, html, error } = await fetchPage(norm);
    const text = stripTags(html);
    const features = detectFeatures(text, html);
    const page = {
      site_id,
      url: finalUrl || norm,
      http_status: status,
      access: status >= 200 && status < 400 ? 'OK' : error ? 'ERROR' : 'HTTP_ERROR',
      title: html ? extractTitle(html) : null,
      h1: html ? extractH1(html) : null,
      meta_description: html ? extractMeta(html, 'description') : null,
      visible_proposition: text.slice(0, 400) || null,
      target_audience: text ? inferAudience(text) : null,
      commercial_cta: features.commercial_cta,
      contact_form: features.contact_form,
      phone_visible: features.phone_visible,
      email_visible: features.email_visible,
      services_covered: text ? inferServices(text) : [],
      geography_claims: {
        novosibirsk: features.geography_novosibirsk,
        russia_wide: features.geography_russia_wide,
      },
      trust_evidence: text ? inferTrust(text) : [],
      fetch_error: error || null,
      audited_at: AUDIT_TS,
    };
    pages.push(page);

    if (html && status >= 200 && status < 400) {
      for (const link of extractLinks(html, finalUrl || norm)) {
        try {
          const u = new URL(link);
          if (u.hostname !== baseHost) continue;
          const n = u.href.replace(/\/$/, '') || u.href;
          if (!seen.has(n) && !queue.includes(n)) queue.push(n);
        } catch {
          /* skip */
        }
      }
    }
  }

  return { site_id, base, pages_crawled: pages.length, pages };
}

async function main() {
  const results = [];
  for (const seed of SEEDS) {
    results.push(await crawlSite(seed));
  }

  const inventory = {
    inventory_id: 'corvonero-phase-6.1-website-page-inventory-v1',
    audit_timestamp: AUDIT_TS,
    method: 'read_only_http_crawl',
    sites: results.map((r) => ({
      site_id: r.site_id,
      base_url: r.base,
      pages_crawled: r.pages_crawled,
      pages: r.pages,
    })),
    total_pages: results.reduce((s, r) => s + r.pages_crawled, 0),
  };

  const outPath = path.join(PILOT, 'CORVONERO-PHASE-6.1-WEBSITE-PAGE-INVENTORY-v1.json');
  fs.writeFileSync(outPath, JSON.stringify(inventory, null, 2));
  console.log(`Wrote ${outPath} (${inventory.total_pages} pages)`);
  return inventory;
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
