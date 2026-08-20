# ISEO-SU-SITE-OPS SAFE UNKNOWN Register v1

**Status:** ACCEPTED; **updated architecture knowledge capture** 2026-07-24; **reconciled post-launch / stabilization** 2026-08-20  
**Canonical locus:** `X:\AI MARS\projects\iseo-su-site-ops\`

Rule: do **not** invent values. Resolve only with evidence.

## Phase / capture links

| Artifact | Path |
|----------|------|
| Current state (brain) | [ISEO-SU-CURRENT-STATE-v1.md](ISEO-SU-CURRENT-STATE-v1.md) |
| Architecture knowledge base | [ISEO-SU-PRODUCTION-ARCHITECTURE-KNOWLEDGE-BASE-v1.md](ISEO-SU-PRODUCTION-ARCHITECTURE-KNOWLEDGE-BASE-v1.md) |
| Route matrix | [ISEO-SU-CANONICAL-ROUTE-OWNERSHIP-MATRIX-v1.md](ISEO-SU-CANONICAL-ROUTE-OWNERSHIP-MATRIX-v1.md) |
| Historical 2B audit | [ISEO-SU-READ-ONLY-PRODUCTION-AUDIT-v1.md](ISEO-SU-READ-ONLY-PRODUCTION-AUDIT-v1.md) |

---

## Resolved or narrowed in architecture capture (2026-07-24)

| ID | Item | Outcome |
|----|------|---------|
| U-009b | Plugin active matrix | **RESOLVED** via Admin: 11 active / 4 inactive listed in WP inventory |
| U-010 | ACF field groups | **RESOLVED at group level** — 4 groups titled; location-rule deep dump still partial |
| U-012 | Header/footer | **CONFIRMED dual-channel** with theme topbar hardcoding |
| U-015 | Web-KP technical surface | **NARROWED** — `/offers` + CPT `offer` + ACF «Предложения» + `single-offer.php`; public `/web-kp` 404; operator nickname confirmation still open |
| U-033 | Menus | **PARTIAL → NARROWED** — Primary / «Меню 1» confirmed; desktop services submenu now includes **Глоссарий** after calculator (accepted 2026-08-18); full item URL harvest still incomplete |
| U-034 | HTML PHP includes | **NARROWED** — sampled marketing HTML has no PHP includes; chrome duplicated |
| — | Permalink structure | **RESOLVED** — `/blog/%postname%.html` |
| — | Homepage editor/ACF use | **RESOLVED** — unused editor; 0 ACF fields on home |

---

## Resolved by accepted glossary launch / final baseline (2026-07-26 … 2026-08-18)

| ID | Item | Outcome |
|----|------|---------|
| G-U-002 | Glossary single `.html` URLs | **RESOLVED** — production uses slash CPT URLs; accepted baseline does not require blog-style `.html` |
| G-U-003 | Related glossary terms | **RESOLVED** — related-term block live; public eligible targets only |
| — | Glossary public exposure | **RESOLVED** — 184 published; 57 non-eligible non-public |
| — | `/glossary/` availability | **RESOLVED** — HTTP 200 archive |
| — | Desktop menu glossary link | **RESOLVED** — live after calculator |
| — | Mobile overflow on glossary | **RESOLVED** — fixed; SHA `4a1202b6…` |

---

## Still open (non-blocking for ordinary classified work)

| ID | Subject | Known | Unknown | Why unresolved | Operational impact | Blocks ordinary work? | Future evidence |
|----|---------|-------|---------|----------------|--------------------|-----------------------|-----------------|
| U-007 | PHP runtime version | Core requires ≥7.4; host serves WP 7.0.2 | Exact PHP version string | Site Health debug scrape inconclusive | Compatibility planning only | **No** | Browser Site Health HITL or hosting panel |
| U-015b | Operator “web-KP” nickname | Technical offers/CPT map ready | Whether staff call only this system “web-KP” | Naming confirmation needs operator | Communication clarity | **No** for edits if route known | One-line operator confirm |
| U-017 | Mail delivery path | Handlers use `mail()` | SMTP plugin/relay details | No mail plugin clearly owning delivery | Silent lead failure risk on handler edits | **No** if handlers untouched | Chartered handler/mail review |
| U-020 | Restore drill details | Beget backups used historically | Exact restore click-path/object IDs | Panel not opened by agent | Emergency speed | **No** for routine | Operator restore notes |
| U-022 | Offline canonical source | Not on production | Local Git/build existence | No server evidence | Sync fantasies | **No** if editing production SoT | Operator attestation |
| U-023 | Full drift inventory | Known twins home/blog; form copies | Complete twin list | Bounded discovery | Overwrite risk | **No** if matrix followed | Ongoing drift log |
| U-036 | WPilot header forwarding | Namespace registered | Auth header behavior | REST not authorized | 6D smoke only | **No** for site content work | GATE 6D |
| U-041 | WPilot DB tables physical | Admin schema said yes historically | Table existence without DB | No DB login | WPilot internals | **No** | DB charter |
| U-045/46 | 6D backup/drift | 6D blocked | Fresh backup line + live drift at 6D | Approvals absent | Bridge gate only | **No** for site content | Exact 6D lines |
| U-047 | `/services.html` intermittent 500 | File exists; later 200 | Root cause of one 500 | Transient server/upstream | Validate after services hub edits | **No** | Repeat probe + error log HITL |
| U-048 | Exact ACF location rules | Groups + consuming templates known | Full location UI export | Admin location panel scrape noisy | Wrong object edits | **No** if editing known objects | Export field groups |
| U-049 | `/offers` listing UX | Page exists; editor empty; CPT exists | How listing markup is composed | Not fully traced beyond default page template | Offers hub text edits | **No** if editing CPT/singles | Bounded template trace |
| U-050 | `varvara-new.php` business role | Title VVR-Searcher; 200 | Product ownership/use | Out of marketing IA | Avoid casual edit | **No** | Operator note |
| G-U-001 | Glossary Yoast focus workflow | Batch SEO titles/metadesc applied via Admin Yoast fields | Long-term preferred REST/meta automation pattern | Preference only | Content waves | **No** | Optional tooling polish |
| G-U-004 | Server inventory JSON retention | File on theme `inc/data/`; import UI disabled | Keep vs remove from production | Ops hygiene | Low | **No** | Operator cleanup preference |
| G-U-005 | Audit REVIEW queue (8 terms) | Independently **DEFERRED** in final corpus | Future reconsideration criteria only | Deferred pool | Blocks only those terms | **No** | Reopen via reconsideration rules |
| G-U-006 | Algorithm status currency | Expert terms may be APPROVED with caution notes | Current official status of АГС/Минусинск/etc. at publish polish | Needs expert docs check | Expert batch only | **No** | Primary-source verification before polish |
| G-U-007 | GEO vocabulary stability | GEO terms published as accepted corpus | Settled industry/official naming forever | Emerging topic | AI/GEO terms only | **No** | Optional expert revisit |

---

## Summary

**OPEN_BLOCKER = 0 · OPEN_REQUIRED = 0** for glossary/site-ops. Remaining SAFE UNKNOWN items are **named** and **non-blocking** for ordinary work that follows Current State, Task Routing Guide, and Route Ownership Matrix.

WPilot bridge/REST remains a separate optional gate (6D), not required for ordinary site content/file tasks.

---

*SAFE UNKNOWN Register v1 · updated stabilization 2026-08-20.*
