# MODERATOR START STALE READ FORENSIC v1

**Phase:** 3G.2.3  
**Actors:** ADMIN_A, MOD_A (labels only)  
**Scope:** Admin.dev `/start` reply-name line vs `/my_reply_profile`  
**No PII / Telegram IDs / raw executions.**

---

## 1. Operator symptom

- `/my_reply_profile` (MOD_A): **Михаил**, enabled, active, receives cards — correct.
- `/start` (MOD_A): `Имя в ответах: не задано` — incorrect in the same contour window.

Authoritative ACCESS_CONTROL storage for MOD_A was already correct (or restored by rehydrate on a prior command). Unified resolver worked on the self-profile path. Start did not.

---

## 2. Live execution proof (sanitized)

| Exec | Command | Actor | Sheet `reply_sender_name` | Auth `access_upsert.reply_sender_name` | Start text | Capture text |
|------|---------|-------|---------------------------|----------------------------------------|------------|--------------|
| **24097** | `/start` | MOD_A | *(blank)* | **Михаил** | `не задано` | `не задано` |
| **24098** | `/start` | MOD_A | **Михаил** | **Михаил** | **Михаил** | **Михаил** |
| **24100** | `/my_reply_profile` | MOD_A | **Михаил** | — | — | **Михаил** |

Source: `start-exec-forensic.sanitized.json` (node names + field presence only).

---

## 3. What Start read

Live Start (pre-3G.2.3) resolved the reply name exclusively from:

```
$('Read ACCESS_CONTROL').all() → row by user_id → reply_sender_name
```

It **did not** read `j.access_upsert` produced by `Check User Authorization` after `rehydrateReplyProfile(...)`.

---

## 4. What Authorization already had

For MOD_A `/start`, Check User Authorization:

1. Normalized the employee row via `rowFromSheet` (profile columns preserved since 3G.2.2).
2. Built `access_upsert = rehydrateReplyProfile(...)` → **Михаил**.
3. Set `access_registry_write=true` for last_seen upsert.

So within **one** execution, post-rehydrate truth existed on `access_upsert` while Start still rendered the pre-rehydrate sheet snapshot.

---

## 5. Why the next command looked fine

Exec 24097 upsert wrote the rehydrated name back to ACCESS_CONTROL. Exec 24098 then read a filled sheet and Start appeared correct — **cross-execution recovery**, not single-execution consistency.

`/my_reply_profile` rehydrates-then-resolves in Reply Profile Commands, so it agreed with storage even when Start had already sent stale text.

---

## 6. Root-cause class

| Hypothesis | Verdict |
|------------|---------|
| Start built before rehydrate | **PASS** — Start runs after Auth rehydrate, but ignores Auth output |
| Start receives old item via another branch | **FAIL** — same Route→Start path; wrong *object*, not wrong branch |
| Upsert result not merged back into Start | **PASS** — Upsert runs *after* Start; Start never saw upsert writeback |
| Resolver output discarded | **PASS for Start** — Start stamped resolver version string but did not call resolve on `access_upsert` |
| Stale `$json` / sheet `$()` reference | **PASS** — `$('Read ACCESS_CONTROL')` is the pre-rehydrate snapshot |
| Name from pre-normalized fields | **PASS** — blank sheet cells, not display_name fallback (fail-closed empty → «не задано») |

---

## 7. Conclusion

**Stale object:** pre-rehydrate `Read ACCESS_CONTROL` row.  
**Authoritative same-execution object:** `access_upsert` (post-rehydrate).  
**Repair:** Start must prefer `access_upsert.reply_sender_name` (unified contract) before any sheet fallback.
