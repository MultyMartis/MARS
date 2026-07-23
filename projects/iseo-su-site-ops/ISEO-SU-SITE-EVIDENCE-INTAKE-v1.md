# ISEO-SU SITE EVIDENCE INTAKE v1

**Programme:** ISEO-SU-SITE-OPS  
**Task ID:** ISEO-SU-SITE-OPS-PHASE-2B-ACCESS-REVIEW-AND-READ-ONLY-PRODUCTION-AUDIT  
**Canonical locus:** `X:\AI MARS\projects\iseo-su-site-ops\`  
**Phase:** PHASE 2B — READ-ONLY PRODUCTION AUDIT COMPLETE (Admin UI residual gap)  
**Status:** Wave A accepted; local access filled; Phase 2B architecture evidence captured  
**Date opened:** 2026-07-22  
**Date Wave A accepted:** 2026-07-22  
**Date Phase 2B audit:** 2026-07-24  
**Production connection:** READ-ONLY SFTP + limited WP/REST under Phase 2B charter (complete); writes still NOT AUTHORIZED  

Classification vocabulary (mandatory):

| Class | Meaning |
|-------|---------|
| **CONFIRMED BY REPOSITORY** | Proven by committed MARS locus / accepted programme docs |
| **CONFIRMED BY OPERATOR** | Explicit operator attestation recorded as fact |
| **CONFIRMED BY SANITIZED EVIDENCE** | Supported by operator-supplied sanitized screenshots/exports |
| **PUBLICLY OBSERVABLE — OPERATOR PROVIDED** | Public URL/page fact supplied by operator (no agent crawl) |
| **OPERATOR CONTEXT** | Operator belief / working hypothesis — not yet technical proof |
| **INFERENCE** | Derived claim — must not be treated as confirmed |
| **CONFLICTING** | Competing claims unresolved |
| **DEFERRED** | Consciously postponed |
| **SAFE UNKNOWN** | Material unknown; do not invent |
| **EXCLUDED** | Out of scope or forbidden in this phase |

Rule: do **not** promote OPERATOR CONTEXT to confirmed technical fact without evidence.  
Rule: do **not** store passwords, tokens, cookies, keys, DSNs, or secret-bearing URLs.

---

## 1. Intake Status

| Field | Value | Classification | Source | Confidence | Risk | Next evidence required |
|-------|-------|----------------|--------|------------|------|------------------------|
| Phase 2 charter | AUTHORIZED for documentation + non-secret operator evidence; Phase 2A adds local-only access templates | CONFIRMED BY REPOSITORY | Phase charter / this task | High | Premature connection | Separate connection charter |
| Wave A receipt | ACCEPTED 2026-07-22 | CONFIRMED BY OPERATOR | Operator Wave A package in Phase 2A task | High | Misclassification of URLs | Operator fill of local access files |
| Waves B–E | NOT REQUESTED yet | DEFERRED | Phase 2 stop / Wave A review | High | Over-collection | After architecture discovery charter |
| Production access | NOT AUTHORIZED | CONFIRMED BY REPOSITORY | Charter / Access classification | High | Unauthorized mutation | Phase 6+ / dedicated charter |
| Local access templates | CREATED and filled; Git-ignored; required FTP/SFTP + WP fields non-empty | CONFIRMED BY LOCAL VALIDATION (Phase 2B) | Phase 2A + operator fill | High | Secrets in chat | Keep local-only |
| Phase 2B read-only audit | Architecture captured; Admin UI JS challenge residual | CONFIRMED BY SANITIZED EVIDENCE | Phase 2B audit docs | High | Treating gap as full Admin inventory | Optional 2C HITL browser Admin |
| Operator Beget backup (2B) | Full hosting backup confirmed 2026-07-24 | CONFIRMED BY OPERATOR | Operator attestation | High | Stale backup on later tasks | Re-confirm each session |

---

## 2. Evidence Rules

| Field | Value | Classification | Source | Confidence | Risk | Next evidence required |
|-------|-------|----------------|--------|------------|------|------------------------|
| Allowed sources | Operator facts; sanitized screenshots/exports; public URLs listed by operator; public page source saved by operator; sanitized inventories; existing MARS docs/reports | CONFIRMED BY REPOSITORY | Phase 2 charter | High | Secret leakage if ignored | Follow redaction guide |
| Forbidden sources | Passwords; tokens; cookies; session IDs; Authorization headers; FTP/DB credentials in chat/Git; wp-config secrets; private/API keys; SMTP passwords; secret-bearing URLs; live Cursor login/connection; network crawl; direct prod FS/WP reads; browser login by agent; plugin install | CONFIRMED BY REPOSITORY | Phase 2 / 2A charter | High | Credential exposure | Quarantine if received |
| Local secrets storage | `X:\AI MARS\local\sites\iseo-su-production\secrets.local.md` only (Git-ignored) | CONFIRMED BY REPOSITORY | LOCAL-ACCESS-MODEL | High | Wrong path / Storage misuse | Operator fill guide |
| Redaction guide | [ISEO-SU-EVIDENCE-REDACTION-GUIDE-v1.md](ISEO-SU-EVIDENCE-REDACTION-GUIDE-v1.md) | CONFIRMED BY REPOSITORY | Phase 2 artifact | High | Incomplete redact | Operator applies guide |
| Evidence request | [ISEO-SU-NON-SECRET-EVIDENCE-REQUEST-v1.md](ISEO-SU-NON-SECRET-EVIDENCE-REQUEST-v1.md) | CONFIRMED BY REPOSITORY | Phase 2 artifact | High | Wave skip | Waves B–E still deferred |
| Access classes | [ISEO-SU-ACCESS-CLASSIFICATION-v1.md](ISEO-SU-ACCESS-CLASSIFICATION-v1.md) | CONFIRMED BY REPOSITORY | Phase 2/2B artifact | High | Confusing capability with authorization | A4/A5 used in 2B; reuse needs new charter; A6–A8 still NOT AUTHORIZED |

---

## 3. Known Operator Context

Items below that were only OPERATOR CONTEXT before Wave A are updated where Wave A resolved them. Remaining architecture beliefs stay OPERATOR CONTEXT until a later read-only audit.

| Item | Statement | Classification | Source | Confidence | Risk | Next evidence required |
|------|-----------|----------------|--------|------------|------|------------------------|
| OC-001 | i-seo.su is an existing production site | CONFIRMED BY OPERATOR | Wave A | High | Wrong lifecycle | Runtime audit later |
| OC-002 | Андрей originally created the frontend layout and forms | CONFIRMED BY OPERATOR | Wave A contributors | Medium–High | Wrong ownership of edit surface | Later surface map |
| OC-003 | Main pages include physical HTML trees; homepage is WP template with static-like markup | CONFIRMED BY SANITIZED EVIDENCE (refined) | Phase 2B | High | Dual home.html drift | Prefer boundary map before edits |
| OC-004 | WordPress is used for the blog | CONFIRMED BY SANITIZED EVIDENCE | Phase 2B `/blog/` | High | Parallel blog.html file | Edit WP blog, not blog.html, unless chartered |
| OC-005 | Header/footer dual: static embeds + WP theme parts; home chrome in `page-home.php` | CONFIRMED BY SANITIZED EVIDENCE | Phase 2B | High | Sitewide chrome breakage | Map surface before chrome edits |
| OC-006 | ACF PRO present on disk; field model unknown | PARTIAL — presence confirmed | Phase 2B | Medium | Wrong field SoT | Admin ACF UI / 2C |
| OC-007 | Tariff cards exist | CONFIRMED BY SANITIZED EVIDENCE | Phase 2B | High | Dual static/theme copies | URL-scoped edits only |
| OC-008 | SEO services calculator exists | CONFIRMED BY SANITIZED EVIDENCE | Phase 2B | High | Handler/JS drift | Protect calculator zone |
| OC-009 | Web commercial-proposal tool | SAFE UNKNOWN label; candidates `/offers` + CPT `offer` | Phase 2B | Medium | Wrong tool touch | Operator names web-KP URL |
| OC-010 | FTP/file-level work may be needed later | CONFIRMED BY OPERATOR (capability exists) | Wave A | High | Premature FTP use | Connection charter before use |
| OC-011 | WordPress/WPilot may later be used for WordPress-owned surfaces | OPERATOR CONTEXT / programme posture | Pre-Wave A + D-007 | Medium | Premature install | Phase 4B only after passport |

Programme-confirmed:

| Item | Statement | Classification | Source | Confidence | Risk | Next evidence required |
|------|-----------|----------------|--------|------------|------|------------------------|
| PC-001 | Site URL `https://i-seo.su/` | CONFIRMED BY OPERATOR | Wave A / Charter | High | Domain drift | Additional routes |
| PC-002 | Organization: i-SEO | CONFIRMED BY OPERATOR / CONFIRMED BY REPOSITORY | Charter | High | Naming drift | None |
| PC-003 | Operator: Andrey | CONFIRMED BY OPERATOR / CONFIRMED BY REPOSITORY | Charter | High | Role confusion | Contributor map below |

---

## 4. Evidence Received

| Evidence ID | Description | Classification | Source | Confidence | Risk | Next evidence required |
|-------------|-------------|----------------|--------|------------|------|------------------------|
| ER-WA-001 | Wave A non-secret answers accepted in Phase 2A task | CONFIRMED BY OPERATOR | Operator → Phase 2A charter text | High | Incomplete architecture | Routes B–E / audit later |
| ER-DOC-001 | Phase 0 / 1 / 1.5 / 2 programme reports and registers exist | CONFIRMED BY REPOSITORY | `reports/` + registers | High | Confusing docs with site proof | Do not treat as hosting proof |
| ER-LOC-001 | Local access templates created (empty secrets) | CONFIRMED BY REPOSITORY | Phase 2A bootstrap | High | Untested credentials | Operator fill; no validation in 2A |

---

## 5. Hosting and Runtime

| Item | Current value | Classification | Source | Confidence | Risk | Next evidence required |
|------|---------------|----------------|--------|------------|------|------------------------|
| Hosting provider | **Beget** | CONFIRMED BY OPERATOR | Wave A | High | Wrong panel assumptions | Panel URL in local file |
| Control panel type | Beget hosting control panel | CONFIRMED BY OPERATOR (provider implies panel family) | Wave A | Medium–High | Wrong login URL | Operator identifies panel URL |
| Beget control-panel URL | `https://cp.beget.com` (host from local profile) | CONFIRMED BY LOCAL PROFILE | Phase 2B local validation | High | Wrong panel path variants | Operator confirms full URL string if needed |
| WordPress Admin URL | `https://i-seo.su/wp-admin/` | CONFIRMED BY OPERATOR | Wave A | High | Misuse as hosting panel | Keep classification clear |
| PHP version | Runtime SAFE UNKNOWN; core requires ≥ 7.4 | SAFE UNKNOWN / PARTIAL | Phase 2B | Medium | Compatibility | Browser Site Health / panel |
| Staging / DEV | **Does not exist** | CONFIRMED BY OPERATOR | Wave A | High | Prod-only testing risk | Remains no staging |
| Operational decision | Work will occur directly on production after future authorization | CONFIRMED BY OPERATOR | Wave A | High | Premature mutation | Per-task charter still required |
| Backup decision | Full Beget backup manually before every future task/work package | CONFIRMED BY OPERATOR | Wave A + 2B attestation 2026-07-24 | High | False safety if treated as only control | Still need scoped backup/validation/rollback/HITL/evidence |

---

## 6. Static Site Surface

| Item | Current value | Classification | Source | Confidence | Risk | Next evidence required |
|------|---------------|----------------|--------|------------|------|------------------------|
| Static / WP split | Hybrid root WP + physical HTML trees; HTML-as-PHP | CONFIRMED BY SANITIZED EVIDENCE | Phase 2B | High | Wrong edit channel | Use boundary map |
| Static docroot / folders | `public_html` with `services/`, `cases/`, shared assets | CONFIRMED BY SFTP | Phase 2B | High | Overwrite risk | Protected zones |
| Frontend layout origin (Андрей) | Original frontend layout and forms by Andrey | CONFIRMED BY OPERATOR | Wave A | Medium–High | Wrong maintainer map | Surface ownership map |

---

## 7. WordPress Surface

| Item | Current value | Classification | Source | Confidence | Risk | Next evidence required |
|------|---------------|----------------|--------|------------|------|------------------------|
| WordPress admin exists | **Yes** | CONFIRMED BY OPERATOR | Wave A | High | Premature mutation | Charter each use |
| WordPress Admin URL | `https://i-seo.su/wp-admin/` | CONFIRMED BY OPERATOR | Wave A | High | Confused with Beget | Classification locked |
| WP physical path | Docroot root install | CONFIRMED BY SFTP | Phase 2B | High | Plugin/file mistakes | Remote FS inventory |
| WP version | **7.0.2** | CONFIRMED BY SANITIZED EVIDENCE | Phase 2B | High | Compatibility | Track on upgrades |
| WPilot on production | **Not installed** | CONFIRMED BY SFTP | Phase 2B | High | Premature install | Phase 4B only |
| Dedicated MARS WP admin | Configured locally (`yes`) | CONFIRMED BY LOCAL VALIDATION | Phase 2B | High | Shared personal account risk | Do not print username |

---

## 8. Shared Header and Footer

| Item | Current value | Classification | Source | Confidence | Risk | Next evidence required |
|------|---------------|----------------|--------|------------|------|------------------------|
| Header/footer owner | Dual static embeds + WP theme parts; home in `page-home.php` | CONFIRMED BY SANITIZED EVIDENCE | Phase 2B | High | Site-wide chrome breakage | Boundary map before edits |

---

## 9. Blog

| Item | Current value | Classification | Source | Confidence | Risk | Next evidence required |
|------|---------------|----------------|--------|------------|------|------------------------|
| Blog on WordPress | **Yes** — `/blog/` | CONFIRMED BY SANITIZED EVIDENCE | Phase 2B | High | Wrong content channel | Prefer WP for posts |
| Blog route(s) | `/blog/` (+ WP page slug `blog`) | CONFIRMED BY SANITIZED EVIDENCE | Phase 2B | High | Parallel `blog.html` | Avoid editing legacy file casually |

---

## 10–15. Structured data / tools / forms / mail / assets

See Phase 2B audit + boundary map + SoT matrix. Summary: ACF PRO on disk (groups SAFE UNKNOWN); tariffs + calculator confirmed; web-KP label SAFE UNKNOWN with `/offers`+`offer` candidates; forms via `*__FORM.php`; shared `css/`/`js/`/`libs/`; no on-server Node build tree.

---

## 16. Frontend Assets and Build Chain

| Item | Current value | Classification | Source | Confidence | Risk | Next evidence required |
|------|---------------|----------------|--------|------------|------|------------------------|
| Local/Git maintained canonical source | Unknown whether a separate maintained source exists | SAFE UNKNOWN | Wave A explicit rule | — | Wrong sync assumptions | Operator attestation later |
| Current confirmed source location | Production runtime is the only confirmed source location | CONFIRMED BY OPERATOR | Wave A | High | Blind overwrite of unknown local copies | Do not claim “no local copies exist” |

---

## 17. Routing / Rewrite / Entry Points

| Item | Current value | Classification | Source | Confidence | Risk | Next evidence required |
|------|---------------|----------------|--------|------------|------|------------------------|
| Static vs WP routing | Hybrid documented in boundary map | CONFIRMED BY SANITIZED EVIDENCE | Phase 2B | High | Wrong ownership map | Follow protected zones |

---

## 18. Source Repositories and Production Drift

| Item | Current value | Classification | Source | Confidence | Risk | Next evidence required |
|------|---------------|----------------|--------|------------|------|------------------------|
| Maintained canonical local/Git source | SAFE UNKNOWN | SAFE UNKNOWN | Wave A | — | Blind sync | Attestation |
| Manual production changes | Must be preserved (policy) | CONFIRMED BY REPOSITORY | Decision D-011 | High | Overwrite | Drift notes later |

---

## 19. Backup and Restore

| Item | Current value | Classification | Source | Confidence | Risk | Next evidence required |
|------|---------------|----------------|--------|------------|------|------------------------|
| Operator Beget full backup rule | Before every future task/work package, operator intends full Beget backup manually | CONFIRMED BY OPERATOR | Wave A | High | Treating as sole safety control | Remains plus scoped backup/validation/rollback/HITL/evidence |
| Hosting restore method details | Unknown | SAFE UNKNOWN | U-020 | — | No rollback proof | Wave E (later) |
| Plugin backup ≠ hosting backup | Policy accepted | CONFIRMED BY REPOSITORY | Decision D-013 | High | False safety | Remains policy |

---

## 20. Security / Cache / CDN / WAF

Unchanged — SAFE UNKNOWN (U-019).

---

## 21. Critical Business Routes

| Item | Current value | Classification | Source | Confidence | Risk | Next evidence required |
|------|---------------|----------------|--------|------------|------|------------------------|
| Public root | `https://i-seo.su/` registered | CONFIRMED BY OPERATOR | Wave A / route register | High | Incomplete inventory | More URLs later |
| Other key routes | Not supplied | SAFE UNKNOWN | Wave A | — | Untouchable-area miss | Operator URL list |
| Protected-zone decision | Operator does **not** declare permanently untouchable areas | CONFIRMED BY OPERATOR | Wave A | High | Misread as broad mutation license | All surfaces remain protected until separately chartered; every task needs scope/backup/validation/rollback |

---

## 22. Current Access Classes

| Class | Status | Classification | Source | Confidence | Risk | Next evidence required |
|-------|--------|----------------|--------|------------|------|------------------------|
| Capability: hosting | Exists (operator) | CONFIRMED BY OPERATOR | Wave A | High | Use without charter | Panel A3 still NOT AUTHORIZED |
| Capability: FTP/SFTP | Exists; SFTP used read-only in Phase 2B | CONFIRMED BY AUDIT | Phase 2B | High | Reuse without charter | New charter per session |
| Capability: WP admin | Exists; dedicated MARS account local; Admin UI challenge | CONFIRMED BY AUDIT (partial) | Phase 2B | High | Reuse without charter | Prefer browser HITL |
| A6 WPilot | Not installed | CONFIRMED BY SFTP | Phase 2B | High | Premature install | Phase 4B |
| Database / phpMyAdmin | Metadata only; not opened | CONFIRMED BY REPOSITORY / TASK | Phase 2B | High | Credential exposure | Separate DB charter |
| Exact protocol/host/port/user/password | Stored local-only; never in docs | CONFIRMED BY LOCAL VALIDATION | Phase 2B | High | Chat leakage | Keep Git-ignored |
| A0–A2 | Evidence classes as before | CONFIRMED BY REPOSITORY | Access classification | High | Secret in screenshot | Redaction guide |
| A3–A8 default | Charter-gated after 2B; A6–A8 unused | CONFIRMED BY REPOSITORY | Access classification / Phase 2B | High | Premature access | Future charters only |

---

## 23. Contributors (Wave A)

| Person | Role (operator statement) | Classification |
|--------|---------------------------|----------------|
| Andrey | Original frontend layout and forms; joint evolution after launch; programme operator | CONFIRMED BY OPERATOR |
| Anton (i-SEO programmer) | WordPress layer, blog, calculators, web commercial-proposal tool, related features; joint evolution | CONFIRMED BY OPERATOR |
| Nikita (owner of i-SEO) | Product ideas | CONFIRMED BY OPERATOR |

---

## 24. Conflicts

| Conflict ID | Description | Classification | Risk | Resolution |
|-------------|-------------|---------------|------|------------|
| CF-001 | Potential confusion: `https://i-seo.su/wp-admin/` vs Beget panel URL | RESOLVED (documentation) | High if ignored | Wave A correction: wp-admin is WordPress only; Beget panel URL remains SAFE UNKNOWN |
| CF-000 | No other Phase 2 evidence conflicts recorded | — | — | — |

---

## 25. SAFE UNKNOWN

See [ISEO-SU-SITE-OPS-SAFE-UNKNOWN-REGISTER-v1.md](ISEO-SU-SITE-OPS-SAFE-UNKNOWN-REGISTER-v1.md).

Wave A resolutions and remaining priorities:

| ID | Item | Wave A outcome |
|----|------|----------------|
| U-001 | Hosting provider | **RESOLVED** → Beget |
| U-002 | Control panel URL | Remains **SAFE UNKNOWN** (panel family Beget; exact URL unknown) |
| U-005 | Static / WP routing | Remains **SAFE UNKNOWN** |
| U-021 | Staging | **RESOLVED** → does not exist |
| U-022 | Maintained canonical source outside production | Remains **SAFE UNKNOWN** (production runtime confirmed as only confirmed source location) |
| U-024 | FTP/SFTP existence | **RESOLVED** existence → yes; exact model remains later |
| — | Exact access protocol/host/port/user | **SAFE UNKNOWN** until local secrets filled (values never enter this ledger) |

---

## 26. Evidence Still Required

**Immediate operator action (Phase 2A closeout):**

1. Fill local-only files per [ISEO-SU-LOCAL-ACCESS-SETUP-GUIDE-v1.md](ISEO-SU-LOCAL-ACCESS-SETUP-GUIDE-v1.md).  
2. Reply only `ACCESS FILES FILLED` + which access classes are populated.  
3. Do **not** paste secrets into chat.

**Deferred:** Waves B–E; architecture audit; Phase 3 passport; any connection.

---

## 27. Phase 2A Stop Condition

Phase 2A ends as **COMPLETE / AWAITING OPERATOR LOCAL ACCESS ENTRY**.

At this stop:

- no site connection;
- no public crawling by agent;
- no browser access by agent;
- no hosting login;
- no FTP/SFTP;
- no WordPress login;
- no WPilot installation;
- no token;
- no REST;
- no database access;
- no Localhost;
- no Storage writes;
- no ATLAS mutation;
- no registry mutation;
- no Git stage/commit/push;
- wait for operator to fill exact local files.

**Next gate:** `ISEO-SU-SITE-OPS — PHASE 2B LOCAL ACCESS FILE PRESENCE REVIEW`  
(Phase 2B verifies local file presence / non-empty required fields only — **no** connection unless a separate external-access charter is approved.)

**Do not authorize Phase 3 yet.**

---

*ISEO-SU SITE EVIDENCE INTAKE v1 · updated 2026-07-22 Phase 2A · no secrets · production connection NOT AUTHORIZED.*
