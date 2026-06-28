# FP-0002 V8 — Sequential Consolidation Plan v1

**Status:** PLAN ONLY — no implementation in bootstrap pass  
**Date:** 2026-06-28  
**Prerequisite:** Operator approval of bootstrap audit + parity evidence

---

## Principles

1. One family per pass — no batch renaming across unrelated blocks.
2. Visual parity with V7 baseline tag before and after each pass.
3. Page-specific class survives only with `REUSE_IMPOSSIBILITY_PROVEN`.
4. V7 remains untouched; all edits in V8 only.
5. Static client demo (V7 tag `fp-0002-v7-static-client-demo-stable-02`) is not redeployed until explicit operator charter.

---

## Phase 0 — Bootstrap (this pass) ✓

- [x] Freeze V7 as `IMMUTABLE_STABLE_FALLBACK`
- [x] Create V8 from `fp-0002-v7-four-template-canonical-demo-baseline-01`
- [x] Exclude o-centre WIP
- [x] Build V8 before consolidation
- [x] Component family audit + registry
- [ ] Operator approval to start Phase 1

---

## Phase 1 — Upper nav band (CF-003) — P1

**Problem:** Three page wrappers + duplicated breadcrumbs/subnav CSS under `.page-service-subdivision-v1` and `.page-service-leaf-v1`.

**Steps:**

1. Capture pixel baseline screenshots (desktop 1440, mobile 390) for three templates — upper nav region only.
2. Design target partial: `partials/components/page-upper-nav.html` accepting breadcrumb + subnav include params.
3. Introduce neutral class family `.page-upper-nav*` (name TBD at implementation — single family).
4. Migrate `uslugi-v2.html` first (simplest breadcrumb depth); verify build + visual diff.
5. Migrate subdivision; remove page-scoped breadcrumb/subnav CSS duplication.
6. Migrate leaf; reconcile intentional 12px vs 14px breadcrumb — **decide against Figma**, not by averaging.
7. Delete obsolete `.page-*__upper-nav` wrappers only after parity sign-off.

**Exit criteria:** One partial, one CSS family, three pages visually match baseline captures.

---

## Phase 2 — Program block unification (CF-005) — P1

**Problem:** `services-program-v2.html` reused with stacked modifiers (`--subdivision`, `service-subdivision-program-v1`, `service-leaf-program-v1`).

**Steps:**

1. Inventory modifier-only diffs vs true visual diffs.
2. Collapse redundant modifier classes that encode the same geometry.
3. Keep content-parameterized includes; avoid new page wrappers.
4. Verify CTA band inclusion rules on hub vs subdivision vs leaf.

---

## Phase 3 — Inner hero container overrides (CF-002) — P2

**Steps:**

1. Merge `.page-service-subdivision-v1 .services-inner-hero-v2__container` and leaf equivalent into hero partial parameters or one modifier with documented visual intent.
2. Retest hero at 1024/767/390.

---

## Phase 4 — Neutral naming for proven cross-page `home-*` blocks — P2

**Order (lowest risk first):**

1. `home-final-form` → site-wide footer form family
2. `home-faq`
3. `home-comfort`
4. `home-founder-quote`
5. `home-reviews`, `home-specialists`, `home-clinic-landscape`

Each rename is a **separate sub-pass** with build + visual check.

---

## Phase 5 — Category section modifiers (CF-004) — P2

Reduce page-specific section modifier sprawl where visuals match hub category blocks.

---

## Phase 6 — New page policy — ongoing

All new pages (including future «О центре») must pass V8 component gate before any page-specific class is created.

---

## Explicitly deferred

- «О центре» page implementation
- Static demo generator port to V8
- Deploy ZIP / hosting changes
- Mass deletion of V7 reviews or historical WIP

---

## Risk register

| Risk | Mitigation |
| ---- | ---------- |
| Accidental visual drift during CSS merge | Per-phase screenshot diff against baseline tag |
| Breaking gulp includes | One page migrated at a time; `npm run build` each step |
| Leaf breadcrumb 12px is intentional | Figma check before normalizing to 14px |
| Renaming `home-*` breaks static demo | Demo stays on V7 until V8 consolidation charter extends to demo |
