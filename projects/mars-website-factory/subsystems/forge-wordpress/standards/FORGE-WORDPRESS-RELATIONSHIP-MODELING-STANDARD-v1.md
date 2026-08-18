# Forge WordPress — Relationship Modeling Standard v1

**ID:** FW-S-29  
**Status:** ACTIVE — PRODUCTION-INFORMED  
**Date:** 2026-08-18  
**Companion:** [CMS ARCHITECTURE](FORGE-WORDPRESS-CMS-ARCHITECTURE-STANDARD-v1.md)

```text
REFERENCE REAL WORDPRESS OBJECTS.
Generate permalinks at render time.
Do not store staging hostnames as content.
```

---

## 1. Field type selection

| Need | Use | Do not use |
|------|-----|------------|
| One internal target (CTA, “related page”) | **Post Object** (max 1) | URL text for internal pages |
| Many internal targets, order matters | **Relationship** (ordered) | Repeater of URLs |
| Classification shared by many | **Taxonomy** | Repeater of category names |
| WordPress user as author/person | **User** (rare; people as CPT is preferred for public profiles) | Typed name only if no profile object |
| External site | **URL** | Post Object |
| Anchor on same page | text fragment (`#section`) + documented | Full absolute URL |
| `tel:` / `mailto:` | Derived from structured phone/email | Duplicate URL field |
| Opaque identifier | text **only** if no WP object exists | when a CPT exists |

**BAD (AP-CMS-014):** “specialist URL” as a text field.  
**BETTER:** Specialist relationship → `get_permalink( $id )`.

This protects slug changes and domain migrations.

---

## 2. Internal linking standard

For internal editable links prefer, in order:

1. object relationship / Post Object / page selector;  
2. relative or dynamic URL generation in PHP;  
3. free URL only when the target is not a WP object.

**Free URL remains necessary for:** external links; in-page anchors; special protocols; custom JS actions (modal IDs as **controlled selects**, not pasted URLs).

CTA type discriminator: [ACF FIELD MODELING](FORGE-WORDPRESS-ACF-FIELD-MODELING-STANDARD-v1.md) §4.

---

## 3. Domain-independent data

Store:

- post IDs;  
- term IDs;  
- attachment IDs;  
- option keys for globals.

Do **not** store:

- `https://staging.example.test/usluga-x/`;  
- copied HTML snippets with hostnames;  
- manually embedded CDN hosts that duplicate attachment URLs without reason.

Cutover then becomes a bounded `home`/`siteurl` + attachment URL migrate, not a content rewrite of every field.

---

## 4. Query and integrity

| Related object state | Frontend |
|----------------------|----------|
| publish | render |
| draft / pending / future / private | skip unless preview context |
| trash / deleted | skip; no broken card |
| unpublished but required for a sold page | do not ship; editor validation should warn |

Never output a card with an empty `href` or a leftover `#`. If a related list becomes empty, hide the section (empty-state contract).

Filter relationships with the same publish rules as primary queries. Do not assume `get_field('related')` returns only public posts.

---

## 5. Bidirectional relations

If Service ↔ Specialist both need the link:

- pick **one owning side** (usually the more frequently edited);  
- the other side is derived in queries **or** an explicit two-way ACF relationship with a documented owner to prevent drift.

Two independently edited lists that must stay in sync by hand are AP-CMS-004.

---

## 6. Certificates / gallery relations (generic pattern)

If certificates are **owned by one person** and never reused: gallery or repeater of images on the person CPT (parent-owned).  
If certificates are **shared documents** (same file on many people, own titles, expiry): Document CPT + relationship.

Do not copy clinical certificate taxonomies from the reference case.

---

## 7. Manual ordering vs relations

`menu_order` orders a CPT collection. Relationship field order orders a **subset** on a parent. Do not store a duplicate custom `order` meta unless core `menu_order` cannot express the need (document why).

---

*FW-S-29 v1 — objects, not pasted URLs.*
