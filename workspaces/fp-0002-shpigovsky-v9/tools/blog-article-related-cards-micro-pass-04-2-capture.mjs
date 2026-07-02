import { createServer } from "http";
import { readFileSync, writeFileSync, mkdirSync } from "fs";
import { join } from "path";
import puppeteer from "puppeteer-core";

const v8Root = "X:/AI MARS/workspaces/fp-0002-shpigovsky-v8";
const distDir = join(v8Root, "dist");
const evidenceRoot =
  "X:/AI MARS STORAGE/website-factory/fp-0002-shpigovsky-v8/blog-article-related-cards-micro-pass-04-2";
const phase = process.argv[2] || "snapshot-before";
const outDir = join(evidenceRoot, phase === "after" ? "after" : "snapshot-before");
const runtimeDir = join(outDir, "runtime");
const PORT = Number(process.env.BLOG_PREVIEW_PORT || 4328);
const CHROME = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const BLOG_PAGE = "/blog/nazvanie-stati.html";

mkdirSync(runtimeDir, { recursive: true });
mkdirSync(join(evidenceRoot, "authority"), { recursive: true });
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

  const relatedCaptures = [
    await captureRegion(page, ".blog-article-related", `related-section-${prefix}`, blogRuntime),
    await captureRegion(page, ".blog-related-card:nth-child(1)", `related-card-1-${prefix}`, blogRuntime),
    await captureRegion(page, ".blog-related-card:nth-child(2)", `related-card-2-${prefix}`, blogRuntime),
    await captureRegion(page, ".blog-related-card:nth-child(3)", `related-card-3-${prefix}`, blogRuntime),
    await captureRegion(
      page,
      ".blog-article-related, .blog-article-lower-stack",
      `related-cta-transition-${prefix}`,
      blogRuntime,
    ),
    await captureRegion(page, ".blog-article-lower-stack", `lower-stack-${prefix}`, blogRuntime),
  ];

  const checks = await page.evaluate(() => {
    const ids = [...document.querySelectorAll("[id]")].map((el) => el.id);
    const dup = ids.filter((id, i) => ids.indexOf(id) !== i);
    const related = document.querySelector(".blog-article-related");
    const grid = document.querySelector(".blog-article-related__grid");
    const gridStyles = grid ? getComputedStyle(grid) : null;
    const card = document.querySelector(".blog-related-card");
    const cardStyles = card ? getComputedStyle(card) : null;
    const image = document.querySelector(".blog-related-card__image");
    const imageStyles = image ? getComputedStyle(image) : null;
    const title = document.querySelector(".blog-related-card__title");
    const titleStyles = title ? getComputedStyle(title) : null;
    const readLink = document.querySelector(".blog-related-card__read-more-link");
    const readStyles = readLink ? getComputedStyle(readLink) : null;
  let forgeCount = 0;
    const walker = document.createTreeWalker(document, NodeFilter.SHOW_COMMENT);
    while (walker.nextNode()) {
      if (walker.currentNode.textContent.includes("FORGE WORDPRESS")) forgeCount += 1;
    }
    return {
      relatedSectionCount: document.querySelectorAll(".blog-article-related").length,
      relatedHeading: document.querySelector(".blog-article-related__heading")?.textContent?.trim(),
      relatedCards: document.querySelectorAll(".blog-article-related__grid .blog-related-card").length,
      articleSemanticCount: document.querySelectorAll(".blog-related-card").length,
      readLinks: document.querySelectorAll(".blog-related-card__read-more-link").length,
      imageLinks: document.querySelectorAll(".blog-related-card__image-link").length,
      titleLinks: document.querySelectorAll(".blog-related-card__title-link").length,
      cardTitles: [...document.querySelectorAll(".blog-related-card__title-link")].map((a) =>
        a.textContent.trim(),
      ),
      readLabels: [...document.querySelectorAll(".blog-related-card__read-more-link")].map((a) =>
        a.textContent.trim(),
      ),
      imagesLoaded: [...document.querySelectorAll(".blog-related-card__image")].every(
        (img) => img.complete && img.naturalWidth > 0,
      ),
      conclusionCount: document.querySelectorAll(".blog-article-conclusion").length,
      founderQuoteCount: document.querySelectorAll(".founder-quote").length,
      sourcesCount: document.querySelectorAll(".blog-article-sources").length,
      sourceItems: document.querySelectorAll(".blog-article-sources__list p").length,
      ctaCount: document.querySelectorAll(".blog-article-lower-stack .program-cta-band").length,
      footerCount: document.querySelectorAll("footer").length,
      tocItems: document.querySelectorAll(".blog-article-toc__list li").length,
      excerptCount: document.querySelectorAll(".blog-article-excerpt").length,
      h2Body: document.querySelectorAll(".blog-article-body__content h2").length,
      h3Body: document.querySelectorAll(".blog-article-body__content h3").length,
      forgeComments: forgeCount,
      duplicateIds: [...new Set(dup)],
      overflowX: document.documentElement.scrollWidth > document.documentElement.clientWidth,
      gridColumns: gridStyles?.gridTemplateColumns || null,
      cardHeight: cardStyles?.height || null,
      cardBackground: cardStyles?.backgroundColor || null,
      imageHeight: imageStyles?.height || null,
      imageBorderRadius: imageStyles?.borderRadius || null,
      titlePadding: titleStyles?.padding || null,
      readColor: readStyles?.color || null,
      readTextTransform: readStyles?.textTransform || null,
    };
  });
  checks.httpStatus = response?.status() ?? null;
  checks.consoleErrors = errors;
  checks.url = blogUrl;

  writeFileSync(
    join(outDir, isAfter ? "runtime-check.json" : "runtime-check-before.json"),
    JSON.stringify({ checks, relatedCaptures, port: PORT }, null, 2),
  );

  if (isAfter) {
    const blogArchivePage = await browser.newPage();
    await blogArchivePage.setViewport({ width: 1437, height: 900, deviceScaleFactor: 1 });
    await blogArchivePage.goto(`http://127.0.0.1:${PORT}/blog.html`, {
      waitUntil: "networkidle0",
      timeout: 60000,
    });
    await captureRegion(
      blogArchivePage,
      ".blog-archive__grid",
      "blog-archive-regression",
      join(evidenceRoot, "after"),
    );
    const archiveChecks = await blogArchivePage.evaluate(() => ({
      cards: document.querySelectorAll(".blog-archive-card").length,
      pagination: document.querySelectorAll(".blog-archive-pagination").length,
      activeNav: document.querySelector(".site-header__nav-link--active")?.textContent?.trim(),
      overflowX: document.documentElement.scrollWidth > document.documentElement.clientWidth,
    }));
    writeFileSync(
      join(evidenceRoot, "evidence", "blog-archive-regression-check.json"),
      JSON.stringify(archiveChecks, null, 2),
    );

    const homePage = await browser.newPage();
    await homePage.setViewport({ width: 1437, height: 900, deviceScaleFactor: 1 });
    await homePage.goto(`http://127.0.0.1:${PORT}/index.html`, {
      waitUntil: "networkidle0",
      timeout: 60000,
    });
    await captureRegion(
      homePage,
      ".home-articles__grid",
      "home-teaser-regression",
      join(evidenceRoot, "after"),
    );
    const homeChecks = await homePage.evaluate(() => ({
      cards: document.querySelectorAll(".home-articles__card").length,
      overflowX: document.documentElement.scrollWidth > document.documentElement.clientWidth,
    }));
    writeFileSync(
      join(evidenceRoot, "evidence", "home-teaser-regression-check.json"),
      JSON.stringify(homeChecks, null, 2),
    );

    await captureRegion(
      homePage,
      ".home-articles__grid",
      "home-teaser-reference",
      join(evidenceRoot, "authority"),
    );
  }

  if (phase === "keep-alive") {
    console.log(JSON.stringify({ keepAlive: true, port: PORT, url: blogUrl }, null, 2));
    return;
  }

  await browser.close();
  server.close();
  console.log(JSON.stringify({ phase, checks, relatedCaptures, port: PORT }, null, 2));
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
