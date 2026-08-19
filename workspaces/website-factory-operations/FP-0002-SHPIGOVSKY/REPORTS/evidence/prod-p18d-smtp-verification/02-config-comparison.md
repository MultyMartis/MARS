# Config Comparison — Saved vs Authoritative Beget

**Wave:** PROD-P18D  
**Date:** 2026-08-19

---

## Saved Admin Settings (Pre-Correction)

| Field | Stored Value |
|-------|-------------|
| smtp_host | `smtp.beget.com` |
| smtp_port | `465` |
| smtp_encryption | `none` |
| smtp_auth | `1` (YES) |
| smtp_username | `noreply@shpigovsky.ru` |
| password | CONFIGURED (not shown) |

## Authoritative Beget Requirements for Port 465

| Field | Required |
|-------|---------|
| smtp_host | `smtp.beget.com` |
| smtp_port | `465` |
| smtp_encryption | **`ssl`** (implicit TLS — SSL handshake before any data) |
| smtp_auth | YES |
| username | Full email address |

---

## Classification: MISMATCH

| Field | Verdict |
|-------|---------|
| smtp_host | VALID |
| smtp_port | VALID |
| smtp_encryption | **MISMATCH** — stored `none`, required `ssl` for port 465 |
| smtp_auth | VALID |
| smtp_username | VALID |
| password | CONFIGURED (unchanged) |

---

## PHPMailer Impact of Mismatch

`SmtpTransport::configure_phpmailer()` sets `SMTPSecure = ''` when `encryption=none`.  
`SMTPAutoTLS = true` is set but applies STARTTLS upgrade, not implicit SSL.  
Port 465 on Beget expects the SSL handshake **before** any protocol exchange.  
Result: connection failure or TLS negotiation failure.

---

## Correction Applied

| Field | Before | After |
|-------|--------|-------|
| smtp_encryption | `none` | `ssl` |

Correction script: `WORDPRESS/validation/p18d-smtp-correct-and-verify.php`  
Method: `update_option('fp02_mail_ops', ...)` — preserves existing password (`OPTION_AUTH` not touched).

---

## Anti-Pattern Triggered

**SMTP-001** — guessing/accepting provider port/encryption without verifying from authoritative source.  
"configured" was accepted as "correct" without provider verification.

---

## SMTP TRANSPORT CONFIGURATION MATCHES BEGET REQUIREMENTS — AFTER CORRECTION
