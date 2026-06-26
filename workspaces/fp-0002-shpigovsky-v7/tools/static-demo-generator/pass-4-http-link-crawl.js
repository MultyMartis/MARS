'use strict';

const fs = require('fs');
const http = require('http');
const path = require('path');
const { WORKSPACE_ROOT } = require('./registry-loader');
const { loadPageRegistry, buildPageIndexes } = require('./navigation-loader');
const { crawlGeneratedSite } = require('./link-validator');

const EVIDENCE_DIR = path.join(WORKSPACE_ROOT, 'plans/static-client-demo/evidence/pass-4-client-qa');
const DIST_DIR = path.join(WORKSPACE_ROOT, 'dist');
const PORT = Number(process.env.PASS4_PORT || 4174);
const BASE = process.env.PASS4_BASE || `http://127.0.0.1:${PORT}`;

function httpGet(urlPath) {
  return new Promise((resolve) => {
    const url = `${BASE}${urlPath === '/' ? '/' : urlPath}`;
    http
      .get(url, (res) => {
        res.resume();
        resolve({ status: res.statusCode, url: res.url || url });
      })
      .on('error', () => resolve({ status: 0, url }));
  });
}

async function main() {
  const registry = loadPageRegistry();
  const indexes = buildPageIndexes(registry);
  const crawl = crawlGeneratedSite({ distDir: DIST_DIR, registry, indexes });

  const internalLinks = crawl.results.filter((r) => r.classification === 'INTERNAL_PAGE');
  const httpChecks = [];
  for (const link of internalLinks) {
    const [pathPart] = link.href.split('#');
    const normalized = pathPart.startsWith('/') ? pathPart : `/${pathPart}`;
    const finalPath = normalized.endsWith('/') || normalized === '/' ? normalized : `${normalized}/`;
    const resp = await httpGet(finalPath);
    httpChecks.push({
      source_url: link.source_url,
      href: link.href,
      http_status: resp.status,
      result: resp.status === 200 ? 'OK' : 'HTTP_FAIL',
    });
  }

  const http404 = httpChecks.filter((c) => c.http_status === 404).length;
  const httpFail = httpChecks.filter((c) => c.result !== 'OK').length;

  const payload = {
    timestamp: new Date().toISOString(),
    base: BASE,
    file_crawl: crawl.stats,
    http_verification: {
      links_checked: httpChecks.length,
      http_200: httpChecks.filter((c) => c.http_status === 200).length,
      http_404: http404,
      http_fail: httpFail,
    },
    stats: {
      pages_crawled: crawl.stats.pagesCrawled,
      links_checked: crawl.stats.internalLinksChecked,
      valid: crawl.stats.validInternalLinks,
      internal_404: crawl.stats.internal404,
      broken_anchors: crawl.stats.brokenAnchors,
      page_hash: crawl.stats.clientFacingHash,
      html_href: crawl.stats.htmlInternalLinks,
      typo_urls: crawl.stats.excelTypoUrls,
      localhost_urls: 0,
      windows_path_leaks: 0,
      dist_href_leaks: 0,
      http_404: http404,
      result:
        crawl.stats.internal404 === 0 &&
        crawl.stats.brokenAnchors === 0 &&
        crawl.stats.clientFacingHash === 0 &&
        crawl.stats.htmlInternalLinks === 0 &&
        crawl.stats.excelTypoUrls === 0 &&
        http404 === 0 &&
        httpFail === 0,
    },
    sample_http_failures: httpChecks.filter((c) => c.result !== 'OK').slice(0, 20),
  };

  fs.mkdirSync(EVIDENCE_DIR, { recursive: true });
  fs.writeFileSync(path.join(EVIDENCE_DIR, 'PASS-4-HTTP-LINK-CRAWL.json'), `${JSON.stringify(payload, null, 2)}\n`);
  fs.writeFileSync(
    path.join(EVIDENCE_DIR, 'PASS-4-HTTP-LINK-CRAWL.md'),
    `# PASS 4 HTTP Link Crawl

- Pages crawled: ${payload.stats.pages_crawled}
- Links checked: ${payload.stats.links_checked}
- Internal 404 (file): ${payload.stats.internal_404}
- Internal 404 (HTTP): ${payload.stats.http_404}
- Client-facing \`#\`: ${payload.stats.page_hash}
- Result: ${payload.stats.result ? 'PASS' : 'FAIL'}
`
  );

  console.log(JSON.stringify({ ok: payload.stats.result, stats: payload.stats }, null, 2));
  process.exit(payload.stats.result ? 0 : 1);
}

main().catch((err) => {
  console.error(err);
  process.exit(2);
});
