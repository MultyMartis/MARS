# I-SEO Report Hub — Local Specialist MVP Acceptance Closeout v0.1

**Date:** 2026-08-27  
**Status:** `LOCAL SPECIALIST MVP ACCEPTED_BY_MARS_REVIEW / OPERATOR_MANUAL_WALKTHROUGH_PENDING`  
**Scope:** local product milestone only — not production acceptance, not SEO-team final sign-off

---

## 1. Status

**Exact status:** `LOCAL SPECIALIST MVP ACCEPTED_BY_MARS_REVIEW / OPERATOR_MANUAL_WALKTHROUGH_PENDING`

This milestone records that:

- **Accepted by MARS/Cursor browser QA** — specialist role exercised locally; routes, forms, content workflow, preview, locks, and access-denied behavior reviewed with screenshots and machine assertions (66/66 PASS in Review Pass 01).
- **Accepted by Web-GPT visual review** — decision after screenshots: `SPECIALIST CONTENT WORKFLOW VISUAL ACCEPTED`; Hybrid MVP flow `work entries → report content workflow → client preview` judged locally assembled and working; UX Polish 02 not urgent.
- **Operator manual walkthrough pending** — product owner (Андрей) has **not** yet personally walked the full specialist path; acceptance so far relies on Web-GPT and MARS/Cursor automation/visual review only.
- **Not production accepted** — host track paused; production config normalization paused; no real client delivery.
- **Not SEO-team accepted** — draft specialist instruction v0.1 exists for future internal review only.

Until the operator completes [I-SEO-REPORT-HUB-OPERATOR-MANUAL-WALKTHROUGH-v0.1.md](../operator-guides/I-SEO-REPORT-HUB-OPERATOR-MANUAL-WALKTHROUGH-v0.1.md), do **not** label this MVP as **operator-confirmed**.

---

## 2. What Works Locally

Verified on local runtime `http://iseo-report-hub.test/` as `seo_specialist`:

| Capability | Local state |
|------------|-------------|
| Login as specialist | Working |
| Dashboard | Working — demo context visible |
| Reporting periods list | Working |
| Monthly report detail | Working — July/August scenarios |
| July finalized read-only | Working — lock notice; no editable textareas/save on content workflow |
| August in-progress editing | Working |
| Work entries list on monthly detail | Working |
| Work entry create | Working — grouped form with field help |
| Work entry edit | Working — e.g. id 28 on August |
| Client preview | Working — client-facing render; content markers visible where saved |
| Specialist content workflow (`/content-workflow`) | Working — six Russian section cards |
| Section editing | Working — per-section save to blocks (Hybrid MVP) |
| Preview reflection | Working — saved section content appears in preview |
| Assembly hints + **Подставить в поле** | Working — client-side fill only in review; no save required for MVP demo |
| Raw block editor route | **Denied** — branded 403 for specialist |
| PDF / export / share | **Parked** — sidebar shows delivery status; no generation in demo |
| Branded 403 access denied | Working — raw technical edit paths blocked |

**Prior checkpoint:** Specialist Content Workflow Review Pass 01 (`SPECIALIST CONTENT WORKFLOW REVIEW PASS`).

---

## 3. Core Routes

Demo user: `seo_specialist` — expectations below assume login as `test@mail.ru` (local demo only).

| Route | Expected for specialist | Meaning |
|-------|-------------------------|---------|
| `/login` | 200 | Login form |
| `/` | 200 | Dashboard — periods/projects context |
| `/reporting-periods` | 200 | List of reporting periods |
| `/monthly-reports/7` | 200 | **July** monthly — status **finalized**; read-only constraints |
| `/monthly-reports/7/preview` | 200 | Client preview for finalized July |
| `/monthly-reports/7/content-workflow` | 200 | Content workflow — **read-only / locked** (finalized) |
| `/monthly-reports/8` | 200 | **August** monthly — status **in_progress**; primary demo month |
| `/monthly-reports/8/work-entries/create` | 200 | Add work entry form |
| `/monthly-report-work-entries/28/edit` | 200 | Edit existing August work entry (demo id) |
| `/monthly-reports/8/content-workflow` | 200 | Six-section report text editor |
| `/monthly-reports/8/preview` | 200 | Client preview for August |
| `/report-blocks/22/edit` | **403** | Raw block edit — **must remain denied** for specialist |

---

## 4. Demo Data

| Item | Value |
|------|-------|
| Demo login | `test@mail.ru` |
| Demo password | local demo only — see operator guide; **not for production** |
| Visible name | `Тест Проверочнов` |
| Role | `seo_specialist` |
| Client / project / site | `ПРОВЕРКА.рф` |
| July monthly report id | **7** — status **finalized** |
| August monthly report id | **8** — status **in_progress** |
| Work entries total | **23** |
| July work entries | **12** |
| August work entries | **11** |
| Snapshots / exports / shares | **0 / 0 / 0** |

**Validation note:** Demo metrics and sample report text are **local/invented fixture content** for workflow demonstration — not verified production SEO metrics.

---

## 5. Known Limitations

1. **Operator has not manually checked** the full specialist path — automation/visual review only.
2. **Host paused** — `https://reports.i-seo.su` not in scope; no deploy/upload this wave.
3. **Production config normalization paused.**
4. **PDF / export / share not implemented** for specialist demo delivery (parked).
5. **Attachments / evidence / external proof links not implemented** — see [I-SEO-REPORT-HUB-REPORT-EVIDENCE-ATTACHMENTS-LINKS-REQUIREMENT-v0.1.md](I-SEO-REPORT-HUB-REPORT-EVIDENCE-ATTACHMENTS-LINKS-REQUIREMENT-v0.1.md).
6. **Admin / lead visual QA** not fully re-run in this milestone.
7. **Real metrics integrity policy** still required before production client reports.
8. **Demo contains invented sample metrics** — must not be shown as real client results.
9. **Test password is demo-only** — must not be reused in production.
10. **Long single-column scroll** on content workflow (P2 residual from review pass) — acceptable for MVP; polish optional later.

---

## 6. Show / Do Not Show Guidance

| Audience | Guidance |
|----------|----------|
| **Operator (Андрей)** | Safe for controlled manual walkthrough on local URL |
| **Internal SEO-team draft review** | Safe **only** with draft instruction v0.1 and explicit “local demo / not production” framing |
| **Real clients** | **Not safe** — no production client reports |
| **Public / host upload** | **Not safe** — host track paused |
| **Final production documentation** | **Not ready** — SEO instruction is draft v0.1 only |

**Do not present** this local MVP as finished product, production-ready hosting, or client-deliverable reporting.

---

## Related documents

- [I-SEO-REPORT-HUB-SPECIALIST-CONTENT-WORKFLOW-REVIEW-PASS-v0.1.md](I-SEO-REPORT-HUB-SPECIALIST-CONTENT-WORKFLOW-REVIEW-PASS-v0.1.md)
- [I-SEO-REPORT-HUB-OPERATOR-MANUAL-WALKTHROUGH-v0.1.md](../operator-guides/I-SEO-REPORT-HUB-OPERATOR-MANUAL-WALKTHROUGH-v0.1.md)
- [I-SEO-REPORT-HUB-SEO-SPECIALIST-DRAFT-INSTRUCTION-v0.1.md](../operator-guides/I-SEO-REPORT-HUB-SEO-SPECIALIST-DRAFT-INSTRUCTION-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-EVIDENCE-ATTACHMENTS-LINKS-REQUIREMENT-v0.1.md](I-SEO-REPORT-HUB-REPORT-EVIDENCE-ATTACHMENTS-LINKS-REQUIREMENT-v0.1.md)
