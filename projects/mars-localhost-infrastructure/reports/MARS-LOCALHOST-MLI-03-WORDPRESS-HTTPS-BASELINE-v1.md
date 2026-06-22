# MARS Localhost MLI-03 — WordPress HTTPS Baseline v1

**Document type:** WordPress HTTPS baseline validation  
**Version:** v1  
**Date:** 2026-06-23  
**Stage:** MLI-03  
**Git baseline:** commit `4621388` on `mars/post-cycle8-live-tests`

---

## Target

| Field | Value |
|-------|-------|
| Site | `fws-0001` |
| Canonical URL (intended) | `https://fws-0001.test/` |
| HTTP fallback | `http://fws-0001.test/` |

---

## Validation results

| Check | Result |
|-------|--------|
| Apache TLS vhost for WordPress profile | **WITH LIMITATIONS** — inherits MLI-02 TLS stack; FWS-0001 vhost not separately re-audited in this pass |
| HTTP via Host header | **PROVEN** — front-end, login, REST all 200 |
| HTTPS Playwright (direct domain) | **NOT PROVEN** — FAIL until `fws-0001.test` in hosts |
| Browser trust (self-signed) | **WITH LIMITATIONS** — same as MLI-02; not trusted by default |

---

## Blocker: hosts elevation

| Domain | Hosts managed entry | Status |
|--------|---------------------|--------|
| `fws-0001.test` | `add-mli-host.ps1` (multi-domain update) | **PENDING ELEVATION** |
| `mli-smoke-001.test` | same tooling | **OPERATOR-VERIFIED PASS** (MLI-02 closure) |

Until `fws-0001.test` resolves to `127.0.0.1`, HTTPS smoke via direct URL and Playwright domain resolution **cannot** be marked PROVEN.

---

## MLI-02 HTTPS baseline (reference)

MLI-02 established self-signed TLS for `mli-smoke-001.test` with Playwright PASS using `ignoreHTTPSErrors` + host resolver map. FWS-0001 HTTPS proof is **downstream** of hosts + vhost parity, not yet complete.

---

## Related

- [MARS-LOCALHOST-MLI-02-HTTPS-BASELINE-REPORT-v1.md](MARS-LOCALHOST-MLI-02-HTTPS-BASELINE-REPORT-v1.md)
- [MARS-LOCALHOST-LOCAL-CERTIFICATE-STANDARD-v1.md](../MARS-LOCALHOST-LOCAL-CERTIFICATE-STANDARD-v1.md)
- [MARS-LOCALHOST-HOSTS-MANAGEMENT-STANDARD-v1.md](../MARS-LOCALHOST-HOSTS-MANAGEMENT-STANDARD-v1.md)

---

*WordPress HTTPS baseline report v1 — MLI-03.*
