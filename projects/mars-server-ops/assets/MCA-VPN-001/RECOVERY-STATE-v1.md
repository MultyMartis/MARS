# Recovery State v1 — MCA-VPN-001

**Status:** Distinguishes **proven partial recovery** from **unproven full DR**  
**Full disaster recovery:** **NOT TESTED**

---

## 1. Summary matrix

| Recovery scope | Status | Evidence class |
|----------------|--------|----------------|
| Targeted 3X-UI panel configuration recovery | **PROVEN** (historical) | Operator confirmed panel worked |
| Blank VPS → restore archive → working VPN | **NOT PROVEN** | No successful drill in handoff |
| Full Ubuntu/server filesystem restore | **NOT PROVEN** | No confirmed full-server backup |
| Client connectivity after clean restore | **NOT PROVEN** | — |

```text
FULL DISASTER RECOVERY STATUS: NOT TESTED
```

---

## 2. PROVEN — Targeted 3X-UI panel configuration recovery

### Context

VPN/Xray remained operational while **management panel** was inaccessible (404 / no UI).

### Demonstrated capability

| Step | Result |
|------|--------|
| SQLite DB readable | YES — `.tables`, `.schema settings` worked |
| `settings` table existed | YES |
| `webPort` restored to known-good **5928** | YES (historical repair) |
| `webBasePath` restored to `<3XUI_PANEL_PATH>` | YES — **value not in Git** |
| `systemctl restart x-ui` | Successful reload |
| Panel reachable | Operator confirmed success ("заработал") |
| VPN continued working | YES after repair |

**This is partial configuration recovery — not disaster recovery proof.**

### Do not document here

- Actual `webBasePath` string value
- SQL UPDATE statements with secret literals

---

## 3. NOT PROVEN — Full restore layers

Extracting these paths alone onto arbitrary new Ubuntu is **insufficient** without further validation:

| Layer | Included in VPN/app archive? | Proven on restore? |
|-------|------------------------------|-------------------|
| `/usr/local/x-ui` | YES | NOT PROVEN end-to-end |
| `/etc/x-ui` | YES | NOT PROVEN end-to-end |
| `/etc/xray` | YES | NOT PROVEN end-to-end |
| `/etc/letsencrypt` | YES (in archive scope) | **ABSENT on live FS** — **CHANGED**; restore implications **NOT PROVEN** |
| `/root/cert` | YES | NOT PROVEN end-to-end |
| OS packages / dependencies | NO | NOT PROVEN |
| Users / groups / permissions | NO | NOT PROVEN |
| systemd unit differences | Partial implicit | NOT PROVEN |
| Firewall (ufw/nftables/iptables) | NO | NOT PROVEN |
| sysctl / networking | NO | NOT PROVEN |
| cron / cert renewal timers | NO | NOT PROVEN |
| Exact Xray generated runtime config | Uncertain authority | NOT PROVEN |
| Boot persistence verification | NO | NOT PROVEN |
| Client smoke test after clean restore | NO | NOT PROVEN |

---

## 4. Planned restore concept (NOT TESTED)

Documented conceptual procedure — **PLANNED / NOT TESTED:**

1. New VPS + Ubuntu  
2. SSH access  
3. Upload backup archive  
4. Restore files to paths  
5. Verify x-ui, Xray, certificates, firewall, panel  
6. Verify VPN client connectivity  
7. Create fresh backup  

**Status:** concept only — requires isolated drill before production trust.

---

## 5. Restore risk classes (Survivability-aligned)

| Action | Risk |
|--------|------|
| Read-only DB inspection | READ-ONLY |
| Targeted settings restore with backup + restart | HIGH — caused outage in Incident 3 when misapplied |
| Restore archive over live filesystem | **DESTRUCTIVE** |
| Certificate replacement | HIGH |
| Firewall/network changes during recovery | HIGH / DESTRUCTIVE |

See [KNOWN-GOOD-PROCEDURES-v1.md](KNOWN-GOOD-PROCEDURES-v1.md) and [INCIDENT-HISTORY-v1.md](INCIDENT-HISTORY-v1.md).

---

## 6. Future requirements (not claimed existing)

Before trusting Server B or refreshed Server A backups:

- [ ] Backup manifest with explicit scope  
- [ ] SHA256 checksum recorded  
- [ ] Off-server encrypted copy  
- [ ] Isolated restore rehearsal  
- [ ] Post-restore client smoke test documented  

---

## Related documents

- [BACKUP-STATE-v1.md](BACKUP-STATE-v1.md)
- [INCIDENT-HISTORY-v1.md](INCIDENT-HISTORY-v1.md)

---

**Live intake note (2026-08-25):** Partial panel recovery remains **historically proven** only. Live filesystem shows cert path migration away from `/etc/letsencrypt`. **Full DR still NOT TESTED.**

---

*Recovery State v1 · partial panel recovery proven · full DR not tested · live cross-ref 2026-08-25.*
