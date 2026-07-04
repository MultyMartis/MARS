# FP-0002 V9-06D8 Seed Wave Design v1

**Date:** 2026-07-05  
**Evidence:** `validation/v9-06d8-content-seed-planning/seed-wave-design.json`  
**Mode:** Planning only — **no execution in V9-06D8**

---

## Execution order

```text
D8-A → D8-B → D8-C → D8-D → D8-E → D8-G
         (D8-F optional parallel source task)
```

---

## Wave table

| Wave | Purpose | Objects/options | Field scope | Writes later | Risk | Rec. |
|---|---|---|---|---|---:|---:|
| **D8-A** Site Options | Global contact/CTA chrome | `fp02-site-settings` | 15 option fields | options only | LOW | yes |
| **D8-B** Home | Home repeaters MVP | page **4** | advantages, FAQ, gallery, hero | ACF page meta | LOW-MED | yes |
| **D8-C** Services MVP | Programme/stages/FAQ | services **73/74/77/84** | structured + FAQ fields | ACF post meta | MED | yes |
| **D8-D** Services Hub | Hub FAQ/intro | page **5** | intro, FAQ | ACF page meta | LOW | yes |
| **D8-E** Contacts | Messengers/map/blocks | page **20** | contacts_* | ACF page meta | LOW-MED | yes |
| **D8-F** Admin UX Repair | ACF labels/help | source only | ACF JSON | source delivery | MED | optional |
| **D8-G** Post-Seed QA | Route/visual smoke | read-only | — | 0 | NONE | yes |

---

## D8-A — Site Options Seed (recommended first)

**Why first:** D7-F flagged unseeded messenger/site options; header/footer/contacts helpers fall back empty.

**Allowed:** `update_field(..., 'option')` for allowlisted keys only.  
**Forbidden:** pages, services, menus, redirects, rewrite flush, media, object CRUD.  
**Operator gate:** real phone, email, address, hours, messenger URLs required.  
**Checkpoint:** DB snapshot before any write.  
**Success:** Chrome shows contact data; routes still 200.

---

## D8-B — Home Content Seed

**Objects:** page ID 4 only.  
**Priority fields:** `home_advantages`, `home_faq_items`.  
**Optional same wave:** `home_gallery_media`, `home_intro_bands`, hero slide text refresh.  
**Media:** hero/gallery images **excluded** unless separate media authorization.  
**Forbidden:** service writes, options (use D8-A first).

---

## D8-C — Services MVP Content Seed

**Priority object:** service **74** (D7-F regression route).  
**Must write:** `programme_items`, `stages`, `faq_items`.  
**Should write:** `cta_title`, `cta_text`, `cta_button_label`.  
**Do not change:** `service_layout_variant` on 74 (`alcohol_special`).  
**73/77/84:** optional enrichment only.  
**Forbidden:** object create/delete, rewrite flush.

---

## D8-D — Services Hub Content Seed

**Object:** page 5.  
**Fields:** `services_hub_faq_items`; optional intro polish.  
**Do not touch:** `services_hub_query_mode`, `services_hub_show_placeholders` without operator approval.

---

## D8-E — Contacts Content Seed

**Depends on:** D8-A (canonical phone/social).  
**Fields:** `contacts_messengers`, `contacts_blocks`, `contacts_map_url`.  
**Forbidden:** live form endpoint, map API keys.  
**Static OK:** theme map PNG, rehab photo from dist until upload authorized.

---

## D8-F — Admin UX Repair (optional)

Separate **source** task: ACF JSON label/instruction/reorder only.  
Not required before D8-A execution.

---

## D8-G — Post-Seed Runtime QA

Repeat D7-F matrix after approved waves.  
Compare gap classification — EXPECTED gaps should shrink; no new blockers.

---

## Result

**COMPLETE**
