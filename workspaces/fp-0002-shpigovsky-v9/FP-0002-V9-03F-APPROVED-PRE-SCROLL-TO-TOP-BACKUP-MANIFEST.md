# FP-0002 V9-03F Approved Pre-Scroll-to-Top Backup Manifest

**Phase:** V9-03G (mandatory pre-edit backup)  
**Created:** 2026-07-02  
**Operator state:** V9-03F Triumph modal runtime visually approved

## Archive

| Field | Value |
|-------|-------|
| ZIP path | `X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v9\v9-03g-scroll-to-top\snapshot-approved-v9-03f-before-scroll-to-top\FP-0002-V9-03F-OPERATOR-APPROVED-PRE-SCROLL-TO-TOP.zip` |
| SHA-256 | `6E5092D2FCCA79ADA16B78BB14934A5E03432EEE21CD43937FEDD515E887D106` |
| Size | 484,766,736 bytes |
| File count | 1938 |
| Route count | 31 |

## Snapshot root

`X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v9\v9-03g-scroll-to-top\snapshot-approved-v9-03f-before-scroll-to-top\`

## Preflight (recorded before edits)

| Check | Result |
|-------|--------|
| Drive | `X:` |
| Volume label | `AI WS` |
| Repository | `X:\AI MARS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD | `5e7c86db73398df6a01074a60af3afa796de41b3` |

## Pre-edit source key hashes

```
D6E0889D5BCFF3A4C00E49CB82B7E4C5B19E712B5EC725891B8D38F383345DFF  src/js/main.js
74071C47583A2C3ACAA4D99AD10E862935F627AD5137DF81644925CF891CF09F  src/scss/style.scss
D1FBC660C60911CFBA142B731CE219A20C4D19B961B044BFC14C1A43A14D9751  src/partials/layout/global-consultation-modal.html
11EA6249A507E0F465B88F2B1D9486E179D560063A6FF37D51EDF8076BF9D4A2  src/partials/layout/footer.html
481B963DA93DB5C1CA8D249762E3E43870B4C6232279441FE7E310A7CB7BC1AB  src/partials/layout/body-start.html
```

## Pre-edit dist asset hashes

Recorded in snapshot `hashes/dist-asset-hashes.txt` (pre-build V9-03F dist at backup time).

## Scope included

- Complete V9 workspace (excluding `node_modules`, caches)
- Generated `dist/`
- V9 tools and local documentation
- Package/build files
- Preflight git status/diff
- Process inventory

## Scope excluded

- `node_modules`
- Recursive Storage evidence
- V8 workspace
- Unrelated projects

## Restore guidance (operator-only)

**Target scope:** `X:\AI MARS\workspaces\fp-0002-shpigovsky-v9` only.

**Requires:**

1. Explicit operator approval
2. Exact target-path verification on `X:` / `AI WS`
3. Backup of any newer state before restore
4. Selective file restore — **no** broad overwrite
5. **No** `/MIR`, **no** `/PURGE`
6. **No** `git reset`, **no** `git clean`

**Forbidden:** restoring over V8, Triumph authority, or unrelated repo paths.

## Confirmation

Backup SHA-256 recorded **before** V9-03G source edits began.
