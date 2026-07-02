import { readFileSync, writeFileSync, mkdirSync } from "fs";
import { join } from "path";
import { createHash } from "crypto";
import puppeteer from "puppeteer-core";

const storageRoot =
  "X:/AI MARS STORAGE/website-factory/fp-0002-shpigovsky-v8/o-centre-micro-pass-13-infrastructure-g5";
const designDir = join(storageRoot, "design");
const beforeDir = join(storageRoot, "before");
const afterDir = join(storageRoot, "after");
const evidenceDir = join(storageRoot, "evidence");

for (const d of [designDir, beforeDir, afterDir, evidenceDir]) {
  mkdirSync(d, { recursive: true });
}

const PORT = Number(process.env.MICRO_PASS_13_PORT || 4728);
const CHROME = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const VIEWPORT_W = 1437;
const MODE = process.argv[2] || "before";
const approvedPngPath =
  "X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/26.06.2026/О центре - десктоп.png";

const approvedBytes = readFileSync(approvedPngPath);
const approvedHash = createHash("sha256").update(approvedBytes).digest("hex").toUpperCase();
const EXPECTED_HASH = "4A3B0D1E47F00738A669A1C18FC7A51DBBD6E660765414B81062A235FDFFB424";
if (approvedHash !== EXPECTED_HASH) {
  console.error("FP0002_OCENTRE_PNG_AUTHORITY_MISMATCH");
  process.exit(2);
}

const CONTEXT_ABOVE = 24;
const CONTEXT_BELOW = 24;
const previewUrl = `http://127.0.0.1:${PORT}/o-centre.html`;

async function waitImages(page) {
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
      new Promise((r) => setTimeout(r, 6000)),
    ]);
    const max = document.documentElement.scrollHeight;
    for (let y = 0; y < max; y += 700) {
      window.scrollTo(0, y);
      await new Promise((r) => setTimeout(r, 120));
    }
    window.scrollTo(0, 0);
    await new Promise((r) => setTimeout(r, 400));
  });
}

async function getG5CropBox(page) {
  return page.evaluate(
    ({ above, below }) => {
      const gallery = document.querySelector(".comfort__gallery");
      const g5 = document.querySelector('[data-inf-group="g5"]');
      const g6 = document.querySelector('[data-inf-group="g6"]');
      const cta = document.getElementById("o-centre-guest-cta");
      if (!gallery || !g5) return { error: "missing anchors", gallery: !!gallery, g5: !!g5 };

      const py = (el) => {
        const r = el.getBoundingClientRect();
        return { top: r.top + window.scrollY, bottom: r.bottom + window.scrollY, height: r.height };
      };

      const galleryPos = py(gallery);
      const g5Pos = py(g5);
      const g6Pos = g6 ? py(g6) : null;
      const ctaPos = cta ? py(cta) : null;

      const top = Math.max(0, galleryPos.bottom - above);
      const lowerBound = g6Pos && g6Pos.top > g5Pos.bottom ? g6Pos.top : ctaPos ? ctaPos.top : g5Pos.bottom;
      const bottom = Math.max(g5Pos.bottom, lowerBound) + below;

      const g5Images = [...g5.querySelectorAll(".infrastructure-narrative__mosaic img")].map((img, i) => ({
        index: i + 1,
        src: (img.getAttribute("src") || "").split("/").pop(),
        width: img.naturalWidth,
        height: img.naturalHeight,
        complete: img.complete,
      }));

      return {
        x: 0,
        y: Math.round(top),
        width: window.innerWidth,
        height: Math.round(Math.max(1, bottom - top)),
        galleryBottom: Math.round(galleryPos.bottom),
        g5Top: Math.round(g5Pos.top),
        g5Bottom: Math.round(g5Pos.bottom),
        g6Top: g6Pos ? Math.round(g6Pos.top) : null,
        ctaTop: ctaPos ? Math.round(ctaPos.top) : null,
        g5ImageCount: g5Images.length,
        g5Images,
      };
    },
    { above: CONTEXT_ABOVE, below: CONTEXT_BELOW },
  );
}

async function cropDesignPng(page, box, outPath) {
  const b64 = approvedBytes.toString("base64");
  await page.setContent(`<html><body style="margin:0"><img id="d" src="data:image/png;base64,${b64}"></body></html>`);
  await page.waitForSelector("#d");
  const el = await page.$("#d");
  const imgBox = await el.boundingBox();
  await page.setViewport({ width: Math.ceil(imgBox.width), height: Math.ceil(imgBox.height), deviceScaleFactor: 1 });
  const y = Math.min(box.y, imgBox.height - 1);
  const h = Math.min(box.height, imgBox.height - y);
  await page.screenshot({
    path: outPath,
    clip: { x: 0, y, width: Math.min(box.width, imgBox.width), height: h },
  });
  return { x: 0, y, width: Math.min(box.width, imgBox.width), height: h };
}

async function captureRuntime(page, outPath, fullPath) {
  await page.setViewport({ width: VIEWPORT_W, height: 1200, deviceScaleFactor: 1 });
  await page.goto(previewUrl, { waitUntil: "load", timeout: 60000 });
  await waitImages(page);
  const box = await getG5CropBox(page);
  if (box.error) throw new Error(JSON.stringify(box));
  await page.evaluate((g5Top) => {
    window.scrollTo(0, Math.max(0, g5Top - 80));
  }, box.g5Top);
  await page.evaluate(async () => {
    const g5 = document.querySelector('[data-inf-group="g5"]');
    if (!g5) return;
    const imgs = [...g5.querySelectorAll("img")];
    await Promise.all(
      imgs.map((img) =>
        img.complete
          ? Promise.resolve()
          : new Promise((resolve) => {
              img.onload = img.onerror = resolve;
            }),
      ),
    );
    await new Promise((r) => setTimeout(r, 500));
  });
  await page.screenshot({ path: fullPath, fullPage: true });
  await page.screenshot({
    path: outPath,
    clip: { x: box.x, y: box.y, width: box.width, height: box.height },
  });
  return box;
}

async function fancyboxQa(page) {
  const consoleErrors = [];
  page.on("console", (msg) => {
    if (msg.type() === "error") consoleErrors.push(msg.text());
  });
  page.on("pageerror", (err) => consoleErrors.push(String(err)));

  await page.setViewport({ width: VIEWPORT_W, height: 1200, deviceScaleFactor: 1 });
  await page.goto(previewUrl, { waitUntil: "load", timeout: 60000 });
  await waitImages(page);

  const first = await page.evaluate(() => {
    const g5 = document.querySelector('[data-inf-group="g5"]');
    const firstLink = g5?.querySelector('a[data-fancybox="o-centre-infrastructure-g5"]');
    if (!firstLink) return { error: "no g5 fancybox link" };
    firstLink.click();
    return { clicked: true, href: firstLink.getAttribute("href") };
  });
  await new Promise((r) => setTimeout(r, 800));

  const openState = await page.evaluate(() => {
    const fb = document.querySelector(".fancybox__container");
    const slides = document.querySelectorAll(".fancybox__slide");
    const infobar = document.querySelector(".fancybox__infobar")?.textContent?.trim() || "";
    return {
      open: !!fb,
      slideCount: slides.length,
      infobar,
    };
  });

  await page.screenshot({
    path: join(evidenceDir, "g5-fancybox-first-open.png"),
    fullPage: false,
  });

  for (let i = 0; i < 5; i++) {
    await page.keyboard.press("ArrowRight");
    await new Promise((r) => setTimeout(r, 250));
  }

  const lastState = await page.evaluate(() => ({
    infobar: document.querySelector(".fancybox__infobar")?.textContent?.trim() || "",
  }));

  await page.screenshot({
    path: join(evidenceDir, "g5-fancybox-last-open.png"),
    fullPage: false,
  });

  await page.keyboard.press("Escape");
  await new Promise((r) => setTimeout(r, 800));

  const closed = await page.evaluate(() => !document.querySelector(".fancybox__container"));

  const groupSeparation = await page.evaluate(() => ({
    g14Count: document.querySelectorAll('[data-fancybox="o-centre-infrastructure"]').length,
    comfortCount: document.querySelectorAll('[data-fancybox="comfort"]').length,
    g5Count: document.querySelectorAll('[data-fancybox="o-centre-infrastructure-g5"]').length,
  }));

  return {
    first,
    openState,
    lastState,
    closed,
    groupSeparation,
    consoleErrors,
  };
}

async function makeSideBySide(page, designPath, beforePath, afterPath, outPath) {
  const toB64 = (p) => readFileSync(p).toString("base64");
  const html = `<!doctype html><html><body style="margin:0;background:#111;display:flex;gap:4px;align-items:flex-start">
    <div><div style="color:#fff;font:12px sans-serif;padding:4px">design</div><img src="data:image/png;base64,${toB64(designPath)}" style="height:1100px;width:auto"></div>
    <div><div style="color:#fff;font:12px sans-serif;padding:4px">before</div><img src="data:image/png;base64,${toB64(beforePath)}" style="height:1100px;width:auto"></div>
    <div><div style="color:#fff;font:12px sans-serif;padding:4px">after</div><img src="data:image/png;base64,${toB64(afterPath)}" style="height:1100px;width:auto"></div>
  </body></html>`;
  await page.setContent(html);
  await page.setViewport({ width: 4200, height: 1160, deviceScaleFactor: 1 });
  await page.screenshot({ path: outPath, fullPage: true });
}

const browser = await puppeteer.launch({
  executablePath: CHROME,
  headless: true,
  args: ["--no-sandbox", "--disable-dev-shm-usage"],
});
const page = await browser.newPage();

try {
  const runtimeDir = MODE === "after" ? afterDir : beforeDir;
  const runtimeCropPath = join(runtimeDir, "g5-runtime-crop.png");
  const runtimeFullPath = join(runtimeDir, "g5-runtime-full.png");
  const runtimeBox = await captureRuntime(page, runtimeCropPath, runtimeFullPath);

  const designCropPath = join(designDir, "g5-design-crop.png");
  const designMeta = await cropDesignPng(page, runtimeBox, designCropPath);

  let fancybox = null;
  if (MODE === "after") {
    fancybox = await fancyboxQa(page);
  }

  const beforePath = join(beforeDir, "g5-runtime-crop.png");
  const afterPath = join(afterDir, "g5-runtime-crop.png");
  if (MODE === "after" && !readFileSync(beforePath)) {
    /* noop */
  }

  if (MODE === "after") {
    const sideBySide = join(evidenceDir, "g5-side-by-side.png");
    await makeSideBySide(page, designCropPath, beforePath, afterPath, sideBySide);
  }

  const anatomyNote = `FP-0002 O-Centre Micro-Pass 13 — G5 anatomy/crop note

PNG SHA-256: ${approvedHash}
Figma parent: Frame 81513620 (1170×1120 desktop)
Row frames: Frame 81513615 (brand+img13), Frame 81513614 (img14-16), Frame 81513613 (img17-18)

Image node → asset mapping:
- 1:2496 / 1:5838 → o-centre-infrastructure-13.webp (OC-INF-13) span 4/6, h 360
- 1:2499 / 1:5839 → o-centre-infrastructure-14.webp (OC-INF-14) span 2/6, h 360
- 1:2500 / 1:5841 → o-centre-infrastructure-15.webp (OC-INF-15) span 2/6, h 360
- 1:2501 / 1:5842 → o-centre-infrastructure-16.webp (OC-INF-16) span 2/6, h 360
- 1:2507 / 1:5846 → o-centre-infrastructure-17.webp (OC-INF-17) span 3/6, h 360
- 1:2508 / 1:5847 → o-centre-infrastructure-18.webp (OC-INF-18) span 3/6, h 360

Grid: 6-column CSS grid, gap var(--pad-gap-line), brand lockup span 2/6 (383/1170).
object-fit: cover; object-position: center (manifest).
Fancybox group: data-fancybox="o-centre-infrastructure-g5" (6 items, DOM order).

Runtime crop y=${runtimeBox.y} h=${runtimeBox.height}
Design crop y=${designMeta.y} h=${designMeta.height}
`;

  writeFileSync(join(evidenceDir, "g5-anatomy-crop-note.txt"), anatomyNote);

  if (fancybox) {
    writeFileSync(
      join(evidenceDir, "g5-fancybox-runtime-note.txt"),
      `G5 Fancybox runtime (${new Date().toISOString()})\n${JSON.stringify(fancybox, null, 2)}\n`,
    );
  }

  const meta = {
    task: "FP-0002 O-Centre Desktop Micro-Pass 13 — Infrastructure G5",
    mode: MODE,
    approved_png_sha256: approvedHash,
    runtime_crop: runtimeBox,
    design_crop: { path: designCropPath, ...designMeta },
    viewport_px: VIEWPORT_W,
    preview_url: previewUrl,
    fancybox,
    paths: {
      design_crop: designCropPath,
      runtime_crop: runtimeCropPath,
      runtime_full: runtimeFullPath,
    },
  };

  writeFileSync(join(evidenceDir, `capture-meta-${MODE}.json`), JSON.stringify(meta, null, 2));
  console.log(JSON.stringify(meta, null, 2));
} finally {
  await browser.close();
}
