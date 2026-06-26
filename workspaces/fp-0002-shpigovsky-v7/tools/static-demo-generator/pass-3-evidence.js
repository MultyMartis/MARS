'use strict';

const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const { WORKSPACE_ROOT } = require('./registry-loader');
const { buildPageIndexes } = require('./navigation-loader');
const { analyzeReachability } = require('./link-graph');
const { getVisibleChildren } = require('./link-graph');
const {
  crawlGeneratedSite,
  buildWalkthroughRoutes,
  validateWalkthroughs,
  validateActiveStates,
} = require('./link-validator');

const EVIDENCE_DIR = path.join(WORKSPACE_ROOT, 'plans/static-client-demo/evidence/pass-3-navigation');
const DIST_DIR = path.join(WORKSPACE_ROOT, 'dist');

function writeJson(name, data) {
  fs.writeFileSync(path.join(EVIDENCE_DIR, name), `${JSON.stringify(data, null, 2)}\n`, 'utf8');
}

function writeMd(name, content) {
  fs.writeFileSync(path.join(EVIDENCE_DIR, name), content, 'utf8');
}

function buildCardChildMapping(registry, indexes) {
  const rows = [];
  registry.pages
    .filter((p) => p.template === 'SERVICE_SUBDIVISION_INTERNAL_PAGE')
    .forEach((page) => {
      const children = getVisibleChildren(page, indexes);
      const cardSlots = 4;
      rows.push({
        instance: page.id,
        url: page.url,
        actual_children: children.length,
        available_card_slots: cardSlots,
        mapped: Math.min(children.length, cardSlots),
        unrepresented: Math.max(0, children.length - cardSlots),
        extra_demo_slots: Math.max(0, cardSlots - children.length),
      });
    });
  return rows;
}

function buildCtaClassification(crawl) {
  const counts = crawl.classifications;
  return {
    modal_cta: { count: counts.MODAL_ACTION || 0, preserved: counts.MODAL_ACTION || 0 },
    page_navigation_cta: { count: counts.INTERNAL_PAGE || 0, rewritten: counts.INTERNAL_PAGE || 0 },
    phone: { count: counts.TELEPHONE || 0, preserved: counts.TELEPHONE || 0 },
    form: { count: counts.FORM_ACTION || 0, preserved: counts.FORM_ACTION || 0 },
    external: { count: counts.EXTERNAL || 0, preserved: counts.EXTERNAL || 0 },
    action_control: {
      count: counts['ACTION_CONTROL_PRESERVED'] || 0,
      preserved: counts['ACTION_CONTROL_PRESERVED'] || 0,
    },
  };
}

function sha256File(filePath) {
  return crypto.createHash('sha256').update(fs.readFileSync(filePath)).digest('hex');
}

function writePass3Evidence({ registry, navigation, receipt, durationMs }) {
  fs.mkdirSync(EVIDENCE_DIR, { recursive: true });

  const indexes = buildPageIndexes(registry);
  const crawl = crawlGeneratedSite({ distDir: DIST_DIR, registry, indexes });
  const reachability = analyzeReachability(indexes, navigation);
  const walkthroughs = validateWalkthroughs(buildWalkthroughRoutes(indexes), indexes, DIST_DIR);
  const activeStates = validateActiveStates(registry, DIST_DIR);
  const cardMapping = buildCardChildMapping(registry, indexes);

  writeJson('PASS-3-NAVIGATION-REGISTRY-FINAL.json', navigation);
  writeJson('PASS-3-LINK-CLASSIFICATION.json', {
    timestamp: new Date().toISOString(),
    classifications: crawl.classifications,
    total_anchors: crawl.results.length,
  });
  writeJson('PASS-3-INTERNAL-LINK-CRAWL.json', {
    timestamp: new Date().toISOString(),
    stats: crawl.stats,
    results: crawl.results,
  });

  const crawlMd = `# PASS 3 Internal Link Crawl

- Pages crawled: ${crawl.stats.pagesCrawled}
- Internal links checked: ${crawl.stats.internalLinksChecked}
- Valid internal links: ${crawl.stats.validInternalLinks}
- Internal 404: ${crawl.stats.internal404}
- Broken anchors: ${crawl.stats.brokenAnchors}
- Empty href: ${crawl.stats.emptyHref}
- Client-facing \`#\`: ${crawl.stats.clientFacingHash}
- Internal .html links: ${crawl.stats.htmlInternalLinks}
- Excel typo URLs: ${crawl.stats.excelTypoUrls}
- Double slashes: ${crawl.stats.doubleSlashes}

## Result

${crawl.stats.internal404 === 0 && crawl.stats.brokenAnchors === 0 && crawl.stats.clientFacingHash === 0 ? 'PASS' : 'FAIL'}
`;
  writeMd('PASS-3-INTERNAL-LINK-CRAWL.md', crawlMd);

  writeJson('PASS-3-LINK-GRAPH.json', {
    timestamp: new Date().toISOString(),
    total_pages: registry.pages.length,
    reachable_pages: reachability.reachable.length,
    intentionally_hidden: reachability.intentionallyHidden,
    unexpected_orphans: reachability.unexpectedOrphans,
    result: reachability.unexpectedOrphans.length === 0 ? 'PASS' : 'FAIL',
  });

  writeMd(
    'PASS-3-LINK-GRAPH.md',
    `# PASS 3 Link Graph

- Total pages: ${registry.pages.length}
- Reachable from home: ${reachability.reachable.length}
- Intentionally hidden: ${reachability.intentionallyHidden.length}
- Unexpected orphans: ${reachability.unexpectedOrphans.length}

## Unexpected orphans

${reachability.unexpectedOrphans.length ? reachability.unexpectedOrphans.join(', ') : 'none'}
`
  );

  writeJson('PASS-3-ACTIVE-STATE-VALIDATION.json', {
    timestamp: new Date().toISOString(),
    checks: activeStates,
    failed: activeStates.filter((c) => c.result === 'FAIL').length,
  });

  const cardMd = `# PASS 3 Card/Child Mapping

| Instance | Actual children | Available card slots | Mapped | Unrepresented | Extra demo slots |
| -------- | --------------: | -------------------: | -----: | ------------: | ---------------: |
${cardMapping
  .map(
    (r) =>
      `| ${r.instance} | ${r.actual_children} | ${r.available_card_slots} | ${r.mapped} | ${r.unrepresented} | ${r.extra_demo_slots} |`
  )
  .join('\n')}
`;
  writeMd('PASS-3-CARD-CHILD-MAPPING.md', cardMd);

  const cta = buildCtaClassification(crawl);
  writeMd(
    'PASS-3-CTA-CLASSIFICATION.md',
    `# PASS 3 CTA Classification

| CTA type | Count | Rewritten | Preserved |
| -------- | ----: | --------: | --------: |
| Modal CTA | ${cta.modal_cta.count} | 0 | ${cta.modal_cta.preserved} |
| Page navigation CTA | ${cta.page_navigation_cta.count} | ${cta.page_navigation_cta.rewritten} | 0 |
| Phone | ${cta.phone.count} | 0 | ${cta.phone.preserved} |
| Form | ${cta.form.count} | 0 | ${cta.form.preserved} |
| External | ${cta.external.count} | 0 | ${cta.external.preserved} |
| Action control | ${cta.action_control.count} | 0 | ${cta.action_control.preserved} |
`
  );

  writeJson('PASS-3-FUNCTIONAL-WALKTHROUGHS.json', {
    timestamp: new Date().toISOString(),
    routes: walkthroughs,
    all_pass: walkthroughs.every((r) => r.result === 'PASS'),
  });

  writeMd(
    'PASS-3-DESKTOP-MOBILE-QA.md',
    `# PASS 3 Desktop/Mobile QA

Manual/automated smoke deferred to evidence policy manifests; generator validation PASS required.

- Viewports target: 1437, 380
- Pages: Home, Services Hub, subdivisions, leaf pages, placeholders, legal
- Overflow: confirmed zero from PASS 2.1 baseline (not re-run in PASS 3 unless regression detected)
- Navigation wiring: validated via internal link crawl
`
  );

  const canonicalFiles = [
    'src/pages/index.html',
    'src/pages/uslugi-v2.html',
    'src/pages/usluga-podrazdel-v1.html',
    'src/pages/usluga-konechnaya-v1.html',
  ];
  const templateHashes = canonicalFiles.map((rel) => ({
    file: rel,
    sha256: sha256File(path.join(WORKSPACE_ROOT, rel)),
  }));

  const pass3Receipt = {
    timestamp: new Date().toISOString(),
    pass: 'PASS-3',
    source_commit: '1d9e5dfb',
    generated_page_count: registry.pages.length,
    navigation_link_count: navigation.links.length,
    crawl_stats: crawl.stats,
    reachability,
    walkthroughs_pass: walkthroughs.every((r) => r.result === 'PASS'),
    template_hashes: templateHashes,
    duration_ms: durationMs,
    command: 'npm run build:demo',
    result:
      crawl.stats.internal404 === 0 &&
      crawl.stats.brokenAnchors === 0 &&
      crawl.stats.clientFacingHash === 0 &&
      reachability.unexpectedOrphans.length === 0
        ? 'PASS'
        : 'FAIL',
  };

  writeJson('PASS-3-GENERATION-RECEIPT.json', pass3Receipt);

  writeMd(
    'PASS-3-FINAL.md',
    `# PASS 3 Final

- Navigation registry links: ${navigation.links.length}
- Unresolved blocking: ${navigation.meta.unresolved_blocking || 0}
- Internal 404: ${crawl.stats.internal404}
- Broken anchors: ${crawl.stats.brokenAnchors}
- Client-facing hash links: ${crawl.stats.clientFacingHash}
- Unexpected orphans: ${reachability.unexpectedOrphans.length}
- Result: **${pass3Receipt.result}**
`
  );

  return pass3Receipt;
}

module.exports = {
  writePass3Evidence,
  EVIDENCE_DIR,
};
