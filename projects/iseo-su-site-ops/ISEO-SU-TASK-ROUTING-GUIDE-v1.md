# ISEO-SU TASK ROUTING GUIDE v1

**Programme:** ISEO-SU-SITE-OPS  
**Purpose:** Practical first stop for ordinary production site tasks after architecture knowledge capture.  
**Authority rank:** #2 (after task-specific accepted production evidence)  
**Companions:** [ISEO-SU-CANONICAL-ROUTE-OWNERSHIP-MATRIX-v1.md](ISEO-SU-CANONICAL-ROUTE-OWNERSHIP-MATRIX-v1.md), [ISEO-SU-PRODUCTION-ARCHITECTURE-KNOWLEDGE-BASE-v1.md](ISEO-SU-PRODUCTION-ARCHITECTURE-KNOWLEDGE-BASE-v1.md)

**Global prerequisites for any production mutation**

1. Fresh full Beget backup (operator).
2. Exact task charter naming paths/surfaces.
3. Classify route via ownership matrix.
4. Preserve foreign WIP; selective Git staging only when chartered.
5. WPilot bridge/writes remain off unless separately approved.

---

## text change

| Step | Action |
|------|--------|
| Inspect first | Route matrix → is target static file, WP editor, or hardcoded template? |
| Likely SoT | Marketing HTML file **or** theme PHP template **or** WP post/ACF field |
| Access | SFTP for files; WP Admin for posts/ACF; never assume WP editor owns `/` |
| Backup | Exact file(s) or WP revision + Beget |
| Modify | Only the owning artifact |
| Validate | Public URL title/H1/snippet |
| Rollback | Restore file / revert post |
| Traps | Editing `home.html` instead of `page-home.php`; editing WP page body when template ignores `the_content` |

---

## SEO metadata

| Step | Action |
|------|--------|
| Inspect first | Static pages: `<title>` / meta in HTML or `page-home.php`. WP posts/pages: Yoast metabox |
| SoT | File head **or** Yoast fields |
| Access | SFTP / WP Admin |
| Backup | File or post |
| Modify | Matching channel only |
| Validate | View-source title/description; sitemap if URL added |
| Rollback | Restore |
| Traps | Homepage meta lives in **template**, not WP editor; dual `home.html` drift |

---

## static page layout

| Step | Action |
|------|--------|
| Inspect first | Physical path under docroot / `services/` / `cases/` |
| SoT | That `.html` file + shared css/js if layout depends on them |
| Access | SFTP read then scoped write |
| Backup | File + any shared asset touched |
| Modify | Prefer page-local markup; avoid `css/main.css` unless necessary |
| Validate | Desktop/mobile spot check; forms still present |
| Rollback | Restore files |
| Traps | PHP-capable HTML; relative `*__FORM.php` copies under `services/` |

---

## WordPress page content

| Step | Action |
|------|--------|
| Inspect first | Pages list — only 4 public pages; check assigned template + whether editor content length is used |
| SoT | If template hardcoded → theme PHP; if default + content → editor |
| Access | WP Admin read-only first |
| Backup | Beget + note template path |
| Modify | Do not “fix” empty homepage body in editor |
| Validate | Public URL |
| Rollback | Revisions / restore template |
| Traps | `glavnaya`, `blog`, `tariff-calc` are template-driven |

---

## blog

| Step | Action |
|------|--------|
| Inspect first | `/blog` hub vs single `/blog/{slug}.html` vs category |
| SoT | Post content + ACF «Записи» + `single.php` / `page-blog.php` |
| Access | WP Admin |
| Backup | Post revisions |
| Modify | Posts/ACF; theme only for chrome |
| Validate | Permalink pattern; category listing |
| Rollback | Revisions |
| Traps | `blog.html` is not live; tags disallowed in robots |

---

## header/footer

| Step | Action |
|------|--------|
| Inspect first | Which surface? Marketing HTML vs WP theme parts |
| SoT | Dual: hardcoded HTML **and** `content-topbar.php` / `content-footer.php` / `header.php` / `footer.php` |
| Access | SFTP both channels if global change intended |
| Backup | All chrome files touched |
| Modify | Explicitly list both channels in charter |
| Validate | `/`, `/blog`, one `.html`, `/tariff-calc` |
| Rollback | Restore chrome files |
| Traps | Updating only WP menu does **not** update marketing HTML chrome |

---

## menu

| Step | Action |
|------|--------|
| Inspect first | WP Admin → Menus («Меню 1», Primary) **and** hardcoded topbar links |
| SoT | Mixed |
| Access | WP Admin + theme parts |
| Backup | Export/screenshot menu; theme file copy |
| Modify | Both if global nav required |
| Validate | WP pages + static pages |
| Rollback | Restore menu + files |
| Traps | Theme topbar hardcodes many `/services/...` links |

---

## form

| Step | Action |
|------|--------|
| Inspect first | Page markup + `js/common.js` endpoint + matching `*__FORM.php` |
| SoT | Handler PHP + JS + page markup |
| Access | SFTP; **no form submit** in audits |
| Backup | Handler + JS + page |
| Modify | Extremely careful; charter required |
| Validate | Structural only unless operator HITL send |
| Rollback | Restore handlers/JS |
| Traps | Service-tree handler copies can diverge from root |

---

## calculator/tariff

| Step | Action |
|------|--------|
| Inspect first | `/tariff-calc` + ACF groups «Настройки калькулятора» / «Настройки каналов и тарифов» + `tarif-calc.php` + `common.js` |
| SoT | Hybrid — identify which layer owns the field |
| Access | WP Admin ACF for rates; SFTP for JS/template/handlers |
| Backup | ACF values attestation + files |
| Modify | One layer per change when possible |
| Validate | Open `/tariff-calc`; do not mail |
| Rollback | Restore layer |
| Traps | Marketing pages also embed tariff UI; theme `content-tarifs-*` mirrors |

---

## ACF

| Step | Action |
|------|--------|
| Inspect first | Field group list; confirm location by editing related object without saving |
| SoT | ACF field group data in DB |
| Access | WP Admin |
| Backup | Beget (DB) |
| Modify | Field values vs field group schema — schema changes are high risk |
| Validate | Front template that calls `get_field` |
| Rollback | DB/Beget |
| Traps | No `acf-json` sync dir on disk |

---

## web-KP

| Step | Action |
|------|--------|
| Inspect first | Treat as CPT `offer` + `/offers` + `single-offer.php` + ACF «Предложения» |
| SoT | WP offer posts + ACF |
| Access | WP Admin; **do not** export customer KP to Git |
| Backup | Beget |
| Modify | Offer fields only under charter |
| Validate | Structural Admin + robots privacy |
| Rollback | Revisions/Beget |
| Traps | `/web-kp` URL does not exist; content is private |

---

## CSS/JS

| Step | Action |
|------|--------|
| Inspect first | Is asset docroot `css/`/`js/` or theme? |
| SoT | Production asset files |
| Access | SFTP |
| Backup | Exact asset files |
| Modify | Minimal diff; avoid drive-by refactors |
| Validate | `/`, `/blog`, marketing sample, `/tariff-calc` |
| Rollback | Restore assets |
| Traps | `js/common.js` is revenue-critical |

---

## image

| Step | Action |
|------|--------|
| Inspect first | Docroot `img/` vs `wp-content/uploads/` |
| SoT | Matching tree |
| Access | SFTP / Media library |
| Backup | Replace with rename-keep-old when possible |
| Validate | Hotlink URLs |
| Rollback | Restore old file name |
| Traps | Homepage template uses relative `img/` / `../img/` paths |

---

## redirect

| Step | Action |
|------|--------|
| Inspect first | `.htaccess` vs physical file vs WP page |
| SoT | Usually `.htaccess` or replace file |
| Access | SFTP; **protected** |
| Backup | `.htaccess` mandatory |
| Modify | Only exact charter |
| Validate | redirect chain + final |
| Rollback | Restore htaccess |
| Traps | Breaking WP rewrite block; HTML-as-PHP line |

---

## plugin

| Step | Action |
|------|--------|
| Inspect first | Active/inactive matrix in knowledge base |
| SoT | Plugin dir + WP options |
| Access | WP Admin under charter |
| Backup | Beget + plugin files |
| Modify | Never casual activate/deactivate |
| Validate | Admin + frontend smoke |
| Rollback | Reverse activation / Beget |
| Traps | WP-Optimize inactive — enabling changes cache behavior |

---

## analytics/script

| Step | Action |
|------|--------|
| Inspect first | Hardcoded in HTML/theme heads; Jetpack may inject |
| SoT | Template/HTML and/or plugin |
| Access | SFTP / plugin settings |
| Backup | Files |
| Validate | View-source |
| Rollback | Restore |
| Traps | Dual chrome means dual insertion points |

---

## emergency repair

| Step | Action |
|------|--------|
| Inspect first | Symptom URL class via matrix; check `/` `/blog` Admin login |
| SoT | Depends |
| Access | Prefer Beget restore for unknown blast radius |
| Backup | Already should exist; take another if possible |
| Modify | Minimal revert of last known change |
| Validate | Critical routes list |
| Rollback | Beget full restore if unsure |
| Traps | Do not “fix” by editing both twins blindly; do not enable WPilot writes as emergency tool |

---

## Critical routes checklist (post-change)

- `/`
- `/blog`
- one marketing HTML (`/contacts.html` or `/about.html`)
- `/tariff-calc`
- `/offers` (if offers/KP adjacent)
- `/sitemap.xml` (if SEO/URL adjacent)

---

*Task routing guide v1 · 2026-07-24.*
