'use strict';

const fs = require('fs');
const path = require('path');

const { WORKSPACE_ROOT } = require('./registry-loader');
const { normalizeDemoUrl } = require('./path-utils');
const { getVisibleChildren, HIDDEN_ORPHAN_PAGE_IDS } = require('./link-graph');
const { STATIC_SELECTOR_TARGETS } = require('./link-rewriter');
const { HOME_TREATMENT_PANELS } = require('./home-treatment-links');

const HUB_SECTION_PARENTS = {
  'services-category-addictions': 'FP0002-DEMO-PG-031',
  'services-category-mental-health': 'FP0002-DEMO-PG-029',
  'services-category-eating-disorders': 'FP0002-DEMO-PG-030',
  'services-category-genotyping': 'FP0002-DEMO-PG-003',
  'service-subdivision-dependencies': null,
};

function makeLink(partial) {
  return {
    id: partial.id,
    surface: partial.surface,
    label: partial.label,
    current_label: partial.label,
    source_scope: partial.source_scope || 'all_pages',
    source_page_id: partial.source_page_id || null,
    source_label: partial.source_label || partial.label,
    target_page_id: partial.target_page_id,
    target_url: partial.target_url,
    mapping_method: partial.mapping_method || 'EXPLICIT_PAGE_ID',
    confidence: partial.confidence || 'HIGH',
    visibility: partial.visibility || 'VISIBLE',
    status: partial.status || 'RESOLVED',
    source_of_mapping: partial.source_of_mapping || 'pass-3-navigation-registry-builder',
    normalization_status: partial.normalization_status || 'EXPLICIT',
  };
}

function buildPass3NavigationRegistry(registry) {
  const links = [];
  let seq = 1;
  const nextId = (prefix) => {
    const id = `NAV-${prefix}-${String(seq).padStart(4, '0')}`;
    seq += 1;
    return id;
  };

  const byId = new Map(registry.pages.map((p) => [p.id, p]));

  const headerItems = [
    { label: 'Лечение и профилактика', target: 'FP0002-DEMO-PG-002' },
    { label: 'Зависимости', target: 'FP0002-DEMO-PG-003' },
    { label: 'Специалисты', target: 'FP0002-DEMO-PG-004' },
    { label: 'О центре', target: 'FP0002-DEMO-PG-005' },
    { label: 'Отзывы', target: 'FP0002-DEMO-PG-006' },
    { label: 'Статьи', target: 'FP0002-DEMO-PG-007' },
    { label: 'Контакты', target: 'FP0002-DEMO-PG-008' },
  ];

  headerItems.forEach((item) => {
    const page = byId.get(item.target);
    ['desktop_header', 'mobile_header'].forEach((surface) => {
      links.push(
        makeLink({
          id: nextId(surface === 'desktop_header' ? 'HDR' : 'MOB'),
          surface,
          label: item.label,
          source_scope: 'all_pages',
          target_page_id: item.target,
          target_url: page.url,
          mapping_method: 'EXPLICIT_PAGE_ID',
        })
      );
    });
  });

  links.push(
    makeLink({
      id: nextId('LOGO'),
      surface: 'logo',
      label: 'Шпиговский дом',
      source_scope: 'all_pages',
      target_page_id: 'FP0002-DEMO-PG-001',
      target_url: '/',
      mapping_method: 'EXPLICIT_PAGE_ID',
    })
  );

  const footerGroups = [
    {
      surface: 'footer_services',
      items: [
        { label: 'Зависимости и пристрастия', target: 'FP0002-DEMO-PG-031' },
        { label: 'Психическое здоровье', target: 'FP0002-DEMO-PG-029' },
        { label: 'Расстройства пищевого поведения', target: 'FP0002-DEMO-PG-030' },
        { label: 'Зависимости', target: 'FP0002-DEMO-PG-003' },
      ],
    },
    {
      surface: 'footer_about',
      items: [
        { label: 'О нас', target: 'FP0002-DEMO-PG-019' },
        { label: 'Программа лечения', target: 'FP0002-DEMO-PG-020' },
        { label: 'Галерея о доме', target: 'FP0002-DEMO-PG-017' },
        { label: 'Специалистам', target: 'FP0002-DEMO-PG-022' },
        { label: 'Родственникам', target: 'FP0002-DEMO-PG-021' },
      ],
    },
    {
      surface: 'footer_legal',
      items: [
        { label: 'Политика конфиденциальности', target: 'FP0002-DEMO-PG-012' },
        { label: 'Пользовательское соглашение', target: 'FP0002-DEMO-PG-013' },
        { label: 'Согласие на обработку персональных данных', target: 'FP0002-DEMO-PG-010' },
        { label: 'Политика Cookie-файлов', target: 'FP0002-DEMO-PG-011' },
      ],
    },
  ];

  footerGroups.forEach((group) => {
    group.items.forEach((item) => {
      const page = byId.get(item.target);
      links.push(
        makeLink({
          id: nextId('FTR'),
          surface: group.surface,
          label: item.label,
          source_scope: 'all_pages',
          target_page_id: item.target,
          target_url: page.url,
          mapping_method: 'EXPLICIT_PAGE_ID',
        })
      );
    });
  });

  STATIC_SELECTOR_TARGETS.forEach((target) => {
    links.push(
      makeLink({
        id: nextId('CTA'),
        surface: 'page_navigation_cta',
        label: target.selector,
        source_scope: 'contextual_sections',
        target_page_id: [...byId.values()].find((p) => p.url === target.url)?.id || null,
        target_url: target.url,
        mapping_method: 'SELECTOR_CLASS',
      })
    );
  });

  Object.entries(HOME_TREATMENT_PANELS).forEach(([panelId, panelLinks]) => {
    panelLinks.forEach((item) => {
      const targetPage = [...byId.values()].find((p) => p.url === item.url);
      links.push(
        makeLink({
          id: nextId('HOME'),
          surface: 'home_treatment_prevention',
          label: item.label,
          source_scope: 'FP0002-DEMO-PG-001',
          source_page_id: 'FP0002-DEMO-PG-001',
          source_label: panelId,
          target_page_id: targetPage ? targetPage.id : null,
          target_url: item.url,
          mapping_method: 'HOME_TREATMENT_PANEL',
          normalization_status: 'OPERATOR_URGENT_TASK_001',
        })
      );
    });
  });

  ['Telegram', 'WhatsApp', 'Max'].forEach((label) => {
    links.push(
      makeLink({
        id: nextId('MSG'),
        surface: 'messenger_action',
        label,
        source_scope: 'header_footer',
        target_page_id: null,
        target_url: '#',
        mapping_method: 'ACTION_CONTROL',
        status: 'ACTION_CONTROL_PRESERVED',
      })
    );
  });

  const indexes = {
    byId,
    childrenByParentId: new Map(),
  };
  registry.pages.forEach((page) => {
    if (page.parent_id) {
      if (!indexes.childrenByParentId.has(page.parent_id)) {
        indexes.childrenByParentId.set(page.parent_id, []);
      }
      indexes.childrenByParentId.get(page.parent_id).push(page);
    }
  });

  registry.pages.forEach((page) => {
    if (page.template === 'SERVICES_HUB_INTERNAL_PAGE') {
      Object.entries(HUB_SECTION_PARENTS).forEach(([sectionId, parentId]) => {
        if (!parentId) {
          return;
        }
        const parent = byId.get(parentId);
        const children = getVisibleChildren(parent, indexes);
        children.forEach((child) => {
          links.push(
            makeLink({
              id: nextId('HUB'),
              surface: 'services_hub_card',
              label: child.client_demo_name,
              source_page_id: page.id,
              source_scope: page.id,
              source_label: child.client_demo_name,
              target_page_id: child.id,
              target_url: child.url,
              mapping_method: 'LABEL_AND_HIERARCHY',
            })
          );
        });
      });
    }

    if (page.template === 'SERVICE_SUBDIVISION_INTERNAL_PAGE') {
      const children = getVisibleChildren(page, indexes);
      children.forEach((child) => {
        links.push(
          makeLink({
            id: nextId('SUB'),
            surface: 'subdivision_card',
            label: child.client_demo_name,
            source_page_id: page.id,
            source_scope: page.id,
            source_label: child.client_demo_name,
            target_page_id: child.id,
            target_url: child.url,
            mapping_method: 'LABEL_AND_HIERARCHY',
          })
        );
      });
    }
  });

  registry.pages
    .filter((p) => p.visibility === 'HIDDEN_FROM_PRIMARY_NAV' || HIDDEN_ORPHAN_PAGE_IDS.has(p.id))
    .forEach((page) => {
      links.push(
        makeLink({
          id: nextId('HID'),
          surface: 'reserved_placeholder',
          label: page.client_demo_name,
          source_scope: page.id,
          source_page_id: page.id,
          target_page_id: page.id,
          target_url: page.url,
          mapping_method: 'RESERVED_SLOT',
          visibility: 'HIDDEN_FOR_DEMO',
          status: 'HIDDEN_FOR_DEMO',
        })
      );
    });

  const statusCounts = links.reduce((acc, link) => {
    acc[link.status] = (acc[link.status] || 0) + 1;
    return acc;
  }, {});

  return {
    meta: {
      version: 'pass-3-final',
      generated_from: 'demo-page-registry.json',
      link_count: links.length,
      status_counts: statusCounts,
      unresolved_blocking: statusCounts.UNRESOLVED_BLOCKING || 0,
    },
    links,
  };
}

function writePass3NavigationRegistry(registry) {
  const nav = buildPass3NavigationRegistry(registry);
  const outPath = path.join(WORKSPACE_ROOT, 'src/data/static-demo/demo-navigation-registry.json');
  fs.writeFileSync(outPath, `${JSON.stringify(nav, null, 2)}\n`, 'utf8');
  return nav;
}

if (require.main === module) {
  const registry = JSON.parse(
    fs.readFileSync(path.join(WORKSPACE_ROOT, 'src/data/static-demo/demo-page-registry.json'), 'utf8')
  );
  const nav = writePass3NavigationRegistry(registry);
  console.log(`Built navigation registry: ${nav.links.length} links`);
}

module.exports = {
  buildPass3NavigationRegistry,
  writePass3NavigationRegistry,
};
