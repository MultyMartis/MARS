# I-SEO Report Hub — Report Delivery Client Handoff UX Implementation Plan v0.1

**Status:** IMPLEMENTATION PLAN / POLICY ONLY — no code in this wave  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-28  
**Authority:** Operator I-SEO Report Hub Report Delivery Client Handoff UX Charter 01  
**Related:**
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-CHARTER-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-DESIGN-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-DESIGN-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-COPY-PACK-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-COPY-PACK-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-VALIDATION-PLAN-v0.1.md)

---

## 1. Recommended next wave

**`I-SEO Report Hub — Report Delivery Client Handoff UX Implementation 01`**

Goal: internal handoff panel + copy pack on existing Public Share MVP.  
No DB migration. No public route change. No email. No portal.

---

## 2. Source areas (expected touchpoints)

Model A — edit `projects/iseo-report-hub/app-source/` then sync to Localhost runtime under separate sync charter if required by implementation wave.

Likely areas (exact files decided in implementation charter):

| Area | Role |
|------|------|
| `app/Views/pages/report-exports/show.php` | Export detail + readiness summary |
| `app/Views/pages/report-export-shares/index.php` (or create-success partial) | Shares list + once success + copy pack |
| `public/assets/css/app.css` | Handoff panel / disclosure / badge styles |
| `public/assets/js/app.js` | Clipboard copy helpers if needed |
| Controllers / services for shares | Pass context fields for templates (no token reconstruction) |
| Optional helper for copy rendering | Server-side fill of placeholders |

Do **not** change:

- public share stream controller behavior (still PDF attachment stream);
- token generation/storage model;
- migrations / schema;
- artifact generation paths.

---

## 3. UI changes

1. **Handoff readiness panel** on export detail / shares page:
   - client / project / period;
   - export id / key / format / template metadata;
   - share status / expiry / access policy summary;
   - pass/fail checklist items;
   - warnings for not-shareable / revoked / expired / once-gone.
2. **Share create success**:
   - existing once URL box;
   - short / email / internal copy blocks + copy buttons;
   - once-only notice.
3. **Revisit active share without once URL**:
   - status only;
   - revoke + recreate CTA;
   - disable client templates requiring `{share_url}`.
4. **Visual QA minors**:
   - unify list badge to `Not shareable`;
   - move relative storage path under technical details; never into copy pack.

---

## 4. Copy pack integration

- Bind templates from Copy Pack v0.1.
- Fill placeholders from authenticated context.
- `{share_url}` only when once plaintext is in current response/session flash.
- Do not write plaintext token or rendered client message with token into DB.

---

## 5. No DB migration path (default)

Implementation 01 proceeds **without** DB-11:

- no `report_delivery_events`;
- no new columns on `report_export_shares`;
- handoff “sent” remains operator-external (manual).

This matches Charter tracking decision.

---

## 6. Optional DB-11 deferred path

Only if operator later requires durable audit:

1. Separate charter: Client Handoff DB-11.
2. Design `report_delivery_events` (export/share, channel, copied_at/sent_at, created_by, note).
3. Apply migration under controlled apply wave.
4. Then wire optional “log handoff” UI.

Do **not** mix DB-11 into Implementation 01 unless operator re-charters.

---

## 7. Validation / smoke

Follow Validation Plan v0.1. Minimum expectations for Implementation 01:

- readiness panel renders for shareable and not-shareable exports;
- once URL + copy pack on create;
- revisit cannot recover URL;
- revoke/recreate path works;
- public stream still PDF + hardened headers;
- no `token_hash` / absolute path leaks;
- labels unified; storage path de-emphasized;
- DB counts unchanged except intentional share create/revoke during smoke (then leave active **0** unless charter says otherwise);
- no package install; no portal/email.

---

## 8. STOP conditions

STOP Implementation 01 if:

- charter requires public landing / portal / email and scope drifts;
- recoverable token storage is proposed;
- DB migration is introduced without DB-11 charter;
- plaintext token would be stored or re-displayed from DB;
- foreign WIP / wrong branch / volume mismatch;
- app-source edits would break Public Share hardening contracts;
- live tokens would be committed to docs/evidence without redaction.
