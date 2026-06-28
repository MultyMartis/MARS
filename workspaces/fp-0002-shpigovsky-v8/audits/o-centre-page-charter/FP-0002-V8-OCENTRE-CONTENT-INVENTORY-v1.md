# FP-0002 V8 O-Centre Content Inventory v1

**Date:** 2026-06-29
**Rule:** Exact text preserved from sources; no copy editing.

| Content ID | Block | Type | Exact source | Text/content (summary or exact) | Status |
|---|---|---|---|---|---|
| C-OC-H1 | OC-B01 | H1 | V7 WIP `o-centre-v1.html` (historical); Figma frame «О центре» | «Шпиговский дом» | CONFIRMED (WIP); verify PDF |
| C-OC-HERO-EYEBROW | OC-B01 | Eyebrow | V7 WIP | «Место, где наступает выздоровление» | CONFIRMED (WIP) |
| C-OC-HERO-LEAD | OC-B01 | Lead | V7 WIP | «— реабилитационный центр профилактики и лечения зависимостей и нарушений психического здоровья.» | CONFIRMED (WIP) |
| C-OC-HERO-CTA | OC-B01 | Button | V8 pattern | «Записаться на консультацию» | CONFIRMED |
| C-OC-BREADCRUMB | OC-B02 | Breadcrumb | URL map / static demo registry | Главная → О центре | CONFIRMED |
| C-OC-SUBNAV-1 | OC-B02 | Nav label | V7 WIP subnav | «Кто мы» → `#about-who-we-are` | PLACEHOLDER anchors — reconcile with BLK-006 design |
| C-OC-SUBNAV-2 | OC-B02 | Nav label | V7 WIP | «Кого мы лечим» | PLACEHOLDER |
| C-OC-SUBNAV-3 | OC-B02 | Nav label | V7 WIP | «Наш подход к лечению» | PLACEHOLDER |
| C-OC-WHO-H2 | OC-B03 | H2 | V7 WIP | «Шпиговский дом — место, где видят человека, а не только диагноз» | CONFIRMED (WIP) |
| C-OC-WHO-LEAD | OC-B03 | Lead bar | V7 WIP | «ВЕДЕМ ПРИЕМ И КОНСУЛЬТИРУЕМ В МОСКВЕ…» | CONFIRMED (WIP) |
| C-OC-WHO-P1–P5 | OC-B03 | Paragraphs | V7 WIP | Five institutional paragraphs (social-psychological space, diagnostics, no locks) | CONFIRMED (WIP) |
| C-OC-TREAT-H2 | OC-B04 | H2 | V7 WIP | «Разные люди, разные истории — одно общее: что-то пошло не так» | CONFIRMED (WIP) |
| C-OC-TREAT-INTRO | OC-B04 | Intro | V7 WIP | Two intro paragraphs | CONFIRMED (WIP) |
| C-OC-TREAT-LEAD | OC-B04 | Lead | V7 WIP | «Мы работаем с широким спектром состояний:» | CONFIRMED (WIP) |
| C-OC-TREAT-BODY | OC-B04 | Body HTML | V7 WIP | Three `<p>` blocks: dependencies, mental health, eating disorders | CONFIRMED (WIP) |
| C-OC-STEPS | OC-B05 | Steps 01–04 | Block inventory BLK-018 | Numbered rehabilitation procedure steps | MISSING in V8 — extract from PDF/fig |
| C-OC-PROGRAM | OC-B06 | Program copy | Services `services-program-v2` on hub | Hub program leads (center-specific) | REUSE_EXISTING copy pattern |
| C-OC-CTA-BAND | OC-B07 | CTA | `program-cta-band` defaults | «Запишитесь на гостевой визит» + phone | CONFIRMED (shared) |
| C-OC-HOME-NARRATIVE | OC-B08 | BLK-037/038 | Block inventory names | «Наш Дом» + Infrastructure narratives | MISSING — PDF SOURCE-011 |
| C-OC-FOUNDER | OC-B09 | Quote | `founder-quote` partial | Founder quote content (variant-b on services) | REUSE_WITH_CONTENT_PARAMETERS |
| C-OC-COMFORT-H2 | OC-B10 | H2 | `comfort.html` default | «Комфорт, приватность, забота» | CONFIRMED (partial default) |
| C-OC-COMFORT-LEAD | OC-B10 | Lead | `comfort.html` | Conversation lead paragraph | CONFIRMED |
| C-OC-SPEC-H2 | OC-B11 | H2 | `specialists.html` param | «Специалисты центра» (Home default) | CONFIRMED |
| C-OC-REVIEWS | OC-B12 | Reviews | `reviews.html` | Shared review cards | CONFIRMED (demo content) |
| C-OC-FAQ-H2 | OC-B13 | H2 | `faq.html` | «Нас часто спрашивают» | CONFIRMED |
| C-OC-FAQ-ITEMS | OC-B13 | Accordion | `faq.html` | Shared FAQ set | CONFIRMED (may need About-specific subset — UNRESOLVED) |
| C-OC-TITLE | Page meta | Title | Static demo registry | «О центре — Шпиговский Дом» | CONFIRMED |
| C-OC-FOOTER-LINKS | OC-G01 | Footer nav | `footer.html` | О нас, Программа, Галерея, Специалистам, Родственникам, Интервью | CONFIRMED (links to subpages) |

**Copy changes performed in this task:** None.

**Conflicts:** Subnav anchors (V7 WIP) vs footer subpage URLs (production IA). FAQ on Figma vs inventory omission.
