# Source/Runtime Diff Inventory — pre-reconcile (V9-06E58)

## Theme product files
| Rel | Classification | Src SHA256 | Rt SHA256 |
|-----|----------------|------------|-----------|
| assets/css/v9-style.css | operator-owned manual edit (runtime authority) | 2F7CC5ACE7E6718ADE81B9871FBE73B62D2D0D3AE5B5C1818E2F9266D374793E | 307A111EB229BA16C8A388C8A83B18C257C80AE57648E1601C2FA0EBF1851E04 |

Operator CSS delta themes: spacing token swaps (--pad-gap-line → --pad-gap), accent color on home articles link, related body spacing.

## Plugin
Exact product-file parity (0 content diffs).

## ACF JSON
- Common files: hash match.
- Source-only filesystem JSON (12 files not copied into runtime acf-json): retained accepted source authority; not operator CSS; do not delete.
- No unexplained product drift requiring promote besides v9-style.css.

## Templates
No template content hash diffs between source and runtime themes at backup time.
