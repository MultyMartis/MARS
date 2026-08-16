# PROD-P07-FU01-CONT2 — Drift gate

**Verdict:** `MATCH` — production-before is still accepted P07; local canonical is ahead only by approved FU01 residual cleanup. No new operator production edits.

| File | Production-before SHA-256 | vs accepted P07 | vs FU01 local |
|------|---------------------------|-----------------|---------------|
| `inc/v9-static-content.php` | `5ee639d1…d158026` | **EQ P07** (`prod_after` 09:50 UTC) | DRIFT (local `3471898f…e55604`) |
| `inc/service-general-helpers.php` | `163f7d2d…819f89ee` | **EQ P07** | DRIFT (local `b4ac89d7…8eb74293`) |
| `inc/services-hub-helpers.php` | `ff4024d0…887c5d0b` | not in P07 upload allowlist | DRIFT (local `6e11bbc4…91e305`) |

Diff scope (Layer B → local):

* hub placeholder suppression (empty V9 Lorem/DEMO card texts; DEMO fallback returns `''`; ACF/V9 placeholder omit);
* slug aliases `emotsionalnoe-vygoranie` / `buliniya`;
* alcohol signs editorial omit;
* alcohol FAQ technical V9 fallback → `[]`; ACF placeholder-answer skip;
* alcohol program ACF Lorem omit; existing `$use_emergency` gate retained.

No unrelated refactor. No ambiguous operator conflict. **No canonize-from-production required.**

Diffs: `cont2-drift-*.diff`
