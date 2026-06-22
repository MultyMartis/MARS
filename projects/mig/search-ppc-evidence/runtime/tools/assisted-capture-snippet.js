/**
 * MIG Wave 2.2 — Operator Assisted SERP Capture (DevTools Snippet)
 *
 * Usage:
 * 1. Open Yandex search results in a normal browser during approved window.
 * 2. Open DevTools → Sources → Snippets (or Console).
 * 3. Paste and run this script.
 * 4. Save the downloaded JSON; place screenshot + page HTML in the bundle folder.
 * 5. Run: node runtime/cli/prepare-assisted-capture-bundle.mjs --finalize --bundle <dir>
 */
(function migAssistedSerpCapture(config) {
  const cfg = Object.assign({
    project_id: 'MIG-W2-1-TECH-PAID-SERP',
    session_id: 'w2-2-assisted-session-001',
    query_id: 'w2-1-q02',
    query: document.title.split('—')[0]?.trim() || '',
    timezone: 'Europe/Moscow',
    region: 'Москва',
    region_lr: 213,
  }, config || {});

  const attestation = {
    attested: true,
    attested_at: new Date().toISOString(),
    statement: 'I observed this page live in an interactive browser session.',
  };

  const manifest = {
    schema_version: '1.0.0',
    acquisition_mode: 'OPERATOR-ASSISTED LIVE SERP CAPTURE',
    project_id: cfg.project_id,
    session_id: cfg.session_id,
    query_id: cfg.query_id,
    query: cfg.query,
    captured_at: new Date().toISOString(),
    timezone: cfg.timezone,
    region: cfg.region,
    region_lr: cfg.region_lr,
    device_browser: navigator.userAgent,
    page_url: location.href,
    page_title: document.title,
    files: { screenshot: 'screenshot.png', html: 'page.html' },
    operator_attestation: attestation,
    production_authority: false,
    technical_test_only: true,
    capture_instructions: [
      'Save full-page screenshot as screenshot.png in bundle folder',
      'Save page HTML as page.html (Ctrl+S or DevTools)',
      'Run prepare-assisted-capture-bundle.mjs --finalize to compute checksums',
    ],
  };

  const blob = new Blob([JSON.stringify(manifest, null, 2)], { type: 'application/json' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = 'capture-manifest.json';
  a.click();
  console.log('[MIG] capture-manifest.json downloaded — complete bundle per operator-assisted contract');
  return manifest;
})();
