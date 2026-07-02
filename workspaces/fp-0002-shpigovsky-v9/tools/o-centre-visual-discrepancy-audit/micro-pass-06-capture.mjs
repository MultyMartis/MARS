import { readFileSync, writeFileSync, mkdirSync } from "fs";
import { join } from "path";
import { createHash } from "crypto";
import { spawnSync } from "child_process";
import puppeteer from "puppeteer-core";

const storageRoot =
  "X:/AI MARS STORAGE/website-factory/fp-0002-shpigovsky-v8/o-centre-micro-pass-06-program";
const designDir = join(storageRoot, "design");
const beforeDir = join(storageRoot, "before");
const afterDir = join(storageRoot, "after");
const evidenceDir = join(storageRoot, "evidence");
const notesDir = join(storageRoot, "notes");
const tempDir = join(storageRoot, "temp");

for (const d of [designDir, beforeDir, afterDir, evidenceDir, notesDir, tempDir]) {
  mkdirSync(d, { recursive: true });
}

const PORT = Number(process.env.MICRO_PASS_06_PORT || 4730);
const CHROME = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const VIEWPORT_W = 1437;
const approvedPngPath =
  "X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/26.06.2026/О центре - десктоп.png";

const approvedBytes = readFileSync(approvedPngPath);
const approvedHash = createHash("sha256").update(approvedBytes).digest("hex").toUpperCase();
const EXPECTED_HASH = "4A3B0D1E47F00738A669A1C18FC7A51DBBD6E660765414B81062A235FDFFB424";
if (approvedHash !== EXPECTED_HASH) {
  console.error("FP0002_OCENTRE_PROGRAM_PNG_AUTHORITY_MISMATCH");
  process.exit(2);
}

// Figma: program 1:2401 y=4639 h=1519; infra 1:2440 y=6158
const DESIGN_CROP = { x: 0, y: 4480, width: 1437, height: 1780 };
const RUNTIME_CONTEXT_ABOVE = 160;
const RUNTIME_CONTEXT_BELOW = 120;

const phase = process.argv[2] || "before";
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
      new Promise((r) => setTimeout(r, 5000)),
    ]);
    const max = document.documentElement.scrollHeight;
    for (let y = 0; y < max; y += 700) {
      window.scrollTo(0, y);
      await new Promise((r) => setTimeout(r, 120));
    }
    const program = document.querySelector("#our-program");
    if (program) {
      program.scrollIntoView({ block: "center" });
      await new Promise((r) => setTimeout(r, 250));
      for (const img of program.querySelectorAll("img")) {
        img.scrollIntoView({ block: "center", inline: "center" });
        void img.offsetHeight;
        if (typeof img.decode === "function") {
          try {
            await img.decode();
          } catch {
            /* ignore decode errors */
          }
        }
        await new Promise((r) => setTimeout(r, 120));
      }
    }
    window.scrollTo(0, 0);
    await new Promise((r) => setTimeout(r, 500));
  });
}

async function getRuntimeCropBox(page) {
  return page.evaluate(
    ({ above, below }) => {
      const clinic = document.querySelector(".clinic-landscape");
      const program = document.querySelector("#our-program");
      const infra = document.querySelector("#our-home");
      if (!program) return null;
      const py = (el) => {
        const r = el.getBoundingClientRect();
        return {
          top: r.top + window.scrollY,
          bottom: r.bottom + window.scrollY,
          height: r.height,
          width: r.width,
        };
      };
      const cs = (el, props) => {
        const s = getComputedStyle(el);
        return Object.fromEntries(props.map((p) => [p, s.getPropertyValue(p)]));
      };
      const pp = py(program);
      const cp = clinic ? py(clinic) : null;
      const ip = infra ? py(infra) : null;
      const head = program.querySelector(".services-program-v2__head");
      const lead = program.querySelector(".services-program-v2__lead");
      const intro = program.querySelector(".services-program-v2__intro");
      const intro2 = program.querySelector(".services-program-v2__intro--continued");
      const grid = program.querySelector(".services-program-v2__grid");
      const items = [...program.querySelectorAll(".services-program-v2__item")];
      const top = cp ? Math.max(cp.bottom - above, cp.top) : pp.top - above;
      const bottom = ip ? Math.min(pp.bottom + below, ip.top + below) : pp.bottom + below;
      return {
        x: 0,
        y: Math.round(Math.max(0, top)),
        width: window.innerWidth,
        height: Math.round(Math.max(1, bottom - top)),
        program: pp,
        clinic: cp,
        infra: ip,
        spacing_clinic_to_program: cp ? pp.top - cp.bottom : null,
        spacing_program_to_infra: ip ? ip.top - pp.bottom : null,
        head: head ? py(head) : null,
        lead: lead ? py(lead) : null,
        intro: intro ? py(intro) : null,
        intro2: intro2 ? py(intro2) : null,
        grid: grid ? { ...py(grid), ...cs(grid, ["gap", "grid-template-columns"]) } : null,
        cards: items.map((item, i) => {
          const media = item.querySelector(".services-program-v2__item-media");
          const img = item.querySelector("img");
          const title = item.querySelector(".services-program-v2__item-title");
          return {
            index: i + 1,
            item: py(item),
            title: title ? py(title) : null,
            media: media ? { ...py(media), ...cs(media, ["height", "border-radius"]) } : null,
            image: img
              ? {
                  ...py(img),
                  src: img.getAttribute("src")?.split("/").pop(),
                  natural: { w: img.naturalWidth, h: img.naturalHeight },
                  ...cs(img, ["object-fit", "object-position", "border-radius"]),
                }
              : null,
          };
        }),
      };
    },
    { above: RUNTIME_CONTEXT_ABOVE, below: RUNTIME_CONTEXT_BELOW },
  );
}

async function captureRuntimeCrop(page, outPath, fullPath) {
  await page.setViewport({ width: VIEWPORT_W, height: 900, deviceScaleFactor: 1 });
  await page.goto(previewUrl, { waitUntil: "load", timeout: 60000 });
  await waitImages(page);
  await page.screenshot({ path: fullPath, fullPage: true });
  const programShot = fullPath.replace("-full.png", "-program-element.png");
  const programEl = await page.$("#our-program");
  if (programEl) {
    await programEl.screenshot({ path: programShot });
  }
  const box = await getRuntimeCropBox(page);
  if (!box) throw new Error("runtime crop box missing");
  const py = join(tempDir, "micro-pass-06-runtime-crop.py");
  writeFileSync(
    py,
    `"""Crop runtime full-page PNG to micro-pass-06 region."""
import json, sys
from pathlib import Path
from PIL import Image
full_path, out_path = Path(sys.argv[1]), Path(sys.argv[2])
x, y, w, h = (int(sys.argv[i]) for i in range(3, 7))
img = Image.open(full_path)
h = min(h, img.height - y)
cropped = img.crop((x, y, x + w, y + h))
out_path.parent.mkdir(parents=True, exist_ok=True)
cropped.save(out_path)
print(json.dumps({"crop": str(out_path), "box": [x, y, w, h], "size": cropped.size}))
`,
  );
  const result = spawnSync(
    "python",
    [py, fullPath, outPath, String(box.x), String(box.y), String(box.width), String(box.height)],
    { encoding: "utf-8" },
  );
  if (result.status !== 0) throw new Error(result.stderr || result.stdout);
  return box;
}

async function diagnose(page) {
  await page.setViewport({ width: VIEWPORT_W, height: 900, deviceScaleFactor: 1 });
  await page.goto(previewUrl, { waitUntil: "load", timeout: 60000 });
  await waitImages(page);
  return page.evaluate(() => {
    const program = document.querySelector("#our-program");
    const items = [...document.querySelectorAll("#our-program .services-program-v2__item")];
    const imgs = [...document.querySelectorAll("#our-program img")].map((img) => ({
      src: img.getAttribute("src")?.split("/").pop(),
      complete: img.complete,
      natural: { w: img.naturalWidth, h: img.naturalHeight },
      rect: img.getBoundingClientRect(),
      opacity: getComputedStyle(img).opacity,
    }));
    const ids = [...document.querySelectorAll("[id]")].map((el) => el.id);
    const dup = ids.filter((id, i) => ids.indexOf(id) !== i);
    return {
      cardCount: items.length,
      programHeight: program?.getBoundingClientRect().height,
      programScrollY: program ? program.getBoundingClientRect().top + window.scrollY : null,
      images: imgs,
      duplicateIds: [...new Set(dup)],
      overflowX: document.documentElement.scrollWidth > window.innerWidth,
      consoleErrors: [],
    };
  });
}

async function makeSideBySide(page, designPath, beforePath, afterPath, outPath) {
  const toB64 = (p) => readFileSync(p).toString("base64");
  const html = `<!doctype html><html><body style="margin:0;background:#111;display:flex;gap:4px;align-items:flex-start">
    <div><div style="color:#fff;font:12px sans-serif;padding:4px">design</div><img src="data:image/png;base64,${toB64(designPath)}" style="height:880px;width:auto"></div>
    <div><div style="color:#fff;font:12px sans-serif;padding:4px">before</div><img src="data:image/png;base64,${toB64(beforePath)}" style="height:880px;width:auto"></div>
    <div><div style="color:#fff;font:12px sans-serif;padding:4px">after</div><img src="data:image/png;base64,${toB64(afterPath)}" style="height:880px;width:auto"></div>
  </body></html>`;
  await page.setContent(html);
  await page.setViewport({ width: 4400, height: 960, deviceScaleFactor: 1 });
  await page.screenshot({ path: outPath, fullPage: true });
}

const browser = await puppeteer.launch({
  executablePath: CHROME,
  headless: true,
  args: ["--no-sandbox", "--disable-dev-shm-usage"],
});
const page = await browser.newPage();
let consoleErrors = [];
page.on("pageerror", (e) => consoleErrors.push(String(e)));
page.on("console", (msg) => {
  if (msg.type() === "error") consoleErrors.push(msg.text());
});

const designCropPath = join(designDir, "o-centre-micro-pass-06-design-crop.png");
const designCropMeta = await cropDesignPng(page, designCropPath);

const meta = {
  task: "FP-0002 O-Centre Program Desktop Micro-Pass 06",
  approved_png_path: approvedPngPath,
  approved_png_sha256: approvedHash,
  approved_png_dimensions: "1437x12830",
  figma_frame: "1:2185",
  program_node: "1:2401",
  infra_node: "1:2440",
  figma_program_y: 4639,
  figma_program_h: 1519,
  visible_card_count: 4,
  visible_card_order: [
    "01 — Генотипирование",
    "02 — Нейропсихологическая коррекция",
    "03 — Психокоррекция",
    "04 — Кинезиотерапия",
  ],
  design_crop: { path: designCropPath, ...designCropMeta },
  viewport_px: VIEWPORT_W,
  preview_url: previewUrl,
};

try {
  if (phase === "before") {
    const beforeCrop = join(beforeDir, "o-centre-micro-pass-06-runtime-before.png");
    const beforeFull = join(beforeDir, "o-centre-micro-pass-06-runtime-before-full.png");
    const runtimeBox = await captureRuntimeCrop(page, beforeCrop, beforeFull);
    const diag = await diagnose(page);
    diag.consoleErrors = consoleErrors;
    meta.runtime_before = beforeCrop;
    meta.runtime_crop_box = runtimeBox;
    meta.diagnosis = diag;
    meta.program_height_delta_vs_figma = diag.programHeight - 1519;
    writeFileSync(join(evidenceDir, "micro-pass-06-before-meta.json"), JSON.stringify(meta, null, 2));
    console.log(JSON.stringify({ phase: "before", ...meta }, null, 2));
  } else {
    const beforeCrop = join(beforeDir, "o-centre-micro-pass-06-runtime-before.png");
    const afterCrop = join(afterDir, "o-centre-micro-pass-06-runtime-after.png");
    const afterFull = join(afterDir, "o-centre-micro-pass-06-runtime-after-full.png");
    const runtimeBox = await captureRuntimeCrop(page, afterCrop, afterFull);
    const diag = await diagnose(page);
    diag.consoleErrors = consoleErrors;
    const sideBySide = join(evidenceDir, "o-centre-micro-pass-06-side-by-side.png");
    await makeSideBySide(page, designCropPath, beforeCrop, afterCrop, sideBySide);
    meta.runtime_after = afterCrop;
    meta.runtime_crop_box = runtimeBox;
    meta.side_by_side = sideBySide;
    meta.diagnosis_after = diag;
    meta.program_height_delta_vs_figma = diag.programHeight - 1519;
    writeFileSync(join(evidenceDir, "micro-pass-06-after-meta.json"), JSON.stringify(meta, null, 2));
    console.log(JSON.stringify({ phase: "after", ...meta }, null, 2));
  }
} finally {
  await browser.close();
}
