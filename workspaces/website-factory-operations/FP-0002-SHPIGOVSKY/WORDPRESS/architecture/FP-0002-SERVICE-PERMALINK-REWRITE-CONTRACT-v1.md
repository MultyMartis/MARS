# FP-0002 Service Permalink and Rewrite Contract v1

**Task:** V9-06A.1 | **Date:** 2026-07-03  
**Status:** ACTIVE — depth-2 full-path mapping applied (REWRITE-RULE-REPAIR 2026-07-04)

---

## 1. Public URL model

**Pattern:**

```text
/uslugi/{service-path}/
```

Where `{service-path}` is the full ancestor slug chain from the top-level service segment:

| Depth | Pattern | Example |
|------:|---------|---------|
| 1 | `/uslugi/{parent-slug}/` | `/uslugi/zavisimosti/` |
| 2 | `/uslugi/{parent-slug}/{child-slug}/` | `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` |

**Maximum supported depth:** 2 (parent subdivision + leaf). No depth-3 services in V9 authority.

**Trailing slash:** Required on public canonical URLs (matches V9 static output and WordPress `/%postname%/` trailing-slash convention).

**Hub route (separate):** `/uslugi/` — owned by native Page, not CPT archive.

---

## 2. Ownership boundary: Page vs CPT

| Surface | Entity | Route | Mechanism |
|---------|--------|-------|-----------|
| Services hub | Native Page (`slug=uslugi`) | `/uslugi/` | Page permalink; template `page-templates/services-hub.php` |
| Service detail | `service` CPT | `/uslugi/{path}/` | CPT rewrite + link filter (see §4) |
| CPT archive | **disabled** | — | `has_archive => false` |

**Invariant:** The `service` CPT must **not** register a public archive competing for `/uslugi/`.

---

## 3. CPT registration parameters (recommended)

```php
register_post_type('service', [
    'public'             => true,
    'publicly_queryable' => true,
    'hierarchical'       => true,
    'has_archive'        => false,
    'rewrite'            => [
        'slug'         => 'uslugi',
        'with_front'   => false,
        'hierarchical' => true,
        'pages'        => true,
    ],
    'query_var'          => true, // default 'service' or explicit 'service'
    'supports'           => ['title', 'editor', 'excerpt', 'thumbnail', 'revisions', 'page-attributes'],
]);
```

**Registration owner:** `shpigovsky-core` (`src/ContentTypes/Service.php`).

---

## 4. Implementation approach

**Selected model:** `CPT_REWRITE_PLUS_POST_TYPE_LINK_FILTER`

**Rationale:**

| Approach | Verdict |
|----------|---------|
| `NATIVE_CPT_REWRITE` alone | **Insufficient** — hierarchical CPT rewrite with slug `uslugi` conflicts with existing Page slug `uslugi`; native `%postname%` for hierarchical CPT does not reliably produce full nested paths under a shared prefix without filters |
| `CPT_REWRITE_PLUS_POST_TYPE_LINK_FILTER` | **Selected** — smallest robust model |
| `CUSTOM_REWRITE_RULES` | Supplement only if filter + native rules fail depth-2 resolution in V9-06C smoke tests |
| `CUSTOM_QUERY_VAR_ROUTER` | **Rejected** — broad custom router unnecessary if WordPress query resolves via standard rewrite + `post_type=service` |

### 4.1 Permalink generation (`post_type_link` filter)

**Owner:** `shpigovsky-core` — hook `post_type_link` for `service`.

**Algorithm:**

1. Load service post and `post_name` (leaf slug).
2. Walk `post_parent` chain collecting ancestor slugs up to root (`post_parent = 0`).
3. Reverse chain to root→leaf order.
4. Build: `home_url('/uslugi/' . implode('/', $slugs) . '/')`.
5. Never emit bare `/uslugi/{leaf-only}/` for depth-2 services.

### 4.2 Rewrite rule registration

**Owner:** `shpigovsky-core` — `init` priority after CPT registration.

1. Rely on WordPress generated rewrite rules from CPT registration with `hierarchical => true`.
2. Add explicit top-priority rules if smoke tests show Page/CPT ambiguity:

```text
^uslugi/([^/]+)/([^/]+)/?$  →  index.php?post_type=service&service=$matches[1]/$matches[2]
^uslugi/([^/]+)/?$          →  index.php?post_type=service&service=$matches[1]
```

**Depth-2 query var:** full parent/child path (`$matches[1]/$matches[2]`), not leaf-only `$matches[2]`. Hierarchical CPT resolution via `get_page_by_path` requires the full path under the CPT base (e.g. `zavisimosti/lechenie-alkogolnoy-zavisimosti` for Service 74). Leaf-only mapping is a `POST_TYPE_LINK_REWRITE_MISMATCH` and yields HTTP 404 for depth-2 services.

**Repair note (2026-07-04):** Corrected in `ServicePermalinks::register_rewrite_rules` (REWRITE-RULE-REPAIR micro-task). Soft rewrite flush required after runtime delivery.

3. **Page `/uslugi/` exact match** must resolve to Page before CPT rules — WordPress Page rules typically take precedence for exact slug; validate in V9-06C.

### 4.3 Request resolution

- Query var: `service` (pagename-style) + `post_type=service`.
- `pre_get_posts` or `request` filter: only if native resolution fails for depth-2 paths.
- Template: `single-service.php` via standard template hierarchy.

### 4.4 Canonical redirect behavior

| Case | Behavior |
|------|----------|
| Missing trailing slash | 301 to slash-terminated URL |
| Non-canonical path (wrong parent chain) | 301 to `post_type_link` output |
| Draft / private | Standard WordPress auth gate; no public canonical |
| Preview | Standard `?preview=true` + nonce; permalink filter applies to preview link |

**Owner:** Theme canonical helper + WordPress `redirect_canonical`; plugin supplies correct permalink via filter.

---

## 5. Slug and collision handling

| Rule | Policy |
|------|--------|
| Sibling slug uniqueness | Required under same `post_parent`; enforced at save |
| Duplicate slug under different parents | **Allowed** — e.g. `specialistam` under `zavisimosti` vs future elsewhere; full path disambiguates |
| Page slug `uslugi` vs CPT base | Page owns exact `/uslugi/`; CPT owns `/uslugi/*` subpaths only |
| Reserved slugs | Block creation of service with slug matching hub Page slug at root |
| Parent reassignment | Regenerate permalink via filter; old URL 301 if published URL changed; log in migration map |
| `genotipirovanie` | Must not exist as Service; foundation Page retired — no canonical replacement |

**Save validation owner:** ACF + `shpigovsky-core` `save_post_service` hook (server-side sibling slug check).

---

## 6. Migration and redirect preservation

| Scenario | Action |
|----------|--------|
| Page→Service migration (3 subdivisions) | CREATE new service → validate URL → switch menu refs → 301 old Page URL if ID/slug drift → retire Page |
| New leaf creates | Direct CPT create; no Page predecessor |
| Old `/specyalisty/` | **Separate** — 301 to `/uslugi/zavisimosti/specialistam/` after canonical target ready (OD-002) |
| `/uslugi/genotipirovanie/` | RETIRE — 410 or remove; no canonical V9 route |
| Foundation Page URLs after migration | 301 to equivalent Service URL if slug preserved |

See [FP-0002-PAGE-TO-SERVICE-MIGRATION-CONTRACT-v1.md](FP-0002-PAGE-TO-SERVICE-MIGRATION-CONTRACT-v1.md).

---

## 7. Rewrite flush policy

| Event | Action |
|-------|--------|
| CPT registration change | Flush rewrite rules once on plugin activation |
| Migration batch complete | Flush after all services created + validated |
| Routine deploy | Do not flush on every request |
| Rollback | Restore rewrite snapshot from pre-migration baseline; flush |

**Owner:** `shpigovsky-core` activation hook + documented migration checklist.

---

## 8. Draft and preview behavior

- **Draft:** No public URL; admin preview uses standard WordPress preview mechanism.
- **Published:** Permalink filter active; canonical enforced.
- **Placeholder services:** Published with placeholder template variant; URL live per V9 static parity.

---

## 9. Test matrix reference

Full cases: [FP-0002-SERVICE-PERMALINK-TEST-MATRIX-v1.json](FP-0002-SERVICE-PERMALINK-TEST-MATRIX-v1.json).

**Smoke tests required in V9-06C (not this task):**

1. `/uslugi/` → Page 200, not CPT archive.
2. Each of 15 service URLs → 200, correct template.
3. Depth-2 URL resolves correct child under correct parent.
4. Trailing slash redirect.
5. Unknown path → 404.
6. Page/CPT slug collision rejected at save.

---

## 10. Contract result

```text
Pattern:           /uslugi/{service-path}/
Hierarchy:         depth 1–2 via post_parent
Implementation:    CPT_REWRITE_PLUS_POST_TYPE_LINK_FILTER
has_archive:       false
Page/CPT conflict: Page owns /uslugi/; CPT owns subpaths
Status:            DEFINED
```

---

*Planning authority — no runtime mutations in V9-06A.1.*
