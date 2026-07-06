# FP-0002 V9-06E11 WP Route Inventory v1

**Runtime:** http://shpigovsky.test
**Route count:** 31

| Route | WP object | Template | Main/hero | Current stack | Notes |
|---|---|---|---|---|---|
| / | 4 | default | site-main site-main--front / hero=True | home-recovery-intro, founder-quote, home-treatment-prevention, home-gallery, home-why-us, home-staff-photo (+13) |  |
| /blog/ | 19 | — | shpigovsky-skeleton shpigovsky-skeleton- / hero=False | shpigovsky-skeleton-breadcrumbs |  |
| /blog/nazvanie-stati/ | None | — | shpigovsky-skeleton shpigovsky-skeleton- / hero=False | shpigovsky-skeleton-breadcrumbs | 404 |
| /consent-personal-data/ | 23 | page-templates/legal.php | page-plain-content__main / hero=False | shpigovsky-skeleton-breadcrumbs, legal-document |  |
| /cookie-files-policy/ | 24 | page-templates/legal.php | page-plain-content__main / hero=False | shpigovsky-skeleton-breadcrumbs, legal-document |  |
| /kontakty/ | 20 | page-templates/contacts.php | page-kontakty__main site-main site-main- / hero=False | shpigovsky-skeleton-breadcrumbs, contacts-body, contacts-rehabilitation-steps |  |
| /o-centre/ | 11 | page-templates/institutional.php | shpigovsky-skeleton shpigovsky-skeleton- / hero=True | services-inner-hero-v2, shpigovsky-skeleton-breadcrumbs |  |
| /o-centre/galereya-o-dome/ | 14 | page-templates/institutional.php | shpigovsky-skeleton shpigovsky-skeleton- / hero=True | services-inner-hero-v2, shpigovsky-skeleton-breadcrumbs |  |
| /o-centre/o-nas/ | 12 | page-templates/institutional.php | shpigovsky-skeleton shpigovsky-skeleton- / hero=True | services-inner-hero-v2, shpigovsky-skeleton-breadcrumbs |  |
| /o-centre/programma-lecheniya/ | 13 | page-templates/institutional.php | shpigovsky-skeleton shpigovsky-skeleton- / hero=True | services-inner-hero-v2, shpigovsky-skeleton-breadcrumbs |  |
| /o-centre/rodstvennikam/ | 16 | page-templates/institutional.php | shpigovsky-skeleton shpigovsky-skeleton- / hero=True | services-inner-hero-v2, shpigovsky-skeleton-breadcrumbs |  |
| /o-centre/specialistam/ | 15 | page-templates/institutional.php | shpigovsky-skeleton shpigovsky-skeleton- / hero=True | services-inner-hero-v2, shpigovsky-skeleton-breadcrumbs |  |
| /otzyvy/ | 18 | page-templates/reviews.php | page-otzyvy__main / hero=False | shpigovsky-skeleton-breadcrumbs, reviews-archive, reviews-rehabilitation-requirements |  |
| /privacy-policy/ | 3 | page-templates/legal.php | page-plain-content__main / hero=False | shpigovsky-skeleton-breadcrumbs, legal-document |  |
| /user-agreement/ | 22 | page-templates/legal.php | page-plain-content__main / hero=False | shpigovsky-skeleton-breadcrumbs, legal-document |  |
| /uslugi/ | 5 | page-templates/services-hub.php | page-uslugi-v2__main site-main site-main / hero=True | services-inner-hero-v2, breadcrumbs, services-page-subnav, services-category-section-v2, services-program-v2, founder-quote (+3) |  |
| /uslugi/psihicheskoe-zdorovie/ | 7 | — | page-service-subdivision-v1__main site-m / hero=True | services-inner-hero-v2, breadcrumbs, services-page-subnav, services-category-section-v2, service-subdivision-nature-v1, program-cta-band-section (+10) |  |
| /uslugi/psihicheskoe-zdorovie/depressiya/ | 78 | single-service.php → placeholder-stack | page-service-leaf-v1__main site-main sit / hero=True | services-inner-hero-v2, breadcrumbs, services-page-subnav, service-leaf-intro-v1, program-cta-band-section, services-program-v2 (+1) |  |
| /uslugi/psihicheskoe-zdorovie/emocionalnoe-vygoranie/ | 80 | single-service.php → placeholder-stack | page-service-leaf-v1__main site-main sit / hero=True | services-inner-hero-v2, breadcrumbs, services-page-subnav, service-leaf-intro-v1, program-cta-band-section, services-program-v2 (+1) |  |
| /uslugi/psihicheskoe-zdorovie/ptrs/ | 79 | single-service.php → placeholder-stack | page-service-leaf-v1__main site-main sit / hero=True | services-inner-hero-v2, breadcrumbs, services-page-subnav, service-leaf-intro-v1, program-cta-band-section, services-program-v2 (+1) |  |
| /uslugi/psihicheskoe-zdorovie/rasstroystva-sna/ | 82 | single-service.php → placeholder-stack | page-service-leaf-v1__main site-main sit / hero=True | services-inner-hero-v2, breadcrumbs, services-page-subnav, service-leaf-intro-v1, program-cta-band-section, services-program-v2 (+1) |  |
| /uslugi/psihicheskoe-zdorovie/travma/ | 83 | single-service.php → placeholder-stack | page-service-leaf-v1__main site-main sit / hero=True | services-inner-hero-v2, breadcrumbs, services-page-subnav, service-leaf-intro-v1, program-cta-band-section, services-program-v2 (+1) |  |
| /uslugi/psihicheskoe-zdorovie/trevozhnye-rasstroystva/ | 81 | single-service.php → placeholder-stack | page-service-leaf-v1__main site-main sit / hero=True | services-inner-hero-v2, breadcrumbs, services-page-subnav, service-leaf-intro-v1, program-cta-band-section, services-program-v2 (+1) |  |
| /uslugi/rasstroystva-pischevogo-povedeniya/ | 8 | — | page-service-subdivision-v1__main site-m / hero=True | services-inner-hero-v2, breadcrumbs, services-page-subnav, services-category-section-v2, service-subdivision-nature-v1, program-cta-band-section (+10) |  |
| /uslugi/rasstroystva-pischevogo-povedeniya/anoreksiya/ | 85 | single-service.php → placeholder-stack | page-service-leaf-v1__main site-main sit / hero=True | services-inner-hero-v2, breadcrumbs, services-page-subnav, service-leaf-intro-v1, program-cta-band-section, services-program-v2 (+1) |  |
| /uslugi/rasstroystva-pischevogo-povedeniya/kompulsivnoe-pereedanie/ | 87 | single-service.php → placeholder-stack | page-service-leaf-v1__main site-main sit / hero=True | services-inner-hero-v2, breadcrumbs, services-page-subnav, service-leaf-intro-v1, program-cta-band-section, services-program-v2 (+1) |  |
| /uslugi/rasstroystva-pischevogo-povedeniya/nervnaya-bulimiya/ | 86 | single-service.php → placeholder-stack | page-service-leaf-v1__main site-main sit / hero=True | services-inner-hero-v2, breadcrumbs, services-page-subnav, service-leaf-intro-v1, program-cta-band-section, services-program-v2 (+1) |  |
| /uslugi/zavisimosti/ | 6 | — | page-service-subdivision-v1__main site-m / hero=True | services-inner-hero-v2, breadcrumbs, services-page-subnav, services-category-section-v2, service-subdivision-nature-v1, program-cta-band-section (+10) |  |
| /uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/ | 74 | single-service.php → alcohol_special-stack | page-service-leaf-v1__main site-main sit / hero=True | services-inner-hero-v2, breadcrumbs, services-page-subnav, service-leaf-intro-v1, service-leaf-bordered-info-v1, program-cta-band-section (+12) |  |
| /uslugi/zavisimosti/profilakticheskiy-analiz/ | 75 | single-service.php → placeholder-stack | page-service-leaf-v1__main site-main sit / hero=True | services-inner-hero-v2, breadcrumbs, services-page-subnav, service-leaf-intro-v1, program-cta-band-section, services-program-v2 (+1) |  |
| /uslugi/zavisimosti/specialistam/ | 15 | page-templates/institutional.php | page-service-leaf-v1__main site-main sit / hero=True | services-inner-hero-v2, breadcrumbs, services-page-subnav, service-leaf-intro-v1, program-cta-band-section, services-program-v2 (+1) |  |