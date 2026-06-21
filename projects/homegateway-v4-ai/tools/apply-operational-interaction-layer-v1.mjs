import fs from 'fs';
import path from 'path';

const root = process.argv[2] || path.resolve('workspaces/homegateway-v4-ai/v1');

function w(rel, content) {
  const p = path.join(root, rel);
  fs.mkdirSync(path.dirname(p), { recursive: true });
  fs.writeFileSync(p, content, 'utf8');
  console.log('wrote', rel);
}

w(
  'src/partials/components/telemetry-indicator.html',
  `<span class="hg-telemetry__item hg-telemetry__item--@@kind" data-telemetry="@@kind" title="@@title">
  <i class="fad @@icon hg-icon hg-icon--telemetry" aria-hidden="true"></i>
  <span class="hg-telemetry__value">@@value</span>
</span>
`
);

w(
  'src/partials/components/telemetry-group.html',
  `<div class="hg-telemetry" role="group" aria-label="Операционная телеметрия">
  @@include("partials/components/telemetry-indicator.html", {"kind":"entities","icon":"fa-folders","title":"Сущности","value":"@@entities"})
  @@include("partials/components/telemetry-indicator.html", {"kind":"problems","icon":"fa-exclamation-triangle","title":"Активные проблемы","value":"@@problems"})
  @@include("partials/components/telemetry-indicator.html", {"kind":"active-tasks","icon":"fa-tasks","title":"Активные задачи","value":"@@active"})
  @@include("partials/components/telemetry-indicator.html", {"kind":"completed-tasks","icon":"fa-check-circle","title":"Завершённые задачи","value":"@@completed"})
</div>
`
);

w(
  'src/partials/components/list-row.html',
  `<li class="hg-list__item">
  <button type="button" class="hg-list__row" data-hook="list-row" data-icon="@@icon">
    <span class="hg-list__icon" aria-hidden="true"><i class="fad @@navIcon hg-icon hg-icon--nav"></i></span>
    <span class="hg-list__title">@@title</span>
    @@include("partials/components/telemetry-group.html", {"entities":"@@entities","problems":"@@problems","active":"@@active","completed":"@@completed"})
  </button>
</li>
`
);

w(
  'src/partials/components/signal-card.html',
  `<article class="hg-signal hg-signal--@@type" data-component="signal-card" data-signal-type="@@type">
  <div class="hg-signal__body">
    <h3 class="hg-signal__title">@@title</h3>
    <p class="hg-signal__desc">@@desc</p>
    <div class="hg-signal__actions">
      <a href="#" class="hg-link" data-hook="signal-detail">Подробнее</a>
      <span class="hg-signal__sep">/</span>
      <button type="button" class="hg-link hg-link--btn" data-hook="signal-dismiss">Удалить</button>
    </div>
  </div>
  <div class="hg-signal__indicator hg-indicator hg-indicator--@@status" data-indicator-type="@@type">
    <i class="fad @@signalIcon hg-icon hg-icon--signal" aria-hidden="true"></i>
    <span class="hg-indicator__label">@@statusLabel</span>
  </div>
</article>
`
);

w(
  'src/partials/components/metric-row.html',
  `<li class="hg-metrics__item">
  <span class="hg-metrics__icon" aria-hidden="true"><i class="fad @@metricIcon hg-icon hg-icon--metric"></i></span>
  <span class="hg-metrics__label">@@label</span>
  <span class="hg-metrics__value">@@value</span>
</li>
`
);

w(
  'src/partials/sections/topbar.html',
  `<header class="hg-topbar" data-component="topbar">
  <nav class="hg-topbar__nav" aria-label="Разделы интерфейса">
    <ul class="hg-topbar__tabs" role="tablist">
      <li role="presentation"><button type="button" class="hg-tab hg-tab--active" role="tab" aria-selected="true" data-hook="nav-tab" data-tab="general">Общий</button></li>
      <li role="presentation"><button type="button" class="hg-tab" role="tab" aria-selected="false" data-hook="nav-tab" data-tab="systems">Системы</button></li>
      <li role="presentation"><button type="button" class="hg-tab" role="tab" aria-selected="false" data-hook="nav-tab" data-tab="focus">Фокус</button></li>
      <li role="presentation"><button type="button" class="hg-tab" role="tab" aria-selected="false" data-hook="nav-tab" data-tab="signals">Сигналы</button></li>
    </ul>
  </nav>
  <div class="hg-topbar__utilities" role="toolbar" aria-label="Служебные действия">
    <button type="button" class="hg-utility-btn hg-utility-btn--icon" data-hook="theme-toggle" data-utility="theme" title="Переключить тему" aria-label="Переключить тему">
      <i class="fad fa-adjust hg-icon" aria-hidden="true"></i>
    </button>
    <button type="button" class="hg-utility-btn hg-utility-btn--icon" data-hook="utility" data-utility="profile" title="Профиль" aria-label="Профиль">
      <i class="fad fa-user-circle hg-icon" aria-hidden="true"></i>
    </button>
    <button type="button" class="hg-utility-btn hg-utility-btn--icon" data-hook="utility" data-utility="settings" title="Настройки" aria-label="Настройки">
      <i class="fad fa-sliders-h hg-icon" aria-hidden="true"></i>
    </button>
    <button type="button" class="hg-utility-btn hg-utility-btn--icon" data-hook="utility" data-utility="about" title="О системе" aria-label="О системе">
      <i class="fad fa-info-circle hg-icon" aria-hidden="true"></i>
    </button>
  </div>
  <div class="hg-topbar__profile hg-profile" data-component="profile">
    <div class="hg-profile__meta">
      <span class="hg-profile__status">Авторизован</span>
      <span class="hg-profile__name">Multy Martis</span>
    </div>
    <div class="hg-profile__avatar" aria-hidden="true">MM</div>
  </div>
</header>
`
);

w(
  'src/partials/sections/left-sidebar.html',
  `<aside class="hg-sidebar hg-sidebar--left" data-component="sidebar-left">
  <div class="hg-sidebar__logo hg-logo">
    <a href="/" class="hg-logo__link">
      <img class="hg-logo__img" src="assets/img/logo/logo-dark.svg" width="200" height="38" alt="Hub Gateway">
    </a>
  </div>

  <section class="hg-panel hg-panel--projects" data-component="projects-block">
    <header class="hg-panel__head">
      <h2 class="hg-panel__title">Проекты</h2>
      <div class="hg-panel__counters">
        @@include("partials/components/counter-pill.html", {"value":"9"})
        @@include("partials/components/counter-pill.html", {"value":"10"})
      </div>
    </header>
    <ul class="hg-list">
      @@include("partials/components/list-row.html", {"title":"Полигон [WSP]","icon":"project","navIcon":"fa-folder-tree","entities":"5","problems":"1","active":"2","completed":"14"})
      @@include("partials/components/list-row.html", {"title":"Метакор [MCA]","icon":"project","navIcon":"fa-folder-tree","entities":"12","problems":"0","active":"4","completed":"28"})
      @@include("partials/components/list-row.html", {"title":"Мероприятие","icon":"project","navIcon":"fa-folder-tree","entities":"999","problems":"3","active":"7","completed":"120"})
    </ul>
  </section>

  <section class="hg-panel hg-panel--tools" data-component="tools-block">
    <header class="hg-panel__head">
      <h2 class="hg-panel__title">Инструменты</h2>
    </header>
    <ul class="hg-list">
      @@include("partials/components/list-row.html", {"title":"Системы","icon":"systems","navIcon":"fa-layer-group","entities":"4","problems":"0","active":"1","completed":"6"})
      @@include("partials/components/list-row.html", {"title":"Процессы","icon":"processes","navIcon":"fa-stream","entities":"18","problems":"2","active":"5","completed":"42"})
      @@include("partials/components/list-row.html", {"title":"Роботы","icon":"robots","navIcon":"fa-robot","entities":"7","problems":"1","active":"3","completed":"19"})
      @@include("partials/components/list-row.html", {"title":"Вики","icon":"wiki","navIcon":"fa-book-open","entities":"124","problems":"0","active":"2","completed":"310"})
    </ul>
  </section>

  <section class="hg-panel hg-panel--quick" data-component="quick-access-block">
    <header class="hg-panel__head">
      <h2 class="hg-panel__title">Быстрый доступ</h2>
    </header>
    <button type="button" class="hg-quick-link" data-hook="quick-access-open">Открыть список</button>
  </section>
</aside>
`
);

w(
  'src/partials/sections/right-sidebar.html',
  `<aside class="hg-sidebar hg-sidebar--right" data-component="sidebar-right">
  <section class="hg-panel hg-panel--monitor" data-component="monitor-block">
    <header class="hg-panel__head">
      <h2 class="hg-panel__title">Монитор</h2>
    </header>
    <div class="hg-signals">
      @@include("partials/components/signal-card.html", {"type":"A1","signalIcon":"fa-exclamation-circle","title":"Название сигнала","desc":"Описание сигнала — демонстрационный placeholder.","status":"OK","statusLabel":"В норме"})
      @@include("partials/components/signal-card.html", {"type":"A2","signalIcon":"fa-bell","title":"Название уведомления","desc":"Описание уведомления — демонстрационный placeholder.","status":"WARN","statusLabel":"Внимание"})
      @@include("partials/components/signal-card.html", {"type":"A3","signalIcon":"fa-stream","title":"Название события","desc":"Описание события — демонстрационный placeholder.","status":"ALERT","statusLabel":"Отклонение"})
    </div>
    <footer class="hg-panel__foot">
      <a href="#" class="hg-link" data-hook="monitor-log">Смотреть весь лог →</a>
    </footer>
  </section>

  <section class="hg-panel hg-panel--status" data-component="system-status-block">
    <header class="hg-panel__head">
      <h2 class="hg-panel__title">Статус системы</h2>
    </header>
    <div class="hg-status-grid">
      <ul class="hg-metrics">
        @@include("partials/components/metric-row.html", {"label":"CPU нагрузка","value":"23%","metricIcon":"fa-microchip"})
        @@include("partials/components/metric-row.html", {"label":"Память","value":"61%","metricIcon":"fa-memory"})
        @@include("partials/components/metric-row.html", {"label":"Диск I/O","value":"412 Mb/s","metricIcon":"fa-hdd"})
      </ul>
      <div class="hg-status-module hg-status-module--a4" data-indicator-type="A4">
        <span class="hg-status-module__head">
          <i class="fad fa-heartbeat hg-icon hg-icon--status-a4" aria-hidden="true"></i>
          <span class="hg-status-module__label">Сводный health-index</span>
        </span>
        <div class="hg-status-module__chart" aria-hidden="true">
          <span class="hg-bar" style="--h:72%"></span>
          <span class="hg-bar" style="--h:48%"></span>
          <span class="hg-bar" style="--h:86%"></span>
          <span class="hg-bar" style="--h:35%"></span>
        </div>
        <p class="hg-status-module__caption">Агрегированное состояние runtime</p>
        <span class="hg-status-module__value">0.94</span>
      </div>
    </div>
  </section>
</aside>
`
);

w(
  'src/partials/sections/favorites-row.html',
  `<div class="hg-favorites" data-component="favorites-row">
  <div class="hg-favorites__track" data-hook="favorites-track">
    <a class="hg-fav-btn" href="https://yandex.ru" target="_blank" rel="noopener noreferrer" data-hook="fav-link">
      <span class="hg-fav-btn__icon-zone" data-slot="fav-icon">
        <i class="fad fa-star hg-fav-btn__icon-placeholder hg-icon" aria-hidden="true"></i>
      </span>
      <span class="hg-fav-btn__text-zone">Яндекс</span>
      <span class="hg-fav-btn__action-zone" aria-hidden="true">
        <span class="hg-fav-btn__external" title="Открыть во внешнем контексте"><i class="fad fa-external-link-alt hg-icon" aria-hidden="true"></i></span>
      </span>
    </a>
    <a class="hg-fav-btn" href="https://google.com" target="_blank" rel="noopener noreferrer" data-hook="fav-link">
      <span class="hg-fav-btn__icon-zone" data-slot="fav-icon">
        <i class="fad fa-star hg-fav-btn__icon-placeholder hg-icon" aria-hidden="true"></i>
      </span>
      <span class="hg-fav-btn__text-zone">Google</span>
      <span class="hg-fav-btn__action-zone" aria-hidden="true">
        <span class="hg-fav-btn__external" title="Открыть во внешнем контексте"><i class="fad fa-external-link-alt hg-icon" aria-hidden="true"></i></span>
      </span>
    </a>
    <a class="hg-fav-btn" href="https://youtube.com" target="_blank" rel="noopener noreferrer" data-hook="fav-link">
      <span class="hg-fav-btn__icon-zone" data-slot="fav-icon">
        <i class="fad fa-star hg-fav-btn__icon-placeholder hg-icon" aria-hidden="true"></i>
      </span>
      <span class="hg-fav-btn__text-zone">YouTube</span>
      <span class="hg-fav-btn__action-zone" aria-hidden="true">
        <span class="hg-fav-btn__external" title="Открыть во внешнем контексте"><i class="fad fa-external-link-alt hg-icon" aria-hidden="true"></i></span>
      </span>
    </a>
    <a class="hg-fav-btn" href="https://mail.ru" target="_blank" rel="noopener noreferrer" data-hook="fav-link">
      <span class="hg-fav-btn__icon-zone" data-slot="fav-icon">
        <i class="fad fa-star hg-fav-btn__icon-placeholder hg-icon" aria-hidden="true"></i>
      </span>
      <span class="hg-fav-btn__text-zone">Mail</span>
      <span class="hg-fav-btn__action-zone" aria-hidden="true">
        <span class="hg-fav-btn__external" title="Открыть во внешнем контексте"><i class="fad fa-external-link-alt hg-icon" aria-hidden="true"></i></span>
      </span>
    </a>
    <a class="hg-fav-btn" href="https://vk.com" target="_blank" rel="noopener noreferrer" data-hook="fav-link">
      <span class="hg-fav-btn__icon-zone" data-slot="fav-icon">
        <i class="fad fa-star hg-fav-btn__icon-placeholder hg-icon" aria-hidden="true"></i>
      </span>
      <span class="hg-fav-btn__text-zone">VK</span>
      <span class="hg-fav-btn__action-zone" aria-hidden="true">
        <span class="hg-fav-btn__external" title="Открыть во внешнем контексте"><i class="fad fa-external-link-alt hg-icon" aria-hidden="true"></i></span>
      </span>
    </a>
  </div>
  <button type="button" class="hg-favorites__slide hg-favorites__slide--icon" data-hook="favorites-slide" title="Следующий набор избранного" aria-label="Следующий набор избранного">
    <i class="fad fa-star hg-icon" aria-hidden="true"></i>
  </button>
</div>
`
);

w(
  'src/partials/shell/head.html',
  `<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="HomeGateway v4.ai — operational cockpit MVP v1">
  <title>HomeGateway v4.ai — MVP v1</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Exo+2:wght@400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/vendor/fontawesome/css/all.min.css">
  <link rel="stylesheet" href="assets/css/main.css">
</head>
`
);

console.log('HTML partials applied to', root);
