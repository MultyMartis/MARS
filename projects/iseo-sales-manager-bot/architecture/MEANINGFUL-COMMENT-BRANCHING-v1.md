# MEANINGFUL COMMENT BRANCHING v1

**Product:** i-SEO Sales Manager Bot  
**Phase:** 3E.2.1  
**Engine:** First Reply Engine v2.1 (`sm-reply-v2.1`)  
**Implementation:** `detectMeaningfulTheme()` in `first-reply-engine-v2.mjs`  
**AI:** OFF — **deterministic keyword rules only**; no NLP / no model calls

---

## Purpose

When the customer comment carries real task signal beyond the form page title, the first reply must **change** — different acknowledgement lines and different follow-up questions. A meaningful comment must not receive the same generic audit questionnaire as a one-word «seo» or «нужно проверить сайт».

**Invariant:** theme detection is read-only classification; it does not mutate Lead Semantic Model fields.

---

## Theme codes

| Code | Typical signal (keywords / context) | Reply impact |
|------|-------------------------------------|--------------|
| `conversion_cart` | конверси + корзин/checkout/оформлен | Cart-specific ack + when/changes/analytics; suppress generic audit page-priority asks |
| `traffic_decline` | падает трафик, снижение трафика | Traffic-decline ack + when/changes/analytics |
| `rankings_visibility` | позици, видимост, ранжир, выдач | Rankings ack + queries/when |
| `technical_errors` | ошибк, не работает, баг, 404, 500 | Technical ack + what/where |
| `indexing` | индекс | Indexing-oriented follow-ups (within audit branch) |
| `site_redesign_migration` | редизайн, миграц, переезд | Migration/redesign acknowledgement |
| `ads_no_leads` | реклам/директ + нет заяв/лид | Ads-no-leads branch (Direct / mixed contexts) |
| `need_new_website` | новый сайт, хочу сайт, разработ + `WebsiteDevelopment` | Dev questions; never ask existing-site URL when absent |
| `website_plus_seo` | site + seo/продвиж or `WebsiteDevelopmentSEO` | Combined dev+SEO ack + combo questions |
| `ai_geo_visibility` | ai, geo, нейросет, chatgpt | AISearch-oriented questions |
| `unclear_request` | comment passes length/meaning bar but no keyword class | Service-aware generic clarification |
| `vague_service` | empty, ultra-short, or boilerplate («seo», «аудит», «нужно проверить сайт») | Natural focus question instead of pretending specificity |

---

## Meaningful comment must change reply content

Harness contract (H24, H25):

- **H16 vs H15:** same Audit form + site provided; H16 comment mentions cart conversion → theme `conversion_cart`, cart questions, **no** «приоритетные страницы»
- **H25:** cart theme must not fall back to generic audit page-priority wording even when `resolved_service=Audit`

If theme is `vague_service`, the engine uses the natural focus prompt — not cart/traffic/ranking-specific lines.

---

## Deterministic keyword rules (no AI)

Evaluation order matters — first match wins (see runtime lib):

1. `conversion_cart` — `/конверси/` (+ optional cart/checkout tokens)
2. `traffic_decline` — падение/снижение трафика patterns
3. `rankings_visibility` — позиции/видимость/ранжирование
4. `technical_errors` — ошибки/404/500/«не работает»
5. `indexing` — `/индекс/`
6. `site_redesign_migration` — редизайн/миграция/переезд
7. `ads_no_leads` — ads + no leads composite pattern
8. `website_plus_seo` — service `WebsiteDevelopmentSEO` or site+seo in comment
9. `need_new_website` — service `WebsiteDevelopment` or new-site phrases
10. `ai_geo_visibility` — ai/geo/neural patterns
11. `vague_service` — `isVagueTask()` true
12. `unclear_request` — `hasMeaningfulComment()` true but no earlier class
13. fallback → `vague_service`

Helper gates:

- `hasMeaningfulComment()` — min length 8; rejects single-token «seo», «аудит», «в тг»
- `isVagueTask()` — boilerplate audit/SEO phrases; short Audit comments without problem keywords

---

## Integration with known-info guard

Theme affects suppression, not customer-visible narration:

- `conversion_cart` → suppress generic audit questions (`suppress_generic_audit_for_cart_theme`)
- Website/phone/email/Telegram suppressions remain independent of theme

---

## Stored field

`meaningful_theme` — persisted on CLEAN / processor output for card diagnostics and linter cross-checks. **Not** shown as raw enum to customer; manager card may use human labels via formatter.

---

## Related

- [HUMAN-REPLY-STYLE-v1.md](HUMAN-REPLY-STYLE-v1.md)
- [FIRST-REPLY-QUALITY-LINTER-v1.md](FIRST-REPLY-QUALITY-LINTER-v1.md) — cart theme acknowledgement checks
- [LEAD-SEMANTIC-MODEL-v1.md](LEAD-SEMANTIC-MODEL-v1.md) — `comment_normalized`, `resolved_service`
- Research: [COMMENT-BOUNDARY-REQUIREMENTS-v1.md](../research/parser-3.3/COMMENT-BOUNDARY-REQUIREMENTS-v1.md)
