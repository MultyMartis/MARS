"use strict";

/**
 * n8n Code node snippets for MIG Session Spine v0.1.
 * Each export is the jsCode body for one workflow node.
 * Requires self-hosted n8n with filesystem access and:
 *   MIG_LIB_ROOT, MIG_SESSION_ROOT
 * Optional n8n env: NODE_FUNCTION_ALLOW_BUILTIN=fs,path,crypto
 *                   NODE_FUNCTION_ALLOW_EXTERNAL=*
 */

function libRootExpr() {
  return "'C:/AI MARS/projects/mig/lib/session-spine'";
}

const snippets = {
  validateIntake: `
const path = require('path');
const libRoot = ${libRootExpr()};
const { validateIntake } = require(path.join(libRoot, 'validate-intake.js'));

const root = $input.first().json;
const body = root.body && typeof root.body === 'object' ? root.body : root;

let validated;
try {
  validated = validateIntake(body);
} catch (err) {
  return [{
    json: {
      status: 'error',
      code: err.code || 'VALIDATION_ERROR',
      message: err.message,
      details: err.details || null,
    },
  }];
}

return [{ json: { validated, status: 'ok' } }];
`.trim(),

  createManifest: `
const path = require('path');
const libRoot = ${libRootExpr()};
const { createInitialManifest } = require(path.join(libRoot, 'create-manifest.js'));

const item = $input.first().json;
if (item.status === 'error') {
  return [{ json: item }];
}

const manifest = createInitialManifest(item.validated);
return [{ json: { ...item, manifest } }];
`.trim(),

  createSessionFolder: `
const fs = require('fs');
const path = require('path');
const libRoot = ${libRootExpr()};
const { getSessionDir } = require(path.join(libRoot, 'paths.js'));

const item = $input.first().json;
if (item.status === 'error') {
  return [{ json: item }];
}

const sessionDir = getSessionDir(item.validated.session_id);
fs.mkdirSync(sessionDir, { recursive: true });

return [{
  json: {
    ...item,
    session_dir: sessionDir,
    folder_created: true,
  },
}];
`.trim(),

  serpInput: `
const item = $input.first().json;
if (item.status === 'error') {
  return [{ json: item }];
}

const validated = item.validated;
let serp_branch = 'fallback';
let serp_raw = null;

if (validated.manual_serp && typeof validated.manual_serp === 'object') {
  serp_branch = 'manual';
  serp_raw = validated.manual_serp;
} else if (
  validated.serp_provider_response &&
  typeof validated.serp_provider_response === 'object'
) {
  serp_branch = 'provider';
  serp_raw = validated.serp_provider_response;
}

return [{
  json: {
    ...item,
    serp_branch,
    serp_raw,
  },
}];
`.trim(),

  normalizeSerp: `
const path = require('path');
const libRoot = ${libRootExpr()};
const { pickSerpSource, normalizeSerp } = require(path.join(libRoot, 'normalize-serp.js'));

const item = $input.first().json;
if (item.status === 'error') {
  return [{ json: item }];
}

const source = pickSerpSource(item.validated);
const serp_result = normalizeSerp(item.validated, source);

return [{
  json: {
    ...item,
    serp_result,
    serp_mode: serp_result.source_mode,
  },
}];
`.trim(),

  researchPackDraft: `
const path = require('path');
const libRoot = ${libRootExpr()};
const { buildResearchPackDraft } = require(path.join(libRoot, 'build-research-pack.js'));

const item = $input.first().json;
if (item.status === 'error') {
  return [{ json: item }];
}

const research_pack_draft = buildResearchPackDraft(item.manifest, item.serp_result);

return [{
  json: {
    ...item,
    research_pack_draft,
  },
}];
`.trim(),

  finalizeManifest: `
const fs = require('fs');
const path = require('path');
const libRoot = ${libRootExpr()};
const { finalizeManifest } = require(path.join(libRoot, 'create-manifest.js'));
const { writeArtifacts } = require(path.join(libRoot, 'write-artifacts.js'));

const item = $input.first().json;
if (item.status === 'error') {
  return [{ json: item }];
}

const final_manifest = finalizeManifest(item.manifest, {
  mode: item.serp_result.source_mode,
  captured_at: item.serp_result.captured_at,
  safe_unknown: item.serp_result.safe_unknown,
});

const written = writeArtifacts(
  item.validated.session_id,
  final_manifest,
  item.serp_result,
  item.research_pack_draft
);

return [{
  json: {
    status: 'ok',
    session_id: item.validated.session_id,
    folder_path: written.session_dir,
    stage: final_manifest.stage,
    serp_mode: item.serp_result.source_mode,
    files: written.files,
  },
}];
`.trim(),
};

module.exports = snippets;
