/**
 * i-SEO Report Hub — Static Demo v0.1
 * Minimal demo-only interactions. No backend.
 */
(function () {
  'use strict';

  // Active nav highlighting
  var currentPage = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.sidebar__nav a[data-page]').forEach(function (link) {
    if (link.getAttribute('data-page') === currentPage) {
      link.classList.add('is-active');
    }
  });

  // Collapsible evidence appendix (client report)
  document.querySelectorAll('[data-collapsible-toggle]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var targetId = btn.getAttribute('data-collapsible-toggle');
      var target = document.getElementById(targetId);
      if (!target) return;
      var isHidden = target.hidden;
      target.hidden = !isHidden;
      btn.textContent = isHidden ? 'Скрыть приложение' : 'Показать приложение';
    });
  });

  // Demo-only approve/revision buttons
  document.querySelectorAll('[data-demo-action]').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      var action = btn.getAttribute('data-demo-action');
      var msg = document.querySelector('[data-demo-feedback]');
      if (msg) {
        var labels = {
          approve: 'Демо: отчёт отмечен как утверждённый (без сохранения).',
          revision: 'Демо: запрос на доработку отправлен (без сохранения).',
          save: 'Демо: черновик сохранён (без сохранения).',
          submit: 'Демо: отправлено на проверку (без сохранения).',
          preview: 'Демо: открывается предпросмотр клиентского отчёта.'
        };
        msg.textContent = labels[action] || 'Демо-действие выполнено (без сохранения).';
        msg.hidden = false;
      }
    });
  });

  // Week selector demo (weekly editor)
  var weekSelect = document.querySelector('[data-week-select]');
  if (weekSelect) {
    weekSelect.addEventListener('change', function () {
      var indicator = document.querySelector('[data-week-indicator]');
      if (indicator) {
        indicator.textContent = 'Неделя ' + weekSelect.value;
      }
    });
  }
})();
