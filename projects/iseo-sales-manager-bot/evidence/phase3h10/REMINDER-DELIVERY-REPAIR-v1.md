# REMINDER DELIVERY REPAIR — Phase 3H.10

## Deployed (Admin.dev `wLrLp4WQHm1VJmxz`)

1. **Prepare Reminder Sheets Wait** — emits `wait_until_iso`
2. **Wait Reminder Sheets Retry** — `resume: specificTime`, `dateTime: ={{$json.wait_until_iso}}`
3. Soft `retryOnFail` on ACCESS read (maxTries 2)
4. Digest renderer + Merge Reminder Send Payload + dynamic inline keyboard
5. `sm:q:` / `sm:f:` callback actions for digest compact / full card

Post-patch Admin nodes: **102** (was 100).

Operational.dev: **unchanged** (45 nodes).

Permanent workflows created: **0**.
