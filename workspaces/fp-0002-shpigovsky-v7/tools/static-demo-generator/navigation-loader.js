'use strict';

const fs = require('fs');
const path = require('path');

const { WORKSPACE_ROOT } = require('./registry-loader');
const { normalizeDemoUrl } = require('./path-utils');

const FINAL_REGISTRY = path.join(WORKSPACE_ROOT, 'src/data/static-demo/demo-page-registry.json');
const FINAL_NAV = path.join(WORKSPACE_ROOT, 'src/data/static-demo/demo-navigation-registry.json');

function loadPageRegistry() {
  return JSON.parse(fs.readFileSync(FINAL_REGISTRY, 'utf8'));
}

function loadNavigationRegistry() {
  return JSON.parse(fs.readFileSync(FINAL_NAV, 'utf8'));
}

function buildPageIndexes(registry) {
  const pages = registry.pages || [];
  const byId = new Map();
  const byUrl = new Map();
  const byOutput = new Map();
  const childrenByParentId = new Map();

  pages.forEach((page) => {
    byId.set(page.id, page);
    byUrl.set(normalizeDemoUrl(page.url), page);
    byOutput.set(page.output, page);
    if (page.parent_id) {
      if (!childrenByParentId.has(page.parent_id)) {
        childrenByParentId.set(page.parent_id, []);
      }
      childrenByParentId.get(page.parent_id).push(page);
    }
  });

  childrenByParentId.forEach((children) => {
    children.sort((a, b) => a.url.localeCompare(b.url, 'ru'));
  });

  return { pages, byId, byUrl, byOutput, childrenByParentId };
}

function normalizeLabel(text) {
  return String(text || '')
    .replace(/\u00a0/g, ' ')
    .replace(/<[^>]+>/g, '')
    .replace(/\s+/g, ' ')
    .trim()
    .toLowerCase();
}

function loadNavigationContext() {
  const registry = loadPageRegistry();
  const navigation = loadNavigationRegistry();
  const indexes = buildPageIndexes(registry);

  const navByLabelSurface = new Map();
  (navigation.links || []).forEach((link) => {
    const key = `${link.surface}::${normalizeLabel(link.current_label || link.label)}`;
    navByLabelSurface.set(key, link);
  });

  return {
    registry,
    navigation,
    indexes,
    navByLabelSurface,
    normalizeLabel,
  };
}

module.exports = {
  FINAL_REGISTRY,
  FINAL_NAV,
  loadPageRegistry,
  loadNavigationRegistry,
  buildPageIndexes,
  loadNavigationContext,
  normalizeLabel,
};
