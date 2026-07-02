import { createServer } from "http";
import { readFileSync, writeFileSync, mkdirSync } from "fs";
import { join } from "path";
import puppeteer from "puppeteer-core";

const v8Root = "X:/AI MARS/workspaces/fp-0002-shpigovsky-v8";
const distDir = join(v8Root, "dist");
const evidenceRoot =
  "X:/AI MARS STORAGE/website-factory/fp-0002-shpigovsky-v8/blog-article-desktop-pass-04";
const phase = process.argv[2] || "after";
const outDir = join(evidenceRoot, phase);
const runtimeDir = join(outDir, "runtime");
const PORT = Number(process.env.BLOG_PREVIEW_PORT || 4323);
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
  if (!el) return { name, ok: false, error: "selector not found" };
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
  const response = await page.goto(url, { waitUntil: "networkidle0", timeout: 60000 });

  await page.screenshot({
    path: join(runtimeDir, "full-page-1437.png"),
    fullPage: true,
  });

  const checks = await page.evaluate(() => {
    const ids = [...document.querySelectorAll("[id]")].map((el) => el.id);
    const dup = ids.filter((id, i) => ids.indexOf(id) !== i);
    const h2s = [...document.querySelectorAll(".blog-article-body__content h2")].map((el) => ({
      id: el.id,
      text: el.textContent.trim(),
    }));
    const h3s = [...document.querySelectorAll(".blog-article-body__content h3")].map((el) =>
      el.textContent.trim(),
    );
    const tocLinks = [...document.querySelectorAll(".blog-article-hero__toc a")].map((a) => ({
      href: a.getAttribute("href"),
      text: a.textContent.trim(),
    }));
    const body = document.body;
    const overflowX = Math.max(0, body.scrollWidth - body.clientWidth);
    const forgeComments = [...document.createNodeIterator(document, 128).nextNode() ? [] : []];
    let forgeCount = 0;
    const walker = document.createTreeWalker(document, NodeFilter.SHOW_COMMENT);
    while (walker.nextNode()) {
      if (walker.currentNode.textContent.includes("FORGE WORDPRESS")) forgeCount += 1;
    }
    return {
      httpOk: true,
      h1Count: document.querySelectorAll("h1").length,
      h2BodyCount: h2s.length,
      h3BodyCount: h3s.length,
      h2s,
      h3s,
      heroCount: document.querySelectorAll(".blog-article-hero").length,
      tocLiCount: document.querySelectorAll(".blog-article-hero__toc li").length,
      excerptCount: document.querySelectorAll(".blog-article-hero__excerpt").length,
      bodySectionCount: document.querySelectorAll(".blog-article-body").length,
      bodyWrapperCount: document.querySelectorAll(".blog-article-body__content").length,
      forgeComments: forgeCount,
      inlineImages: document.querySelectorAll(".blog-article-body__content img").length,
      featuredImages: document.querySelectorAll(".blog-article-hero__media img").length,
      conclusionCount: document.querySelectorAll(".blog-article-conclusion").length,
      authorCardCount: document.querySelectorAll(".blog-article-author-card").length,
      sourcesCount: document.querySelectorAll(".blog-article-sources").length,
      sourceItemCount: document.querySelectorAll(".blog-article-sources__list p").length,
      relatedSectionCount: document.querySelectorAll(".blog-article-related").length,
      relatedCardCount: document.querySelectorAll(".blog-related-card").length,
      ctaCount: document.querySelectorAll(".page-blog-article .program-cta-band").length,
      footerCount: document.querySelectorAll("footer").length,
      modalCount: document.querySelectorAll('[data-modal="consultation"]').length,
      relatedOutsideContent:
        document.querySelector(".blog-article-related") &&
        !document.querySelector(".blog-article-body__content")?.contains(
          document.querySelector(".blog-article-related"),
        ),
      ctaOutsideContent:
        document.querySelector(".page-blog-article .program-cta-band") &&
        !document.querySelector(".blog-article-body__content")?.contains(
          document.querySelector(".page-blog-article .program-cta-band"),
        ),
      tocLinks,
      duplicateIds: [...new Set(dup)],
      overflowX,
      activeBlog: document.querySelector(".site-header__nav-link--active")?.textContent?.trim(),
    };
  });

  checks.httpStatus = response?.status() ?? 0;

  const captures = [
    await captureRegion(page, "#statsionarnoe-lechenie", "chapter-5-h2"),
    await captureRegion(page, ".blog-article-conclusion", "conclusion"),
    await captureRegion(page, ".blog-article-author-card", "author-block"),
    await captureRegion(page, ".blog-article-sources", "sources"),
    await captureRegion(page, ".blog-article-related", "related-section"),
    await captureRegion(page, ".blog-related-card:nth-child(1)", "related-card-1"),
    await captureRegion(page, ".blog-related-card:nth-child(2)", "related-card-2"),
    await captureRegion(page, ".blog-related-card:nth-child(3)", "related-card-3"),
    await captureRegion(page, ".page-blog-article .program-cta-band", "compact-cta"),
    await captureRegion(page, "footer", "footer"),
  ];

  if (phase === "before") {
    captures.unshift(
      await captureRegion(page, ".blog-article-body", "chapter-5-footer-boundary"),
    );
  } else {
    captures.unshift(
      await captureRegion(page, ".blog-article-body", "chapter-5-conclusion-boundary"),
    );
  }

  writeFileSync(
    join(outDir, "runtime-check.json"),
    JSON.stringify({ checks, captures, consoleErrors: errors, port: PORT, url }, null, 2),
  );

  await browser.close();
  if (phase !== "keep-alive") server.close();
  console.log(JSON.stringify({ phase, checks, captures, consoleErrors: errors, port: PORT }, null, 2));
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
