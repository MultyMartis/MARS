# MARS Localhost MLI-01 — Laragon Installation Audit v1

**Document type:** Installation audit report  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-01  
**Method:** Read-only inspection + controlled enablement verification

---

## Executive summary

| Item | Finding |
|------|---------|
| **Install path** | `D:\MARS-Localhost\laragon` — **exists, operational** |
| **Executable** | `laragon.exe` present (v8.6.1.60301) |
| **Install type** | Full Laragon tree (`app`, `bin`, `data`, `etc`, `usr`, `www`, `tmp`) |
| **Portable markers** | Relocated install; `bin\laragon\laragon.cmd` retains stale paths from prior installer location — **documented, not migrated** |
| **MLI-00 preferred path** | `D:\MARS-Localhost\runtime\laragon` — **empty placeholder** |

---

## Path and structure

```text
D:\MARS-Localhost\laragon\
├── laragon.exe          # v8.6.1.60301
├── app\
├── bin\                 # apache, php, mysql, nginx, git, composer, nodejs, …
├── data\                # MySQL data initialized MLI-01
├── etc\                 # apache2, nginx configs
├── usr\                 # laragon.ini, Procfile, profiles
├── www\                 # Laragon document root (junction registry layer)
└── tmp\
```

---

## Components detected

| Component | Present | Version / notes |
|-----------|---------|-----------------|
| **Apache** | Yes | httpd-2.4.66-260223-Win64-VS18 — **default web server** |
| **Nginx** | Yes | nginx-1.28.2 — optional profile |
| **PHP** | Yes | php-8.3.30-Win32-vs16-x64 |
| **MySQL** | Yes | mysql-8.4.3-winx64 (MySQL Community, not MariaDB) |
| **Composer** | Yes (bundled) | Laragon `bin\composer\`; MLI copy at `tools\composer\` |
| **Git** | Yes | 2.47.1.windows.1 (Laragon bundled) |
| **Node.js** | Partial | Profile lists node-v22; Laragon `bin\nodejs` folder incomplete — system Node v24.13.1 available in PATH |
| **Redis, Mailpit, Memcached, etc.** | Present | Not enabled in default MLI profile |

---

## Configuration state (at audit)

| Setting | Value |
|---------|-------|
| **laragon.ini DocumentRoot** | `D:\MARS-Localhost\laragon\www` |
| **httpd.conf DocumentRoot** | `D:/MARS-Localhost/laragon/www` |
| **Auto Virtual Hosts** | Enabled (`AutoVirtualHosts=-1`) |
| **Apache** | Enabled |
| **MySQL** | Enabled |
| **Run at Windows startup** | Was enabled; **set to disabled** in MLI-01 (`RunAtStartup=0`) |
| **Language** | Russian UI |

---

## Sites and databases

| Item | State |
|------|-------|
| **Existing www sites** | Default Laragon `index.php` only (pre-smoke) |
| **MLI sites tree** | `D:\MARS-Localhost\sites\` — category folders present; no CMS installs |
| **MySQL databases** | Fresh initialization MLI-01; no application databases |
| **Operator project data** | None inspected beyond MLI smoke artefact |

---

## Integrity assessment

| Criterion | Result |
|-----------|--------|
| Install complete | **PASS** |
| Binaries executable | **PASS** |
| Conflicting duplicate Laragon | **NONE** at `runtime\laragon` (empty) |
| Safe to adopt as canonical | **YES** — no migration required |
| Stale path references | **PASS WITH LIMITATION** — `laragon.cmd` has old `D:\Projects\Laragon-installer\` paths; MLI uses `activate-mli.cmd` instead |

---

## Security / redaction

- No Windows usernames published
- No database passwords published
- No operator project contents inspected

---

## Related

- [MARS-LOCALHOST-LARAGON-PATH-RECONCILIATION-v1.md](../MARS-LOCALHOST-LARAGON-PATH-RECONCILIATION-v1.md)
- [MARS-LOCALHOST-DOCUMENT-ROOT-DECISION-v1.md](../MARS-LOCALHOST-DOCUMENT-ROOT-DECISION-v1.md)

---

*MLI-01 Laragon installation audit v1.*
