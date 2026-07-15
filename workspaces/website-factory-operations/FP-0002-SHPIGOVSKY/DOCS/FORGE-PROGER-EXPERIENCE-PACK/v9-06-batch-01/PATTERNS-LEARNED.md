# Patterns Learned — FP-0002 V9-06 Batch 01

Patterns proven useful on Shpigovsky. Candidates for later Forge Proger reuse — **not yet rules**.

---

## 1. frontend-canon → admin parity → ACF SoT → seed → validate → freeze

Do not start with mass DB writes. Sequence:

1. Frontend block inventory against accepted static/canon.
2. Admin field model matching frontend order.
3. Declare ACF the normal SoT.
4. Seed current visible content.
5. Validate FE + admin + regression.
6. Freeze with backup + marker.

## 2. Demo content migration into ACF

If the page already shows good content from templates/demo:

- Export what is visible.
- Write into ACF fields (page-specific).
- Then remove normal-path hardcoded inject.

Do not invent new marketing copy during migration.

## 3. Empty optional fields hide (not template demo inject)

Contract:

- Optional empty → section/block hidden or empty-safe.
- Do **not** silently refill from template demo.
- Emergency fallbacks may exist in code but must not be the admin-facing SoT story.

## 4. Emergency fallback vs normal source

| Mode | Allowed |
|------|---------|
| Normal | ACF / options / Media Library |
| Emergency | PHP helper returns last-resort markup/text |
| Forbidden as normal | Template demo presented to editor as “source” |

## 5. Placeholder mode as render-only switch

Switching to Заглушка:

- Changes render stack only.
- Preserves ACF meta/content.
- Must be reversible without re-seed.

## 6. Real admin save validation

Trust hierarchy:

1. Authenticated wp-admin form POST with ACF nonce + `acf[field_…]` names.
2. Operator visual confirmation.
3. Meta/`update_post_meta` / `acf_save_post` simulation — supporting only.

Never close a save bug on (3) alone.

## 7. Role / layout split

- Editor sees: Раздел / Услуга / Заглушка (Russian, few choices).
- System stores: technical `service_layout_variant` / stack.
- Sync on save; hide advanced technical controls by default.

## 8. Editor-facing simple choices vs technical layout values

Rename/alias technical values when they leak brand-specific history (`alcohol_special` → `service_general`). Keep legacy resolver aliases if needed; do not show them in UI.

## 9. Representative rollout before full rollout

Seed 3–5 representative pages spanning edge cases (parent child tiles, nested ordinary, specialty branches). Validate FE + admin. Only then mass-seed.

## 10. Freeze before persistence

Operator accept → freeze backup/marker → then Git. Freezing is the product checkpoint; commit is the archive checkpoint.

## 11. Persistence before push

Commit locally with exact path allowlist. Push is a separate gate (ahead review, remote ancestry, no force).

## 12. Clean worktree for Git divergence

When remote tip is not an ancestor of dirty HEAD:

- Do not pull/merge/rebase dirty main.
- Do not reset/clean/stash foreign WIP.
- Use a clean worktree based on remote tip; merge the desired commit(s); push from there if conflict-free.

## 13. Operator visual review loop

Text evidence ≠ visual accept. Stop after each UX-sensitive stage for human glance. Quote acceptance in freeze marker.

## 14. Admin UX as product quality

If fields are correct but screens look like noisy grey ACF grids, the product is not done. Section titles, spacing, and muted internal separators matter.

## 15. When to avoid over-generalizing into global rules

Project-specific field keys, route lists, medical copy, and one-off page IDs must stay local until a second project confirms the pattern.
