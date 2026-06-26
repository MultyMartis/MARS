# FP-0002 Service Subdivision — Design Crop Registry v1

Source: `SERVICE-SUBDIVISION-DESIGN-AUTHORITY-*.png` (operator PNG, frame `1:3491` / `1:7096`).

Boundaries determined by visual strip inspection of full-page raster (not JSON/tree).

## Desktop

| № | Crop | Y range | Visible heading | First body words | Items | Assets | CTA |
|---:|---|---:|---|---|---:|---|---|
| 1 | DESIGN-D-01-HEADER-HERO | 0–900 | Зависимости и пристрастия | Lorem ipsum dolor sit amet, consectetur adipiscing elit… | 1 hero | Hero painting | ЗАПИСАТЬСЯ НА КОНСУЛЬТАЦИЮ |
| 2 | DESIGN-D-02-UPPER-CONTENT | 820–1200 | — | Главная / Услуги / Зависимости и пристрастия | 7 subnav pills | — | — |
| 3 | DESIGN-D-03-DEPENDENCIES | 900–2100 | Зависимости, которые мы лечим | Lorem ipsum dolor sit amet… | 4 dependency rows | Lifebuoy decor (forbidden override) | ЗАПИСАТЬСЯ НА КОНСУЛЬТАЦИЮ |
| 4 | DESIGN-D-04-NATURE | 2100–3200 | Природа зависимости | LOREM IPSUM DOLOR SIT AMET… (red line) | 2 info cards + 2 subheads | Lifebuoy decor (forbidden) | ПОДРОБНЕЕ О ГЕНОТИПИРОВАНИИ |
| 5 | DESIGN-D-05-CTA-01 | 3200–3500 | Запишитесь на встречу | Опишите ситуацию… | 1 band | Interior photo | ЗАПИСАТЬСЯ + phone |
| 6 | DESIGN-D-06-PROGRAM | 3500–5200 | Наша программа включает 4 направления | LOREM IPSUM… | 4 program cards | 4 paintings | ПОДРОБНЕЕ |
| 7 | DESIGN-D-07-REHABILITATION-STAGES | 5200–6800 | Что нужно для прохождения реабилитации и лечения | Мы гарантируем конфиденциальность… | 4 steps | — | — |
| 8 | DESIGN-D-08-CTA-02 | 6800–7200 | (second dark band) | — | 1 | Photo | Записаться |
| 9 | DESIGN-D-09-APPROACH-INTERIOR | 7200–9000 | Corridor / approach block | — | 1 large photo | Interior | — |
| 10 | DESIGN-D-10-TEAM-CENTER | 9000–10200 | Team + stats composite | — | Stats grid | Team photo | — |
| 11 | DESIGN-D-11-SPECIALISTS | 10200–11200 | Специалисты центра | — | 3 cards | Portraits | — |
| 12 | DESIGN-D-12-FOUNDER | 11200–12000 | Слово спецу / quote | — | 1 | Portrait | — |
| 13 | DESIGN-D-13-COMFORT | 12000–13200 | Комфорт, приватность, забота | — | Gallery | 6 images | — |
| 14 | DESIGN-D-14-REVIEWS | 12800–13150 | Отзывы | — | Carousel | Photos | — |
| 15 | DESIGN-D-15-FAQ | 13150–13450 | Нас часто спрашивают | — | Accordion | — | — |
| 16 | DESIGN-D-16-FINAL-FORM-FOOTER | 13450–end | Остались вопросы? | Опишите вашу ситуацию… | Form + footer | — | Отправить |

## Mobile

Parallel registry `DESIGN-M-01` … `DESIGN-M-16` in `design-crops/mobile/` with viewport width 380px. Each block cropped individually (no mixed 4–13 registry).

**Note:** Mobile upper block after hero shows psych/intro stack distinct from desktop; requires per-block mobile reconciliation (not desktop DOM shrink).
