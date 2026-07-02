import { readFileSync, writeFileSync, mkdirSync, copyFileSync } from "fs";
import { join } from "path";
import { createHash } from "crypto";
import puppeteer from "puppeteer-core";

const storageRoot =
  "X:/AI MARS STORAGE/website-factory/fp-0002-shpigovsky-v8/o-centre-micro-pass-12-lower-shared-assembly";
const designDir = join(storageRoot, "design");
const beforeDir = join(storageRoot, "before");
const afterDir = join(storageRoot, "after");
const evidenceDir = join(storageRoot, "evidence");

for (const d of [designDir, beforeDir, afterDir, evidenceDir]) {
  mkdirSync(d, { recursive: true });
}

const PORT = Number(process.env.MICRO_PASS_12_PORT || 4728);
const CHROME = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const VIEWPORT_W = 1437;
const approvedPngPath =
  "X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/26.06.2026/О центре - десктоп.png";

const approvedBytes = readFileSync(approvedPngPath);
const approvedHash = createHash("sha256").update(approvedBytes).digest("hex").toUpperCase();
const EXPECTED_HASH = "4A3B0D1E47F00738A669A1C18FC7A51DBBD6E660765414B81062A235FDFFB424";
if (approvedHash !== EXPECTED_HASH) {
  console.error("FP0002_OCENTRE_PNG_AUTHORITY_MISMATCH");
  process.exit(2);
}

const DESIGN_CROP = { x: 0, y: 9180, width: 1437, height: 3650 };
const RUNTIME_CONTEXT_ABOVE = 32;
const RUNTIME_CONTEXT_BELOW = 48;
const previewUrl = `http://127.0.0.1:${PORT}/o-centre.html`;

async function cropDesignPng(page, outPath) {
  const b64 = approvedBytes.toString("base64");
  await page.setContent(`<html><body style="margin:0"><img id="d" src="data:image/png;base64,${b64}"></body></html>`);
  await page.waitForSelector("#d");
  const el = await page.$("#d");
  const box = await el.boundingBox();
  await page.setViewport({ width: Math.ceil(box.width), height: Math.ceil(box.height), deviceScaleFactor: 1 });
  const h = Math.min(DESIGN_CROP.height, box.height - DESIGN_CROP.y);
  await page.screenshot({
    path: outPath,
    clip: { x: DESIGN_CROP.x, y: DESIGN_CROP.y, width: DESIGN_CROP.width, height: h },
  });
  return { ...DESIGN_CROP, height: h };
}

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

async function getLowerTailCropBox(page) {
  return page.evaluate(
    ({ above, below }) => {
      const gallery = document.querySelector(".comfort__gallery");
      const footer = document.querySelector("footer, .site-footer, .footer");
      const cta = document.getElementById("o-centre-guest-cta");
      const specialists = document.getElementById("specialists");
      const reviews = document.getElementById("reviews");
      const finalForm = document.querySelector(".final-form");
      if (!gallery || !footer) return { error: "missing anchors", gallery: !!gallery, footer: !!footer };

      const py = (el) => {
        const r = el.getBoundingClientRect();
        return { top: r.top + window.scrollY, bottom: r.bottom + window.scrollY, height: r.height };
      };

      const galleryPos = py(gallery);
      const footerPos = py(footer);
      const top = Math.max(0, galleryPos.bottom - above);
      const bottom = footerPos.bottom + below;

      const blocks = [];
      for (const [name, el] of [
        ["comfort__gallery", gallery],
        ["o-centre-guest-cta", cta],
        ["specialists", specialists],
        ["reviews", reviews],
        ["final-form", finalForm],
        ["footer", footer],
      ]) {
        if (!el) {
          blocks.push({ name, present: false });
          continue;
        }
        const p = py(el);
        blocks.push({ name, present: true, top: Math.round(p.top), bottom: Math.round(p.bottom), height: Math.round(p.height) });
      }

      return {
        x: 0,
        y: Math.round(top),
        width: window.innerWidth,
        height: Math.round(Math.max(1, bottom - top)),
        blocks,
        galleryBottom: Math.round(galleryPos.bottom),
        footerBottom: Math.round(footerPos.bottom),
      };
    },
    { above: RUNTIME_CONTEXT_ABOVE, below: RUNTIME_CONTEXT_BELOW },
  );
}

async function captureRuntimeCrop(page, outPath, fullPath) {
  await page.setViewport({ width: VIEWPORT_W, height: 1200, deviceScaleFactor: 1 });
  await page.goto(previewUrl, { waitUntil: "load", timeout: 60000 });
  await waitImages(page);
  const box = await getLowerTailCropBox(page);
  if (box.error) throw new Error(JSON.stringify(box));
  await page.screenshot({ path: fullPath, fullPage: true });
  await page.screenshot({
    path: outPath,
    clip: { x: box.x, y: box.y, width: box.width, height: box.height },
  });
  return box;
}

async function runtimeQa(page) {
  const consoleErrors = [];
  page.on("console", (msg) => {
    if (msg.type() === "error") consoleErrors.push(msg.text());
  });
  page.on("pageerror", (err) => consoleErrors.push(String(err)));

  await page.setViewport({ width: VIEWPORT_W, height: 1200, deviceScaleFactor: 1 });
  await page.goto(previewUrl, { waitUntil: "load", timeout: 60000 });
  await waitImages(page);

  const qa = await page.evaluate(() => {
    const dupIds = (() => {
      const seen = new Map();
      for (const el of document.querySelectorAll("[id]")) {
        const id = el.id;
        if (!id) continue;
        seen.set(id, (seen.get(id) || 0) + 1);
      }
      return [...seen.entries()].filter(([, c]) => c > 1).map(([id, count]) => ({ id, count }));
    })();

    const overflowX = document.documentElement.scrollWidth > window.innerWidth + 1;

    const selectors = [
      ".comfort__gallery",
      "#o-centre-guest-cta",
      "#specialists",
      "#reviews",
      ".final-form",
      "footer, .site-footer",
    ];
    const order = selectors
      .map((sel) => {
        const el = document.querySelector(sel);
        if (!el) return { sel, present: false };
        const r = el.getBoundingClientRect();
        return {
          sel,
          present: true,
          top: Math.round(r.top + window.scrollY),
          text: (el.querySelector("h2, .program-cta-band__title, .reviews__title")?.textContent || "").trim().slice(0, 60),
        };
      })
      .filter((x) => x.present)
      .sort((a, b) => a.top - b.top);

    const ctaPhone = document.querySelector("#o-centre-guest-cta .program-cta-band__phone");
    const ctaBtn = document.querySelector("#o-centre-guest-cta .program-cta-band__button");
    const form = document.querySelector(".final-form form[data-lead-form]");
    const formFields = form ? [...form.querySelectorAll("input, textarea, button")].map((el) => el.name || el.type) : [];

    const infraG5 = document.querySelector('[data-inf-group="g5"]');
    const gallery = document.querySelector(".comfort__gallery");

    const betweenGalleryAndCta = (() => {
      if (!gallery || !document.getElementById("o-centre-guest-cta")) return null;
      const gBottom = gallery.getBoundingClientRect().bottom + window.scrollY;
      const ctaTop = document.getElementById("o-centre-guest-cta").getBoundingClientRect().top + window.scrollY;
      const g5Between =
        infraG5 &&
        infraG5.getBoundingClientRect().top + window.scrollY >= gBottom - 4 &&
        infraG5.getBoundingClientRect().bottom + window.scrollY <= ctaTop + 4;
      return { galleryBottom: Math.round(gBottom), ctaTop: Math.round(ctaTop), g5Between };
    })();

    return {
      pageHeight: document.documentElement.scrollHeight,
      viewportWidth: window.innerWidth,
      scrollWidth: document.documentElement.scrollWidth,
      overflowX,
      duplicateIds: dupIds,
      blockOrder: order,
      ctaPhoneHref: ctaPhone?.getAttribute("href") || null,
      ctaButtonModal: ctaBtn?.getAttribute("data-modal-open") || null,
      formFieldCount: formFields.length,
      formFields,
      galleryItemCount: gallery?.querySelectorAll(".comfort__gallery-item").length || 0,
      betweenGalleryAndCta,
      specialistsSlider: !!document.querySelector("[data-specialists-slider]"),
      reviewsSlider: !!document.querySelector("[data-reviews-slider]"),
    };
  });

  return { ...qa, consoleErrors };
}

async function makeSideBySide(page, designPath, runtimePath, outPath) {
  const toB64 = (p) => readFileSync(p).toString("base64");
  const html = `<!doctype html><html><body style="margin:0;background:#111;display:flex;gap:4px;align-items:flex-start">
    <div><div style="color:#fff;font:12px sans-serif;padding:4px">design</div><img src="data:image/png;base64,${toB64(designPath)}" style="height:1200px;width:auto"></div>
    <div><div style="color:#fff;font:12px sans-serif;padding:4px">runtime</div><img src="data:image/png;base64,${toB64(runtimePath)}" style="height:1200px;width:auto"></div>
  </body></html>`;
  await page.setContent(html);
  await page.setViewport({ width: 3000, height: 1260, deviceScaleFactor: 1 });
  await page.screenshot({ path: outPath, fullPage: true });
}

const browser = await puppeteer.launch({
  executablePath: CHROME,
  headless: true,
  args: ["--no-sandbox", "--disable-dev-shm-usage"],
});
const page = await browser.newPage();

try {
  const designCropPath = join(designDir, "o-centre-lower-tail-design-crop.png");
  const designCropMeta = await cropDesignPng(page, designCropPath);

  const beforePath = join(beforeDir, "o-centre-lower-tail-before.png");
  const beforeFull = join(beforeDir, "o-centre-lower-tail-before-full.png");
  const runtimeBox = await captureRuntimeCrop(page, beforePath, beforeFull);

  const afterPath = join(afterDir, "o-centre-lower-tail-after.png");
  copyFileSync(beforePath, afterPath);

  const qa = await runtimeQa(page);
  const sideBySide = join(evidenceDir, "o-centre-lower-tail-side-by-side.png");
  await makeSideBySide(page, designCropPath, afterPath, sideBySide);

  const meta = {
    task: "FP-0002 O-Centre Desktop Micro-Pass 12 — Lower Shared Assembly",
    approved_png_path: approvedPngPath,
    approved_png_sha256: approvedHash,
    design_crop: { path: designCropPath, ...designCropMeta },
    runtime_crop: runtimeBox,
    viewport_px: VIEWPORT_W,
    preview_url: previewUrl,
    qa,
    paths: {
      design_crop: designCropPath,
      before: beforePath,
      after: afterPath,
      side_by_side: sideBySide,
    },
  };

  writeFileSync(join(evidenceDir, "capture-meta.json"), JSON.stringify(meta, null, 2));
  console.log(JSON.stringify(meta, null, 2));
} finally {
  await browser.close();
}
