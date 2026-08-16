const fs = require('fs');
const path = require('path');

const OUT = process.argv[2] || path.join(__dirname, 'readmore-probe-result.json');

async function getBrowser() {
  try {
    const { chromium } = require('playwright');
    return { kind: 'playwright', browser: await chromium.launch({ headless: true }) };
  } catch (e) {
    // try puppeteer
  }
  try {
    const puppeteer = require('puppeteer');
    return { kind: 'puppeteer', browser: await puppeteer.launch({ headless: true }) };
  } catch (e) {
    // try system chrome with playwright-core
  }
  const chromeCandidates = [
    'C:\\\\Program Files\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe',
    'C:\\\\Program Files (x86)\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe',
    process.env.LOCALAPPDATA + '\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe',
    'C:\\\\Program Files\\\\Microsoft\\\\Edge\\\\Application\\\\msedge.exe',
  ];
  let executablePath = null;
  for (const c of chromeCandidates) {
    if (c && fs.existsSync(c)) { executablePath = c; break; }
  }
  if (!executablePath) throw new Error('No browser found');
  try {
    const { chromium } = require('playwright-core');
    return { kind: 'playwright-core', browser: await chromium.launch({ headless: true, executablePath }) };
  } catch (e) {
    const puppeteer = require('puppeteer-core');
    return { kind: 'puppeteer-core', browser: await puppeteer.launch({ headless: true, executablePath }) };
  }
}

async function measurePage(page, url) {
  const consoleErrors = [];
  page.on('pageerror', (err) => consoleErrors.push(String(err)));
  page.on('console', (msg) => {
    if (msg.type() === 'error') consoleErrors.push(msg.text());
  });

  const resp = await page.goto(url, { waitUntil: 'networkidle', timeout: 60000 });
  await page.waitForTimeout(400);

  const initial = await page.evaluate(() => {
    const root = document.querySelector('.service-leaf-signs-v1');
    const editorial = document.querySelector('.service-leaf-signs-v1__editorial');
    const button = document.querySelector('.service-leaf-signs-v1__read-more');
    if (!root || !editorial) {
      return { present: false };
    }
    const cs = getComputedStyle(editorial);
    const lh = parseFloat(cs.lineHeight) || (parseFloat(cs.fontSize) * 1.5);
    return {
      present: true,
      hasButton: !!button,
      buttonHidden: button ? button.hidden || getComputedStyle(button).display === 'none' : true,
      ariaExpanded: button ? button.getAttribute('aria-expanded') : null,
      isClamped: editorial.classList.contains('is-clamped'),
      isExpanded: editorial.classList.contains('is-expanded'),
      clientHeight: editorial.clientHeight,
      scrollHeight: editorial.scrollHeight,
      lineHeight: lh,
      fiveLines: lh * 5,
      overflow: editorial.scrollHeight > editorial.clientHeight + 2,
      textLen: (editorial.textContent || '').trim().length,
    };
  });

  let afterClick = null;
  if (initial.present && initial.hasButton && !initial.buttonHidden) {
    await page.click('.service-leaf-signs-v1__read-more');
    await page.waitForTimeout(550);
    afterClick = await page.evaluate(() => {
      const editorial = document.querySelector('.service-leaf-signs-v1__editorial');
      const button = document.querySelector('.service-leaf-signs-v1__read-more');
      return {
        buttonHidden: button ? button.hidden || getComputedStyle(button).display === 'none' : true,
        ariaExpanded: button ? button.getAttribute('aria-expanded') : null,
        isClamped: editorial.classList.contains('is-clamped'),
        isExpanded: editorial.classList.contains('is-expanded'),
        clientHeight: editorial.clientHeight,
        scrollHeight: editorial.scrollHeight,
        overflow: editorial.scrollHeight > editorial.clientHeight + 2,
      };
    });
  }

  // Short-text simulation without DB mutation
  let shortText = null;
  if (initial.present) {
    shortText = await page.evaluate(() => {
      const editorial = document.querySelector('.service-leaf-signs-v1__editorial');
      const button = document.querySelector('.service-leaf-signs-v1__read-more');
      if (!editorial || !button) return { ok: false };
      editorial.textContent = 'Короткий текст.';
      button.hidden = false;
      button._signsReadMoreExpanded = false;
      editorial.classList.remove('is-clamped', 'is-expanded', 'is-animated');
      editorial.style.removeProperty('--signs-editorial-clamp-height');
      editorial.style.removeProperty('--signs-editorial-full-height');
      editorial.style.maxHeight = '';
      // re-trigger resize handler via dispatch
      window.dispatchEvent(new Event('resize'));
      return new Promise((resolve) => {
        setTimeout(() => {
          const cs = getComputedStyle(editorial);
          const lh = parseFloat(cs.lineHeight) || (parseFloat(cs.fontSize) * 1.5);
          resolve({
            ok: true,
            buttonHidden: button.hidden || getComputedStyle(button).display === 'none',
            isClamped: editorial.classList.contains('is-clamped'),
            clientHeight: editorial.clientHeight,
            scrollHeight: editorial.scrollHeight,
            fiveLines: lh * 5,
            overflow: editorial.scrollHeight > lh * 5 + 2,
          });
        }, 200);
      });
    });
  }

  return {
    url,
    http: resp ? resp.status() : null,
    consoleErrors,
    initial,
    afterClick,
    shortText,
  };
}

(async () => {
  const pack = await getBrowser();
  const browser = pack.browser;
  const page = await browser.newPage();
  const results = {
    kind: pack.kind,
    alcohol: await measurePage(page, 'http://shpigovsky.test/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/'),
    p314: null,
    p78: null,
    home: null,
    uslugi: null,
    zavisimosti: null,
  };

  // lighter checks for other pages
  async function smoke(url) {
    const consoleErrors = [];
    page.removeAllListeners('pageerror');
    page.removeAllListeners('console');
    page.on('pageerror', (err) => consoleErrors.push(String(err)));
    const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
    await page.waitForTimeout(200);
    const hasSigns = await page.evaluate(() => !!document.querySelector('.service-leaf-signs-v1'));
    return { url, http: resp ? resp.status() : null, hasSigns, consoleErrors };
  }

  results.p314 = await smoke('http://shpigovsky.test/?p=314');
  results.p78 = await smoke('http://shpigovsky.test/?p=78');
  results.zavisimosti = await smoke('http://shpigovsky.test/uslugi/zavisimosti/');
  results.uslugi = await smoke('http://shpigovsky.test/uslugi/');
  results.home = await smoke('http://shpigovsky.test/');

  fs.writeFileSync(OUT, JSON.stringify(results, null, 2), 'utf8');
  console.log(JSON.stringify(results, null, 2));
  await browser.close();
})().catch((err) => {
  console.error(String(err && err.stack || err));
  process.exit(1);
});
