/**
 * V6 final-wave controlled rollout — armatura canonical + ORCA packs only.
 * NOT a blind generator; explicit per-route content from approved packs.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, '..');
const PARTIALS = path.join(ROOT, 'src/partials/sections/v5-ppc');
const PAGES = path.join(ROOT, 'src/pages');

const nb = (s) => s.replace(/ /g, '&nbsp;');

const FACTOR_ICONS = [
  'fa-weight-hanging',
  'fa-ruler-horizontal',
  'fa-box',
  'fa-road',
  'fa-truck-loading',
  'fa-clock',
];

const CARGO_ICONS = [
  'fa-clipboard-list',
  'fa-weight-hanging',
  'fa-hard-hat',
  'fa-arrows-alt-h',
  'fa-box',
  'fa-truck-loading',
];

function kickerFrom(text) {
  const w = text.split(/\s+/)[0].replace(/[^а-яА-ЯёЁa-zA-Z]/g, '');
  return w.length > 12 ? w.slice(0, 10) : w;
}

function slugFromCargo(label, index) {
  const latin = {
    кирпич: 'kirpich',
    блоки: 'bloki',
    стройматериалы: 'stroymat',
    паллеты: 'pallet',
    'строительные грузы': 'stroy-gruz',
    стройка: 'stroyka',
    арматура: 'armatura',
    'грузы на участок': 'uchastok',
    объекты: 'obekty',
    'сложный подъезд': 'podiezd',
    оборудование: 'oborud',
    бытовки: 'bytovki',
    контейнеры: 'konteynery',
    'поставки на объект': 'postavka',
    снабжение: 'snab',
    'объекты по краю': 'kray-obj',
    межгород: 'mezhgorod',
  };
  const key = label.toLowerCase().trim();
  return latin[key] || `cargo-${index + 1}`;
}

function heroHtml(r) {
  const specs = r.hero.specs
    .map(
      (line) => {
        const [label, value] = line.split(' — ');
        const icon =
          label.includes('Борт') ? 'fa-truck-moving'
          : label.includes('Стрела') && !label.includes('Вылет') ? 'fa-truck-loading'
          : label.includes('Вылет') ? 'fa-arrows-alt-h'
          : label.includes('Кузов') ? 'fa-ruler-horizontal'
          : label.includes('привод') || label.includes('Привод') ? 'fa-truck-moving'
          : 'fa-clock';
        return `                    <li><i class="fas ${icon}" aria-hidden="true"></i><span>${nb(line)}</span></li>`;
      },
    )
    .join('\n');

  const proofIcons = ['fa-shipping-fast', 'fa-file-invoice-dollar', 'fa-hard-hat', 'fa-business-time'];
  const proof = r.hero.proof
    .map(
      (label, i) => `                <div class="hero-proof__item">
                    <i class="fas ${proofIcons[i] || 'fa-shipping-fast'}" aria-hidden="true"></i>
                    <span class="hero-proof__label">${nb(label)}</span>
                </div>`,
    )
    .join('\n');

  const cargo = r.hero.cargo
    .map((label, i) => {
      const icon = CARGO_ICONS[i] || 'fa-box';
      const slug = slugFromCargo(label, i);
      return `            <li>
                <button type="button" class="hero__cargo-card" data-modal-open="modal-callback" data-cta-source="${r.prefix}-hero-cargo-${slug}" data-modal-title="${r.modalTitle}">
                    <i class="fas ${icon}" aria-hidden="true"></i>
                    <span>${nb(label)}</span>
                    <span class="hero__cargo-action">Заказать перевозку &gt;</span>
                </button>
            </li>`;
    })
    .join('\n');

  const h1Parts = r.hero.h1.match(/^(.+?)(\s+в\s+.+)$/i);
  const h1Main = h1Parts ? h1Parts[1] : r.hero.h1;
  const h1Span = h1Parts ? h1Parts[2] : '';

  return `<section class="hero hero--v5" id="hero" aria-labelledby="hero-title">
    <div class="hero__shell">
        <div class="hero__main">
            <div class="hero__content">
                <h1 class="hero__title" id="hero-title">${nb(h1Main)}${h1Span ? ` <span>${nb(h1Span.trim())}</span>` : ''}</h1>
                <p class="hero__lead">${nb(r.hero.lead)}</p>

                <ul class="hero__specs" aria-label="Параметры манипулятора">
${specs}
                </ul>
            </div>

            <aside class="hero__aside" aria-label="Быстрая заявка">
                <form
                    class="hero-form site-form--dark"
                    action="#"
                    method="post"
                    data-form
                    data-form-id="${r.prefix}-hero-quote"
                    data-page-type="${r.pageType}"
                    data-form-name="${r.hero.formTitle}"
                    data-cta-source="${r.prefix}-hero-inline"
                    data-form-success="Спасибо! Заявка принята — скоро перезвоним и уточним детали."
                    aria-label="Форма расчёта стоимости"
                >
                    <h2 class="hero-form__title">${nb(r.hero.formTitle)}</h2>
                    <p class="hero-form__lead">${nb(r.hero.formLead)}</p>
                    <label>
                        <span>Имя</span>
                        <input type="text" name="name" placeholder="Ваше имя" autocomplete="name" required>
                    </label>
                    <label>
                        <span>Телефон</span>
                        <input type="tel" name="phone" placeholder="Телефон" autocomplete="tel" required>
                    </label>
                    <button class="button button--primary" type="submit">${nb(r.hero.formSubmit)}</button>
                    <p class="hero-form__note">${nb(r.hero.formNote)}</p>

                    <div class="site-form__field site-form__field--consent" data-form-field-wrap>
                        <label class="site-form__consent">
                            <input
                                class="site-form__consent-input"
                                type="checkbox"
                                name="consent"
                                value="1"
                                data-validate="required consent"
                                required
                            >
                            <span class="site-form__consent-box" aria-hidden="true"></span>
                            <span class="site-form__consent-text">Я&nbsp;даю согласие на&nbsp;обработку персональных данных в&nbsp;соответствии с&nbsp;<a href="/consent-personal-data/" target="_blank">Согласием на&nbsp;обработку персональных данных</a> и&nbsp;соглашаюсь с&nbsp;<a href="/privacy-policy/" target="_blank">Политикой конфиденциальности</a>.</span>
                        </label>
                        <span class="site-form__error" data-form-error hidden>Подтвердите согласие на&nbsp;обработку данных</span>
                    </div>

                    <a class="hero-form__call button button--outline" href="tel:+79004658331" data-desktop-modal-open="modal-phone">Позвонить</a>
                </form>
            </aside>
        </div>

        <div class="hero__lower">
            <aside class="hero-proof hero-proof--v5" aria-label="Преимущества подачи">
            <div class="hero-proof__grid">
${proof}
            </div>
        </aside>

        <div class="hero__cargo-block">
            <ul class="hero__cargo" aria-label="${r.hero.cargoAria}">
${cargo}
            </ul>
        </div>
        </div>
    </div>
</section>
`;
}

function specsHtml(r) {
  const rows = r.specs.rows
    .map(([label, value], i) => {
      const icons = ['fa-truck-loading', 'fa-weight-hanging', 'fa-ruler-horizontal', 'fa-truck-moving', 'fa-clock', 'fa-truck-moving'];
      return `                        <div class="machine-showcase__spec-row">
                            <dt><i class="fas ${icons[i] || 'fa-truck-moving'}" aria-hidden="true"></i><span>${nb(label)}</span></dt>
                            <dd>${nb(value)}</dd>
                        </div>`;
    })
    .join('\n');

  return `<section class="prices section-light section-light--upper" id="specs" aria-labelledby="specs-title">
    <div class="section-shell">
        <div class="machine-showcase machine-showcase--ops-panel">
            <figure class="machine-showcase__media machine-showcase__media--index-baseline">
                <img src="/assets/img/v5/second-screen/second-screen-index-baseline.jpg" alt="${r.specs.imgAlt}" width="1696" height="2528" loading="lazy" decoding="async">
            </figure>

            <div class="machine-showcase__summary">
                <header class="machine-showcase__intro">
                    <p class="section-eyebrow">${nb(r.specs.eyebrow)}</p>
                    <h2 class="machine-showcase__title" id="specs-title">${nb(r.specs.title)}</h2>
                    <p class="machine-showcase__lead">${nb(r.specs.lead)}</p>
                </header>

                <div class="machine-showcase__spec-panel">
                    <dl class="machine-showcase__specs" aria-label="Параметры машины">
${rows}
                    </dl>

                    <p class="machine-showcase__ops">${nb(r.specs.ops)}</p>

                    <div class="machine-showcase__action">
                        <div class="machine-showcase__cta">
                            <a class="button button--primary" href="#contacts" data-modal-open="modal-callback" data-cta-source="${r.prefix}-specs-primary" data-modal-title="${r.modalTitle}">${nb(r.specs.cta)}</a>
                        </div>
                        <p class="machine-showcase__micro">${nb(r.specs.micro)}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
`;
}

function tasksHtml(r) {
  const allowed = r.tasks.allowed
    .map(
      (text) => `                    <li>
                        <i class="fas fa-check" aria-hidden="true"></i>
                        <div class="machine-transport__item-copy">
                            <span class="machine-transport__item-kicker">${nb(kickerFrom(text))}</span>
                            <span class="machine-transport__item-text">${nb(text)}</span>
                        </div>
                    </li>`,
    )
    .join('\n');

  const denied = r.tasks.denied
    .map((text) => `                        <li><i class="fas fa-times" aria-hidden="true"></i><span>${nb(text)}</span></li>`)
    .join('\n');

  const points = r.tasks.ctaPoints
    .map((p) => `                            <li>${nb(p)}</li>`)
    .join('\n');

  return `<section class="prices section-light" id="tasks" aria-labelledby="tasks-title">
    <div class="section-shell">
        <div class="machine-transport machine-transport--ops-grid">
            <section class="machine-transport__card machine-transport__card--allowed" aria-labelledby="tasks-title">
                <p class="machine-transport__eyebrow">${nb(r.tasks.eyebrow)}</p>
                <h2 class="machine-transport__heading" id="tasks-title">${nb(r.tasks.title)}</h2>
                <ul class="machine-transport__list machine-transport__list--allowed">
${allowed}
                </ul>
                <div class="machine-transport__note-block">
                    <span class="machine-transport__note-label">${nb(r.tasks.noteLabel)}</span>
                    <p class="machine-transport__note">${nb(r.tasks.noteText)}</p>
                </div>
            </section>

            <div class="machine-transport__utility-stack">
                <section class="machine-transport__card machine-transport__card--denied" aria-labelledby="machine-denied-title">
                    <p class="machine-transport__eyebrow">Ограничения по заявкам</p>
                    <h3 id="machine-denied-title">Что не перевозим</h3>
                    <ul class="machine-transport__list machine-transport__list--denied">
${denied}
                    </ul>
                </section>

                <aside class="machine-transport__cta" aria-label="Расчёт по параметрам задачи">
                    <p class="machine-transport__eyebrow">${nb(r.tasks.ctaEyebrow)}</p>
                    <div class="machine-transport__cta-head">
                        <i class="fas fa-clipboard-list" aria-hidden="true"></i>
                        <div class="machine-transport__cta-copy">
                            <h3 class="machine-transport__cta-title">${nb(r.tasks.ctaTitle)}</h3>
                            <p class="machine-transport__cta-text">${nb(r.tasks.ctaText)}</p>
                        </div>
                    </div>
                    <div class="machine-transport__cta-actions">
                        <ul class="machine-transport__cta-points" aria-label="Что уточняем перед расчётом">
${points}
                        </ul>
                        <a class="button button--primary button--sm" href="#contacts" data-modal-open="modal-callback" data-cta-source="${r.prefix}-tasks-quote" data-modal-title="${r.modalTitle}">${nb(r.tasks.ctaButton)}</a>
                    </div>
                </aside>
            </div>
        </div>
    </div>
</section>
`;
}

function orderHtml(r) {
  const icons = ['fa-phone-alt', 'fa-clipboard-list', 'fa-handshake', 'fa-truck-loading'];
  const steps = r.order.steps
    .map((step, i) => {
      const isFirst = i === 0;
      const isLast = i === r.order.steps.length - 1;
      const num = i + 1;
      return `            <li class="order-steps__step${isFirst ? ' order-steps__step--first' : ''}${isLast ? ' order-steps__step--last' : ''}">
                <div class="order-steps__track" aria-hidden="true">
                    <span class="order-steps__num">${num}</span>${isLast ? '' : '\n                    <span class="order-steps__connector"></span>'}
                </div>
                <div class="order-steps__card">
                    <i class="fas ${icons[i]}" aria-hidden="true"></i>
                    <h3 class="order-steps__title">${nb(step.title)}</h3>
                    <p>${nb(step.body)}</p>
                </div>
            </li>`;
    })
    .join('\n');

  return `<section class="order-steps order-steps--process section-light" id="order" aria-labelledby="order-title">
    <div class="section-shell">
        <div class="section-heading section-heading--center">
            <p class="section-eyebrow">Как заказать</p>
            <h2 class="section-title" id="order-title">${nb(r.order.title)}</h2>
        </div>

        <ol class="order-steps__flow" aria-label="Шаги заказа">
${steps}
        </ol>

        <div class="order-steps__cta">
            <a class="button button--primary" href="tel:+79004658331">Позвонить</a>
            <a class="button button--outline" href="#contacts" data-modal-open="modal-callback" data-cta-source="${r.prefix}-order-steps-quote" data-modal-title="${r.modalTitle}">${nb(r.order.secondaryCta)}</a>
        </div>
    </div>
</section>
`;
}

function pricingHtml(r) {
  const notes = r.pricing.notes
    .map(
      (text, i) => `                    <li>
                        <i class="fas ${i === 0 ? 'fa-file-invoice-dollar' : 'fa-clock'}" aria-hidden="true"></i>
                        <span>${nb(text)}</span>
                    </li>`,
    )
    .join('\n');

  const factors = r.pricing.factors
    .map((text, i) => `                    <li><i class="fas ${FACTOR_ICONS[i % FACTOR_ICONS.length]}" aria-hidden="true"></i><span>${nb(text)}</span></li>`)
    .join('\n');

  return `<section class="pricing-factors pricing-factors--system section-light" id="pricing" aria-labelledby="pricing-title">
    <div class="section-shell">
        <div class="section-heading section-heading--center">
            <p class="section-eyebrow">${nb(r.pricing.eyebrow)}</p>
            <h2 class="section-title" id="pricing-title">${nb(r.pricing.title)}</h2>
        </div>

        <div class="pricing-factors__layout">
            <aside class="pricing-factors__aside">
                <p class="pricing-factors__intro">${nb(r.pricing.intro)}</p>

                <ul class="pricing-factors__notes" aria-label="Условия расчёта">
${notes}
                </ul>

                <span class="pricing-factors__accent" aria-hidden="true"></span>

                <p class="pricing-factors__anchor">${nb(r.pricing.anchor)}</p>

                <div class="pricing-factors__cta">
                    <a class="button button--primary" href="#contacts" data-modal-open="modal-callback" data-cta-source="${r.prefix}-pricing-primary" data-modal-title="${r.modalTitle}">${nb(r.pricing.cta)}</a>
                </div>
            </aside>

            <div class="pricing-factors__panel">
                <p class="pricing-factors__panel-label">${nb(r.pricing.factorsLabel)}</p>
                <ul class="pricing-factors__list" aria-label="Факторы стоимости">
${factors}
                </ul>
            </div>
        </div>
    </div>
</section>
`;
}

function faqHtml(r) {
  const items = r.faq.items
    .map(
      (item, i) => `                    <details class="faq-item"${i === 0 ? ' open' : ''}>
                        <summary><span>${i + 1}.</span> ${item.q}</summary>
                        <div class="faq-item__body"><p>${nb(item.a)}</p></div>
                    </details>`,
    )
    .join('\n');

  return `<section class="faq faq--split-cta section-light section-light--upper" id="faq" aria-labelledby="faq-title">
    <div class="section-shell">
        <div class="faq__split">
            <div class="faq__split-main">
                <div class="section-heading">
                    <p class="section-eyebrow">FAQ</p>
                    <h2 class="faq__title" id="faq-title">Частые вопросы</h2>
                    <p class="section-lead">${nb(r.faq.lead)}</p>
                </div>
                <div class="faq__list">
${items}
                </div>
            </div>
            <aside class="faq__split-aside contact-cta contact-cta--embedded" id="contacts" aria-labelledby="contact-title">
                <div class="contact-cta__content">
                    <h2 id="contact-title">${nb(r.formsCta.title)}</h2>
                    <p>${nb(r.formsCta.lead)}</p>
                    <div class="contact-cta__channels" aria-label="Способы связи">
                        <a class="contact-cta__phone" href="tel:+79004658331"><i class="fas fa-phone-alt" aria-hidden="true"></i><span>+7&nbsp;(900)&nbsp;465-83-31</span></a>
                        <a href="#contacts" data-link-todo="max-url-required"><img src="/assets/img/social/MAX-ico.svg" alt="" width="28" height="28" decoding="async"><span>MAX<small>Написать</small></span></a>
                        <a href="#contacts" data-link-todo="telegram-url-required"><img src="/assets/img/social/Telegram-ico.svg" alt="" width="28" height="28" decoding="async"><span>Telegram<small>Написать</small></span></a>
                        <a href="https://wa.me/79004658331" target="_blank" rel="noopener noreferrer"><img src="/assets/img/social/WhatsApp-ico.svg" alt="" width="28" height="28" decoding="async"><span>WhatsApp<small>Написать</small></span></a>
                    </div>
                </div>
                <form class="contact-form" action="#" method="post" data-form data-form-id="${r.prefix}-contact-quote" data-page-type="${r.pageType}" data-form-name="Форма заявки" data-cta-source="${r.prefix}-contacts-inline" data-form-success="Спасибо! Заявка принята — скоро перезвоним и уточним детали." aria-label="Форма заявки">
                    <h3 class="contact-form__title">${nb(r.formsCta.formTitle)}</h3>
                    <p class="contact-form__note">${nb(r.formsCta.formNote)}</p>
                    <label><span>Имя</span><input type="text" name="name" placeholder="Ваше имя" autocomplete="name" required></label>
                    <label><span>Телефон</span><input type="tel" name="phone" placeholder="Телефон" autocomplete="tel" required></label>
                    <button class="button button--primary" type="submit">${nb(r.formsCta.submit)}</button>
                    <div class="site-form__field site-form__field--consent" data-form-field-wrap>
                        <label class="site-form__consent">
                            <input class="site-form__consent-input" type="checkbox" name="consent" value="1" data-validate="required consent" required>
                            <span class="site-form__consent-box" aria-hidden="true"></span>
                            <span class="site-form__consent-text">Я&nbsp;даю согласие на&nbsp;обработку персональных данных в&nbsp;соответствии с&nbsp;<a href="/consent-personal-data/" target="_blank">Согласием на&nbsp;обработку персональных данных</a> и&nbsp;соглашаюсь с&nbsp;<a href="/privacy-policy/" target="_blank">Политикой конфиденциальности</a>.</span>
                        </label>
                        <span class="site-form__error" data-form-error hidden>Подтвердите согласие на&nbsp;обработку данных</span>
                    </div>
                    <a class="contact-form__call button button--outline" href="tel:+79004658331" data-desktop-modal-open="modal-phone">Позвонить</a>
                </form>
            </aside>
        </div>
    </div>
</section>
`;
}

function pageHtml(r) {
  return `@@include("partials/layout/head-v5-page01.html", {"lang":"ru","title":"${r.pageTitle}","description":"${r.pageDescription}","robots":"noindex,nofollow","ogType":"website"})
<body id="top" data-page-type="${r.pageType}" data-landing-id="${r.landingId}">
    <div class="first-screen" aria-label="Первый экран">
        <div class="first-screen__bg" aria-hidden="true">
            <img
                class="first-screen__bg-media"
                src="/assets/img/hero/hero-bg-final.jpg"
                alt=""
                width="2560"
                height="1440"
                decoding="async"
                fetchpriority="high"
            >
        </div>
        <div class="first-screen__overlay" aria-hidden="true"></div>
        @@include("partials/layout/header-v5-page01.html", {"prefix": "${r.prefix}"})
        @@include("partials/sections/v5-ppc/${r.folder}/screen-01-hero.html")
    </div>

    <main class="landing-main" id="main">
        @@include("partials/sections/v5-ppc/${r.folder}/screen-02-specs.html")
        @@include("partials/sections/v5-ppc/${r.folder}/screen-02-tasks.html")
        @@include("partials/sections/v5-ppc/${r.folder}/screen-02b-order-steps.html")
        @@include("partials/sections/v5-ppc/${r.folder}/screen-02c-pricing-factors.html")
        @@include("partials/sections/v5-page01/screen-03-trust-reviews.html")
        @@include("partials/sections/v5-page01/screen-03b-b2b.html")
        @@include("partials/sections/v5-page01/dark-proof-strip.html")
        @@include("partials/sections/v5-ppc/${r.folder}/screen-04-faq.html")
    </main>

    @@include("partials/sections/v5-page01/landing-footer.html")
    @@include("partials/components/callback-modal.html", {"prefix": "${r.prefix}"})
    @@include("partials/layout/scripts-v5-page01.html")
</body>
</html>
`;
}

const DENIED = [
  'Грузы с неизвестным весом',
  'Негабарит без предварительного согласования',
  'Грузы вне параметров машины',
  'Опасные грузы',
  'Эвакуация техники',
];

const SPECS_BASE = [
  ['Грузоподъёмность борта', '5 т'],
  ['Грузоподъёмность стрелы', '3 т'],
  ['Вылет стрелы', '14 м'],
  ['Размер кузова', '6.2 × 2.2 м'],
  ['Минимальный заказ', '2 часа'],
];

const ROUTES = [
  {
    folder: 'kirpich-bloki',
    pageFile: 'kirpich-bloki.html',
    pageType: 'ppc-kirpich-bloki',
    landingId: 'kirpich-bloki',
    prefix: 'kirpich-bloki',
    pageTitle: 'Перевозка&nbsp;кирпича&nbsp;и&nbsp;блоков&nbsp;манипулятором&nbsp;в&nbsp;Краснодаре&nbsp;|&nbsp;Триумф',
    pageDescription: 'Доставка&nbsp;кирпича,&nbsp;блоков&nbsp;и&nbsp;стройматериалов&nbsp;манипулятором&nbsp;в&nbsp;Краснодаре&nbsp;и&nbsp;крае:&nbsp;борт&nbsp;5&nbsp;т,&nbsp;стрела&nbsp;3&nbsp;т,&nbsp;вылет&nbsp;14&nbsp;м.&nbsp;Расчет&nbsp;до&nbsp;выезда.',
    modalTitle: 'Рассчитаем доставку кирпича и блоков',
    hero: {
      h1: 'Перевозка кирпича и блоков манипулятором в Краснодаре',
      lead: 'Доставляем кирпич, блоки и другие стройматериалы на строительные объекты: берем на себя погрузку, перевозку и разгрузку стрелой в точке подачи по Краснодару и краю.',
      specs: ['Борт — 5 т', 'Стрела — 3 т', 'Вылет стрелы — 14 м', 'Кузов — 6.2 × 2.2 м', 'Минимальный заказ — 2 часа'],
      proof: ['Работаем по Краснодару и Краснодарскому краю', 'Делаем расчет до выезда по параметрам заявки', 'Доставляем стройматериалы на объект в согласованное время', 'Работаем в параметрах 5 т / 3 т / 14 м'],
      cargo: ['Кирпич', 'Блоки', 'Стройматериалы', 'Паллеты', 'Строительные грузы', 'Стройка'],
      cargoAria: 'Типовые грузы по кирпичу и блокам',
      formTitle: 'Оставьте имя и телефон',
      formLead: 'Перезвоним, уточним вес, объем и условия разгрузки на объекте.',
      formNote: 'Точный расчет делаем после уточнения параметров груза и маршрута.',
      formSubmit: 'Рассчитать стоимость',
    },
    specs: {
      eyebrow: 'Параметры техники',
      title: 'Параметры манипулятора для перевозки кирпича и блоков',
      lead: 'Блок помогает быстро понять, подходит ли машина под вашу задачу по доставке кирпича, блоков и других стройматериалов.',
      rows: SPECS_BASE,
      ops: 'Манипулятор подходит для перевозки кирпича, блоков, паллет и других строительных грузов в рамках параметров техники по весу и габаритам.',
      cta: 'Уточнить параметры груза',
      micro: 'Сообщите тип материала, вес, объем и условия на объекте, и мы сразу подтвердим возможность подачи и дадим расчет до выезда.',
      imgAlt: 'Манипулятор доставляет кирпич и блоки на строительный объект',
    },
    tasks: {
      eyebrow: 'Что выполняем по заявкам на кирпич и блоки',
      title: 'Задачи по доставке стройматериалов на объекты',
      allowed: ['Доставка кирпича на строительный объект', 'Перевозка блоков по Краснодару и краю', 'Доставка стройматериалов', 'Разгрузка паллет стрелой', 'Подача материалов на объект', 'Перевозка строительных грузов'],
      noteLabel: 'Важно перед подачей',
      noteText: 'Для точного расчета заранее уточняем тип и объем стройматериалов, вес, адреса, условия подъезда и точку разгрузки на объекте.',
      denied: DENIED,
      ctaEyebrow: 'Нужен расчет по кирпичу и блокам',
      ctaTitle: 'Проверим параметры и подтвердим подачу манипулятора',
      ctaText: 'Оставьте заявку или позвоните: уточним параметры груза и условия на объекте, после этого дадим расчет стоимости до выезда.',
      ctaPoints: ['Проверяем соответствие параметрам машины', 'Согласуем время подачи на объект', 'Рассчитываем стоимость до выезда'],
      ctaButton: 'Рассчитать стоимость',
    },
    order: {
      title: 'Как заказать доставку кирпича и блоков',
      steps: [
        { title: 'Позвоните или оставьте заявку', body: 'Принимаем заявку по телефону и через форму, чтобы сразу перейти к расчету доставки кирпича и блоков.' },
        { title: 'Собираем данные по стройматериалам и объекту', body: 'Уточняем тип груза, вес, объем, формат паллет, адреса и условия подъезда для подачи машины.' },
        { title: 'Проверяем задачу в параметрах манипулятора', body: 'Сверяем груз и условия разгрузки с возможностями машины, согласуем время и даем расчет до выезда.' },
        { title: 'Погрузка, перевозка и разгрузка на объекте', body: 'Подаем манипулятор в согласованное время, доставляем материалы и разгружаем стрелой в нужной точке на стройке.' },
      ],
      secondaryCta: 'Рассчитать стоимость',
    },
    pricing: {
      eyebrow: 'Расчет стоимости перевозки кирпича и блоков',
      title: 'Стоимость перевозки кирпича и блоков рассчитывается по параметрам задачи',
      intro: 'Итоговая стоимость зависит от объема стройматериалов, веса груза, маршрута, условий подъезда, объема разгрузки и объема работы стрелой на объекте.',
      notes: ['Без публикации фиктивных цен и ставок «от»', 'Точная стоимость только после расчета оператором'],
      anchor: 'Точная цена формируется после уточнения параметров груза и условий на адресах.',
      factorsLabel: 'Что влияет на стоимость',
      factors: ['Объем стройматериалов', 'Вес груза', 'Маршрут перевозки', 'Условия подъезда на погрузке и разгрузке', 'Объем разгрузки', 'Объем работы стрелой на объекте'],
      cta: 'Отправить параметры груза для расчета',
    },
    faq: {
      lead: 'Ответы по доставке кирпича, блоков и разгрузке на объекте.',
      items: [
        { q: 'Какие стройматериалы перевозите?', a: 'Перевозим кирпич, блоки, паллеты и другие строительные материалы в рамках параметров машины по весу и габаритам.' },
        { q: 'Как понять, подойдёт ли манипулятор?', a: 'Перед выездом сверяем тип груза, вес, объем, упаковку и условия на объекте. После проверки подтверждаем, подходит ли машина под вашу задачу.' },
        { q: 'Можно ли разгрузить паллеты стрелой?', a: 'Да, если вес паллет, вылет и площадка позволяют безопасно выполнить разгрузку стрелой.' },
        { q: 'Что влияет на стоимость?', a: 'На цену влияют объем и вес стройматериалов, маршрут, условия подъезда, объем разгрузки и объем работы стрелой.' },
        { q: 'Работаете ли по краю?', a: 'Да, выполняем перевозки по Краснодару и Краснодарскому краю.' },
        { q: 'Что нужно для расчёта?', a: 'Нужны тип материала, вес, объем, адрес погрузки, адрес разгрузки и краткое описание условий на объекте.' },
        { q: 'Что не перевозите?', a: 'Не берем грузы с неизвестным весом, негабарит без согласования, опасные грузы, позиции вне параметров машины и заявки на эвакуацию техники.' },
      ],
    },
    formsCta: {
      title: 'Нужна доставка кирпича и блоков манипулятором на объект?',
      lead: 'Свяжитесь с нами, уточним параметры груза и подготовим расчет до выезда.',
      formTitle: 'Оставьте имя и телефон',
      formNote: 'Перезвоним, уточним вес, объем и условия разгрузки на объекте.',
      submit: 'Рассчитать стоимость',
    },
  },
  {
    folder: 'stroymaterialy',
    pageFile: 'stroymaterialy.html',
    pageType: 'ppc-stroymaterialy',
    landingId: 'stroymaterialy',
    prefix: 'stroymaterialy',
    pageTitle: 'Перевозка&nbsp;стройматериалов&nbsp;манипулятором&nbsp;в&nbsp;Краснодаре&nbsp;|&nbsp;Триумф',
    pageDescription: 'Доставка&nbsp;стройматериалов&nbsp;манипулятором&nbsp;в&nbsp;Краснодаре&nbsp;и&nbsp;крае:&nbsp;погрузка,&nbsp;перевозка&nbsp;и&nbsp;разгрузка&nbsp;на&nbsp;объекте.&nbsp;Расчет&nbsp;до&nbsp;выезда.',
    modalTitle: 'Рассчитаем доставку стройматериалов',
    hero: {
      h1: 'Перевозка стройматериалов манипулятором в Краснодаре',
      lead: 'Организуем доставку, погрузку и разгрузку стройматериалов на строительные объекты: подаем машину в согласованное время и выполняем поставку на стройку по Краснодару и краю.',
      specs: ['Борт — 5 т', 'Стрела — 3 т', 'Вылет стрелы — 14 м', 'Кузов — 6.2 × 2.2 м', 'Минимальный заказ — 2 часа'],
      proof: ['Работаем по Краснодару и Краснодарскому краю', 'Делаем расчет до выезда по параметрам заявки', 'Доставляем материалы на объект в согласованное время', 'Параметры машины: 5 т / 3 т / 14 м'],
      cargo: ['Стройматериалы', 'Кирпич', 'Блоки', 'Арматура', 'Паллеты', 'Строительные грузы'],
      cargoAria: 'Типовые стройматериалы',
      formTitle: 'Рассчитать доставку стройматериалов',
      formLead: 'Отправьте параметры груза: подготовим расчет до выезда и согласуем подачу машины на строительный объект.',
      formNote: 'Перезвоним и уточним: тип груза · адрес подачи · возможность работы · ориентировочную стоимость.',
      formSubmit: 'Рассчитать стоимость',
    },
    specs: {
      eyebrow: 'Техника для доставки стройматериалов на стройку',
      title: 'Параметры манипулятора под строительные грузы',
      lead: 'Одна машина с понятными параметрами для подрядчиков: погрузка, доставка и разгрузка материалов на объекте в согласованных условиях.',
      rows: [
        ['Грузоподъёмность борта', 'до 5 т'],
        ['Грузоподъёмность стрелы', 'до 3 т'],
        ['Вылет стрелы', 'до 14 м'],
        ['Размер кузова', '6.2 × 2.2 м'],
        ['Формат работы', 'погрузка, доставка и разгрузка на объекте'],
      ],
      ops: 'Перед выездом проверяем соответствие груза параметрам машины, условиям подъезда и точке подачи на объекте.',
      cta: 'Уточнить параметры груза',
      micro: 'Сообщите тип материалов, вес, объем и условия на объекте — подтвердим возможность подачи и дадим расчет до выезда.',
      imgAlt: 'Манипулятор доставляет стройматериалы на строительный объект',
    },
    tasks: {
      eyebrow: 'Какие задачи выполняем по строительной логистике',
      title: 'Доставка и подача стройматериалов на объект',
      allowed: ['Доставка стройматериалов', 'Подача материалов на объект', 'Разгрузка паллет стрелой', 'Перевозка строительных грузов', 'Доставка кирпича и блоков', 'Перевозка арматуры'],
      noteLabel: 'Важно перед подачей',
      noteText: 'Для расчета заранее уточняем вес и объем груза, формат упаковки, маршрут, условия подъезда и требования к разгрузке стрелой на стройплощадке.',
      denied: DENIED,
      ctaEyebrow: 'Нужен расчет под вашу поставку',
      ctaTitle: 'Проверим поставку стройматериалов до выезда',
      ctaText: 'Оставьте заявку или позвоните: уточним параметры материалов, проверим условия погрузки и разгрузки и дадим расчет до подачи машины.',
      ctaPoints: ['Проверяем соответствие груза параметрам техники', 'Учитываем условия подъезда и разгрузки на объекте', 'Считаем стоимость до выезда'],
      ctaButton: 'Рассчитать стоимость',
    },
    order: {
      title: 'Как заказать доставку стройматериалов',
      steps: [
        { title: 'Позвоните или оставьте заявку', body: 'Принимаем заявку по телефону и через форму, чтобы сразу перейти к расчету доставки материалов на объект.' },
        { title: 'Собираем данные по материалам и объекту', body: 'Уточняем тип материалов, вес, объем, формат упаковки, адреса и условия подъезда для подачи машины.' },
        { title: 'Проверяем задачу в параметрах манипулятора', body: 'Сверяем груз и условия разгрузки с возможностями машины, согласуем время и подтверждаем расчет до выезда.' },
        { title: 'Погрузка, перевозка и разгрузка на стройке', body: 'Подаем манипулятор в согласованное время, доставляем материалы на объект и разгружаем стрелой в точке подачи.' },
      ],
      secondaryCta: 'Рассчитать стоимость',
    },
    pricing: {
      eyebrow: 'Расчет стоимости по доставке стройматериалов',
      title: 'Стоимость перевозки стройматериалов рассчитываем до выезда',
      intro: 'Итоговая стоимость зависит от объема и веса материалов, маршрута и условий подачи и разгрузки на объекте.',
      notes: ['Публичную фиксированную ставку не указываем без данных по заявке.', 'Точный расчет даем после уточнения параметров материалов и условий подачи машины.'],
      anchor: 'Точная сумма формируется по реальным условиям доставки стройматериалов на ваш объект.',
      factorsLabel: 'Что влияет на стоимость',
      factors: ['Объем материалов', 'Вес груза', 'Маршрут перевозки', 'Условия подъезда к точке подачи', 'Условия разгрузки на объекте', 'Объем работы стрелой'],
      cta: 'Отправить параметры груза для расчета',
    },
    faq: {
      lead: 'Ответы по доставке стройматериалов, параметрам техники и стоимости.',
      items: [
        { q: 'Какие стройматериалы перевозите?', a: 'Перевозим кирпич, блоки, арматуру, паллетированные материалы и другие строительные грузы в рамках параметров машины.' },
        { q: 'Как понять, подойдёт ли манипулятор?', a: 'Перед выездом сверяем тип груза, вес, объем, упаковку и условия на объекте. После проверки подтверждаем, подходит ли машина под вашу задачу.' },
        { q: 'Можно ли разгрузить материалы стрелой?', a: 'Да, если вес груза, вылет стрелы и площадка позволяют безопасно выполнить разгрузку в точке подачи.' },
        { q: 'Что влияет на стоимость?', a: 'На цену влияют объем материалов, вес, маршрут, условия подъезда, сложность разгрузки и время работы стрелой.' },
        { q: 'Работаете ли по краю?', a: 'Да, выполняем перевозки по Краснодару и Краснодарскому краю.' },
        { q: 'Что нужно для расчёта?', a: 'Нужны тип стройматериалов, вес, объем, формат упаковки, адрес погрузки, адрес разгрузки и краткое описание условий подъезда и разгрузки.' },
        { q: 'Что не перевозите?', a: 'Не берем грузы с неизвестным весом, негабарит без согласования, грузы вне параметров машины, опасные грузы и заявки на эвакуацию техники.' },
      ],
    },
    formsCta: {
      title: 'Нужна доставка стройматериалов манипулятором на объект?',
      lead: 'Свяжитесь с нами — уточним параметры материалов и подготовим расчет до выезда.',
      formTitle: 'Оставьте имя и телефон',
      formNote: 'Перезвоним, уточним тип материалов, вес, объем и условия разгрузки.',
      submit: 'Рассчитать стоимость',
    },
  },
  {
    folder: 'vezdehod',
    pageFile: 'vezdehod.html',
    pageType: 'ppc-vezdehod',
    landingId: 'vezdehod',
    prefix: 'vezdehod',
    pageTitle: 'Манипулятор-вездеход&nbsp;в&nbsp;Краснодаре&nbsp;|&nbsp;Триумф',
    pageDescription: 'Манипулятор-вездеход&nbsp;6×6&nbsp;для&nbsp;сложного&nbsp;подъезда&nbsp;и&nbsp;объектов&nbsp;вне&nbsp;асфальта:&nbsp;борт&nbsp;5&nbsp;т,&nbsp;стрела&nbsp;3&nbsp;т.&nbsp;Расчёт&nbsp;до&nbsp;выезда.',
    modalTitle: 'Уточнить возможность подачи',
    hero: {
      h1: 'Манипулятор-вездеход в Краснодаре',
      lead: 'Подаём и перевозим грузы в сложных условиях: на стройке, участке и объектах с проблемным подъездом, грунтом и ограниченным проходом. Работаем по Краснодару и краю — расчёт до выезда.',
      specs: ['Борт — 5 т', 'Стрела — 3 т', 'Вылет стрелы — 14 м', 'Полный привод — 6×6', 'Минимальный заказ — 2 часа'],
      proof: ['Работаем по Краснодару и Краснодарскому краю', 'Берём задачи со сложными условиями подачи', 'Делаем расчёт до выезда по параметрам заявки', 'Параметры машины: 5 т / 3 т / 14 м'],
      cargo: ['Стройматериалы', 'Бытовки', 'Контейнеры', 'Грузы на участок', 'Объекты', 'Сложный подъезд'],
      cargoAria: 'Типовые задачи для вездехода',
      formTitle: 'Рассчитать стоимость',
      formLead: 'Оставьте имя и телефон — перезвоним и уточним задачу на объекте.',
      formNote: 'Точный расчёт делаем после уточнения груза, маршрута и условий подъезда.',
      formSubmit: 'Рассчитать стоимость',
    },
    specs: {
      eyebrow: 'Параметры техники для сложных условий',
      title: 'Манипулятор-вездеход для работы на объектах с трудным подъездом',
      lead: 'Полный привод 6×6 и рабочие параметры стрелы помогают заранее понять, подходит ли машина для вашего участка, стройки или объекта без нормального покрытия.',
      rows: [
        ['Грузоподъёмность борта', '5 т'],
        ['Грузоподъёмность стрелы', '3 т'],
        ['Вылет стрелы', '14 м'],
        ['Кузов', '6.2 × 2.2 м'],
        ['Привод', '6×6'],
        ['Минимальный заказ', '2 часа'],
      ],
      ops: 'Работаем на стройплощадках, грунтовых дорогах, участках со сложным подъездом, загородных и строительных объектах. Перед подачей согласуем состояние подъезда, тип покрытия, особенности территории и возможность погрузки, перевозки и разгрузки стрелой.',
      cta: 'Уточнить возможность подачи',
      micro: 'Сообщите адрес объекта, тип груза, примерный вес и кратко опишите подъезд — подскажем, подходит ли вездеход и когда возможна подача.',
      imgAlt: 'Манипулятор-вездеход 6×6 на строительном объекте с грунтовым подъездом в Краснодаре',
    },
    tasks: {
      eyebrow: 'Задачи на сложном подъезде и на объектах',
      title: 'Что выполняем манипулятором-вездеходом',
      allowed: ['Доставка на участок', 'Работа на стройке', 'Подача материалов в сложных условиях', 'Перевозка бытовок', 'Перевозка контейнеров', 'Работа на грунте'],
      noteLabel: 'Важно перед подачей',
      noteText: 'Для расчёта заранее уточняем тип груза, примерный вес, адрес объекта, состояние подъезда, покрытие дороги и условия разгрузки стрелой на площадке.',
      denied: DENIED,
      ctaEyebrow: 'Нужен расчёт под ваш объект',
      ctaTitle: 'Проверим возможность подачи до выезда',
      ctaText: 'Оставьте заявку или позвоните: уточним подъезд, параметры груза и условия работы на объекте, после этого дадим расчёт.',
      ctaPoints: ['Проверяем проходимость и условия подъезда', 'Сверяем груз с параметрами борта и стрелы', 'Считаем стоимость до выезда'],
      ctaButton: 'Рассчитать стоимость',
    },
    order: {
      title: 'Как заказать манипулятор-вездеход',
      steps: [
        { title: 'Позвоните или оставьте заявку', body: 'Принимаем заявку по телефону и через форму, чтобы сразу перейти к проверке возможности подачи на объект.' },
        { title: 'Уточняем условия подъезда и задачу', body: 'Собираем адрес, тип груза, примерный вес, состояние дороги и подъезда, а также требования к разгрузке на площадке.' },
        { title: 'Согласуем возможность работы до выезда', body: 'Проверяем, подходит ли вездеход под ваш объект, согласуем время подачи и фиксируем расчёт до выезда техники.' },
        { title: 'Подача, перевозка и разгрузка', body: 'Подаём машину в согласованное время, выполняем погрузку, перевозку и разгрузку стрелой по согласованным параметрам.' },
      ],
      secondaryCta: 'Рассчитать стоимость',
    },
    pricing: {
      eyebrow: 'Расчёт стоимости по условиям объекта',
      title: 'Стоимость работы вездехода рассчитываем до выезда',
      intro: 'Итоговая сумма зависит не только от расстояния, но и от сложности подъезда, состояния дороги, условий разгрузки и параметров груза на объекте.',
      notes: ['Публичную фиксированную ставку не указываем без данных по заявке.', 'Точный расчёт даём после уточнения подъезда, маршрута и условий работы на площадке.'],
      anchor: 'Точная сумма формируется по реальным условиям подачи на ваш объект — согласуем её до выезда техники.',
      factorsLabel: 'Что влияет на стоимость',
      factors: ['Сложность подъезда и проходимость участка', 'Состояние дороги и покрытия на маршруте', 'Маршрут и расстояние', 'Условия разгрузки на объекте', 'Необходимость и объём работы стрелой', 'Тип, вес и габариты груза'],
      cta: 'Отправить параметры задачи для расчёта',
    },
    faq: {
      lead: 'Ответы по работе вездехода, подъезду и стоимости.',
      items: [
        { q: 'Где может работать манипулятор-вездеход?', a: 'На стройплощадках, участках, грунтовых дорогах и объектах со сложным подъездом — там, где обычному манипулятору трудно пройти. Перед выездом уточняем адрес и состояние территории.' },
        { q: 'Можно ли подать машину на участок?', a: 'Да, если по описанию подъезда, покрытия и параметров груза подтверждаем возможность безопасной подачи и работы. Сообщите адрес и особенности участка — подскажем до выезда.' },
        { q: 'Что влияет на стоимость?', a: 'На расчёт влияют сложность подъезда, состояние дороги, маршрут, условия разгрузки, время и объём работы стрелой, а также тип и вес груза.' },
        { q: 'Работаете ли по краю?', a: 'Да, выполняем заявки по Краснодару, пригородам и Краснодарскому краю.' },
        { q: 'Что нужно для расчёта?', a: 'Нужны адрес объекта, тип груза, примерный вес, краткое описание подъезда и дороги, адреса погрузки и разгрузки, а также нужна ли работа стрелой.' },
        { q: 'Какие грузы перевозите?', a: 'Стройматериалы, бытовки, контейнеры, оборудование и другие грузы на участок или объект — в пределах параметров борта 5 т и стрелы 3 т при согласованных условиях подъезда.' },
        { q: 'Что не перевозите?', a: 'Не берём грузы с неизвестным весом, негабарит без согласования, грузы вне параметров машины, опасные грузы и заявки на эвакуацию техники.' },
      ],
    },
    formsCta: {
      title: 'Нужно уточнить подачу на объект со сложным подъездом?',
      lead: 'Свяжитесь с нами — проверим возможность работы вездехода, условия подъезда и дадим расчёт до выезда.',
      formTitle: 'Оставьте имя и телефон',
      formNote: 'Перезвоним и уточним: тип груза, адрес объекта, подъезд и ориентировочную стоимость.',
      submit: 'Рассчитать стоимость',
    },
  },
  {
    folder: 'yurlic',
    pageFile: 'yurlic.html',
    pageType: 'ppc-yurlic',
    landingId: 'yurlic',
    prefix: 'yurlic',
    pageTitle: 'Манипулятор&nbsp;для&nbsp;юридических&nbsp;лиц&nbsp;в&nbsp;Краснодаре&nbsp;|&nbsp;Триумф',
    pageDescription: 'Подача&nbsp;манипулятора&nbsp;для&nbsp;организаций&nbsp;и&nbsp;подрядчиков:&nbsp;поставки&nbsp;на&nbsp;объекты,&nbsp;безнал,&nbsp;расчёт&nbsp;до&nbsp;выезда.',
    modalTitle: 'Рассчитать подачу на объект',
    hero: {
      h1: 'Манипулятор для юридических лиц в Краснодаре',
      lead: 'Организуем подачу манипулятора для организаций, подрядчиков и строительных объектов: согласуем поставки материалов и оборудования, условия разгрузки и расчёт до выезда по Краснодару и краю.',
      specs: ['Борт — 5 т', 'Стрела — 3 т', 'Вылет стрелы — 14 м', 'Кузов — 6.2 × 2.2 м', 'Минимальный заказ — 2 часа'],
      proof: ['Работа с юридическими лицами', 'Расчёт до выезда', 'Поставки на объекты', 'Параметры машины: 5 т / 3 т / 14 м'],
      cargo: ['Стройматериалы', 'Оборудование', 'Бытовки', 'Контейнеры', 'Поставки на объект', 'Снабжение'],
      cargoAria: 'Типовые поставки для организаций',
      formTitle: 'Получить расчёт',
      formLead: 'Оставьте контакты — уточним объект, поставку и условия подачи.',
      formNote: 'Перезвоним: тип задачи · объект · возможность работы · ориентировочный расчёт.',
      formSubmit: 'Получить расчёт',
    },
    specs: {
      eyebrow: 'Техника для работы с организациями на объекте',
      title: 'Манипулятор для поставок и задач на строительных объектах',
      lead: 'Одна машина с понятными параметрами для подрядчиков и юридических лиц: погрузка, подача на объект и разгрузка стрелой в согласованных условиях.',
      rows: SPECS_BASE,
      ops: 'Подбираем подачу под задачу организации: стройматериалы, оборудование, бытовки, контейнеры и снабжение объекта с учётом графика работ и условий площадки. Работаем с юридическими лицами — доступны наличный и безналичный расчёт.',
      cta: 'Уточнить условия подачи',
      micro: 'Сообщите объект, тип поставки, параметры груза и желаемое время — подготовим расчёт и подтвердим возможность работы.',
      imgAlt: 'Манипулятор на строительном объекте в Краснодаре — подача и разгрузка для организации',
    },
    tasks: {
      eyebrow: 'Задачи для организаций и строительных объектов',
      title: 'Что организуем для юридических лиц и подрядчиков',
      allowed: ['Поставки на строительные объекты', 'Работа с подрядчиками', 'Доставка стройматериалов', 'Перевозка оборудования', 'Подача бытовок', 'Разгрузка стрелой на объекте'],
      noteLabel: 'Важно перед подачей',
      noteText: 'Для расчёта заранее уточняем объект, график подачи, параметры груза, условия подъезда и требования к разгрузке на площадке.',
      denied: DENIED,
      ctaEyebrow: 'Нужен расчёт под объект',
      ctaTitle: 'Согласуем подачу до выезда',
      ctaText: 'Оставьте заявку или позвоните: уточним объект, параметры поставки и условия работы, после чего дадим расчёт.',
      ctaPoints: ['Работаем с юридическими лицами', 'Учитываем график подачи и условия объекта', 'Подтверждаем стоимость до выезда'],
      ctaButton: 'Получить расчёт',
    },
    order: {
      title: 'Как заказать манипулятор для организации',
      steps: [
        { title: 'Позвоните или оставьте заявку', body: 'Принимаем заявку от организации по телефону и через форму — переходим к уточнению объекта и условий подачи.' },
        { title: 'Собираем данные по поставке', body: 'Уточняем юридическое лицо, объект, тип груза, параметры, адреса, график подачи и условия разгрузки.' },
        { title: 'Подтверждаем возможность работы', body: 'Сверяем груз с параметрами машины, согласуем время подачи, формат оплаты и расчёт до выезда.' },
        { title: 'Выполняем поставку по согласованию', body: 'Подаём манипулятор в согласованное время, выполняем погрузку, доставку и разгрузку стрелой на объекте.' },
      ],
      secondaryCta: 'Рассчитать подачу',
    },
    pricing: {
      eyebrow: 'Расчёт стоимости для организаций',
      title: 'Стоимость согласуем по объёму работ и условиям на объекте',
      intro: 'Итоговая сумма зависит от параметров поставки, маршрута, графика подачи и реальных условий разгрузки на площадке — без публичных «фиксированных» ставок без данных по заявке.',
      notes: ['Публичную фиксированную цену не указываем без уточнения задачи организации.', 'Точный расчёт даём после получения данных по объекту, грузу и графику работ.'],
      anchor: 'Сумму подтверждаем до выезда техники — после проверки параметров груза и условий на объекте.',
      factorsLabel: 'Что влияет на стоимость',
      factors: ['Объём работ', 'Маршрут', 'График подачи', 'Условия разгрузки', 'Работа стрелой', 'Параметры груза'],
      cta: 'Получить расчёт по заявке',
    },
    faq: {
      lead: 'Ответы для организаций и подрядчиков по подаче и оплате.',
      items: [
        { q: 'Работаете ли с юридическими лицами?', a: 'Да. Работаем с организациями, подрядчиками, строительными и коммерческими объектами. Заявку можно оформить от юридического лица — условия согласуем до выезда.' },
        { q: 'Есть ли безналичная оплата?', a: 'Да. Доступны наличный и безналичный расчёт. Формат оплаты и комплект документов уточняем по заявке.' },
        { q: 'Можно ли организовать поставки на объект?', a: 'Да. Организуем подачу на строительный или коммерческий объект с учётом графика работ, подъезда и разгрузки стрелой в согласованной точке.' },
        { q: 'Что влияет на стоимость?', a: 'На расчёт влияют объём работ, маршрут, график подачи, условия разгрузки, необходимость работы стрелой и параметры груза.' },
        { q: 'Работаете ли по краю?', a: 'Да. Подаём технику по Краснодару, пригородам и Краснодарскому краю.' },
        { q: 'Что нужно для расчёта?', a: 'Нужны данные организации для связи, объект или адреса, тип поставки, параметры груза, желаемое время подачи и краткое описание условий на площадке.' },
        { q: 'Какие грузы не перевозите?', a: 'Не берём грузы с неизвестным весом, негабарит без согласования, грузы вне параметров машины, опасные грузы и заявки на эвакуацию техники.' },
      ],
    },
    formsCta: {
      title: 'Нужно согласовать подачу манипулятора на объект?',
      lead: 'Свяжитесь с нами — уточним технику, график подачи и расчёт до выезда.',
      formTitle: 'Оставьте имя и телефон',
      formNote: 'Перезвоним и уточним объект, параметры поставки и условия работы.',
      submit: 'Уточнить условия',
    },
  },
  {
    folder: 'kray',
    pageFile: 'kray.html',
    pageType: 'ppc-kray',
    landingId: 'kray',
    prefix: 'kray',
    pageTitle: 'Манипулятор&nbsp;по&nbsp;Краснодарскому&nbsp;краю&nbsp;|&nbsp;Триумф',
    pageDescription: 'Выезд&nbsp;манипулятора&nbsp;по&nbsp;Краснодарскому&nbsp;краю:&nbsp;доставка&nbsp;на&nbsp;объекты,&nbsp;межгород,&nbsp;расчёт&nbsp;до&nbsp;выезда.',
    modalTitle: 'Уточнить маршрут и выезд',
    hero: {
      h1: 'Манипулятор по Краснодарскому краю',
      lead: 'Выезжаем на объекты по Краснодарскому краю: доставляем и подаём грузы на стройплощадки, базы и удалённые точки — в том числе за пределами города. Маршрут, подъезд и параметры груза согласуем до выезда.',
      specs: ['Борт — 5 т', 'Стрела — 3 т', 'Вылет стрелы — 14 м', 'Кузов — 6.2 × 2.2 м', 'Минимальный заказ — 2 часа'],
      proof: ['Работа по Краснодарскому краю', 'Выезд на объекты', 'Расчёт до выезда', 'Параметры машины: 5 т / 3 т / 14 м'],
      cargo: ['Стройматериалы', 'Бытовки', 'Контейнеры', 'Оборудование', 'Объекты по краю', 'Межгород'],
      cargoAria: 'Типовые перевозки по краю',
      formTitle: 'Рассчитать выезд',
      formLead: 'Оставьте имя и телефон — перезвоним и уточним маршрут и объект.',
      formNote: 'Точный расчёт делаем после уточнения маршрута, груза и условий подъезда.',
      formSubmit: 'Рассчитать выезд',
    },
    specs: {
      eyebrow: 'Техника для работ по Краснодарскому краю',
      title: 'Манипулятор для выезда на объекты и перевозок по краю',
      lead: 'Одна машина с понятными параметрами для региональных заявок: погрузка, доставка по маршруту и разгрузка стрелой на объекте — с согласованием подъезда и расстояния до выезда.',
      rows: SPECS_BASE,
      ops: 'Выезжаем на объекты и населённые пункты по Краснодарскому краю, пригородные и загородные площадки, строительные и производственные объекты, межгородские маршруты в пределах согласованной зоны. Перед подачей согласуем маршрут, расстояние, условия подъезда и возможность работы стрелой.',
      cta: 'Уточнить маршрут и выезд',
      micro: 'Сообщите адреса подачи и разгрузки, тип груза, примерный вес и кратко опишите подъезд — подскажем возможность работы и подготовим расчёт до выезда.',
      imgAlt: 'Манипулятор на маршруте по Краснодарскому краю — доставка груза на строительный объект',
    },
    tasks: {
      eyebrow: 'Задачи по краю и на удалённых объектах',
      title: 'Что выполняем при выезде по Краснодарскому краю',
      allowed: ['Доставка по Краснодарскому краю', 'Выезд на удалённые объекты', 'Перевозка стройматериалов', 'Перевозка бытовок', 'Доставка оборудования', 'Разгрузка стрелой на объекте'],
      noteLabel: 'Важно перед выездом',
      noteText: 'Для расчёта заранее уточняем маршрут, расстояние, адреса подачи и разгрузки, тип и вес груза, условия подъезда и необходимость работы стрелой на площадке.',
      denied: DENIED,
      ctaEyebrow: 'Нужен расчёт выезда по маршруту',
      ctaTitle: 'Согласуем маршрут и подачу до выезда',
      ctaText: 'Оставьте заявку или позвоните: уточним объект, маршрут и условия подъезда, после этого дадим расчёт.',
      ctaPoints: ['Проверяем маршрут и возможность подачи', 'Сверяем груз с параметрами борта и стрелы', 'Считаем стоимость до выезда'],
      ctaButton: 'Рассчитать выезд',
    },
    order: {
      title: 'Как заказать выезд манипулятора по краю',
      steps: [
        { title: 'Позвоните или оставьте заявку', body: 'Принимаем заявку по телефону и через форму, чтобы перейти к расчёту выезда по маршруту.' },
        { title: 'Собираем данные по перевозке', body: 'Уточняем адреса подачи и разгрузки, расстояние, тип груза, примерный вес, условия подъезда и требования к разгрузке на объекте.' },
        { title: 'Согласуем возможность работы до выезда', body: 'Проверяем маршрут, соответствие груза параметрам машины, время подачи и фиксируем расчёт до выезда техники.' },
        { title: 'Подача, доставка и разгрузка', body: 'Подаём манипулятор по согласованному маршруту, доставляем груз и выполняем разгрузку стрелой в точке работы.' },
      ],
      secondaryCta: 'Рассчитать выезд',
    },
    pricing: {
      eyebrow: 'Расчёт стоимости по маршруту',
      title: 'Стоимость выезда по краю рассчитываем до подачи техники',
      intro: 'Итоговая сумма зависит от расстояния, маршрута, условий подъезда на объекте, времени работы, разгрузки и параметров груза — без публичных «фиксированных» ставок без данных по заявке.',
      notes: ['Публичную фиксированную цену не указываем без уточнения маршрута и задачи.', 'Точный расчёт даём после получения адресов, расстояния, параметров груза и условий подъезда.'],
      anchor: 'Сумму согласуем до выезда — после проверки маршрута, груза и условий на объекте.',
      factorsLabel: 'Что влияет на стоимость',
      factors: ['Расстояние и маршрут', 'Условия подъезда в точке подачи и разгрузки', 'Время работы и ожидания', 'Разгрузка и объём работы стрелой', 'Тип, вес и габариты груза', 'Межгородской участок маршрута'],
      cta: 'Отправить маршрут и параметры груза для расчёта',
    },
    faq: {
      lead: 'Ответы по выездам по Краснодарскому краю и межгороду.',
      items: [
        { q: 'По каким районам работаете?', a: 'Выполняем выезды по Краснодарскому краю: на объекты в районах края, в пригородных и загородных точках, на строительные и производственные площадки. Конкретный маршрут и возможность подачи подтверждаем по заявке до выезда.' },
        { q: 'Можно ли заказать выезд за Краснодар?', a: 'Да, при согласовании маршрута, расстояния, условий подъезда и параметров груза. Сообщите адреса подачи и разгрузки — проверим возможность работы и подготовим расчёт.' },
        { q: 'Что влияет на стоимость?', a: 'На расчёт влияют расстояние, маршрут, условия подъезда, время работы, разгрузка стрелой, тип и вес груза, а также межгородской участок перевозки.' },
        { q: 'Как рассчитывается межгород?', a: 'Учитываем расстояние между точками, время в пути, условия подъезда на объекте, параметры груза и объём работы стрелой. После уточнения маршрута даём расчёт до выезда — без скрытых доплат после подачи.' },
        { q: 'Что нужно для расчёта?', a: 'Нужны адрес подачи, адрес разгрузки, тип груза, примерный вес, краткое описание подъезда, нужна ли разгрузка стрелой и желаемое время работы.' },
        { q: 'Какие грузы перевозите?', a: 'Стройматериалы, бытовки, контейнеры, оборудование и другие грузы на объекты по краю — в пределах параметров борта 5 т и стрелы 3 т при согласованных условиях маршрута и подъезда.' },
        { q: 'Что не перевозите?', a: 'Не берём грузы с неизвестным весом, негабарит без согласования, грузы вне параметров машины, опасные грузы и заявки на эвакуацию техники.' },
      ],
    },
    formsCta: {
      title: 'Нужен выезд манипулятора по Краснодарскому краю?',
      lead: 'Свяжитесь с нами — уточним маршрут, объект и дадим расчёт до выезда.',
      formTitle: 'Оставьте имя и телефон',
      formNote: 'Перезвоним и уточним адреса, тип груза, подъезд и ориентировочную стоимость.',
      submit: 'Получить расчёт',
    },
  },
];

for (const r of ROUTES) {
  const dir = path.join(PARTIALS, r.folder);
  fs.mkdirSync(dir, { recursive: true });
  const files = {
    'screen-01-hero.html': heroHtml(r),
    'screen-02-specs.html': specsHtml(r),
    'screen-02-tasks.html': tasksHtml(r),
    'screen-02b-order-steps.html': orderHtml(r),
    'screen-02c-pricing-factors.html': pricingHtml(r),
    'screen-04-faq.html': faqHtml(r),
  };
  for (const [name, content] of Object.entries(files)) {
    fs.writeFileSync(path.join(dir, name), content, 'utf8');
  }
  fs.writeFileSync(path.join(PAGES, r.pageFile), pageHtml(r), 'utf8');
  console.log(`OK ${r.folder}`);
}

console.log('Done — 5 routes × 6 partials + 5 pages');
