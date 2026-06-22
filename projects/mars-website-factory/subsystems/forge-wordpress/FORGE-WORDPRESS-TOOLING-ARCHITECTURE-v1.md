# Forge WordPress — Tooling Architecture v1

**Document type:** Tooling boundary (classes only — no implementation)  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-01

**Rule:** FW-03 designs tooling integration; FW-01 classifies tool **classes** only.

---

## 1. Tool class registry

| Tool class | FW-01 status | Environment | Human approval | Risk | Windows | Shared hosting | WPilot relation |
|------------|--------------|-------------|----------------|------|---------|----------------|-----------------|
| **Filesystem and Git** | **Required** | Local/DEV | Merge/hotfix: required | R2 | **Yes** | N/A (dev) | WPilot uses Git for deploy artifacts |
| **PHP and Composer** | **Candidate** | Local/DEV | Dependency add: required | R2 | **Yes** | Target env must support | Plugin deps in manifest |
| **npm and Factory frontend build** | **Required** | Local/DEV | Rebuild: report | R1 | **Yes** | Asset build offline | Ships static assets to theme |
| **WordPress local environment** | **Candidate** | Local/DEV | Stack choice: FW-03 | R2 | **Yes** (required) | N/A | DEV mirror optional |
| **WP-CLI** | **Candidate** | Local/DEV | Destructive cmds: prohibited | R3 | **Yes** | If host provides | WPilot may use for ops |
| **PHPCS / WPCS** | **Required** (design) | Local/DEV/CI | Fail: block WV2 | R2 | **Yes** | N/A | Code quality pre-handoff |
| **Static analysis (PHPStan/Psalm)** | **Deferred** | Local | FW-03 | R2 | **Yes** | N/A | Optional gate |
| **PHP unit/integration tests** | **Candidate** | Local/DEV | FW-03 | R2 | **Yes** | Rare on shared host | Test evidence in manifest |
| **Playwright** | **Candidate** | Local/DEV | FW-03 | R2 | **Yes** | N/A | E2E pre-handoff |
| **Screenshot comparison** | **Candidate** | Local/DEV | Visual sign-off: human | R2 | **Yes** | N/A | Parity evidence |
| **Accessibility (axe, etc.)** | **Deferred** | Local/DEV | FW-03 | R2 | **Yes** | N/A | WV8 |
| **Performance (Lighthouse)** | **Deferred** | Local/DEV | FW-03 | R2 | **Yes** | Post-handoff often WPilot | WV8 |
| **Security scanning (WPScan, etc.)** | **Candidate** | Local/DEV | Plugin add: required | R3 | **Yes** | Limited on shared | WV4 |
| **Packaging (ZIP, manifest)** | **Required** (design) | Local | Release: required | R2 | **Yes** | Deploy via host panel/FTP by WPilot | WPilot consumes package |
| **Staging/release tools** | **Deferred** | Staging | WPilot/operator | R3 | **Yes** | **Primary** | **WPilot domain** |
| **Docker / enterprise CI** | **Deferred** | — | Not mandatory | R1 | Optional | N/A | **REJECT** as FW mandatory |

---

## 2. Local WordPress environment candidates (FW-03 decision)

| Candidate | Classification | Notes |
|-----------|----------------|-------|
| **WordPress Playground** | **ADAPT** | Browser/CLI; good for agent sandbox; Windows-friendly |
| **wp-env (Playground runtime)** | **ADAPT** | No Docker requirement aligns with MARS |
| **Local WP / Laragon / XAMPP** | **ADOPT** as operator-familiar option | Windows proven |
| **Docker-based stacks** | **DEFER** | Not mandatory |

---

## 3. Production tooling boundary

| Allowed in Forge WordPress | **WPilot / operator only** |
|----------------------------|----------------------------|
| Local/DEV stack manipulation | Production deploy |
| Dev database reset | Production DB migration |
| Plugin install on local | Production plugin install |
| Export package | Live search-replace |

---

## 4. Frontend build reuse

| Rule | Definition |
|------|------------|
| **R-TOOL-01** | Factory `npm run build` output is primary asset source for Mode A |
| **R-TOOL-02** | Theme enqueues built CSS/JS — no duplicate build pipeline without WAD |
| **R-TOOL-03** | Gulp architecture preserved — Forge WordPress does not replace Gulp |

---

## 5. FW-03 deliverables (forward reference)

- Selected local stack standard
- Validation runner scripts (human-invoked)
- Playground/PR preview evaluation
- Windows setup quickstart

---

## Related documents

- [FORGE-WORDPRESS-VALIDATION-ARCHITECTURE-v1.md](FORGE-WORDPRESS-VALIDATION-ARCHITECTURE-v1.md)
- [FORGE-WORDPRESS-HUMAN-CONTROL-MODEL-v1.md](FORGE-WORDPRESS-HUMAN-CONTROL-MODEL-v1.md)

---

*Tooling architecture v1 — classes only; no tools deployed.*
