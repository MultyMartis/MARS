# Kill Switch Forensic

## Old local producer kill switch

- Path: `X:\AI MARS STORAGE\runtime-state\client-ops-site-002-producer\config\kill-switch.json`
- Mode observed: `ENABLED`
- Controlled: Windows Node producer / unattended monitor→Client Ops path (D6D–D6F era)
- After D6G1: producer task **Disabled**; normal reports are **server completion dispatch**
- Therefore old local kill switch is **not authoritative** for server-side outbound reporting

## D6G1 ambiguity

`D6G1_KILL_SWITCH_ENABLED=NO` meant: formalized server-side dispatch kill-switch semantics were not yet explicit — **not** that Telegram outbound was disabled (server_dispatch_enabled was already true).

## Server prestate

- `server_dispatch_enabled`: true (D6G1 local config)
- `CLIENT_OPS_DISPATCH_ENABLED`: absent prestate → added in D6G1A

## Workflow active ≠ kill switch

Workflow `tkM4H0G0gM3q9Foi` active=true is separate from dispatch authorization.
