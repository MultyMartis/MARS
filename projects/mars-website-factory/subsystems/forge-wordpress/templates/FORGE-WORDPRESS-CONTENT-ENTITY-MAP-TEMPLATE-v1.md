# {PROJECT-ID} — Content Entity Map v1

**Artifact ID:** CONTENT-ENTITY-MAP  
**Project:**  
**Date:**  
**Author:**  
**Standard:** [CMS ARCHITECTURE](../standards/FORGE-WORDPRESS-CMS-ARCHITECTURE-STANDARD-v1.md)

---

## 1. Entity registry

| Entity | Signals (URL / reuse / CRUD / SEO / relations / growth) | Primitive | Slug / hub | Archive | Notes |
|--------|----------------------------------------------------------|-----------|------------|---------|-------|
| | | page \| post \| CPT \| taxonomy \| options \| repeater \| hardcoded | | yes/no | |

---

## 2. Reusability scores

| Candidate | Q1 many pages | Q2 lifecycle | Q3 URL | Q4 search | Q5 relation target | Q6 collection order | Q7 SEO | Q8 growth | Score | Decision |
|-----------|---------------|--------------|--------|-----------|--------------------|---------------------|--------|-----------|-------|----------|
| | y/n | y/n | y/n | y/n | y/n | y/n | y/n | y/n | /8 | |

---

## 3. CPT / taxonomy evaluation

| Pattern | CPT? | Taxonomy? | Repeater? | Decision | Rationale |
|---------|------|-----------|-----------|----------|-----------|
| | | | | | |

Hard CPT questions (FW-S-10): independent add/remove; own permalink; dedicated Admin list.

---

## 4. Storage map (summary)

| Content | Page | Post | CPT | Tax | Options | Repeater | Flex layout | Hardcoded |
|---------|------|------|-----|-----|---------|----------|-------------|-----------|
| | | | | | | | | |

---

## 5. Lifecycle

| Entity | draft | publish | private | scheduled | who creates |
|--------|-------|---------|---------|-----------|-------------|
| | | | | | editor \| admin |

---

## 6. URL ownership

| Public URL pattern | Owner object | `has_archive` | Hub page |
|--------------------|--------------|---------------|----------|
| | | | |

---

## 7. SEO ownership

| Public type | seo_title / meta_description group | Fallback |
|-------------|--------------------------------------|----------|
| | | post title / excerpt |

---

## 8. SAFE UNKNOWN / blockers

| Item | Blocks |
|------|--------|
| | P1b / frontend |

---

*Fill before ACF groups. Summary also goes into CONTENT-MODEL (FW-T-04).*
