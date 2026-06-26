'use strict';

const { resolveActiveNavKey } = require('./link-graph');

const NAV_ACTIVE_MAP = {
  uslugi: '/uslugi/',
  zavisimosti: '/zavisimosti/',
  specialisty: '/specialisty/',
  oCentre: '/o-centre/',
  otzyvy: '/otzyvy/',
  stati: '/blog/',
  kontakty: '/kontakty/',
};

function stripActiveFromNavLinks(html) {
  let result = html;
  result = result.replace(/\s+site-header__nav-link--active/g, '');
  result = result.replace(/\s+offcanvas__nav-link--active/g, '');
  result = result.replace(
    /(<a\b[^>]*class="[^"]*(?:site-header__nav-link|offcanvas__nav-link)[^"]*")([^>]*)\s+aria-current="page"/gi,
    '$1$2'
  );
  return result;
}

function addClassToTag(openTag, className) {
  if (openTag.includes(className)) {
    return openTag;
  }
  if (/class="/.test(openTag)) {
    return openTag.replace(/class="/, `class="${className} `);
  }
  return openTag.replace(/<a\b/, `<a class="${className}"`);
}

function addAriaCurrent(openTag) {
  if (/aria-current=/.test(openTag)) {
    return openTag.replace(/aria-current="[^"]*"/, 'aria-current="page"');
  }
  return openTag.replace(/<a\b/, '<a aria-current="page"');
}

function applyFooterLegalCurrent(html, page) {
  const legalUrls = [
    '/privacy-policy/',
    '/user-agreement/',
    '/consent-personal-data/',
    '/cookie-files-policy/',
  ];
  if (!legalUrls.includes(page.url)) {
    return html;
  }
  const escaped = page.url.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const re = new RegExp(
    `(<a\\b[^>]*class="[^"]*site-footer__nav-link[^"]*"[^>]*href="${escaped}"[^>]*>)`,
    'gi'
  );
  return html.replace(re, (tag) => addAriaCurrent(tag));
}

function applyActiveStates(html, page) {
  let result = stripActiveFromNavLinks(html);
  const activeKey = resolveActiveNavKey(page);
  if (!activeKey) {
    return applyFooterLegalCurrent(result, page);
  }

  const targetHref = NAV_ACTIVE_MAP[activeKey];
  if (!targetHref) {
    return applyFooterLegalCurrent(result, page);
  }

  const hrefPattern = targetHref.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const desktopRe = new RegExp(
    `(<a\\b[^>]*class="[^"]*site-header__nav-link[^"]*"[^>]*href="${hrefPattern}"[^>]*>)`,
    'gi'
  );
  const mobileRe = new RegExp(
    `(<a\\b[^>]*class="[^"]*offcanvas__nav-link[^"]*"[^>]*href="${hrefPattern}"[^>]*>)`,
    'gi'
  );

  result = result.replace(desktopRe, (tag) => {
    let updated = addClassToTag(tag, 'site-header__nav-link--active');
    if (activeKey === 'uslugi') {
      updated = addAriaCurrent(updated);
    }
    return updated;
  });
  result = result.replace(mobileRe, (tag) => {
    let updated = addClassToTag(tag, 'offcanvas__nav-link--active');
    if (activeKey === 'uslugi') {
      updated = addAriaCurrent(updated);
    }
    return updated;
  });

  return applyFooterLegalCurrent(result, page);
}

module.exports = {
  applyActiveStates,
  stripActiveFromNavLinks,
};
