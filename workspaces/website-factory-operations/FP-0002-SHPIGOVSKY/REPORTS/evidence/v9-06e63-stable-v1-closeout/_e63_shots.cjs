const { chromium } = require("playwright");
const fs = require("fs");
const path = require("path");
(async () => {
  const out = process.env.EVDIR;
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  const consoleErrors = [];
  const pageErrors = [];
  page.on("pageerror", (e) => pageErrors.push(String(e)));
  page.on("console", (m) => { if (m.type() === "error") consoleErrors.push(m.text()); });

  async function probe(name, url, w, h, opts = {}) {
    await page.setViewportSize({ width: w, height: h });
    const resp = await page.goto(url, { waitUntil: "domcontentloaded", timeout: 60000 });
    await page.waitForTimeout(500);
    if (opts.scrollY) { await page.evaluate(y => window.scrollTo(0,y), opts.scrollY); await page.waitForTimeout(400); }
    if (opts.openSearch) { const t = page.locator("[data-search-toggle]"); if (await t.count()) { await t.first().click(); await page.waitForTimeout(300); } }
    const overflow = await page.evaluate(() => {
      const doc = document.documentElement;
      return Math.max(doc.scrollWidth, document.body.scrollWidth) > Math.ceil(window.innerWidth) + 1;
    });
    const brokenAssets = await page.evaluate(() => {
      const bad = [];
      document.querySelectorAll("img[src],link[href],script[src]").forEach(el => {
        const u = el.src || el.href;
        if (!u) return;
        if (u.includes("localhost") || u.includes("shpigovsky.test") || u.startsWith("/")) {
          // checked via network below
        }
      });
      return bad;
    });
    await page.screenshot({ path: path.join(out, name + ".png"), fullPage: !!opts.fullPage });
    return { name, url, w, h, status: resp ? resp.status() : null, overflow, console_errors_so_far: consoleErrors.length, page_errors_so_far: pageErrors.length };
  }

  const results = [];
  const viewports = [[1440,900],[1024,768],[480,900],[370,812]];
  // Critical CSS-affected + priority routes at 1440; mobile subset
  const critical = [
    ["home", "http://shpigovsky.test/", false],
    ["uslugi", "http://shpigovsky.test/uslugi/", true],
    ["service-alcohol", "http://shpigovsky.test/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/", true],
    ["ocentre", "http://shpigovsky.test/o-centre/", true],
    ["program-child", "http://shpigovsky.test/o-centre/programma-lecheniya/genotipirovanie/", true],
    ["contacts", "http://shpigovsky.test/kontakty/", false],
    ["blog", "http://shpigovsky.test/blog/", false],
    ["reviews", "http://shpigovsky.test/otzyvy/", false],
    ["search-blank", "http://shpigovsky.test/?s=", true],
    ["search-results", "http://shpigovsky.test/?s=%D0%B0", true],
    ["search-page2", "http://shpigovsky.test/page/2/?s=%D0%B0", true],
    ["search-empty", "http://shpigovsky.test/?s=zzznomatchxyz", true],
    ["404", "http://shpigovsky.test/this-route-does-not-exist-e63-404/", false],
    ["specialist", "http://shpigovsky.test/specyalisty/shipovsky/", false],
    ["legal", "http://shpigovsky.test/privacy-policy/", false],
  ];

  for (const [name, url, full] of critical) {
    results.push(await probe(`${name}__1440x900`, url, 1440, 900, { fullPage: full }));
  }
  // mobile overflow checks on key pages
  for (const [w,h] of [[480,900],[370,812]]) {
    for (const [name, url] of [["home","http://shpigovsky.test/"],["search","http://shpigovsky.test/?s="],["uslugi","http://shpigovsky.test/uslugi/"],["404","http://shpigovsky.test/this-route-does-not-exist-e63-404/"]]) {
      results.push(await probe(`${name}__${w}x${h}`, url, w, h, { fullPage: false }));
    }
  }
  // desktop search open
  results.push(await probe("desktop-search-open__1440x900", "http://shpigovsky.test/", 1440, 900, { openSearch: true }));

  fs.writeFileSync(path.join(out, "screenshot-probe-matrix.json"), JSON.stringify({ results, consoleErrors, pageErrors }, null, 2));
  console.log(JSON.stringify({ shots: results.length, overflow: results.filter(r=>r.overflow).length, consoleErrors: consoleErrors.length, pageErrors: pageErrors.length }, null, 2));
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
