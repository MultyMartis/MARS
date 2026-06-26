'use strict';

const { resolveActiveNavKey, matchChildByCardLabel, getVisibleChildren } = require('./link-graph');
const { normalizeDemoUrl } = require('./path-utils');
const { applyActiveStates } = require('./active-state');
const { injectHomeTreatmentPreventionLinks } = require('./home-treatment-links');

const STATIC_SELECTOR_TARGETS = [
  { selector: 'home-treatment-prevention__all-link', url: '/uslugi/' },
  { selector: 'home-genotyping__all-link', url: '/zavisimosti/' },
  { selector: 'home-specialists__all-link', url: '/specialisty/' },
  { selector: 'home-reviews__all-link', url: '/otzyvy/' },
  { selector: 'home-rehabilitation-program__all-link', url: '/o-centre/programma-lecheniya/' },
  { selector: 'home-articles__all-link', url: '/blog/' },
  { selector: 'home-comfort__all-link', url: '/o-centre/galereya-o-dome/' },
  { selector: 'services-comfort-v2__all-link', url: '/o-centre/galereya-o-dome/' },
];

const ARTICLE_PAGE_IDS = ['FP0002-DEMO-PG-016', 'FP0002-DEMO-PG-014', 'FP0002-DEMO-PG-015'];

function replaceHrefOnClass(html, className, newHref) {
  const regex = new RegExp(
    `(<a\\b[^>]*class="[^"]*${className}[^"]*"[^>]*href=")[^"]*(")`,
    'gi'
  );
  return html.replace(regex, `$1${newHref}$2`);
}

function fixTypoUrls(html) {
  return html
    .replace(/href="\/specyalisty\//g, 'href="/specialisty/')
    .replace(/href='\/specyalisty\//g, "href='/specialisty/")
    .replace(/\/specyalisty\//g, '/specialisty/')
    .replace(/pilzovatelyu/g, 'polzovatelyu');
}

function applyStaticSelectorTargets(html) {
  let result = html;
  STATIC_SELECTOR_TARGETS.forEach(({ selector, url }) => {
    result = replaceHrefOnClass(result, selector, url);
  });
  return result;
}

function rewriteReviewReadMoreLinks(html) {
  return html.replace(
    /(<footer class="home-reviews__read-all">[\s\S]*?<a\b[^>]*href=")#(")/gi,
    '$1/otzyvy/$2'
  );
}

function rewriteHomeArticleCards(html, indexes) {
  const articlePages = ARTICLE_PAGE_IDS.map((id) => indexes.byId.get(id)).filter(Boolean);
  if (!articlePages.length) {
    return html;
  }

  let cardIndex = 0;
  return html.replace(
    /(<a\b[^>]*class="[^"]*home-articles__card-link[^"]*"[^>]*href=")[^"]*(")/gi,
    (match, prefix, suffix) => {
      const page = articlePages[cardIndex] || articlePages[articlePages.length - 1];
      cardIndex += 1;
      return `${prefix}${page.url}${suffix}`;
    }
  );
}

function demoteAnchorToSpan(anchorHtml) {
  return anchorHtml
    .replace(/^<a\b/, '<span')
    .replace(/<\/a>$/, '</span>')
    .replace(/\s+href="[^"]*"/i, '')
    .replace(/\s+href='[^']*'/i, '')
    .replace(/<span\b/, '<span data-demo-non-nav="true"');
}

const HUB_SECTION_PARENTS = {
  'services-category-addictions': 'FP0002-DEMO-PG-031',
  'services-category-mental-health': 'FP0002-DEMO-PG-029',
  'services-category-eating-disorders': 'FP0002-DEMO-PG-030',
  'services-category-genotyping': 'FP0002-DEMO-PG-003',
};

function migrateGenotipirovanieNavigation(html) {
  let result = html;
  const navLinkPatterns = [
    /(<a\b[^>]*class="[^"]*site-header__nav-link[^"]*"[^>]*href=")\/uslugi\/genotipirovanie\/("[^>]*>)\s*Генотипирование/gi,
    /(<a\b[^>]*class="[^"]*offcanvas__nav-link[^"]*"[^>]*href=")\/uslugi\/genotipirovanie\/("[^>]*>)\s*Генотипирование/gi,
    /(<a\b[^>]*class="[^"]*site-footer__nav-link[^"]*"[^>]*href=")\/uslugi\/genotipirovanie\/("[^>]*>)\s*Генотипирование/gi,
  ];
  navLinkPatterns.forEach((pattern) => {
    result = result.replace(pattern, '$1/zavisimosti/$2Зависимости');
  });
  result = result.replace(/href="\/uslugi\/genotipirovanie\/"/g, 'href="/zavisimosti/"');
  result = result.replace(/href='\/uslugi\/genotipirovanie\/'/g, "href='/zavisimosti/'");
  return result;
}

function getExpandedChildren(parentPage, indexes) {
  if (!parentPage) {
    return [];
  }
  const direct = getVisibleChildren(parentPage, indexes);
  const nested = [];
  direct.forEach((child) => {
    nested.push(child);
    getVisibleChildren(child, indexes).forEach((grandchild) => nested.push(grandchild));
  });
  return nested;
}

function resolveCardChildrenForSection(sectionBlock, page, indexes) {
  if (page.template === 'SERVICES_HUB_INTERNAL_PAGE') {
    const sectionId = (sectionBlock.match(/id="([^"]+)"/) || [])[1];
    const parentId = HUB_SECTION_PARENTS[sectionId];
    if (parentId) {
      return getExpandedChildren(indexes.byId.get(parentId), indexes);
    }
    return [];
  }
  if (page.template === 'SERVICE_SUBDIVISION_INTERNAL_PAGE') {
    return getExpandedChildren(page, indexes);
  }
  return getVisibleChildren(page, indexes);
}

function rewriteServiceCardsInSection(html, page, indexes) {
  if (
    page.template !== 'SERVICE_SUBDIVISION_INTERNAL_PAGE' &&
    page.template !== 'SERVICES_HUB_INTERNAL_PAGE'
  ) {
    return html;
  }

  const sectionRegex =
    /<section class="services-category-section-v2[\s\S]*?<\/section>/gi;
  let slotCounter = 0;

  return html.replace(sectionRegex, (sectionBlock) => {
    const children = resolveCardChildrenForSection(sectionBlock, page, indexes);
    if (!children.length) {
      return sectionBlock;
    }

    const articleRegex =
      /<article class="services-category-section-v2__service">([\s\S]*?)<\/article>/gi;
    let sectionSlot = 0;

    return sectionBlock.replace(articleRegex, (articleBlock) => {
      const nameMatch = articleBlock.match(
        /<span class="services-category-section-v2__service-name">([\s\S]*?)<\/span>/i
      );
      if (!nameMatch) {
        return articleBlock;
      }

      const label = nameMatch[1];
      let child = matchChildByCardLabel(label, children);
      if (!child && page.template === 'SERVICE_SUBDIVISION_INTERNAL_PAGE' && children[sectionSlot]) {
        child = children[sectionSlot];
      }
      sectionSlot += 1;
      slotCounter += 1;

      if (!child) {
        const hrefMatch = articleBlock.match(/href="([^"]+)"/i);
        if (hrefMatch && indexes.byUrl.get(normalizeDemoUrl(hrefMatch[1]))) {
          return articleBlock;
        }
        return articleBlock.replace(
          /<a\b([^>]*class="[^"]*services-category-section-v2__service-link[^"]*"[^>]*)href="[^"]*"([^>]*>)/i,
          (m, before, after) => demoteAnchorToSpan(`<a${before}href="#"${after}`)
        );
      }

      return articleBlock.replace(
        /(<a\b[^>]*class="[^"]*services-category-section-v2__service-link[^"]*"[^>]*href=")[^"]*(")/i,
        `$1${child.url}$2`
      );
    });
  });
}

function rewriteInternalHtmlLinks(html) {
  return html.replace(/href="([^"]*\.html)"/gi, (match, href) => {
    if (href.includes('assets/')) {
      return match;
    }
    const normalized = normalizeDemoUrl(href.replace(/\.html$/, '/').replace(/^\.\//, ''));
    return `href="${normalized}"`;
  });
}

function applyNavigationRewrites(html, page, indexes) {
  let result = html;
  result = fixTypoUrls(result);
  result = rewriteInternalHtmlLinks(result);
  result = applyStaticSelectorTargets(result);
  result = rewriteReviewReadMoreLinks(result);

  if (page.template === 'HOME_PAGE_TEMPLATE') {
    result = rewriteHomeArticleCards(result, indexes);
    result = injectHomeTreatmentPreventionLinks(result);
  }

  result = migrateGenotipirovanieNavigation(result);

  if (
    page.template === 'SERVICE_SUBDIVISION_INTERNAL_PAGE' ||
    page.template === 'SERVICES_HUB_INTERNAL_PAGE'
  ) {
    result = rewriteServiceCardsInSection(result, page, indexes);
  }

  result = applyActiveStates(result, page);
  return result;
}

module.exports = {
  applyNavigationRewrites,
  fixTypoUrls,
  applyStaticSelectorTargets,
  rewriteServiceCardsInSection,
  demoteAnchorToSpan,
  STATIC_SELECTOR_TARGETS,
};
