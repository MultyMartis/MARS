/**
 * V5 Typography Live QA Pass 3 — headless line-break analyzer
 */
const puppeteer = require('puppeteer');
const path = require('path');

const INDEX = path.resolve(__dirname, '../dist/index.html');
const WIDTHS = [320, 375, 390, 420, 760, 1180, 1320, 1440];

const SELECTORS = [
  { key: 'h1', sel: '.hero__title' },
  { key: 'h2-section', sel: '.section-title' },
  { key: 'h2-transport', sel: '.machine-transport__heading' },
  { key: 'h2-faq', sel: '.faq__title' },
  { key: 'h2-cta', sel: '.contact-cta h2' },
  { key: 'h3-denied', sel: '.machine-transport__card h3' },
  { key: 'faq-summary', sel: '.faq-item summary' },
];

function analyzeText(text, lines) {
  const words = text.replace(/\s+/g, ' ').trim().split(' ');
  const issues = [];

  for (const line of lines) {
    const trimmed = line.trim();
    if (!trimmed) continue;
    if (/[а-яёА-ЯЁ]-$/.test(trimmed)) {
      issues.push({ type: 'mid-word-split', line: trimmed });
    }
    const lineWords = trimmed.split(/\s+/);
    if (lineWords.length === 1 && lineWords[0].length <= 5 && words.length >= 3 && !/^\d/.test(lineWords[0])) {
      issues.push({ type: 'orphan-word', line: trimmed });
    }
  }

  if (lines.length >= 2) {
    const last = lines[lines.length - 1].trim().split(/\s+/);
    if (last.length === 1 && words.length >= 4) {
      issues.push({ type: 'widow-word', line: lines[lines.length - 1].trim() });
    }
  }

  return issues;
}

(async () => {
  const browser = await puppeteer.launch({ headless: 'new' });
  const page = await browser.newPage();
  await page.goto('file:///' + INDEX.replace(/\\/g, '/'), { waitUntil: 'networkidle0' });

  const results = {};

  for (const width of WIDTHS) {
    await page.setViewport({ width, height: 900 });
    await new Promise((r) => setTimeout(r, 150));

    const pageOverflow = await page.evaluate(() => ({
      scrollW: document.documentElement.scrollWidth,
      clientW: document.documentElement.clientWidth,
      overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth + 1,
    }));

    results[width] = { overflow: pageOverflow, elements: {}, cards: null };

    for (const { key, sel } of SELECTORS) {
      const allIssues = await page.$$eval(sel, (els) =>
        els.map((el) => {
          const range = document.createRange();
          range.selectNodeContents(el);
          const lines = [];
          let currentTop = null;
          let currentText = '';

          const textNodes = [];
          const walk = (node) => {
            if (node.nodeType === Node.TEXT_NODE) textNodes.push(node);
            else node.childNodes.forEach(walk);
          };
          walk(el);

          for (const tn of textNodes) {
            const r = document.createRange();
            r.selectNodeContents(tn);
            for (const rect of r.getClientRects()) {
              if (rect.width === 0) continue;
              const top = Math.round(rect.top);
              if (currentTop === null || Math.abs(top - currentTop) > 2) {
                if (currentText.trim()) lines.push(currentText.trim());
                currentTop = top;
                currentText = tn.textContent;
              } else {
                currentText += tn.textContent;
              }
            }
          }
          if (currentText.trim()) lines.push(currentText.trim());

          const cs = getComputedStyle(el);
          return {
            text: el.textContent.replace(/\s+/g, ' ').trim(),
            lines,
            lineCount: lines.length,
            fontSize: cs.fontSize,
            lineHeight: cs.lineHeight,
            textWrap: cs.textWrap || cs.getPropertyValue('text-wrap'),
            width: Math.round(el.getBoundingClientRect().width),
          };
        })
      );

      const flagged = allIssues
        .map((data, index) => ({ index, ...data, issues: analyzeText(data.text, data.lines) }))
        .filter((d) => d.issues.length || d.lineCount >= 3);

      if (flagged.length) results[width].elements[key] = flagged;
    }

    results[width].cards = await page.evaluate(() => {
      const allowed = document.querySelector('.machine-transport__card--allowed');
      const denied = document.querySelector('.machine-transport__card--denied');
      const cta = document.querySelector('.machine-transport__cta');
      const pricingLi = document.querySelector('.pricing-factors__list li');
      const transport = document.querySelector('.machine-transport');
      return {
        allowedW: Math.round(allowed?.getBoundingClientRect().width ?? 0),
        deniedW: Math.round(denied?.getBoundingClientRect().width ?? 0),
        ctaW: Math.round(cta?.getBoundingClientRect().width ?? 0),
        pricingLiW: Math.round(pricingLi?.getBoundingClientRect().width ?? 0),
        transportCols: transport ? getComputedStyle(transport).gridTemplateColumns : '',
      };
    });
  }

  await browser.close();
  console.log(JSON.stringify(results, null, 2));
})();
