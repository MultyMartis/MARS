# Forge WordPress — Production incident lessons v1

**Date:** 2026-08-18  
**Source:** FP-0002 (anonymized). Prevention maps to anti-patterns / SOPs.

---

## INC-01 — Host IP access block / access recovery

| | |
|--|--|
| Detection | SSH/SFTP fail after IP policy; Admin antibot |
| Impact | Deploy/QA blocked; false “host down” |
| Root cause | Hosting firewall vs operator/agent IPs; jail to placeholder docroot |
| Fix | Unblock; bind to **real** docroot; re-validate access matrix |
| Prevention | Access matrix first (P03/P04 pattern); do not assume `beget.tech` jail = product |

## INC-02 — Duplicate slug UI

| | |
|--|--|
| Detection | Two permalink rows; slug revert |
| Impact | URL uncertainty |
| Root cause | Custom UI + native + custom `post_name` preference |
| Fix | P13-FU01 native-only |
| Prevention | AP-002 |

## INC-03 — iOS lifebuoy repeated false-positive fixes

| | |
|--|--|
| Detection | Operator: Apple static; Windows OK |
| Impact | Extra waves; false technical PASS |
| Root cause | Emulation; stacked transform/contain/fixed |
| Fix | Physical iPhone; bounded iOS fallback |
| Prevention | AP-010, AP-011, FW-S-17 |

## INC-04 — Public `mars-runtime` mutating script

| | |
|--|--|
| Detection | Hygiene audit; GET created pages/menus |
| Impact | Live object pollution |
| Root cause | Leftover HTTP-executable populate script |
| Fix | Snapshot; delete folder; rollback objects |
| Prevention | AP-012, AP-013, FW-S-20 |

## INC-05 — Local-runtime residue on production

| | |
|--|--|
| Detection | `WP_ENVIRONMENT_TYPE=local`; local-labelled MU |
| Impact | Wrong classification; mail labeled local |
| Root cause | Full local→host copy |
| Fix | P15 env cleanup; reclassify suppress |
| Prevention | FW-RB-05 |

## INC-06 — `.test` URLs on production frontend

| | |
|--|--|
| Detection | HTML crawl |
| Impact | Broken links; unprofessional |
| Root cause | Seeded local URLs |
| Fix | Bounded option/postmeta rewrite to current host |
| Prevention | Env scan before pre-cutover |

## INC-07 — Manual operator CSS drift risk

| | |
|--|--|
| Detection | SHA mismatch `v9-style.css` |
| Impact | Next deploy would destroy accepted UI |
| Root cause | Live CSS edits |
| Fix | Canonize into source |
| Prevention | AP-003 |

## INC-08 — ACF/content authority drift

| | |
|--|--|
| Detection | Admin values ≠ old DB dump |
| Impact | Wrong restore |
| Root cause | Treating Git/old dump as content SoT |
| Fix | Live DB is Admin truth |
| Prevention | FW-RB-01 |

## INC-09 — Raw Options Admin exposure

| | |
|--|--|
| Detection | Menu audit |
| Impact | Accidental option destroy |
| Root cause | Developer leftovers |
| Fix | Menu hygiene |
| Prevention | AP-006 |

## INC-10 — Beget placeholder vs real docroot

| | |
|--|--|
| Detection | FTP home empty `*.beget.tech` while product lives under domain folder |
| Impact | Working on the wrong tree |
| Root cause | Account jail |
| Fix | Access repair to real `public_html` |
| Prevention | Access validation before any write |

## INC-11 — SEO robots destroyed by indexability OPEN template

| | |
|--|--|
| Detection | Live `/robots.txt` became short generic OPEN body after CLOSE→OPEN |
| Impact | Editor SEO crawl policy lost while site remained “OPEN” |
| Root cause | `IndexingControl::robots_body(true)` wrote a generic template after CLOSE overwrote the physical SEO file |
| Fix | Canonical SEO policy asset; OPEN restores it; CLOSE backs up first |
| Prevention | ROBOTS-001…003 (`FORGE-WORDPRESS-ROBOTS-OWNERSHIP-LESSONS-v1.md`) |

---

*Incident lessons v1.*
