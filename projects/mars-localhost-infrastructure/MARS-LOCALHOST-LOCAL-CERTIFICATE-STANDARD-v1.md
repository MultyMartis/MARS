# MARS Localhost — Local Certificate Standard v1

**Document type:** Local TLS certificate standard  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-02

---

## Scope

Local development certificates for `.test` vhosts on D: only. **Production certificates forbidden.**

---

## Storage (runtime, outside Git)

```text
E:\MARS-Localhost\laragon\etc\ssl\
  {domain}.crt
  {domain}.key
```

Private keys **must not** be committed to `C:\AI MARS`.

---

## Generation (MLI-02 smoke)

Script:

```text
E:\MARS-Localhost\tools\ssl\generate-mli-smoke-cert.cmd
```

Uses Laragon-bundled OpenSSL with `OPENSSL_CONF` pointing at Laragon Apache `openssl.cnf`.

---

## Apache integration

- Enable `mod_ssl` and `mod_socache_shmcb` in Laragon `httpd.conf` (MLI-02 baseline).
- Include `etc/apache2/httpd-ssl.conf` for global SSL parameters.
- Per-site SSL vhost in `sites-enabled/*-ssl.conf` referencing cert paths on D:.

---

## Trust policy

| Layer | MLI-02 state |
|-------|----------------|
| Self-signed issuer | Local MLI Dev CA (per-cert self-signed) |
| Windows trust store | **Operator-controlled** — not automated in MLI-02 |
| Browser warning | Expected until CA/cert trusted |
| Playwright / CLI | May use `ignoreHTTPSErrors` or OpenSSL verification for smoke only |
| HTTP fallback | Remains available on port 80 |

---

## Redirect policy

No forced HTTP→HTTPS redirect in MLI-02 smoke baseline. Consumers may add redirects in MLI-03+ profiles.

---

## Related

- [reports/MARS-LOCALHOST-MLI-02-HTTPS-BASELINE-REPORT-v1.md](reports/MARS-LOCALHOST-MLI-02-HTTPS-BASELINE-REPORT-v1.md)

---

*Local certificate standard v1 — MLI-02.*
