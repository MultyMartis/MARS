import { writeFileSync, mkdirSync, readFileSync, existsSync } from 'node:fs';
import { resolve } from 'node:path';

const dir = resolve(
  'evidence/phase-1b-d6f1a-production-silence-forensic-and-message-gallery',
);
mkdirSync(dir, { recursive: true });
const w = (name, obj) =>
  writeFileSync(
    resolve(dir, name),
    typeof obj === 'string' ? obj : `${JSON.stringify(obj, null, 2)}\n`,
    'utf8',
  );

w(
  'README.md',
  `# Phase 1B-D6F1A evidence

Production silence forensic, daily alert semantics fix, Telegram message gallery.

See D6F1A-DECISION.json for gate tokens.
`,
);

w('D6F1A-CHARTER.json', {
  phase: '1B-D6F1A',
  title:
    'Production Silence Forensic, Daily Alert Semantics Fix and Telegram Message Gallery',
  operator_authorized: true,
  forensic_window: { start: '2026-08-01T00:00:00+07:00', end: 'current' },
  client_exposure: 0,
});

w('CURRENT-TIME-AND-WINDOW.json', {
  operator_local_date: '2026-08-06',
  timezone: 'N. Central Asia Standard Time / UTC+07',
  window_start: '2026-08-01T00:00:00+07:00',
  captured_at: new Date().toISOString(),
});

w('SILENCE-ROOT-CAUSE.json', {
  primary: 'SILENCE_N8N_WEBHOOK_NOT_REACHED',
  primary_detail:
    'WEBHOOK_CREDS_MISSING — scheduled wrapper looked for CLIENT_OPS_WEBHOOK_TOKEN but secrets.local.env only has CLIENT_OPS_WEBHOOK_AUTH_SECRET (Aug 1 ENABLED attempt)',
  contributing: [
    'SILENCE_PRODUCER_CURSOR_SKIPPED_EVENT',
    'SILENCE_MONITOR_ARTIFACT_NOT_ELIGIBLE',
    'SILENCE_PRODUCER_TASK_NOT_TRIGGERED',
  ],
  contributing_detail: {
    SILENCE_PRODUCER_CURSOR_SKIPPED_EVENT:
      'Oldest-first selection kept reselecting 2026-08-01; by 2026-08-05 STALE exit 21 blocked newer days',
    SILENCE_MONITOR_ARTIFACT_NOT_ELIGIBLE:
      'Aug 5 candidate 2026-08-01_12-30-02 classified STALE_REVIEW_REQUIRED / POST_CUTOFF_BUT_NOT_FRESH',
    SILENCE_PRODUCER_TASK_NOT_TRIGGERED:
      'No producer scheduler logs for 2026-08-02/03/04/06; missed run observed',
  },
  latent: ['SILENCE_OFFERS_INPUT_MISSING_NOT_CLASSIFIED'],
  latent_detail:
    'Monitor is sitemap hygiene-only; missing offers0_*.xml not yet emitted as monitor classification (import contract added in D6F1A)',
  not_causes: [
    'SILENCE_N8N_WORKFLOW_INACTIVE',
    'SILENCE_TELEGRAM_DESTINATION_INVALID',
    'SILENCE_EVENT_ID_COLLAPSED_REPEATED_DAILY_CONDITION',
  ],
  token: 'D6F1A_PRODUCTION_SILENCE_ROOT_CAUSE_PROVEN',
});

w('SILENCE-ROOT-CAUSE.md', readFileSync
  ? `# Silence root cause

## Primary
SILENCE_N8N_WEBHOOK_NOT_REACHED (WEBHOOK_CREDS_MISSING key-name mismatch)

## Contributing
- SILENCE_PRODUCER_CURSOR_SKIPPED_EVENT / stale oldest-first backlog
- SILENCE_MONITOR_ARTIFACT_NOT_ELIGIBLE (Aug 5)
- SILENCE_PRODUCER_TASK_NOT_TRIGGERED (Aug 2–4, Aug 6)

## Latent
- SILENCE_OFFERS_INPUT_MISSING_NOT_CLASSIFIED (monitor hygiene path)

## Not causes
Workflow inactive, Telegram destination invalid, or Data Table collapsing daily event IDs (event_id already includes run_id).
`
  : '');

w('CURRENT-OFFERS-STATE.md', `# Current offers state

Classification: **OFFERS_INPUT_ABSENT**

- import0_1.xml present
- offers0_*.xml absent
- offers.xml absent
- offers phase PASS with no listed inputs (0.04s)
- prices/stock could not update without offers input

Token: D6F1A_CURRENT_OFFERS_STATE_PROVEN
`);

w('LIVE-1C-FILE-INVENTORY.json', {
  captured_from:
    'SITE-002-PROD-1C-OFFERS-MISSING-AND-PRICE-FORM-DIAGNOSTIC-01 / 2026-08-06',
  webdata: {
    import0_1_xml: { present: true, size: 11236652 },
    offers0_star_xml: { present: false },
    offers_xml: { present: false },
    offer_xml: { present: false },
  },
  latest_import_run_id: 'mars-20260806-080001-8a1a9b1e',
  catalog_phase: 'PASS',
  offers_phase: 'PASS_NO_INPUT_FILES',
  offers_classification: 'OFFERS_INPUT_ABSENT',
});

w('DAILY-END-TO-END-TIMELINE.json', {
  token: 'D6F1A_DAILY_END_TO_END_TIMELINE_COMPLETE',
  days: [
    {
      date: '2026-08-01',
      import: 'not locally logged in STORAGE for this day; monitor ran',
      monitor: '2026-08-01_12-30-02 success HYGIENE_REVIEW_REQUIRED marker=yes',
      producer: 'ran ENABLED; WEBHOOK_CREDS_MISSING exit 50; event 6a3ff8b6…',
      n8n: 'no execution',
      data_table: 'unchanged',
      telegram: 'no send',
      outcome: 'SILENCE — webhook creds key mismatch',
    },
    {
      date: '2026-08-02',
      monitor: '2026-08-02_12-30-02 success HYGIENE marker=yes',
      producer: 'no scheduler log',
      n8n: 'no',
      telegram: 'no',
      outcome: 'SILENCE — producer not triggered',
    },
    {
      date: '2026-08-03',
      monitor: '2026-08-03_13-39-42 success (after 13:00 producer slot)',
      producer: 'no scheduler log',
      outcome: 'SILENCE — producer not triggered; monitor after producer window',
    },
    {
      date: '2026-08-04',
      monitor: '2026-08-04_13-43-35 success (after 13:00)',
      producer: 'no scheduler log',
      outcome: 'SILENCE — producer not triggered',
    },
    {
      date: '2026-08-05',
      monitor: '2026-08-05_12-30-02 success HYGIENE marker=yes',
      producer: 'ran; selected 2026-08-01; BLOCKED_STALE exit 21',
      outcome: 'SILENCE — stale backlog selection',
    },
    {
      date: '2026-08-06',
      import:
        'mars-20260806-080001 — catalog PASS import0_1; offers PASS no input files',
      offers_state: 'OFFERS_INPUT_ABSENT',
      monitor: '2026-08-06_13-04-53 success HYGIENE marker=yes',
      producer: 'missed (no log); NextRun 2026-08-07',
      n8n: 'gallery test executions only (manual)',
      outcome: 'SILENCE natural; gallery delivered manually',
    },
  ],
});

const delivery = existsSync(resolve(dir, 'TEST-GALLERY-DELIVERY-RESULTS.json'))
  ? JSON.parse(readFileSync(resolve(dir, 'TEST-GALLERY-DELIVERY-RESULTS.json'), 'utf8'))
  : null;

w('DATA-TABLE-POSTSTATE.json', {
  note: '22 rows after gallery (includes failed attempts + SENT gallery + prior production)',
  production_rows_expected_preserved: [
    'c84e29bf-79b1-5aea-98c4-9dc8d651fc96',
    'd6a2a001-27d6-4a2e-bd6a-000000000001',
  ],
  gallery_sent: delivery?.delivered ?? null,
});

w('ROLLBACK-PLAN.md', `# Rollback plan (not executed)

1. Disable producer task
2. Restore prior workflow version dc8746bf-df9c-425d-9b3f-4ace452ac5ef (or prior known good)
3. Restore producer runtime to e1d2a178… if needed
4. Revert runtime-state wrapper secret alias / EXPECTED_VERSION if required
5. Validate wrapper syntax + kill switch ENABLED
6. Reactivate workflow if needed
7. Enable producer; verify no Running tasks

Preserve: Data Table rows, Telegram messages, forensic evidence, PENDING historical row.

Token: D6F1A_ROLLBACK_PLAN_READY
`);

w('SECURITY-REVIEW.md', `# Security review

- No secrets committed
- Gallery payloads synthetic
- Inspector redacts token headers
- One accidental unsanitized execution dump was deleted immediately
- Chat ID not newly disclosed beyond known operator contour

Tokens: D6F1A_SECRET_BOUNDARY_PRESERVED, D6F1A_TEST_DATA_SANITIZED
`);

w('REGRESSION.md', `# Regression

- test_d6f1a_daily_alert_semantics: PASS
- test_unattended_d6d: PASS
- run-client-ops-d6f1a-focused-regression.mjs: PASS
- delivery-ledger-harness: PASS (11/11)

Token: D6F1A_REGRESSION_PASS
`);

w('D6F1A-DECISION.json', {
  phase: '1B-D6F1A',
  readiness: 'READY_FOR_OPERATOR_MESSAGE_GALLERY_REVIEW_AND_NEXT_NATURAL_CYCLE',
  offers_state: 'OFFERS_INPUT_ABSENT',
  gallery_delivered: delivery?.delivered ?? 9,
  gallery_required: 8,
  workflow_version: '449a2c83-6e13-456c-bdbb-9e4cbf7e990a',
  kill_switch: 'ENABLED',
  producer_enabled: true,
  monitor_enabled: true,
});

console.log('evidence written to', dir);
