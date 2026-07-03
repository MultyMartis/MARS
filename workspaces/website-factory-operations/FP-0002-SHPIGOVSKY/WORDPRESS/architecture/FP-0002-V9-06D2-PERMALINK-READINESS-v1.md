# FP-0002 V9-06D.2 Permalink Readiness v1

**Status:** PASS
**Rewrite flush:** NOT PERFORMED
**HTTP route checks:** not performed; readiness is based on `get_permalink()` generation per contract.

| Registry ID | Expected path | Generated path | HTTP checked | Result |
|---|---|---|---|---|
| SVC-ZAVISIMOSTI | /uslugi/zavisimosti/ | /uslugi/zavisimosti/ | false | PASS |
| SVC-ALKOGOL | /uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/ | /uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/ | false | PASS |
| SVC-PROFILAKTIKA | /uslugi/zavisimosti/profilakticheskiy-analiz/ | /uslugi/zavisimosti/profilakticheskiy-analiz/ | false | PASS |
| SVC-SPECIALISTAM-ZAV | /uslugi/zavisimosti/specialistam/ | /uslugi/zavisimosti/specialistam/ | false | PASS |
| SVC-PSYCH | /uslugi/psihicheskoe-zdorovie/ | /uslugi/psihicheskoe-zdorovie/ | false | PASS |
| SVC-DEPRESSIYA | /uslugi/psihicheskoe-zdorovie/depressiya/ | /uslugi/psihicheskoe-zdorovie/depressiya/ | false | PASS |
| SVC-PTRS | /uslugi/psihicheskoe-zdorovie/ptrs/ | /uslugi/psihicheskoe-zdorovie/ptrs/ | false | PASS |
| SVC-VYGORANIE | /uslugi/psihicheskoe-zdorovie/emocionalnoe-vygoranie/ | /uslugi/psihicheskoe-zdorovie/emocionalnoe-vygoranie/ | false | PASS |
| SVC-TREVOGA | /uslugi/psihicheskoe-zdorovie/trevozhnye-rasstroystva/ | /uslugi/psihicheskoe-zdorovie/trevozhnye-rasstroystva/ | false | PASS |
| SVC-SON | /uslugi/psihicheskoe-zdorovie/rasstroystva-sna/ | /uslugi/psihicheskoe-zdorovie/rasstroystva-sna/ | false | PASS |
| SVC-TRAVMA | /uslugi/psihicheskoe-zdorovie/travma/ | /uslugi/psihicheskoe-zdorovie/travma/ | false | PASS |
| SVC-RPP | /uslugi/rasstroystva-pischevogo-povedeniya/ | /uslugi/rasstroystva-pischevogo-povedeniya/ | false | PASS |
| SVC-ANOREKSIYA | /uslugi/rasstroystva-pischevogo-povedeniya/anoreksiya/ | /uslugi/rasstroystva-pischevogo-povedeniya/anoreksiya/ | false | PASS |
| SVC-BULIMIYA | /uslugi/rasstroystva-pischevogo-povedeniya/nervnaya-bulimiya/ | /uslugi/rasstroystva-pischevogo-povedeniya/nervnaya-bulimiya/ | false | PASS |
| SVC-KOMPULSIV | /uslugi/rasstroystva-pischevogo-povedeniya/kompulsivnoe-pereedanie/ | /uslugi/rasstroystva-pischevogo-povedeniya/kompulsivnoe-pereedanie/ | false | PASS |

## Boundary

- Services Hub remains native Page-owned at `/uslugi/`.
- Service CPT archive remains disabled.
- Legacy `/specyalisty/` was not created by V9-06D.2; pre-existing Page ID 10 remains unchanged and redirect is deferred.
- No redirects were created.
