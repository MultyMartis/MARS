import { createServer } from "http";
import { readFileSync, writeFileSync, mkdirSync } from "fs";
import { join } from "path";
import puppeteer from "puppeteer-core";

const v8Root = "X:/AI MARS/workspaces/fp-0002-shpigovsky-v8";
const distDir = join(v8Root, "dist");
const evidenceRoot =
  "X:/AI MARS STORAGE/website-factory/fp-0002-shpigovsky-v8/blog-article-desktop-pass-02";
const phase = process.argv[2] || "after";
const outDir = join(evidenceRoot, phase);
const runtimeDir = join(outDir, "runtime");
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
  await page.goto(url, { waitUntil: "networkidle0", timeout: 60000 });

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
    const tocLinks = [...document.querySelectorAll(".blog-article-hero__toc-link")].map((a) => ({
      href: a.getAttribute("href"),
      text: a.textContent.trim(),
    }));
    const body = document.body;
    const overflowX = Math.max(0, body.scrollWidth - body.clientWidth);
    return {
      h1Count: document.querySelectorAll("h1").length,
      h2BodyCount: h2s.length,
      h3BodyCount: h3s.length,
      h2s,
      h3s,
      heroCount: document.querySelectorAll(".blog-article-hero").length,
      excerptCount: document.querySelectorAll(".blog-article-hero__excerpt").length,
      bodySectionCount: document.querySelectorAll(".blog-article-body").length,
      bodyWrapperCount: document.querySelectorAll(".blog-article-body__content").length,
      forgeComments: [...document.querySelectorAll("*")]
        .filter((n) => n.nodeType === 8 && n.textContent.includes("FORGE WORDPRESS")).length,
      inlineImages: document.querySelectorAll(".blog-article-body__content img").length,
      featuredImages: document.querySelectorAll(".blog-article-hero__media img").length,
      tocLinks,
      duplicateIds: [...new Set(dup)],
      overflowX,
      activeBlog: document.querySelector(".site-header__nav-link--active")?.textContent?.trim(),
    };
  });

  const captures = [];
  if (phase === "after") {
    captures.push(
      await captureRegion(page, "#alkogolizm-kak-bolezn-mozga", "chapter-1-h2"),
      await captureRegion(page, "#kto-na-samom-dele-pyuet", "chapter-2-h2"),
      await captureRegion(page, "img[src*='inline-02']", "inline-image-02"),
      await captureRegion(page, "#psihologicheskie-mehanizmy-zavisimosti", "chapter-3-h2"),
      await captureRegion(page, "img[src*='inline-03']", "inline-image-03"),
      await captureRegion(page, ".blog-article-body", "chapter-3-footer-boundary"),
    );
  } else {
    captures.push(
      await captureRegion(page, ".blog-article-body", "chapter-1-footer-boundary"),
    );
  }

  writeFileSync(
    join(outDir, "runtime-check.json"),
    JSON.stringify({ checks, captures, consoleErrors: errors }, null, 2),
  );

  await browser.close();
  server.close();
  console.log(JSON.stringify({ phase, checks, captures, consoleErrors: errors }, null, 2));
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
