# FRIENDHOSTING-DE — TLS / ACME lifecycle v1

**inventory_ref:** FRIENDHOSTING-DE  
**Domain:** `metacode-cloud.com`  
**Status:** **CANONICAL**  
**Secrets:** private keys never in Git  

---

## 1. Current design

| Item | Value |
|------|-------|
| CA | Let's Encrypt |
| Challenge | HTTP-01 |
| Public ACME surface | TCP/`80` → nginx webroot |
| Webroot | `/var/www/letsencrypt` (accepted P2 design) |
| Scheduler | `certbot.timer` |
| Dry-run | **PASS** (P2 clean hardening reconciliation 02) |
| Consumers | nginx `:443`; 3X-UI/Xray TLS for `:8443` |

Deploy/reload hook must keep **both** nginx and Xray consumers consistent after renew.

---

## 2. Operator monitoring requirement

Track certificate **notAfter** and renew health. Do not wait for browser/client TLS failures.

Minimum human cadence until automated monitoring exists: check expiry / timer / last renew log on a scheduled ops review (charter later for monitoring wave).

---

## 3. Incident paths

### Certificate near expiry

1. Confirm `certbot certificates` / nginx SSL paths (read-only first).  
2. Run `certbot renew --dry-run` if safe.  
3. If dry-run PASS but live near expiry: `certbot renew` under charter + verify hook reloads.  
4. Validate `:443` and `:8443` TLS; VPN smoke (WSP-ONE).

### Renewal dry-run failure

1. Classify: `:80` blocked? webroot path? nginx ACME location? DNS? rate limit?  
2. Do **not** switch to random TLS modes or move VPN off `:8443`.  
3. Fix ACME path; re-dry-run; then renew.  
4. Evidence: REPORT + restore strategy if config edits.

### Hook failure (cert renewed, services stale)

1. Confirm new cert files on disk.  
2. Reload nginx; restart/reload x-ui/Xray as required by stack.  
3. Validate both `:443` panel TLS and `:8443` VPN TLS.  
4. Fix hook for next renew.

### nginx renewal regression

1. Confirm `:80` UFW allow and ACME location still present.  
2. Confirm HTTP→HTTPS does not break challenge path.  
3. Restore nginx ACME snippets from final backup if needed.

### Xray certificate reload regression

1. Confirm Xray still serves TLS on `:8443` with expected SNI.  
2. Prefer panel/documented cert paths over inventing new inbound TLS.  
3. Scoped restore of x-ui/TLS material from verified backup if corrupted.

---

## 4. Explicit non-goals

- Do not terminate VPN TLS on nginx `:443`.  
- Do not open extra ports “for ACME convenience” beyond accepted `:80`.  
- Do not put private keys in Git or REPORT bodies.

---

## 5. Related

- Architecture: [FRIENDHOSTING-DE-ARCHITECTURE-v1.md](FRIENDHOSTING-DE-ARCHITECTURE-v1.md)  
- P2 report: [../../reports/MARS-SERVER-OPS-FRIENDHOSTING-P2-CLEAN-HARDENING-RECONCILIATION-02.md](../../reports/MARS-SERVER-OPS-FRIENDHOSTING-P2-CLEAN-HARDENING-RECONCILIATION-02.md)

---

*TLS/ACME lifecycle v1 · 2026-08-30.*
