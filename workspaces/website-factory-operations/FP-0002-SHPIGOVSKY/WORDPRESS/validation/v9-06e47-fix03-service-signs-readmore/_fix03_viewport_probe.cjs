const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright-core');

const chromeCandidates = [
  'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
  'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
  process.env.LOCALAPPDATA + '\\Google\\Chrome\\Application\\chrome.exe',
  'C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe',
];
let executablePath = chromeCandidates.find((c) => c && fs.existsSync(c));

async function probe(viewport) {
  const browser = await chromium.launch({ headless: true, executablePath });
  const page = await browser.newPage({ viewport });
  const consoleErrors = [];
  page.on('pageerror', (e) => consoleErrors.push(String(e)));
  await page.goto('http://shpigovsky.test/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/', {
    waitUntil: 'networkidle',
    timeout: 60000,
  });
  await page.waitForTimeout(500);
  const initial = await page.evaluate(() => {
    const editorial = document.querySelector('.service-leaf-signs-v1__editorial');
    const button = document.querySelector('.service-leaf-signs-v1__read-more');
    const cs = getComputedStyle(editorial);
    const lh = parseFloat(cs.lineHeight) || (parseFloat(cs.fontSize) * 1.5);
    return {
      clientHeight: editorial.clientHeight,
      scrollHeight: editorial.scrollHeight,
      lineHeight: lh,
      fiveLines: lh * 5,
      isClamped: editorial.classList.contains('is-clamped'),
      buttonHidden: button.hidden || getComputedStyle(button).display === 'none',
      buttonTag: button.tagName,
      ariaExpanded: button.getAttribute('aria-expanded'),
      textWidth: editorial.getBoundingClientRect().width,
    };
  });

  let afterClick = null;
  if (!initial.buttonHidden) {
    await page.click('.service-leaf-signs-v1__read-more');
    await page.waitForTimeout(600);
    afterClick = await page.evaluate(() => {
      const editorial = document.querySelector('.service-leaf-signs-v1__editorial');
      const button = document.querySelector('.service-leaf-signs-v1__read-more');
      return {
        clientHeight: editorial.clientHeight,
        scrollHeight: editorial.scrollHeight,
        isClamped: editorial.classList.contains('is-clamped'),
        buttonHidden: button.hidden || getComputedStyle(button).display === 'none',
        ariaExpanded: button.getAttribute('aria-expanded'),
      };
    });
  }

  // Artificial long text to force overflow without DB write
  const forced = await page.evaluate(async () => {
    const editorial = document.querySelector('.service-leaf-signs-v1__editorial');
    const button = document.querySelector('.service-leaf-signs-v1__read-more');
    editorial.textContent = Array(40).fill('Длинная строка редакционного текста для проверки clamp и кнопки читать больше.').join(' ');
    button._signsReadMoreExpanded = false;
    button.hidden = false;
    editorial.classList.remove('is-clamped', 'is-expanded', 'is-animated');
    editorial.style.removeProperty('--signs-editorial-clamp-height');
    editorial.style.removeProperty('--signs-editorial-full-height');
    editorial.style.maxHeight = '';
    window.dispatchEvent(new Event('resize'));
    await new Promise((r) => setTimeout(r, 250));
    const before = {
      isClamped: editorial.classList.contains('is-clamped'),
      buttonHidden: button.hidden || getComputedStyle(button).display === 'none',
      clientHeight: editorial.clientHeight,
      scrollHeight: editorial.scrollHeight,
      ariaExpanded: button.getAttribute('aria-expanded'),
    };
    if (!before.buttonHidden) {
      button.click();
      await new Promise((r) => setTimeout(r, 550));
    }
    const after = {
      isClamped: editorial.classList.contains('is-clamped'),
      buttonHidden: button.hidden || getComputedStyle(button).display === 'none',
      clientHeight: editorial.clientHeight,
      scrollHeight: editorial.scrollHeight,
      ariaExpanded: button.getAttribute('aria-expanded'),
      overflow: editorial.scrollHeight > editorial.clientHeight + 2,
    };
    return { before, after };
  });

  await browser.close();
  return { viewport, consoleErrors, initial, afterClick, forced };
}

(async () => {
  const out = {
    desktop: await probe({ width: 1440, height: 900 }),
    tablet: await probe({ width: 768, height: 1024 }),
    mobile: await probe({ width: 390, height: 844 }),
  };
  fs.writeFileSync(path.join(__dirname, 'readmore-viewport-probe.json'), JSON.stringify(out, null, 2));
  console.log(JSON.stringify(out, null, 2));
})();
