# Legacy migration path v1 (Wave 5)

**Status:** **documented** — **legacy Gulp workspace → Wave 5 compatible** adoption.  
**Not:** automated migrator, **not** Triumph production proof.

**Preferred reference logic:** Triumph V1/V2 workspaces (`triumph-manipulator-landing`, `triumph-manipulator-landing-v2`) — battle-tested patterns; migrate **structure**, not client copy.

---

## Target state

Workspace matches:

- [_template-client-v1](../../workspaces/_template-client-v1/) or [website-factory-reference-v1](../../workspaces/website-factory-reference-v1/) layout  
- [foundation-adoption-charter-v1.md](foundation-adoption-charter-v1.md)  
- [adoption-validation-flow-v1.md](adoption-validation-flow-v1.md)

---

## Adoption sequence

```text
1. Inventory   — list sections, global JS, builder markup (WPBakery = compatibility only)
2. Freeze scope  — one page route first (usually index)
3. Scaffold      — copy _template-client-v1 OR align folders to reference
4. Foundations   — wholesale copy foundations + js/core (no merge with legacy resets)
5. Shell         — header/footer/modal from reference pattern
6. Sections      — one block_id per session; Triumph → extract via discipline doc
7. Validate      — adoption-validation + operational QA entry
8. REPORT        — each phase; chat ≠ SoT
```

---

## Safe migration order

| Order | Layer | Risk | Triumph lesson |
|-------|-------|------|----------------|
| 1 | `foundations/` + `js/core/` | Critical | Do not blend legacy `$tm-*` tokens into `_tokens.scss` piecemeal — map once |
| 2 | Layout shell | High | HEADER ≠ HERO — keep separate partials |
| 3 | `hero` | High | First viewport + modal path |
| 4 | `social_proof` / `pricing` | Medium | Conversion spine |
| 5 | `lead_form` / `contact_block` | Medium | Form endpoint project-local |
| 6 | `faq` / trust blocks | Medium | Extract neutralized — see Wave 5 FAQ example |
| 7 | `sticky_cta` | High | z-index + destroy cleanup |
| 8 | Remaining sections | Per handoff | No bulk paste from Triumph HTML |

**Do not** migrate all sections in one pass unless HITL charter explicitly allows.

---

## Freeze expectations

- **No freeze** until `npm run build` PASS + adoption validation **Adoption-ready**.  
- Legacy `$tm-*` / `.trust-*` selectors stay in old files until section replaced — do not alias into foundations.  
- Freeze records: block_ids migrated, blocks still legacy, SAFE UNKNOWN tests.

---

## Replacement strategy

- Per [section-replacement-contract-v1.md](section-replacement-contract-v1.md): destroy → swap partial → init.  
- Legacy section left in place until replacement PASS — avoid dual `id` anchors.  
- Remove Triumph-specific assets (Yandex logos, client photos) on extract — placeholders only in library.

---

## Foundation adoption order

1. Copy `scss/foundations/*`, `js/core/*`  
2. Replace `main.scss` shell with reference import order  
3. Map brand into `_tokens.scss` only  
4. Delete or quarantine legacy global z-index / `!important` fixes when section migrates  
5. Run [production-hardening-rules-v1.md](production-hardening-rules-v1.md)

---

## Survivability checkpoints

| Checkpoint | Pass signal |
|------------|-------------|
| Build | `gulp build` / `npm run build` exit 0 |
| Modal | open/close after hero + pricing CTAs |
| Form | single submit lock; survives one replace test |
| Sticky | no ghost after `destroySection` |
| Migration REPORT | lists legacy vs WF block_ids |

---

## Triumph-oriented notes (safe)

- **V2** `faq-cta-footer` → split FAQ (library) vs CTA/footer (project-local) — Wave 5 extracted FAQ only.  
- **V2** `trust-reviews` / `trust-cases` — high coupling to icons/assets; extract sub-patterns only with HITL.  
- **V3/V4** — reconstruction/battle-test docs are lessons; **do not** claim as Factory defaults.

---

## When to stop

- Adoption validation **Blocked** → fix foundations before more sections.  
- Builder markup unmigrateable in one slice → compatibility mode + REPORT gap.  
- Do not expand governance to “solve” migration.

*Wave 5 — first real production migration path.*
