# MAIN-PREFLIGHT — D6E2B

| Check | Result |
|-------|--------|
| cwd | `X:\AI MARS` |
| Volume X: label | AI WS |
| Branch | `mars/canonical-post-recovery` |
| MAIN_HEAD_A | `929cda7b8fd41544df5f643896eb124d6074aa83` |
| origin/mars/canonical-post-recovery | `812d15154d033698295b7c80d5bd4355d0ea1b64` |
| ahead/behind (origin...HEAD) | 258 ahead / 86 behind (foreign divergence; not reconciled) |
| Staged path cardinality | 299 |
| Staged diff stat | 299 files, +74 / -17202 (pre-existing foreign staged WIP including inverse-cache Client Ops deletes) |
| Index tree hash (`git write-tree`) | `ec342ee8c7dc7f55be3ab49014ba7fddbbfb30a0` |
| Foreign WIP | present (dirty MAIN; staged + unstaged + untracked outside D6E/D6E2 allowlist) |
| Task MAIN index mutations | **0** |
| Pre-existing staged state blocker? | **NO** (per D6E2B charter — do not clean) |

**Token context:** MAIN index must remain untouched by D6E2B (`MAIN_INDEX_UNTOUCHED_BY_D6E2B`).
