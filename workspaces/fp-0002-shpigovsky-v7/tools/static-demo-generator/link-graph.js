'use strict';

const { normalizeDemoUrl } = require('./path-utils');
const { normalizeLabel } = require('./navigation-loader');

const TOP_LEVEL_NAV = {
  home: { pageId: 'FP0002-DEMO-PG-001', url: '/', labels: ['главная'] },
  uslugi: {
    pageId: 'FP0002-DEMO-PG-002',
    url: '/uslugi/',
    labels: ['лечение и профилактика', 'услуги'],
    headerLabel: 'Лечение и профилактика',
  },
  genotipirovanie: {
    pageId: 'FP0002-DEMO-PG-003',
    url: '/uslugi/genotipirovanie/',
    labels: ['генотипирование'],
  },
  specialisty: {
    pageId: 'FP0002-DEMO-PG-004',
    url: '/specialisty/',
    labels: ['специалисты'],
  },
  oCentre: {
    pageId: 'FP0002-DEMO-PG-005',
    url: '/o-centre/',
    labels: ['о центре'],
  },
  otzyvy: {
    pageId: 'FP0002-DEMO-PG-006',
    url: '/otzyvy/',
    labels: ['отзывы'],
  },
  stati: {
    pageId: 'FP0002-DEMO-PG-007',
    url: '/blog/',
    labels: ['статьи', 'блог'],
  },
  kontakty: {
    pageId: 'FP0002-DEMO-PG-008',
    url: '/kontakty/',
    labels: ['контакты'],
  },
};

const CARD_LABEL_ALIASES = {
  'алкогольная зависимость': ['лечение алкогольной зависимости', 'алкоголь'],
  'наркотическая зависимость': ['лечение наркотической зависимости', 'наркотики'],
  'лекарственная зависимость': ['лечение лекарственной зависимости', 'лекарства'],
  'поведенческие зависимости': ['поведенческие зависимости', 'лечение поведенческой зависимости'],
  депрессия: ['депрессия'],
  'птср (посттравматическое стрессовое расстройство)': ['птср', 'посттравматическое стрессовое расстройство'],
  'эмоциональное выгорание': ['эмоциональное выгорание', 'эмомциональное выгорание'],
  'тревожные расстройства': ['тревожные расстройства'],
  'расстройства сна': ['расстройства сна'],
  травма: ['травма'],
  'нервная анорексия': ['нервная анорексия', 'анорексия'],
  'нервная булимия': ['нервная булимия', 'булимия'],
  'компульсивное переедание': ['компульсивное переедание', 'коммпульсивное переедание'],
};

const HIDDEN_ORPHAN_PAGE_IDS = new Set([
  'FP0002-DEMO-PG-034',
  'FP0002-DEMO-PG-035',
  'FP0002-DEMO-PG-036',
  'FP0002-DEMO-PG-050',
  'FP0002-DEMO-PG-051',
]);

function resolveActiveNavKey(page) {
  if (!page || page.template === 'HOME_PAGE_TEMPLATE') {
    return null;
  }
  const url = normalizeDemoUrl(page.url);
  if (url.startsWith('/uslugi/')) {
    return 'uslugi';
  }
  if (url.startsWith('/specialisty')) {
    return 'specialisty';
  }
  if (url.startsWith('/o-centre')) {
    return 'oCentre';
  }
  if (url.startsWith('/otzyvy')) {
    return 'otzyvy';
  }
  if (url.startsWith('/blog') || url.startsWith('/stati')) {
    return 'stati';
  }
  if (url.startsWith('/kontakty')) {
    return 'kontakty';
  }
  return null;
}

function matchChildByCardLabel(label, children) {
  const norm = normalizeLabel(label);
  if (!norm || !children.length) {
    return null;
  }

  const direct = children.find((child) => {
    const childNorm = normalizeLabel(child.client_demo_name || child.name);
    return childNorm === norm || norm.includes(childNorm) || childNorm.includes(norm);
  });
  if (direct) {
    return direct;
  }

  const aliases = CARD_LABEL_ALIASES[norm] || [];
  for (const alias of aliases) {
    const match = children.find((child) => {
      const childNorm = normalizeLabel(child.client_demo_name || child.name);
      return childNorm.includes(alias) || alias.includes(childNorm);
    });
    if (match) {
      return match;
    }
  }

  return null;
}

function getVisibleChildren(page, indexes) {
  const children = indexes.childrenByParentId.get(page.id) || [];
  return children.filter((child) => child.visibility !== 'HIDDEN_FROM_PRIMARY_NAV');
}

function buildDirectedGraph(indexes) {
  const edges = [];
  indexes.pages.forEach((page) => {
    if (page.parent_id) {
      edges.push({ from: page.parent_id, to: page.id, type: 'parent_child' });
    }
  });
  return edges;
}

function analyzeReachability(indexes, navigation) {
  const adjacency = new Map();
  const addEdge = (fromId, toId) => {
    if (!fromId || !toId) {
      return;
    }
    if (!adjacency.has(fromId)) {
      adjacency.set(fromId, new Set());
    }
    adjacency.get(fromId).add(toId);
  };

  indexes.pages.forEach((page) => {
    if (page.parent_id) {
      addEdge(page.id, page.parent_id);
      addEdge(page.parent_id, page.id);
    }
  });

  (navigation.links || []).forEach((link) => {
    if (
      link.status === 'HIDDEN_FOR_DEMO' ||
      link.status === 'UNRESOLVED_BLOCKING' ||
      link.status === 'ACTION_CONTROL_PRESERVED'
    ) {
      return;
    }
    if (!link.target_page_id) {
      return;
    }
    if (link.source_page_id) {
      addEdge(link.source_page_id, link.target_page_id);
    }
    if (link.source_scope === 'all_pages') {
      addEdge('FP0002-DEMO-PG-001', link.target_page_id);
    }
  });

  const homeId = 'FP0002-DEMO-PG-001';
  const visited = new Set();
  const queue = [homeId];
  while (queue.length) {
    const current = queue.shift();
    if (visited.has(current)) {
      continue;
    }
    visited.add(current);
    const next = adjacency.get(current);
    if (next) {
      next.forEach((id) => {
        if (!visited.has(id)) {
          queue.push(id);
        }
      });
    }
  }

  const allIds = indexes.pages.map((p) => p.id);
  const intentionallyHidden = allIds.filter((id) => {
    const page = indexes.byId.get(id);
    return page.visibility === 'HIDDEN_FROM_PRIMARY_NAV' || HIDDEN_ORPHAN_PAGE_IDS.has(id);
  });
  const unexpectedOrphans = allIds.filter(
    (id) => !visited.has(id) && !intentionallyHidden.includes(id)
  );

  return {
    reachable: [...visited],
    intentionallyHidden,
    unexpectedOrphans,
    totalPages: allIds.length,
  };
}

module.exports = {
  TOP_LEVEL_NAV,
  CARD_LABEL_ALIASES,
  HIDDEN_ORPHAN_PAGE_IDS,
  resolveActiveNavKey,
  matchChildByCardLabel,
  getVisibleChildren,
  buildDirectedGraph,
  analyzeReachability,
};
