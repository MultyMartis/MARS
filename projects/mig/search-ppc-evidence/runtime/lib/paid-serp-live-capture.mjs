/**
 * MIG Search PPC — bounded live Yandex Paid SERP capture (Wave 2.1)
 * Isolated technical adapter — not Corvonero production tooling.
 */
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';
import { nowIso, writeJson } from './utils.mjs';
import { parsePaidSerpCapture } from './paid-serp-runtime.mjs';
import { captureLandingEvidence } from './landing-evidence.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../../..');

const PLAYWRIGHT_CANDIDATES = [
  path.join(REPO_ROOT, 'incoming/mig/pilots/triumph-gruzotaxi-krasnodar/evidence/serp-multi-20260604/node_modules/playwright'),
  'playwright',
];

function resolvePlaywright() {
  for (const candidate of PLAYWRIGHT_CANDIDATES) {
    try {
      const require = createRequire(import.meta.url);
      if (candidate === 'playwright') return require('playwright');
      return require(candidate);
    } catch {
      /* try next */
    }
  }
  throw new Error('Playwright runtime not available — install or set PLAYWRIGHT_MODULE_PATH');
}

function delayMs(base = 45000, jitter = 5000) {
  if (jitter <= 0) return base;
  return base + Math.floor(Math.random() * jitter);
}

function categorizeItems(items) {
  const ads = items.filter((i) => i.surface_type === 'ad');
  const organic = items.filter((i) => i.surface_type === 'organic');
  return { ads, organic };
}

export async function captureLiveQuery(page, { queryRecord, regionLr, timezone, device, headful }) {
  const query = queryRecord.text;
  const searchUrl = `https://yandex.ru/search/?text=${encodeURIComponent(query)}&lr=${regionLr}`;

  await page.goto(searchUrl, { waitUntil: 'domcontentloaded', timeout: 90000 });
  await page.waitForTimeout(4500);

  const title = await page.title();
  const finalUrl = page.url();

  const extracted = await page.evaluate(() => {
    const items = [];
    const pushItem = (el, surfaceType) => {
      const link = el.closest('a') || el.querySelector('a[href]') || (el.tagName === 'A' ? el : null);
      if (!link) return;
      const href = link.href || '';
      if (!href || href.startsWith('javascript:')) return;
      if (href.includes('yandex.ru/search') && !href.includes('yabs.')) return;

      const titleEl =
        el.querySelector('.OrganicTitle-LinkText') ||
        el.querySelector('.OrganicTitle') ||
        el.querySelector('.Link') ||
        el.querySelector('h2') ||
        link;
      const titleText = (titleEl?.innerText || link.innerText || '').trim().split('\n')[0];
      const pathEl =
        el.querySelector('.Path') ||
        el.querySelector('.organic__path') ||
        el.querySelector('.Organic-Path') ||
        el.querySelector('.Organic-Subtitle');
      const pathText = (pathEl?.innerText || '').trim();
      if (!titleText || titleText.length < 3) return;

      const key = `${surfaceType}|${href}|${titleText.slice(0, 80)}`;
      if (items.some((i) => i.key === key)) return;
      items.push({ key, title: titleText, url: href, path_text: pathText, surface_type: surfaceType });
    };

    document.querySelectorAll('.AdvItem, .serp-adv, [data-log-node*="adv"], .serp-item_type_ad').forEach((el) =>
      pushItem(el, 'ad'),
    );
    document.querySelectorAll('.Organic, .serp-item, li.serp-item, .VanillaReact').forEach((el) => {
      if (el.closest('.AdvItem, .serp-adv, .serp-item_type_ad')) return;
      pushItem(el, 'organic');
    });

    const bodyText = document.body?.innerText || '';
    const hasCaptcha = /не робот|not a robot|captcha|Подтвердите|SmartCaptcha/i.test(bodyText + ' ' + document.title);
    return { hasCaptcha, bodyPreview: bodyText.slice(0, 2500), items };
  });

  const cats = categorizeItems(extracted.items);
  const ts = nowIso();
  const captchaStatus = extracted.hasCaptcha ? 'blocked' : 'none';

  return {
    schema_version: '1.0.0',
    query_id: queryRecord.query_id,
    query,
    timestamp: ts,
    timezone,
    region: queryRecord.region || 'Москва',
    region_lr: Number(regionLr),
    device,
    browser_mode: headful ? 'headful' : 'headless',
    search_url: searchUrl,
    final_url: finalUrl,
    page_title: title,
    captcha_status: captchaStatus,
    visible_ads: cats.ads.map(({ title: t, url: u, path_text }) => ({ title: t, url: u, path_text })),
    organic_results: cats.organic.map(({ title: t, url: u, path_text }) => ({ title: t, url: u, path_text })),
    extracted_count: extracted.items.length,
    acquisition_method: 'mig_wave21_live_paid_serp_adapter',
    limitations: extracted.hasCaptcha
      ? ['CAPTCHA detected — STOP_ON_CAPTCHA; no bypass attempted']
      : extracted.items.length === 0
        ? ['Zero extracted SERP items — parser or empty page']
        : [],
    _page: page,
    _extracted: extracted,
  };
}

async function openBrowserContext(pw, sessionConfig, headful) {
  const { chromium } = pw;
  const profile = sessionConfig.browser_profile || {};
  const launchOpts = {
    headless: !headful,
    slowMo: headful ? 50 : 0,
    channel: profile.channel || undefined,
  };

  if (profile.persistent_user_data_dir) {
    fs.mkdirSync(profile.persistent_user_data_dir, { recursive: true });
    const context = await chromium.launchPersistentContext(profile.persistent_user_data_dir, {
      ...launchOpts,
      locale: 'ru-RU',
      timezoneId: sessionConfig.timezone,
      viewport: sessionConfig.device_profile?.viewport || { width: 1280, height: 800 },
      userAgent: sessionConfig.device_profile?.user_agent || undefined,
    });
    return { browser: context, context, page: context.pages()[0] || (await context.newPage()), persistent: true };
  }

  const browser = await chromium.launch(launchOpts);
  const context = await browser.newContext({
    locale: 'ru-RU',
    timezoneId: sessionConfig.timezone,
    viewport: sessionConfig.device_profile?.viewport || { width: 1280, height: 800 },
    userAgent: sessionConfig.device_profile?.user_agent || undefined,
  });
  const page = await context.newPage();
  return { browser, context, page, persistent: false };
}

async function warmNavigateIfConfigured(page, sessionConfig, runLog) {
  const warm = sessionConfig.warm_navigation;
  if (!warm?.enabled) return;
  const url = warm.url || 'https://yandex.ru/';
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
  const waitMs = warm.wait_ms || 3000;
  await page.waitForTimeout(waitMs);
  runLog.push({ at: nowIso(), event: 'warm_navigation', url, wait_ms: waitMs });
}

export async function runLivePaidSerpSession({
  sessionConfig,
  querySet,
  receipt,
  playwrightModule,
}) {
  const pw = playwrightModule || resolvePlaywright();

  const outputPath = sessionConfig.output_path;
  fs.mkdirSync(outputPath, { recursive: true });

  const sessionId = sessionConfig.session_id || `live-paid-serp-${Date.now()}`;
  const headful = sessionConfig.capture_policy?.headful !== false;
  const stopOnCaptcha = sessionConfig.captcha_policy === 'STOP_ON_CAPTCHA';
  const pacingMs = sessionConfig.pause_policy?.between_queries_ms || 45000;
  const pacingJitter = sessionConfig.pause_policy?.jitter_ms || 5000;
  const maxQueries = sessionConfig.query_limit || querySet.queries.length;

  const queries = querySet.queries.slice(0, maxQueries);
  const runLog = [];
  const results = [];
  let stoppedOnCaptcha = false;
  let unprocessed = [];

  for (let i = 0; i < queries.length; i += 1) {
    const q = queries[i];
    const queryDir = path.join(outputPath, 'captures', q.query_id);
    fs.mkdirSync(queryDir, { recursive: true });

    const { browser, context, page, persistent } = await openBrowserContext(pw, sessionConfig, headful);

    let serpJson;
    try {
      await warmNavigateIfConfigured(page, sessionConfig, runLog);
      serpJson = await captureLiveQuery(page, {
        queryRecord: q,
        regionLr: sessionConfig.region_lr,
        timezone: sessionConfig.timezone,
        device: sessionConfig.device_profile?.label || 'desktop',
        headful,
      });

      await serpJson._page.screenshot({ path: path.join(queryDir, 'serp-full-page.png'), fullPage: true });
      const html = await serpJson._page.content();
      fs.writeFileSync(path.join(queryDir, 'serp.html'), html, 'utf8');
      delete serpJson._page;
      delete serpJson._extracted;

      serpJson.screenshot_reference = 'serp-full-page.png';
      serpJson.html_reference = 'serp.html';
      writeJson(path.join(queryDir, 'serp.json'), serpJson);

      const parsed = parsePaidSerpCapture(serpJson, {
        sessionId,
        projectId: sessionConfig.project_id,
        queryId: q.query_id,
      });
      writeJson(path.join(queryDir, 'observation.json'), parsed);

      const landingEvidence = [];
      for (const ad of (parsed.ads || []).slice(0, 2)) {
        if (!ad.destination_url) continue;
        landingEvidence.push(
          captureLandingEvidence({
            destinationUrl: ad.destination_url,
            pageData: { final_url: ad.destination_url, page_title: null },
            evidenceLinks: {},
          }),
        );
      }
      if (landingEvidence.length) writeJson(path.join(queryDir, 'landing-evidence.json'), landingEvidence);

      results.push({
        query_id: q.query_id,
        query: q.text,
        observation_state: parsed.observation_state,
        ads_count: parsed.ads?.length || 0,
        organic_count: parsed.organic_results?.length || 0,
        captcha: serpJson.captcha_status,
        capture_dir: queryDir,
        degraded: parsed.degraded,
      });
      runLog.push({ at: nowIso(), event: 'query_complete', query_id: q.query_id, state: parsed.observation_state });

      if (serpJson.captcha_status === 'blocked' && stopOnCaptcha) {
        stoppedOnCaptcha = true;
        unprocessed = queries.slice(i + 1).map((x) => x.query_id);
        runLog.push({ at: nowIso(), event: 'stop_on_captcha', query_id: q.query_id });
        if (!persistent) {
          await page.close();
          await context.close();
          await browser.close();
        } else {
          await context.close();
        }
        break;
      }
    } catch (err) {
      const fail = {
        query_id: q.query_id,
        query: q.text,
        observation_state: 'PAGE LOAD FAILURE',
        error: String(err.message || err),
        capture_dir: queryDir,
        degraded: true,
      };
      writeJson(path.join(queryDir, 'error.json'), fail);
      results.push(fail);
      runLog.push({ at: nowIso(), event: 'query_error', query_id: q.query_id, error: String(err.message || err) });
    } finally {
      try {
        if (persistent) await context.close();
        else {
          await page.close();
          await context.close();
          await browser.close();
        }
      } catch {
        /* ignore */
      }
    }

    if (i < queries.length - 1 && !stoppedOnCaptcha) {
      const wait = delayMs(pacingMs, pacingJitter);
      runLog.push({ at: nowIso(), event: 'pacing_wait', ms: wait });
      await new Promise((r) => setTimeout(r, wait));
    }
  }

  const collectionStatus = stoppedOnCaptcha
    ? 'COLLECTION DEGRADED'
    : results.every((r) => !r.degraded && r.observation_state !== 'PAGE LOAD FAILURE')
      ? 'COMPLETE'
      : results.some((r) => r.observation_state && r.observation_state !== 'PAGE LOAD FAILURE')
        ? 'COLLECTION DEGRADED'
        : 'FAILED';

  const summary = {
    schema_version: '1.0.0',
    session_id: sessionId,
    mode: 'PAID SERP — BUSINESS HOURS',
    evidence_class: 'TECHNICAL LIVE EVIDENCE',
    production_authority: false,
    project_id: sessionConfig.project_id,
    generated_at: nowIso(),
    query_count: results.length,
    queries_requested: queries.length,
    queries_unprocessed: unprocessed,
    ads_observed: results.filter((r) => r.observation_state === 'ADS OBSERVED').length,
    no_ads_observed: results.filter((r) => r.observation_state === 'NO ADS OBSERVED').length,
    captcha_or_interrupted: results.filter((r) =>
      ['CAPTCHA', 'SESSION STOPPED', 'PAGE LOAD FAILURE'].includes(r.observation_state),
    ).length,
    collection_status: collectionStatus,
    stopped_on_captcha: stoppedOnCaptcha,
    results,
    run_log: runLog,
    execution_receipt_id: receipt?.receipt_id || null,
  };

  writeJson(path.join(outputPath, 'session-summary.json'), summary);
  return { ok: collectionStatus !== 'FAILED', summary, session_path: path.join(outputPath, 'session-summary.json') };
}
