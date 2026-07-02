import { createServer } from "http";
import { readFileSync, writeFileSync, mkdirSync } from "fs";
import { join } from "path";
import puppeteer from "puppeteer-core";

const v8Root = "X:/AI MARS/workspaces/fp-0002-shpigovsky-v8";
const distDir = join(v8Root, "dist");
const evidenceRoot =
  "X:/AI MARS STORAGE/website-factory/fp-0002-shpigovsky-v8/blog-article-desktop-pass-01";
const runtimeDir = join(evidenceRoot, "runtime");
const PORT = 4321;
const CHROME = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const PAGE = "/blog/nazvanie-stati.html";

mkdirSync(runtimeDir, { recursive: true });

function startServer() {
  return new Promise((resolvePromise) => {
    const server = createServer((req, res) => {
      let rel = decodeURIComponent(req.url.split("?")[0]);
      if (rel === "/") rel = PAGE;
      const filePath = join(distDir, rel.replace(/^\//, "").replace(/\.\./g, ""));
      try {
        const data = readFileSync(filePath);
        const ext = filePath.split(".").pop();
        const types = {
          html: "text/html; charset=utf-8",
          css: "text/css; charset=utf-8",
          js: "application/javascript",
          webp: "image/webp",
          png: "image/png",
          svg: "image/svg+xml",
          woff2: "font/woff2",
          woff: "font/woff",
        };
        res.writeHead(200, { "Content-Type": types[ext] || "application/octet-stream" });
        res.end(data);
      } catch {
        res.writeHead(404);
        res.end("not found");
      }
    });
    server.listen(PORT, "127.0.0.1", () => resolvePromise(server));
  });
}

async function captureRegion(page, selector, name) {
  const el = await page.$(selector);
  if (!el) {
    return { name, ok: false, error: "selector not found" };
  }
  const path = join(runtimeDir, `${name}.png`);
  await el.screenshot({ path });
  return { name, ok: true, path };
}

async function main() {
  const server = await startServer();
  const browser = await puppeteer.launch({
    executablePath: CHROME,
    headless: true,
    args: ["--no-sandbox", "--disable-setuid-sandbox"],
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1437, height: 900, deviceScaleFactor: 1 });
  const url = `http://127.0.0.1:${PORT}${PAGE}`;
  const errors = [];
  page.on("pageerror", (err) => errors.push(String(err)));
  await page.goto(url, { waitUntil: "networkidle0", timeout: 60000 });

  const fullPath = join(runtimeDir, "full-page-1437.png");
  await page.screenshot({ path: fullPath, fullPage: true });

  const checks = await page.evaluate(() => {
    const ids = [...document.querySelectorAll("[id]")].map((el) => el.id);
    const dup = ids.filter((id, i) => ids.indexOf(id) !== i);
    return {
      h1Count: document.querySelectorAll("h1").length,
      h1Text: document.querySelector("h1")?.textContent?.trim() || "",
      dateText: document.querySelector(".blog-article__date")?.textContent?.trim() || "",
      readingTime: document.querySelector(".blog-article__reading-time")?.textContent?.trim() || "",
      authorText: document.querySelector(".blog-article__author")?.textContent?.trim() || "",
      h2InBodyCount: document.querySelectorAll(".blog-article__body h2").length,
      h3InBodyCount: document.querySelectorAll(".blog-article__body h3").length,
      tocNavCount: document.querySelectorAll('nav[aria-label="Содержание статьи"]').length,
      tocLinkCount: document.querySelectorAll(".blog-article__toc-link").length,
      heroLoaded: !!document.querySelector(".blog-article__hero-image")?.naturalWidth,
      inlineLoaded: !!document.querySelector(".blog-article__inline-image")?.naturalWidth,
      activeBlog: document.querySelector(".site-header__nav-link--active")?.textContent?.trim() || "",
      breadcrumbItems: document.querySelectorAll(".breadcrumbs__item").length,
      hasConclusion: !!document.querySelector(".blog-article")?.textContent?.includes("Заключение") &&
        !document.querySelector('nav[aria-label="Содержание статьи"]')?.textContent?.includes("Заключение"),
      hasSources: !!document.querySelector(".blog-article__body")?.textContent?.includes("Источники:"),
      hasRelated: !!document.querySelector(".blog-article")?.textContent?.includes("Рекомендуем к прочтению"),
      hasLowerCta: !!document.querySelector(".program-cta-band"),
      chapter2H2Present: !!document.querySelector("#kto-na-samom-dele-pyuet"),
      overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth,
      duplicateIds: [...new Set(dup)],
    };
  });
  checks.consoleErrors = errors;

  const h3s = await page.$$(".blog-article__body .blog-article__h3");
  const h3Captures = [];
  for (let i = 0; i < h3s.length; i++) {
    const path = join(runtimeDir, `h3-subsection-${i + 1}.png`);
    await h3s[i].screenshot({ path });
    h3Captures.push(path);
  }

  const regions = await Promise.all([
    captureRegion(page, ".blog-article-page__breadcrumbs", "header-breadcrumbs"),
    captureRegion(page, ".blog-article__title", "h1-title"),
    captureRegion(page, ".blog-article__header", "metadata-hero"),
    captureRegion(page, ".blog-article__intro", "toc-lead"),
    captureRegion(page, "#alkogolizm-kak-bolezn-mozga", "first-h2"),
    captureRegion(page, ".blog-article__figure", "first-inline-image"),
    captureRegion(page, ".blog-article__chapter", "chapter-footer-boundary"),
  ]);

  await browser.close();
  server.close();

  const report = { url, port: PORT, checks, regions, h3Captures, fullPath };
  mkdirSync(join(evidenceRoot, "evidence"), { recursive: true });
  writeFileSync(join(evidenceRoot, "evidence/runtime-check.json"), JSON.stringify(report, null, 2));
  console.log(JSON.stringify(report, null, 2));
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
