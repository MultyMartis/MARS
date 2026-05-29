# SAFE UNKNOWN — triumph-manipulyator-zakaz-pack-v1

Facts not provable from repo snapshot without operator / production verification.

| Field | Unknown | Would verify |
|-------|---------|--------------|
| Live URL parity | Does production match `dist/index.html`? | HTTP 200 + visual diff |
| Form POST | Is `data-form-endpoint` live or mock? | Network tab on prod |
| SLA «От 30 минут» | Operational truth | Operator dispatch policy |
| Conversion split | Call vs form performance | Analytics (if exists) |
| Mobile fold | Form below specs on stack — friction level | Device QA matrix |
| Scroll depth to trust | Do users reach reviews? | Analytics / session replay |
| `intent_continuity_ack` | Process only — landing may be ready before ack | Operator PPC review |
| Route registry | Is master hot registered in landing-route-registry? | Registry file read |
| Yandex QS impact | H1 mismatch A1 hypothesis | Ads platform data |
| Hero notice visibility | Present in HTML — contrast/readability on mobile | Visual QA |
| NAP / hours | Footer final lock | Operator business data |
| Indexing | robots noindex until operator opens | robots + Search Console |

## Security / claims

- No invented fleet, prices, or review counts in this pack
- Review sources (Яндекс, Авито) referenced in trust partial — **live link validity UNKNOWN**

## Pack honesty

This pack describes **as-built v5 in repo**, not a hypothetical redesign. Where calibration docs disagree with current partials (e.g. D1 notice), **as-built partial wins** until calibration docs are updated.
