/**
 * Evidence pack manifest generators for MetaBOT SEO Content Agent Beta v14 exports.
 */

/**
 * @typedef {Object} WorkflowExportRecord
 * @property {string} name
 * @property {string} id
 * @property {boolean} active
 * @property {Record<string, unknown>} sanitized
 * @property {import('../sanitize-workflow.mjs').SanitizationStats} stats
 * @property {string} sanitizedFile
 */

/**
 * @param {unknown[]} nodes
 * @returns {string}
 */
function inferExternalService(node) {
  const type = String(node?.type || '');
  if (type.includes('telegram')) return 'Telegram';
  if (type.includes('googleSheets') || type.includes('google-sheet')) return 'Google Sheets';
  if (type.includes('openAi') || type.includes('openRouter') || type.includes('lmChat')) {
    return 'OpenRouter/LLM';
  }
  if (type.includes('httpRequest')) return 'HTTP';
  if (type.includes('webhook')) return 'Webhook';
  if (type.includes('executeWorkflow')) return 'n8n sub-workflow';
  return '';
}

/**
 * @param {unknown} node
 * @returns {string}
 */
function inferLikelyRole(node) {
  const name = String(node?.name || '').toLowerCase();
  const type = String(node?.type || '').toLowerCase();
  if (name.includes('route') || type.includes('switch')) return 'routing';
  if (name.includes('lock')) return 'lock/state';
  if (name.includes('admin') || name.includes('stop')) return 'admin/recovery';
  if (name.includes('telegram') || type.includes('telegram')) return 'telegram IO';
  if (name.includes('seoqa') || name.includes('factcheck') || name.includes('qa')) {
    return 'quality layer';
  }
  if (type.includes('code')) return 'code transform';
  if (type.includes('webhook')) return 'trigger/handoff';
  if (type.includes('executeworkflow')) return 'cross-workflow handoff';
  if (type.includes('googlesheets')) return 'storage';
  if (type.includes('openai') || type.includes('lmchat')) return 'LLM generation';
  return 'processing';
}

/**
 * @param {unknown} node
 * @returns {boolean}
 */
function nodeHasCredentials(node) {
  const params = node?.parameters;
  if (!params || typeof params !== 'object') return false;
  return (
    'credentials' in /** @type {Record<string, unknown>} */ (params) ||
    'authentication' in /** @type {Record<string, unknown>} */ (params)
  );
}

/**
 * @param {unknown} node
 * @returns {boolean}
 */
function nodeHasCode(node) {
  const params = node?.parameters;
  if (!params || typeof params !== 'object') return false;
  const p = /** @type {Record<string, unknown>} */ (params);
  return typeof p.jsCode === 'string' || typeof p.code === 'string';
}

/**
 * @param {unknown} node
 * @returns {boolean}
 */
function nodeHasPrompt(node) {
  const params = node?.parameters;
  if (!params || typeof params !== 'object') return false;
  const p = /** @type {Record<string, unknown>} */ (params);
  const keys = ['prompt', 'text', 'messages', 'systemMessage', 'userMessage', 'input'];
  return keys.some((k) => k in p);
}

/**
 * @param {unknown} node
 * @returns {string}
 */
function getNodeContent(node) {
  const params = node?.parameters;
  if (!params || typeof params !== 'object') return '';
  const p = /** @type {Record<string, unknown>} */ (params);
  if (typeof p.jsCode === 'string') return p.jsCode;
  if (typeof p.code === 'string') return p.code;
  if (typeof p.prompt === 'string') return p.prompt;
  if (typeof p.text === 'string') return p.text;
  if (typeof p.systemMessage === 'string') return p.systemMessage;
  try {
    return JSON.stringify(p.messages ?? p);
  } catch {
    return '';
  }
}

/**
 * @param {string} content
 * @returns {string}
 */
function secretScanResult(content) {
  if (!content) return 'empty';
  const risky = [
    /\bsk-[A-Za-z0-9_-]{10,}\b/,
    /\bBearer\s+[A-Za-z0-9._-]{10,}\b/i,
    /\b\d{8,10}:[A-Za-z0-9_-]{30,}\b/,
    /docs\.google\.com\/spreadsheets\/d\/(?!REDACTED_SHEET_ID)[a-zA-Z0-9_-]{10,}/i,
    /"documentId"\s*:\s*\{[^}]*"value"\s*:\s*"(?!REDACTED_SHEET_ID)[a-zA-Z0-9_-]{20,}"/i,
    /n8n\.ai-metacode\.com\/webhook/i,
  ];
  return risky.some((r) => r.test(content)) ? 'RISK_REMAINING' : 'CLEAN_AFTER_SANITIZE';
}

/**
 * @param {WorkflowExportRecord[]} exports_
 * @param {Object} options
 * @param {string} options.date
 * @param {'LIVE_API_EXPORT' | 'DRY_RUN_ONLY'} options.classification
 * @param {boolean} options.safeToCommit
 * @param {Array<{ file: string, pattern: string }>} options.securityFindings
 * @returns {Record<string, string>}
 */
export function generateManifestDocs(exports_, options) {
  const { date, classification, safeToCommit, securityFindings } = options;

  return {
    'EXPORT-MANIFEST.md': renderExportManifest(exports_, date, classification),
    'SANITIZATION-REPORT.md': renderSanitizationReport(
      exports_,
      date,
      classification,
      safeToCommit,
      securityFindings,
    ),
    'NODE-INVENTORY-v14.md': renderNodeInventory(exports_),
    'WORKFLOW-MAP-v14.md': renderWorkflowMap(exports_),
    'PROMPT-AND-CODE-NODE-INDEX-v14.md': renderPromptCodeIndex(exports_),
    'RISK-AND-UNKNOWN-REGISTER-v14.md': renderRiskRegister(exports_, classification),
  };
}

/**
 * @param {WorkflowExportRecord[]} exports_
 * @param {string} date
 * @param {string} classification
 */
function renderExportManifest(exports_, date, classification) {
  const lines = [
    '# EXPORT-MANIFEST — MetaBOT SEO Content Agent Beta v14',
    '',
    `**Export date:** ${date}`,
    `**Evidence classification:** ${classification}`,
    `**Source:** n8n REST API (GET-only read-only exporter)`,
    '',
    '## Workflows',
    '',
    '| Workflow | ID | Active | Sanitized file |',
    '|----------|-----|--------|----------------|',
  ];

  for (const row of exports_) {
    lines.push(
      `| ${row.name} | ${row.id} | ${row.active ? 'yes' : 'no'} | ${row.sanitizedFile} |`,
    );
  }

  lines.push(
    '',
    '## Policy',
    '',
    '- Raw exports (if any) belong under `projects/metabot-seo-content-agent/raw/` (gitignored).',
    '- Sanitized evidence belongs under `projects/metabot-seo-content-agent/exports/live-v14-evidence/`.',
    '- Operator must review `SANITIZATION-REPORT.md` before any git commit.',
    '',
  );

  return lines.join('\n');
}

function renderSanitizationReport(exports_, date, classification, safeToCommit, securityFindings) {
  const lines = [
    '# SANITIZATION-REPORT — MetaBOT SEO Content Agent Beta v14',
    '',
    `**Date:** ${date}`,
    `**Classification:** ${classification}`,
    `**Safe to commit:** ${safeToCommit ? 'SAFE_TO_COMMIT — operator review still required' : 'NOT_SAFE_TO_COMMIT'}`,
    '',
    '## Per-workflow stats',
    '',
    '| Workflow | credentials | tokens | webhook URLs | webhook IDs | sheet IDs | personal IDs | pinData | executionData | blockers | review labels |',
    '|----------|-------------|--------|--------------|-------------|-----------|--------------|---------|---------------|----------|---------------|',
  ];

  for (const row of exports_) {
    const s = row.stats;
    lines.push(
      `| ${row.name} | ${s.credentialsRedacted} | ${s.tokensRedacted} | ${s.webhookUrlsRedacted} | ${s.webhookIdsRedacted} | ${s.sheetIdsRedacted} | ${s.personalIdsRedacted} | ${s.pinDataRemoved} | ${s.executionDataRemoved} | ${s.riskyPatternsRemaining.length} | ${s.reviewLabelsOnly.length} |`,
    );
  }

  if (exports_.some((e) => e.stats.riskyPatternsRemaining.length)) {
    lines.push('', '## Commit blockers (must be zero before commit)', '');
    for (const row of exports_) {
      if (!row.stats.riskyPatternsRemaining.length) continue;
      lines.push(`### ${row.name}`, '');
      for (const label of row.stats.riskyPatternsRemaining) {
        lines.push(`- ${label}`);
      }
      lines.push('');
    }
  }

  if (exports_.some((e) => e.stats.reviewLabelsOnly.length)) {
    lines.push('', '## Residual review labels (REVIEW_LABEL_ONLY — not commit blockers)', '');
    for (const row of exports_) {
      if (!row.stats.reviewLabelsOnly.length) continue;
      lines.push(`### ${row.name}`, '');
      for (const label of row.stats.reviewLabelsOnly) {
        lines.push(`- ${label}`);
      }
      lines.push('');
    }
  }

  if (
    !exports_.some((e) => e.stats.riskyPatternsRemaining.length) &&
    !exports_.some((e) => e.stats.reviewLabelsOnly.length)
  ) {
    lines.push('', '## Risky patterns remaining', '', '- None flagged.', '');
  }

  if (securityFindings.length) {
    lines.push('## Post-export security scan findings', '');
    for (const f of securityFindings) {
      lines.push(`- **${f.file}**: ${f.pattern}`);
    }
    lines.push('');
  }

  lines.push(
    '## Redaction markers used',
    '',
    '- REDACTED_CREDENTIAL',
    '- REDACTED_CREDENTIAL_ID',
    '- REDACTED_TOKEN',
    '- REDACTED_WEBHOOK_URL',
    '- REDACTED_WEBHOOK_ID',
    '- REDACTED_SHEET_ID',
    '- REDACTED_PRIVATE_DATA',
    '- REDACTED_PERSONAL_ID',
    '- REDACTED_EXECUTION_DATA',
    '- REDACTED_PINNED_DATA',
    '',
  );

  return lines.join('\n');
}

function renderNodeInventory(exports_) {
  const lines = [
    '# NODE-INVENTORY-v14 — MetaBOT SEO Content Agent Beta v14',
    '',
    '| workflow | node name | node type | disabled? | likely role | external service | has credentials reference? | has code? | has prompt? | risk flag | notes |',
    '|----------|-----------|-----------|-----------|-------------|------------------|----------------------------|-----------|-------------|-----------|-------|',
  ];

  for (const wf of exports_) {
    const nodes = Array.isArray(wf.sanitized?.nodes) ? wf.sanitized.nodes : [];
    for (const node of nodes) {
      const name = String(node?.name ?? '');
      const type = String(node?.type ?? '');
      const disabled = node?.disabled === true ? 'yes' : 'no';
      const role = inferLikelyRole(node);
      const service = inferExternalService(node);
      const hasCred = nodeHasCredentials(node) ? 'yes' : 'no';
      const hasCode = nodeHasCode(node) ? 'yes' : 'no';
      const hasPrompt = nodeHasPrompt(node) ? 'yes' : 'no';
      const content = getNodeContent(node);
      const risk =
        secretScanResult(content) === 'RISK_REMAINING' || hasCred === 'yes'
          ? 'review'
          : 'low';
      lines.push(
        `| ${wf.name} | ${name} | ${type} | ${disabled} | ${role} | ${service || '—'} | ${hasCred} | ${hasCode} | ${hasPrompt} | ${risk} | |`,
      );
    }
  }

  lines.push('');
  return lines.join('\n');
}

function renderWorkflowMap(exports_) {
  const lines = [
    '# WORKFLOW-MAP-v14 — MetaBOT SEO Content Agent Beta v14',
    '',
    '## Workflow list',
    '',
  ];

  for (const wf of exports_) {
    lines.push(`- ${wf.name} (id: ${wf.id}, active: ${wf.active ? 'yes' : 'no'})`);
  }

  const sections = [
    { title: 'Triggers', match: (n) => /webhook|telegram|trigger/i.test(String(n?.type)) },
    { title: 'Route nodes', match: (n) => /route|switch/i.test(String(n?.name + n?.type)) },
    { title: 'Output nodes', match: (n) => /send|reply|respond|output/i.test(String(n?.name)) },
    {
      title: 'Cross-workflow handoff',
      match: (n) => /executeWorkflow|sub-workflow/i.test(String(n?.type + n?.name)),
    },
    { title: 'Telegram nodes', match: (n) => /telegram/i.test(String(n?.type)) },
    {
      title: 'OpenRouter/LLM/HTTP nodes',
      match: (n) => /openAi|openRouter|lmChat|httpRequest/i.test(String(n?.type)),
    },
    { title: 'Google Sheets nodes', match: (n) => /googleSheets|google-sheet/i.test(String(n?.type)) },
    { title: 'Code nodes', match: (n) => /code/i.test(String(n?.type)) },
    { title: 'Lock/state nodes', match: (n) => /lock|state|active_jobs/i.test(String(n?.name)) },
    {
      title: 'Admin/recovery nodes',
      match: (n) => /admin|stop|recovery|health/i.test(String(n?.name)),
    },
    {
      title: 'Quality layers',
      match: (n) => /seoqa|factcheck|score|cleanup|repair/i.test(String(n?.name)),
    },
  ];

  for (const section of sections) {
    lines.push('', `## ${section.title}`, '');
    let found = false;
    for (const wf of exports_) {
      const nodes = Array.isArray(wf.sanitized?.nodes) ? wf.sanitized.nodes : [];
      for (const node of nodes) {
        if (section.match(node)) {
          found = true;
          lines.push(`- **${wf.name}** → ${node?.name} (\`${node?.type}\`)`);
        }
      }
    }
    if (!found) lines.push('- SAFE UNKNOWN — none matched in sanitized export');
  }

  lines.push(
    '',
    '## Cross-workflow handoff (logical)',
    '',
    '- Intake → Worker: **SAFE UNKNOWN** — confirm live n8n executeWorkflow/webhook pattern',
    '- Intake → Admin: **SAFE UNKNOWN**',
    '- Admin → Worker/Sheets: **SAFE UNKNOWN**',
    '',
  );

  return lines.join('\n');
}

function renderPromptCodeIndex(exports_) {
  const lines = [
    '# PROMPT-AND-CODE-NODE-INDEX-v14',
    '',
    '| workflow | node name | node type | content type | purpose | approximate size | secret scan result | quality relevance | migration relevance | notes |',
    '|----------|-----------|-----------|--------------|---------|------------------|--------------------|-------------------|---------------------|-------|',
  ];

  for (const wf of exports_) {
    const nodes = Array.isArray(wf.sanitized?.nodes) ? wf.sanitized.nodes : [];
    for (const node of nodes) {
      const hasCode = nodeHasCode(node);
      const hasPrompt = nodeHasPrompt(node);
      if (!hasCode && !hasPrompt) continue;

      const content = getNodeContent(node);
      const contentType = hasCode && hasPrompt ? 'code+prompt' : hasCode ? 'code' : 'prompt';
      const purpose = inferLikelyRole(node);
      const size = content.length;
      const scan = secretScanResult(content);
      const quality = /seoqa|factcheck|score|cleanup|repair/i.test(String(node?.name))
        ? 'high'
        : 'medium';
      const migration = /route|lock|memory|task_id/i.test(content) ? 'high' : 'medium';

      lines.push(
        `| ${wf.name} | ${node?.name} | ${node?.type} | ${contentType} | ${purpose} | ${size} chars | ${scan} | ${quality} | ${migration} | |`,
      );
    }
  }

  lines.push('');
  return lines.join('\n');
}

function renderRiskRegister(exports_, classification) {
  const lines = [
    '# RISK-AND-UNKNOWN-REGISTER-v14',
    '',
    `**Evidence classification:** ${classification}`,
    '',
    '## Known unknowns',
    '',
    '- Exact Intake → Worker invocation mechanism — **SAFE UNKNOWN**',
    '- Whether Admin is always reached via Intake — **SAFE UNKNOWN**',
    '- Live Worker version parity with v14 naming — verify in n8n UI',
    '- Webhook production URLs — redacted; live paths require operator verification',
    '- Google Sheets table/column truth — **SAFE UNKNOWN** from export alone',
    '',
    '## Security risks',
    '',
  ];

  let anyRisk = false;
  for (const wf of exports_) {
    if (wf.stats.riskyPatternsRemaining.length) {
      anyRisk = true;
      lines.push(`### ${wf.name}`, '');
      for (const label of wf.stats.riskyPatternsRemaining) {
        lines.push(`- ${label}`);
      }
      lines.push('');
    }
  }
  if (!anyRisk) {
    lines.push('- No commit-blocking pattern labels flagged in sanitizer stats.', '');
  }

  if (exports_.some((e) => e.stats.reviewLabelsOnly.length)) {
    lines.push('## Residual review labels (REVIEW_LABEL_ONLY)', '');
    for (const wf of exports_) {
      if (!wf.stats.reviewLabelsOnly.length) continue;
      lines.push(`### ${wf.name}`, '');
      for (const label of wf.stats.reviewLabelsOnly) {
        lines.push(`- ${label}`);
      }
      lines.push('');
    }
  }

  lines.push(
    '## Operator gates',
    '',
    '1. Review sanitized JSON manually before commit.',
    '2. Confirm `SANITIZATION-REPORT.md` safe-to-commit status.',
    '3. Never commit raw exports from `raw/` folder.',
    '4. Live workflow changes require separate operator charter.',
    '',
  );

  return lines.join('\n');
}
