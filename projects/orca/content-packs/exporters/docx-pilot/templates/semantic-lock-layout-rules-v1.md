# Semantic Lock Layout Rules v1

## Global (cover)

Display `semantic_lock: ACTIVE (MODE 1)` when frontmatter `semantic_lock: active`.

## Per section

1. Subheading **Semantic lock state**
2. Shaded block `#EEEEEE` with lines prefixed `🔒`
3. If no per-section list in pack → single inherit line: *Active — inherit global MODE 1 locks from pack*

## Factory section (global)

Dedicated **Factory implementation notes** with MODE 1 callout box:

- Website Factory may NOT rewrite approved copy
- Presentation layer only
- Forbidden: paraphrase, invent fleet/pricing/stats, strip UNKNOWN

## Export footer row

Each section ends with metadata table row:

| label | value |
|-------|--------|
| semantic_lock | ACTIVE (MODE 1) |
| section_export | validated |

`validated` means structurally exported — **not** a runtime validation claim.
