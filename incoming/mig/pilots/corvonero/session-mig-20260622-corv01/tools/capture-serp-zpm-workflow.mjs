/**
 * Corvonero R1 — ZPM-workflow-labelled SERP capture.
 * Mechanics recovered from Triumph capture-serp-multi.mjs (verified Grade B evidence).
 * Fresh browser per query; conservative pacing; no CAPTCHA bypass.
 */
import { readFileSync, writeFileSync, mkdirSync, appendFileSync, existsSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";
import { createRequire } from "module";

const __dirname = dirname(fileURLToPath(import.meta.url));
const SESSION_ROOT = join(__dirname, "..");
const LR = "65";
const CAPTURE_ROOT = join(
  SESSION_ROOT,
  "evidence/serp/zpm-workflow-corv01/capture-run/captures"
);
const RUN_ROOT = join(SESSION_ROOT, "evidence/serp/zpm-workflow-corv01/capture-run");
const LOG_PATH = join(RUN_ROOT, "execution-log.md");

const PLAYWRIGHT_ROOT =
  "C:/AI MARS/incoming/mig/pilots/triumph-gruzotaxi-krasnodar/evidence/serp-multi-20260604/node_modules/playwright";
const require = createRequire(import.meta.url);
const { chromium, devices } = require(PLAYWRIGHT_ROOT);

const VALIDATION_BATCH = [
  { r1_id: "r1q01", query: "программист 1С Новосибирск" },
  { r1_id: "r1q05", query: "интеграция 1С с сайтом Новосибирск" },
  { r1_id: "r1q07", query: "маркировка в 1С Новосибирск" },
];

const REMAINING_BATCH = [
  { r1_id: "r1q02", query: "сопровождение 1С Новосибирск" },
  { r1_id: "r1q03", query: "доработка 1С Новосибирск" },
  { r1_id: "r1q04", query: "доработка отчёта 1С Новосибирск" },
  { r1_id: "r1q06", query: "интеграция 1С Битрикс Новосибирск" },
  { r1_id: "r1q08", query: "Честный знак 1С Новосибирск" },
  { r1_id: "r1q09", query: "настройка ТС ПИОТ" },
  { r1_id: "r1q10", query: "программа 1С не работает Новосибирск" },
];

const ALL_QUERIES = Object.fromEntries(
  [...VALIDATION_BATCH, ...REMAINING_BATCH].map((q) => [q.r1_id, q])
);

function existingGradeB(r1_id) {
  const serpPath = join(CAPTURE_ROOT, r1_id, "serp.json");
  if (!existsSync(serpPath)) return false;
  try {
    const j = JSON.parse(readFileSync(serpPath, "utf8"));
    return j.evidence_grade === "B";
  } catch {
    return false;
  }
}

function resolveBatchQueries(ids) {
  const queries = [];
  for (const id of ids) {
    const q = ALL_QUERIES[id];
    if (!q) {
      console.error(`Unknown query id: ${id}`);
      process.exit(1);
    }
    if (process.env.SKIP_EXISTING_GRADE_B === "1" && existingGradeB(id)) {
      logLine(`SKIP ${id}: existing Grade B preserved`);
      continue;
    }
    queries.push(q);
  }
  return queries;
}

function logLine(text) {
  const line = `- ${new Date().toISOString()} — ${text}\n`;
  appendFileSync(LOG_PATH, line, "utf8");
  console.log(text);
}

function delayMs() {
  const base = Number(process.env.CAPTURE_DELAY_MS || "55000");
  const jitter = Number(process.env.CAPTURE_DELAY_JITTER_MS || "5000");
  if (jitter <= 0) return base;
  return base + Math.floor(Math.random() * jitter);
}

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

async function captureOne(page, queryRecord, outDir, opts) {
  const query = queryRecord.query;
  const searchUrl = `https://yandex.ru/search/touch/?text=${encodeURIComponent(query)}&lr=${LR}`;

  if (opts.warmup) {
    await page.goto("https://yandex.ru/", {
      waitUntil: "domcontentloaded",
      timeout: 90000,
    });
    await page.waitForTimeout(2500);
  }

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
  const gradeB = !extracted.hasCaptcha && extracted.items.length > 0;

  const serpJson = {
    schema_version: "1",
    query_id: queryRecord.r1_id,
    query,
    timestamp: new Date().toISOString(),
    region: "Новосибирск",
    region_lr: Number(LR),
    device: "mobile",
    viewport: "iPhone 13 (Playwright)",
    browser_mode: opts.headless ? "headless" : "headful",
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
    acquisition_method: "playwright_mobile_yandex_zpm_workflow_derived",
    workflow_ref: "triumph capture-serp-multi.mjs",
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

async function runQuery(queryRecord, opts, summary) {
  const outDir = join(CAPTURE_ROOT, queryRecord.r1_id);
  mkdirSync(outDir, { recursive: true });
  logLine(`START ${queryRecord.r1_id}: ${queryRecord.query}`);

  const headless = process.env.CAPTURE_HEADLESS !== "false";
  let result;

  const browser = await chromium.launch({ headless, slowMo: headless ? 0 : 50 });
  const context = await browser.newContext({
    ...devices["iPhone 13"],
    locale: "ru-RU",
    timezoneId: "Asia/Novosibirsk",
    hasTouch: true,
  });
  const page = await context.newPage();

  try {
    result = await captureOne(page, queryRecord, outDir, {
      headless,
      warmup: opts.warmup,
    });
  } catch (err) {
    result = {
      query_id: queryRecord.r1_id,
      captcha_status: "error",
      evidence_grade: "C",
      error: String(err),
      extracted_count: 0,
    };
    writeFileSync(join(outDir, "serp.json"), JSON.stringify(result, null, 2), "utf8");
    logLine(`ERROR ${queryRecord.r1_id}: ${err.message || err}`);
  } finally {
    await page.close();
    await context.close();
    await browser.close();
  }

  const row = {
    r1_id: queryRecord.r1_id,
    query: queryRecord.query,
    ok: result.evidence_grade === "B",
    grade: result.evidence_grade,
    captcha: result.captcha_status,
    extracted_count: result.extracted_count ?? 0,
    page_title: result.page_title ?? null,
  };
  summary.push(row);
  logLine(
    `DONE ${queryRecord.r1_id}: grade=${row.grade} captcha=${row.captcha} items=${row.extracted_count}`
  );
  return row;
}

async function runBatch(queries, opts, summary) {
  for (let i = 0; i < queries.length; i++) {
    const row = await runQuery(queries[i], { warmup: i === 0 && opts.warmup }, summary);
    if (row.captcha === "blocked" && process.env.STOP_ON_CAPTCHA === "1") {
      logLine(`STOP_ON_CAPTCHA after ${queries[i].r1_id}`);
      return { stopped: true, after: queries[i].r1_id };
    }
    if (i < queries.length - 1) {
      const wait = delayMs();
      logLine(`Waiting ${wait}ms before next query`);
      await new Promise((r) => setTimeout(r, wait));
    }
  }
  return { stopped: false };
}

async function main() {
  const mode = process.argv[2] || "validation";
  mkdirSync(CAPTURE_ROOT, { recursive: true });
  mkdirSync(RUN_ROOT, { recursive: true });

  if (!existsSync(LOG_PATH)) {
    writeFileSync(
      LOG_PATH,
      `# ZPM-workflow Corvonero SERP execution log\n\n**Session:** mig-20260622-corv01\n\n`,
      "utf8"
    );
  }

  logLine(`MODE ${mode} headless=${process.env.CAPTURE_HEADLESS !== "false"}`);

  const summary = [];
  let meta = { validation_complete: false, remaining_run: false, stopped_on_captcha: false };

  if (mode === "validation" || mode === "all") {
    const stop = await runBatch(VALIDATION_BATCH, { warmup: true }, summary);
    meta.validation_complete = true;
    if (stop.stopped) {
      meta.stopped_on_captcha = true;
      meta.stopped_after = stop.after;
    } else if (mode === "all") {
      const allOk = summary.every((r) => r.ok);
      if (allOk) {
        await new Promise((r) => setTimeout(r, delayMs()));
        const stop2 = await runBatch(REMAINING_BATCH, { warmup: false }, summary);
        meta.remaining_run = true;
        if (stop2.stopped) {
          meta.stopped_on_captcha = true;
          meta.stopped_after = stop2.after;
        }
      } else {
        meta.remaining_skipped = "validation_not_all_grade_b";
      }
    }
  } else if (mode === "remaining") {
    const stop = await runBatch(REMAINING_BATCH, { warmup: true }, summary);
    meta.remaining_run = true;
    if (stop.stopped) {
      meta.stopped_on_captcha = true;
      meta.stopped_after = stop.after;
    }
  } else if (mode === "batch") {
    const batchLabel = process.argv[3] || "batch";
    const ids = process.argv.slice(4);
    if (ids.length === 0) {
      console.error("Usage: node capture-serp-zpm-workflow.mjs batch <label> r1q02 r1q03 ...");
      process.exit(1);
    }
    const queries = resolveBatchQueries(ids);
    meta.batch_label = batchLabel;
    meta.batch_ids = ids;
    if (queries.length === 0) {
      logLine(`Batch ${batchLabel}: all queries skipped (Grade B preserved)`);
    } else {
      const stop = await runBatch(queries, { warmup: true }, summary);
      if (stop.stopped) {
        meta.stopped_on_captcha = true;
        meta.stopped_after = stop.after;
      }
    }
  } else {
    console.error(
      "Usage: node capture-serp-zpm-workflow.mjs [validation|remaining|all|batch <label> <ids...>]"
    );
    process.exit(1);
  }

  const batchPayload = {
    captured_at: new Date().toISOString(),
    workflow_label: "zpm-workflow-corv01",
    source_script: "tools/capture-serp-zpm-workflow.mjs",
    triumph_ref:
      "incoming/mig/pilots/triumph-gruzotaxi-krasnodar/evidence/serp-multi-20260604/capture-serp-multi.mjs",
    mode,
    browser_mode: process.env.CAPTURE_HEADLESS !== "false" ? "headless" : "headful",
    delay_ms_base: Number(process.env.CAPTURE_DELAY_MS || "55000"),
    delay_ms_jitter: Number(process.env.CAPTURE_DELAY_JITTER_MS || "5000"),
    region_lr: LR,
    meta,
    results: summary,
    grade_b_count: summary.filter((r) => r.grade === "B").length,
    grade_c_count: summary.filter((r) => r.grade === "C").length,
  };

  if (process.env.MERGE_SUMMARY === "1") {
    const summaryPath = join(RUN_ROOT, "capture-run-summary.json");
    let merged = batchPayload;
    if (existsSync(summaryPath)) {
      try {
        const prev = JSON.parse(readFileSync(summaryPath, "utf8"));
        const byId = new Map((prev.results || []).map((r) => [r.r1_id, r]));
        for (const row of summary) byId.set(row.r1_id, row);
        const allResults = [...byId.values()];
        merged = {
          ...prev,
          ...batchPayload,
          captured_at: batchPayload.captured_at,
          meta: { ...(prev.meta || {}), ...meta },
          results: allResults,
          grade_b_count: allResults.filter((r) => r.grade === "B").length,
          grade_c_count: allResults.filter((r) => r.grade === "C").length,
        };
      } catch {
        merged = batchPayload;
      }
    }
    writeFileSync(summaryPath, JSON.stringify(merged, null, 2), "utf8");
    console.log(JSON.stringify(merged, null, 2));
  } else {
    writeFileSync(
      join(RUN_ROOT, "capture-run-summary.json"),
      JSON.stringify(batchPayload, null, 2),
      "utf8"
    );
    console.log(JSON.stringify(batchPayload, null, 2));
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
