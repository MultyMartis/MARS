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

  // Rewrite quoted relative asset roots used in src/href/preload links.
  result = result.replace(/(["'])(?:\.\/)?assets\//g, `$1${prefix}`);

  // Rewrite unquoted url(...) references if present in inline markup.
  result = result.replace(/url\((["']?)(?:\.\/)?assets\//g, `url($1${prefix}`);

  // Remaining bare assets/ tokens outside absolute URLs.
  result = result.replace(/(?<![\w/"'=])assets\//g, prefix);

  result = result.replace(/\/assets\/assets\//g, '/assets/');
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
