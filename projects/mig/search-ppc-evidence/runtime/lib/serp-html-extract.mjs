/**
 * Extract SERP items from saved HTML (assisted capture import).
 * Mirrors in-page extraction logic from paid-serp-live-capture.mjs.
 */
export function extractSerpItemsFromHtml(html) {
  const items = [];
  const bodyText = stripTags(html).slice(0, 8000);
  const hasCaptcha = /не робот|not a robot|captcha|Подтвердите|SmartCaptcha|showcaptcha/i.test(bodyText + html);

  const adBlocks = [
    ...matchBlocks(html, /class="[^"]*(?:AdvItem|serp-adv|serp-item_type_ad)[^"]*"/gi),
  ];
  for (const block of adBlocks) {
    const item = parseBlock(block, 'ad');
    if (item) items.push(item);
  }

  const organicBlocks = matchBlocks(html, /class="[^"]*(?:Organic|serp-item)[^"]*"/gi);
  for (const block of organicBlocks) {
    if (/AdvItem|serp-adv|serp-item_type_ad/i.test(block)) continue;
    const item = parseBlock(block, 'organic');
    if (item) items.push(item);
  }

  const yabsLinks = [...html.matchAll(/href="(https?:\/\/yabs\.yandex[^"]+)"/gi)];
  for (const m of yabsLinks) {
    const href = m[1];
    const key = `ad|${href}`;
    if (items.some((i) => i.key === key)) continue;
    const context = html.slice(Math.max(0, m.index - 400), m.index + 400);
    const title = extractTitleFromContext(context) || 'yabs-ad';
    items.push({ key, title, url: href, path_text: '', surface_type: 'ad' });
  }

  return { hasCaptcha, items, bodyPreview: bodyText.slice(0, 2500) };
}

function matchBlocks(html, pattern) {
  const blocks = [];
  let match;
  const re = new RegExp(pattern.source, pattern.flags);
  while ((match = re.exec(html)) !== null) {
    const start = Math.max(0, match.index - 50);
    const end = Math.min(html.length, match.index + 2500);
    blocks.push(html.slice(start, end));
  }
  return blocks;
}

function parseBlock(block, surfaceType) {
  const hrefMatch = block.match(/href="(https?:\/\/[^"]+)"/i);
  if (!hrefMatch) return null;
  const href = hrefMatch[1];
  if (href.startsWith('javascript:')) return null;
  if (href.includes('yandex.ru/search') && !href.includes('yabs.')) return null;

  const title =
    extractBetween(block, 'OrganicTitle-LinkText', 'class') ||
    extractBetween(block, 'OrganicTitle', 'class') ||
    stripTags(block).split('\n').map((s) => s.trim()).find((s) => s.length > 5) ||
    '';
  if (!title || title.length < 3) return null;

  const pathText = extractPathText(block);
  const key = `${surfaceType}|${href}|${title.slice(0, 80)}`;
  return { key, title: title.slice(0, 300), url: href, path_text: pathText, surface_type: surfaceType };
}

function extractTitleFromContext(context) {
  const t = stripTags(context).split('\n').map((s) => s.trim()).filter((s) => s.length > 8);
  return t[0] || null;
}

function extractPathText(block) {
  const path = block.match(/class="[^"]*Path[^"]*"[^>]*>([^<]+)/i);
  return path ? path[1].trim() : '';
}

function extractBetween(html, classHint) {
  const idx = html.indexOf(classHint);
  if (idx < 0) return null;
  const slice = html.slice(idx, idx + 800);
  const text = stripTags(slice).trim();
  return text.split('\n')[0]?.trim() || null;
}

function stripTags(html) {
  return String(html)
    .replace(/<script[\s\S]*?<\/script>/gi, ' ')
    .replace(/<style[\s\S]*?<\/style>/gi, ' ')
    .replace(/<[^>]+>/g, '\n')
    .replace(/\s+/g, ' ');
}

export function buildSerpJsonFromAssistedBundle(bundle, extracted, queryRecord) {
  const ads = extracted.items.filter((i) => i.surface_type === 'ad');
  const organic = extracted.items.filter((i) => i.surface_type === 'organic');

  return {
    schema_version: '1.0.0',
    query_id: bundle.query_id,
    query: bundle.query,
    timestamp: bundle.captured_at,
    timezone: bundle.timezone,
    region: bundle.region,
    region_lr: bundle.region_lr || queryRecord?.region_lr,
    device: bundle.device_browser || 'desktop',
    browser_mode: 'operator-assisted',
    search_url: bundle.page_url,
    final_url: bundle.page_url,
    page_title: bundle.page_title || null,
    captcha_status: extracted.hasCaptcha ? 'blocked' : 'none',
    visible_ads: ads.map(({ title, url, path_text }) => ({ title, url, path_text })),
    organic_results: organic.map(({ title, url, path_text }) => ({ title, url, path_text })),
    extracted_count: extracted.items.length,
    acquisition_method: 'operator_assisted_live_serp_capture',
    acquisition_mode: 'OPERATOR-ASSISTED LIVE SERP CAPTURE',
    limitations: extracted.hasCaptcha
      ? ['CAPTCHA page in assisted capture — no ads parsed']
      : extracted.items.length === 0
        ? ['Zero extracted SERP items from assisted HTML']
        : [],
  };
}
