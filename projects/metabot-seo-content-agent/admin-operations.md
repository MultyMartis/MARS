# Admin operations

**Audience:** operators maintaining MetaBOT in n8n + Telegram + Sheets.

---

## Typical duties

- Monitor **`/locks`** and clear stale locks when users report stuck runs — [lock-system.md](lock-system.md).
- Inspect **`seo_active_jobs`** for rows stuck in **pending** after locks released — [known-issues.md](known-issues.md).
- Watch **Google Sheets** quota errors during `/health` — throttle probes or cache reads — [known-issues.md](known-issues.md).
- Verify **Worker** deployment (**v13 stable**) after edits — **SAFE UNKNOWN** promotion process.

---

## Admin commands

**SAFE UNKNOWN:** exact Telegram command list and ACL.

Intended capabilities (documentation level):

- Extended lock management vs user `/locks`.
- Possibly user/task inspection beyond `/get` — **not** confirmed.

---

## What admins should not do in MARS repo

- **Do not** paste production credentials or full workflow JSON into MARS unless governed by a separate release process.
- Prefer **sanitized** maps in [workflow-map.md](workflow-map.md) and this pack.

---

## SAFE UNKNOWN

- Runbooks for partial n8n outage.
- Alerting (PagerDuty, Telegram to ops channel, etc.).

---

*See [admin-workflow.md](admin-workflow.md), [integration-boundary.md](integration-boundary.md).*
