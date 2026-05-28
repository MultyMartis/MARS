# V4 Single-Block Replacement Workflow

## Purpose

This workflow prepares Triumph V4 for controlled survivability tests where one existing screen or block is replaced by a different version while the rest of the landing remains unchanged.

It is a localized rebuild strategy, not permission to redesign the full page.

## Replacement Scope

- Replace exactly one owned section at a time: hero, prices, trust, proof strip, FAQ, final CTA, or footer.
- Keep header and footer unchanged unless the selected block is the footer itself.
- Preserve section order, anchors, Russian copy integrity, `&nbsp;`, shared assets, and Font Awesome delivery unless the task explicitly targets them.
- Do not mutate neighboring sections to make the replacement fit.

## Survivability Rules

- **Replacement isolation:** new HTML, SCSS, assets, and JS must stay section-local.
- **Section ownership:** each block owns only its partial and matching SCSS section file.
- **No global CSS poisoning:** avoid changing tokens, reset, base, header, buttons, or shared layout unless the replacement contract explicitly requires it.
- **No rhythm collapse:** preserve the page cadence before and after the replaced block; do not compress or inflate adjacent section spacing.
- **No background leakage:** backgrounds, overlays, crops, and decorative media must be scoped to the replaced section.
- **No header/footer mutation:** navigation, brand shell, legal/footer closure, and contact fallbacks remain stable unless they are the target block.
- **No unrelated spacing drift:** do not tune other sections to hide local replacement issues.
- **Safe rollback path:** keep the previous section partial/SCSS recoverable through git diff or a branch checkpoint.
- **Section-level replaceability:** the landing should still build and read correctly if the replacement is reverted alone.

## Controlled Replacement Steps

1. Name the target section and its source files.
2. Record current acceptance checks: section appears once, anchors work, no V2/V3 contamination, FA assets resolve, Russian text is readable.
3. Replace only the target section partial and section SCSS.
4. Add new local assets only under the section's existing asset boundary.
5. Run `npm run build`.
6. Verify target replacement plus unchanged neighboring sections.
7. Report what changed, what stayed intentionally stable, and what can be rolled back.

## Post-Launch Redesign Loop

Use conversion-driven redesign loops one section at a time:

- define the conversion problem for the selected block;
- create one alternative;
- test the replacement without global drift;
- keep or revert based on evidence;
- only then move to another block.

SAFE UNKNOWN: this workflow does not prove conversion lift, browser parity, or visual superiority without live review and measurement.
