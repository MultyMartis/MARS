# START EXECUTION ORDER v1

**Phase:** 3G.2.3  
**Workflow:** Admin.dev `wLrLp4WQHm1VJmxz` (85 nodes)  
**Command:** recognized moderator `/start`

---

## Proven order (live exec 24097 / 24098)

1. **Telegram Trigger** (ingress)
2. **Normalize Command** → `/start`
3. **Read Authorization Config** → **Collapse Authorization Context**
4. **Read ACCESS_CONTROL** (authoritative sheet snapshot — may be blank for profile columns)
5. **Check User Authorization**
   - `rowFromSheet` normalization (includes reply-profile fields)
   - anti-wipe / **rehydrate** decision → `access_upsert.reply_sender_name=Михаил` when seed matches
   - last_seen fields merged into `access_upsert`
6. **IF Authorized** → **Route Command** → **Start**
7. **Start Reply builder** *(defect pre-3G.2.3: read sheet; repair: read `access_upsert`)*
8. **IF Access Registry Write** → **Prepare Access Upsert** → **Upsert ACCESS_CONTROL**
9. **Restore Admin Reply Target** → **Capture Admin Reply** → **Safe Telegram Reply** / Telegram Send

---

## Object Start must consume (post-repair)

| Priority | Object | When |
|----------|--------|------|
| 1 | `j.access_upsert` | Present after Auth rehydrate (admin/moderator `/start`) |
| 2 | `Read ACCESS_CONTROL` row | Fallback only if upsert name empty |
| — | display_name / username | **Forbidden** |

Unified contract version stamped on Start output: `iseo-reply-profile-resolver-v1.0`.

---

## Alternative safe order (acceptable)

Any order is acceptable **if and only if** the Telegram reply text is built from the post-rehydrate resolved profile within the same execution (no dependency on the next command).
