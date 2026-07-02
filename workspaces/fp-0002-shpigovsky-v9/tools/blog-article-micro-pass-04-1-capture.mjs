import { createServer } from "http";
import { readFileSync, writeFileSync, mkdirSync } from "fs";
import { join } from "path";
import puppeteer from "puppeteer-core";

const v8Root = "X:/AI MARS/workspaces/fp-0002-shpigovsky-v8";
const distDir = join(v8Root, "dist");
const evidenceRoot =
  "X:/AI MARS STORAGE/website-factory/fp-0002-shpigovsky-v8/blog-article-desktop-micro-pass-04-1";
const phase = process.argv[2] || "snapshot-before";
const outDir = join(evidenceRoot, phase);
const runtimeDir = join(outDir, "runtime");
const PORT = Number(process.env.BLOG_PREVIEW_PORT || 4327);
const CHROME = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const BLOG_PAGE = "/blog/nazvanie-stati.html";

mkdirSync(runtimeDir, { recursive: true });
mkdirSync(join(evidenceRoot, "authority"), { recursive: true });
mkdirSync(join(evidenceRoot, "after"), { recursive: true });
mkdirSync(join(evidenceRoot, "after", "runtime"), { recursive: true });
mkdirSync(join(evidenceRoot, "evidence"), { recursive: true });

function startServer() {
  return new Promise((resolvePromise) => {
    const server = createServer((req, res) => {
      let rel = decodeURIComponent(req.url.split("?")[0]);
      if (rel === "/") rel = BLOG_PAGE;
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

async function captureRegion(page, selector, name, dir) {
  const el = await page.$(selector);
  if (!el) return { name, ok: false, error: "selector not found" };
  const path = join(dir, `${name}.png`);
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
  const errors = [];
  page.on("pageerror", (err) => errors.push(String(err)));

  const blogUrl = `http://127.0.0.1:${PORT}${BLOG_PAGE}`;
  const response = await page.goto(blogUrl, { waitUntil: "networkidle0", timeout: 60000 });

  const isAfter = phase === "after";
  const blogRuntime = isAfter ? join(evidenceRoot, "after", "runtime") : runtimeDir;
  const prefix = isAfter ? "after" : "before";

  await page.screenshot({
    path: join(blogRuntime, `full-page-1437-${prefix}.png`),
    fullPage: true,
  });

  await captureRegion(page, ".blog-article-conclusion", `conclusion-${prefix}`, blogRuntime);
  await captureRegion(
    page,
    isAfter ? ".founder-quote" : ".blog-article-conclusion__panel",
    `conclusion-label-${prefix}`,
    blogRuntime
  );
  await captureRegion(page, ".blog-article-sources", `conclusion-sources-transition-${prefix}`, blogRuntime);

  const checks = await page.evaluate(() => {
    const ids = [...document.querySelectorAll("[id]")].map((el) => el.id);
    const dup = ids.filter((id, i) => ids.indexOf(id) !== i);
    const label = document.querySelector(".blog-article-conclusion__label");
    const labelStyles = label ? getComputedStyle(label) : null;
    return {
      httpPath: location.pathname,
      conclusionLabelIdCount: document.querySelectorAll("#blog-article-conclusion-label").length,
      conclusionLabelClassCount: document.querySelectorAll(".blog-article-conclusion__label").length,
      founderQuoteCount: document.querySelectorAll(".founder-quote").length,
      authorCardCount: document.querySelectorAll(".blog-article-author-card").length,
      conclusionCount: document.querySelectorAll(".blog-article-conclusion").length,
      sourcesCount: document.querySelectorAll(".blog-article-sources").length,
      sourceItems: document.querySelectorAll(".blog-article-sources__list p").length,
      relatedSectionCount: document.querySelectorAll(".blog-article-related").length,
      relatedCards: document.querySelectorAll(".blog-article-related__grid .blog-related-card").length,
      ctaCount: document.querySelectorAll(".blog-article-lower-stack .program-cta-band").length,
      footerCount: document.querySelectorAll("footer").length,
      tocItems: document.querySelectorAll(".blog-article-toc__list li").length,
      excerptCount: document.querySelectorAll(".blog-article-excerpt").length,
      h2Body: document.querySelectorAll(".blog-article-body__content h2").length,
      h3Body: document.querySelectorAll(".blog-article-body__content h3").length,
      duplicateIds: [...new Set(dup)],
      overflowX: document.documentElement.scrollWidth > document.documentElement.clientWidth,
      founderQuoteText: document.querySelector(".founder-quote__text span")?.textContent?.trim() || null,
      founderName: document.querySelector(".founder-quote__name")?.textContent?.trim() || null,
      founderRole: document.querySelector(".founder-quote__role")?.textContent?.trim() || null,
      labelDom: label?.outerHTML || null,
      labelStyles: labelStyles
        ? {
            fontSize: labelStyles.fontSize,
            lineHeight: labelStyles.lineHeight,
            color: labelStyles.color,
          }
        : null,
      consoleErrors: [],
    };
  });
  checks.httpStatus = response?.status() ?? null;
  checks.consoleErrors = errors;

  const jsonName = isAfter ? "runtime-check.json" : "conclusion-label-dom-before.json";
  writeFileSync(join(outDir, jsonName), JSON.stringify(checks, null, 2));

  const ocentrePage = await browser.newPage();
  await ocentrePage.setViewport({ width: 1437, height: 900, deviceScaleFactor: 1 });
  await ocentrePage.goto(`http://127.0.0.1:${PORT}/o-centre.html`, {
    waitUntil: "networkidle0",
    timeout: 60000,
  });
  const ocentreDir = join(evidenceRoot, isAfter ? "after" : "authority");
  await captureRegion(
    ocentrePage,
    ".founder-quote",
    isAfter ? "o-centre-founder-quote-regression" : "o-centre-founder-quote-reference",
    ocentreDir
  );
  const ocentreChecks = await ocentrePage.evaluate(() => ({
    founderQuoteCount: document.querySelectorAll(".founder-quote").length,
    quoteParagraphs: document.querySelectorAll(".founder-quote__text").length,
    firstQuoteSnippet: document.querySelector(".founder-quote__text span")?.textContent?.slice(0, 80) || null,
    name: document.querySelector(".founder-quote__name")?.textContent?.trim() || null,
    role: document.querySelector(".founder-quote__role")?.textContent?.trim() || null,
    ctaPresent: !!document.querySelector(".founder-quote__cta"),
    overflowX: document.documentElement.scrollWidth > document.documentElement.clientWidth,
  }));
  writeFileSync(
    join(evidenceRoot, "evidence", isAfter ? "o-centre-regression-check.json" : "o-centre-reference.json"),
    JSON.stringify(ocentreChecks, null, 2)
  );

  await browser.close();
  server.close();
  console.log(JSON.stringify({ phase, checks, ocentreChecks }, null, 2));
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
