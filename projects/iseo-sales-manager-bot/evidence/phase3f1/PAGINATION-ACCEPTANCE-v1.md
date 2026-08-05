# PAGINATION ACCEPTANCE v1

**Function:** `paginatePending(view, pageRaw, pageSize)` in `implementation/runtime-libs/pending-leads-lib.mjs`.

## Rules

- Default page size: **5** (`DEFAULT_PAGE_SIZE`); maximum: **10** (`MAX_PAGE_SIZE`).
- `pageSize` is clamped into `[1, 10]`.
- `page` is parsed as an integer; non-finite or `<1` values fall back to page `1`.
- A page number beyond the last available page is clamped to the last page (`pageCount`), never an empty/error result.
- `startOrdinal` gives the 1-based ordinal of the first item on the page for correct numbering in `/pending_leads` output across pages.

## Cases proven

| Case | Input | Expected | Result |
|---|---|---|---|
| Page 1 default | `paginatePending(view, 1, 5)` | ≤5 items, `page=1` | PASS (#11) |
| Later page, custom size | `paginatePending(view, 2, 2)` | `page=2`, `startOrdinal=3` | PASS (#12) |
| Invalid/out-of-range page | `paginatePending(view, 999, 5)` | clamped to `pageCount` | PASS (#13) |
| Argument parsing | `parsePendingLeadsArgs(['2'])` | `page=2` | PASS (X7) |

No error state is surfaced to the manager for an out-of-range page — pagination degrades gracefully to the last valid page rather than failing the command.

## Harness coverage

Checks 11–13, X7 in `implementation/harness/phase3f1-harness.mjs`.

*Related: [PENDING-LIST-ACCEPTANCE-v1.md](PENDING-LIST-ACCEPTANCE-v1.md).*
