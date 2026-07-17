# Tail Ledger — FP-0002 V9 Stable v1

| Tail | Previous status | Final disposition | Release impact | Future action |
|------|-----------------|-------------------|----------------|---------------|
| Operator visual acceptance (CSS/Search/404/Blog/Reviews/O-centre/Contacts/Services/Home/Specialists/responsive) | Pending review loops E59–E62E | CLOSED_FOR_STABLE_V1 | Operator requested stable closeout; result accepted | None for Stable v1 |
| Latest operator CSS (`v9-style`, `fp02-search`) + slider JS defaults | Runtime-only drift after E62E-FIX01 | CLOSED_FOR_STABLE_V1 | Canonized into source | Preserve as visual canon |
| Demo Blog posts #1745–1754 | Open cleanup backlog | ACCEPTED_DEFERRED | Retained for local pagination demos | Mandatory cleanup before public launch |
| Demo Reviews (20 of 30 rows) | Open cleanup backlog | ACCEPTED_DEFERRED | Retained; stable `review_uid` preserved (30/30) | Replace/remove before public launch |
| Native WP Search baseline | Functional; advanced relevance open | CLOSED_FOR_STABLE_V1 (baseline) / ACCEPTED_DEFERRED (advanced) | Accepted functional baseline | Custom-field indexing / relevance later |
| SMTP / production mail | Local forms without SMTP (E56) | ACCEPTED_DEFERRED | MANDATORY PRE-PRODUCTION DEPLOYMENT TASK | Configure SMTP + recipient at launch |
| Local noindex policy | Intentional local | CLOSED_FOR_STABLE_V1 | Unchanged | Review production indexability at launch; Search `noindex,follow`; 404 `noindex,nofollow` |
| Source-only ACF JSON (8 groups) | Known E58+ inventory | ACCEPTED_DEFERRED (documented) | Not release-blocking; PHP registration owns groups | See ACF disposition doc |
| Public production deployment | Not started | OUT_OF_SCOPE | Stable v1 is local near-production only | Separate deployment charter |
| Advanced Search relevance | Not implemented | ACCEPTED_DEFERRED | None | Future development |
| Site Settings Admin IA Audit | Future task doc exists | ACCEPTED_DEFERRED | None | Future charter |
