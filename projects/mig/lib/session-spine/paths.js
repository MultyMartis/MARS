"use strict";

const path = require("path");

function getSessionRoot() {
  let root = null;
  if (typeof process !== "undefined" && process.env) {
    root = process.env.MIG_SESSION_ROOT;
  }
  if (root && String(root).trim()) {
    return path.resolve(String(root).trim());
  }
  return path.resolve(__dirname, "..", "..", "sessions");
}

function getSessionDir(sessionId) {
  return path.join(getSessionRoot(), sessionId);
}

module.exports = {
  getSessionRoot,
  getSessionDir,
};
