# FP-0002 — Services V2 Program Build Validation v1

| Check | Result |
| ----- | ------ |
| Build command | `npm run build` |
| Exit code | **0** |
| EBUSY | none (server left running on 4174) |
| Preview | `http://127.0.0.1:4174/uslugi-v2.html` |
| Program root in dist | yes (`#services-program`) |
| Items | 4 |
| Lorem in program item 02 | yes |
| Modal hook | yes |
| Probe `overflowX` | false |

Compiled probe: `screenshots/compiled-content-probe.json`

**Verdict:** **PASS**
