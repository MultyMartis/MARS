# Search PPC semantic curation standard v1

**Implementation:** `semantic-classification-controls.mjs`, `contracts/search-ppc-regression-corpus-v1.json`

## Intent classes

- Buyer service order (`нужен`, `найти`, `ищу`)
- Commercial price (`стоимость`, `цена`, `сколько стоит`) — **not** auto-reject
- Employment / career — reject or HOLD
- Education / courses — reject
- Tutorial-only — reject
- Download/piracy — reject
- Foreign market — reject (Russia-only scope)

## Geo routing

| Pattern | Routing |
|---------|---------|
| Новосибирск | LOCAL_ONLY |
| Other Russian cities | REMOTE_ONLY |
| Минск, Алматы, etc. | REJECT_RUSSIA_ONLY_SCOPE |

## Service-family routing

CA-01 programmer search, CA-02 support, CA-03 modification, CA-04 integrations, CA-05 Honest Sign — see regression corpus examples.

## Operator review required

Ambiguous «как» queries, short role phrases, brand ambiguity, document commercial ambiguity.

## Severity

- **HARD_FAIL** — automation may reject
- **WARNING** — flag for review
- **OPERATOR_REVIEW** — human decision mandatory

## Lifecycle

RAW → NORMALIZED → CLASSIFIED → HOLD_RESOLVED → OPERATOR_SEMANTIC_APPROVED → AUTHORITY_FROZEN (see `semantic-lifecycle.mjs`)
