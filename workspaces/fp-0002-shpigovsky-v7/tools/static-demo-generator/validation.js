'use strict';

const VALID_TEMPLATES = new Set([
  'HOME_PAGE_TEMPLATE',
  'SERVICES_HUB_INTERNAL_PAGE',
  'SERVICE_SUBDIVISION_INTERNAL_PAGE',
  'SERVICE_LEAF_INTERNAL_PAGE',
  'PLACEHOLDER_PAGE',
]);

function clientFacingBlob(page) {
  return JSON.stringify({
    url: page.url,
    title: page.title,
    h1: page.h1,
    name: page.name,
    client_demo_name: page.client_demo_name,
    breadcrumbs: page.breadcrumbs,
    placeholder_message: page.placeholder_message,
  });
}

function validateRegistry(registry) {
  const errors = [];
  const pages = registry.pages || [];

  if (pages.length !== 56) {
    errors.push(`Expected 56 pages, got ${pages.length}`);
  }

  const ids = new Set();
  const urls = new Set();
  const outputs = new Set();
  const titles = new Set();
  const h1s = new Set();
  const idMap = new Map(pages.map((p) => [p.id, p]));

  pages.forEach((page) => {
    if (!VALID_TEMPLATES.has(page.template)) {
      errors.push(`Invalid template for ${page.id}: ${page.template}`);
    }
    if (ids.has(page.id)) {
      errors.push(`Duplicate id: ${page.id}`);
    }
    ids.add(page.id);

    if (urls.has(page.url)) {
      errors.push(`Duplicate url: ${page.url}`);
    }
    urls.add(page.url);

    if (outputs.has(page.output)) {
      errors.push(`Duplicate output: ${page.output}`);
    }
    outputs.add(page.output);

    if (titles.has(page.title)) {
      errors.push(`Duplicate title: ${page.title}`);
    }
    titles.add(page.title);

    if (page.template !== 'HOME_PAGE_TEMPLATE' && page.h1) {
      if (h1s.has(page.h1)) {
        errors.push(`Duplicate h1: ${page.h1}`);
      }
      h1s.add(page.h1);
    }

    if (page.parent_id && !idMap.has(page.parent_id)) {
      errors.push(`Broken parent_id ${page.parent_id} for ${page.id}`);
    }

    const serialized = clientFacingBlob(page);
    if (serialized.includes('Название')) {
      errors.push(`Client-facing Название in ${page.id}`);
    }
    if (/specyalisty|pilzovatelyu/.test(page.url || '')) {
      errors.push(`Typo URL in demo url for ${page.id}: ${page.url}`);
    }
    if (/(?:^|[^:])\/\//.test(page.url || '')) {
      errors.push(`Double-slash path in demo url for ${page.id}`);
    }
    if (/\{\{[^}]+\}\}/.test(serialized)) {
      errors.push(`Unresolved template markers in ${page.id}`);
    }

    if (page.client_demo_name && page.client_demo_name.includes('Название')) {
      errors.push(`Client-facing Название in client_demo_name for ${page.id}`);
    }
    if (page.h1 && page.h1.includes('Название')) {
      errors.push(`Client-facing Название in h1 for ${page.id}`);
    }
    if (page.title && page.title.includes('Название')) {
      errors.push(`Client-facing Название in title for ${page.id}`);
    }

    if (Array.isArray(page.breadcrumbs)) {
      page.breadcrumbs.forEach((crumb, index) => {
        if (index === 0 && crumb.name !== 'Главная') {
          errors.push(`Breadcrumb home name invalid for ${page.id}`);
        }
      });
    }
  });

  const counts = pages.reduce((acc, page) => {
    acc[page.template] = (acc[page.template] || 0) + 1;
    return acc;
  }, {});

  const expected = {
    HOME_PAGE_TEMPLATE: 1,
    SERVICES_HUB_INTERNAL_PAGE: 1,
    SERVICE_SUBDIVISION_INTERNAL_PAGE: 6,
    SERVICE_LEAF_INTERNAL_PAGE: 18,
    PLACEHOLDER_PAGE: 30,
  };

  Object.entries(expected).forEach(([template, count]) => {
    if (counts[template] !== count) {
      errors.push(`Template count mismatch ${template}: expected ${count}, got ${counts[template] || 0}`);
    }
  });

  return { valid: errors.length === 0, errors, counts };
}

function validateGeneratedHtml(html, page) {
  const errors = [];
  const titleMatch = html.match(/<title>([^<]*)<\/title>/i);
  if (!titleMatch) {
    errors.push('Missing title');
  } else if (titleMatch[1].trim() !== page.title) {
    errors.push(`Title mismatch: expected "${page.title}", got "${titleMatch[1].trim()}"`);
  }

  const h1Matches = [...html.matchAll(/<h1\b[^>]*>[\s\S]*?<\/h1>/gi)];
  if (page.template === 'HOME_PAGE_TEMPLATE') {
    // home marketing layout may include multiple h1 blocks
  } else if (page.template === 'PLACEHOLDER_PAGE') {
    const placeholderH1 = html.match(/<h1 class="page-placeholder__title"[^>]*>[\s\S]*?<\/h1>/i);
    if (!placeholderH1) {
      errors.push('Placeholder H1 missing');
    } else if (page.h1) {
      const h1Text = placeholderH1[0].replace(/<[^>]+>/g, '').replace(/\s+/g, ' ').trim();
      const expected = page.h1.replace(/\u00a0/g, ' ').replace(/\s+/g, ' ').trim();
      if (!h1Text.includes(expected) && !expected.includes(h1Text)) {
        errors.push(`H1 mismatch: "${h1Text}" vs "${expected}"`);
      }
    }
  } else if (page.h1) {
    const heroH1 = html.match(/<h1\b[^>]*class="[^"]*services-inner-hero-v2__title[^"]*"[^>]*>[\s\S]*?<\/h1>/i);
    if (!heroH1) {
      errors.push('Primary hero H1 missing');
    } else {
      const h1Text = heroH1[0].replace(/<[^>]+>/g, '').replace(/\s+/g, ' ').trim();
      const expected = page.h1.replace(/\u00a0/g, ' ').replace(/\s+/g, ' ').trim();
      if (!h1Text.includes(expected) && !expected.includes(h1Text)) {
        errors.push(`H1 mismatch: "${h1Text}" vs "${expected}"`);
      }
    }
  }

  const headerCount = (html.match(/<header class="site-header"/gi) || []).length;
  const mainCount = (html.match(/<main\b/gi) || []).length;
  const footerCount = (html.match(/<footer class="site-footer"/gi) || []).length;

  if (headerCount !== 1) {
    errors.push(`site-header count ${headerCount}`);
  }
  if (mainCount !== 1) {
    errors.push(`main count ${mainCount}`);
  }
  if (footerCount !== 1) {
    errors.push(`site-footer count ${footerCount}`);
  }

  const modalCount = (html.match(/data-modal="consultation"/gi) || []).length;
  if (modalCount < 1) {
    errors.push('Modal markers missing');
  }

  if (html.includes('Название')) {
    errors.push('Contains client-facing Название');
  }
  if (/specyalisty|pilzovatelyu/.test(html)) {
    errors.push('Contains typo URL');
  }
  if (/\{\{[^}]+\}\}/.test(html)) {
    errors.push('Unresolved template markers');
  }

  return errors;
}

module.exports = {
  validateRegistry,
  validateGeneratedHtml,
};
