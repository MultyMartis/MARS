# 08 — Active projects and lanes (migration v0)

**Registry source:** `registry/project-registry.md` (authoritative rows).

---

## Classification table

| Project / area | Typical lane | Status label | Notes |
|----------------|--------------|--------------|-------|
| **MARS core** | B | **active** (docs) | Governance, workflows, architecture maps |
| **Website Factory** | B | **active** (docs) | `projects/mars-website-factory/`, C16 |
| **Frontend Gulp Agent** | A | **active** (operational pack) | `agents/frontend-gulp-agent/` |
| **Triumph Manipulator Landing** | A (+ project docs) | **active** | `projects/triumph-manipulator-landing/`, `workspaces/triumph-manipulator-landing/` |
| **MetaBOT — SEO Content Agent** | B / integration docs | **active (canonical docs)** | `projects/metabot-seo-content-agent/` — external system; MARS holds sanitized knowledge |
| **SEO Content Agent (folder)** | B / legacy | **legacy** | `projects/seo-content-agent/` — do not extend as canonical |
| **mars-runtime** | Runtime | **reference + partial code** | Contracts + experimental adapters/tests — **not** full product runtime |
| **integrations leftovers** | B / legacy | **legacy** | e.g. `projects/seo-content-agent/integrations/*` bridge notes |
| **web-gpt-sources** | B | **reference** | Imported Web-GPT pack; distinguish from “current product code” |
| **shared/assets/icon-libraries** | A (if used by Triumph) | **SAFE UNKNOWN** until operator classifies license + lane | Large untracked vendor drop at export time |

---

## Lane quick map

- **Governance + Factory evolution** → **Lane B**.  
- **Triumph build + workspace + design-for-implementation** → **Lane A**.  
- **Adapter/test experiments** → **Runtime** (own commits, no mix).

## SAFE UNKNOWN (cross-project)

- Pilot **charter** completion in Stage 16 (“missing” per master build map).  
- Whether **all** legacy SEO artifacts will be retired vs archived.
