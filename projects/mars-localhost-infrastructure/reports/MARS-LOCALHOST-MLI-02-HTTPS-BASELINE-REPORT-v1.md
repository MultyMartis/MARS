# MARS Localhost MLI-02 — HTTPS Baseline Report v1

**Document type:** HTTPS baseline report  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-02

---

## Target

`https://mli-smoke-001.test/`

---

## Certificate

| Field | Value |
|-------|-------|
| Issuer | CN=mli-smoke-001.test, O=MARS Localhost, O=MLI Dev CA (self-signed) |
| Subject | CN=mli-smoke-001.test |
| SAN | `mli-smoke-001.test`, `*.mli-smoke-001.test` |
| Valid from | 2026-06-22 |
| Valid to | 2028-09-24 |
| Storage | `D:\MARS-Localhost\laragon\etc\ssl\` (outside Git) |

---

## Trust status

| Check | Result |
|-------|--------|
| OpenSSL `s_client` + SNI | **PASS** — TLS handshake succeeds |
| Windows schannel / curl to IP | **PASS WITH LIMITATION** — handshake issues without SNI |
| Browser trust | **NOT TRUSTED** by default (self-signed) |
| Playwright headless | **PASS** with `ignoreHTTPSErrors` + host resolver map |

---

## Apache

- `mod_ssl` + `mod_socache_shmcb` enabled MLI-02
- Port **443 listening**
- Vhost: `sites-enabled\mli-smoke-001.test-ssl.conf`

---

## Redirect policy

No forced HTTPS redirect on smoke site. HTTP remains on port 80.

---

## Fallback

HTTP `http://mli-smoke-001.test/` remains valid baseline.

---

## Related

- [MARS-LOCALHOST-LOCAL-CERTIFICATE-STANDARD-v1.md](../MARS-LOCALHOST-LOCAL-CERTIFICATE-STANDARD-v1.md)

---

*HTTPS baseline report v1 — MLI-02.*
