'use strict';

const path = require('path');

function normalizeDemoUrl(url) {
  if (!url || typeof url !== 'string') {
    return url;
  }
  let normalized = url
    .replace(/specyalisty/g, 'specialisty')
    .replace(/pilzovatelyu/g, 'polzovatelyu');
  normalized = normalized.replace(/\/{2,}/g, '/');
  if (!normalized.startsWith('/')) {
    normalized = `/${normalized}`;
  }
  if (normalized.length > 1 && !normalized.endsWith('/')) {
    normalized = `${normalized}/`;
  }
  return normalized;
}

function urlToOutputPath(url) {
  const clean = normalizeDemoUrl(url);
  if (clean === '/') {
    return 'index.html';
  }
  const trimmed = clean.replace(/^\/|\/$/g, '');
  return path.posix.join(trimmed, 'index.html');
}

function outputPathToDistRelative(outputPath) {
  const normalized = outputPath.replace(/^dist[\\/]/, '').replace(/\\/g, '/');
  return normalized;
}

function depthFromOutput(outputRelative) {
  if (outputRelative === 'index.html') {
    return 0;
  }
  const dir = path.posix.dirname(outputRelative);
  return dir === '.' ? 0 : dir.split('/').length;
}

function rewriteAssetPathsToRoot(html, outputRelative) {
  const depth = depthFromOutput(outputRelative);
  if (depth === 0) {
    return html;
  }

  let result = html;
  const prefix = '/assets/';
  result = result.replace(/(?<![/"'=])assets\//g, prefix);
  result = result.replace(/href="\/assets\/assets\//g, 'href="/assets/');
  result = result.replace(/src="\/assets\/assets\//g, 'src="/assets/');
  return result;
}

function normalizeTypoUrlsInHtml(html) {
  return html
    .replace(/specyalisty/g, 'specialisty')
    .replace(/pilzovatelyu/g, 'polzovatelyu')
    .replace(/([^:])\/{2,}/g, '$1/');
}

module.exports = {
  normalizeDemoUrl,
  urlToOutputPath,
  outputPathToDistRelative,
  depthFromOutput,
  rewriteAssetPathsToRoot,
  normalizeTypoUrlsInHtml,
};
