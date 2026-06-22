# MARS Localhost — Service Profile v1

**Document type:** Default service profile  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-01

---

## Default profile (MLI baseline)

| Component | Selection |
|-----------|-----------|
| **Web server** | Apache httpd 2.4.66 |
| **Alternate web server** | Nginx 1.28.2 (installed, not default) |
| **PHP** | 8.3.30 (ZTS, VS16 x64) |
| **Database** | MySQL 8.4.3 Community Server |
| **HTTP port** | 80 |
| **MySQL port** | 3306 |

---

## Rationale (Apache default)

- Closer to shared hosting (Beget-class)
- `.htaccess` support for WordPress and OpenCart
- Reduces environment delta for Forge WordPress and OCPilot profiles

Nginx remains installed for optional future profile switching.

---

## Start / stop policy

| Rule | Value |
|------|-------|
| **Autostart with Windows** | **DISABLED** (`RunAtStartup=0` in `laragon.ini`) |
| **Start** | Operator or Cursor session — Laragon UI **Start All** or controlled `httpd` / `mysqld` |
| **Stop** | Laragon **Stop All** or `mysqladmin shutdown` + Apache process stop |
| **Laragon UI** | Not required to remain open after services start |
| **Conflict policy** | Do not install parallel XAMPP/WAMP on same ports without explicit MLI exception |

---

## Autostart status (MLI-01)

| Setting | Before MLI-01 | After MLI-01 |
|---------|---------------|--------------|
| `RunAtStartup` | `-1` (enabled) | `0` (disabled) |

---

## Related

- [MARS-LOCALHOST-SERVICE-CONTROL-POLICY-v1.md](MARS-LOCALHOST-SERVICE-CONTROL-POLICY-v1.md)
- [reports/MARS-LOCALHOST-MLI-01-SERVICE-CONTROL-VERIFICATION-v1.md](reports/MARS-LOCALHOST-MLI-01-SERVICE-CONTROL-VERIFICATION-v1.md)

---

*Service profile v1 — MLI-01.*
