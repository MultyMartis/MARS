const puppeteer = require('puppeteer');
const path = require('path');

const evidence = String.raw`X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\REPORTS\evidence\v9-06e62a-404-breadcrumb-wrapper-phone-mask\screenshots`;

(async () => {
  const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
  const page = await browser.newPage();
  const widths = [1440, 1024, 480, 370];
  const heights = { 1440: 900, 1024: 768, 480: 900, 370: 812 };

  for (const w of widths) {
    await page.setViewport({ width: w, height: heights[w], deviceScaleFactor: 1 });
    await page.goto('http://shpigovsky.test/this-page-definitely-does-not-exist-e62a/', {
      waitUntil: 'networkidle2',
      timeout: 60000,
    });
    await page.screenshot({ path: path.join(evidence, `404-${w}.png`), fullPage: true });
    console.log('shot 404', w);
  }

  await page.setViewport({ width: 1440, height: 900 });
  await page.goto('http://shpigovsky.test/o-centre/galereya-o-dome/', {
    waitUntil: 'networkidle2',
    timeout: 60000,
  });
  await page.screenshot({ path: path.join(evidence, 'galereya-1440.png'), fullPage: false });

  for (const w of [1440, 480]) {
    await page.setViewport({ width: w, height: w === 1440 ? 900 : 900 });
    await page.goto('http://shpigovsky.test/', { waitUntil: 'networkidle2', timeout: 60000 });
    await page.click('[data-modal-open="consultation"]');
    await page.waitForSelector('#modal-consultation-phone', { visible: true });
    await page.click('#modal-consultation-phone', { clickCount: 3 });
    await page.type('#modal-consultation-phone', '9991234567');
    const val = await page.$eval('#modal-consultation-phone', (el) => el.value);
    console.log('MASKED', w, val);
    await page.screenshot({ path: path.join(evidence, `phone-modal-masked-${w}.png`) });

    await page.click('#modal-consultation-phone', { clickCount: 3 });
    await page.keyboard.press('Backspace');
    await page.type('#modal-consultation-phone', '89991234567');
    const val8 = await page.$eval('#modal-consultation-phone', (el) => el.value);
    console.log('MASKED8', w, val8);

    await page.click('#modal-consultation-phone', { clickCount: 3 });
    await page.keyboard.press('Backspace');
    await page.type('#modal-consultation-phone', '+79991234567');
    const valPlus = await page.$eval('#modal-consultation-phone', (el) => el.value);
    console.log('MASKEDPLUS', w, valPlus);

    // incomplete should not look like complete 11-digit
    await page.click('#modal-consultation-phone', { clickCount: 3 });
    await page.keyboard.press('Backspace');
    await page.type('#modal-consultation-phone', '999');
    const incomplete = await page.$eval('#modal-consultation-phone', (el) => el.value);
    const digits = incomplete.replace(/\D/g, '');
    console.log('INCOMPLETE', w, incomplete, 'digits', digits.length);
  }

  // overflow check on 404
  await page.setViewport({ width: 370, height: 812 });
  await page.goto('http://shpigovsky.test/this-page-definitely-does-not-exist-e62a/', {
    waitUntil: 'networkidle2',
    timeout: 60000,
  });
  const overflow = await page.evaluate(() => {
    const doc = document.documentElement;
    return {
      scrollWidth: doc.scrollWidth,
      clientWidth: doc.clientWidth,
      overflowX: doc.scrollWidth > doc.clientWidth + 1,
    };
  });
  console.log('OVERFLOW_404_370', JSON.stringify(overflow));

  const jsErrors = [];
  page.on('pageerror', (err) => jsErrors.push(String(err)));
  await page.goto('http://shpigovsky.test/', { waitUntil: 'networkidle2', timeout: 60000 });
  await page.goto('http://shpigovsky.test/this-page-definitely-does-not-exist-e62a/', {
    waitUntil: 'networkidle2',
    timeout: 60000,
  });
  console.log('JS_ERRORS', jsErrors.length, jsErrors.join(' | '));

  await browser.close();
  console.log('SCREENSHOTS_DONE');
})().catch((e) => {
  console.error(e);
  process.exit(1);
});
