# FP-0002 V8 O-Centre FAQ Decision v1

## Conflict

| Source | States |
|---|---|
| O-Centre charter OC-B13 | Reuse `faq.html` accordion (BLK-034) |
| Page inventory | FAQ accordion on About family |
| Spig_v1.2 desktop `1:2578` «faq» | Consultation form «Остались вопросы?» |
| Spig_v1.2 mobile `1:5918` «faq» | Same final-form pattern |

## Figma content (authoritative)

| Field | Value | Node |
|---|---|---|
| Heading | Остались вопросы? | 1:2581 |
| Subtext | Опишите вашу ситуацию в форме заявки… | 1:2582 |
| Fields | Ваш телефон / email / Опишите ситуацию | 1:2586–1:2589 |
| Legal | Отправляя форму, вы соглашаетесь… | 1:2592 |

**No** «Нас часто спрашивают» heading or accordion items found in O-Centre extract.

## Decision

| Field | Value |
|---|---|
| Include FAQ accordion | **No** |
| Include final consultation form | **Yes** |
| Position | After «Отзывы», before footer (order 12) |
| Content source | Spig_v1.2 nodes above |
| Canonical partial | **`final-form.html` / CF-009** — not `faq.html` |
| Item set | N/A (no accordion) |
| Content gap | None for form shell; form handler inherited |

## Rationale

Canonical Figma composition wins. Frame is misnamed `faq` but content matches site-wide final form pattern, not FAQ accordion.

## Charter impact

Update OC-B13 reuse from `faq.html` → `final-form.html` (CF-009). Record historical charter expectation without deletion.

## Result

**RESOLVED** — FAQ conflict closed.
