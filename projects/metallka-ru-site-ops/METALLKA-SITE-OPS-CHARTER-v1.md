# METALLKA-SITE-OPS Charter v1

**Status:** ACCEPTED (Phase 1.5)  
**Decision date:** 2026-07-25  
**Canonical locus:** `X:\AI MARS\projects\metallka-ru-site-ops\`  
**Programme:** METALLKA-RU-SITE-OPS  
**Site:** `metallka.ru`

---

## 1. Purpose

Establish a durable MARS programme for **existing production WordPress site operations** on `metallka.ru`, including a controlled path to WPilot onboarding — **documentation and planning first**, with every live gate separately HITL-controlled.

---

## 2. Scope

### 2.1 Current allowed (Phase 1.5)

| Activity | Status |
|----------|--------|
| Documentation | **ALLOWED** |
| Repo analysis (read-only) | **ALLOWED** |
| Project setup (this locus) | **ALLOWED** |
| Site architecture planning | **ALLOWED** |
| Access-model planning | **ALLOWED** |
| Package revalidation planning | **ALLOWED** |
| Discovery planning | **ALLOWED** |

### 2.2 Current blocked

| Activity | Status |
|----------|--------|
| Credentials request | **BLOCKED** |
| Production access | **BLOCKED** |
| FTP / SFTP | **BLOCKED** |
| WP Admin | **BLOCKED** |
| WPilot install | **BLOCKED** |
| WPilot activation | **BLOCKED** |
| Token creation | **BLOCKED** |
| Bridge enablement | **BLOCKED** |
| REST smoke | **BLOCKED** |
| Writes | **BLOCKED** |
| Local mirror | **BLOCKED** |
| ATLAS mint (ORG / WEB / DOM) | **BLOCKED** |
| Production backup execution | **BLOCKED** |
| WPilot source mutation / new plugin package | **BLOCKED** |
| i-seo / FP-0002 / Forge material mutation | **BLOCKED** |

---

## 3. Future execution model (gates)

Do **not** over-fragment into one phase per click. Each gate remains **separately HITL-controlled**.

| Gate | Intent |
|------|--------|
| **Gate A** | Production read-only discovery |
| **Gate B** | Package / compatibility + backup acceptance |
| **Gate C** | Install + activate + safe-default verification |
| **Gate D** | Token creation |
| **Gate E** | Bridge + read-only smoke |
| **Gate F** | Write enable + controlled write smoke |

**Next documentary step after Phase 1.5:** PHASE 2A — Gate A **charter preparation** only (does **not** authorize access).

---

## 4. Precedent model

None of the following is a one-to-one blueprint for metallka.ru.

### 4.1 i-seo.su — production onboarding / security precedent

| Class | Items |
|-------|-------|
| **Proven (production)** | RC6 install / update; safe defaults; production token generation (local-only storage) |
| **Not proven (production)** | REST auth; ping; read routes; backup endpoint; dry-run; scoped replace; rollback; production writes |
| **Do not transfer** | Hosting paths, credentials model details as facts for metallka, site IDs, content architecture |

Evidence locus: `projects/iseo-su-site-ops/` (Phases 6A–6C-P reports and WPilot evidence docs).

### 4.2 dev.gktriumph.ru — technical DEV precedent

| Class | Items |
|-------|-------|
| **Proven (DEV)** | The7 child theme; WPBakery; nested `vc_*` shortcodes; `vc_raw_html`; `post_content` mutation experience; WPilot RC5 connection + content-write proof on DEV |
| **Do not transfer** | IDs, versions, theme options, paths, tokens, shortcodes, page structure |

Evidence locus: `projects/wpilot/` (RC5 final state / proven capabilities).

### 4.3 FP-0002 / Forge — methodology precedent

| Class | Items |
|-------|-------|
| **Reusable** | Source/runtime authority discipline; admin parity; operator-change canon; bounded-first rollout; rollback; frontend/mobile QA |
| **Do not transfer** | Custom theme architecture; ACF as automatic SoT; custom CPT structure; field schema |

Evidence locus: Forge WordPress + `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/`.

---

## 5. ATLAS binding

| Field | Value |
|-------|-------|
| **Binding status** | **PARTIAL / INCOMPLETE** |
| **Known** | `PER-0003` — Лиматов Роман Курбанович (Person **active**, E0; primary org **SAFE UNKNOWN**) |
| **Organization** | **NOT FOUND** |
| **Website** | **NOT FOUND** |
| **Domain** | **NOT FOUND** |

**Normative:** Person record does **not** prove ownership, client contract, or legal binding to `metallka.ru`. Do **not** mint ORG/WEB/DOM in this programme without a separate ATLAS charter.

Re-verified read-only against ATLAS Wave 2 population / attestation docs (2026-07-25 session). Counterparty-card storage slug `metallka\` exists as a **storage folder label** — not an attested Organization entity.

---

## 6. Source / runtime policy (project default)

Until source authority is discovered and attested:

- **Production runtime** is the **provisional authority** for existing site files and content.

For later filesystem work (only when separately chartered):

1. Fetch current production file  
2. Hash it  
3. Retain before-copy  
4. Compare against any discovered source  
5. Resolve authority  
6. Modify exact file only  
7. Deploy exact file only  
8. Fetch back  
9. Verify hash  
10. Frontend / admin QA  

**No** broad site synchronization.

**Admin-first:** use WP Admin / WPBakery / The7 UI for content/settings where that layer is confirmed owner.  
**Filesystem-first** only for actual code-owned surfaces.

---

## 7. First future safe task policy (record only — do not execute)

### 7.1 Recommended first normal development task (after full onboarding)

- One small text change  
- On one low-risk existing WPBakery page  
- Inside one non-global `vc_column_text` block  
- No layout change  
- No URL change  
- No form  
- No header/footer  
- No `vc_raw_html`

### 7.2 Recommended first future WPilot write smoke

- Separate draft/private test page  
- One exact-once marker in plain `post_content`  
- **Never** use `vc_raw_html` as first write target

---

## 8. Local mirror policy

| Field | Value |
|-------|-------|
| **Current decision** | **DEFER** |
| **Runtime profile** | **Not created** |

**Remote-only acceptable for (later, when chartered):**

- Simple content changes  
- Menu edits  
- Small builder edits  
- WPilot install / onboarding

**Local mirror strongly recommended / required for:**

- PHP  
- Child-theme architecture  
- Large JS  
- Plugin development / integration  
- Major WPBakery restructuring  
- Major section development  
- Refactor  
- Schema work

---

## 9. Explicit exclusions

- Claiming production connection or WPilot presence on metallka without evidence  
- Filling SAFE UNKNOWN from analogy to i-seo / triumph / FP-0002  
- Broad Git staging / foreign WIP interference  
- Secret files, tokens, or credentials in this locus  

---

*Charter v1 · Phase 1.5 · documentation only.*
