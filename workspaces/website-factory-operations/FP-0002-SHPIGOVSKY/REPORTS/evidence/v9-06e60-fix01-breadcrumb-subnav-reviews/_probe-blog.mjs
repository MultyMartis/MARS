import { chromium } from '../v9-06e60-nav-breadcrumb-cta-service-links/node_modules/playwright/index.mjs';
const b = await chromium.launch({headless:true});
const p = await b.newPage({viewport:{width:1440,height:900}});
await p.goto('http://shpigovsky.test/blog/', {waitUntil:'networkidle'});
const hrefs = await p.$$eval('a[href]', as => as.map(a=>a.getAttribute('href')).filter(h=>h && /\/blog\//.test(h) && h!=='/blog/' && !h.includes('#')).slice(0,10));
console.log('blog hrefs', hrefs);
await p.goto('http://shpigovsky.test/', {waitUntil:'networkidle'});
await p.evaluate(() => window.scrollTo(0, 2000));
await p.waitForTimeout(500);
const dec = await p.evaluate(() => ({
  lifebuoy: [...document.querySelectorAll('[class*="lifebuoy"], [class*="fp02-lifebuoy"], .fp02-lifebuoy-parallax')].map(e=>e.className).slice(0,5),
  floating: [...document.querySelectorAll('[class*="floating"], .site-header.is-floating, .site-header--scrolled')].map(e=>e.className).slice(0,5),
  bodyClasses: document.body.className,
}));
console.log(JSON.stringify(dec,null,2));
if (hrefs[0]) {
  const u = hrefs[0].startsWith('http') ? hrefs[0] : 'http://shpigovsky.test'+hrefs[0];
  await p.setViewportSize({width:1024,height:768});
  await p.goto(u, {waitUntil:'networkidle'});
  const crumb = await p.evaluate(() => {
    const el = document.querySelector('.blog-article-hero__breadcrumbs .breadcrumbs__link, .breadcrumbs__link');
    if (!el) return {found:false, classes:[...document.querySelectorAll('[class*="breadcrumb"]')].map(e=>e.className).slice(0,8)};
    const s = getComputedStyle(el);
    return {found:true, fs:s.fontSize, lh:s.lineHeight, path: location.pathname};
  });
  console.log('blog single 1024', crumb);
}
await b.close();
