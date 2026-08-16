# Forge Proger Experience — FP-0002 V9 Stable v1 Phase 02

**Classification:** Documentation / experience capture only  
**Not:** brain upgrade, runtime product, governance authority, cleanup execution  
**Scope project:** FP-0002 — Shpigovsky.ru (Website Factory WordPress delivery)  
**Wave covered:** V9-06E54 → V9-06E63 (after Phase 1 / E53 admin UX freeze through Stable v1)

---

## 1. Evolution from E53 to Stable v1

Phase 1 ended with an **accepted admin-parity baseline**: ACF as normal SoT for major page types, placeholder mode proven via real wp-admin save, E53 admin CSS accepted («Ну вот теперь гуд.»), and Experience Pack Batch 01 written under `v9-06-batch-01/`.

Phase 2 covers the next maturity jump:

| Stage | Meaning |
|-------|---------|
| E53 freeze | Working **admin product** + frozen page-type models |
| E54–E57 | Shell motion / Site Settings UX / operator asset refinements |
| E58 | Visual-audit freeze + Figma findings (decision pack, not blind “fix everything”) |
| E59–E62E | Incremental visual + admin + reusable-component acceptance loops |
| E63 | **Stable local near-production system**: operator canonized, frozen, committed, pushed |

The project moved from “implementation works and is frozen by page type” to “the whole local WordPress system is an accepted near-production baseline,” **without** claiming public production readiness.

Authoritative release identity: `REPORTS/STABLE-V1/RELEASE-MANIFEST-FP-0002-V9-STABLE-V1.md`.

---

## 2. From working implementation to stable near-production

Stable v1 required more than green local PASS reports:

1. **Operator acceptance of the current result** (not “all open tails closed”).
2. **Runtime → source canonization** of latest operator CSS/JS before freeze.
3. **Tail ledger** with explicit dispositions (ACCEPTED_DEFERRED / CLOSED / OUT_OF_SCOPE).
4. **ACF source/runtime disposition** without broad JSON sync.
5. **Release validation pack** (routes, viewports, lint, duplicate IDs).
6. **Authoritative freeze backup** + rollback notes.
7. **Clean-worktree exact-allowlist Git** (dirty main untouched; no force push).
8. **Deferred production checklist** kept separate from Stable claims.

Formulation locked in release docs: **Stable local near-production baseline**. Production deployment: **not performed**.

---

## 3. Operator ↔ Cursor / Forge Proger interaction model

Observed durable model:

```text
Operator visual/manual edits (often runtime CSS/templates)
        ↓
Cursor/Forge wave: preflight audit → promote legitimate runtime → scoped mutate
        ↓
Local validation evidence (hashes, screenshots, smoke)
        ↓
Operator visual review (accept / reject / refine)
        ↓
Optional freeze → optional Git persistence → optional push (separate gates)
```

Key behavioral rules that emerged after E53:

- Text PASS ≠ operator acceptance.
- Broad mixed charters create oversized waves and hidden regressions.
- Operator manual edits on runtime are **first-class canon during active visual development**.
- Agents must **merge into latest operator files**, not restore old “source truth” over them.
- “No follow-up needed” is unsafe while tails remain in the ledger.

---

## 4. Incremental visual acceptance

E54–E62 progressed as many small accepted deltas rather than one mega-wave:

- Floating header → FIX01 background/menu scroll.
- Site Settings admin UX (options-page DOM ≠ post edit DOM).
- Operator asset batch → hero/slider FU → Libertinus → lifebuoy parallax FIX01/FIX02.
- E58 freeze-before-audit → FU01 decision pack → only E58-VA-001 confirmed for E59.
- Layout polish / maps / Comfort CTA → FIX01 decor + Contacts cleanup.
- Nav/CTA unify → FIX01 breadcrumb hover + Reviews typography correction.
- Large E61 admin/content batch (PARTIAL; tails explicit) → E62A–E62E staged completion.

**Lesson:** visual acceptance compounds. Each FIX wave is cheaper than reopening a “finished” surface after a mega-batch.

---

## 5. Runtime-first operator canon

During E54–E62, runtime frequently became **newer** than Git source because the operator edited live CSS/JS. The safe pattern:

1. Hash-compare source ↔ runtime for protected files (`v9-style.css`, later `fp02-search.css`, `v9-shell.js`).
2. If runtime is ahead and edits are legitimate → **promote runtime → source**.
3. Apply wave changes **on top of promoted files**.
4. Exact-file delivery; no broad sync; no MIR restore of older backups as “fix.”

At E63, the development-time runtime canon was **frozen into source/runtime parity** and hashed into the release manifest. See [RUNTIME-OPERATOR-CANON-PATTERN.md](./RUNTIME-OPERATOR-CANON-PATTERN.md).

---

## 6. Architectural maturity gained (post–Phase 1)

| Area | Maturity added in Phase 2 |
|------|---------------------------|
| Shell UX | Floating header, lifebuoy parallax, local Libertinus titles |
| Admin | Site Settings options UX; breadcrumb toggles; Contacts multi-location; Blog/Reviews pagination admin; O-centre cleanup; Service legacy groups `active:false` |
| Ownership | Page-owned fields vs reusable blocks; Founder Quote seeding; Treatment Program mini-descriptions on child pages |
| Frontend reuse | Shared CTA band; review cards + stable `review_uid`; breadcrumb wrappers; Triumph phone mask; Search baseline; 404 decor |
| Visual process | Figma audit with false-positive filtering; visual authority hierarchy |
| Release | Tail ledger, ACF disposition, clean-worktree Stable push |

---

## 7. Current limits of automation

Automation / agent execution remains **assistive**, not autonomous product ownership:

| Can automate (with human gate) | Must stay human-supervised |
|--------------------------------|----------------------------|
| Hash audits, exact-file promote, PHP lint, route smoke | Visual acceptance of layout/motion/typography |
| Backup creation + manifest hashes | Choosing which backup is style authority |
| Screenshot capture packs | Deciding Figma vs operator-accepted runtime wins |
| Idempotent seed helpers | Demo-content production cleanup decisions |
| Allowlist generation / clean-worktree copy | Push timing; force-push forever forbidden |
| Tail ledger drafting | Declaring Stable vs production readiness |

**SAFE UNKNOWN examples still open at Stable v1:** production SMTP behavior, production indexing, whether demo Blog/Reviews will be replaced or deleted, exact ACF Extended DB-duplicate inventory beyond filesystem disposition.

---

## 8. Answers to the ten Phase 2 questions (summary)

1. **What was built?** Shell polish, Site Settings UX, visual-audit process, reusable FE/admin patterns, Search/404, Stable v1 freeze+Git.  
2. **How safely?** Checkpoint backups, exact-file delivery, runtime promote-first, no broad sync, clean-worktree Git.  
3. **What worked?** Incremental FIX waves, E58 decision pack, stable review UIDs, `active:false` hide (not delete), exact allowlist release.  
4. **What failed / false PASS?** Local PASS without operator accept; accent-hover vs E58 accent; index-based review anchors; nested CTA `<section>`; incomplete admin screenshots; oversized E61.  
5. **Future similar WP projects?** Follow runtime-operator canon + visual authority hierarchy + page-type ownership matrix.  
6. **Reusable capabilities?** See capability backlog.  
7. **Human-supervised?** Visual accept, ownership design, release push, production cleanup.  
8. **Protect runtime/manual edits?** Preflight promote; never restore older backup over newer operator files without charter.  
9. **Admin UX / ACF / blocks?** Page-owned vs global block; visibility toggles ≠ content duplication; PHP registration may own source-only JSON.  
10. **Close long wave in dirty monorepo?** Tail ledger → freeze → allowlist → clean worktree → normal push → verify remote tip ≠ dirty main.

Detailed evidence: [TIMELINE-E54-E63.md](./TIMELINE-E54-E63.md), [SOURCE-TRACEABILITY-MATRIX.md](./SOURCE-TRACEABILITY-MATRIX.md).

---

## 9. Explicit non-integration statement

This Phase 2 pack lives under FP-0002 docs.

- Forge Proger brains: **unchanged**
- Global MARS authority / AGENTS / `.cursorrules`: **unchanged by this pack**
- System prompts: **unchanged**
- Product / runtime / DB: **unchanged by this documentation wave**
- Cleanup: **not executed**

Upgrade of Forge Proger rules requires a later operator charter after Phase 3 polish and/or a second project validation.
