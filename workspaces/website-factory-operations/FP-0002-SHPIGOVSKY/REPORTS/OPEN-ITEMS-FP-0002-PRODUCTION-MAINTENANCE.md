# OPEN ITEMS — FP-0002 Production Maintenance

**Phase:** PRODUCTION / MAINTENANCE — STABLE  
**Updated:** 2026-09-09 (knowledge promotion + workspace closeout; production core `0.3.32-blog-hub-announcement-01`)

Launch implementation tasks are **CLOSED**. Later accepted production-maintenance waves (Specialists Hub, canonical URL, SEO meta, Contacts maps, Schema.org, Open Graph, Blog Hub announcement) are **CLOSED**. Only operator / external / optional follow-ups remain.

Classification: **OPEN** = still actionable · **OPTIONAL** = non-blocking · **OPERATOR / EXTERNAL** = needs human UI or third party · **CLOSED** = do not reopen as a blocker · **STALE** = superseded.

---

## Operator follow-ups (non-blocking)

| # | Item | Classification | Owner | Evidence |
|---|------|----------------|-------|----------|
| 1 | Submit sitemap to **Google Search Console** (`https://shpigovsky.ru/wp-sitemap.xml`) | **OPERATOR / EXTERNAL** — OPEN | Operator | P18I AUTH BLOCKER; no later GSC proof |
| 2 | Submit sitemap to **Yandex Webmaster** | **OPERATOR / EXTERNAL** — OPEN | Operator | P18I AUTH BLOCKER; no later Webmaster proof |
| 3 | Final **legal sign-off** on Cookie Policy (factually current) | **OPERATOR / EXTERNAL** — OPEN | Operator / Legal | P18H; no legal sign-off evidence |
| 4 | Set `lead_retention_days=730` if accepted; align Privacy Policy wording | **OPERATOR / EXTERNAL** — OPEN | Operator | P18H recommended; production config still `0` unless later Admin change |
| 5 | Ongoing content, SEO, and feature work via Admin (normal production) | **OPTIONAL** (standing) | Editor / Operator | Normal ops — not a defect |
| 6 | Optional: tune anti-spam thresholds from real spam evidence (keep false-positive risk low) | **OPTIONAL** | Operator / Tech | No new real-spam charter since anti-spam v1 |
| 7 | Optional SEO: legal pages `Disallow` in robots but currently lack `noindex` meta | **OPERATOR / EXTERNAL** — OPEN | SEO / Operator | Olya robots ownership; human decision |
| 8 | Optional authenticated **Yandex Schema.org validator** on live URLs | **OPTIONAL / EXTERNAL** | Operator | Schema wave ATTENTION; not evidenced |
| 9 | Optional external **Facebook/Meta OG debugger** on live URLs | **OPTIONAL / EXTERNAL** | Operator | OG wave ATTENTION; not evidenced |

Do **not** auto-close items 1–4, 7–9 without operator evidence.

---

## Closed (do not reopen as launch or tech blockers)

- Indexing approval — **OPEN — human-approved**; P18G guard active; P18J synthetic QA separated
- Olya SEO robots restoration + OPEN/CLOSED ownership separation — **CLOSED** (2026-08-21)
- SMTP verification — **CLOSED** (P18D-FU01)
- Privacy / cookie runtime — **CLOSED** (P18E)
- Pre-cutover / cutover / launch crawl — **CLOSED** (P18I)
- Sitemap **technical** validity — **CLOSED** (submission remains operator)
- Native form anti-spam v1 — **CLOSED**
- Dashboard / Russian mail UX polish — **CLOSED** (P23)
- Workspace / Git / MARS stabilization (2026-08) — **CLOSED** (later waves reopened then closed their own tails)
- WPilot Bearer/TLS background probe — **INVALID EVIDENCE**; `X-WPilot-Token` read-only probe **CLOSED**
- Specialists Hub (dedicated template, automatic listing, Admin enable/disable, existing cards) — **CLOSED**
- Specialists Hub Admin UX (ACFE checkbox shim + reusable enable/disable) — **CLOSED**
- Specialists Hub layout polish — **CLOSED**
- Specialists canonical URL `/specialisty/` + `/specyalisty/` 301 — **CLOSED**
- Global SEO title / Meta Description output across supported public types — **CLOSED**
- Contacts Yandex Constructor maps + per-row scroll toggle — **CLOSED**
- Project-owned Yandex-oriented JSON-LD Schema.org — **CLOSED** (authenticated Yandex validator remains optional #8)
- Global Open Graph owner — **CLOSED** (Facebook debugger remains optional #9)
- Blog Hub dedicated announcement field `article_hub_announcement` — **CLOSED** (SHA-record: `33d13bed`)
- Knowledge promotion + FP-0002 Git/worktree closeout 01 — **CLOSED** when that wave is pushed (docs only)

---

## Operational rules (maintenance)

1. **Editorial truth** = current production DB (Olya/Admin edits).
2. Technical waves start with **fresh intake** from **current origin** — do not restore old launch baselines over live content.
3. **Indexing is human-owned** — agents must not close without explicit command.
4. **SEO robots policy is Olya-owned** — OPEN serves canonical SEO robots; hashes in reports are evidence, not eternal policy (`DOCS/OPERATIONS-INDEXING-ROBOTS-OWNERSHIP-v1.md`).
5. P18G guard remains active; synthetic guard QA must use authorized QA context only (P18J).
6. New features → new bounded waves with their own reports and a **new clean worktree**.
7. Form spam controls stay **first-party** unless a new charter authorizes an external CAPTCHA provider.
8. WPilot probes use **`X-WPilot-Token`** only; never assume Bearer. Distinguish `TRANSPORT_ERROR` / `AUTH_ERROR` / `VALID_RUNTIME_RESPONSE`.
9. Distinct frontend surfaces need **dedicated editorial owners** (hero lead ≠ hub card ≠ SEO ≠ OG ≠ Schema). One SEO field set may feed OG/Schema **consumers**; each output layer stays a separate technical owner.
10. Trusted Admin embeds (e.g. Yandex Constructor) require **narrow** output handling — never a global script allowlist.

---

## References

- Current handoff: `REPORTS/FP-0002-NEXT-WEBGPT-HANDOFF.md`
- Current status: `PROJECT-STATUS.md`
- Knowledge closeout: `REPORTS/REPORT-FP-0002-KNOWLEDGE-PROMOTION-FINAL-WORKSPACE-CLOSEOUT-01.md`
- Olya robots restoration: `REPORTS/REPORT-FP-0002-PROD-MAINT-OLYA-ROBOTS-RESTORATION.md`
- Robots ownership runbook: `DOCS/OPERATIONS-INDEXING-ROBOTS-OWNERSHIP-v1.md`
- Native anti-spam v1: `REPORTS/REPORT-FP-0002-PROD-MAINT-NATIVE-ANTISPAM-V1.md`
- Maintenance baseline snapshot (2026-08-24): `REPORTS/BASELINE-FP-0002-PRODUCTION-MAINTENANCE-STABLE.md`
