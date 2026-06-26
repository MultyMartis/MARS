'use strict';

const { renderBreadcrumbsHtml, escapeHtml, replaceTitle, replaceMetaContent } = require('./template-renderer');

function replaceTitleLocal(html, title) {
  return replaceTitle(html, title);
}

function replaceMetaContentLocal(html, attr, value) {
  return replaceMetaContent(html, attr, value);
}

function extractShellParts(html) {
  const mainOpen = html.search(/<main\b/i);
  const mainClose = html.search(/<\/main>/i);
  if (mainOpen === -1 || mainClose === -1) {
    throw new Error('Shell extraction failed: main element not found');
  }

  const beforeMain = html.slice(0, mainOpen);
  const afterMain = html.slice(mainClose + '</main>'.length);
  return { beforeMain, afterMain };
}

function renderPlaceholderMain(page) {
  const breadcrumbsHtml = renderBreadcrumbsHtml(page.breadcrumbs);
  const h1 = escapeHtml(page.h1 || page.client_demo_name || page.name);
  const message = escapeHtml(page.placeholder_message || 'Раздел скоро будет опубликован');

  return `<main class="page-placeholder" data-demo-page-id="${page.id}">
  <section class="page-placeholder__section">
    <div class="container">
      ${breadcrumbsHtml}
      <h1 class="page-placeholder__title">${h1}</h1>
      <p class="page-placeholder__message">${message}</p>
    </div>
  </section>
</main>`;
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
  return result;
}

function renderPlaceholderPage(shellHtml, page) {
  const { beforeMain, afterMain } = extractShellParts(shellHtml);
  const mainHtml = renderPlaceholderMain(page);
  let html = `${beforeMain}${mainHtml}${afterMain}`;
  html = replaceTitleLocal(html, page.title);
  html = replaceMetaContentLocal(html, 'property="og:title"', page.title);
  if (page.url && page.url !== '/') {
    const canonical = `https://shpigovsky.ru${page.url}`;
    html = replaceMetaContentLocal(html, 'rel="canonical"', canonical);
    html = replaceMetaContentLocal(html, 'property="og:url"', canonical);
  }
  html = injectDemoPageId(html, page.id);
  return html;
}

module.exports = {
  extractShellParts,
  renderPlaceholderMain,
  renderPlaceholderPage,
};
