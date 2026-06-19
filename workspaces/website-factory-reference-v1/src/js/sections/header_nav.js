/**
 * HEADER_NAV — mobile menu toggle (minimal reference behavior)
 */
(function (global) {
  'use strict';

  var OPEN_CLASS = 'wf-header-nav--menu-open';
  var DESKTOP_MQ = global.matchMedia('(min-width: 1024px)');

  function setMenuState(root, toggle, panel, isOpen) {
    root.classList.toggle(OPEN_CLASS, isOpen);
    toggle.setAttribute('aria-expanded', String(isOpen));
    toggle.setAttribute('aria-label', isOpen ? 'Close navigation' : 'Open navigation');
    panel.hidden = !isOpen;
    panel.setAttribute('aria-hidden', String(!isOpen));
  }

  function init(root) {
    if (!root || root.__wfHeaderNavBound) return;
    root.__wfHeaderNavBound = true;

    var toggle = root.querySelector('.wf-header-nav__toggle');
    var panel = root.querySelector('#wf-header-nav-menu');

    if (!toggle || !panel) return;

    var mobileLinks = panel.querySelectorAll('.wf-header-nav__mobile-link');

    function closeMenu() {
      if (!root.classList.contains(OPEN_CLASS)) return;
      setMenuState(root, toggle, panel, false);
    }

    function openMenu() {
      if (root.classList.contains(OPEN_CLASS)) return;
      setMenuState(root, toggle, panel, true);
    }

    toggle.addEventListener('click', function () {
      if (root.classList.contains(OPEN_CLASS)) {
        closeMenu();
      } else {
        openMenu();
      }
    });

    mobileLinks.forEach(function (link) {
      link.addEventListener('click', closeMenu);
    });

    document.addEventListener('keydown', function (event) {
      if (event.key !== 'Escape') return;
      if (!root.classList.contains(OPEN_CLASS)) return;
      event.preventDefault();
      closeMenu();
      toggle.focus();
    });

    function handleViewportChange() {
      if (DESKTOP_MQ.matches) {
        closeMenu();
      }
    }

    if (typeof DESKTOP_MQ.addEventListener === 'function') {
      DESKTOP_MQ.addEventListener('change', handleViewportChange);
    } else if (typeof DESKTOP_MQ.addListener === 'function') {
      DESKTOP_MQ.addListener(handleViewportChange);
    }

    if (global.WfLifecycle && typeof global.WfLifecycle.onResize === 'function') {
      global.WfLifecycle.onResize(handleViewportChange);
    }
  }

  function destroy(root) {
    if (!root) return;

    var toggle = root.querySelector('.wf-header-nav__toggle');
    var panel = root.querySelector('#wf-header-nav-menu');

    if (toggle && panel) {
      setMenuState(root, toggle, panel, false);
    }

    root.classList.remove(OPEN_CLASS);
    delete root.__wfHeaderNavBound;
  }

  if (global.WfLifecycle) {
    global.WfLifecycle.registerModule('header-nav', { init: init, destroy: destroy });
  }
})(typeof window !== 'undefined' ? window : global);
