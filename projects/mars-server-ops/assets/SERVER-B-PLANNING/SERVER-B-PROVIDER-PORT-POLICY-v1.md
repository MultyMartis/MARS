# Server B Provider Port Policy v1 — AdminVPS

**Status:** **RETRIEVED** — 2026-08-25  
**Wave:** MARS Server Ops Phase 3D  
**Source URL:** https://my.adminvps.ru/knowledgebase/561/zablokirovannye-porty-na-usluge-vps.html  
**Retrieval method:** live knowledge-base fetch (2026-08-25)  
**Location applicability:** Finland (Server B) is listed under **location-specific** outbound restrictions  
**Not:** provider panel change, support ticket, or VPN port assignment

---

## 1. Retrieval state

| Field | Value |
|-------|-------|
| Retrieval date | **2026-08-25** |
| Provider URL | https://my.adminvps.ru/knowledgebase/561/zablokirovannye-porty-na-usluge-vps.html |
| Live reverify | **DONE this wave** — re-check before opening future VPN ports |
| Credentials exposed | **NONE** |

---

## 2. Location-specific blocks (includes Finland)

Applies to: Netherlands, Germany, **Finland**, Poland, France, Spain, UK.

| Protocol | Ports | Direction note |
|----------|-------|----------------|
| **TCP** | 25, 2525, 110, 143, 465, 587, 993, 995, **22 (outbound)** | Outbound SMTP/mail + outbound SSH |
| **UDP** | 110, 143, 993, 995, 5060 | Mail-related + SIP |

**Implication for Server B (Finland):** outbound SSH to remote hosts on TCP/22 may be restricted. Inbound SSH to this VPS on TCP/22 remains the operator path and is currently working.

---

## 3. Global blocked ports (all VPS locations)

### Remote management / legacy Windows

| Protocol | Ports |
|----------|-------|
| TCP | 23, 135, 139, 445, 5985 |
| UDP | 135, 137, 138, 445, 520, 1900, 5353 |

### RPC / NFS / databases / caches

| Protocol | Ports |
|----------|-------|
| TCP | 111, 2049, 5432, 1433, 1521, 6379, 11211, 27017, 9200, 9300 |
| UDP | 111, 2049, 11211, 1433, 1521 |

### UDP/TCP amplifiers / unsafe services

| Protocol | Ports |
|----------|-------|
| UDP | **69, 123, 161, 162, 389, 636** |
| TCP | 69, 389, 636 |

### Proxies / atypical backdoors

| Protocol | Ports |
|----------|-------|
| TCP | 1080, 3128, 4444, 1337, 31337, 17, 1183, 5223, 53413 |
| UDP | 17, 1183, 53413, 4444, 1337, 31337 |

---

## 4. Ports support may unblock

Provider states blocked ports can be opened via **technical support** with:

1. A-record of domain/subdomain pointing at the VPS IP  
2. Support ticket describing service purpose  
3. Domain/subdomain used for the service  
4. Possible identity / abuse-risk questions  

Support may refuse risky scenarios.

---

## 5. Consequences for Server B architecture

| Topic | Consequence |
|-------|-------------|
| **NTP (UDP 123)** | Global block list includes **UDP 123**. Phase 3D observed `systemd-timesyncd` timeouts to `ntp.ubuntu.com`. Treat NTP sync failure as **provider-policy residual** until support unblocks or an approved alternate time path is chartered. |
| **Future VPN / Reality / WS ports** | Must be chosen **outside** the global + Finland lists. Do not open any app ports in Phase 3D. |
| **TCP 8444** | **Not listed** in the 2026-08-25 blocked tables. Historical caution remains: re-verify live page before selecting 8444 for any future panel/service. Prefer ports with explicit non-blocked confirmation. |
| **Outbound SSH 22 (Finland)** | May be blocked outbound — do not design Server B as a jump host that SSHes outbound on 22 without support confirmation. |
| **Mail / SIP** | Not planned for Server B VPN role; leave blocked. |

---

## 6. Phase 3D posture

No VPN/application ports opened on Server B host firewall. Public allow remains **TCP/22 only**.

---

*Provider port policy · retrieved 2026-08-25 · no secrets.*
