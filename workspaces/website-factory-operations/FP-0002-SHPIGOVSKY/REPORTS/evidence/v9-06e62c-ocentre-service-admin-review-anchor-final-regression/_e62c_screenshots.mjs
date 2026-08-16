const { spawnSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const chrome = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const outDir = 'X:\\AI MARS\\workspaces\\website-factory-operations\\FP-0002-SHPIGOVSKY\\REPORTS\\evidence\\v9-06e62c-ocentre-service-admin-review-anchor-final-regression\\screenshots';
fs.mkdirSync(outDir, { recursive: true });

const viewports = [
  { name: '1440x900', w: 1440, h: 900 },
  { name: '1024x768', w: 1024, h: 768 },
  { name: '480x900', w: 480, h: 900 },
  { name: '370x812', w: 370, h: 812 },
];

const routes = [
  { slug: 'home', url: 'http://shpigovsky.test/' },
  { slug: 'uslugi', url: 'http://shpigovsky.test/uslugi/' },
  { slug: 'section-zavisimosti', url: 'http://shpigovsky.test/uslugi/zavisimosti/' },
  { slug: 'service-alcohol', url: 'http://shpigovsky.test/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/' },
  { slug: 'o-centre', url: 'http://shpigovsky.test/o-centre/' },
  { slug: 'o-centre-gallery', url: 'http://shpigovsky.test/o-centre/galereya-o-dome/' },
  { slug: 'specyalisty', url: 'http://shpigovsky.test/specyalisty/' },
  { slug: 'specialist-kostyuk', url: 'http://shpigovsky.test/specyalisty/kostyuk/' },
  { slug: 'kontakty', url: 'http://shpigovsky.test/kontakty/' },
  { slug: 'blog', url: 'http://shpigovsky.test/blog/' },
  { slug: 'blog-page-2', url: 'http://shpigovsky.test/blog/page/2/' },
  { slug: 'blog-single', url: 'http://shpigovsky.test/blog/demo-pagination-article-10/' },
  { slug: 'otzyvy', url: 'http://shpigovsky.test/otzyvy/' },
  { slug: 'otzyvy-page-2', url: 'http://shpigovsky.test/otzyvy/page/2/' },
  { slug: 'otzyvy-page-3', url: 'http://shpigovsky.test/otzyvy/page/3/' },
  { slug: '404', url: 'http://shpigovsky.test/this-route-should-404-e62c/' },
];

const rows = ['viewport,route,file,bytes,status'];

for (const vp of viewports) {
  for (const route of routes) {
    const file = path.join(outDir, `${route.slug}__${vp.name}.png`);
    const args = [
      '--headless=new',
      '--disable-gpu',
      '--hide-scrollbars',
      `--window-size=${vp.w},${vp.h}`,
      `--screenshot=${file}`,
      route.url,
    ];
    const res = spawnSync(chrome, args, { encoding: 'utf8', timeout: 60000 });
    const exists = fs.existsSync(file);
    const bytes = exists ? fs.statSync(file).size : 0;
    const status = exists && bytes > 1000 ? 'PASS' : 'FAIL';
    rows.push(`${vp.name},${route.slug},${path.basename(file)},${bytes},${status}`);
    process.stdout.write(`${status} ${vp.name} ${route.slug} ${bytes}\n`);
  }
}

fs.writeFileSync(path.join(outDir, '..', 'viewport-screenshot-matrix.csv'), rows.join('\n'), 'utf8');
console.log('DONE screenshots', rows.length - 1);
