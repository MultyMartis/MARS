# I-SEO Report Hub — Report Delivery Client Handoff UX Charter v0.1

**Status:** PLANNING / CHARTER ONLY — no app-source; no runtime; no DB mutation; no SQL/migration; no share token; no public route change; no artifact regeneration  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-28  
**Authority:** Operator I-SEO Report Hub Report Delivery Client Handoff UX Charter 01  
**Related:**
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-DESIGN-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-DESIGN-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-COPY-PACK-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-COPY-PACK-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-IMPLEMENTATION-PLAN-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-VALIDATION-PLAN-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-VISUAL-QA-RESULT-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-VISUAL-QA-RESULT-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-HARDENING-RESULT-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-HARDENING-RESULT-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-IMPLEMENTATION-RESULT-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-IMPLEMENTATION-RESULT-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-CHARTER-v0.1.md)

---

## 1. Purpose

Спроектировать **docs/policy слой** Client Handoff UX после готового Public Share MVP.

Charter отвечает:

1. Что делает i-SEO специалист после финализации отчёта?
2. Как понять, что отчёт delivery-ready?
3. Какой export/share отправлять клиенту?
4. Какой текст/ссылку отправлять?
5. Что видит или получает клиент?
6. Как не отправить неверную/устаревшую ссылку?
7. Как (пока) отслеживать handoff — и нужно ли DB?
8. Что входит в MVP и что откладывается?
9. Как учесть Visual QA minor issues до/в UX implementation?

Эта волна — **documentation / policy only**. Code, DB-11, token creation, public route change и artifact mutation **не** выполняются здесь.

---

## 2. Current Baseline

### Report Delivery Public Share Visual QA 01

| Item | Value |
|------|-------|
| Primary | `9e9101879904b4a981cf58a5e04aeac64cd3baf2` |
| Hash-record | `ce5214428b8026c274d9b7634650769d316f248f` |
| Tip HEAD (at charter start) | `d98482799eacee6560ef89ad7bdc674665a89e12` |
| Status | **COMPLETE** |
| Verdict | **PASS_WITH_MINOR_ISSUES** |
| Push | **no** |
| Smoke | **86/86 PASS** |
| BLOCKER / MAJOR / MINOR | **0** / **0** / **2** |
| Active shares | **0** |
| `report_export_shares` | **4** revoked rows (all export id **4**) |
| Artifacts | unchanged |
| App-source / runtime code | unchanged |

Minor issues:

| ID | Finding |
|----|---------|
| `UI-REL-STORAGE-PATH` | Auth export detail shows relative `storage/exports/...` path |
| `UI-LIST-SHARE-LABEL` | List badge says `No`; detail says `Not shareable` |

Evidence: `X:\AI MARS STORAGE\incoming\iseo-report-hub\public-share-visual-qa-01\`

### Public Share Hardening / Implementation / DB-10

| Wave | Key facts |
|------|-----------|
| Hardening 01 | Token exact 64-hex; malformed/invalid **404**; revoked/expired/max_access **410**; PDF stream headers hardened; once UI only; smoke **66/66** |
| Implementation 01 | Public `GET /share/report/{token}`; internal shares CRUD/revoke; token_hash only; plaintext once |
| DB-10 | Table `report_export_shares`; token hash only; no plaintext token column |

### Public share route / eligibility (current)

| Route | Behavior |
|-------|----------|
| `GET /share/report/{token}` | Direct PDF stream (no client cover page) |
| Internal shares | Create / list / revoke for eligible export |

| Export id | Shareable? | Reason |
|-----------|------------|--------|
| 1 | No | HTML + legacy |
| 2 | No | Legacy PDF metadata NULL |
| 3 | No | HTML |
| 4 | Yes | Styled PDF v2 |

### DB current share state (read-only check this charter)

| Metric | Value |
|--------|-------|
| Target | `iseo_report_hub_dev` @ `127.0.0.1` |
| schema_migrations | **9** |
| tables | **16** |
| report_exports | **4** |
| report_export_shares | **4** (all revoked; export id **4**) |
| active shares | **0** |
| users / roles | **1** / **6** |
| clients / projects / sites | **1** / **1** / **1** |
| reporting_periods | **2** |
| weekly_checkpoints | **4** |
| monthly_report_contents | **1** |
| report_blocks | **6** |
| report_snapshots | **1** |

### Current limitation

Public delivery is a **raw PDF token stream**, not a client handoff experience. Operator can create/revoke links, but there is:

- no client-facing cover page;
- no handoff checklist;
- no prepared copy / email / Telegram text;
- no “delivery-ready” operator workflow;
- no durable “handed off” tracking;
- no recoverable public URL after once-display (token_hash only).

---

## 3. Problem

Public Share MVP exists and passed hardening + visual QA, but **operator → client handoff is not productized**.

Without a handoff layer, specialists risk:

- sending wrong/old/revoked links;
- sending HTML or legacy PDF exports;
- forgetting expiry wording;
- having no standard client message;
- having no clear “ready to send” gate after finalize → export → share.

---

## 4. Scope

### In scope (this charter)

- handoff UX design;
- product options A–E comparison;
- MVP decision;
- copy pack requirements;
- readiness checklist;
- operator warnings;
- client experience decision for MVP;
- Visual QA minor issues handling policy;
- next-wave recommendation (implementation vs DB-11).

### Out of scope

- app-source / runtime code edits;
- DB migration / SQL;
- share token creation;
- public route behavior change;
- client portal;
- email automation;
- artifact regeneration / new exports;
- production deployment.

---

## 5. Product Options

### Option A — Direct PDF token link only

Current Public Share MVP. Operator creates share and sends URL manually.

| Pros | Cons |
|------|------|
| Already implemented | No client context |
| Simple; low public surface | No checklist / standard wording |
| | Easy to send wrong/old link |

### Option B — Internal handoff panel + copy pack

Internal UI around existing token: readiness checklist, copy client message, link status, latest styled PDF guidance. **No new public route.**

| Pros | Cons |
|------|------|
| Low risk | Client still gets direct PDF link |
| Improves operator workflow | No branded public page |
| No portal / no email | |
| Fits current MVP security model | |

### Option C — Public lightweight landing page

Token route shows landing (title/month/client, download button, expiry, contact) then download.

| Pros | Cons |
|------|------|
| Better client UX | Larger public surface |
| | Route behavior change |
| | Extra privacy review |
| | Conflicts with current direct PDF stream |

### Option D — Client portal

Client login, view/download reports.

| Pros | Cons |
|------|------|
| Strongest long-term model | Large scope (auth, roles, onboarding) |

### Option E — Email delivery automation

System sends email with link/copy.

| Pros | Cons |
|------|------|
| Automated delivery | Mail config, deliverability, templates, privacy, reputation |

---

## 6. Recommended MVP Decision

**Option B:** Internal handoff panel + copy pack.

Keep public route as **direct PDF token stream**.

Do **not** build in this next layer:

- public landing page (Option C);
- client portal (Option D);
- email automation (Option E).

Rationale:

- Public Share security model stays intact (hash-only, once URL, hardened headers).
- Operator friction is the main gap after Visual QA PASS.
- Public surface expansion can wait until handoff copy/readiness prove useful.

---

## 7. Handoff Status / Tracking Decision

| Option | Summary | Recommendation |
|--------|---------|----------------|
| A — No DB status | UI-only readiness; send outside system | **Use for immediate Implementation 01** |
| B — `report_delivery_events` (DB-11) | Durable audit of copy/send events | **Defer** until operator confirms need |
| C — Columns on `report_export_shares` | Mix share lifecycle with delivery events | **Reject** |

**Decision:** No DB tracking in immediate Client Handoff UX Implementation 01. Defer **DB-11 `report_delivery_events`** until operator confirms logged delivery is required.

Phase split:

1. **Handoff UX Charter 01** — this wave (docs only).
2. Optional later: **Handoff UX DB-11 Charter/Apply** if tracking needed.
3. **Handoff UX Implementation 01** — no-migration internal UX + copy pack (+ Visual QA minor label fixes).

---

## 8. Safety Boundary

Must preserve:

- no plaintext token storage;
- no `token_hash` display;
- no raw absolute path in public response;
- no public listing;
- no public landing page in MVP;
- no email sending;
- no client portal;
- no export row mutation / artifact regeneration from handoff UX;
- no legacy/HTML share;
- once-only plaintext URL (no recoverable secret storage);
- existing Public Share hardening/eligibility policies.

Client copy must never include:

- storage paths;
- `token_hash`;
- internal absolute paths;
- admin URLs / credentials.

---

## 9. Next Wave

Recommended next action:

**`I-SEO Report Hub — Report Delivery Client Handoff UX Implementation 01`**

Scope preview:

- copy pack immediately after share creation success;
- handoff readiness panel on export detail / shares page;
- clear once-URL + revoke/recreate guidance;
- unify shareability labels / de-emphasize storage path (Visual QA minors);
- **no** DB migration;
- **no** public route change;
- **no** email / portal.

Only if operator later requires durable “handoff logged”:

**`I-SEO Report Hub — Report Delivery Client Handoff DB-11 Charter 01`**
