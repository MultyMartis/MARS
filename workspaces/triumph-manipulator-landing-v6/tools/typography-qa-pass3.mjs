/**
 * V5 Typography Live QA Pass 3 — headless line-break analyzer
 * Read-only diagnostic; does not modify the site.
 */
import { chromium } from 'playwright';
import { fileURLToPath } from 'url';
import path from 'path';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const INDEX = path.resolve(__dirname, '../dist/index.html');
const WIDTHS = [320, 375, 390, 420, 760, 1180, 1320, 1440];

const SELECTORS = [
  { key: 'h1', sel: '.hero__title' },
  { key: 'h2-section', sel: '.section-title' },
  { key: 'h2-transport', sel: '.machine-transport__heading' },
  { key: 'h2-faq', sel: '.faq__title' },
  { key: 'h2-cta', sel: '.contact-cta h2' },
  { key: 'h3-denied', sel: '.machine-transport__card h3' },
  { key: 'faq-summary-long', sel: '.faq-item summary' },
];

const analyzeText = (text, lines) => {
  const words = text.replace(/\s+/g, ' ').trim().split(' ');
  const issues = [];

  for (const line of lines) {
    const trimmed = line.trim();
    if (!trimmed) continue;
    // mid-word split heuristic: line ends with hyphen or starts lowercase after break in Cyrillic word
    if (/[а-яёА-ЯЁ]-$/.test(trimmed)) {
      issues.push({ type: 'mid-word-split', line: trimmed });
    }
    // orphan: single short word line (< 4 chars) that's not a number
    const lineWords = trimmed.split(/\s+/);
    if (lineWords.length === 1 && lineWords[0].length <= 4 && !/^\d/.test(lineWords[0])) {
      issues.push({ type: 'orphan-word', line: trimmed });
    }
  }

  // widow: last line is single word and first lines have many words
  if (lines.length >= 2) {
    const last = lines[lines.length - 1].trim().split(/\s+/);
    if (last.length === 1 && words.length >= 4) {
      issues.push({ type: 'widow-word', line: lines[lines.length - 1].trim() });
    }
  }

  return issues;
};

const browser = await chromium.launch();
const page = await browser.newPage();
await page.goto(`file:///${INDEX.replace(/\\/g, '/')}`);

const results = {};

for (const width of WIDTHS) {
  await page.setViewportSize({ width, height: 900 });
  await page.waitForTimeout(120);

  const pageOverflow = await page.evaluate(() => ({
    scrollW: document.documentElement.scrollWidth,
    clientW: document.documentElement.clientWidth,
    overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth + 1,
  }));

  results[width] = { overflow: pageOverflow, elements: {} };

  for (const { key, sel } of SELECTORS) {
    const nodes = await page.$$(sel);
    if (!nodes.length) {
      results[width].elements[key] = { missing: true };
      continue;
    }

    const allIssues = [];
    for (let i = 0; i < nodes.length; i++) {
      const data = await nodes[i].evaluate((el) => {
        const range = document.createRange();
        range.selectNodeContents(el);
        const rects = Array.from(range.getClientRects());
        const lines = [];
        let currentTop = null;
        let currentText = '';

        const textNodes = [];
        const walk = (node) => {
          if (node.nodeType === Node.TEXT_NODE) {
            textNodes.push(node);
          } else {
            node.childNodes.forEach(walk);
          }
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
          overflowWrap: cs.overflowWrap,
          wordBreak: cs.wordBreak,
          width: el.getBoundingClientRect().width,
        };
      });

      const issues = analyzeText(data.text, data.lines);
      if (issues.length || data.lineCount >= 4) {
        allIssues.push({ index: i, ...data, issues });
      }
    }

    if (allIssues.length) {
      results[width].elements[key] = allIssues;
    }
  }

  // Card width check
  const cards = await page.evaluate(() => {
    const allowed = document.querySelector('.machine-transport__card--allowed');
    const denied = document.querySelector('.machine-transport__card--denied');
    const cta = document.querySelector('.machine-transport__cta');
    const pricingLi = document.querySelector('.pricing-factors__list li');
    return {
      allowedW: allowed?.getBoundingClientRect().width ?? 0,
      deniedW: denied?.getBoundingClientRect().width ?? 0,
      ctaW: cta?.getBoundingClientRect().width ?? 0,
      pricingLiW: pricingLi?.getBoundingClientRect().width ?? 0,
      transportCols: getComputedStyle(document.querySelector('.machine-transport')).gridTemplateColumns,
    };
  });
  results[width].cards = cards;
}

await browser.close();

console.log(JSON.stringify(results, null, 2));
