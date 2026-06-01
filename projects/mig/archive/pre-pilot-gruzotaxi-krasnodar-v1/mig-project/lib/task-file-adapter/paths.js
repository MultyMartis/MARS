"use strict";

const path = require("path");

const REPO_ROOT = path.resolve(__dirname, "..", "..", "..", "..");

function getMigInboxRoot() {
  const env = process.env.MIG_INBOX_ROOT;
  if (env && String(env).trim()) {
    return path.resolve(String(env).trim());
  }
  return path.join(REPO_ROOT, "incoming", "mig");
}

function inboxSubdir(name) {
  return path.join(getMigInboxRoot(), name);
}

function getRegistryPath() {
  return path.join(inboxSubdir("registry"), "request-index.json");
}

const REQUEST_FILENAME_RE = /^request-[a-zA-Z0-9][a-zA-Z0-9_-]*\.json$/;

function isProcessableRequestFilename(basename) {
  if (!basename || typeof basename !== "string") return false;
  if (basename.startsWith("example-")) return false;
  return REQUEST_FILENAME_RE.test(basename);
}

module.exports = {
  REPO_ROOT,
  getMigInboxRoot,
  inboxSubdir,
  getRegistryPath,
  REQUEST_FILENAME_RE,
  isProcessableRequestFilename,
};
