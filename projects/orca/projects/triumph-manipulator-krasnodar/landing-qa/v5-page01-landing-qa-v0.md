# v5 Page 01 — Landing QA v0

**route_id:** `manipulyator-5-tonn`  
**project_id:** `triumph-manipulator-krasnodar`  
**URL:** `https://manipulator-triumph.ru/5-tonn.html`  
**Date:** 2026-05-21  
**Checker:** Assisted pre-check (repo evidence); **final `approved_for_ads` requires human operator**

**Handoff SoT:** [`triumph-manipulator-v5-page-01-manipulyator-5-tonn-handoff.md`](../../../ppc/triumph-manipulator/handoff/triumph-manipulator-v5-page-01-manipulyator-5-tonn-handoff.md)  
**Build:** [`workspaces/triumph-manipulator-landing-v4/dist/manipulyator-5-tonn/`](../../../../workspaces/triumph-manipulator-landing-v4/dist/manipulyator-5-tonn/)  
**Contract:** [`ppc-landing-qa-contract-v0.md`](../../../intelligence/ppc-landing-qa-contract-v0.md)

---

## QA status

| Field | Value |
|-------|--------|
| **final_status** | `draft` — pending manual browser QA |
| **approved_for_ads** | **no** (pending operator sign-off) |
| **registry_status** | Align to `approved_for_ads` only after human pass |

---

## Checklist (per PPC landing QA contract)

| # | Check | Pre-check (repo) | Manual browser required |
|---|-------|------------------|-------------------------|
| 1 | Search intent continuity | **pass** — handoff locks 5 т / 3 т / 14 м capability intent | confirm hero above fold |
| 2 | Ad headline ↔ hero H1 | **pass** — H1 «Манипулятор 5 тонн в Краснодаре» matches ad H1 in handoff | visual compare to live ad preview |
| 3 | CTA consistency | **pass** — call + form primary per handoff; messengers MAX→TG→WA | tap targets on device |
| 4 | Offer consistency | **pass** — specs locked; no fake hourly hero price | — |
| 5 | Trust consistency | **pass** — Яндекс + Авито only in handoff | verify logos/links live |
| 6 | No fake claims | **pass** — handoff forbids fleet, fake «от X ₽», autopark | scan full scroll |
| 7 | Qualification blocks | **pass** — «что не перевозим», anti-evacuation line in handoff | — |
| 8 | Mobile CTA visibility | **UNKNOWN** | **required** — primary CTA without excessive scroll |
| 9 | Form simplicity | **pass** — handoff: имя + телефон only | submit test / validation UX |
| 10 | Region consistency | **pass** — Краснодар и край in copy | — |
| 11 | Route continuity | **pass** — slug `/manipulyator-5-tonn/` matches registry + export group 01 | live URL 200 |
| 12 | Semantic lock (MODE 1) | **pass** — build follows handoff; no unauthorized positioning drift detected in scope review | operator spot-check copy |

---

## Positioning locks verified (handoff §2)

| Rule | Result |
|------|--------|
| One machine (5 т / 3 т / 14 м) | pass (handoff + partials) |
| No fleet framing | pass (explicit ban in handoff) |
| No fake pricing in hero | pass |
| Price honesty (по задаче) | pass |
| Messenger order MAX → Telegram → WhatsApp | pass (handoff) |

---

## Overflow / layout

| Item | Status |
|------|--------|
| Horizontal overflow mobile | **UNKNOWN** — needs browser QA |
| Section rhythm vs v4 | **pass** (structure reuses v4 partials per handoff map) |

---

## Findings

- **No blocking findings** from static handoff ↔ dist structure review in this initialization pass.
- **Blocking for `approved_for_ads`:** manual browser QA items 8, 11 (live), and operator sign-off.
- **Live deploy:** SAFE UNKNOWN — dist exists in repo; production serve not verified.

---

## Operator actions

1. Open dist or staging URL on mobile + desktop.
2. Complete checks 8, 9, 11 against live environment.
3. Log pass/fail; if pass, set `approved_for_ads` in [`approvals/approval-state-v0.md`](../approvals/approval-state-v0.md) and update registry `status` for `manipulyator-5-tonn`.
4. Do not assign URL in Commander for group 01 until `approved_for_ads` = yes.

---

## Related

- [`landing-route-registry.json`](../landing-route-registry.json) — route `manipulyator-5-tonn`
- [`approval-state-v0.md`](../approvals/approval-state-v0.md)
