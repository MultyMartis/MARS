'use strict';

const path = require('path');
const { WORKSPACE_ROOT } = require('./registry-loader');
const { loadPageRegistry, loadNavigationRegistry, buildPageIndexes } = require('./navigation-loader');
const { crawlGeneratedSite } = require('./link-validator');
const { writePass3Evidence } = require('./pass-3-evidence');

const registry = loadPageRegistry();
const navigation = loadNavigationRegistry();
const indexes = buildPageIndexes(registry);
const crawl = crawlGeneratedSite({
  distDir: path.join(WORKSPACE_ROOT, 'dist'),
  registry,
  indexes,
});

console.log(JSON.stringify(crawl.stats, null, 2));
writePass3Evidence({ registry, navigation, receipt: {}, durationMs: 0 });
