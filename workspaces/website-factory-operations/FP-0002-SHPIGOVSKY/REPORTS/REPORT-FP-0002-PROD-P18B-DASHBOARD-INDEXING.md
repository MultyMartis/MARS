# REPORT — FP-0002 PROD-P18B Dashboard + Indexing Control

**Date:** 2026-08-19  
**Project:** FP-0002 / Шпиговский Дом  
**Wave:** PROD-P18B  
**Core:** `0.3.11-p18b`  
**Evidence:** `REPORTS/evidence/prod-p18b-dashboard-indexing/`

---

## 1. Status

**PARTIAL PASS**

P18B operator-status and indexing-control work is complete on the WordPress origin. Public `https://shpigovsky.ru/` was WordPress at first intake and later consistently served **legacy Craftum CMS** (five-shot reprobe). The Dashboard was updated to tell that truth. Indexing was **not** left OPEN.

Required closeout string is therefore **not** claimed as a full production-HTTPS-on-apex close. The three P18B responsibilities (Dashboard truth, safe indexing control, WP Forge knowledge) **are** delivered.

---

## 2. Production Reality

Required: **P18B CURRENT PRODUCTION REALITY VERIFIED**

| Surface | Value |
|---------|--------|
| Live domain (WP `home` / `siteurl`) | `https://shpigovsky.ru` |
| WordPress | 7.0.4 |
| PHP (php8.2 probe / widget CLI) | 8.2.28 |
| HTTPS certificate | Let's Encrypt valid for `shpigovsky.ru` + `www` (and archive SANs) |
| HTTP → HTTPS | 301 |
| Public apex at latest verification | **Craftum CMS** (`generator` Craftum; ~531 KB) — **not** WordPress |
| WordPress origin | Beget docroot `/home/s/shpigovsky/shpigovsky.ru/public_html`; inner routes on `shpigovsky.beget.tech` |
| NS | Operator: cutover **DONE**. Public A @8.8.8.8 = `45.130.41.70`. Resolver NS answers remain split (local REG.RU vs earlier Beget). Dashboard does **not** show NS as pending. |
| SMTP mailbox | `noreply@shpigovsky.ru` exists (operator); WP SMTP **PENDING** |
| Mail | **suppressed** (`pre_wp_mail` MU present) |
| Indexing (WordPress) | **CLOSED** (`blog_public=0`, origin `robots.txt` `Disallow: /`) |
| WPilot | 0.3.2 · write disabled |
| Debug | off |
| Environment | `production` |

Do **not** treat public Craftum `robots.txt` (`Disallow: /*?`, sitemap `/sitemap.xml`) as the WordPress indexing owner.

---

## 3. Backup

Required: **FRESH BEGET BACKUP CONFIRMED BY OPERATOR**

Exact Beget timestamp was **not** safely discoverable. No additional full dump was created. Exact-file Layer B snapshots: `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p18b-layer-b-pre`. A local MARS full backup is **not** claimed.

---

## 4. Dashboard Before

Stale operator-facing values (option `fp02_metacode_system_meta` + widget copy):

- Latest wave P18A / P17-FU02 era next steps
- Temporary host `shpigovsky.beget.tech` / “future host”
- SSL IN PROGRESS / public apex routing pending phrased as if NS were the remaining gate
- Backup text still pointing at P14 / “launch backup required”
- English-heavy pre-cutover wording

See `DASHBOARD-BEFORE.json`.

---

## 5. Dashboard After

Required: **METACODE DASHBOARD REFLECTS CURRENT PRODUCTION REALITY**

Widget (`MetaCODE / Состояние системы`) now:

- Russian operator labels (Сайт, Среда, Боевой домен, Текущее состояние, Последняя волна, Домен, DNS/NS, HTTPS, Почта, Индексация, Бэкап, Последняя проверка, Следующие шаги)
- Runtime reads for WP/PHP, indexing, debug, WPilot, mail suppression, core version, `home`/`siteurl` host
- Metadata for wave, backup acknowledgement, DNS/NS note, public-origin note, last verification
- Indexing banner **before** the status table
- No “Future host”, no “READY FOR MANUAL NS SWITCH”
- Next step 1 = bind public apex to WordPress (because latest public probe is Craftum)
- Then SMTP → forms QA → Metrika goals → internal stats → Olya indexing → sitemaps → crawl

Rendered as user `admin` (Olya): CLOSED banner, «Открыть индексацию», nonce + POST + confirm present. See `DASHBOARD-RENDER.json` (nonce redacted in HTML snippet).

---

## 6. Indexing Control

Required: **ONE INDEXING STATE OWNER / ONE ADMIN OPERATION**

| Item | Implementation |
|------|----------------|
| Owner | `Shpigovsky\Core\Admin\IndexingControl` |
| Operation | `SET SITE INDEXABILITY = OPEN / CLOSED` |
| Surfaces | `blog_public` + physical `robots.txt` (when the file exists); core meta robots follow `blog_public` |
| Button | «Открыть индексацию» / «Закрыть индексацию» from **real** `blog_public` |
| Permission | `manage_options` (Administrator — Olya `admin`) |
| Nonce | `fp02_set_indexability` |
| Confirmation | `window.confirm` + hidden `fp02_confirm=1` |
| Mutation | POST `admin_post_fp02_set_indexability` only — no GET, no `nopriv` |
| After | verify state; admin notice; **no** sitemap submission; **no** Search Console/Yandex |

Search pages remain `noindex` via theme helpers even when OPEN (intentional exclusion).

---

## 7. Human Approval

Required: **INDEXING OPEN REQUIRES EXPLICIT HUMAN ACTION**

FP-0002 approval: **Olya** or explicit operator instruction.

Implementing the button is **not** authorization to launch indexing. This wave left production **CLOSED**.

---

## 8. QA

Required: **INDEXING QA COMPLETE — FINAL STATE CLOSED**

| Case | Result |
|------|--------|
| 1 CLOSED | `blog_public=0`; origin robots `Disallow: /`; `/privacy-policy/` on Beget inner host `noindex, nofollow`; Dashboard CLOSED |
| 2 OPEN (reversible CLI only) | `set_site_indexability(true)` → `blog_public=1`; origin robots WP-style allow; no sitemap push |
| 3 CLOSE again | `set_site_indexability(false)` + emergency close after first-run print crash → `blog_public=0` |

Public HTTPS robots during CASE 2/3 still showed Craftum when apex was not WordPress — **not** used as WP pass/fail.

---

## 9. Robots / Meta

| Owner | CLOSED (final) |
|-------|----------------|
| `blog_public` | `0` |
| WP origin `robots.txt` | `Disallow: /` + Sitemap `https://shpigovsky.ru/wp-sitemap.xml` |
| Representative WP page | `noindex, nofollow` (`/privacy-policy/` on Beget inner host) |
| Public apex robots | Craftum `Disallow: /*?` when apex is not WP — separate site |

No contradictory WP state (`blog_public=0` with origin robots allowing `/`).

---

## 10. Mail / SMTP

- Mailbox exists: **YES** — `noreply@shpigovsky.ru`
- WordPress SMTP configuration: **PENDING**
- Suppression: **ON**
- This wave did **not** configure SMTP and did **not** remove suppression.
- No mailbox password stored in Git.

---

## 11. Forms Next Wave

Recorded only (not implemented):

1. Admin-configurable Yandex Metrika JS goal per form; fire after **backend-confirmed success**, not click.
2. Internal WP lead statistics / lead registry (timestamp, form, source page, delivery status, safe contact data, UTM, optional Metrika status).

---

## 12. Dashboard DoD Knowledge

Required: **MAJOR PRODUCTION WAVE IS NOT DONE WHILE OPERATOR STATUS UI IS STALE**

Canonized in WP Forge Definition of Done (FW-S-19) operational status panel section.

---

## 13. WP Forge Knowledge

| Rule | Where |
|------|--------|
| Live status panel is production state | FW-S-19 DoD · Admin UX §10.3 · AP-021 |
| Explicit indexing approval + Dashboard control | FW-S-32 |
| Default SMTP technical sender `noreply@<domain>` | Forms/SMTP §5 · ADR-P19 · starter checklist · launch SOP |

---

## 14. Source / Production Parity

**6/6 MATCH** — see `SOURCE-PROD-PARITY-FINAL.json`.

Touched: core bootstrap, `SystemDashboard.php`, **new** `IndexingControl.php`, `ModuleRegistry.php`, `ActivityLog.php`, theme `seo-integrations.php`.

Client page content was not mutated.

---

## 15. Git

Isolated worktree from `origin/mars/canonical-post-recovery`. Dirty main foreign WIP untouched. Secret scan on staged paths. No SMTP password.

SHAs: `REPORTS/evidence/prod-p18b-dashboard-indexing/GIT-CHECKPOINT.json` (written after push).

---

## 16. Remaining Work

1. Bind public apex to WordPress  
2. SMTP (`noreply@shpigovsky.ru`)  
3. Forms delivery QA  
4. Metrika form goals (backend-confirmed)  
5. Internal form statistics  
6. Olya indexing approval  
7. Sitemap submissions  
8. Final crawl  

Completed items **not** reopened: NS (operator), `home`/`siteurl`, legacy 7/7, legal DEMO owner.

---

## 17. Acceptance

**Not claimed as full P18B COMPLETE on public apex HTTPS/WordPress**, because visitors to `https://shpigovsky.ru/` currently may see Craftum.

**Claimed:**

- MetaCODE Dashboard updated to **current** live-operator reality (including the public-origin warning)
- Stale pre-cutover “NS pending / future host” **removed**
- Safe Admin indexing control implemented
- Indexing requires explicit human approval
- Final WordPress indexing state remains **CLOSED**
- Fresh Beget backup acknowledged
- `noreply@` SMTP naming recorded in WP Forge
- Operational status panels are part of major-wave Definition of Done

```text
THE WORDPRESS DASHBOARD MUST TELL OLYA AND THE OPERATOR
THE TRUTH ABOUT THE SITE RIGHT NOW.
```
