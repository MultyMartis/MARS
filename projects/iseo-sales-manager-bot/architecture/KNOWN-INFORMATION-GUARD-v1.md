# KNOWN-INFORMATION GUARD v1

**Phase:** 3E.2 / **3E.2.1** (silent guard enforced)  
**Engine:** First Reply Engine v2.1 (`sm-reply-v2.1`) + Human Reply Style `sm-human-v1.0`  
**Implementation:** `applyKnownInformationGuard()` in `first-reply-engine-v2.mjs`

## Rule

Before rendering each candidate question, suppress it if the requested fact is already present in the Lead Semantic Model.

## Required suppressions

| Condition | Reason code |
|-----------|-------------|
| `website_state=provided` and question asks for site URL | `suppress_ask_website_provided` |
| `website_state=explicitly_absent` and question asks for current-site URL | `suppress_ask_website_absent` |
| Telegram/messenger known | `suppress_ask_telegram_known` |
| Phone known | `suppress_ask_phone_known` |
| Email known | `suppress_ask_email_known` |
| Meaningful task known + generic “что требуется?” | `suppress_ask_generic_task_known` |
| Region already in comment | `suppress_ask_region_known` |
| Resolved service known + “какая услуга?” | `suppress_ask_service_known` |

## Matching discipline

Website suppression matches **URL/address asks** only (e.g. «пришлите адрес сайта»), not every mention of the word «сайт» inside a legitimate clarification (e.g. «тип сайта», «проблема на сайте»).

## Silent guard — no customer narration (3E.2.1)

When a question is suppressed, the engine **must not** insert explanatory text such as «адрес уже указан» or «мы учли ваш комментарий». The customer sees only natural acknowledgement and remaining questions.

Violations are caught by the quality linter → `first_reply_ready=false`. See [HUMAN-REPLY-STYLE-v1.md](HUMAN-REPLY-STYLE-v1.md) forbidden phrases and [FIRST-REPLY-QUALITY-LINTER-v1.md](FIRST-REPLY-QUALITY-LINTER-v1.md).

Theme-aware suppression (Phase 3E.2.1):

| Condition | Reason code |
|-----------|-------------|
| `meaningful_theme=conversion_cart` + generic audit page-priority ask | `suppress_generic_audit_for_cart_theme` |

## Notes

- Source-page / form context alone is **not** treated as customer-confirmed task detail.
- Development + SEO must acknowledge both stages; do not ask for a current-site URL.
- Suppressed codes are stored in `first_reply_reason_codes` for diagnostics (not shown to customer).
