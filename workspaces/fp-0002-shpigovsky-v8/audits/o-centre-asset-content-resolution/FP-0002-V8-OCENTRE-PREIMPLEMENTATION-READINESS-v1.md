# FP-0002 V8 O-Centre Preimplementation Readiness v1

**Task:** FP-0002 V8 O-Centre Asset + Content Resolution  
**HEAD:** `508837a02658e357ce18dca777a46231d2575b25`

| Gate | Before | After | Evidence | Missing |
|---|---|---|---|---|
| Design | PASS_WITH_KNOWN_GAPS | **PASS** | Spig_v1.2 node map; 13 desktop sections mapped | — |
| Content | PASS_WITH_KNOWN_GAPS | **PASS_WITH_KNOWN_GAPS** | Content pack JSON | Founder quote; program Lorem; steps absent |
| Assets | PASS_WITH_KNOWN_GAPS | **PASS_WITH_KNOWN_GAPS** | Hero exported; 22 photos pending | Infrastructure photo export |
| Reuse | PASS | **PASS** | FAQ→final-form; composition updated | — |
| Responsive | PASS | **PASS** | Mobile frames mapped | Comfort mobile photos |
| Accessibility | PASS_WITH_KNOWN_GAPS | PASS_WITH_KNOWN_GAPS | Subnav labels confirmed | Alt text for pending photos |
| Implementation | PASS (charter) | **NOT AUTHORIZED** | Blockers below | See critical |

## Overall

**NOT READY** for full implementation prompt.

## Critical blockers

1. OC-B05 / BLK-018 steps — absent from canonical Figma O-Centre page  
2. Founder quote body — Lorem ipsum in Figma (`1:2301`)  
3. 22 infrastructure photos — not yet exported to `src/img/content/o-centre/`

## Non-critical gaps

- Program approach card Lorem ipsum placeholders  
- Meta title not extracted from Figma  
- Anchor IDs proposed but not wired  
- Frame `2 - Дом - вступление` image-only section semantics  

## Recommended next task

**`READY_FOR_FP0002_V8_OCENTRE_TARGETED_ASSET_EXPORT`**

Sequence:

1. Bulk export `преимущества` / mobile comfort images with hash validation  
2. Operator supplies founder quote canonical text (or approved alternate source)  
3. Confirm removal of BLK-018 steps from scope **or** supply copy source  
4. Then narrow implementation prompt without steps block / with resolved assets

## Full implementation prompt allowed?

**No** — hero resolved but BLK-037/038 assets pending, steps unresolved, founder quote blocked.
