# I-SEO Report Hub — Report Delivery Client Handoff UX Design v0.1

**Status:** DESIGN / POLICY ONLY — no implementation in this wave  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-28  
**Authority:** Operator I-SEO Report Hub Report Delivery Client Handoff UX Charter 01  
**Related:**
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-CHARTER-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-COPY-PACK-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-COPY-PACK-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-IMPLEMENTATION-PLAN-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-VALIDATION-PLAN-v0.1.md)

---

## 1. Purpose

Описать operator/client handoff UX поверх существующего Public Share MVP: journey, readiness, once-URL, copy UI, revoke/recreate, Visual QA minors — **без** public landing page в MVP.

---

## 2. User journey (operator)

```
finalized monthly report
        │
        ▼
 active report snapshot
        │
        ▼
 styled PDF export ready (template metadata present)
        │
        ▼
 open export detail / shares (handoff panel)
        │
        ├─ if no active share ──► create share
        │                              │
        │                              ▼
        │                     once-URL + copy pack
        │                     (copy short / email / note)
        │                              │
        │                              ▼
        │                     send outside system
        │                     (Telegram / email / messenger)
        │
        └─ if active share exists ──► show status / expiry
                                      (no recoverable URL)
                                      warn: copy was only at create
                                      if URL lost → revoke + recreate
```

Client journey (MVP):

```
receive message with share URL
        │
        ▼
 GET /share/report/{token}
        │
        ▼
 direct PDF download stream
 (no cover page / no portal)
```

---

## 3. Readiness checklist

Handoff-ready requires all of:

| Check | Rule |
|-------|------|
| Monthly status | finalized |
| Snapshot | active snapshot exists |
| Export | styled PDF; status ready; format `pdf` |
| Template metadata | e.g. `iseo_default_v1` v1; `render_target = pdf_export` |
| Share | active, non-expired, policy OK |
| Artifact | checksum validates |
| UI clarity | client/project/period; export id/key; share id/status; expiry visible |
| Secrets | no `token_hash` shown; storage path not in client copy |

Warnings (block or strong warn):

- do not send revoked / expired link;
- do not send legacy export (metadata NULL);
- do not send HTML export;
- do not invent/recover URL from DB.

---

## 4. Share creation success state

Primary MVP surface for copy pack.

On successful create:

1. Show plaintext public URL **once** (existing once-box).
2. Show expiry timestamp.
3. Show copy actions:
   - Copy URL;
   - Copy short message;
   - Copy formal email (subject + body);
   - Copy internal note (operator only).
4. Explicit notice: URL cannot be shown again after leaving this screen.
5. If operator did not copy: revoke + create new share.

Do not show:

- `token_hash`;
- storage path in client templates;
- absolute filesystem paths.

---

## 5. Copy message UI

| Control | Behavior |
|---------|----------|
| Tabs or stacked blocks | Short / Email / Internal note |
| Placeholders filled from DB context | client, project, period, share URL (once), expires_at, specialist name if available |
| Copy button | Copies rendered text to clipboard |
| Disabled states | If share revoked/expired/missing once URL → disable client templates that need `{share_url}` |

Full templates: [COPY-PACK](I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-COPY-PACK-v0.1.md).

---

## 6. Expired / revoked / no-active states

| State | Operator UX |
|-------|-------------|
| No active share | Readiness incomplete; CTA “Create share for handoff” |
| Active + once just created | Full copy pack available |
| Active + revisit (once gone) | Status/expiry visible; message: URL not recoverable; offer revoke+recreate |
| Revoked | Badge revoked; no client send CTA; recreate allowed |
| Expired | Treat as not sendable; recreate required |
| Not shareable export | Show unified **Not shareable** + reason; no create CTA |

---

## 7. No URL recovery rule

Current model stores **token_hash only**. After once display, public URL **cannot** be reconstructed from DB.

MVP policy:

- Do **not** store recoverable/encrypted plaintext token.
- Handoff panel must state clearly that the public URL is shown only when a share is created.
- Lost URL → **revoke old share and create a new one** (preferred path).

---

## 8. Revoke and recreate path

1. Operator opens shares for eligible export.
2. Revokes active share (if any).
3. Creates new share.
4. Immediately uses copy pack on success screen.
5. Sends new message to client; previous URL becomes **410**.

This is the supported recovery path for lost URLs.

---

## 9. UX surfaces

| Surface | MVP role |
|---------|----------|
| Export detail / shares page | **Primary** handoff panel |
| Share creation success | **Primary** copy pack |
| Monthly report detail | Optional later summary link to handoff |
| Snapshot detail | Optional later summary link |
| Public token route | **Unchanged** direct PDF stream |

No public landing page in MVP.

---

## 10. Visual QA minor issues integration

| ID | Design handling |
|----|-----------------|
| `UI-REL-STORAGE-PATH` | De-emphasize: move under technical details disclosure; label “internal artifact path”; never include in client copy |
| `UI-LIST-SHARE-LABEL` | Unify list badge to **Not shareable** (match detail); optional reason tooltip |

Recommended: include both in **Client Handoff UX Implementation 01** (no migration needed). They are not blockers for charter; they should be fixed before or with handoff UI polish so operators do not confuse shareability.

---

## 11. Out of MVP (design deferrals)

- Public lightweight landing page;
- Client portal;
- Email send automation;
- DB-backed delivery event log (until DB-11 confirmed);
- Recoverable token storage;
- Changing public route from PDF stream to HTML cover.
