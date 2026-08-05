# LIVE FIRST REPLY ACCEPTANCE v1 — Phase 3E.2

**Status:** paced synthetic fixtures A–H delivered for operator copy review  
**Operator visual copy acceptance:** **PENDING**  
**Engine:** `sm-reply-v2.0` · **Card:** `sm-msg-v2.4` · **Parser:** `sm-parser-v3.3`

Sanitized machine packet: [LIVE-FIRST-REPLY-OPERATOR-COMPARISON.json](LIVE-FIRST-REPLY-OPERATOR-COMPARISON.json)

## Contour

| Item | Value |
|------|-------|
| Operational.dev | `xSnXPy8cEHoZw6xG` active, 45 nodes |
| Admin.dev | `wLrLp4WQHm1VJmxz` active, 59 nodes (untouched) |
| Sales-Manager-v2 | `h8I2Tl2yl4uzhUnB` inactive |
| AI / OpenRouter | OFF |
| Gmail intake | exactly one |
| Eligible recipients | 2 |

## Case matrix

| Case | website_state | service | replyReady | mode | sendOk | deliveries | dup |
|------|---------------|---------|------------|------|--------|------------|-----|
| A | provided | Audit | true | normal | 2 | 2 | 0 |
| B | provided | Audit | true | normal | 2 | 2 | 0 |
| C | explicitly_absent | WebsiteDevelopment | true | normal | 2 | 2 | 0 |
| D | explicitly_absent | WebsiteDevelopmentSEO | true | normal | 2 | 2 | 0 |
| E | provided | SEO | true | normal | 2 | 2 | 0 |
| F | alternative_contact | NeedsClarification | true | normal | 2 | 2 | 0 |
| G | provided | Audit | false | contact_suppressed | 2 | 2 | 0 |
| H | provided | SEO | false | test_suppressed | 2 | 0* | 0 |

\* Case H: Telegram `sendOk=2` and suppression verified; Sheets `LEAD_DELIVERIES`/`LEAD_EVENTS` rate-limited after paced A–G wave.

## Operator must confirm

- reply sounds natural and acknowledges the real task  
- no known data re-asked  
- no irrelevant questions  
- development vs SEO cases differ  
- alternative contact handled correctly  
- damaged contact not send-ready  
- test lead has no real-client draft  
- copy block convenient  

**Do not claim Phase 3E.2 COMPLETE until this visual acceptance.**

## Safety

AI calls=0 · client auto-messages=0 · workflows created=0 · access changes=0 · reminder implementation=0 · historical bulk reply regen=0 · real-client tests=0 · duplicate deliveries on accepted A–G=0
