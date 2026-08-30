# EXP-A01b session evidence

Harness: EQ-ALT-A-REALITY-VISION-1.0.0
Session directory: X:\AI MARS\projects\mars-server-ops\evidence\EQVPS-TRANSPORT-ALTERNATIVES-WAVE-01\2026-08-29_190730_dryvalidate
DryValidate: True

## Purpose
Operator-guided offline acceptance capture:
VEESP baseline → EQVPS switch → transport + real apps → VEESP restore → recovery.

## Important
If the harness aborts (Ctrl+C / exception) after EQVPS phase started:

**Manually restore VEESP RAW :8443 in v2rayN.**

Do not change TUN / System Proxy / routing / DNS / MTU / other settings.
This harness never switches VPN automatically and never edits v2rayN config.

## Secrets policy
Evidence must not contain VLESS UUIDs, URIs, passwords, panel paths, tokens, or subscription links.
Log extracts are redacted best-effort.

## Files
- session-summary.json
- session-events.csv
- baseline-veesp.json / transport-veesp.txt
- eqvps.json / transport-eqvps.txt
- eqvps-post-app.json / transport-eqvps-post-app.txt (if reached)
- recovery-veesp.json / transport-recovery.txt
- manual-acceptance.csv
- process-snapshot.txt
- v2rayn-log-extract.txt
- xray-client-log-extract.txt
- COMPLETED.marker (only on full completion)

After completion with VEESP restored, return to Cursor and provide this directory path.
