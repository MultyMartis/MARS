# Timeline — FP-0002 V9-06 (Experience Batch 01)

Structured stages for Forge Proger learning. Each stage: purpose → main decision → accepted result → what we learned.

---

## E26–E29 — Base WordPress parity

| | |
|--|--|
| **Purpose** | Stabilize WP shell/blog/readiness after earlier D-series visual port |
| **Main decision** | Treat WP as delivery target with Git `WORDPRESS/` as editable source |
| **Accepted result** | Local readiness baseline; blog archive ACF port path opened |
| **Learned** | Route/rewrite ownership must be proven before “visual done” claims |

---

## E30–E35 — Services / specialists / blog rollout

| | |
|--|--|
| **Purpose** | Expand CPT/page coverage beyond Home skeleton |
| **Main decision** | Incremental page-type ports with selective Git persistence checkpoints |
| **Accepted result** | Services/specialists/blog surfaces live in local runtime |
| **Learned** | Selective persistence beats “dirty main commit everything” |

---

## E36–E37 — Mobile CSS fixes

| | |
|--|--|
| **Purpose** | Home mobile polish after desktop parity |
| **Main decision** | Persist operator-accepted CSS with explicit checkpoint |
| **Accepted result** | Mobile polish PASS + selective persistence |
| **Learned** | Operator CSS may diverge from source on purpose — document drift |

---

## E38–E42 — Home admin parity / freeze

| | |
|--|--|
| **Purpose** | Make Home fully editable in admin matching frontend blocks |
| **Main decision** | Home ACF group as SoT; freeze Home after operator accept (E42) |
| **Accepted result** | Home frozen; 74-field model; hero slider + toggles |
| **Learned** | Freeze markers create a hard “do not touch without charter” boundary |

---

## E43–E44 — Services hub / freeze

| | |
|--|--|
| **Purpose** | Apply Home admin-parity pattern to `/uslugi/` |
| **Main decision** | Hub ACF + freeze; start layout-variant governance |
| **Accepted result** | Hub frozen (E44); Option B layout model recommended |
| **Learned** | Same parity loop transfers across page types |

---

## E45 — Layout governance

| | |
|--|--|
| **Purpose** | Replace confusing technical layout dropdown with editor roles |
| **Main decision** | `service_editor_role` + hidden/tech sync to `service_layout_variant` |
| **Accepted result** | Раздел / Услуга (+ later Заглушка); `alcohol_special` → `service_general` rename |
| **Learned** | Editor-facing simplicity requires backend sync discipline |

---

## E46 — Section page model

| | |
|--|--|
| **Purpose** | Раздел pages admin-editable in frontend order |
| **Main decision** | Large section parity ACF group; later remove “template as normal SoT” wording |
| **Accepted result** | Sections editable; emergency fallbacks only |
| **Learned** | Demo fallback must not become the quiet default source |

---

## E47 — Service page model

| | |
|--|--|
| **Purpose** | Услуга pages full block admin parity (alcohol #74 control) |
| **Main decision** | Dedicated general-parity group; many FIX loops for ACF render/UX/read-more |
| **Accepted result** | Услуга model frozen after FIX04 operator accept |
| **Learned** | Nested ACF conditionals can hide entire groups silently |

---

## E48 — Representative rollout

| | |
|--|--|
| **Purpose** | Seed a small representative set before all services |
| **Main decision** | Page-specific / neutral DEMO; no alcohol copy-paste |
| **Accepted result** | Controls `#74/#314/#78/#81/#85` validated |
| **Learned** | Representative gate catches contamination early |

---

## E49 — Full rollout (+ FIX01)

| | |
|--|--|
| **Purpose** | Seed remaining Услуга pages |
| **Main decision** | Mass seed with alcohol paste ban; freeze; restore `#315` when drifted to placeholder |
| **Accepted result** | Full rollout freeze after FIX01; `#315` back to Услуга |
| **Learned** | Freeze can expose post-rollout drift; fix restores before re-freeze |

---

## E50 — Service sections ACF SoT

| | |
|--|--|
| **Purpose** | Sections demo texts living in ACF; empty → hide |
| **Main decision** | Remove normal-path hardcoded inject; keep emergency helpers technical-only |
| **Accepted result** | Sections freeze accepted («Всё гуд!») |
| **Learned** | Empty-hide is part of SoT contract, not a FE convenience |

---

## E51 — Placeholder mode (+ FIX01 false-positive / FIX02)

| | |
|--|--|
| **Purpose** | Restore Заглушка as render-only stub layout |
| **Main decision** | Role→stack mapping; real wp-admin save must keep `acf[field_…]` names |
| **Accepted result** | Placeholder freeze; `#78` ends as Услуга after real switch proof |
| **Learned** | Simulation PASS ≠ operator admin PASS |

---

## E52 — Generic pages ACF SoT + placeholder

| | |
|--|--|
| **Purpose** | Ordinary `generic.php` pages leave hardcoded demo path |
| **Main decision** | `generic_page_lead/body` SoT; seed from page `post_content`; retain layout mode |
| **Accepted result** | 15 pages PASS; placeholder validated on `#1039` (final full) |
| **Learned** | Generic pages need admin CSS enqueue too (gap closed in E53) |

---

## E53 — Admin UX polish

| | |
|--|--|
| **Purpose** | Make ACF screens readable for Olga |
| **Main decision** | Unified admin CSS; mute internal borders; keep section titles; expand enqueue |
| **Accepted result** | Operator: «Ну вот теперь гуд.» — frozen |
| **Learned** | Admin UX is acceptance-critical even with correct fields |

---

## Git persistence / push incident and resolution

| | |
|--|--|
| **Purpose** | Persist accepted E38–E51 source; later publish despite monorepo divergence |
| **Main decision** | Exact-path staging only; no dirty-main reset; clean worktree merge for non-ancestor remote |
| **Accepted result** | Persistence commits landed; remote tip advanced via divergence-resolve merge (`03ff6777…`); E52–E53 closeout follows same rules |
| **Learned** | Ahead stacks mix projects — review path scope before push; base commit must be ancestor, not necessarily HEAD; postcommit evidence can create commit tails |

---

## Closeout of this pack (E52–E53)

| | |
|--|--|
| **Purpose** | Freeze E53; persist E52–E53 + document Forge Proger experience |
| **Main decision** | Docs-only experience pack; no brain/rules integration |
| **Accepted result** | This batch folder + freeze marker + persistence charter |
| **Learned** | Capture experience immediately after acceptance, before chat migration |
