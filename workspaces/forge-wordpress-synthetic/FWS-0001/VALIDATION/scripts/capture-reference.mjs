import { chromium, devices } from 'playwright';
import { mkdir } from 'fs/promises';
import path from 'path';
import { fileURLToPath } from 'url';
import http from 'http';
import fs from 'fs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(__dirname, '..');
const distDir = path.join(root, 'FRONTEND', 'dist');
const outDir = path.join(__dirname, '..', 'reference');

const viewports = [
  { name: 'desktop-1440', width: 1440, height: 900 },
  { name: 'tablet-1024', width: 1024, height: 900 },
  { name: 'mobile-390', width: 390, height: 844 },
];

const pages = [
  { file: 'index.html', slug: 'home' },
  { file: 'services.html', slug: 'services' },
  { file: 'service-single.html', slug: 'service-single' },
  { file: 'contacts.html', slug: 'contacts' },
];

function contentType(file) {
  if (file.endsWith('.css')) return 'text/css';
  if (file.endsWith('.js')) return 'application/javascript';
  if (file.endsWith('.html')) return 'text/html';
  return 'application/octet-stream';
}

function startStaticServer() {
  return new Promise((resolve) => {
    const server = http.createServer((req, res) => {
      let urlPath = decodeURIComponent(req.url.split('?')[0]);
      if (urlPath === '/') urlPath = '/index.html';
      const filePath = path.join(distDir, urlPath.replace(/^\//, ''));
      if (!filePath.startsWith(distDir) || !fs.existsSync(filePath)) {
        res.statusCode = 404;
        res.end('Not found');
        return;
      }
      res.setHeader('Content-Type', contentType(filePath));
      fs.createReadStream(filePath).pipe(res);
    });
    server.listen(0, '127.0.0.1', () => {
      const { port } = server.address();
      resolve({ server, baseUrl: `http://127.0.0.1:${port}` });
    });
  });
}

async function main() {
  await mkdir(outDir, { recursive: true });
  const { server, baseUrl } = await startStaticServer();
  const browser = await chromium.launch();

  try {
    for (const vp of viewports) {
      const context = await browser.newContext({
        viewport: { width: vp.width, height: vp.height },
        deviceScaleFactor: 1,
      });
      const page = await context.newPage();
      await page.emulateMedia({ reducedMotion: 'reduce' });

      for (const p of pages) {
        const url = `${baseUrl}/${p.file}`;
        await page.goto(url, { waitUntil: 'networkidle' });
        const out = path.join(outDir, `${p.slug}__${vp.name}.png`);
        await page.screenshot({ path: out, fullPage: true });
        console.log('Captured', out);
      }
      await context.close();
    }
  } finally {
    await browser.close();
    server.close();
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
