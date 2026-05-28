const { chromium } = require('playwright');
const path = require('path');

const INDEX = path.resolve(__dirname, '../dist/index.html');
const WIDTHS = [320, 375, 390, 420, 760, 1180, 1320, 1440];

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file:///' + INDEX.replace(/\\/g, '/'));

  const dump = {};

  for (const width of WIDTHS) {
    await page.setViewportSize({ width, height: 900 });
    await page.waitForTimeout(100);

    dump[width] = await page.evaluate(() => {
      const getLines = (el) => {
        const lines = [];
        let currentTop = null;
        let currentText = '';
        const walk = (node) => {
          if (node.nodeType === Node.TEXT_NODE) {
            const r = document.createRange();
            r.selectNodeContents(node);
            for (const rect of r.getClientRects()) {
              if (rect.width === 0) continue;
              const top = Math.round(rect.top);
              if (currentTop === null || Math.abs(top - currentTop) > 2) {
                if (currentText.trim()) lines.push(currentText.trim());
                currentTop = top;
                currentText = node.textContent;
              } else currentText += node.textContent;
            }
          } else node.childNodes.forEach(walk);
        };
        walk(el);
        if (currentText.trim()) lines.push(currentText.trim());
        return lines;
      };

      const headings = [...document.querySelectorAll('h1, h2, h3, .section-title, .machine-transport__heading, .faq-item summary')].map((el) => ({
        tag: el.tagName + (el.className ? '.' + String(el.className).split(' ')[0] : ''),
        text: el.textContent.replace(/\s+/g, ' ').trim().slice(0, 80),
        lines: getLines(el),
        w: Math.round(el.getBoundingClientRect().width),
        fs: getComputedStyle(el).fontSize,
        tw: getComputedStyle(el).textWrap || getComputedStyle(el).getPropertyValue('text-wrap'),
      }));

      const overflowEls = [...document.querySelectorAll('*')]
        .filter((el) => el.getBoundingClientRect().right > document.documentElement.clientWidth + 1)
        .slice(0, 8)
        .map((el) => ({
          tag: el.tagName + (el.className ? '.' + String(el.className).split(' ')[0] : ''),
          right: Math.round(el.getBoundingClientRect().right),
          w: Math.round(el.getBoundingClientRect().width),
        }));

      const midWord = [];
      document.querySelectorAll('h1,h2,h3,h4,.section-title,.machine-transport__heading,.faq-item summary,.button,.machine-transport__list li span,.pricing-factors__list li span,.hero__lead,.section-lead').forEach((el) => {
        const t = el.textContent;
        const lines = getLines(el);
        lines.forEach((line) => {
          // detect broken cyrillic words: partial word at line end without space
          if (/[а-яёА-ЯЁ]$/.test(line) && lines.length > 1) {
            const idx = lines.indexOf(line);
            if (idx < lines.length - 1) {
              const combined = (line + lines[idx + 1]).replace(/\s/g, '');
              if (/[а-яё]{4,}/i.test(combined) && !/\s/.test(line.slice(-8))) {
                // possible split - check if line ends mid-word by comparing to full words
                const words = t.replace(/\s+/g, ' ').trim().split(' ');
                for (const w of words) {
                  if (w.length > 5 && line.endsWith(w.slice(0, Math.ceil(w.length / 2))) && !line.endsWith(w)) {
                    midWord.push({ el: el.tagName, text: t.slice(0, 60), line });
                  }
                }
              }
            }
          }
          if (line.split(/\s+/).length === 1 && line.length <= 6 && lines.length >= 2) {
            midWord.push({ el: el.tagName, type: 'orphan', text: t.slice(0, 60), line });
          }
        });
      });

      return {
        overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth + 1,
        scrollW: document.documentElement.scrollWidth,
        overflowEls,
        headings,
        midWord,
      };
    });
  }

  await browser.close();
  console.log(JSON.stringify(dump, null, 2));
})();
