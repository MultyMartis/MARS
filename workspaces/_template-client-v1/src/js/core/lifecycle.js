/**
 * Website Factory — lifecycle core (vanilla, jQuery-compatible)
 * @global WfLifecycle
 */
(function (global) {
  'use strict';

  var MODULES = Object.create(null);
  var coreInitialized = false;
  var resizeCallbacks = [];
  var resizeTimer = null;

  function debouncedResize() {
    if (resizeTimer) clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function () {
      resizeCallbacks.forEach(function (cb) {
        try {
          cb();
        } catch (err) {
          console.error('[WfLifecycle] resize callback error', err);
        }
      });
    }, 150);
  }

  function registerModule(name, impl) {
    if (!name || !impl || typeof impl.init !== 'function' || typeof impl.destroy !== 'function') {
      throw new Error('[WfLifecycle] invalid module: ' + name);
    }
    MODULES[name] = impl;
  }

  function onResize(fn) {
    resizeCallbacks.push(fn);
    return function off() {
      resizeCallbacks = resizeCallbacks.filter(function (cb) {
        return cb !== fn;
      });
    };
  }

  function initCore() {
    if (coreInitialized) return;
    coreInitialized = true;
    global.addEventListener('resize', debouncedResize);

    global.addEventListener('click', function (e) {
      var openBtn = e.target.closest('[data-modal-open]');
      if (openBtn && global.WfModal) {
        var id = openBtn.getAttribute('data-modal-open');
        if (id) global.WfModal.open(id, openBtn);
      }
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && global.WfModal) {
        global.WfModal.closeTop();
      }
    });
  }

  function initSection(root) {
    if (!root || root.__wfSectionInit) return;
    root.__wfSectionInit = true;
    var nodes = root.querySelectorAll('[data-module]');
    nodes.forEach(function (el) {
      var name = el.getAttribute('data-module');
      var mod = MODULES[name];
      if (mod) mod.init(el);
    });
  }

  function destroySection(root) {
    if (!root) return;
    var nodes = root.querySelectorAll('[data-module]');
    nodes.forEach(function (el) {
      var name = el.getAttribute('data-module');
      var mod = MODULES[name];
      if (mod) mod.destroy(el);
    });
    delete root.__wfSectionInit;
  }

  function reinitSection(root) {
    destroySection(root);
    initSection(root);
  }

  function initPage() {
    var sections = document.querySelectorAll('[data-section]');
    sections.forEach(initSection);
    var orphanModules = document.querySelectorAll('body > [data-module], main ~ [data-module]');
    orphanModules.forEach(function (el) {
      if (!el.closest('[data-section]')) {
        var name = el.getAttribute('data-module');
        var mod = MODULES[name];
        if (mod) mod.init(el);
      }
    });
  }

  /**
   * Section replacement helper — battle-test survivability
   * @param {HTMLElement} root - section with data-section
   * @param {string} html - new inner HTML for section (keeps outer section attrs)
   */
  function replaceSectionContent(root, html) {
    if (!root || !root.hasAttribute('data-section')) {
      console.warn('[WfLifecycle] replaceSectionContent: not a section root');
      return null;
    }
    destroySection(root);
    root.innerHTML = html;
    initSection(root);
    return root;
  }

  global.WfLifecycle = {
    registerModule: registerModule,
    onResize: onResize,
    initCore: initCore,
    initPage: initPage,
    initSection: initSection,
    destroySection: destroySection,
    reinitSection: reinitSection,
    replaceSectionContent: replaceSectionContent
  };
})(typeof window !== 'undefined' ? window : global);
