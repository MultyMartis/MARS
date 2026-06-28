import { chromium } from 'playwright';
import { mkdir } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.webp': 'image/webp',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.svg': 'image/svg+xml',
  '.woff2': 'font/woff2',
  '.woff': 'font/woff',
  '.json': 'application/json',
};
function mimeFor(filePath) {
  return MIME[path.extname(filePath).toLowerCase()] || 'application/octet-stream';
}

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(__dirname, '..');
const dist = path.join(root, 'dist');
const outDir = path.join(root, 'docs', 'ai-workflow', 'evidence', 'o-centre-phase-a-v4');
const urlPath = '/o-centre-v1.html';

const blockSelectors = [
  { id: 'block-01', selector: '.services-inner-hero-v2' },
  { id: 'block-02', selector: '#about-who-we-are' },
  { id: 'block-03', selector: '.home-founder-quote' },
  { id: 'block-04', selector: '#who-we-treat' },
  { id: 'block-05', selector: '.service-leaf-cta-01-v1' },
  { id: 'block-06', selector: '#service-leaf-approach' },
];

function startStaticServer() {
  return new Promise((resolve) => {
    const server = createServer(async (req, res) => {
      try {
        const reqPath = decodeURIComponent(req.url.split('?')[0]);
        const filePath = path.join(dist, reqPath === '/' ? 'index.html' : reqPath.replace(/^\//, ''));
        const data = await readFile(filePath);
        res.writeHead(200, { 'Content-Type': mimeFor(filePath) });
        res.end(data);
      } catch {
        res.writeHead(404).end('Not found');
      }
    });
    server.listen(0, '127.0.0.1', () => resolve(server));
  });
}

const server = await startStaticServer();
const { port } = server.address();
const baseUrl = `http://127.0.0.1:${port}${urlPath}`;

await mkdir(outDir, { recursive: true });

const browser = await chromium.launch();
const results = { console: [], overflow: null, assets: [] };

for (const viewport of [
  { name: 'desktop-1437', width: 1437, height: 900 },
  { name: 'mobile-380', width: 380, height: 812 },
]) {
  const page = await browser.newPage({ viewport: { width: viewport.width, height: viewport.height } });
  page.on('console', (msg) => {
    if (msg.type() === 'error') results.console.push(msg.text());
  });
  page.on('pageerror', (err) => results.console.push(String(err)));

  await page.goto(baseUrl, { waitUntil: 'networkidle' });
  await page.waitForTimeout(500);

  if (viewport.name === 'desktop-1437') {
    results.overflow = await page.evaluate(() => ({
      scrollWidth: document.documentElement.scrollWidth,
      clientWidth: document.documentElement.clientWidth,
      horizontalOverflow: document.documentElement.scrollWidth > document.documentElement.clientWidth,
    }));
    results.assets = await page.evaluate(() =>
      [...document.querySelectorAll('img')]
        .filter((img) => !img.complete || img.naturalWidth === 0)
        .map((img) => img.getAttribute('src'))
    );
  }

  await page.screenshot({
    path: path.join(outDir, `${viewport.name}-full.png`),
    fullPage: true,
  });

  for (const block of blockSelectors) {
    const el = page.locator(block.selector).first();
    if (await el.count()) {
      await el.screenshot({ path: path.join(outDir, `${viewport.name}-${block.id}.png`) });
    }
  }

  await page.close();
}

await browser.close();
server.close();

const meta = {
  capturedAt: new Date().toISOString(),
  url: baseUrl,
  outputDir: outDir,
  consoleErrors: [...new Set(results.console)],
  horizontalOverflow: results.overflow,
  failedImages: results.assets,
};

await import('node:fs/promises').then((fs) =>
  fs.writeFile(path.join(outDir, 'capture-metadata.json'), JSON.stringify(meta, null, 2))
);

console.log(JSON.stringify(meta, null, 2));
