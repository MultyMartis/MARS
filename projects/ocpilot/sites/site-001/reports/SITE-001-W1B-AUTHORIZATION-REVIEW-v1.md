# SITE-001 W1B Authorization Review v1

**Type:** Pre-W1B authorization review — **documentation only**; discovery performed read-only  
**Date:** 2026-06-08  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`

**Reviews:**

| Document | Role |
|----------|------|
| [SITE-001-W1B-THEME-BRANDING-MAP-v1.md](SITE-001-W1B-THEME-BRANDING-MAP-v1.md) | W1B discovery inventory |
| [SITE-001-W1-EXECUTION-PACK-v1.md](SITE-001-W1-EXECUTION-PACK-v1.md) | W1B scope and targets |
| [SITE-001-W1-EXECUTION-AUTHORIZATION-v1.md](SITE-001-W1-EXECUTION-AUTHORIZATION-v1.md) | Program-level W1 authorization |
| [SITE-001-W1A-DECISION-v1.md](SITE-001-W1A-DECISION-v1.md) | W1A **PASS WITH NOTES** — prerequisite |
| [project-access-brief.md](../project-access-brief.md) | Theme write flag **YES** on TEST |

---

## Authorization question

**May supervised W1B (theme hardcoded contacts and brand strings) begin on TEST?**

## **AUTHORIZED WITH NOTES**

---

## Gate review

### Can W1B be executed safely?

**YES — on TEST, under existing W1 charter**, with the notes below.

| Safety factor | Status | Evidence |
|---------------|--------|----------|
| Environment | **TEST only** | `sibcar.new-site.space` |
| W1A prerequisite | **COMPLETE** | [SITE-001-W1A-DECISION-v1.md](SITE-001-W1A-DECISION-v1.md) — PASS WITH NOTES |
| Write charter | **ACTIVE** | Approver **Андрей**; theme writes **YES** on TEST |
| Change Request | **APPROVED** | CR-SITE-001-W1-2026-06-08 |
| Rollback plan | **AVAILABLE** | [SITE-001-W1-ROLLBACK-PLAN-v1.md](SITE-001-W1-ROLLBACK-PLAN-v1.md) T2 — theme file revert |
| Backup | **EXECUTED** | Operator-confirmed 2026-06-08 (pre-W1A; still valid for W1B per charter) |
| Discovery complete | **YES** | [SITE-001-W1B-THEME-BRANDING-MAP-v1.md](SITE-001-W1B-THEME-BRANDING-MAP-v1.md) |
| Production | **NOT TOUCHED** | **PRODUCTION WRITES FORBIDDEN** |

**Safe execution path:** Edit 7 primary theme files via FTP; clear theme/modification cache; verify homepage header/footer/contact page; retain Beget file backup or take pre-W1B file snapshot.

---

### Any blockers?

| ID | Blocker | Status | Impact on W1B |
|----|---------|--------|---------------|
| **C-04** | WhatsApp link decision | **OPEN** | Blocks **W1B-D** URL replacement only — can **hold** `wa.me/79539979910` or remove link until operator decides |
| C-03 | Logo assets staged | **OPEN** | Blocks **W1D only** — does **not** block W1B text/phone/alt edits |
| C-10 | Admin URL on access brief | **OPEN** | Informational — not blocking W1B |

**No hard blocker** for W1B text, phone, copyright, legal line, logo **alt text**, or homepage H1/body — provided C-04 is handled as **hold-or-skip** for WhatsApp URLs.

---

### Any dependency on logos?

**NO — for W1B execution.**

| Item | W1B | W1D |
|------|-----|-----|
| Logo `alt="АЦ Хмельницкий"` → `alt="СИБКАР"` | **YES** — text only | — |
| Logo SVG/PNG file swap | — | **YES** — requires C-03 staged assets |
| Visual logo appearance | Legacy artwork remains until W1D | Expected after W1B-F alt change only |

W1B can proceed **without** new logo files. W1D should follow when C-03 closes.

---

### Any dependency on W1C?

**NO — W1B does not require W1C first.**

| Surface | W1B | W1C |
|---------|-----|-----|
| `header.twig` / `footer.twig` phones, copyright, alt | **W1B** | — |
| `home.twig` H1 and body | **W1B** | — |
| `contact.twig` / `about.twig` visible H1 and body | **W1B** | — |
| `/contact/` `<title>` and meta description | — | **W1C** (`contact.php` controller) |
| `/about` controller meta | — | **W1C** (`about.php`) |
| Information module pages (privacy, loan-terms, etc.) | — | **W1C** |

**Recommended order:** W1B before or parallel to W1C. W1C still required for full page-level SEO on custom routes.

---

## Notes (non-blocking / conditional)

| # | Note |
|---|------|
| N-01 | **C-04:** Do not change WhatsApp URLs until operator supplies target URL or approves link removal. Other W1B rows may proceed. |
| N-02 | Admin `config_telephone` (`+73833886890`) ≠ theme phone (`+73833885523`) — consider syncing in W1B session. |
| N-03 | Address `ул. Богдана Хмельницкого` in `header.twig` is **geographic** — apply operator address policy before replacing with LE-0005 legal address. |
| N-04 | Product template review quotes (`category_backup.twig`) — optional W1B scope; include in W1F grep if deferred. |
| N-05 | **PRODUCTION WRITES FORBIDDEN** — unchanged. |
| N-06 | Pre-W1B incremental file backup recommended (7–10 files) even though pre-W1A full backup exists. |

---

## Verdict rationale

W1B discovery is **complete**. All W1 execution gates except **C-04 (WhatsApp)** remain compatible with supervised theme edits on TEST. Logo file swap is **not** a prerequisite for W1B. W1C is **complementary**, not blocking.

**W1B may begin** under supervised session with `# REPORT — SITE-001 W1 W1B`, editing scope per [SITE-001-W1B-THEME-BRANDING-MAP-v1.md](SITE-001-W1B-THEME-BRANDING-MAP-v1.md).

**Production:** **NOT AUTHORIZED**.

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-08 | **CREATED** — verdict **AUTHORIZED WITH NOTES** |

*SITE-001 W1B Authorization Review v1 — review + read-only discovery; no theme modifications.*
