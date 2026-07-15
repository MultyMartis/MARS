# Forge Proger Experience — FP-0002 V9-06 Batch 01

**Classification:** Documentation / experience capture only  
**Not:** brain upgrade, runtime product, governance authority  
**Scope project:** FP-0002 — Shpigovsky.ru (Website Factory WordPress delivery)  
**Wave covered:** V9-06 WordPress parity & admin SoT roughly E26–E53 (with deepest lessons E38–E53)

---

## 1. What project this was

FP-0002 is a Website Factory client project: medical clinic site for Shpigovsky, delivered as:

1. Static V9 frontend baseline (operator-approved).
2. Local WordPress runtime on MARS-Localhost (`shpigovsky.test`, `mars_wp_fp0002`).
3. Canonical Git source under `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/`.
4. Editor-facing admin (ACF) for Olga — not developer tooling — as a first-class product surface.

Factory lane: Web-GPT planning + Cursor execution under MARS monorepo discipline.

---

## 2. What we built (accepted outcomes)

| Layer | Outcome |
|-------|---------|
| Frontend canon | V9 static parity ported into WP theme templates/partials |
| Home admin parity | Frozen E42 — ACF SoT for Home blocks, hero slider, toggles |
| Services hub | Frozen E44 — hub page ACF + layout governance start |
| Service layout model | Editor roles Раздел / Услуга / Заглушка; technical stacks underneath |
| Section (Раздел) pages | ACF SoT + demo seed; empty optional hides (E46/E50) |
| Service (Услуга) pages | Large ACF parity model; representative then full rollout (E47–E49) |
| Placeholder mode | Render-only stub; real admin save validation required (E51+FIX02) |
| Generic pages | ACF SoT + placeholder mode; 15 pages seeded (E52) |
| Admin UX polish | Section styling: mute internal ACF borders; keep major separators (E53) |
| Git | Selective persistence for E38–E51 pushed via clean-worktree divergence resolve; E52–E53 closeout in this batch |

---

## 3. Why it was hard

1. **Two sources of truth temptation** — hardcoded template demo vs ACF vs Media Library vs operator CSS drift.
2. **Editor ≠ developer mental model** — technical layout variants leaked into UI; had to invent editor role + sync.
3. **False-positive validation** — meta/`acf_save_post` simulation passed while real wp-admin save failed (E51-FIX01).
4. **Monorepo Git gravity** — dirty main, interleaved MetaBOT/OCPilot commits, non-ancestor remote tips, forbidden `git add .` / reset / force-push.
5. **Scale vs safety** — dozens of service pages; alcohol copy-paste risk; representative rollout before mass seed.
6. **Admin visual quality** — ACF default chrome made editable screens unusable for non-developers even when fields were correct.
7. **Freeze culture** — operator visual acceptance loops required backup→validate→freeze→persist, not “commit when green.”

---

## 4. Key decisions

| Decision | Rationale |
|----------|-----------|
| ACF is normal SoT for admin-managed pages | Hardcoded demo only as emergency fallback |
| Empty optional fields hide | Never re-inject demo content on empty |
| Placeholder is render-only | Do not delete ACF content when switching Заглушка |
| Editor role vs technical layout | Show simple Russian choices; sync technical variant behind the scenes |
| Representative then full rollout | Catch alcohol-copy and layout bugs on 5 pages before 26 |
| Real admin form POST for layout switches | Only trusted proof of editor switch reliability |
| Freeze before persistence; persistence before push | Separate human-gated waves |
| Clean worktree for divergence | Never reset/clean/stash dirty main |
| Admin CSS is product | Treat wp-admin readability as acceptance criterion |
| Experience pack ≠ brain inject | Capture first; integrate later under charter |

---

## 5. Patterns that emerged

See [PATTERNS-LEARNED.md](./PATTERNS-LEARNED.md). Short list:

- frontend-canon → admin parity → ACF SoT → seed → validate → freeze
- page-type factories (Home, hub, section, service, generic) share the same loop
- operator CSS intentional drift is a first-class preserved state
- evidence CSVs + freeze markers as operational memory

---

## 6. What should be reused in Forge Proger (later)

Candidates for a **future** brain/rules upgrade (not this batch):

1. Page-type admin-parity playbook (audit → fields → seed → empty-hide → freeze).
2. Real-admin-save validation checklist (nonce + `acf[field_…]` names).
3. Monorepo selective persistence / clean-worktree push protocol.
4. Admin UX bar for non-developer editors (section titles, muted internal borders, RU labels).
5. Placeholder/render-mode contract (content preserved).
6. Representative rollout gate before mass content mutation.
7. Source↔runtime hash sync + operator-CSS-drift rule.

---

## 7. What should NOT yet become a rule

| Item | Why wait |
|------|----------|
| Exact ACF field counts / Shpigovsky group keys | Project-specific |
| Alcohol `#74` special-case gates | Domain-specific |
| Exact Russian medical copy patterns | Client content |
| Hard-coded route lists from this site | Not portable |
| “Always 15 generic pages” | Inventory-dependent |
| Immediate global admin CSS standard | Needs second project confirmation |
| Automatic push after every freeze | Still high-risk in monorepo |

---

## 8. What to validate in the next project / batch

1. Does the admin-parity loop transfer to a non-clinic Website Factory site?
2. Does real-admin-save false-positive risk recur with different ACF nesting?
3. Can placeholder mode generalize without breaking dedicated templates?
4. Is clean-worktree merge still the right default for divergence in 2026 ops?
5. Second experience batch from the next Web-GPT chat — then consider brain upgrade charter.

---

## 9. Explicit non-integration statement

This pack lives under FP-0002 docs.

- Forge Proger brains: **unchanged**
- Global MARS authority / AGENTS / .cursorrules: **unchanged by this pack**
- System prompts: **unchanged**

Upgrade requires a later operator charter after batch-02 (or equivalent) experience.
