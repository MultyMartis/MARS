/**
 * Multi-query Yandex mobile SERP capture — MIG Multi-Query Groundtruth.
 * One evidence package per query_id under ./captures/<query_id>/
 */
import { chromium, devices } from "playwright";
import { readFileSync, writeFileSync, mkdirSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const LR = "35";
const QUERY_SET_PATH = join(
  __dirname,
  "..",
  "..",
  "multi-query-market-query-set-v1.json"
);

const querySet = JSON.parse(readFileSync(QUERY_SET_PATH, "utf8"));
const QUERIES = querySet.approved_query_set;

function searchQueryText(declared) {
  return declared
    .replace(/Краснодар/g, "краснодар")
    .replace(/Краснодару/g, "краснодару");
}

async function captureOne(page, queryRecord, outDir) {
  const queryDeclared = queryRecord.query_text;
  const query = searchQueryText(queryDeclared);
  const searchUrl = `https://yandex.ru/search/touch/?text=${encodeURIComponent(query)}&lr=${LR}`;

  await page.goto(searchUrl, { waitUntil: "domcontentloaded", timeout: 90000 });
  await page.waitForTimeout(4500);

  const title = await page.title();
  const url = page.url();

  await page.screenshot({
    path: join(outDir, "serp-full-viewport.png"),
    fullPage: false,
  });
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
      items.push({
        key,
        title: titleText,
        url: href,
        path_text: pathText,
        surface_type: surfaceType,
      });
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
    const hasCaptcha = /не робот|not a robot|captcha/i.test(bodyText + " " + document.title);

    return {
      hasCaptcha,
      bodyPreview: bodyText.slice(0, 2500),
      items,
      htmlLength: document.documentElement.outerHTML.length,
    };
  });

  const rawDump = {
    captured_at: new Date().toISOString(),
    query_id: queryRecord.query_id,
    query_text: queryRecord.query_text,
    query_text_search: query,
    query_role: queryRecord.role,
    search_url: searchUrl,
    final_url: url,
    page_title: title,
    device: "iPhone 13 emulation (Playwright)",
    region_lr: LR,
    has_captcha: extracted.hasCaptcha,
    extracted_count: extracted.items.length,
    items: extracted.items,
    body_preview: extracted.bodyPreview,
  };

  writeFileSync(join(outDir, "capture-raw.json"), JSON.stringify(rawDump, null, 2), "utf8");
  const html = await page.content();
  writeFileSync(join(outDir, "serp-page.html"), html, "utf8");

  return rawDump;
}

async function main() {
  const onlyId = process.argv[2] || null;
  const toRun = onlyId
    ? QUERIES.filter((q) => q.query_id === onlyId)
    : QUERIES;

  if (!toRun.length) {
    console.error("No queries to run");
    process.exit(1);
  }

  mkdirSync(join(__dirname, "captures"), { recursive: true });

  const summary = [];
  const delayMs = Number(process.env.CAPTURE_DELAY_MS || "55000");
  const maxAttempts = Number(process.env.CAPTURE_MAX_ATTEMPTS || "4");

  for (const q of toRun) {
    const outDir = join(__dirname, "captures", q.query_id);
    mkdirSync(outDir, { recursive: true });
    console.log(`Capturing ${q.query_id}: ${q.query_text}`);

    let lastRaw = null;
    let ok = false;

    for (let attempt = 1; attempt <= maxAttempts; attempt++) {
      if (attempt > 1) {
        const wait = delayMs * attempt;
        console.log(`  retry ${attempt}/${maxAttempts} after ${wait}ms`);
        await new Promise((r) => setTimeout(r, wait));
      }

      const browser = await chromium.launch({ headless: true });
      const context = await browser.newContext({
        ...devices["iPhone 13"],
        locale: "ru-RU",
        timezoneId: "Europe/Moscow",
      });
      const page = await context.newPage();
      try {
        lastRaw = await captureOne(page, q, outDir);
        ok = !lastRaw.has_captcha && lastRaw.extracted_count > 0;
        if (ok) break;
      } catch (err) {
        console.error(err);
        lastRaw = { has_captcha: true, extracted_count: 0, error: String(err) };
      } finally {
        await page.close();
        await context.close();
        await browser.close();
      }
    }

    summary.push({
      query_id: q.query_id,
      ok,
      extracted_count: lastRaw?.extracted_count ?? 0,
      has_captcha: lastRaw?.has_captcha ?? true,
    });

    if (toRun.indexOf(q) < toRun.length - 1) {
      console.log(`Waiting ${delayMs}ms before next query…`);
      await new Promise((r) => setTimeout(r, delayMs));
    }
  }
  writeFileSync(
    join(__dirname, "capture-run-summary.json"),
    JSON.stringify({ captured_at: new Date().toISOString(), results: summary }, null, 2),
    "utf8"
  );
  console.log(JSON.stringify(summary, null, 2));
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
