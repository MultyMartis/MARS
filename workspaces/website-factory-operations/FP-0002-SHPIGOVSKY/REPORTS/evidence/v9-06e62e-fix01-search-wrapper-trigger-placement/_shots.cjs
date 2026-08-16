const { chromium } = require("playwright");
const fs = require("fs");
const path = require("path");

(async () => {
  const out = process.env.EVDIR;
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  const consoleErrors = [];
  page.on("pageerror", (err) => consoleErrors.push(String(err)));
  page.on("console", (msg) => {
    if (msg.type() === "error") consoleErrors.push(msg.text());
  });

  async function shot(name, url, w, h, opts = {}) {
    await page.setViewportSize({ width: w, height: h });
    await page.goto(url, { waitUntil: "networkidle", timeout: 60000 });
    if (opts.scrollY) {
      await page.evaluate((y) => window.scrollTo(0, y), opts.scrollY);
      await page.waitForTimeout(600);
    }
    if (opts.openOffcanvas) {
      await page.click("[data-offcanvas-open]");
      await page.waitForTimeout(400);
    }
    if (opts.openSearch) {
      const toggle = page.locator('[data-search-toggle]');
      await toggle.first().click();
      await page.waitForTimeout(400);
    }
    await page.screenshot({
      path: path.join(out, name),
      fullPage: !!opts.fullPage,
    });
    console.log("shot", name);
  }

  // Breadcrumb / blank search pages
  await shot("search-results-1440.png", "http://shpigovsky.test/?s=%D0%B0%D0%BB%D0%BA%D0%BE%D0%B3%D0%BE%D0%BB%D1%8C", 1440, 900, { fullPage: true });
  await shot("search-no-results-1440.png", "http://shpigovsky.test/?s=zzzznotfoundxyz", 1440, 900, { fullPage: true });
  await shot("search-blank-1440.png", "http://shpigovsky.test/?s=", 1440, 900, { fullPage: true });
  await shot("search-pagination-1440.png", "http://shpigovsky.test/page/2/?s=%D0%B7%D0%B0%D0%B2%D0%B8%D1%81%D0%B8%D0%BC", 1440, 900, { fullPage: true });

  // Desktop header + search dropdown
  await shot("desktop-header-1440.png", "http://shpigovsky.test/", 1440, 900);
  await shot("desktop-search-open-1440.png", "http://shpigovsky.test/", 1440, 900, { openSearch: true });

  // Floating header (scrolled) — no search
  await shot("floating-header-1440.png", "http://shpigovsky.test/", 1440, 900, { scrollY: 900 });

  // Mobile header — no search
  await shot("mobile-header-1024.png", "http://shpigovsky.test/", 1024, 768);
  await shot("mobile-header-480.png", "http://shpigovsky.test/", 480, 900);
  await shot("mobile-header-370.png", "http://shpigovsky.test/", 370, 812);

  // Offcanvas search link
  await shot("offcanvas-search-1024.png", "http://shpigovsky.test/", 1024, 768, { openOffcanvas: true });
  await shot("offcanvas-search-480.png", "http://shpigovsky.test/", 480, 900, { openOffcanvas: true });
  await shot("offcanvas-search-370.png", "http://shpigovsky.test/", 370, 812, { openOffcanvas: true });

  // JS interaction matrix
  const matrix = [];
  async function check(label, fn) {
    try {
      const ok = await fn();
      matrix.push({ label, ok: !!ok, detail: ok === true ? "PASS" : String(ok) });
    } catch (e) {
      matrix.push({ label, ok: false, detail: String(e.message || e) });
    }
  }

  await page.setViewportSize({ width: 1440, height: 900 });
  await page.goto("http://shpigovsky.test/", { waitUntil: "networkidle", timeout: 60000 });

  await check("desktop_toggle_count", async () => {
    const n = await page.locator("[data-search-toggle]").count();
    return n === 1 ? true : `count=${n}`;
  });
  await check("desktop_open_focus", async () => {
    await page.click("[data-search-toggle]");
    await page.waitForTimeout(200);
    const focused = await page.evaluate(() => {
      const el = document.activeElement;
      return !!(el && (el.matches('input[name="s"]') || el.matches("[data-search-focus]")));
    });
    const open = await page.locator('[data-search-panel][data-search-state="open"]').count();
    return focused && open === 1;
  });
  await check("desktop_escape_closes", async () => {
    await page.keyboard.press("Escape");
    await page.waitForTimeout(150);
    const open = await page.locator('[data-search-panel][data-search-state="open"]').count();
    return open === 0;
  });

  await page.setViewportSize({ width: 1024, height: 768 });
  await page.goto("http://shpigovsky.test/", { waitUntil: "networkidle", timeout: 60000 });
  await check("mobile_no_visible_search_toggle", async () => {
    const visible = await page.locator("[data-search-toggle]").evaluateAll((els) =>
      els.filter((el) => {
        const s = window.getComputedStyle(el);
        const r = el.getBoundingClientRect();
        return s.display !== "none" && s.visibility !== "hidden" && r.width > 0 && r.height > 0;
      }).length
    );
    // Parent may hide via display:none on .site-header__bottom
    const parentHidden = await page.locator(".site-header__bottom").evaluate((el) => getComputedStyle(el).display === "none");
    return visible === 0 || parentHidden;
  });
  await check("mobile_no_header_search_button", async () => {
    return (await page.locator(".site-header__search--mobile, .fp02-floating-header__search").count()) === 0;
  });
  await check("offcanvas_search_link", async () => {
    await page.click("[data-offcanvas-open]");
    await page.waitForTimeout(300);
    const href = await page.locator("a.offcanvas__nav-link--search").getAttribute("href");
    return href && /[?&]s=/.test(href) ? true : `href=${href}`;
  });
  await check("offcanvas_search_navigates_blank", async () => {
    await page.click("a.offcanvas__nav-link--search");
    await page.waitForLoadState("networkidle");
    const url = page.url();
    const instr = await page.locator(".page-search__summary").innerText();
    const cards = await page.locator(".search-result-card").count();
    return /[?&]s=/.test(url) && /Введите поисковый запрос/.test(instr) && cards === 0;
  });

  await page.setViewportSize({ width: 1440, height: 900 });
  await page.goto("http://shpigovsky.test/", { waitUntil: "networkidle", timeout: 60000 });
  await page.evaluate(() => window.scrollTo(0, 1200));
  await page.waitForTimeout(700);
  await check("floating_no_search", async () => {
    const floating = page.locator("[data-fp02-floating-header].is-visible");
    const visible = await floating.count();
    const search = await page.locator(".fp02-floating-header__search").count();
    return visible > 0 && search === 0;
  });

  // Overflow spot-check
  await check("no_horizontal_overflow_home_1440", async () => {
    await page.goto("http://shpigovsky.test/", { waitUntil: "networkidle" });
    return page.evaluate(() => document.documentElement.scrollWidth <= document.documentElement.clientWidth + 1);
  });
  await check("no_horizontal_overflow_search_blank_480", async () => {
    await page.setViewportSize({ width: 480, height: 900 });
    await page.goto("http://shpigovsky.test/?s=", { waitUntil: "networkidle" });
    return page.evaluate(() => document.documentElement.scrollWidth <= document.documentElement.clientWidth + 1);
  });

  fs.writeFileSync(path.join(out, "js-interaction-matrix.json"), JSON.stringify({ matrix, consoleErrors }, null, 2));
  console.log("matrix", JSON.stringify(matrix, null, 2));
  console.log("consoleErrors", consoleErrors.length);
  await browser.close();
})().catch((e) => {
  console.error(e);
  process.exit(1);
});
