"use strict";

function nowIso() {
  return new Date().toISOString();
}

function mergeSafeUnknown(manifest, entries) {
  const incoming = Array.isArray(entries) ? entries : entries ? [entries] : [];
  const existing = manifest.safe_unknown || [];
  const merged = [...existing];
  for (const item of incoming) {
    if (item && !merged.includes(item)) {
      merged.push(item);
    }
  }
  return merged;
}

function appendError(manifest, errorEntry) {
  const errors = [...(manifest.errors || [])];
  errors.push(errorEntry);
  return errors;
}

/**
 * Apply partial manifest update; always bumps updated_at.
 */
function updateSessionManifest(manifest, patch) {
  const next = {
    ...manifest,
    ...patch,
    updated_at: nowIso(),
  };

  if (patch.serp) {
    next.serp = { ...manifest.serp, ...patch.serp };
  }
  if (patch.competitor_discovery) {
    next.competitor_discovery = { ...manifest.competitor_discovery, ...patch.competitor_discovery };
  }
  if (patch.website_acquisition) {
    next.website_acquisition = { ...manifest.website_acquisition, ...patch.website_acquisition };
  }
  if (patch.landing_analysis) {
    next.landing_analysis = { ...manifest.landing_analysis, ...patch.landing_analysis };
  }
  if (patch.pack) {
    next.pack = { ...manifest.pack, ...patch.pack };
  }
  if (patch.artifacts) {
    next.artifacts = { ...manifest.artifacts, ...patch.artifacts };
  }
  if (patch.coverage) {
    next.coverage = { ...manifest.coverage, ...patch.coverage };
  }
  if (patch.runtime_metadata) {
    next.runtime_metadata = { ...manifest.runtime_metadata, ...patch.runtime_metadata };
  }
  if (patch.pass_status) {
    next.pass_status = { ...manifest.pass_status, ...patch.pass_status };
  }
  if (patch.approval) {
    next.approval = { ...manifest.approval, ...patch.approval };
  }
  if (patch.safe_unknown) {
    next.safe_unknown = mergeSafeUnknown(manifest, patch.safe_unknown);
  }
  if (patch.errors) {
    next.errors = [...(manifest.errors || []), ...patch.errors];
  }

  return next;
}

function setStagePhase(manifest, { stage, phase, status, last_pass }) {
  const patch = { stage, phase };
  if (status) {
    patch.status = status;
  }
  if (last_pass) {
    patch.runtime_metadata = {
      ...manifest.runtime_metadata,
      last_pass,
    };
  }
  return updateSessionManifest(manifest, patch);
}

module.exports = {
  mergeSafeUnknown,
  appendError,
  updateSessionManifest,
  setStagePhase,
};
