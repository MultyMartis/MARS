import { createServer } from "http";
import { readFileSync, writeFileSync, mkdirSync, readdirSync, statSync } from "fs";
import { join, resolve, dirname } from "path";
import { fileURLToPath } from "url";
import { createHash } from "crypto";
import { spawnSync } from "child_process";
import puppeteer from "puppeteer-core";

const __dir = dirname(fileURLToPath(import.meta.url));
const v8Root = resolve(__dir, "../..");
const distDir = join(v8Root, "dist");
const storageRoot = "X:/AI MARS STORAGE/website-factory/fp-0002-shpigovsky-v8/o-centre-micro-pass-01";
const designDir = join(storageRoot, "design");
const beforeDir = join(storageRoot, "before");
const afterDir = join(storageRoot, "after");
const evidenceDir = join(storageRoot, "evidence");

for (const d of [designDir, beforeDir, afterDir, evidenceDir]) mkdirSync(d, { recursive: true });

const PORT = Number(process.env.MICRO_PASS_PORT || 4721);
const CHROME = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const VIEWPORT_W = 1437;
const CROP = { x: 0, y: 4300, width: 1437, height: 4500 };

const approvedDir =
  "X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/26.06.2026";
const approvedFile = readdirSync(approvedDir).find(
  (f) => f.endsWith(".png") && statSync(join(approvedDir, f)).size === 13496724,
);
if (!approvedFile) throw new Error("Approved O-Centre desktop PNG not found");
const approvedPngPath = join(approvedDir, approvedFile);
const approvedBytes = readFileSync(approvedPngPath);
const approvedHash = createHash("sha256").update(approvedBytes).digest("hex").toUpperCase();

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

async function cropDesignPng(page, outPath) {
  const b64 = approvedBytes.toString("base64");
  await page.setContent(`<html><body style="margin:0"><img id="d" src="data:image/png;base64,${b64}"></body></html>`);
  await page.waitForSelector("#d");
  const el = await page.$("#d");
  const box = await el.boundingBox();
  await page.setViewport({ width: Math.ceil(box.width), height: Math.ceil(box.height), deviceScaleFactor: 1 });
  await page.screenshot({
    path: outPath,
    clip: { x: CROP.x, y: CROP.y, width: CROP.width, height: Math.min(CROP.height, box.height - CROP.y) },
  });
}

async function captureRuntime(page, outPath) {
  await page.setViewport({ width: VIEWPORT_W, height: 900, deviceScaleFactor: 1 });
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
      new Promise((r) => setTimeout(r, 4000)),
    ]);
    const max = document.documentElement.scrollHeight;
    for (let y = 0; y < max; y += 700) {
      window.scrollTo(0, y);
      await new Promise((r) => setTimeout(r, 120));
    }
    window.scrollTo(0, 0);
    await new Promise((r) => setTimeout(r, 300));
  });
  const fullPath = outPath.replace(/\.png$/, "-full.png");
  await page.screenshot({ path: fullPath, fullPage: true });
  return fullPath;
}

function cropRuntimeFull(fullPath, outPath) {
  const py = join(__dir, "micro-pass-01-crop.py");
  const result = spawnSync("python", [py, fullPath, outPath], { encoding: "utf-8" });
  if (result.status !== 0) {
    throw new Error(`crop failed: ${result.stderr || result.stdout}`);
  }
}

async function diagnose(page) {
  await page.setViewport({ width: VIEWPORT_W, height: 900, deviceScaleFactor: 1 });
  await page.goto(`http://127.0.0.1:${PORT}/o-centre.html`, { waitUntil: "load", timeout: 60000 });
  return page.evaluate(() => {
    const pick = (sel) => {
      const el = document.querySelector(sel);
      if (!el) return null;
      const cs = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      const before = getComputedStyle(el, "::before");
      return {
        selector: sel,
        rect: { top: r.top, left: r.left, width: r.width, height: r.height },
        display: cs.display,
        visibility: cs.visibility,
        opacity: cs.opacity,
        position: cs.position,
        zIndex: cs.zIndex,
        overflow: cs.overflow,
        minHeight: cs.minHeight,
        maxHeight: cs.maxHeight,
        beforeContent: before.content,
        beforeOpacity: before.opacity,
        beforeBgImage: before.backgroundImage?.slice(0, 100),
        beforeBgSize: before.backgroundSize,
      };
    };
    const imgs = [...document.querySelectorAll("#our-program img, #our-home img")].slice(0, 8).map((img) => {
      const cs = getComputedStyle(img);
      const r = img.getBoundingClientRect();
      return {
        src: img.getAttribute("src")?.split("/").pop(),
        complete: img.complete,
        natural: { w: img.naturalWidth, h: img.naturalHeight },
        rect: { w: r.width, h: r.height },
        opacity: cs.opacity,
        visibility: cs.visibility,
        display: cs.display,
        position: cs.position,
        objectFit: cs.objectFit,
        height: cs.height,
        minHeight: cs.minHeight,
      };
    });
    return {
      program: pick("#our-program"),
      programMedia: pick("#our-program .services-program-v2__item-media"),
      programImage: pick("#our-program .services-program-v2__item-image"),
      infra: pick("#our-home"),
      infraContainer: pick("#our-home .infrastructure-narrative__container"),
      infraFigure: pick("#our-home .infrastructure-narrative__figure"),
      infraImage: pick("#our-home .infrastructure-narrative__image"),
      sampleImages: imgs,
      pageHeight: document.documentElement.scrollHeight,
      overflowX: document.documentElement.scrollWidth > window.innerWidth,
    };
  });
}

async function makeSideBySide(page, designPath, beforePath, afterPath, outPath) {
  const toB64 = (p) => readFileSync(p).toString("base64");
  const html = `<!doctype html><html><body style="margin:0;background:#111;display:flex;gap:4px">
    <div><div style="color:#fff;font:12px sans-serif;padding:4px">design</div><img src="data:image/png;base64,${toB64(designPath)}" style="height:900px;width:auto"></div>
    <div><div style="color:#fff;font:12px sans-serif;padding:4px">before</div><img src="data:image/png;base64,${toB64(beforePath)}" style="height:900px;width:auto"></div>
    <div><div style="color:#fff;font:12px sans-serif;padding:4px">after</div><img src="data:image/png;base64,${toB64(afterPath)}" style="height:900px;width:auto"></div>
  </body></html>`;
  await page.setContent(html);
  await page.setViewport({ width: 4400, height: 1000, deviceScaleFactor: 1 });
  await page.screenshot({ path: outPath, fullPage: true });
}

const phase = process.argv[2] || "before";
const server = await startServer();
const browser = await puppeteer.launch({
  executablePath: CHROME,
  headless: true,
  args: ["--no-sandbox", "--disable-dev-shm-usage"],
});
const page = await browser.newPage();

const meta = {
  approved_png_path: approvedPngPath,
  approved_png_sha256: approvedHash,
  crop: CROP,
  viewport: VIEWPORT_W,
  port: PORT,
};

try {
  const designCrop = join(designDir, "o-centre-micro-pass-01-design-crop.png");
  await cropDesignPng(page, designCrop);
  meta.design_crop = designCrop;

  if (phase === "before") {
    const beforeCrop = join(beforeDir, "o-centre-micro-pass-01-runtime-before.png");
    const diag = await diagnose(page);
    const beforeFull = await captureRuntime(page, beforeCrop);
    cropRuntimeFull(beforeFull, beforeCrop);
    meta.before_crop = beforeCrop;
    meta.diagnosis = diag;
    writeFileSync(join(evidenceDir, "micro-pass-01-before-meta.json"), JSON.stringify(meta, null, 2));
    console.log(JSON.stringify({ phase: "before", ...meta }, null, 2));
  } else {
    const beforeCrop = join(beforeDir, "o-centre-micro-pass-01-runtime-before.png");
    const afterCrop = join(afterDir, "o-centre-micro-pass-01-runtime-after.png");
    const diag = await diagnose(page);
    const afterFull = await captureRuntime(page, afterCrop);
    cropRuntimeFull(afterFull, afterCrop);
    const sideBySide = join(evidenceDir, "o-centre-micro-pass-01-side-by-side.png");
    await makeSideBySide(page, designCrop, beforeCrop, afterCrop, sideBySide);
    meta.after_crop = afterCrop;
    meta.side_by_side = sideBySide;
    meta.diagnosis_after = diag;
    writeFileSync(join(evidenceDir, "micro-pass-01-after-meta.json"), JSON.stringify(meta, null, 2));
    console.log(JSON.stringify({ phase: "after", ...meta }, null, 2));
  }
} finally {
  await browser.close();
  server.close();
}
