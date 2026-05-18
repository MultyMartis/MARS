# WPilot WPBakery Safe Edit Pipeline v0

**Status:** CORE / PLANNED / DEV-ONLY.
**Scope:** shortcode-aware safety model for first installable plugin MVP.

This pipeline converts prior WPBakery DEV evidence into a conservative MVP editing contract. It does not claim full WPBakery rendering, full theme compatibility, or universal shortcode support.

## Safety Principle

The MVP should prefer safe refusal over dangerous modification.

Allowed edits are text-only replacements inside clearly classified content zones. The plugin must not rewrite shortcode structure, attributes, layout, raw HTML blocks, JavaScript, CSS, or encoded fragments.

## Shortcode-Aware Boundaries

The parser should detect common WPBakery shortcodes:

- `vc_row`
- `vc_column`
- `vc_column_text`
- `vc_raw_html`

The parser should identify:

- Opening shortcode boundaries.
- Closing shortcode boundaries.
- Attribute areas.
- Inner content areas.
- Nesting depth.
- Raw HTML or encoded content areas where possible.

The parser may return **SAFE UNKNOWN** for unsupported shortcodes or unclear structures.

## Allowed Edit Zones

**CORE / PLANNED:** text-only replacement may be allowed when all conditions are true:

- Target is inside plain text content.
- Target is inside a supported content area, usually `vc_column_text`.
- Target does not overlap shortcode syntax.
- Target does not overlap shortcode attributes.
- Target does not overlap HTML tag syntax.
- Target appears exactly once.
- Replacement text does not introduce shortcode-like syntax.
- Replacement text does not introduce script, style, iframe, form, or PHP-like content.
- The structural map before and after replacement remains equivalent at shortcode-boundary level.

## Forbidden Edit Zones

**EXCLUDED:** the MVP must refuse edits in:

- Shortcode names.
- Shortcode attributes.
- Opening or closing shortcode brackets.
- `vc_raw_html` content unless separately classified as safe plain text, which is **SAFE UNKNOWN** for MVP.
- Encoded content.
- Inline scripts.
- Inline styles.
- HTML tag names and attributes.
- Theme-generated wrappers.
- Unknown builder shortcodes.
- Plugin/theme/core files.
- Any content outside the approved page/post content field.

## Nested Shortcode Handling

Nested shortcode content is allowed only when the parser can produce a stable boundary map.

Rules:

- Track nesting depth.
- Keep opening and closing shortcode counts stable.
- Keep shortcode order stable.
- Keep parent/child relationships stable.
- Refuse replacement if target spans more than one node.
- Refuse replacement if nested boundaries are malformed or ambiguous.

The MVP does not need to understand every WPBakery semantic. It only needs enough structural awareness to avoid corrupting shortcode boundaries.

## Text-Only Replacement Rules

The MVP replacement is accepted only when:

- Match mode is exact string match.
- Match count is exactly one.
- Replacement count is exactly one.
- Before text and replacement text are provided as plain text.
- Replacement does not request regex, wildcard, fuzzy match, translation, summarization, or layout rewrite.
- Replacement does not include PHP tags, `<script>`, `<style>`, iframe, shortcode brackets, or other high-risk markup.
- The operation has a backup and approval reference.

## Structure Integrity Checks

Before and after replacement, compare:

- Total shortcode boundary count.
- Shortcode names by sequence.
- Nesting depth sequence.
- Opening/closing pair consistency.
- Target node identity where available.
- Content checksum before and after.

The post-write map must be valid enough to confirm the replacement did not corrupt known shortcode boundaries.

## Malformed Shortcode Detection

The parser should report malformed or unsafe structure when it sees:

- Unbalanced `[` or `]` shortcode-like syntax.
- Missing closing shortcode where expected.
- Closing shortcode without known opener.
- Shortcode boundaries inside the target replacement span.
- Attribute-like syntax broken by replacement target.
- Unsupported escaping or encoding.
- Deep nesting beyond configured MVP limit.
- Mixed raw HTML and shortcode content that cannot be classified.

Malformed structure is not automatically repaired by the MVP.

## Replacement Refusal Conditions

The plugin must refuse replacement if:

- Target text appears zero times.
- Target text appears more than once.
- Target appears in multiple structural zones.
- Target crosses shortcode, HTML, or encoded boundaries.
- Target is inside forbidden zone.
- Parser result is **SAFE UNKNOWN** for the target zone.
- Replacement text contains disallowed markup or shortcode-like syntax.
- Backup is missing or failed.
- Approval reference is missing for execute mode.
- Expected checksum does not match current content.
- Post-replacement structure check cannot be performed.

## Output Of The Pipeline

Dry validation should return:

- Operation status: accepted, rejected, or SAFE UNKNOWN.
- Target page ID.
- Match count.
- Target zone type.
- Shortcode map summary.
- Refusal reason where applicable.
- Backup requirement.
- Manual approval reminder.

Execution should return:

- Operation ID.
- Backup ID.
- Replacement count.
- Before checksum.
- After checksum.
- Post-write structure status.
- Manual frontend verification reminder.

## SAFE UNKNOWN

- Full WPBakery shortcode grammar.
- Theme-specific shortcode wrappers.
- The7-specific builder integrations.
- Encoded `vc_raw_html` semantics.
- Mixed shortcode and HTML edge cases.
- Content generated outside `post_content`.

