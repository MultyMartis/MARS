"use strict";

const fs = require("fs");
const path = require("path");

const DEFAULT_EXCLUSIONS_PATH = path.join(
  __dirname,
  "..",
  "..",
  "config",
  "landing-nav-noise-exclusions-v2.json"
);

function normalizeNavText(text) {
  if (!text || typeof text !== "string") {
    return "";
  }
  return text
    .toLowerCase()
    .replace(/\s+/g, " ")
    .replace(/[«»"']/g, "")
    .trim();
}

function loadNavNoiseConfig(configPath) {
  const filePath = configPath || DEFAULT_EXCLUSIONS_PATH;
  return JSON.parse(fs.readFileSync(filePath, "utf8"));
}

/**
 * Rules-only: nav section headings must not become OFFERS.
 */
function isNavNoise(text, config) {
  const normalized = normalizeNavText(text);
  if (!normalized) {
    return false;
  }
  const cfg = config || loadNavNoiseConfig();
  if (cfg.exact_matches_normalized.includes(normalized)) {
    return true;
  }
  for (const prefix of cfg.prefix_matches_normalized || []) {
    if (normalized.startsWith(prefix)) {
      return true;
    }
  }
  if (/^вопросы и ответы\b/.test(normalized)) {
    return true;
  }
  if (/^отзывы\b/.test(normalized) && normalized.length < 40) {
    return true;
  }
  return false;
}

function filterOfferCandidates(candidates, options = {}) {
  const config = options.config || loadNavNoiseConfig(options.configPath);
  const kept = [];
  const excluded = [];

  for (const item of candidates) {
    const text = item.text || item;
    if (isNavNoise(text, config)) {
      excluded.push({
        text,
        excluded_reason: config.excluded_reason || "nav_noise",
        snapshot_field: item.snapshot_field || null,
      });
    } else {
      kept.push(item);
    }
  }

  return { kept, excluded };
}

module.exports = {
  normalizeNavText,
  loadNavNoiseConfig,
  isNavNoise,
  filterOfferCandidates,
  DEFAULT_EXCLUSIONS_PATH,
};
