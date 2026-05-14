# MARS — External system boundaries (MetaBOT / SEO Content Agent)

**Status:** **documented** — governance clarification only. **Version:** v0 (Phase S2).

**Scope:** Reduce confusion between **MetaBOT — SEO Content Agent**, the **legacy** `seo-content-agent` pack, and **in-repo runtime adapters**. **No** architecture expansion.

---

## 1. What MetaBOT is

**MetaBOT — SEO Content Agent** is an **external multi-workflow operational system** (n8n-hosted Intake / Worker / Admin, plus documented future areas). It **owns** branching, retries, credentials, and live graph truth.

**Canonical in-repo documentation** for that system lives under **`projects/metabot-seo-content-agent/`** (see `registry/project-registry.md`). That **does not** move execution ownership into MARS.

---

## 2. What a runtime adapter is **not**

Files under **`mars-runtime/adapters/`** (e.g. SEO Content Agent–shaped adapter) are **local experimental I/O helpers** for narrow demos. They are **not**:

- a duplicate of MetaBOT’s internal graphs  
- a declaration that MARS **dispatches** or **owns** MetaBOT  
- proof that a governance **`tool_id`** is enforced repo-wide  

**Rule:** Say **adapter** when referring to this code; say **MetaBOT** when referring to the external system.

---

## 3. Legacy pack

**`projects/seo-content-agent/`** is **legacy** (early spec / bridge artifacts). **Do not** treat it as the current integration story; **do not** extend it for new MetaBOT work. Prefer the MetaBOT pack + [integration-boundary.md](../projects/metabot-seo-content-agent/integration-boundary.md).

---

## 4. External workflow IDs vs MARS entities

- **n8n workflow IDs, node names, Telegram command strings** are **native to those platforms**.  
- They **do not** automatically become **MARS canonical governance entities** (agents, tools, projects) unless a **human** adds an explicit mapping in the appropriate registry or contract doc.  
- **Integration existence** (a webhook works in a demo) **≠** **ownership** of the external system by MARS.

---

## 5. Source of execution truth

**Live n8n** (and related provider consoles) remains authoritative for **what actually runs**. This repository may hold **sanitized** maps and contracts — see [registry-source-of-truth.md](registry-source-of-truth.md) and [runtime-registry-boundaries.md](runtime-registry-boundaries.md).

---

*No new bridges, services, or persistence are introduced by this document.*
