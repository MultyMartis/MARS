# Incident History v1 — MCA-VPN-001

**Status:** CONFIRMED HISTORICAL operational lessons — preserve for Server Ops discipline  
**Authority:** Maps to [CHANGE-RISK-MODEL-v1.md](../../CHANGE-RISK-MODEL-v1.md) and MARS Survivability risk classes

---

## Permanent operational rule (from Incident 3)

```text
READ-ONLY FIRST.
```

**Never stop/disable the only working VPN runtime during exploratory diagnostics.**

Any future mutation on production VPN requires:

1. Impact analysis  
2. Verified emergency access (e.g. provider browser console)  
3. Backup / checkpoint  
4. Rollback plan  
5. **Explicit operator approval**

---

## Incident 1 — 3X-UI panel inaccessible (VPN still worked)

| Dimension | Detail |
|-----------|--------|
| **Problem** | Management panel unreachable; VPN traffic continued |
| **Symptoms** | Candidate URLs returned no panel / 404; remembered URL forms included port 5928 and secret path variants |
| **Root cause** | Panel settings no longer on known-good port/base-path combination (`webPort`, `webBasePath`). Exact change mechanism not proven — possible association with 3X-UI update (MEDIUM causality) |
| **Fix** | SQLite update of `webPort` and `webBasePath` to known-good values; `systemctl restart x-ui` |
| **Verification** | Browser opened panel; operator confirmed success |
| **Prevention** | Before 3X-UI upgrade: preserve DB, panel port, base path, cert settings, version, service state, client connectivity baseline |
| **Risk class** | HIGH (DB mutation + service restart on production VPN) |

---

## Incident 2 — False hypothesis: missing `/usr/local/x-ui/web`

| Dimension | Detail |
|-----------|--------|
| **Problem** | Troubleshooting assumed missing web directory caused 404 |
| **Symptoms** | Expected web static path absent on filesystem |
| **Root cause** | **Wrong diagnostic assumption** — historical working backup also lacked that directory |
| **Fix** | Abandon filesystem-web-directory hypothesis; focus on DB panel settings |
| **Verification** | Comparison with `3xui_full_backup.tar.gz` contents |
| **Prevention** | Compare against known-good backup before declaring missing path abnormal |
| **Risk class** | LOW direct — but delayed correct fix |

---

## Incident 3 — Unsafe troubleshooting interrupted working VPN

| Dimension | Detail |
|-----------|--------|
| **Problem** | Diagnostic/change action interrupted VPN runtime on single-access production node |
| **Symptoms** | VPN dropped; operator lost normal network path to server |
| **Root cause** | Unsafe operational procedure on production VPN while operator depended on same path for access |
| **Fix / recovery** | VEESP emergency browser console; VPS reboot |
| **Verification** | Service restored after reboot; subsequent targeted panel repair succeeded |
| **Prevention** | **READ-ONLY FIRST**; no stop/disable/DB manipulation without charter; restart only with understood interruption |
| **Risk class** | **CRITICAL** — maps to Survivability destructive/high-impact production change without adequate guardrails |

**This is the strongest operational lesson in the legacy handoff.**

---

## Incident 4 — `inventory.sh` CRLF (`/bin/bash^M`)

| Dimension | Detail |
|-----------|--------|
| **Problem** | Inventory script failed to execute |
| **Symptoms** | `/bin/bash^M: bad interpreter` |
| **Root cause** | Windows CRLF line endings in script uploaded/edited on Windows |
| **Fix** | `sed -i 's/\r$//' /root/MCA/scripts/inventory.sh` then `bash /root/MCA/scripts/inventory.sh` |
| **Verification** | Inventory outputs generated |
| **Prevention** | Server shell scripts must use LF; validate before upload |
| **Risk class** | LOW |

---

## Incident 5 — v2rayN client-side TUN/startup (post-Windows reinstall)

| Dimension | Detail |
|-----------|--------|
| **Problem** | Client UX failures after Windows reinstall |
| **Symptoms** | Unreliable startup/minimize; TUN required UAC; first enable did not persist; second enable worked |
| **Root cause** | **Not established** — client-side; server not proven responsible |
| **Fix** | Operator workaround (second TUN enable); search for alternative clients |
| **Verification** | Client-side observation only |
| **Prevention** | Document client baseline separately from server state; do not assume server fault from client-only symptoms |
| **Risk class** | N/A (client-side) |

---

## Cross-incident lessons

| Worked | Failed |
|--------|--------|
| SQLite inspection of settings table | Guessing missing `/usr/local/x-ui/web` |
| Comparing with historical backup | Risky runtime changes without recovery path |
| Restoring only relevant panel settings | Treating VPN archive as full-server backup |
| Preserving historical backup archive | Multi-line commands in provider emergency console |

---

## Related documents

- [KNOWN-GOOD-PROCEDURES-v1.md](KNOWN-GOOD-PROCEDURES-v1.md)
- [RECOVERY-STATE-v1.md](RECOVERY-STATE-v1.md)
- [projects/mars-survivability/contracts/agent-operation-risk-classes-v1.md](../../../mars-survivability/contracts/agent-operation-risk-classes-v1.md)

---

*Incident History v1 · READ-ONLY FIRST · Survivability-aligned.*
