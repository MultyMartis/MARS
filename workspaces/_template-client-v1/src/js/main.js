/**
 * Client workspace entry — load after core/*.js
 */
(function () {
  'use strict';

  function boot() {
    if (!window.WfLifecycle) {
      console.error('[Client] WfLifecycle missing — check script order in page entry');
      return;
    }
    window.WfLifecycle.initCore();
    window.WfLifecycle.initPage();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
