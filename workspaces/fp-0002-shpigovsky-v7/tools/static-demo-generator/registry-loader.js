'use strict';

const fs = require('fs');
const path = require('path');
const { normalizeDemoUrl, urlToOutputPath } = require('./path-utils');

const WORKSPACE_ROOT = path.resolve(__dirname, '..', '..');
const DRAFT_REGISTRY = path.join(
  WORKSPACE_ROOT,
  'plans/static-client-demo/data/demo-page-registry.draft.json'
);
const FINAL_REGISTRY = path.join(WORKSPACE_ROOT, 'src/data/static-demo/demo-page-registry.json');
const DRAFT_NAV = path.join(
  WORKSPACE_ROOT,
  'plans/static-client-demo/data/demo-navigation-registry.draft.json'
);
const FINAL_NAV = path.join(WORKSPACE_ROOT, 'src/data/static-demo/demo-navigation-registry.json');

const BLOG_ARTICLE_URLS = {
  'FP0002-DEMO-PG-016': '/stati/statya-1/',
  'FP0002-DEMO-PG-014': '/stati/statya-2/',
  'FP0002-DEMO-PG-015': '/stati/statya-3/',
};

const RESERVED_CLIENT_NAMES = {
  'FP0002-DEMO-PG-034': 'Дополнительная услуга 1',
  'FP0002-DEMO-PG-035': 'Дополнительная услуга 2',
  'FP0002-DEMO-PG-036': 'Дополнительная услуга 3',
  'FP0002-DEMO-PG-050': 'Дополнительное направление 1',
  'FP0002-DEMO-PG-051': 'Дополнительное направление 2',
};

function parseSourceRow(sourceRow) {
  if (!sourceRow || !sourceRow.includes('!')) {
    return { sheet: 'Структура', row: null };
  }
  const [sheet, row] = sourceRow.split('!');
  return { sheet, row: Number(row) };
}

function normalizeBreadcrumbName(name, pageId) {
  if (name === '/' || name === 'Главная') {
    return 'Главная';
  }
  if (name === 'Название' && RESERVED_CLIENT_NAMES[pageId]) {
    return RESERVED_CLIENT_NAMES[pageId];
  }
  return name;
}

function transformBreadcrumbs(breadcrumbs, urlById, nameById) {
  if (!Array.isArray(breadcrumbs) || breadcrumbs.length === 0) {
    return [];
  }

  return breadcrumbs.map((crumb, index) => {
    const pageId = crumb.page_id;
    const isHome = index === 0 || crumb.url === '/' || crumb.name === '/';
    const name = isHome
      ? 'Главная'
      : normalizeBreadcrumbName(
          nameById[pageId] || crumb.name,
          pageId
        );
    const url = isHome ? '/' : normalizeDemoUrl(urlById[pageId] || crumb.url);
    return {
      name,
      url,
      page_id: pageId,
      current: false,
    };
  });
}

function buildFinalRegistryFromDraft() {
  const draft = JSON.parse(fs.readFileSync(DRAFT_REGISTRY, 'utf8'));
  const interimPages = draft.pages.map((page) => {
    const sourceUrl = page.url ? page.url : null;
    let demoUrl = sourceUrl ? normalizeDemoUrl(sourceUrl) : page.url;
    let normalizationStatus = 'EXPLICIT';

    if (BLOG_ARTICLE_URLS[page.page_id]) {
      demoUrl = BLOG_ARTICLE_URLS[page.page_id];
      normalizationStatus = 'NORMALIZED_FOR_CLIENT_DEMO';
    } else if (
      sourceUrl &&
      (sourceUrl.includes('specyalisty') ||
        sourceUrl.includes('pilzovatelyu') ||
        sourceUrl.includes('//'))
    ) {
      normalizationStatus = 'NORMALIZED_FOR_CLIENT_DEMO';
    }

    const isReserved = page.raw_name === 'Название';
    const clientDemoName = isReserved
      ? RESERVED_CLIENT_NAMES[page.page_id]
      : page.normalized_name || page.raw_name;

    let title = page.title;
    let h1 = page.h1;
    if (isReserved && RESERVED_CLIENT_NAMES[page.page_id]) {
      const neutral = RESERVED_CLIENT_NAMES[page.page_id];
      title = `${neutral} — Шпиговский Дом`;
      h1 = neutral;
      normalizationStatus = 'RESERVED_SOURCE_SLOT_NORMALIZED_FOR_CLIENT_DEMO';
    }

    if (page.template === 'HOME_PAGE_TEMPLATE') {
      h1 = null;
    } else if (h1 === '/') {
      h1 = null;
    }

    return {
      draft: page,
      id: page.page_id,
      source: {
        sheet: parseSourceRow(page.source_row).sheet,
        row: parseSourceRow(page.source_row).row,
        raw_name: page.raw_name,
        raw_url: page.raw_url || sourceUrl,
        source_url: sourceUrl,
      },
      name: isReserved ? RESERVED_CLIENT_NAMES[page.page_id] : page.normalized_name || page.raw_name,
      client_demo_name: clientDemoName,
      template: page.template,
      parent_resolved: page.parent_resolved ? normalizeDemoUrl(page.parent_resolved) : null,
      level: page.hierarchy_level,
      menu: Boolean(page.menu_presence),
      footer: Boolean(
        page.footer_presence ||
          (page.source_row && String(page.source_row).includes('footer.html'))
      ),
      url: demoUrl,
      output: urlToOutputPath(demoUrl),
      title,
      h1,
      eyebrow:
        page.template === 'SERVICE_SUBDIVISION_INTERNAL_PAGE' ||
        page.template === 'SERVICE_LEAF_INTERNAL_PAGE'
          ? 'Заболевания, которые мы\u00a0лечим'
          : null,
      placeholder_message: page.placeholder_message || (page.template === 'PLACEHOLDER_PAGE'
        ? 'Раздел скоро будет опубликован'
        : null),
      visibility: isReserved ? 'HIDDEN_FROM_PRIMARY_NAV' : 'VISIBLE',
      normalization_status: normalizationStatus,
      breadcrumbs_raw: page.breadcrumbs || [],
    };
  });

  const urlById = Object.fromEntries(interimPages.map((p) => [p.id, p.url]));
  const nameById = Object.fromEntries(interimPages.map((p) => [p.id, p.client_demo_name]));

  interimPages.forEach((p) => {
    if (p.parent_resolved) {
      const parent = interimPages.find((candidate) => candidate.url === p.parent_resolved);
      p.parent_id = parent ? parent.id : null;
    } else {
      p.parent_id = null;
    }
  });

  const pages = interimPages.map((p) => {
    const breadcrumbs = transformBreadcrumbs(p.breadcrumbs_raw, urlById, nameById).map((crumb, index, arr) => ({
      name: crumb.name,
      url: crumb.url,
      current: index === arr.length - 1,
    }));

    if (p.template === 'HOME_PAGE_TEMPLATE') {
      return {
        id: p.id,
        source: p.source,
        name: p.name,
        client_demo_name: p.client_demo_name,
        template: p.template,
        parent_id: null,
        level: p.level,
        menu: p.menu,
        footer: p.footer,
        url: p.url,
        output: p.output,
        title: p.title,
        h1: null,
        eyebrow: null,
        breadcrumbs: [],
        placeholder_message: null,
        visibility: p.visibility,
        normalization_status: p.normalization_status,
      };
    }

    return {
      id: p.id,
      source: p.source,
      name: p.name,
      client_demo_name: p.client_demo_name,
      template: p.template,
      parent_id: p.parent_id,
      level: p.level,
      menu: p.menu,
      footer: p.footer || false,
      url: p.url,
      output: p.output,
      title: p.title,
      h1: p.h1,
      eyebrow: p.eyebrow,
      breadcrumbs,
      placeholder_message: p.placeholder_message,
      visibility: p.visibility,
      normalization_status: p.normalization_status,
    };
  });

  return {
    meta: {
      version: 'pass-2-final',
      generated_from: 'demo-page-registry.draft.json',
      page_count: pages.length,
      planning_commit: '797dab58',
      operator_decisions_applied: true,
    },
    pages,
  };
}

function buildFinalNavigationFromDraft(urlById) {
  const draft = JSON.parse(fs.readFileSync(DRAFT_NAV, 'utf8'));
  const links = draft.links.map((link) => {
    const targetUrl = normalizeDemoUrl(urlById[link.target_page_id] || link.target_url);
    let normalizationStatus = 'EXPLICIT';
    if (link.target_url && link.target_url !== targetUrl) {
      normalizationStatus = 'NORMALIZED_FOR_CLIENT_DEMO';
    }
    return {
      ...link,
      source_url: link.target_url,
      target_url: targetUrl,
      normalization_status: normalizationStatus,
    };
  });

  return {
    meta: {
      version: 'pass-2-final',
      generated_from: 'demo-navigation-registry.draft.json',
      link_count: links.length,
    },
    links,
  };
}

function ensureFinalRegistries({ rebuildNavigation = false } = {}) {
  const registry = buildFinalRegistryFromDraft();

  fs.mkdirSync(path.dirname(FINAL_REGISTRY), { recursive: true });
  fs.writeFileSync(FINAL_REGISTRY, `${JSON.stringify(registry, null, 2)}\n`, 'utf8');

  let navigation;
  if (rebuildNavigation) {
    const urlById = Object.fromEntries(registry.pages.map((p) => [p.id, p.url]));
    navigation = buildFinalNavigationFromDraft(urlById);
    fs.writeFileSync(FINAL_NAV, `${JSON.stringify(navigation, null, 2)}\n`, 'utf8');
  } else if (fs.existsSync(FINAL_NAV)) {
    navigation = JSON.parse(fs.readFileSync(FINAL_NAV, 'utf8'));
  } else {
    const urlById = Object.fromEntries(registry.pages.map((p) => [p.id, p.url]));
    navigation = buildFinalNavigationFromDraft(urlById);
    fs.writeFileSync(FINAL_NAV, `${JSON.stringify(navigation, null, 2)}\n`, 'utf8');
  }

  return { registry, navigation };
}

function loadRegistry() {
  if (!fs.existsSync(FINAL_REGISTRY)) {
    return ensureFinalRegistries().registry;
  }
  return JSON.parse(fs.readFileSync(FINAL_REGISTRY, 'utf8'));
}

module.exports = {
  WORKSPACE_ROOT,
  FINAL_REGISTRY,
  FINAL_NAV,
  ensureFinalRegistries,
  loadRegistry,
  buildFinalRegistryFromDraft,
};
