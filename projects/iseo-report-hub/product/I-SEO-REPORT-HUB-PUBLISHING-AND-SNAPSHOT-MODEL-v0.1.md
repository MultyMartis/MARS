# I-SEO Report Hub — Publishing and Snapshot Model v0.1

**Status:** PLANNING — product architecture Layer 02 companion  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-24  
**Implementation:** **NOT STARTED**

---

## 1. Purpose of Published Snapshot

A **published snapshot** is a frozen, client-safe representation of an approved monthly report used for client web delivery.

It exists so that:

- clients see a stable document;
- specialists can continue editing drafts without changing what the client already received;
- audit can prove **what was shown** and **when**;
- revoke/supersede is possible without deleting history.

---

## 2. Why Client Report Must Not Be Live Draft

| Risk if client URL points at live draft | Consequence |
|-----------------------------------------|-------------|
| Incomplete blocks appear mid-edit | Trust damage |
| Internal notes leak | Confidentiality failure |
| Reviewer comments visible | Process leakage |
| Accidental publish of WIP metrics | Business risk |
| No version identity | “Which report did they see?” unknown |

**Rule:** Client-facing URL resolves to **published snapshot only**, never to editable draft tables.

---

## 3. Snapshot vs Draft

| Aspect | Draft / working report | Published snapshot |
|--------|------------------------|--------------------|
| Mutability | Editable by specialist | Immutable or soft-immutable |
| Audience | Internal | Client (+ internal viewers) |
| Includes internal notes | Yes | No |
| Includes reviewer comments | Yes | No |
| Access | Auth workspace | Controlled client access |
| Identity | `monthly_report_id` | `snapshot_id` + version |

---

## 4. Client URL Model Options

### Option 1 — Unlisted token URL

Opaque path/token (e.g. `/report/{token}`) mapped to a live snapshot.

| Pros | Cons |
|------|------|
| Simple MVP | Link forwarding = access |
| No client login | Token leak risk |

### Option 2 — Password-protected URL

Token URL plus shared password.

| Pros | Cons |
|------|------|
| Extra barrier | Password sharing friction |
| Still no portal | Password rotation ops |

### Option 3 — Client login portal

Authenticated client accounts.

| Pros | Cons |
|------|------|
| Stronger identity | Out of MVP scope |
| Multi-report history UX | Auth/product cost |

---

## 5. Recommended MVP Access Model

**Primary recommendation for MVP:** **unlisted token URL** (Option 1), with:

- non-guessable tokens;
- revoke/unpublish support;
- no sequential public IDs as canonical delivery;
- optional later upgrade to password (Option 2) if operator requires.

**Not MVP:** Option 3 client login portal.

Exact token entropy, TTL, and HTTPS-only rules: security gate later — **SAFE UNKNOWN** details.

---

## 6. Snapshot Immutability Levels

| Level | Behavior |
|-------|----------|
| **Soft immutable** | Snapshot content not edited in place; Admin may patch with audit (discouraged) |
| **Strict immutable** | No in-place edits; only new version or revoke |
| **Superseded snapshots** | Previous live snapshot remains readable as history or becomes unavailable per policy; new version becomes live |

**MVP recommendation:** treat as **strict immutable** for content; allow **supersede** by publishing a new version; allow **revoke**. Soft immutable only as emergency Admin escape with mandatory audit.

---

## 7. What Is Included in Snapshot

- Client-visible meta (client, project/site, period)
- Approved client-facing blocks and values
- Client-visible work items (dictionary wording)
- Client-visible KPI values and short interpretations
- Approved client-visible evidence links/files
- Topvisor (or other) external report link if approved
- Publish timestamp and version label

---

## 8. What Is Excluded

- Internal notes
- Reviewer comments
- Raw source data dumps / import payloads
- Secrets and credentials
- Non-approved evidence
- Blocks marked `hidden_internal`
- Specialist-only readiness checklists
- Draft/incomplete block contents

---

## 9. Version History

| Concept | Rule |
|---------|------|
| Version number | Monotonic per monthly report (v1, v2, …) |
| Live pointer | At most one `live` snapshot per period (typical) |
| History | Superseded versions retained for audit |
| Client default | Latest live version |
| Deep link to old version | Optional; policy TBD |

---

## 10. Unpublish / Revoke

| Action | Effect |
|--------|--------|
| Unpublish / revoke | Client URL returns safe “unavailable” |
| Workspace | Period/report may return to `approved` or stay published-with-revoked flag |
| Audit | Actor, time, reason recorded |
| Re-publish | Creates new snapshot or restores prior — policy TBD; prefer new version |

---

## 11. Audit Trail

Record at minimum:

- who published;
- when;
- snapshot version id;
- token issued / rotated / revoked;
- who unpublish/superseded;
- optional “sent to client” flag by Account Manager.

---

## 12. SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Token TTL / expiry | **UNKNOWN** |
| Whether superseded versions remain client-reachable | **UNKNOWN** |
| Password option required day one | **UNKNOWN** — default no |
| Hosting path (`i-seo.su` vs subdomain) | **UNKNOWN** — platform-dependent |

---

## Document control

- **Created:** 2026-07-24  
- **Does not claim:** renderer or URL delivery exists  
- **Upstream:** Web Report Structure v0.1 URL strategy
