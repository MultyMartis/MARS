/**
 * V9-06E58 Figma visual layout audit — capture + metrics (read-only).
 * Excludes: lifebuoy, heroes, main header, floating header, footer.
 */
import { createRequire } from 'module';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { createServer } from 'http';

const require = createRequire(import.meta.url);
const { chromium } = require('../v9-06e54-fix01-floating-header/_probe/node_modules/playwright');

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const outDir = __dirname;
const wpBase = 'http://shpigovsky.test';
const v9Dist = 'X:\\AI MARS\\workspaces\\fp-0002-shpigovsky-v9\\dist';
const viewports = [
  { w: 1440, h: 1100, key: '1440' },
  { w: 1024, h: 900, key: '1024' },
  { w: 480, h: 900, key: '480' },
  { w: 370, h: 800, key: '370' },
];

const routes = [
  { id: 'home', path: '/', type: 'home', v9: '/', refDesktop: null, refMobile: null },
  { id: 'uslugi', path: '/uslugi/', type: 'services-hub', v9: '/uslugi/', refKey: 'Услуги общая' },
  { id: 'section-rpp', path: '/uslugi/rasstroystva-pischevogo-povedeniya/', type: 'service-section', v9: '/uslugi/rasstroystva-pischevogo-povedeniya/', refKey: 'Услуга подраздел' },
  { id: 'service-alcohol', path: '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/', type: 'service', v9: '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/', refKey: 'Услуга' },
  { id: 'service-narc', path: '/uslugi/psihicheskoe-zdorovie/nartsissizm/', type: 'service', v9: '/uslugi/psihicheskoe-zdorovie/depressiya/', refKey: 'Услуга' },
  { id: 'generic-geno', path: '/o-centre/programma-lecheniya/genotipirovanie/', type: 'generic', v9: '/o-centre/programma-lecheniya/', refKey: 'Типовой контент' },
  { id: 'specialist', path: '/specyalisty/shipovsky/', type: 'specialist-child', v9: null, refKey: 'Типовой контент' },
  { id: 'ocentre', path: '/o-centre/', type: 'institutional', v9: '/o-centre/', refKey: 'О центре' },
  { id: 'kontakty', path: '/kontakty/', type: 'contacts', v9: '/kontakty/', refKey: 'Контакты' },
  { id: 'blog', path: '/blog/', type: 'blog', v9: '/blog/', refKey: 'Блог' },
  { id: 'blog-single', path: '/blog/sryvy-i-retsidivy-signal-k-korrektirovke/', type: 'blog-single', v9: '/blog/nazvanie-stati/', refKey: 'Статья блога' },
];

const HIDE_CSS = `
  .fp02-lifebuoy-parallax, [class*="lifebuoy"], .fp02-floating-header,
  header.header, .header, .site-header, .fp02-header,
  footer, .footer, .site-footer,
  .hero, .hero--home, .hero--home-slider, .services-inner-hero-v2,
  .page-hero, .institutional-hero, .blog-hero, [class*="__hero"]:not([class*="__hero-card"])
  { visibility: hidden !important; }
`;

function slug(s) {
  return String(s).replace(/[^a-z0-9_-]+/gi, '-').replace(/-+/g, '-').replace(/^-|-$/g, '');
}

async function measure(page) {
  return page.evaluate(() => {
    const doc = document.documentElement;
    const body = document.body;
    const overflowX = Math.max(doc.scrollWidth, body.scrollWidth) - window.innerWidth;
    const main =
      document.querySelector('main') ||
      document.querySelector('.site-content') ||
      document.querySelector('#content') ||
      body;
    const containers = Array.from(
      document.querySelectorAll('.container, .l-container, .wrapper, [class*="container"]')
    ).slice(0, 12);
    const containerStats = containers.map((el) => {
      const cs = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return {
        class: el.className?.toString?.().slice(0, 80) || '',
        width: Math.round(r.width),
        maxWidth: cs.maxWidth,
        paddingLeft: cs.paddingLeft,
        paddingRight: cs.paddingRight,
        marginLeft: cs.marginLeft,
        marginRight: cs.marginRight,
      };
    });
    const sections = Array.from(
      main.querySelectorAll('section, .section, [class*="section-"], [class*="__section"]')
    ).slice(0, 40);
    const sectionStats = sections.map((el) => {
      const cs = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return {
        class: (el.className?.toString?.() || el.tagName).slice(0, 100),
        top: Math.round(r.top + window.scrollY),
        height: Math.round(r.height),
        width: Math.round(r.width),
        paddingTop: cs.paddingTop,
        paddingBottom: cs.paddingBottom,
        marginTop: cs.marginTop,
        marginBottom: cs.marginBottom,
      };
    });
    const buttons = Array.from(document.querySelectorAll('.btn, button.btn, a.btn, .button')).slice(0, 20);
    const buttonStats = buttons.map((el) => {
      const cs = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return {
        text: (el.textContent || '').trim().slice(0, 40),
        w: Math.round(r.width),
        h: Math.round(r.height),
        fontSize: cs.fontSize,
        padding: `${cs.paddingTop} ${cs.paddingRight} ${cs.paddingBottom} ${cs.paddingLeft}`,
        radius: cs.borderRadius,
      };
    });
    const cards = Array.from(
      document.querySelectorAll('[class*="card"], .services-category-section-v2__item, .home-articles__item')
    ).slice(0, 20);
    const cardStats = cards.map((el) => {
      const cs = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return {
        class: (el.className?.toString?.() || '').slice(0, 80),
        w: Math.round(r.width),
        h: Math.round(r.height),
        padding: `${cs.paddingTop} ${cs.paddingRight} ${cs.paddingBottom} ${cs.paddingLeft}`,
        radius: cs.borderRadius,
      };
    });
    const h2s = Array.from(document.querySelectorAll('h2')).slice(0, 15).map((el) => {
      const cs = getComputedStyle(el);
      return { text: (el.textContent || '').trim().slice(0, 50), size: cs.fontSize, lh: cs.lineHeight, ff: cs.fontFamily.slice(0, 60) };
    });
    const overlaps = [];
    const actionable = Array.from(document.querySelectorAll('a, button, input, textarea, select')).slice(0, 80);
    for (let i = 0; i < actionable.length; i++) {
      for (let j = i + 1; j < Math.min(actionable.length, i + 8); j++) {
        const a = actionable[i].getBoundingClientRect();
        const b = actionable[j].getBoundingClientRect();
        if (a.width < 2 || b.width < 2) continue;
        const overlap =
          Math.max(0, Math.min(a.right, b.right) - Math.max(a.left, b.left)) *
          Math.max(0, Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top));
        if (overlap > 40 && a.top > 120) {
          overlaps.push({
            a: (actionable[i].textContent || '').trim().slice(0, 30),
            b: (actionable[j].textContent || '').trim().slice(0, 30),
            area: Math.round(overlap),
          });
        }
      }
    }
    return {
      viewport: { w: window.innerWidth, h: window.innerHeight },
      overflowX: overflowX,
      scrollHeight: Math.max(doc.scrollHeight, body.scrollHeight),
      containerStats,
      sectionStats,
      buttonStats,
      cardStats,
      h2s,
      overlaps: overlaps.slice(0, 10),
    };
  });
}

async function captureRoute(browser, route, vp, baseUrl, tag) {
  const page = await browser.newPage({ viewport: { width: vp.w, height: vp.h } });
  const url = baseUrl.replace(/\/$/, '') + route.path;
  const result = { route: route.id, viewport: vp.key, url, ok: false, metrics: null, errors: [] };
  page.on('pageerror', (e) => result.errors.push(String(e.message || e)));
  try {
    const resp = await page.goto(url, { waitUntil: 'networkidle', timeout: 60000 });
    result.status = resp?.status() || 0;
    await page.waitForTimeout(600);
    const fullName = `${slug(route.id)}__${vp.key}__${tag}__full.png`;
    await page.screenshot({ path: path.join(outDir, 'screenshots', fullName), fullPage: true });
    await page.addStyleTag({ content: HIDE_CSS });
    await page.waitForTimeout(200);
    const bodyName = `${slug(route.id)}__${vp.key}__${tag}__body.png`;
    await page.screenshot({ path: path.join(outDir, 'screenshots', bodyName), fullPage: true });
    result.metrics = await measure(page);
    result.ok = result.status === 200;
    result.shots = { full: fullName, body: bodyName };
  } catch (e) {
    result.errors.push(String(e.message || e));
  } finally {
    await page.close();
  }
  return result;
}

function startStaticServer(root, port) {
  return new Promise((resolve, reject) => {
    const server = createServer((req, res) => {
      let urlPath = decodeURIComponent((req.url || '/').split('?')[0]);
      if (urlPath.endsWith('/')) urlPath += 'index.html';
      if (urlPath === '') urlPath = '/index.html';
      const filePath = path.join(root, urlPath.replace(/^\//, '').replace(/\//g, path.sep));
      fs.readFile(filePath, (err, data) => {
        if (err) {
          res.writeHead(404);
          res.end('not found');
          return;
        }
        const ext = path.extname(filePath).toLowerCase();
        const types = {
          '.html': 'text/html; charset=utf-8',
          '.css': 'text/css',
          '.js': 'application/javascript',
          '.png': 'image/png',
          '.jpg': 'image/jpeg',
          '.webp': 'image/webp',
          '.svg': 'image/svg+xml',
          '.woff2': 'font/woff2',
          '.ttf': 'font/ttf',
        };
        res.writeHead(200, { 'Content-Type': types[ext] || 'application/octet-stream' });
        res.end(data);
      });
    });
    server.listen(port, '127.0.0.1', () => resolve(server));
    server.on('error', reject);
  });
}

async function main() {
  fs.mkdirSync(path.join(outDir, 'screenshots'), { recursive: true });
  fs.mkdirSync(path.join(outDir, 'metrics'), { recursive: true });
  fs.mkdirSync(path.join(outDir, 'refs'), { recursive: true });

  const browser = await chromium.launch({ headless: true });
  const all = [];

  for (const route of routes) {
    for (const vp of viewports) {
      console.log('WP', route.id, vp.key);
      const r = await captureRoute(browser, route, vp, wpBase, 'wp');
      all.push(r);
      fs.writeFileSync(
        path.join(outDir, 'metrics', `${slug(route.id)}__${vp.key}__wp.json`),
        JSON.stringify(r, null, 2)
      );
    }
  }

  let v9Server = null;
  const v9Port = 8765;
  try {
    v9Server = await startStaticServer(v9Dist, v9Port);
    const v9Base = `http://127.0.0.1:${v9Port}`;
    for (const route of routes) {
      if (!route.v9) continue;
      for (const vp of viewports.filter((v) => v.key === '1440' || v.key === '480')) {
        console.log('V9', route.id, vp.key);
        const r = await captureRoute(browser, { ...route, path: route.v9 }, vp, v9Base, 'v9');
        all.push(r);
        fs.writeFileSync(
          path.join(outDir, 'metrics', `${slug(route.id)}__${vp.key}__v9.json`),
          JSON.stringify(r, null, 2)
        );
      }
    }
  } catch (e) {
    console.error('V9 static server failed', e);
  } finally {
    if (v9Server) v9Server.close();
  }

  await browser.close();

  const matrix = [['route', 'type', '1440', '1024', '480', '370', 'overflow_notes']];
  for (const route of routes) {
    const row = [route.id, route.type];
    const notes = [];
    for (const vp of viewports) {
      const m = all.find((x) => x.route === route.id && x.viewport === vp.key && x.shots?.full?.includes('__wp__'));
      const ok = m?.ok ? 'OK' : 'FAIL';
      const ox = m?.metrics?.overflowX ?? '';
      row.push(`${ok}${ox !== '' && ox > 1 ? ` ox=${ox}` : ''}`);
      if (ox > 2) notes.push(`${vp.key}:overflowX=${ox}`);
      if (m?.errors?.length) notes.push(`${vp.key}:js=${m.errors[0]}`);
    }
    row.push(notes.join('; ') || 'none');
    matrix.push(row);
  }
  fs.writeFileSync(
    path.join(outDir, 'route-viewport-matrix.csv'),
    matrix.map((r) => r.map((c) => `"${String(c).replace(/"/g, '""')}"`).join(',')).join('\n'),
    'utf8'
  );
  fs.writeFileSync(path.join(outDir, 'capture-summary.json'), JSON.stringify({ routes, viewports, results: all }, null, 2));
  console.log('DONE captures', all.length);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
