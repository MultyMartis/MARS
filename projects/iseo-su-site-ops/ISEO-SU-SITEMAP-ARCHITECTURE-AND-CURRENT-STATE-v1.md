# ISEO-SU SITEMAP ARCHITECTURE AND CURRENT STATE v1

**Programme:** ISEO-SU-SITE-OPS  
**Updated:** 2026-08-24  
**Status:** CURRENT / SPECIALIZED / DOCUMENTATION ONLY  
**Implementation state:** OPEN — target architecture is not deployed

## 1. Current Status

The production sitemap architecture currently has two working surfaces and one defective root entry point. Latest accepted evidence is the read-only technical/SEO audit dated 2026-08-21; this document does not claim a new production probe or mutation.

| Surface | Current accepted state |
|---|---|
| `/sitemap-static.xml` | working |
| `/wp-sitemap.xml` | working WordPress sitemap index |
| `/sitemap.xml` | responds, but advertises three obsolete children observed 404 |
| Target root index | planned, **not implemented** |

## 2. Working Sitemap Surfaces

### `/sitemap-static.xml`

Physical/static marketing URL inventory. It is a working sitemap surface and must remain synchronized with intended indexable static pages.

### `/wp-sitemap.xml`

WordPress core sitemap index. It owns WordPress pages/posts/CPT/taxonomy surfaces, including the public glossary set. Accepted glossary evidence records 184 glossary term URLs in the WordPress sitemap family.

The coexistence of static and WordPress sitemap ownership is `EXPECTED`; it is not itself a defect.

## 3. Current Root Sitemap Problem

`/sitemap.xml` currently advertises:

- `/sitemap-static.xml` — working;
- `/post-sitemap.xml` — observed 404;
- `/page-sitemap.xml` — observed 404;
- `/category-sitemap.xml` — observed 404.

Finding `SM-CHILD-404` is **HIGH / OPEN_TECH**, owner **MARS / SITE OPS**. It is incorrect to describe the current root as a healthy Yoast index. The working WordPress index is `/wp-sitemap.xml`.

## 4. Target Architecture

Target, **not implemented**:

```text
/sitemap.xml                canonical sitemap index / entry point
├── /sitemap-static.xml     static marketing URL set
└── /wp-sitemap.xml         WordPress sitemap index
```

Valid sitemap-index semantics require `/sitemap.xml` to be a `<sitemapindex>` whose child `<sitemap><loc>` values contain absolute URLs for the two actual sitemap surfaces:

- `https://i-seo.su/sitemap-static.xml`
- `https://i-seo.su/wp-sitemap.xml`

The diagram means that root **references** both child surfaces. It does not mean redirect chaining, XML inclusion, or placing `<url>` records directly inside the root index. A sitemap index may reference another sitemap index; crawler compatibility and response/XML validity must be checked during implementation.

## 5. robots.txt Target

After the root repair is deployed and validated, robots should reference only:

```text
Sitemap: https://i-seo.su/sitemap.xml
```

This is a planned policy. Current `robots.txt` is protected and must not be changed ahead of a working root index.

## 6. Static Sitemap Maintenance

Decision remains open:

1. **Preferred:** safe automatic regeneration/update tied to authoritative static route inventory, with deterministic output and no WordPress duplication.
2. **Fallback:** bounded one-time rebuild plus a documented operator procedure covering source inventory, generation, XML validation, deployment, and regression checks.

Before choosing automation, identify the real generator/source-of-truth and prove it cannot remove valid entries or introduce private/non-indexable/WordPress duplicates.

## 7. Current Audit Evidence

- [ISEO-SU-TECH-SEO-AUDIT-EVIDENCE-v1.md](ISEO-SU-TECH-SEO-AUDIT-EVIDENCE-v1.md), especially sitemap/robots findings.
- `audits/tech-seo/ISEO-SU-TECH-SEO-FINDINGS-v1.csv`:
  - `SM-CHILD-404` — HIGH / confirmed issue / MARS / SITE OPS;
  - `SM-DUAL-ARCH` — INFO / expected behavior / SEO REVIEW;
  - `SM-MISSING-INDEXABLE`, `SM-NONINDEX` — MEDIUM / SEO review before bulk changes.
- [reports/ISEO-SU-TECH-SEO-AUDIT-FOR-SEO-TEAM-v1.md](reports/ISEO-SU-TECH-SEO-AUDIT-FOR-SEO-TEAM-v1.md).

## 8. Open Implementation Task

One future charter should:

1. back up `/sitemap.xml`, `/sitemap-static.xml`, and `robots.txt`;
2. identify the actual runtime owner/generator of `/sitemap.xml`;
3. replace obsolete child references with the two working absolute `<loc>` values;
4. validate HTTP status, XML namespaces/schema semantics, and child reachability;
5. decide and implement static sitemap maintenance;
6. update/verify robots to reference only root after root validation;
7. run a targeted sitemap/indexability crawl and record rollback evidence;
8. promote lasting runtime changes to the applicable canonical source/procedure.

**No sitemap, robots, WordPress, or production mutation was performed by this documentation task.**
