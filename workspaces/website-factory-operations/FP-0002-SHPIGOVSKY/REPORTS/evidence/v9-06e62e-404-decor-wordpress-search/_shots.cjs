const { chromium } = require("playwright");
(async () => {
  const out = process.env.EVDIR;
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  const shots = [
    ["404-1440x900.png", "http://shpigovsky.test/missing-e62e/", 1440, 900],
    ["404-1024x768.png", "http://shpigovsky.test/missing-e62e/", 1024, 768],
    ["404-480x900.png", "http://shpigovsky.test/missing-e62e/", 480, 900],
    ["404-370x812.png", "http://shpigovsky.test/missing-e62e/", 370, 812],
    ["search-results-1440.png", "http://shpigovsky.test/?s=%D0%B0%D0%BB%D0%BA%D0%BE%D0%B3%D0%BE%D0%BB%D1%8C", 1440, 900],
    ["search-no-results-1440.png", "http://shpigovsky.test/?s=zzzznotfoundxyz", 1440, 900],
    ["search-pagination-1440.png", "http://shpigovsky.test/?s=%D0%B7%D0%B0%D0%B2%D0%B8%D1%81%D0%B8%D0%BC", 1440, 900],
  ];
  for (const [name, url, w, h] of shots) {
    await page.setViewportSize({ width: w, height: h });
    await page.goto(url, { waitUntil: "networkidle", timeout: 60000 });
    await page.screenshot({ path: out + "/" + name, fullPage: true });
    console.log("shot", name);
  }
  // dropdown open on home
  await page.setViewportSize({ width: 1440, height: 900 });
  await page.goto("http://shpigovsky.test/", { waitUntil: "networkidle", timeout: 60000 });
  await page.click('[data-search-toggle]');
  await page.waitForTimeout(400);
  await page.screenshot({ path: out + "/search-dropdown-open-1440.png", fullPage: false });
  console.log("shot dropdown");
  await browser.close();
})().catch((e) => { console.error(e); process.exit(1); });
