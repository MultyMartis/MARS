/**
 * One-shot Yandex mobile SERP capture for MIG Pilot #1.
 * Operator-supervised evidence collection — not MIG runtime.
 */
import { chromium, devices } from "playwright";
import { writeFileSync, mkdirSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const QUERY = "грузотакси краснодар";
const LR = "35"; // Krasnodar krai / city region code on Yandex
const OUT_DIR = __dirname;

async function main() {
  mkdirSync(OUT_DIR, { recursive: true });

  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    ...devices["iPhone 13"],
    locale: "ru-RU",
    timezoneId: "Europe/Moscow",
    userAgent:
      "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
  });

  const page = await context.newPage();
  const searchUrl = `https://yandex.ru/search/touch/?text=${encodeURIComponent(QUERY)}&lr=${LR}`;

  await page.goto(searchUrl, { waitUntil: "networkidle", timeout: 60000 });
  await page.waitForTimeout(4000);

  const title = await page.title();
  const url = page.url();

  await page.screenshot({
    path: join(OUT_DIR, "serp-full-viewport.png"),
    fullPage: false,
  });

  await page.screenshot({
    path: join(OUT_DIR, "serp-full-page.png"),
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

      if (!titleText || titleText.length < 3) return;

      const key = `${surfaceType}|${href}|${titleText.slice(0, 80)}`;
      if (items.some((i) => i.key === key)) return;
      items.push({ key, title: titleText, url: href, surface_type: surfaceType });
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
      bodyPreview: bodyText.slice(0, 2000),
      items,
      htmlLength: document.documentElement.outerHTML.length,
    };
  });

  const rawDump = {
    captured_at: new Date().toISOString(),
    query: QUERY,
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

  writeFileSync(join(OUT_DIR, "capture-raw.json"), JSON.stringify(rawDump, null, 2), "utf8");

  const html = await page.content();
  writeFileSync(join(OUT_DIR, "serp-page.html"), html, "utf8");

  await browser.close();
  console.log(JSON.stringify({ ok: true, ...rawDump }, null, 2));
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
