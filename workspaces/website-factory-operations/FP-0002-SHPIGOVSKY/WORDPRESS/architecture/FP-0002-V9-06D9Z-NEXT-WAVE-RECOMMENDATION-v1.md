# FP-0002 V9-06D9-Z — Next Wave Recommendation v1

**Phase:** V9-06D9-Z  
**Date:** 2026-07-06  
**Evidence:** `validation/v9-06d9z-wordpress-readiness-audit/next-wave-recommendation.json`

---

## Recommended next phase

**CREATE_V9_06E0_LEGAL_NATIVE_CONTENT_REVIEW_TASK**

---

## Rationale

### What is ready

- Local runtime environment stable (`shpigovsky` theme, expected plugins, Classic Editor, ACF PRO).
- Key route set (Home, Services hub, service parents/leaf, Contacts, Reviews) returns HTTP 200 without PHP fatals.
- Reviews admin/frontend chain **CLOSED** (D9-Y): OPTIONS source mode; Home + `/otzyvy/` show **Андрей, Москва**; Site Settings duplicate absent.
- Managed template pages (Home, Hub, Contacts, Reviews) have ACF-driven admin UX; native editor hidden where designed (D9-N).
- Content seeds D8-A through D8-E applied for site options, home partials, services MVP, hub, contacts.

### What remains partial or deferred

- **Content/legal:** 10 pages from D9-M deferred set still carry starter placeholder or garbled legal native content.
- **Legal templates:** Pages #22–24 have empty native content post-D9-M; need operator/legal copy decision.
- **Admin evidence:** Authenticated wp-admin screenshots require operator session; functional state confirmed via D9-X/Y + DB.
- **ACF hygiene:** 3 trashed duplicate review field-group DB posts (harmless, optional future cleanup).
- **Production migration:** Explicitly out of scope.

### Why not the alternatives

| Alternative | Rejection |
|-------------|-----------|
| CREATE_V9_06E0_ADMIN_GENERAL_QA_TASK | No new admin defects beyond auth-gated screenshots; Reviews chain closed |
| CREATE_V9_06E0_WORDPRESS_STABLE_CHECKPOINT_TASK | Unresolved legal/native content prevents honest checkpoint |
| OPERATOR_DECISION_REQUIRED | Findings clearly prioritize content/legal review |

---

## Suggested E0 scope (planning hint only)

1. Classify each deferred page: keep native, migrate to ACF, publish/draft, or delete route.
2. Replace garbled privacy policy #3 seed with operator-approved legal text.
3. Populate legal templates #22–24 from authoritative source.
4. Review blog/specialists/genotyping/institutional child pages for MVP vs defer.
5. Re-run read-only route/legal link audit after operator decisions (no auto-mutation without charter).

---

## Verdict

Proceed to **V9-06E0 Legal / Native Content Review** before WordPress stable checkpoint or production migration planning.
