#!/usr/bin/env node
/** One-time explicit placeholder page source generator for V9-01 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const PAGES = path.resolve(__dirname, '../src/pages');
const NAV = '{"activeNavUslugiClass": "", "activeNavOffcanvasClass": "", "activeNavUslugiAria": "", "activeNavOtzyvyClass": "", "activeNavOtzyvyOffcanvasClass": "", "activeNavOtzyvyAria": "", "activeNavKontaktyClass": "", "activeNavKontaktyOffcanvasClass": "", "activeNavKontaktyAria": "", "activeNavBlogClass": "", "activeNavBlogOffcanvasClass": "", "activeNavBlogAria": ""}';

const pages = [
  { file: 'uslugi/psihicheskoe-zdorovie.html', title: 'Психическое здоровье', desc: 'Психическое здоровье — Шпиговский дом', route: '/uslugi/psihicheskoe-zdorovie/', crumbMiddle: 'Услуги', crumbMiddleHref: '/uslugi/', crumbMiddle2: '', crumbMiddleHref2: '', crumbCurrent: 'Психическое здоровье', slug: 'psihicheskoe-zdorovie' },
  { file: 'uslugi/psihicheskoe-zdorovie/depressiya.html', title: 'Депрессия', desc: 'Депрессия — Шпиговский дом', route: '/uslugi/psihicheskoe-zdorovie/depressiya/', crumbMiddle: 'Услуги', crumbMiddleHref: '/uslugi/', crumbMiddle2: 'Психическое здоровье', crumbMiddleHref2: '/uslugi/psihicheskoe-zdorovie/', crumbCurrent: 'Депрессия', slug: 'depressiya' },
  { file: 'uslugi/psihicheskoe-zdorovie/ptrs.html', title: 'ПТСР', desc: 'ПТСР — Шпиговский дом', route: '/uslugi/psihicheskoe-zdorovie/ptrs/', crumbMiddle: 'Услуги', crumbMiddleHref: '/uslugi/', crumbMiddle2: 'Психическое здоровье', crumbMiddleHref2: '/uslugi/psihicheskoe-zdorovie/', crumbCurrent: 'ПТСР', slug: 'ptrs' },
  { file: 'uslugi/psihicheskoe-zdorovie/emocionalnoe-vygoranie.html', title: 'Эмоциональное выгорание', desc: 'Эмоциональное выгорание — Шпиговский дом', route: '/uslugi/psihicheskoe-zdorovie/emocionalnoe-vygoranie/', crumbMiddle: 'Услуги', crumbMiddleHref: '/uslugi/', crumbMiddle2: 'Психическое здоровье', crumbMiddleHref2: '/uslugi/psihicheskoe-zdorovie/', crumbCurrent: 'Эмоциональное выгорание', slug: 'emocionalnoe-vygoranie' },
  { file: 'uslugi/psihicheskoe-zdorovie/trevozhnye-rasstroystva.html', title: 'Тревожные расстройства', desc: 'Тревожные расстройства — Шпиговский дом', route: '/uslugi/psihicheskoe-zdorovie/trevozhnye-rasstroystva/', crumbMiddle: 'Услуги', crumbMiddleHref: '/uslugi/', crumbMiddle2: 'Психическое здоровье', crumbMiddleHref2: '/uslugi/psihicheskoe-zdorovie/', crumbCurrent: 'Тревожные расстройства', slug: 'trevozhnye-rasstroystva' },
  { file: 'uslugi/psihicheskoe-zdorovie/rasstroystva-sna.html', title: 'Расстройства сна', desc: 'Расстройства сна — Шпиговский дом', route: '/uslugi/psihicheskoe-zdorovie/rasstroystva-sna/', crumbMiddle: 'Услуги', crumbMiddleHref: '/uslugi/', crumbMiddle2: 'Психическое здоровье', crumbMiddleHref2: '/uslugi/psihicheskoe-zdorovie/', crumbCurrent: 'Расстройства сна', slug: 'rasstroystva-sna' },
  { file: 'uslugi/psihicheskoe-zdorovie/travma.html', title: 'Травма', desc: 'Травма — Шпиговский дом', route: '/uslugi/psihicheskoe-zdorovie/travma/', crumbMiddle: 'Услуги', crumbMiddleHref: '/uslugi/', crumbMiddle2: 'Психическое здоровье', crumbMiddleHref2: '/uslugi/psihicheskoe-zdorovie/', crumbCurrent: 'Травма', slug: 'travma' },
  { file: 'uslugi/rasstroystva-pischevogo-povedeniya.html', title: 'Расстройства пищевого поведения', desc: 'Расстройства пищевого поведения — Шпиговский дом', route: '/uslugi/rasstroystva-pischevogo-povedeniya/', crumbMiddle: 'Услуги', crumbMiddleHref: '/uslugi/', crumbMiddle2: '', crumbMiddleHref2: '', crumbCurrent: 'Расстройства пищевого поведения', slug: 'rasstroystva-pischevogo-povedeniya' },
  { file: 'uslugi/rasstroystva-pischevogo-povedeniya/anoreksiya.html', title: 'Нервная анорексия', desc: 'Нервная анорексия — Шпиговский дом', route: '/uslugi/rasstroystva-pischevogo-povedeniya/anoreksiya/', crumbMiddle: 'Услуги', crumbMiddleHref: '/uslugi/', crumbMiddle2: 'Расстройства пищевого поведения', crumbMiddleHref2: '/uslugi/rasstroystva-pischevogo-povedeniya/', crumbCurrent: 'Нервная анорексия', slug: 'anoreksiya' },
  { file: 'uslugi/rasstroystva-pischevogo-povedeniya/nervnaya-bulimiya.html', title: 'Нервная булимия', desc: 'Нервная булимия — Шпиговский дом', route: '/uslugi/rasstroystva-pischevogo-povedeniya/nervnaya-bulimiya/', crumbMiddle: 'Услуги', crumbMiddleHref: '/uslugi/', crumbMiddle2: 'Расстройства пищевого поведения', crumbMiddleHref2: '/uslugi/rasstroystva-pischevogo-povedeniya/', crumbCurrent: 'Нервная булимия', slug: 'nervnaya-bulimiya' },
  { file: 'uslugi/rasstroystva-pischevogo-povedeniya/kompulsivnoe-pereedanie.html', title: 'Компульсивное переедание', desc: 'Компульсивное переедание — Шпиговский дом', route: '/uslugi/rasstroystva-pischevogo-povedeniya/kompulsivnoe-pereedanie/', crumbMiddle: 'Услуги', crumbMiddleHref: '/uslugi/', crumbMiddle2: 'Расстройства пищевого поведения', crumbMiddleHref2: '/uslugi/rasstroystva-pischevogo-povedeniya/', crumbCurrent: 'Компульсивное переедание', slug: 'kompulsivnoe-pereedanie' },
  { file: 'uslugi/zavisimosti/profilakticheskiy-analiz.html', title: 'Профилактический анализ', desc: 'Профилактический анализ — Шпиговский дом', route: '/uslugi/zavisimosti/profilakticheskiy-analiz/', crumbMiddle: 'Услуги', crumbMiddleHref: '/uslugi/', crumbMiddle2: 'Зависимости', crumbMiddleHref2: '/uslugi/zavisimosti/', crumbCurrent: 'Профилактический анализ', slug: 'profilakticheskiy-analiz' },
  { file: 'uslugi/zavisimosti/specialistam.html', title: 'Специалистам', desc: 'Специалистам — Шпиговский дом', route: '/uslugi/zavisimosti/specialistam/', crumbMiddle: 'Услуги', crumbMiddleHref: '/uslugi/', crumbMiddle2: 'Зависимости', crumbMiddleHref2: '/uslugi/zavisimosti/', crumbCurrent: 'Специалистам', slug: 'zavisimosti-specialistam' },
];

function pageHtml(p) {
  const canonical = `https://shpigovsky.ru${p.route}`;
  return `<!DOCTYPE html>
<html lang="ru">
<head>
  @@include('partials/layout/head.html', {"title": "${p.title} — Шпиговский дом", "description": "${p.desc}", "canonical": "${canonical}", "robots": "noindex, nofollow", "ogType": "website", "ogTitle": "${p.title} — Шпиговский дом", "ogDescription": "${p.desc}", "ogUrl": "${canonical}", "ogImage": "https://shpigovsky.ru/assets/img/social/og-default.jpg", "ogImageAlt": "${p.title} — Шпиговский дом"})
</head>
<body class="page-placeholder" data-page="${p.slug}">
  @@include('partials/layout/header.html', ${NAV})
  <main class="page-placeholder__main">
    @@include('partials/components/placeholder-breadcrumbs.html', {"crumbHome": "Главная", "crumbMiddle": "${p.crumbMiddle}", "crumbMiddleHref": "${p.crumbMiddleHref}", "crumbMiddle2": "${p.crumbMiddle2}", "crumbMiddleHref2": "${p.crumbMiddleHref2}", "crumbCurrent": "${p.crumbCurrent}"})
    @@include('partials/sections/placeholder-page.html', {"titleId": "${p.slug}-title", "pageTitle": "${p.title}"})
  </main>
  @@include('partials/layout/footer.html')
  @@include('partials/components/modal-consultation.html')
  <script src="assets/vendor/swiper/swiper-bundle.min.js" defer></script>
  <script src="assets/vendor/fancybox/fancybox.umd.js" defer></script>
  <script src="https://cdn.jsdelivr.net/npm/inputmask@5.0.9/dist/inputmask.min.js" defer></script>
  <script src="assets/js/main.js" defer></script>
</body>
</html>
`;
}

for (const p of pages) {
  const out = path.join(PAGES, p.file.replace(/\//g, path.sep));
  fs.mkdirSync(path.dirname(out), { recursive: true });
  fs.writeFileSync(out, pageHtml(p), 'utf8');
  console.log('Wrote', p.file);
}
