# MARS Website Factory — SEO and marketing layer

## Scope

This layer covers **on-site** SEO strategy patterns, **commercial messaging**, and **QA** — within the **Website Factory** static-site context. It is **related but distinct** from **MetaBOT — SEO Content Agent** (`projects/metabot-seo-content-agent/`), which documents an **external** multi-workflow system (n8n) for **content** operations.

## Marketing strand

- **Marketing Strategy Agent** (planned): positioning, narrative, offer structure.
- Uses **Commercial Pattern Library** (see [registries.md](registries.md)) under **ethical** and **HITL** constraints.

## SEO strand

- **SEO Strategy Agent** (planned): search intent hypotheses, page-level focus, internal linking **intent**.
- **SEO Pattern Library** for titles, snippets, structured data **where appropriate**.
- **SEO QA Agent** (planned): on-page checks, thin content warnings, heading hierarchy.

## Integration boundary

| System | Relation |
|--------|----------|
| **Website Factory** | **Docs + contracts** for factory SEO/marketing stages; static implementation via **Gulp Frontend Agent**. |
| **MetaBOT SEO Content Agent** | **Optional** upstream/downstream **content** workflows — integration **not** assumed; any bridge needs an explicit **integration contract** (future). |

## SAFE UNKNOWN

- Live keyword data, SERP APIs, or analytics — **not** specified in this pack.
- Automated schema.org validation in CI — **not** evidenced in MARS core.
