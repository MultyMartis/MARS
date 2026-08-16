import { chromium } from '../v9-06e60-nav-breadcrumb-cta-service-links/node_modules/playwright/index.mjs';
const b = await chromium.launch({headless:true});
const p = await b.newPage({viewport:{width:1024,height:768}});
const url = 'http://shpigovsky.test/blog/sryvy-i-retsidivy-signal-k-korrektirovke/';
await p.goto(url, {waitUntil:'networkidle'});
const crumb = await p.evaluate(() => {
  const el = document.querySelector('.blog-article-hero__breadcrumbs .breadcrumbs__link, .breadcrumbs__link');
  if (!el) return {found:false, html: document.body.innerHTML.includes('breadcrumbs')};
  const s = getComputedStyle(el);
  return {found:true, fs:s.fontSize, lh:s.lineHeight, path: location.pathname, className: el.className};
});
console.log(JSON.stringify(crumb,null,2));
await p.screenshot({path:'screenshots/blog-single-1024x768.png', fullPage:false});
await b.close();
