const { chromium } = require("playwright");
const path = require("path");
const fs = require("fs");

const baseUrl = "http://127.0.0.1:4174";
const outDir = path.join(__dirname, "screenshots");
fs.mkdirSync(outDir, { recursive: true });

const shots = [
  { file: "SERVICES-V2-CONTENT-FIDELITY-FULL-1398.png", width: 1398, height: 900, full: true },
  { file: "SERVICES-V2-CONTENT-FIDELITY-FULL-390.png", width: 390, height: 844, full: true },
  { file: "SERVICES-V2-CATEGORY-01-CONTENT-1398.png", width: 1398, selector: "#services-category-addictions" },
  { file: "SERVICES-V2-CATEGORY-01-CONTENT-390.png", width: 390, selector: "#services-category-addictions" },
  { file: "SERVICES-V2-CATEGORY-02-CONTENT-1398.png", width: 1398, selector: "#services-category-mental-health" },
  { file: "SERVICES-V2-CATEGORY-02-CONTENT-390.png", width: 390, selector: "#services-category-mental-health" },
  { file: "SERVICES-V2-CATEGORY-03-CONTENT-1398.png", width: 1398, selector: "#services-category-eating-disorders" },
  { file: "SERVICES-V2-CATEGORY-03-CONTENT-390.png", width: 390, selector: "#services-category-eating-disorders" },
  { file: "SERVICES-V2-CATEGORY-04-CONTENT-1398.png", width: 1398, selector: "#services-category-genotyping" },
  { file: "SERVICES-V2-CATEGORY-04-CONTENT-390.png", width: 390, selector: "#services-category-genotyping" },
  { file: "SERVICES-V1-CATEGORY-CONTENT-1398.png", width: 1398, url: "/uslugi.html", full: true },
  { file: "SERVICES-V1-CATEGORY-CONTENT-390.png", width: 390, url: "/uslugi.html", full: true },
  { file: "HOME-SMOKE-AFTER-SERVICES-V2-CONTENT-1398.png", width: 1398, url: "/index.html", full: true },
  { file: "HOME-SMOKE-AFTER-SERVICES-V2-CONTENT-390.png", width: 390, url: "/index.html", full: true },
];

(async () => {
  const browser = await chromium.launch();
  const report = [];
  for (const shot of shots) {
    const page = await browser.newPage({ viewport: { width: shot.width, height: shot.height || 900 } });
    const url = `${baseUrl}${shot.url || "/uslugi-v2.html"}`;
    await page.goto(url, { waitUntil: "networkidle" });
    const target = shot.selector ? page.locator(shot.selector) : page;
    await target.screenshot({ path: path.join(outDir, shot.file), fullPage: !!shot.full && !shot.selector });
    report.push({ file: shot.file, url, selector: shot.selector || "page", width: shot.width });
    await page.close();
  }
  // Transition + decor composites from V2 full page
  const page = await browser.newPage({ viewport: { width: 1398, height: 900 } });
  await page.goto(`${baseUrl}/uslugi-v2.html`, { waitUntil: "networkidle" });
  await page.screenshot({ path: path.join(outDir, "SERVICES-V2-CATEGORY-TRANSITIONS-1398.png"), fullPage: true });
  await page.setViewportSize({ width: 390, height: 844 });
  await page.screenshot({ path: path.join(outDir, "SERVICES-V2-CATEGORY-TRANSITIONS-390.png"), fullPage: true });
  for (const id of ["services-category-addictions", "services-category-mental-health", "services-category-eating-disorders", "services-category-genotyping"]) {
    const decor = page.locator(`#${id} .services-category-section-v2__decor`);
    if (await decor.count()) {
      await decor.screenshot({ path: path.join(outDir, `SERVICES-V2-DECOR-${id.split("-").pop()}-1398.png`) });
    }
  }
  await page.close();
  await browser.close();
  fs.writeFileSync(path.join(outDir, "capture-report.json"), JSON.stringify(report, null, 2));
  console.log("capture complete", report.length);
})();
