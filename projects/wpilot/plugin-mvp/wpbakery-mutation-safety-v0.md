# WPilot WPBakery Mutation Safety v0

**Status:** CORE / PLANNED / DEV-ONLY.
**Scope:** WPBakery/The7 mutation safety constraints for Phase 2 exact replacement.

This document defines what future WPilot mutation may and may not touch. It does not implement mutation or claim full WPBakery parsing.

## Safety Philosophy

WPBakery content is structure-bearing text. A small text edit can corrupt layout if it touches shortcode syntax, attributes, raw HTML, encoded blocks, or nested boundaries.

The MVP must refuse unless the target is plainly safe.

SAFE UNKNOWN is a refusal state.

## Allowed

**CORE / PLANNED:** plain text replacement inside safe content zones only.

Allowed when all are true:

- Target is inside page `post_content`.
- Target appears exactly once.
- Target is plain human-readable text.
- Target is inside a supported content zone, usually inner content of `vc_column_text`.
- Target does not overlap shortcode syntax.
- Target does not overlap HTML tag syntax.
- Target does not overlap encoded content.
- Replacement is also plain deterministic text.
- Shortcode boundary summary remains stable before and after candidate replacement.

## Forbidden

**EXCLUDED:** the MVP must refuse:

- Shortcode name changes.
- Shortcode attribute mutation.
- Nested structure rewrite.
- `vc_raw_html` mutation.
- Shortcode rebalancing.
- HTML structure rewriting.
- Script/style mutation.
- Encoded block mutation.
- Layout rewrite.
- Element insertion or deletion.
- New shortcode creation.
- Closing shortcode repair.
- Theme wrapper mutation.
- Mutation outside approved content field.

## Shortcode Name Changes

Forbidden examples:

- Changing `vc_row`.
- Changing `vc_column`.
- Changing `vc_column_text`.
- Changing any shortcode tag name.

Reason: shortcode names define builder structure. The MVP is not a builder transformer.

## Attribute Mutation

Forbidden examples:

- Editing values inside `[vc_row ...]`.
- Changing class names, IDs, widths, responsive settings, animation settings, colors, URLs, or shortcode parameters.
- Adding or removing attributes.

Reason: attributes can carry layout, rendering, script, tracking, and theme behavior.

## Nested Structure Rewrite

Forbidden examples:

- Moving content between nested shortcodes.
- Reordering shortcodes.
- Adding or removing nested nodes.
- Editing text that spans more than one structural node.

Reason: nested builder structures require full semantic parsing, which is outside MVP.

## `vc_raw_html` Mutation

`vc_raw_html` is forbidden for MVP mutation.

Refuse even when visible text appears simple because raw HTML may be encoded, escaped, script-bearing, or structurally sensitive.

## Shortcode Rebalancing

The plugin must not:

- Add missing closing shortcodes.
- Remove extra shortcodes.
- Rebalance nested structures.
- Repair malformed builder content.

Malformed content is a refusal condition and manual review item.

## HTML Structure Rewriting

The MVP must not rewrite:

- Tag names.
- Attributes.
- Links.
- Classes.
- Inline styles.
- HTML nesting.
- Forms.
- Embedded widgets.

Plain text inside a clearly safe text zone may be eligible only when it does not touch tag syntax.

## Script/Style Mutation

The MVP must refuse matches inside:

- `<script>` blocks.
- `<style>` blocks.
- Inline event handlers.
- CSS declarations.
- JavaScript snippets.
- Tracking snippets.

No automatic sanitization or repair is allowed.

## Encoded Block Mutation

The MVP must refuse:

- Base64-like content.
- URL-encoded builder payloads.
- JSON-in-shortcode attributes.
- Escaped HTML blocks that cannot be classified.
- Any content requiring decoding before safe matching.

## Safe Zone Validation

Validation should produce:

- zone classification
- shortcode boundary summary
- match span
- match count
- forbidden-zone flag
- SAFE UNKNOWN flag

Execution must re-run the same validation against current content before mutation.

## Safe Refusal Philosophy

When classification is uncertain, refuse with a deterministic code and operator-readable reason.

The plugin must not:

- Guess the intended zone.
- Use rendered frontend position to bypass stored-content ambiguity.
- Ask AI to infer safety.
- Mutate then inspect.
- Hide unsafe-zone refusal behind generic failure.

## Post-write Structure Check

After a future write, the plugin must verify:

- shortcode names sequence is unchanged
- shortcode boundary count is unchanged
- nesting summary is unchanged where tracked
- no new unsupported shortcode-like syntax was introduced
- replacement occurred exactly once

If verification fails after mutation, rollback handling and manual review are required.

## SAFE UNKNOWN

- Full WPBakery grammar.
- The7-specific wrapper semantics.
- Encoded `vc_raw_html` internals.
- Mixed HTML and shortcode edge cases.
- Third-party shortcode behavior.

