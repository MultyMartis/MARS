/**
 * Corvonero MIG R1 — Playwright mobile Yandex SERP capture (Novosibirsk lr=65).
 * Reuses Triumph capture-serp-multi.mjs mechanics; reads serp_r1_index.json.
 */
import { readFileSync, writeFileSync, mkdirSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";
import { createRequire } from "module";

const __dirname = dirname(fileURLToPath(import.meta.url));
const SESSION_ROOT = join(__dirname, "..");
const LR = "65";
const CAPTURE_ROOT = join(SESSION_ROOT, "evidence/serp/r1-corv01/captures");

const PLAYWRIGHT_ROOT =
  "C:/AI MARS/incoming/mig/pilots/triumph-gruzotaxi-krasnodar/evidence/serp-multi-20260604/node_modules/playwright";
const require = createRequire(import.meta.url);
const { chromium, devices } = require(PLAYWRIGHT_ROOT);

const index = JSON.parse(readFileSync(join(SESSION_ROOT, "serp_r1_index.json"), "utf8"));
const QUERIES = index.queries;

function categorizeItems(items) {
  const ads = items.filter((i) => i.surface_type === "ad");
  const organic = items.filter((i) => i.surface_type === "organic");
  const maps = items.filter((i) => i.surface_type === "local_pack");
  const vacancy = organic.filter((i) =>
    /hh\.ru|superjob|rabota|ваканс/i.test(i.url + i.title)
  );
  const informational = organic.filter((i) =>
    /forum|wiki|help|инструк|blog|youtube|habr/i.test(i.url + i.title)
  );
  const commercial = organic.filter(
    (i) =>
      !vacancy.includes(i) &&
      !informational.includes(i) &&
      /\.ru|\.com|\.рф/i.test(i.url)
  );
  const aggregators = organic.filter((i) =>
    /yandex\.ru\/maps|2gis|zoon|flamp|yell/i.test(i.url)
  );
  return { ads, organic, maps, vacancy, informational, commercial, aggregators };
}

async function captureOne(page, queryRecord, outDir) {
  const query = queryRecord.query;
  const searchUrl = `https://yandex.ru/search/touch/?text=${encodeURIComponent(query)}&lr=${LR}`;

  await page.goto(searchUrl, { waitUntil: "domcontentloaded", timeout: 90000 });
  await page.waitForTimeout(4500);

  const title = await page.title();
  const url = page.url();

  await page.screenshot({
    path: join(outDir, "serp-full-page.png"),
    fullPage: true,
  });

  const extracted = await page.evaluate(() => {
    const items = [];
    const pushItem = (el, surfaceType) => {
      const link =
        el.closest("a") ||
        el.querySelector("a[href]") ||
        (el.tagName === "A" ? el : null);
      if (!link) return;
      const href = link.href || "";
      if (!href || href.startsWith("javascript:")) return;
      if (href.includes("yandex.ru/search") && !href.includes("yabs.")) return;

      let titleText = "";
      const titleEl =
        el.querySelector(".OrganicTitle-LinkText") ||
        el.querySelector(".OrganicTitle") ||
        el.querySelector(".Link") ||
        el.querySelector("h2") ||
        el.querySelector('[role="heading"]') ||
        link;
      titleText = (titleEl?.innerText || link.innerText || "").trim().split("\n")[0];

      const pathEl =
        el.querySelector(".Path") ||
        el.querySelector(".organic__path") ||
        el.querySelector(".Organic-Path") ||
        el.querySelector(".Organic-Subtitle");
      const pathText = (pathEl?.innerText || "").trim();
      if (!titleText || titleText.length < 3) return;

      const key = `${surfaceType}|${href}|${titleText.slice(0, 80)}`;
      if (items.some((i) => i.key === key)) return;
      items.push({ key, title: titleText, url: href, path_text: pathText, surface_type: surfaceType });
    };

    document.querySelectorAll(".AdvItem, .serp-adv, [data-log-node*='adv']").forEach((el) =>
      pushItem(el, "ad")
    );
    document
      .querySelectorAll(".Organic, .serp-item, li.serp-item, .VanillaReact")
      .forEach((el) => {
        if (el.closest(".AdvItem, .serp-adv")) return;
        const inMaps =
          el.closest(".Companies") ||
          el.closest(".MiniOrg") ||
          el.closest("[class*='Map']") ||
          el.closest(".RelatedPlaces");
        pushItem(el, inMaps ? "local_pack" : "organic");
      });
    document
      .querySelectorAll(".Companies .MiniOrg, .RelatedPlaces .MiniOrg, .OrgSnippet")
      .forEach((el) => pushItem(el, "local_pack"));

    const bodyText = document.body?.innerText || "";
    const hasCaptcha = /не робот|not a robot|captcha|Подтвердите/i.test(
      bodyText + " " + document.title
    );
    return { hasCaptcha, bodyPreview: bodyText.slice(0, 2500), items };
  });

  const html = await page.content();
  writeFileSync(join(outDir, "serp.html"), html, "utf8");

  const cats = categorizeItems(extracted.items);
  const gradeB =
    !extracted.hasCaptcha && extracted.items.length > 0;

  const serpJson = {
    schema_version: "1",
    query_id: queryRecord.r1_id,
    query,
    timestamp: new Date().toISOString(),
    region: "Новосибирск",
    region_lr: Number(LR),
    device: "mobile",
    viewport: "iPhone 13 (Playwright)",
    search_url: searchUrl,
    final_url: url,
    page_title: title,
    captcha_status: extracted.hasCaptcha ? "blocked" : "none",
    visible_ads: cats.ads.map(({ title: t, url: u, path_text }) => ({ title: t, url: u, path_text })),
    organic_results: cats.organic.map(({ title: t, url: u, path_text }) => ({ title: t, url: u, path_text })),
    maps: cats.maps.map(({ title: t, url: u }) => ({ title: t, url: u })),
    aggregators: cats.aggregators.map(({ title: t, url: u }) => ({ title: t, url: u })),
    vacancy_results: cats.vacancy.map(({ title: t, url: u }) => ({ title: t, url: u })),
    informational_results: cats.informational.map(({ title: t, url: u }) => ({ title: t, url: u })),
    commercial_pages: cats.commercial.slice(0, 15).map(({ title: t, url: u, path_text }) => ({
      title: t,
      url: u,
      path_text,
    })),
    screenshot_reference: "serp-full-page.png",
    html_reference: "serp.html",
    evidence_grade: gradeB ? "B" : "C",
    acquisition_method: "playwright_mobile_yandex",
    limitations: extracted.hasCaptcha
      ? ["CAPTCHA on final screen — no bypass attempted"]
      : extracted.items.length === 0
        ? ["Zero extracted SERP items — parser or empty page"]
        : [],
    extracted_count: extracted.items.length,
  };

  writeFileSync(join(outDir, "serp.json"), JSON.stringify(serpJson, null, 2), "utf8");
  return serpJson;
}

async function main() {
  const onlyId = process.argv[2] || null;
  const toRun = onlyId ? QUERIES.filter((q) => q.r1_id === onlyId) : QUERIES;
  if (!toRun.length) {
    console.error("No queries");
    process.exit(1);
  }

  mkdirSync(CAPTURE_ROOT, { recursive: true });
  const delayMs = Number(process.env.CAPTURE_DELAY_MS || "50000");
  const headless = process.env.CAPTURE_HEADLESS !== "false";
  const summary = [];

  const browser = await chromium.launch({ headless });
  const context = await browser.newContext({
    ...devices["iPhone 13"],
    locale: "ru-RU",
    timezoneId: "Asia/Novosibirsk",
    hasTouch: true,
  });

  for (let i = 0; i < toRun.length; i++) {
    const q = toRun[i];
    const outDir = join(CAPTURE_ROOT, q.r1_id);
    mkdirSync(outDir, { recursive: true });
    console.log(`Capturing ${q.r1_id}: ${q.query}`);

    const page = await context.newPage();
    let result;
    try {
      result = await captureOne(page, q, outDir);
    } catch (err) {
      result = {
        query_id: q.r1_id,
        captcha_status: "error",
        evidence_grade: "C",
        error: String(err),
        extracted_count: 0,
      };
      writeFileSync(join(outDir, "serp.json"), JSON.stringify(result, null, 2), "utf8");
    } finally {
      await page.close();
    }

    summary.push({
      r1_id: q.r1_id,
      ok: result.evidence_grade === "B",
      grade: result.evidence_grade,
      captcha: result.captcha_status,
      extracted_count: result.extracted_count ?? 0,
    });

    if (i < toRun.length - 1) {
      console.log(`Waiting ${delayMs}ms…`);
      await new Promise((r) => setTimeout(r, delayMs));
    }
  }

  await context.close();
  await browser.close();

  writeFileSync(
    join(SESSION_ROOT, "evidence/serp/r1-corv01/capture-run-summary.json"),
    JSON.stringify({ captured_at: new Date().toISOString(), results: summary }, null, 2),
    "utf8"
  );
  console.log(JSON.stringify(summary, null, 2));
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
