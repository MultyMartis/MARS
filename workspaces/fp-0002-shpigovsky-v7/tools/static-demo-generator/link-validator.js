'use strict';

const { TOP_LEVEL_NAV, resolveActiveNavKey } = require('./link-graph');

const LEGAL_URLS = new Set([
  '/privacy-policy/',
  '/user-agreement/',
  '/consent-personal-data/',
  '/cookie-files-policy/',
]);

function stripTags(text) {
  return String(text || '')
    .replace(/<[^>]+>/g, '')
    .replace(/\u00a0/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

function extractAnchorContext(html, index) {
  const start = Math.max(0, index - 120);
  const end = Math.min(html.length, index + 200);
  return html.slice(start, end).replace(/\s+/g, ' ').trim();
}

function isMessengerPlaceholder(tag) {
  return (
    (/offcanvas__messenger-link|site-header__messenger-link|mobile-header__messengers/i.test(tag) ||
      /site-footer__social-link/i.test(tag)) &&
    /aria-label="(?:Telegram|WhatsApp|Max|YouTube|VK|ВКонтакте)"/i.test(tag)
  );
}

function isModalAction(tag) {
  return /data-modal-open=|data-offcanvas-open=|data-offcanvas-close=|data-accordion-button/i.test(tag);
}

function isFancybox(tag) {
  return /data-fancybox=/i.test(tag);
}

function classifyHref(href, tag, page) {
  if (!href || href.trim() === '') {
    return 'BROKEN_OR_EMPTY';
  }

  if (isModalAction(tag)) {
    return 'MODAL_ACTION';
  }

  if (href.startsWith('tel:')) {
    return 'TELEPHONE';
  }
  if (href.startsWith('mailto:')) {
    return 'EMAIL';
  }
  if (href.startsWith('http://') || href.startsWith('https://')) {
    return 'EXTERNAL';
  }
  if (isFancybox(tag) || href.startsWith('assets/') || href.startsWith('/assets/')) {
    return 'MEDIA/FANCYBOX';
  }
  if (tag.includes('type="submit"') || tag.includes('<form')) {
    return 'FORM_ACTION';
  }

  if (href === '#') {
    if (isMessengerPlaceholder(tag)) {
      return 'ACTION_CONTROL_PRESERVED';
    }
    if (isModalAction(tag)) {
      return 'MODAL_ACTION';
    }
    return 'PLACEHOLDER_TECHNICAL';
  }

  if (href.startsWith('#')) {
    const anchorId = href.slice(1);
    if (page && page.html && page.html.includes(`id="${anchorId}"`)) {
      return 'SAME_PAGE_ANCHOR';
    }
    return 'BROKEN_OR_EMPTY';
  }

  if (href.includes('.html') && !href.includes('assets/')) {
    return 'BROKEN_OR_EMPTY';
  }

  if (/specyalisty|pilzovatelyu/.test(href)) {
    return 'BROKEN_OR_EMPTY';
  }

  if (/(?:^|[^:])\/\//.test(href)) {
    return 'BROKEN_OR_EMPTY';
  }

  if (href.startsWith('/')) {
    return 'INTERNAL_PAGE';
  }

  return 'EXTERNAL';
}

function normalizeInternalUrl(href) {
  const [pathPart, anchor] = href.split('#');
  let path = pathPart;
  if (!path.startsWith('/')) {
    path = `/${path}`;
  }
  if (path.length > 1 && !path.endsWith('/')) {
    path = `${path}/`;
  }
  return anchor ? `${path}#${anchor}` : path;
}

function crawlGeneratedSite({ distDir, registry, indexes }) {
  const fs = require('fs');
  const path = require('path');

  const results = [];
  const classifications = {};
  const stats = {
    pagesCrawled: 0,
    internalLinksChecked: 0,
    validInternalLinks: 0,
    internal404: 0,
    brokenAnchors: 0,
    emptyHref: 0,
    clientFacingHash: 0,
    htmlInternalLinks: 0,
    excelTypoUrls: 0,
    doubleSlashes: 0,
  };

  registry.pages.forEach((page) => {
    const filePath = path.join(distDir, page.output);
    if (!fs.existsSync(filePath)) {
      results.push({
        source_page_id: page.id,
        source_output: page.output,
        href: null,
        result: 'MISSING_OUTPUT',
      });
      return;
    }

    const html = fs.readFileSync(filePath, 'utf8');
    stats.pagesCrawled += 1;
    const pageCtx = { ...page, html };

    const re = /<a\b[^>]*href\s*=\s*(["'])(.*?)\1[^>]*>/gi;
    let match;
    while ((match = re.exec(html)) !== null) {
      const href = match[2];
      const tag = match[0];
      const type = classifyHref(href, tag, pageCtx);
      classifications[type] = (classifications[type] || 0) + 1;

      const record = {
        source_page_id: page.id,
        source_output: page.output,
        source_url: page.url,
        href,
        link_text: stripTags(tag),
        selector_context: extractAnchorContext(html, match.index),
        classification: type,
        result: 'OK',
      };

      if (type === 'BROKEN_OR_EMPTY') {
        if (!href) {
          stats.emptyHref += 1;
        }
        record.result = 'BROKEN';
        results.push(record);
        continue;
      }

      if (type === 'PLACEHOLDER_TECHNICAL') {
        stats.clientFacingHash += 1;
        record.result = 'CLIENT_FACING_HASH';
        results.push(record);
        continue;
      }

      if (type === 'INTERNAL_PAGE') {
        stats.internalLinksChecked += 1;
        const [pathPart, anchorPart] = href.split('#');
        const normalized = normalizeInternalUrl(pathPart);
        const target = indexes.byUrl.get(normalized);
        if (!target) {
          stats.internal404 += 1;
          record.result = 'INTERNAL_404';
          record.target_url = normalized;
        } else {
          stats.validInternalLinks += 1;
          record.target_page_id = target.id;
          record.target_url = target.url;

          if (anchorPart) {
            const targetHtml = fs.readFileSync(path.join(distDir, target.output), 'utf8');
            const anchorHtml = target.id === page.id ? html : targetHtml;
            if (!anchorHtml.includes(`id="${anchorPart}"`)) {
              stats.brokenAnchors += 1;
              record.result = 'BROKEN_ANCHOR';
            }
          }
        }

        if (href.includes('.html')) {
          stats.htmlInternalLinks += 1;
        }
        if (/specyalisty|pilzovatelyu/.test(href)) {
          stats.excelTypoUrls += 1;
        }
        if (/(?:^|[^:])\/\//.test(href)) {
          stats.doubleSlashes += 1;
        }
      }

      if (type === 'SAME_PAGE_ANCHOR') {
        const anchorId = href.slice(1);
        if (!html.includes(`id="${anchorId}"`)) {
          stats.brokenAnchors += 1;
          record.result = 'BROKEN_ANCHOR';
        }
      }

      results.push(record);
    }
  });

  return { results, classifications, stats };
}

function buildWalkthroughRoutes(indexes) {
  return [
    {
      id: 'route-1-service-journey',
      name: 'Service journey',
      steps: [
        { page_id: 'FP0002-DEMO-PG-001', url: '/' },
        { page_id: 'FP0002-DEMO-PG-002', url: '/uslugi/' },
        { page_id: 'FP0002-DEMO-PG-031', url: '/uslugi/zavisimosti/' },
        { page_id: 'FP0002-DEMO-PG-032', url: '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/' },
        { page_id: 'FP0002-DEMO-PG-002', url: '/uslugi/' },
        { page_id: 'FP0002-DEMO-PG-001', url: '/' },
      ],
    },
    {
      id: 'route-2-informational',
      name: 'Informational',
      steps: [
        { page_id: 'FP0002-DEMO-PG-001', url: '/' },
        { page_id: 'FP0002-DEMO-PG-005', url: '/o-centre/' },
        { page_id: 'FP0002-DEMO-PG-019', url: '/o-centre/o-nas/' },
        { page_id: 'FP0002-DEMO-PG-001', url: '/' },
      ],
    },
    {
      id: 'route-3-specialists',
      name: 'Specialists',
      steps: [
        { page_id: 'FP0002-DEMO-PG-004', url: '/specialisty/' },
        { page_id: 'FP0002-DEMO-PG-023', url: '/specialisty/shipovsky/' },
        { page_id: 'FP0002-DEMO-PG-004', url: '/specialisty/' },
      ],
    },
    {
      id: 'route-4-articles',
      name: 'Articles',
      steps: [
        { page_id: 'FP0002-DEMO-PG-007', url: '/blog/' },
        { page_id: 'FP0002-DEMO-PG-016', url: '/stati/statya-1/' },
        { page_id: 'FP0002-DEMO-PG-014', url: '/stati/statya-2/' },
        { page_id: 'FP0002-DEMO-PG-007', url: '/blog/' },
      ],
    },
    {
      id: 'route-5-legal',
      name: 'Legal',
      steps: [
        { page_id: 'FP0002-DEMO-PG-012', url: '/privacy-policy/' },
        { page_id: 'FP0002-DEMO-PG-001', url: '/' },
      ],
    },
  ];
}

function validateWalkthroughs(routes, indexes, distDir) {
  const fs = require('fs');
  const path = require('path');

  return routes.map((route) => {
    const stepResults = route.steps.map((step) => {
      const page = indexes.byId.get(step.page_id);
      const exists = page && fs.existsSync(path.join(distDir, page.output));
      return {
        page_id: step.page_id,
        url: step.url,
        output: page ? page.output : null,
        exists,
        result: exists ? 'OK' : 'MISSING',
      };
    });
    const completed = stepResults.every((s) => s.result === 'OK');
    return {
      ...route,
      steps: stepResults,
      completed,
      result: completed ? 'PASS' : 'FAIL',
    };
  });
}

function validateActiveStates(registry, distDir) {
  const fs = require('fs');
  const path = require('path');
  const checks = [];

  registry.pages.forEach((page) => {
    const filePath = path.join(distDir, page.output);
    if (!fs.existsSync(filePath)) {
      return;
    }
    const html = fs.readFileSync(filePath, 'utf8');
    const activeKey = resolveActiveNavKey(page);
    if (!activeKey) {
      checks.push({ page_id: page.id, active_key: null, result: 'N/A' });
      return;
    }
    const cfg = TOP_LEVEL_NAV[activeKey];
    const hasActive =
      html.includes('site-header__nav-link--active') ||
      html.includes('offcanvas__nav-link--active') ||
      LEGAL_URLS.has(page.url);
    checks.push({
      page_id: page.id,
      active_key: activeKey,
      expected_url: cfg.url,
      has_active_class: hasActive,
      result: hasActive || LEGAL_URLS.has(page.url) ? 'PASS' : 'FAIL',
    });
  });

  return checks;
}

module.exports = {
  classifyHref,
  crawlGeneratedSite,
  buildWalkthroughRoutes,
  validateWalkthroughs,
  validateActiveStates,
};
