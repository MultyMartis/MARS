#!/usr/bin/env node
/** Generate FP-0002 Demo 1 template-clone source pages (Phase 07C-B) */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const PAGES = path.resolve(__dirname, '../src/pages');

const HEADER_PARAMS = '{"activeNavUslugiClass": "", "activeNavOffcanvasClass": "", "activeNavUslugiAria": "", "activeNavOtzyvyClass": "", "activeNavOtzyvyOffcanvasClass": "", "activeNavOtzyvyAria": "", "activeNavKontaktyClass": "", "activeNavKontaktyOffcanvasClass": "", "activeNavKontaktyAria": "", "activeNavBlogClass": "", "activeNavBlogOffcanvasClass": "", "activeNavBlogAria": ""}';

const FOOT = `  @@include('partials/layout/footer.html')
  @@include('partials/components/modal-consultation.html')
  <script src="assets/vendor/swiper/swiper-bundle.min.js" defer></script>
  <script src="assets/vendor/fancybox/fancybox.umd.js" defer></script>
  <script src="https://cdn.jsdelivr.net/npm/inputmask@5.0.9/dist/inputmask.min.js" defer></script>
  <script src="assets/js/main.js" defer></script>
</body>
</html>`;

function shell({ title, description, canonical, bodyClass, dataPage, mainClass, breadcrumb, mainContent }) {
  return `<!DOCTYPE html>
<html lang="ru">
<head>
  @@include('partials/layout/head.html', {"title": "${title}", "description": "${description}", "canonical": "${canonical}", "robots": "noindex, nofollow", "ogType": "website", "ogTitle": "${title}", "ogDescription": "${description}", "ogUrl": "${canonical}", "ogImage": "https://shpigovsky.ru/assets/img/social/og-default.jpg", "ogImageAlt": "${title}"})
</head>
<body class="${bodyClass}" data-page="${dataPage}" data-content-status="demo-placeholder">
  @@include('partials/layout/header.html', ${HEADER_PARAMS})
  <main class="${mainClass}">
    ${breadcrumb}
    ${mainContent}
    @@include('partials/sections/final-form.html', {"leadSource": "${dataPage}-final", "headingId": "${dataPage}-final-heading", "headingText": "Остались вопросы?", "leadText": "Опишите вашу ситуацию в&nbsp;форме заявки, и&nbsp;мы расскажем, как сможем помочь", "sectionModifierClass": ""})
  </main>
${FOOT}`;
}

function breadcrumb(params) {
  return `@@include('partials/components/internal-page-nav.html', ${JSON.stringify({ ...params, listHtml: '' }).replace(/"listHtml":""/, '"listHtml": ""')})`;
}

function plainSection(titleId, pageTitle, bodyHtml, showDemoNote = true, useH1 = false) {
  const note = showDemoNote
    ? '<p class="plain-page-content__demo-note">Текст страницы представлен в&nbsp;демонстрационном виде для внутреннего просмотра и&nbsp;подлежит замене после проверки.</p>'
    : '';
  return `@@include('partials/sections/plain-page-content.html', {"contentStatusAttr": "data-content-status=\\"demo-placeholder\\"", "titleId": "${titleId}", "pageTitle": "${pageTitle}", "bodyHtml": "${bodyHtml.replace(/"/g, '\\"')}", "demoNoteHtml": "${note.replace(/"/g, '\\"')}", "useH1": "${useH1 ? 'true' : 'false'}"})`;
}

function serviceLeafPage(cfg) {
  const bc = breadcrumb({
    crumbHome: 'Главная',
    crumbMiddle: 'Услуги',
    crumbMiddleHref: '/uslugi/',
    crumbMiddle2: cfg.parentLabel,
    crumbMiddleHref2: cfg.parentRoute,
    crumbCurrent: cfg.crumbCurrent,
  });
  const intro = `<section class="service-leaf-intro-v1" id="service-leaf-intro"><div class="container service-leaf-intro-v1__container"><h2 class="service-leaf-intro-v1__heading">${cfg.introHeading}</h2><p class="service-leaf-intro-v1__lead block-whith-red-line">${cfg.introLead}</p></div></section>`;
  const main = `@@include('partials/sections/services-inner-hero-v2.html', {"titleId": "${cfg.id}-hero-title", "heroImage": "${cfg.heroImage}", "heroWidth": "850", "heroHeight": "567", "heroEyebrow": "Заболевания, которые мы&nbsp;лечим", "heroTitle": "${cfg.heroTitle}", "heroLead": "${cfg.heroLead}", "heroCtaText": "Записаться на&nbsp;консультацию", "heroCtaSource": "${cfg.id}-hero"})
    ${bc}
    ${intro}
    @@include('partials/components/program-cta-band.html', {"wrapSection": "true", "wrapContainer": "", "sectionId": "${cfg.id}-cta", "headingId": "${cfg.id}-cta-heading", "headingText": "Запишитесь на&nbsp;встречу", "buttonFirst": "true", "marginFlush": "true", "ctaTitle": "Запишитесь на&nbsp;встречу", "ctaSubtitle": "Опишите ситуацию в&nbsp;удобном для вас формате.", "ctaPhone": "8&nbsp;(925)&nbsp;183-64-64", "ctaPhoneHint": "Или позвоните нам", "ctaText": "Записаться", "ctaSource": "${cfg.id}-cta"})
    @@include('partials/sections/comfort.html', {"sectionId": "${cfg.id}-comfort", "headingId": "${cfg.id}-comfort-heading", "headingText": "Комфорт, приватность, забота", "sectionModifierClass": ""})`;
  return shell({
    title: cfg.title,
    description: cfg.description,
    canonical: cfg.canonical,
    bodyClass: 'page-service-leaf-v1',
    dataPage: cfg.id,
    mainClass: 'page-service-leaf-v1__main',
    breadcrumb: '',
    mainContent: main,
  });
}

function serviceSubdivisionPage(cfg) {
  const servicesHtml = cfg.services
    .map(
      (s) =>
        `<article class="services-category-section-v2__service"><div class="services-category-section-v2__service-head"><h3 class="services-category-section-v2__service-title"><span class="services-category-section-v2__service-name">${s.name}</span></h3><a class="services-category-section-v2__service-link home-rehabilitation-program__all-link" href="${s.href}"><span class="home-rehabilitation-program__all-text">узнать больше</span><span class="home-rehabilitation-program__all-icon" aria-hidden="true"><i class="fas fa-play"></i></span></a></div></article>`
    )
    .join('');
  const bc = breadcrumb({
    crumbHome: 'Главная',
    crumbMiddle: 'Услуги',
    crumbMiddleHref: '/uslugi/',
    crumbMiddle2: '',
    crumbMiddleHref2: '',
    crumbCurrent: cfg.crumbCurrent,
  });
  const main = `@@include('partials/sections/services-inner-hero-v2.html', {"titleId": "${cfg.id}-hero-title", "heroImage": "assets/img/content/services/service-subdivision-hero.webp", "heroWidth": "1134", "heroHeight": "613", "heroEyebrow": "Заболевания, которые мы&nbsp;лечим", "heroTitle": "${cfg.heroTitle}", "heroLead": "${cfg.heroLead}", "heroCtaText": "Записаться на&nbsp;консультацию", "heroCtaSource": "${cfg.id}-hero"})
    ${bc}
    @@include('partials/sections/services-category-section-v2.html', {"id": "${cfg.id}-services", "modifierClass": "services-category-section-v2--subdivision-dependencies", "sectionId": "${cfg.id}-services-heading", "icon": "01", "hideMarker": "", "heading": "${cfg.sectionHeading}", "intro": "${cfg.intro}", "lead": "${cfg.lead}", "bodyHtml": "", "hideCta": "", "ctaText": "Записаться на&nbsp;консультацию", "ctaSource": "${cfg.id}-cta", "servicesHtml": "${servicesHtml.replace(/"/g, '\\"')}", "galleryHtml": ""})
    @@include('partials/sections/comfort.html', {"sectionId": "${cfg.id}-comfort", "headingId": "${cfg.id}-comfort-heading", "headingText": "Комфорт, приватность, забота", "sectionModifierClass": ""})`;
  return shell({
    title: cfg.title,
    description: cfg.description,
    canonical: cfg.canonical,
    bodyClass: 'page-service-subdivision-v1',
    dataPage: cfg.id,
    mainClass: 'page-service-subdivision-v1__main',
    breadcrumb: '',
    mainContent: main,
  });
}

function institutionalPage(cfg) {
  const bc = breadcrumb({
    crumbHome: 'Главная',
    crumbMiddle: 'О центре',
    crumbMiddleHref: '/o-centre/',
    crumbMiddle2: '',
    crumbMiddleHref2: '',
    crumbCurrent: cfg.crumbCurrent,
  });
  const body = plainSection(cfg.id + '-title', cfg.h1, cfg.body);
  const main = `@@include('partials/sections/services-inner-hero-v2.html', {"titleId": "${cfg.id}-hero-title", "heroImage": "assets/img/content/o-centre/o-centre-hero.webp", "heroWidth": "1890", "heroHeight": "1260", "heroEyebrow": "О центре", "heroTitle": "${cfg.h1}", "heroLead": "${cfg.heroLead}", "heroCtaText": "Записаться на&nbsp;консультацию", "heroCtaSource": "${cfg.id}-hero"})
    ${bc}
    ${body}`;
  return shell({
    title: cfg.title,
    description: cfg.description,
    canonical: cfg.canonical,
    bodyClass: 'page-o-centre page-plain-content',
    dataPage: cfg.id,
    mainClass: 'page-plain-content__main',
    breadcrumb: '',
    mainContent: main,
  });
}

function legalPage(cfg) {
  const bc = breadcrumb({
    crumbHome: 'Главная',
    crumbMiddle: '',
    crumbMiddleHref: '',
    crumbMiddle2: '',
    crumbMiddleHref2: '',
    crumbCurrent: cfg.h1,
  });
  const body = plainSection(cfg.id + '-title', cfg.h1, cfg.body, true, true);
  const main = `${bc}\n    ${body}`;
  return shell({
    title: cfg.title,
    description: cfg.description,
    canonical: cfg.canonical,
    bodyClass: 'page-legal-plain page-plain-content',
    dataPage: cfg.id,
    mainClass: 'page-plain-content__main',
    breadcrumb: '',
    mainContent: main,
  });
}

const files = {
  'uslugi/psihicheskoe-zdorovie.html': serviceSubdivisionPage({
    id: 'psihicheskoe-zdorovie',
    title: 'Психическое здоровье — Шпиговский дом',
    description: 'Психическое здоровье: поддержка и реабилитация в центре «Шпиговский дом».',
    canonical: 'https://shpigovsky.ru/uslugi/psihicheskoe-zdorovie/',
    heroTitle: 'Психическое здоровье',
    heroLead: 'Тревога, депрессия, эмоциональное выгорание и&nbsp;другие состояния требуют внимательного, мультидисциплинарного подхода. В&nbsp;демо-версии представлен обзор направления.',
    crumbCurrent: 'Психическое здоровье',
    sectionHeading: 'Состояния, с&nbsp;которыми мы&nbsp;работаем',
    intro: 'Раздел описывает направления работы центра с&nbsp;нарушениями психического здоровья.',
    lead: 'Для демонстрации структуры сайта опубликована одна представительная страница услуги.',
    services: [
      { name: 'Депрессия', href: '/uslugi/psihicheskoe-zdorovie/depressiya/' },
      { name: 'Тревожные расстройства', href: '/uslugi/psihicheskoe-zdorovie/' },
      { name: 'ПТСР', href: '/uslugi/psihicheskoe-zdorovie/' },
    ],
  }),
  'uslugi/psihicheskoe-zdorovie/depressiya.html': serviceLeafPage({
    id: 'depressiya',
    title: 'Депрессия — Шпиговский дом',
    description: 'Поддержка при депрессии в реабилитационном центре «Шпиговский дом».',
    canonical: 'https://shpigovsky.ru/uslugi/psihicheskoe-zdorovie/depressiya/',
    parentLabel: 'Психическое здоровье',
    parentRoute: '/uslugi/psihicheskoe-zdorovie/',
    crumbCurrent: 'Депрессия',
    heroTitle: 'Депрессия',
    heroLead: 'Депрессия влияет на&nbsp;энергию, сон, отношения и&nbsp;ощущение смысла. В&nbsp;центре мы&nbsp;рассматриваем состояние в&nbsp;контексте биологии, психологии и&nbsp;образа жизни человека.',
    heroImage: 'assets/img/content/services/services-mental-health-01.webp',
    introHeading: 'Депрессия&nbsp;— не&nbsp;слабость и&nbsp;не&nbsp;лень',
    introLead: 'Это состояние, с&nbsp;которым можно работать при бережной и&nbsp;структурированной поддержке.',
  }),
  'uslugi/rasstroystva-pischevogo-povedeniya.html': serviceSubdivisionPage({
    id: 'rasstroystva-pischevogo-povedeniya',
    title: 'Расстройства пищевого поведения — Шпиговский дом',
    description: 'Расстройства пищевого поведения: реабилитация в центре «Шпиговский дом».',
    canonical: 'https://shpigovsky.ru/uslugi/rasstroystva-pischevogo-povedeniya/',
    heroTitle: 'Расстройства пищевого поведения',
    heroLead: 'Отношения с&nbsp;едой и&nbsp;телом часто отражают глубинные тревоги и&nbsp;переживания. В&nbsp;демо-версии показана структура раздела.',
    crumbCurrent: 'Расстройства пищевого поведения',
    sectionHeading: 'Расстройства, с&nbsp;которыми мы&nbsp;работаем',
    intro: 'Центр оказывает поддержку при нарушениях пищевого поведения.',
    lead: 'Для демонстрации опубликована представительная страница услуги.',
    services: [
      { name: 'Нервная анорексия', href: '/uslugi/rasstroystva-pischevogo-povedeniya/anoreksiya/' },
      { name: 'Нервная булимия', href: '/uslugi/rasstroystva-pischevogo-povedeniya/' },
      { name: 'Компульсивное переедание', href: '/uslugi/rasstroystva-pischevogo-povedeniya/' },
    ],
  }),
  'uslugi/rasstroystva-pischevogo-povedeniya/anoreksiya.html': serviceLeafPage({
    id: 'anoreksiya',
    title: 'Нервная анорексия — Шпиговский дом',
    description: 'Поддержка при нервной анорексии в центре «Шпиговский дом».',
    canonical: 'https://shpigovsky.ru/uslugi/rasstroystva-pischevogo-povedeniya/anoreksiya/',
    parentLabel: 'Расстройства пищевого поведения',
    parentRoute: '/uslugi/rasstroystva-pischevogo-povedeniya/',
    crumbCurrent: 'Нервная анорексия',
    heroTitle: 'Нервная анорексия',
    heroLead: 'Нервная анорексия затрагивает физическое и&nbsp;психическое здоровье. Работа в&nbsp;центре направлена на&nbsp;восстановление безопасного отношения к&nbsp;себе и&nbsp;питанию.',
    heroImage: 'assets/img/content/services/services-mental-health-02.webp',
    introHeading: 'Расстройство пищевого поведения требует комплексной поддержки',
    introLead: 'В&nbsp;демо-версии представлена структура страницы услуги для согласования с&nbsp;оператором.',
  }),
  'uslugi/genotipirovanie.html': serviceLeafPage({
    id: 'genotipirovanie',
    title: 'Генотипирование — Шпиговский дом',
    description: 'Генотипирование как инструмент диагностики в центре «Шпиговский дом».',
    canonical: 'https://shpigovsky.ru/uslugi/genotipirovanie/',
    parentLabel: 'Услуги',
    parentRoute: '/uslugi/',
    crumbCurrent: 'Генотипирование',
    heroTitle: 'Генотипирование',
    heroLead: 'Анализ, который позволяет увидеть индивидуальные генетические особенности системы регуляции настроения и&nbsp;оценить предрасположенности.',
    heroImage: 'assets/img/content/rehabilitation-program/program-genotyping.webp',
    introHeading: 'Генотипирование&nbsp;— инструмент диагностики',
    introLead: 'Результат исследования помогает выстраивать персонализированную программу поддержки с&nbsp;учётом индивидуальных особенностей.',
  }),
};

const institutional = [
  { file: 'o-centre/o-nas.html', id: 'o-nas', h1: 'О нас', lead: 'Краткая информация о&nbsp;команде и&nbsp;миссии центра для демонстрации структуры сайта.', body: '<p>«Шпиговский дом»&nbsp;— реабилитационный центр профилактики и&nbsp;лечения зависимостей и&nbsp;нарушений психического здоровья. Эта страница подготовлена как демонстрационный материал.</p><p>Финальный текст будет согласован с&nbsp;оператором и&nbsp;заменён перед публикацией.</p>' },
  { file: 'o-centre/programma-lecheniya.html', id: 'programma-lecheniya', h1: 'Программа лечения', lead: 'Обзор мультидисциплинарной программы центра.', body: '<p>Программа включает генотипирование, нейропсихологическую коррекцию, психокоррекцию и&nbsp;кинезиотерапию. Маршрут формируется индивидуально.</p><p>Текст демонстрационный и&nbsp;требует детализации по&nbsp;согласованию с&nbsp;оператором.</p>' },
  { file: 'o-centre/galereya-o-dome.html', id: 'galereya-o-dome', h1: 'Галерея о доме', lead: 'Фотоматериалы о&nbsp;пространстве центра.', body: '<p>Раздел предназначен для галереи интерьеров и&nbsp;территории. В&nbsp;демо-версии размещён текстовый заглушечный контент.</p>' },
  { file: 'o-centre/specialistam.html', id: 'specialistam', h1: 'Специалистам', lead: 'Информация для профессионального сообщества.', body: '<p>Страница для врачей, психотерапевтов и&nbsp;партнёров. Демонстрационный текст.</p>' },
  { file: 'o-centre/rodstvennikam.html', id: 'rodstvennikam', h1: 'Родственникам', lead: 'Поддержка близких людей, обращающихся за&nbsp;помощью.', body: '<p>Материал для родственников и&nbsp;опекунов. Текст временный и&nbsp;подлежит замене.</p>' },
];

for (const inst of institutional) {
  files[inst.file] = institutionalPage({
    id: inst.id,
    title: `${inst.h1} — Шпиговский дом`,
    description: `${inst.h1} — центр «Шпиговский дом». Демонстрационная страница.`,
    canonical: `https://shpigovsky.ru/o-centre/${inst.id}/`,
    h1: inst.h1,
    heroLead: inst.lead,
    crumbCurrent: inst.h1,
    body: inst.body,
  });
}

const legal = [
  { file: 'privacy-policy.html', id: 'privacy-policy', h1: 'Политика конфиденциальности', body: '<p>Настоящий документ описывает порядок обработки персональных данных посетителей сайта. Текст подготовлен в&nbsp;демонстрационном виде и&nbsp;не&nbsp;является финальной юридической редакцией.</p><p>Перед публикацией документ должен быть проверен уполномоченным специалистом.</p>' },
  { file: 'user-agreement.html', id: 'user-agreement', h1: 'Пользовательское соглашение', body: '<p>Условия использования сайта центра «Шпиговский дом». Демонстрационная версия для внутреннего просмотра.</p>' },
  { file: 'consent-personal-data.html', id: 'consent-personal-data', h1: 'Согласие на обработку персональных данных', body: '<p>Формулировка согласия на&nbsp;обработку персональных данных для форм обратной связи. Требует юридической проверки.</p>' },
  { file: 'cookie-files-policy.html', id: 'cookie-files-policy', h1: 'Политика Cookie-файлов', body: '<p>Информация об&nbsp;использовании cookie-файлов на&nbsp;сайте. Демонстрационный текст.</p>' },
];

for (const leg of legal) {
  files[leg.file] = legalPage({
    id: leg.id,
    title: `${leg.h1} — Шпиговский дом`,
    description: `${leg.h1}. Демонстрационная страница.`,
    canonical: `https://shpigovsky.ru/${leg.id}/`,
    h1: leg.h1,
    body: leg.body,
  });
}

for (const [rel, content] of Object.entries(files)) {
  const full = path.join(PAGES, rel);
  fs.mkdirSync(path.dirname(full), { recursive: true });
  fs.writeFileSync(full, content, 'utf8');
  console.log('Wrote', rel);
}

console.log('Done:', Object.keys(files).length, 'pages');
