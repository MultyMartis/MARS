'use strict';

const HOME_TREATMENT_PANELS = {
  'home-treatment-prevention-panel-2': [
    { label: 'Депрессия', url: '/uslugi/psihicheskoe-zdorovie/depressiya/' },
    { label: 'ПТСР', url: '/uslugi/psihicheskoe-zdorovie/ptsr/' },
    { label: 'Эмоциональное выгорание', url: '/uslugi/psihicheskoe-zdorovie/emotsionalnoe-vygoranie/' },
    { label: 'Тревожные расстройства', url: '/uslugi/psihicheskoe-zdorovie/trevozhnye-rasstroystva/' },
    { label: 'Расстройства сна', url: '/uslugi/psihicheskoe-zdorovie/rasstroystva-sna/' },
    { label: 'Травма', url: '/uslugi/psihicheskoe-zdorovie/travma/' },
  ],
  'home-treatment-prevention-panel-3': [
    { label: 'Нервная анорексия', url: '/uslugi/rasstroystva-pischevogo-povedeniya/anoreksiya/' },
    { label: 'Нервная булимия', url: '/uslugi/rasstroystva-pischevogo-povedeniya/buliniya/' },
    { label: 'Компульсивное переедание', url: '/uslugi/rasstroystva-pischevogo-povedeniya/kompulsivnoe-pereedanie/' },
  ],
  'home-treatment-prevention-panel-4': [
    { label: 'Профилактический анализ', url: '/zavisimosti/genotipirovanie/profilakticheskiy-analiz/' },
    { label: 'Специалистам', url: '/zavisimosti/genotipirovanie/specialistam/' },
  ],
};

function renderServiceItem(label, url) {
  return `            <li class="home-treatment-prevention__service-list-item">
              <a
                class="home-treatment-prevention__service-item"
                href="${url}"
              >
                <span class="home-treatment-prevention__service-name">${label}</span>
                <span class="home-treatment-prevention__service-leader" aria-hidden="true"></span>
                <span class="home-treatment-prevention__service-icon" aria-hidden="true"><img class="home-treatment-prevention__service-icon-image" src="assets/svg/external-link.svg" width="20" height="20" alt=""></span>
              </a>
            </li>`;
}

function renderServiceList(links) {
  const items = links.map((link) => renderServiceItem(link.label, link.url)).join('\n');
  return `<ul class="home-treatment-prevention__service-list">\n${items}\n          </ul>`;
}

function injectHomeTreatmentPreventionLinks(html) {
  let result = html;
  Object.entries(HOME_TREATMENT_PANELS).forEach(([panelId, links]) => {
    const panelRegex = new RegExp(
      `(<div\\b[^>]*id="${panelId}"[^>]*>)(\\s*)(</div>)`,
      'i'
    );
    result = result.replace(panelRegex, `$1\n          ${renderServiceList(links)}\n        $3`);
  });
  return result;
}

module.exports = {
  HOME_TREATMENT_PANELS,
  injectHomeTreatmentPreventionLinks,
};
