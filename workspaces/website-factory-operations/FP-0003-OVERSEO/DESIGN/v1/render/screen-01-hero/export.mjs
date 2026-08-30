import puppeteer from "puppeteer";
import path from "node:path";
import { fileURLToPath } from "node:url";
import fs from "node:fs";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const htmlPath = path.join(__dirname, "index.html");
const outputPath = path.join(__dirname, "..", "..", "exports", "SCREEN-01-HERO-DESKTOP-v1.png");

const browser = await puppeteer.launch({
  headless: true,
  args: ["--font-render-hinting=medium"],
});

try {
  const page = await browser.newPage();
  await page.setViewport({ width: 1920, height: 820, deviceScaleFactor: 1 });
  await page.goto(`file:///${htmlPath.replace(/\\/g, "/")}`, {
    waitUntil: "networkidle0",
  });
  await page.evaluateHandle("document.fonts.ready");

  const canvasHeight = await page.evaluate(() => {
    const canvas = document.querySelector(".design-canvas");
    return canvas ? Math.ceil(canvas.getBoundingClientRect().height) : 820;
  });

  await page.setViewport({ width: 1920, height: canvasHeight, deviceScaleFactor: 1 });

  await page.screenshot({
    path: outputPath,
    type: "png",
    clip: { x: 0, y: 0, width: 1920, height: canvasHeight },
  });

  console.log(`Exported: ${outputPath}`);
  console.log(`Dimensions: 1920 x ${canvasHeight}`);
} finally {
  await browser.close();
}
