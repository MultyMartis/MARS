# FP-0002 — Services General Content Map v1

**Planning ID:** `services-general-01`  
**Date:** 2026-06-26  
**Sources:** PNG 26.06.2026 (primary composition), Figma `Spig_v1.2.fig` / `Услуги хаб` (text evidence), existing Home partials (proven strings)

Hidden Figma layers excluded per project rules.

---

## Content table

| Section | Element | Visible text | Source authority | HTML destination |
| ------- | ------- | ------------ | ---------------- | ---------------- |
| Hero | H1 | Лечение и профилактика | PNG + Figma SECTION-03 heading | `hero-inner.html` → `.hero__title` |
| Hero | Tagline | SAFE_UNKNOWN — lead line under H1 in PNG; exact wording needs Figma text node export | PNG (visible) | `.hero__tagline` |
| Hero | CTA | Записаться на консультацию *(or variant «ЗАПИСАТЬСЯ…»)* | PNG | Modal trigger via header/hero pattern |
| Category 1 | H2 | Зависимости и пристрастия | Figma accordion label + Home partial | New hub heading |
| Category 1 | Lead | Мы работаем с зависимостью… *(Home treatment lead)* | `home-treatment-prevention.html` @ source | Hub lead — **confirm Services-specific copy in Figma** |
| Category 1 | Service links | Алкогольная зависимость; Наркотическая зависимость; Лекарственная зависимость; Поведенческие зависимости | Home partial panel 1 | Hub service list |
| Category 2 | H2 | Психическое здоровье | Home accordion item 2 | Hub heading |
| Category 2 | Services | SAFE_UNKNOWN — panel empty in source | Figma `Услуги хаб` | Hub list |
| Category 3 | H2 | Расстройства пищевого поведения | Home accordion item 3 | Hub heading |
| Category 3 | Services | SAFE_UNKNOWN | Figma | Hub list |
| Category 4 | H2 | Генотипирование | Home accordion item 4 | Hub heading |
| Category 4 | Services | SAFE_UNKNOWN | Figma | Hub list |
| Category * | CTA | SAFE_UNKNOWN per block — PNG shows red button; label TBD | PNG | Hub CTA |
| Program | H2 | Наша программа включает 4 направления *(current param)* | `uslugi.html` param | `programHeading` — **PNG may differ** → operator decision |
| Program | Lead / intros | Existing program partial copy | Source | `home-rehabilitation-program.html` |
| Founder | Quote body | Existing founder partial (4 paragraphs) | Source | `home-founder-quote.html` |
| Founder | Name / role | Сергей Юрьевич Шпиговский; Основатель центра… | Source | figcaption |
| Founder | CTA | Записаться на консультацию | Source | button |
| Comfort | H2 | Комфорт, приватность, забота | Source | **PNG shows «анонимность»** — operator decision |
| Comfort | Lead | Existing comfort lead | Source | partial |
| Comfort | All link | подробнее о доме | Source | partial |
| FAQ | H2 | ОТВЕТЫ НА ВОПРОСЫ *(PNG)* vs «Нас часто спрашивают» *(source)* | PNG primary | Parameterize heading |
| FAQ | Questions | Existing FAQ questions (Home copy) | Source | partial — **Services Q/A TBD** |
| FAQ | Answers | Lorem ipsum (temporary) | Source status | Replace when content ready |
| Final form | H2 | Остались вопросы? | Source | partial |
| Final form | Lead | Опишите вашу ситуацию… | Source | partial |
| Final form | Labels | Ваше имя; Ваш телефон; Опишите ситуацию | Source | form fields |
| Final form | Submit | Записаться на консultation | Source | submit btn |
| Breadcrumb | — | Not visible on PNG hero | PNG | **Omit Pass 1** unless operator adds |

---

## SAFE_UNKNOWN summary (non-blocking unless noted)

- Hero tagline exact string
- Category 2–4 service link labels and hrefs
- Per-category CTA button labels
- Program section H2 if PNG title differs from current param
- Comfort H2: «приватность» vs «анонимность»
- FAQ heading + Services-specific Q/A set
- Mid-page CTA band copy (if block confirmed)

---

## Content verdict

**Sufficient for Pass 1 shell + category 1 (dependencies) implementation** using Home-proven strings. Categories 2–4 and FAQ content require Figma text export or operator copy before full parity.

---

*End of content map v1.*
