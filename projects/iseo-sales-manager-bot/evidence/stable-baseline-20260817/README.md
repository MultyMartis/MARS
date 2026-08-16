# Evidence — Production Stable Baseline Freeze 2026-08-17

Sanitized live snapshots for **Sales Manager v2 — Production Stable Baseline 2026-08-17**.

| File | Purpose |
|------|---------|
| `PREFLIGHT.json` | Live contour preflight checks |
| `NO-DRIFT.json` | No-functional-drift vs accepted contour |
| `REGRESSION.json` | Non-destructive R1–R27 + gate rollup |
| `POSTSTATE.json` | Compact production post-freeze state |
| `WORKFLOW-SNAPSHOT.json` | Sanitized workflow identities, hashes, reminder/AI |
| `REMINDER-OBSERVATION.json` | Natural Monday reminder observation status |
| `FREEZE-BOUNDARY.json` | TMP/experimental boundary proof |
| `ACCEPTANCE-MATRIX.json` | Machine-readable acceptance matrix |
| `PRIVACY-REVIEW.md` | Privacy / secrets review |

**Not stored:** Gmail credentials, Telegram credentials/chat IDs, n8n secrets, Sheets credentials, webhook secrets, full production Gmail bodies, phone/email/IP/lead PII, private acceptance payloads.

Accepted live test lead reference only: `LEAD_4CC52CE3F311` (no literal body).

Local harness (STORAGE, non-canonical runtime):  
`X:\AI MARS STORAGE\incoming\iseo-sales-manager-bot\stable-baseline-freeze-20260817-local\`
