# FRIENDHOSTING-DE — Port / service map v1

**inventory_ref:** FRIENDHOSTING-DE  
**Status:** **CANONICAL**  
**Secrets:** none  

Classification vocabulary:

| Class | Meaning |
|-------|---------|
| **PUBLIC REQUIRED** | Must be reachable from Internet for primary mission |
| **PUBLIC NARROW** | Publicly allowed for a narrow purpose (e.g. ACME) |
| **LOCALHOST** | Bound to loopback; not a public service |
| **DENIED** | Externally blocked (UFW); process may still listen |
| **DEFERRED** | Planned; not present on host |

---

## Port table

| Port / bind | Class | Owning service | Purpose | Operator touch? | Security boundary |
|-------------|-------|----------------|---------|-----------------|-------------------|
| `80/tcp` | PUBLIC NARROW | nginx | ACME HTTP-01 webroot; optional HTTP→HTTPS | Only for cert/nginx charters | UFW allow; no panel/VPN |
| `3333/tcp` | PUBLIC REQUIRED | sshd | Operational + recovery SSH | Key-based only; charter for changes | UFW allow; fail2ban; PasswordAuthentication off |
| `443/tcp` | PUBLIC REQUIRED | nginx | TLS front for 3X-UI | Prefer panel UX via browser; nginx edits = charter | UFW allow; TLS; secret path |
| `8443/tcp` | PUBLIC REQUIRED | Xray | Primary VLESS TLS RAW VPN | Prefer 3X-UI client mgmt; do not churn transport | UFW allow; per-device UUIDs |
| `127.0.0.1:20901` | LOCALHOST | 3X-UI (x-ui) | Panel API/UI backend | Via nginx `:443` only | Not published; UFW deny if probed externally |
| `*:2096` (typical) | DENIED | 3X-UI related listener | Historical subscription/panel-related surface | **Do not** open for convenience | **UFW DENY** = **ACCEPTED HARDENED BOUNDARY** (process may still listen) |
| `24443/tcp` | DEFERRED | (planned Xray) | Reserve VLESS TLS RAW | Only after P4 charter | Not listening today |

---

## Operator rules

1. Do not expose `:20901` publicly.  
2. Do not treat UFW-denied `:2096` as “port fully absent” — classify as **DENIED / ACCEPTED HARDENED BOUNDARY**.  
3. Do not invent `:24443` during restore or routine ops.  
4. Prefer 3X-UI for client create/revoke/QR over editing Xray JSON by hand.

---

## Related

- Architecture: [FRIENDHOSTING-DE-ARCHITECTURE-v1.md](FRIENDHOSTING-DE-ARCHITECTURE-v1.md)  
- Security: [FRIENDHOSTING-DE-SECURITY-POSTURE-v1.md](FRIENDHOSTING-DE-SECURITY-POSTURE-v1.md)

---

*Port map v1 · 2026-08-30.*
