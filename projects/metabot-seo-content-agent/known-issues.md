# Known issues — MetaBOT SEO Content Agent

Grouped per user briefing. **Status** reflects operations narrative, not automated tests in this repo.

---

## Runtime issues

| Issue | Notes |
|-------|--------|
| **`/get task_id` sometimes does not respond** | Intermittent; causes **SAFE UNKNOWN** (timeout, Sheets, lock, Telegram API). |
| **`/run` lock vs `seo_active_jobs`** | Lock may **close** while job row stays **pending** — treat tables as potentially **out of sync**. |

---

## Quality issues

| Issue | Notes |
|-------|--------|
| **Strict layer still improving** | Undesired phrases may appear: *order now*, *professional*, *improvement*, *helps*, *affects*, *visibility*. |
| **Cleanup rewrite ≠ full QA** | Editorial pass helps; **canonical strict** remains `/seoqa --strict` / `/factcheck --strict` with `from:task_id`. |

---

## Infrastructure issues

| Issue | Notes |
|-------|--------|
| **`/health` vs Google Sheets** | May hit rate limits: *“The service is receiving too many requests from you”*. |
| **Sheets as state store** | No transactions; races possible under concurrency — see [storage-layer.md](storage-layer.md). |

---

## UX issues

| Issue | Notes |
|-------|--------|
| **`/get` silence** | User perception: “bot ignored me” — see runtime issues. |
| **Strict inheritance** | Users might assume `/run` implies strict QA — **not** current requirement; document clearly — [seoqa-and-factcheck.md](seoqa-and-factcheck.md). |

---

## SAFE UNKNOWN

- Frequency metrics for each issue.
- Whether fixes are deployed uniformly across Intake/Worker/Admin.

---

*See [roadmap.md](roadmap.md).*
