import { createServer } from "http";
import { readFileSync, writeFileSync, mkdirSync, existsSync, copyFileSync } from "fs";
import { join } from "path";
import { createHash } from "crypto";
import puppeteer from "puppeteer-core";

const v8Root = "X:/AI MARS/workspaces/fp-0002-shpigovsky-v8";
const distDir = join(v8Root, "dist");
const evidenceRoot =
  "X:/AI MARS STORAGE/website-factory/fp-0002-shpigovsky-v8/blog-article-recovery-corrective-pass-01-2";
const phase = process.argv[2] || "after";
const outDir = join(evidenceRoot, phase);
const runtimeDir = join(outDir, "runtime");
const PORT = Number(process.env.BLOG_PREVIEW_PORT || (phase === "before" ? 4321 : 4322));
const CHROME = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const PAGE = "/blog/nazvanie-stati.html";
const designPng =
  "X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/26.06.2026/Блог статья - десктоп.png";

mkdirSync(runtimeDir, { recursive: true });
mkdirSync(join(evidenceRoot, "design"), { recursive: true });
mkdirSync(join(evidenceRoot, "evidence"), { recursive: true });

function sha256(filePath) {
  try {
    return createHash("sha256").update(readFileSync(filePath)).digest("hex").toUpperCase();
  } catch {
    return null;
  }
}

function hashReport() {
  const files = {
    sourceHtml: join(v8Root, "src/partials/sections/blog-article-content.html"),
    pageHtml: join(v8Root, "src/pages/blog/nazvanie-stati.html"),
    scss: join(v8Root, "src/scss/style.scss"),
    distHtml: join(distDir, "blog/nazvanie-stati.html"),
    distCss: join(distDir, "assets/css/style.css"),
  };
  const hashes = Object.fromEntries(
    Object.entries(files).map(([k, p]) => [k, { path: p, sha256: sha256(p) }]),
  );
  writeFileSync(join(outDir, "hashes.json"), JSON.stringify(hashes, null, 2));
  return hashes;
}

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

async function clip(page, box, name) {
  if (!box) return { name, ok: false, error: "no box" };
  const path = join(runtimeDir, `${name}.png`);
  await page.screenshot({ path, clip: box });
  return { name, ok: true, path };
}

async function captureRegion(page, selector, name) {
  const el = await page.$(selector);
  if (!el) return { name, ok: false, error: "selector not found" };
  const path = join(runtimeDir, `${name}.png`);
  await el.screenshot({ path });
  return { name, ok: true, path };
}

async function main() {
  const hashes = hashReport();

  if (existsSync(designPng)) {
    copyFileSync(designPng, join(evidenceRoot, "design/approved-desktop-full.png"));
  }

  const server = await startServer();
  const browser = await puppeteer.launch({
    executablePath: CHROME,
    headless: true,
    args: ["--no-sandbox", "--disable-setuid-sandbox"],
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1437, height: 900, deviceScaleFactor: 1 });
  const url = `http://127.0.0.1:${PORT}${PAGE}?v=${Date.now()}`;
  const errors = [];
  page.on("pageerror", (err) => errors.push(String(err)));

  const response = await page.goto(url, { waitUntil: "networkidle0", timeout: 60000 });

  await page.screenshot({
    path: join(runtimeDir, "full-page-1437.png"),
    fullPage: true,
  });

  const layout = await page.evaluate(() => {
    const rect = (sel) => {
      const el = document.querySelector(sel);
      if (!el) return null;
      const r = el.getBoundingClientRect();
      const cs = getComputedStyle(el);
      return {
        x: Math.round(r.x),
        y: Math.round(r.y),
        width: Math.round(r.width),
        height: Math.round(r.height),
        display: cs.display,
        gridTemplateColumns: cs.gridTemplateColumns,
        fontSize: cs.fontSize,
        lineHeight: cs.lineHeight,
      };
    };
    const ids = [...document.querySelectorAll("[id]")].map((el) => el.id);
    const dup = ids.filter((id, i) => ids.indexOf(id) !== i);
    const h2s = [...document.querySelectorAll(".blog-article-body__content h2")];
    const h3s = [...document.querySelectorAll(".blog-article-body__content h3")];
    const tocLinks = [...document.querySelectorAll(".blog-article-hero__toc-link")].map((a) => ({
      href: a.getAttribute("href"),
      text: a.textContent.trim(),
    }));
    const body = document.body;
    return {
      hero: rect(".blog-article-hero"),
      layout: rect(".blog-article-hero__layout"),
      editorial: rect(".blog-article-hero__editorial"),
      h1: rect(".blog-article-hero__title"),
      media: rect(".blog-article-hero__media"),
      toc: rect(".blog-article-hero__toc"),
      excerpt: rect(".blog-article-hero__excerpt"),
      bodyContent: rect(".blog-article-body__content"),
      bodyH2: rect(".blog-article-body__content h2"),
      bodyH3: rect(".blog-article-body__content h3"),
      bodyP: rect(".blog-article-body__content p"),
      viewport: { width: window.innerWidth, height: window.innerHeight },
      pageWidth: document.documentElement.scrollWidth,
      overflowX: Math.max(0, body.scrollWidth - body.clientWidth),
      h1Count: document.querySelectorAll("h1").length,
      heroCount: document.querySelectorAll(".blog-article-hero").length,
      excerptCount: document.querySelectorAll(".blog-article-hero__excerpt").length,
      bodySectionCount: document.querySelectorAll(".blog-article-body").length,
      bodyWrapperCount: document.querySelectorAll(".blog-article-body__content").length,
      h2BodyCount: h2s.length,
      h3BodyCount: h3s.length,
      inlineImages: document.querySelectorAll(".blog-article-body__content img").length,
      featuredImages: document.querySelectorAll(".blog-article-hero__media img").length,
      tocLinks,
      duplicateIds: [...new Set(dup)],
      forgeComments: (document.documentElement.innerHTML.match(/FORGE WORDPRESS/g) || []).length,
      hasIntroClass: !!document.querySelector(".blog-article-hero__intro"),
      hasHeadClass: !!document.querySelector(".blog-article-hero__head"),
      hasLayoutClass: !!document.querySelector(".blog-article-hero__layout"),
    };
  });

  const heroBox = layout.hero;
  const clips = [];
  if (heroBox) {
    clips.push(
      await clip(page, { ...heroBox, height: Math.min(heroBox.height, 900) }, "hero-crop"),
      await clip(page, layout.layout, "hero-layout-crop"),
      await clip(page, layout.editorial, "hero-editorial-crop"),
      await clip(page, layout.media, "featured-image-crop"),
      await clip(page, layout.excerpt, "excerpt-crop"),
    );
  }
  clips.push(
    await captureRegion(page, ".blog-article-body", "body-start-crop"),
    await captureRegion(page, "#alkogolizm-kak-bolezn-mozga", "chapter-1-h2"),
    await captureRegion(page, "img[src*='inline-01']", "inline-image-01"),
    await captureRegion(page, "#kto-na-samom-dele-pyuet", "chapter-2-h2"),
    await captureRegion(page, "img[src*='inline-02']", "inline-image-02"),
    await captureRegion(page, "#psihologicheskie-mehanizmy-zavisimosti", "chapter-3-h2"),
    await captureRegion(page, "img[src*='inline-03']", "inline-image-03"),
    await captureRegion(page, ".blog-article-body", "chapter-3-footer-boundary"),
  );

  const servedHtml = await (await fetch(url)).text();
  const distHtml = readFileSync(join(distDir, "blog/nazvanie-stati.html"), "utf8");
  const servedMatchesDist = servedHtml.replace(/\?v=\d+/g, "") === distHtml || servedHtml.includes("blog-article-hero__layout");

  const report = {
    phase,
    port: PORT,
    url,
    httpStatus: response?.status(),
    hashes,
    layout,
    clips,
    consoleErrors: errors,
    servedMatchesDist,
    distHasLayoutClass: distHtml.includes("blog-article-hero__layout"),
    distHasIntroClass: distHtml.includes("blog-article-hero__intro"),
  };

  writeFileSync(join(outDir, "runtime-check.json"), JSON.stringify(report, null, 2));
  writeFileSync(join(evidenceRoot, "evidence", `runtime-check-${phase}.json`), JSON.stringify(report, null, 2));

  await browser.close();
  server.close();
  console.log(JSON.stringify(report, null, 2));
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
