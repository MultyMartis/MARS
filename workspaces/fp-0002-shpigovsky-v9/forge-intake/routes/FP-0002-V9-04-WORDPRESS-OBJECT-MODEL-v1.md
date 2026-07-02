# FP-0002 V9-04 WordPress Object Model v1

**Date:** 2026-07-02

## Default principles

- **Pages** for all hierarchical service, institutional, contacts, legal, and placeholder routes.
- **Posts** + **Posts page** for blog archive and articles — **no CPT** unless operator later mandates reviews singles.
- No flexible-content page builder.
- Parent-child slugs mirror V9 manifest.

## Object summary

| Object type | Count | Routes |
|-------------|-------|--------|
| `page` | 29 | All except blog archive/single |
| `posts_page` + `home.php` | 1 | `/blog/` |
| `post` | 1+ | Fixture + future articles |

### `/`
- **post_type:** page
- **parent:** —
- **slug:** home
- **template:** TPL-FRONT-PAGE
- **editor:** ACF + native title
- **indexing:** intended index when launch-ready

### `/uslugi/`
- **post_type:** page
- **parent:** —
- **slug:** uslugi
- **template:** TPL-SERVICES-HUB
- **editor:** ACF + native title
- **indexing:** intended index when launch-ready

### `/uslugi/zavisimosti/`
- **post_type:** page
- **parent:** /uslugi/
- **slug:** uslugi/zavisimosti
- **template:** TPL-SERVICE-SUBDIVISION
- **editor:** ACF + native title
- **indexing:** intended index when launch-ready

### `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/`
- **post_type:** page
- **parent:** /uslugi/zavisimosti/
- **slug:** uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti
- **template:** TPL-SERVICE-LEAF
- **editor:** ACF + native title
- **indexing:** intended index when launch-ready

### `/uslugi/zavisimosti/profilakticheskiy-analiz/`
- **post_type:** page
- **parent:** /uslugi/zavisimosti/
- **slug:** uslugi/zavisimosti/profilakticheskiy-analiz
- **template:** TPL-SERVICE-LEAF
- **editor:** placeholder template + future ACF
- **indexing:** blocked until content/legal approval

### `/uslugi/zavisimosti/specialistam/`
- **post_type:** page
- **parent:** /uslugi/zavisimosti/
- **slug:** uslugi/zavisimosti/specialistam
- **template:** TPL-SERVICE-LEAF
- **editor:** placeholder template + future ACF
- **indexing:** blocked until content/legal approval

### `/uslugi/psihicheskoe-zdorovie/`
- **post_type:** page
- **parent:** /uslugi/
- **slug:** uslugi/psihicheskoe-zdorovie
- **template:** TPL-SERVICE-SUBDIVISION
- **editor:** placeholder template + future ACF
- **indexing:** blocked until content/legal approval

### `/uslugi/psihicheskoe-zdorovie/depressiya/`
- **post_type:** page
- **parent:** /uslugi/psihicheskoe-zdorovie/
- **slug:** uslugi/psihicheskoe-zdorovie/depressiya
- **template:** TPL-SERVICE-LEAF
- **editor:** placeholder template + future ACF
- **indexing:** blocked until content/legal approval

### `/uslugi/psihicheskoe-zdorovie/ptrs/`
- **post_type:** page
- **parent:** /uslugi/psihicheskoe-zdorovie/
- **slug:** uslugi/psihicheskoe-zdorovie/ptrs
- **template:** TPL-SERVICE-LEAF
- **editor:** placeholder template + future ACF
- **indexing:** blocked until content/legal approval

### `/uslugi/psihicheskoe-zdorovie/emocionalnoe-vygoranie/`
- **post_type:** page
- **parent:** /uslugi/psihicheskoe-zdorovie/
- **slug:** uslugi/psihicheskoe-zdorovie/emocionalnoe-vygoranie
- **template:** TPL-SERVICE-LEAF
- **editor:** placeholder template + future ACF
- **indexing:** blocked until content/legal approval

### `/uslugi/psihicheskoe-zdorovie/trevozhnye-rasstroystva/`
- **post_type:** page
- **parent:** /uslugi/psihicheskoe-zdorovie/
- **slug:** uslugi/psihicheskoe-zdorovie/trevozhnye-rasstroystva
- **template:** TPL-SERVICE-LEAF
- **editor:** placeholder template + future ACF
- **indexing:** blocked until content/legal approval

### `/uslugi/psihicheskoe-zdorovie/rasstroystva-sna/`
- **post_type:** page
- **parent:** /uslugi/psihicheskoe-zdorovie/
- **slug:** uslugi/psihicheskoe-zdorovie/rasstroystva-sna
- **template:** TPL-SERVICE-LEAF
- **editor:** placeholder template + future ACF
- **indexing:** blocked until content/legal approval

### `/uslugi/psihicheskoe-zdorovie/travma/`
- **post_type:** page
- **parent:** /uslugi/psihicheskoe-zdorovie/
- **slug:** uslugi/psihicheskoe-zdorovie/travma
- **template:** TPL-SERVICE-LEAF
- **editor:** placeholder template + future ACF
- **indexing:** blocked until content/legal approval

### `/uslugi/rasstroystva-pischevogo-povedeniya/`
- **post_type:** page
- **parent:** /uslugi/
- **slug:** uslugi/rasstroystva-pischevogo-povedeniya
- **template:** TPL-SERVICE-SUBDIVISION
- **editor:** placeholder template + future ACF
- **indexing:** blocked until content/legal approval

### `/uslugi/rasstroystva-pischevogo-povedeniya/anoreksiya/`
- **post_type:** page
- **parent:** /uslugi/rasstroystva-pischevogo-povedeniya/
- **slug:** uslugi/rasstroystva-pischevogo-povedeniya/anoreksiya
- **template:** TPL-SERVICE-LEAF
- **editor:** placeholder template + future ACF
- **indexing:** blocked until content/legal approval

### `/uslugi/rasstroystva-pischevogo-povedeniya/nervnaya-bulimiya/`
- **post_type:** page
- **parent:** /uslugi/rasstroystva-pischevogo-povedeniya/
- **slug:** uslugi/rasstroystva-pischevogo-povedeniya/nervnaya-bulimiya
- **template:** TPL-SERVICE-LEAF
- **editor:** placeholder template + future ACF
- **indexing:** blocked until content/legal approval

### `/uslugi/rasstroystva-pischevogo-povedeniya/kompulsivnoe-pereedanie/`
- **post_type:** page
- **parent:** /uslugi/rasstroystva-pischevogo-povedeniya/
- **slug:** uslugi/rasstroystva-pischevogo-povedeniya/kompulsivnoe-pereedanie
- **template:** TPL-SERVICE-LEAF
- **editor:** placeholder template + future ACF
- **indexing:** blocked until content/legal approval

### `/o-centre/`
- **post_type:** page
- **parent:** —
- **slug:** o-centre
- **template:** TPL-INSTITUTIONAL
- **editor:** ACF + native title
- **indexing:** intended index when launch-ready

### `/o-centre/o-nas/`
- **post_type:** page
- **parent:** /o-centre/
- **slug:** o-centre/o-nas
- **template:** TPL-INSTITUTIONAL
- **editor:** placeholder template + future ACF
- **indexing:** blocked until content/legal approval

### `/o-centre/programma-lecheniya/`
- **post_type:** page
- **parent:** /o-centre/
- **slug:** o-centre/programma-lecheniya
- **template:** TPL-INSTITUTIONAL
- **editor:** placeholder template + future ACF
- **indexing:** blocked until content/legal approval

### `/o-centre/galereya-o-dome/`
- **post_type:** page
- **parent:** /o-centre/
- **slug:** o-centre/galereya-o-dome
- **template:** TPL-INSTITUTIONAL
- **editor:** placeholder template + future ACF
- **indexing:** blocked until content/legal approval

### `/o-centre/specialistam/`
- **post_type:** page
- **parent:** /o-centre/
- **slug:** o-centre/specialistam
- **template:** TPL-INSTITUTIONAL
- **editor:** placeholder template + future ACF
- **indexing:** blocked until content/legal approval

### `/o-centre/rodstvennikam/`
- **post_type:** page
- **parent:** /o-centre/
- **slug:** o-centre/rodstvennikam
- **template:** TPL-INSTITUTIONAL
- **editor:** placeholder template + future ACF
- **indexing:** blocked until content/legal approval

### `/otzyvy/`
- **post_type:** page
- **parent:** —
- **slug:** otzyvy
- **template:** TPL-REVIEWS
- **editor:** ACF + native title
- **indexing:** intended index when launch-ready

### `/blog/`
- **post_type:** posts_page
- **parent:** —
- **slug:** blog
- **template:** TPL-BLOG-ARCHIVE
- **editor:** ACF + native title
- **indexing:** intended index when launch-ready

### `/blog/nazvanie-stati/`
- **post_type:** post
- **parent:** /blog/
- **slug:** blog/nazvanie-stati
- **template:** TPL-BLOG-SINGLE
- **editor:** ACF + native title
- **indexing:** intended index when launch-ready

### `/kontakty/`
- **post_type:** page
- **parent:** —
- **slug:** kontakty
- **template:** TPL-CONTACTS
- **editor:** ACF + native title
- **indexing:** intended index when launch-ready

### `/privacy-policy/`
- **post_type:** page
- **parent:** —
- **slug:** privacy-policy
- **template:** TPL-LEGAL
- **editor:** controlled HTML / legal template
- **indexing:** blocked until content/legal approval

### `/user-agreement/`
- **post_type:** page
- **parent:** —
- **slug:** user-agreement
- **template:** TPL-LEGAL
- **editor:** controlled HTML / legal template
- **indexing:** blocked until content/legal approval

### `/consent-personal-data/`
- **post_type:** page
- **parent:** —
- **slug:** consent-personal-data
- **template:** TPL-LEGAL
- **editor:** controlled HTML / legal template
- **indexing:** blocked until content/legal approval

### `/cookie-files-policy/`
- **post_type:** page
- **parent:** —
- **slug:** cookie-files-policy
- **template:** TPL-LEGAL
- **editor:** controlled HTML / legal template
- **indexing:** blocked until content/legal approval


## CPT rejection analysis

| Candidate CPT | Rejected because |
|---------------|------------------|
| `review` | No single-review routes in V9; archive satisfied by page repeater |
| `service` | Native Pages preserve hierarchy and menu simplicity |
| `article` | Native Posts satisfy blog fixture structure |
