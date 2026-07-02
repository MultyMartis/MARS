import { createServer } from "http";
import { readFileSync, writeFileSync, mkdirSync, statSync } from "fs";
import { dirname, join, resolve } from "path";
import { fileURLToPath } from "url";
import puppeteer from "puppeteer-core";

const __dir = dirname(fileURLToPath(import.meta.url));
const v8Root = resolve(__dir, "../..");
const distDir = join(v8Root, "dist");
const outJson = process.argv[2];
const screenshotDir = process.argv[3];
mkdirSync(screenshotDir, { recursive: true });

const PORT = 4217;
const CHROME = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";

const REGION_SPECS = [
  { region_id: "OC-HERO", selector: ".services-inner-hero-v2, .service-inner-hero-v2", source: "services-inner-hero-v2.html" },
  { region_id: "OC-SUBNAV", selector: ".services-page-subnav", source: "internal-page-nav.html" },
  { region_id: "OC-INST", selector: "#who-we-are.institutional-narrative", source: "institutional-narrative.html" },
  { region_id: "OC-WHO-TREAT", selector: "#who-we-treat.services-category-section-v2", source: "services-category-section-v2.html" },
  { region_id: "OC-APPROACH", selector: "#our-approach.program-approach-band", source: "inline o-centre.html" },
  { region_id: "OC-PROGRAM", selector: "#our-program.services-program-v2", source: "services-program-v2.html" },
  { region_id: "OC-CTA-MID", selector: "#o-centre-mid-cta", source: "program-cta-band.html" },
  { region_id: "OC-FOUNDER", selector: ".founder-quote", source: "founder-quote.html" },
  { region_id: "OC-INFRA", selector: "#our-home.infrastructure-narrative", source: "infrastructure-narrative.html" },
  { region_id: "OC-CTA-GUEST", selector: "#o-centre-guest-cta", source: "program-cta-band.html" },
  { region_id: "OC-SPECIALISTS", selector: "#specialists", source: "specialists.html" },
  { region_id: "OC-REVIEWS", selector: "#reviews", source: "reviews.html" },
  { region_id: "OC-FINAL-FORM", selector: ".final-form", source: "final-form.html" },
];

function startServer() {
  return new Promise((resolvePromise) => {
    const server = createServer((req, res) => {
      let rel = decodeURIComponent(req.url.split("?")[0]);
      if (rel === "/") rel = "/o-centre.html";
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
          mp4: "video/mp4",
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

async function captureViewport(page, width, screenshotPath) {
  await page.setViewport({ width, height: 900, deviceScaleFactor: 1 });
  await page.goto(`http://127.0.0.1:${PORT}/o-centre.html`, { waitUntil: "load", timeout: 60000 });
  await page.evaluate(async () => {
    const imgs = [...document.images];
    await Promise.race([
      Promise.all(
        imgs.map((img) =>
          img.complete
            ? Promise.resolve()
            : new Promise((resolve) => {
                img.onload = img.onerror = resolve;
              }),
        ),
      ),
      new Promise((r) => setTimeout(r, 3000)),
    ]);
  });
  const metrics = await page.evaluate((specs) => {
    const regions = specs.map((spec, idx) => {
      const el = document.querySelector(spec.selector);
      if (!el) {
        return {
          order: idx + 1,
          region_id: spec.region_id,
          selector: spec.selector,
          source: spec.source,
          y: null,
          height: null,
          width: null,
          major: "MISSING",
          mobile: "same DOM",
        };
      }
      const r = el.getBoundingClientRect();
      const y = Math.round(r.top + window.scrollY);
      return {
        order: idx + 1,
        region_id: spec.region_id,
        selector: spec.selector,
        source: spec.source,
        y,
        height: Math.round(r.height),
        width: Math.round(r.width),
        major: el.querySelector("h1,h2")?.textContent?.trim().slice(0, 80) || spec.region_id,
        mobile: "same DOM",
      };
    });
    const pageHeight = Math.max(document.body.scrollHeight, document.documentElement.scrollHeight);
    return { page_height: pageHeight, viewport_width: window.innerWidth, regions };
  }, REGION_SPECS);

  await page.screenshot({ path: screenshotPath, fullPage: true });
  const st = statSync(screenshotPath);
  return { ...metrics, screenshot_bytes: st.size };
}

const server = await startServer();
const browser = await puppeteer.launch({
  executablePath: CHROME,
  headless: true,
  protocolTimeout: 180000,
  args: ["--no-sandbox", "--disable-dev-shm-usage"],
});

try {
  const page = await browser.newPage();
  const desktopPath = join(screenshotDir, "o-centre-desktop-1437-full.png");
  const mobilePath = join(screenshotDir, "o-centre-mobile-390-full.png");
  const desktop = await captureViewport(page, 1437, desktopPath);
  const mobile = await captureViewport(page, 390, mobilePath);

  const figmaMap = {
    "OC-HERO": 905,
    "OC-INST": 1131,
    "OC-WHO-TREAT": 598,
    "OC-CTA-MID": 168,
    "OC-APPROACH": 1837,
    "OC-PROGRAM": 1519,
    "OC-INFRA": 3621,
    "OC-CTA-GUEST": 107,
    "OC-SPECIALISTS": 561,
    "OC-REVIEWS": 429,
    "OC-FINAL-FORM": 366,
  };
  let figmaCum = 0;
  const cumulative_drift = [];
  for (const [region, h] of Object.entries(figmaMap)) {
    figmaCum += h;
    const impl = desktop.regions.find((r) => r.region_id === region);
    cumulative_drift.push({
      region_end: region,
      figma_cumulative_y: figmaCum,
      implementation_cumulative_y: impl?.y != null ? impl.y + impl.height : null,
      drift_px: impl?.y != null ? impl.y + impl.height - figmaCum : null,
      primary_cause: "Order/subregion mismatch — see reconciliation",
    });
  }

  const geometry = desktop.regions
    .filter((r) => r.y != null)
    .map((r) => {
      const figmaH = figmaMap[r.region_id];
      return {
        region: r.region_id,
        metric: "block_height",
        figma: figmaH ?? "ESTIMATED",
        implementation: r.height,
        delta_px: figmaH != null ? r.height - figmaH : null,
        delta_pct: figmaH != null ? Math.round(((r.height - figmaH) / figmaH) * 100) : null,
        severity:
          figmaH != null && Math.abs(r.height - figmaH) > figmaH * 0.35
            ? "STRUCTURAL"
            : figmaH != null && Math.abs(r.height - figmaH) > figmaH * 0.15
              ? "MAJOR"
              : "ESTIMATED",
      };
    });

  const payload = {
    captured_at: new Date().toISOString(),
    git_head: "dbc057cbc37e7adc07983ddbdb0ac053046293f9",
    url: `http://127.0.0.1:${PORT}/o-centre.html`,
    browser: "Google Chrome via puppeteer-core",
    desktop: {
      viewport_width: 1437,
      device_scale_factor: 1,
      page_height: desktop.page_height,
      screenshot: desktopPath,
      screenshot_bytes: desktop.screenshot_bytes,
    },
    mobile: {
      viewport_width: 390,
      device_scale_factor: 1,
      page_height: mobile.page_height,
      screenshot: mobilePath,
      screenshot_bytes: mobile.screenshot_bytes,
    },
    regions: desktop.regions,
    geometry,
    cumulative_drift,
  };

  writeFileSync(outJson, JSON.stringify(payload, null, 2), "utf8");
  console.log("Wrote", outJson);
} finally {
  await browser.close();
  server.close();
}
