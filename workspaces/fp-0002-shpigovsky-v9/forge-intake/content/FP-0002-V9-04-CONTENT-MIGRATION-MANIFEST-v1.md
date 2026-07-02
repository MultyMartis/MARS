# FP-0002 V9-04 Content Migration Manifest v1

**Date:** 2026-07-02

| `/` | src/pages/index.html | page | TPL-FRONT-PAGE | CURRENT_DEMO_CONTENT | ready |
| `/uslugi/` | src/pages/uslugi-v2.html | page | TPL-SERVICES-HUB | CURRENT_DEMO_CONTENT | ready |
| `/uslugi/zavisimosti/` | src/pages/usluga-podrazdel-v1.html | page | TPL-SERVICE-SUBDIVISION | TEMPLATE_FIXTURE | ready |
| `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | src/pages/usluga-konechnaya-v1.html | page | TPL-SERVICE-LEAF | TEMPLATE_FIXTURE | ready |
| `/uslugi/zavisimosti/profilakticheskiy-analiz/` | src/pages/uslugi/zavisimosti/profilakticheskiy-analiz.html | page | TPL-SERVICE-LEAF | PLACEHOLDER_PENDING_CONTENT | blocked |
| `/uslugi/zavisimosti/specialistam/` | src/pages/uslugi/zavisimosti/specialistam.html | page | TPL-SERVICE-LEAF | PLACEHOLDER_PENDING_CONTENT | blocked |
| `/uslugi/psihicheskoe-zdorovie/` | src/pages/uslugi/psihicheskoe-zdorovie.html | page | TPL-SERVICE-SUBDIVISION | PLACEHOLDER_PENDING_CONTENT | blocked |
| `/uslugi/psihicheskoe-zdorovie/depressiya/` | src/pages/uslugi/psihicheskoe-zdorovie/depressiya.html | page | TPL-SERVICE-LEAF | PLACEHOLDER_PENDING_CONTENT | blocked |
| `/uslugi/psihicheskoe-zdorovie/ptrs/` | src/pages/uslugi/psihicheskoe-zdorovie/ptrs.html | page | TPL-SERVICE-LEAF | PLACEHOLDER_PENDING_CONTENT | blocked |
| `/uslugi/psihicheskoe-zdorovie/emocionalnoe-vygoranie/` | src/pages/uslugi/psihicheskoe-zdorovie/emocionalnoe-vygoranie.html | page | TPL-SERVICE-LEAF | PLACEHOLDER_PENDING_CONTENT | blocked |
| `/uslugi/psihicheskoe-zdorovie/trevozhnye-rasstroystva/` | src/pages/uslugi/psihicheskoe-zdorovie/trevozhnye-rasstroystva.html | page | TPL-SERVICE-LEAF | PLACEHOLDER_PENDING_CONTENT | blocked |
| `/uslugi/psihicheskoe-zdorovie/rasstroystva-sna/` | src/pages/uslugi/psihicheskoe-zdorovie/rasstroystva-sna.html | page | TPL-SERVICE-LEAF | PLACEHOLDER_PENDING_CONTENT | blocked |
| `/uslugi/psihicheskoe-zdorovie/travma/` | src/pages/uslugi/psihicheskoe-zdorovie/travma.html | page | TPL-SERVICE-LEAF | PLACEHOLDER_PENDING_CONTENT | blocked |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` | src/pages/uslugi/rasstroystva-pischevogo-povedeniya.html | page | TPL-SERVICE-SUBDIVISION | PLACEHOLDER_PENDING_CONTENT | blocked |
| `/uslugi/rasstroystva-pischevogo-povedeniya/anoreksiya/` | src/pages/uslugi/rasstroystva-pischevogo-povedeniya/anoreksiya.html | page | TPL-SERVICE-LEAF | PLACEHOLDER_PENDING_CONTENT | blocked |
| `/uslugi/rasstroystva-pischevogo-povedeniya/nervnaya-bulimiya/` | src/pages/uslugi/rasstroystva-pischevogo-povedeniya/nervnaya-bulimiya.html | page | TPL-SERVICE-LEAF | PLACEHOLDER_PENDING_CONTENT | blocked |
| `/uslugi/rasstroystva-pischevogo-povedeniya/kompulsivnoe-pereedanie/` | src/pages/uslugi/rasstroystva-pischevogo-povedeniya/kompulsivnoe-pereedanie.html | page | TPL-SERVICE-LEAF | PLACEHOLDER_PENDING_CONTENT | blocked |
| `/o-centre/` | src/pages/o-centre.html | page | TPL-INSTITUTIONAL | CURRENT_DEMO_CONTENT | ready |
| `/o-centre/o-nas/` | src/pages/o-centre/o-nas.html | page | TPL-INSTITUTIONAL | PLACEHOLDER_PENDING_CONTENT | blocked |
| `/o-centre/programma-lecheniya/` | src/pages/o-centre/programma-lecheniya.html | page | TPL-INSTITUTIONAL | PLACEHOLDER_PENDING_CONTENT | blocked |
| `/o-centre/galereya-o-dome/` | src/pages/o-centre/galereya-o-dome.html | page | TPL-INSTITUTIONAL | PLACEHOLDER_PENDING_CONTENT | blocked |
| `/o-centre/specialistam/` | src/pages/o-centre/specialistam.html | page | TPL-INSTITUTIONAL | PLACEHOLDER_PENDING_CONTENT | blocked |
| `/o-centre/rodstvennikam/` | src/pages/o-centre/rodstvennikam.html | page | TPL-INSTITUTIONAL | PLACEHOLDER_PENDING_CONTENT | blocked |
| `/otzyvy/` | src/pages/otzyvy.html | page | TPL-REVIEWS | CURRENT_DEMO_CONTENT | ready |
| `/blog/` | src/pages/blog.html | posts_page | TPL-BLOG-ARCHIVE | CURRENT_DEMO_CONTENT | ready |
| `/blog/nazvanie-stati/` | src/pages/blog/nazvanie-stati.html | post | TPL-BLOG-SINGLE | CURRENT_DEMO_CONTENT | ready |
| `/kontakty/` | src/pages/kontakty.html | page | TPL-CONTACTS | CURRENT_DEMO_CONTENT | ready |
| `/privacy-policy/` | src/pages/privacy-policy.html | page | TPL-LEGAL | LEGAL_DEMO_PENDING_OPERATOR_DATA | blocked |
| `/user-agreement/` | src/pages/user-agreement.html | page | TPL-LEGAL | LEGAL_DEMO_PENDING_OPERATOR_DATA | blocked |
| `/consent-personal-data/` | src/pages/consent-personal-data.html | page | TPL-LEGAL | LEGAL_DEMO_PENDING_OPERATOR_DATA | blocked |
| `/cookie-files-policy/` | src/pages/cookie-files-policy.html | page | TPL-LEGAL | LEGAL_DEMO_PENDING_OPERATOR_DATA | blocked |

Header: | Route | Source | WP object | Template | Content status | Blocker |

## Migration methods

- **Full pages:** manual + scripted HTML import into ACF where structured
- **Placeholders:** copy approved placeholder partial content
- **Legal:** import body partials with DEMO tokens flagged
- **Blog fixture:** single post migration from `blog/nazvanie-stati.html`
- **Globals:** extract from header/footer/contacts
