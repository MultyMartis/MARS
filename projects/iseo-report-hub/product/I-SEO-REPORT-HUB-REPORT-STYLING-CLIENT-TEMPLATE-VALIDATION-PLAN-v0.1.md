# I-SEO Report Hub — Report Styling / Client Template Validation Plan v0.1

**Status:** PLANNING ONLY — no execution in charter wave  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Styling / Client Template Charter 01  
**Parent:** [I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-CHARTER-v0.1.md)  
**Implementation plan:** [I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-IMPLEMENTATION-PLAN-v0.1.md)

---

## 1. Purpose

Define validation gates for **future** `Report Styling Default Template Implementation 01` (and any related repair/regeneration). This charter wave itself performs **no** styling validation beyond read-only baseline confirmation.

---

## 2. Baseline validation (before implementation edits)

| Check | Expected |
|-------|----------|
| Branch | `mars/canonical-post-recovery` |
| Volume | `AI WS` on `X:` |
| DB | `iseo_report_hub_dev` @ `127.0.0.1` |
| migrations / tables | **7** / **15** |
| report_exports | **2** (html id **1**, pdf id **2**) |
| HTML checksum | `c194c62b81c6ec04a52a651a24263e54e33d9cac2aa0453f3a95214b626fadc4` |
| PDF checksum | `707e72d65f253de17070980e2be36b91f59c4e6faf4352e73d3b1849880d0320` |
| Snapshot | id **1** active; checksum `0d0c863c5c283edf508aa2fb52a96acb57c6b358e0f45ac7582c970a03997a38` |
| Outside public/Git | both artifacts |

Capture mtimes/checksums before any write.

---

## 3. Template metadata validation

For any **new** styled HTML output:

| Check | Pass criteria |
|-------|---------------|
| `template_id` present | equals `iseo_default_v1` |
| `template_version` present | equals `1` (or documented bump) |
| Location | HTML comment and/or meta; optional footer |
| Determinism | same inputs → same ids in output |

If DB-09 not present: absence of DB columns is OK; HTML metadata required.

---

## 4. HTML output validation

| Check | Pass criteria |
|-------|---------------|
| Charset | UTF-8 |
| Lang | `ru` (or documented) |
| Escaping | no raw unescaped user/snapshot HTML injection |
| Structure | H1 once; sections/blocks ordered as design |
| Embedded CSS | present; includes print/@page rules |
| No JS | no `<script>` |
| No external assets | no remote CSS/font/img URLs |
| Snapshot-only | content from snapshot payload, not live mutable blocks |

---

## 5. PDF output validation

When PDF generated from styled HTML:

| Check | Pass criteria |
|-------|---------------|
| Engine | Edge (or documented allowlisted fallback) |
| Magic | starts with `%PDF` |
| Size | > 0; recorded if persisted |
| Hardening | `validateReadyArtifact` PASS if registered |
| Source link | PDF tied to HTML export id when persisted |
| Idempotency | second create does not rewrite ready file |

---

## 6. Visual sanity checks

Operator/agent spot-check:

- header brand text visible;
- title/meta readable;
- blocks separated;
- no dashboard card clutter;
- light theme;
- no obvious overflow at ~A4 width.

---

## 7. Cyrillic / font checks

| Check | Pass criteria |
|-------|---------------|
| Sample Russian text | readable in HTML open |
| PDF sample | readable Cyrillic (no tofu boxes for body) |
| Font stack | local/system only; no CDN |

---

## 8. A4 / print checks

| Check | Pass criteria |
|-------|---------------|
| `@page` | size A4; margins set |
| `@media print` | present or equivalent print rules |
| Breaks | blocks not catastrophically split (best-effort Edge) |
| Margins | content not clipped at edges in spot-check |

---

## 9. No external assets / JS

Automated greps on generated HTML:

- no `https://` / `http://` in `link`/`script`/`src`/`href` for assets (allow `mailto:` if ever present — not expected);
- no `<script`;
- no `@import` remote.

---

## 10. No old artifact mutation

| Check | Pass criteria |
|-------|---------------|
| HTML id 1 checksum | unchanged vs baseline unless repair charter |
| PDF id 2 checksum | unchanged vs baseline unless repair charter |
| report_exports count | unchanged unless new version explicitly allowed |
| Snapshot checksum | unchanged |
| monthly/blocks/periods/weekly | unchanged |

---

## 11. Checksum / idempotency regression

| Check | Pass criteria |
|-------|---------------|
| Idempotent HTML POST | returns existing id; no rewrite |
| Idempotent PDF POST | returns existing id; `rewritten=false` behavior retained |
| Download | auth + safe headers + checksum match |
| Failure-mode subset | path/MIME/magic rejects still PASS |

---

## 12. No public route

| Check | Pass criteria |
|-------|---------------|
| Public share | still absent (404 / no route) |
| Download | auth-only |
| client_viewer | create/list denied as today |

---

## 13. STOP conditions

STOP validation / implementation if:

- baseline checksums already drifted unexpectedly;
- old artifacts would be overwritten to “prove” styling;
- external network assets appear;
- DB mutated without charter;
- hardening suite regresses;
- Cyrillic illegible in PDF;
- cannot keep docs/code scope within allowlist.

---

## 14. Charter-wave validation (this task)

For Report Styling / Client Template Charter 01 itself:

| Check | Expected |
|-------|----------|
| Docs-only paths committed | allowlisted product + report + OPERATIONAL-INDEX |
| No app-source / runtime / DB / artifact changes | **yes** |
| Push | **no** |
