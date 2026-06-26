'use strict';

function escapeHtml(text) {
  return String(text)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function renderBreadcrumbsHtml(breadcrumbs) {
  if (!breadcrumbs || breadcrumbs.length === 0) {
    return '';
  }

  const items = breadcrumbs
    .map((crumb, index) => {
      const isLast = index === breadcrumbs.length - 1 || crumb.current;
      const name = escapeHtml(crumb.name);
      if (isLast) {
        return `    <li class="breadcrumbs__item breadcrumbs__item--current" aria-current="page">
      <span class="breadcrumbs__current">${name}</span>
    </li>`;
      }
      if (!crumb.url) {
        return `    <li class="breadcrumbs__item">
      <span class="breadcrumbs__text">${name}</span>
    </li>`;
      }
      return `    <li class="breadcrumbs__item">
      <a class="breadcrumbs__link" href="${escapeHtml(crumb.url)}">${name}</a>
    </li>`;
    })
    .join('\n');

  return `<nav class="breadcrumbs" aria-label="Хлебные крошки">
  <ol class="breadcrumbs__list">
${items}
  </ol>
</nav>`;
}

function replaceTitle(html, title) {
  return html.replace(/<title>[^<]*<\/title>/i, `<title>${escapeHtml(title)}</title>`);
}

function replaceMetaContent(html, attr, value) {
  const pattern = new RegExp(`(<meta[^>]+${attr}=["'][^"']*["'][^>]*content=["'])([^"']*)(["'])`, 'i');
  if (pattern.test(html)) {
    return html.replace(pattern, `$1${escapeHtml(value)}$3`);
  }
  return html;
}

function replacePrimaryHeroH1(html, h1) {
  return html.replace(
    /(<h1\b[^>]*class="[^"]*services-inner-hero-v2__title[^"]*"[^>]*>)([\s\S]*?)(<\/h1>)/i,
    `$1${h1}$3`
  );
}

function replacePrimaryHeroEyebrow(html, eyebrow) {
  if (!eyebrow) {
    return html;
  }
  return html.replace(
    /(<p\b[^>]*class="[^"]*services-inner-hero-v2__eyebrow[^"]*"[^>]*>)([\s\S]*?)(<\/p>)/i,
    `$1${eyebrow}$3`
  );
}

function replaceBreadcrumbsBlock(html, breadcrumbsHtml) {
  if (!breadcrumbsHtml) {
    return html;
  }
  return html.replace(/<nav class="breadcrumbs"[\s\S]*?<\/nav>/i, breadcrumbsHtml);
}

function injectDemoPageId(html, pageId) {
  let result = html;
  if (/<body\b[^>]*data-demo-page-id=/.test(result)) {
    result = result.replace(
      /(<body\b[^>]*data-demo-page-id=["'])[^"']*(["'])/i,
      `$1${pageId}$2`
    );
  } else {
    result = result.replace(/<body\b/i, `<body data-demo-page-id="${pageId}"`);
  }

  if (/<main\b[^>]*data-demo-page-id=/.test(result)) {
    result = result.replace(
      /(<main\b[^>]*data-demo-page-id=["'])[^"']*(["'])/i,
      `$1${pageId}$2`
    );
  } else {
    result = result.replace(/<main\b/i, `<main data-demo-page-id="${pageId}"`);
  }

  return result;
}

function countPrimaryH1(html) {
  return (html.match(/<h1\b[^>]*class="[^"]*services-inner-hero-v2__title/gi) || []).length;
}

function applyTemplateInstance(html, page) {
  let result = html;
  result = replaceTitle(result, page.title);
  result = replaceMetaContent(result, 'property="og:title"', page.title);
  result = replaceMetaContent(result, 'name="description"', page.title);

  if (page.h1) {
    const heroH1Count = countPrimaryH1(result);
    if (heroH1Count !== 1) {
      throw new Error(`Template defect: expected 1 primary hero H1, found ${heroH1Count} for ${page.id}`);
    }
    result = replacePrimaryHeroH1(result, page.h1);
  }

  result = replacePrimaryHeroEyebrow(result, page.eyebrow);

  const breadcrumbsHtml = renderBreadcrumbsHtml(page.breadcrumbs);
  result = replaceBreadcrumbsBlock(result, breadcrumbsHtml);
  result = injectDemoPageId(result, page.id);

  if (page.url && page.url !== '/') {
    const canonical = `https://shpigovsky.ru${page.url}`;
    result = replaceMetaContent(result, 'rel="canonical"', canonical);
    result = replaceMetaContent(result, 'property="og:url"', canonical);
  }

  return result;
}

module.exports = {
  renderBreadcrumbsHtml,
  applyTemplateInstance,
  escapeHtml,
  replaceTitle,
  replaceMetaContent,
};
