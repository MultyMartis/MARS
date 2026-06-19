/**
 * SEARCH — clear control, mobile panel, demo submit (no backend)
 */
(function (global) {
  'use strict';

  var OPEN_CLASS = 'wf-search--panel-open';
  var BODY_LOCK_CLASS = 'wf-search-reference--panel-open';
  var DESKTOP_MQ = global.matchMedia('(min-width: 1024px)');

  function isDesktop() {
    return DESKTOP_MQ.matches;
  }

  function isCompact(root) {
    return root.classList.contains('wf-search--compact');
  }

  function getStatusNode(root) {
    var host = root.closest('.wf-search-reference-main');
    return host ? host.querySelector('.wf-search-reference__status') : null;
  }

  function setStatus(root, message) {
    var status = getStatusNode(root);
    if (!status) return;
    status.textContent = message;
  }

  function syncClearButton(input, clearButton) {
    if (!input || !clearButton) return;
    var hasValue = input.value.trim().length > 0;
    clearButton.hidden = !hasValue;
    clearButton.disabled = !hasValue;
  }

  function getTriggers(root) {
    return Array.prototype.slice.call(root.querySelectorAll('[data-search-open]'));
  }

  function setTriggerState(triggers, isOpen) {
    triggers.forEach(function (trigger) {
      trigger.setAttribute('aria-expanded', String(isOpen));
    });
  }

  function setPanelOpen(root, backdrop, triggers, isOpen) {
    root.classList.toggle(OPEN_CLASS, isOpen);
    document.body.classList.toggle(BODY_LOCK_CLASS, isOpen && !isDesktop() && isCompact(root));

    if (backdrop) {
      backdrop.hidden = !isOpen || isDesktop() || !isCompact(root);
      backdrop.setAttribute('aria-hidden', String(!isOpen || isDesktop() || !isCompact(root)));
    }

    setTriggerState(triggers, isOpen);
  }

  function init(root) {
    if (!root || root.__wfSearchBound) return;
    root.__wfSearchBound = true;

    var form = root.querySelector('[data-search-form]');
    var input = root.querySelector('[data-search-input]');
    var clearButton = root.querySelector('[data-search-clear]');
    var backdrop = root.querySelector('[data-search-backdrop]');
    var closeButtons = root.querySelectorAll('[data-search-close]');
    var triggers = getTriggers(root);

    function closePanel() {
      if (!root.classList.contains(OPEN_CLASS)) return;
      setPanelOpen(root, backdrop, triggers, false);
    }

    function openPanel() {
      if (isDesktop() || !isCompact(root) || root.classList.contains(OPEN_CLASS)) return;
      setPanelOpen(root, backdrop, triggers, true);
      if (input) input.focus();
    }

    function handleViewportChange() {
      if (isDesktop() || !isCompact(root)) {
        closePanel();
        document.body.classList.remove(BODY_LOCK_CLASS);
        if (backdrop) {
          backdrop.hidden = true;
          backdrop.setAttribute('aria-hidden', 'true');
        }
        setTriggerState(triggers, false);
      }
    }

    triggers.forEach(function (trigger) {
      trigger.addEventListener('click', function () {
        if (isDesktop() || !isCompact(root)) return;
        if (root.classList.contains(OPEN_CLASS)) {
          closePanel();
          trigger.focus();
        } else {
          openPanel();
        }
      });
    });

    closeButtons.forEach(function (button) {
      button.addEventListener('click', function () {
        closePanel();
        var firstTrigger = triggers[0];
        if (firstTrigger) firstTrigger.focus();
      });
    });

    if (backdrop) {
      backdrop.addEventListener('click', closePanel);
    }

    root.__wfSearchKeydown = function (event) {
      if (event.key !== 'Escape') return;
      if (!root.classList.contains(OPEN_CLASS)) return;
      event.preventDefault();
      closePanel();
      var firstTrigger = triggers[0];
      if (firstTrigger) firstTrigger.focus();
    };

    document.addEventListener('keydown', root.__wfSearchKeydown);

    if (input) {
      root.__wfSearchInput = function () {
        syncClearButton(input, clearButton);
      };

      input.addEventListener('input', root.__wfSearchInput);
      syncClearButton(input, clearButton);
    }

    if (clearButton && input) {
      clearButton.addEventListener('click', function () {
        input.value = '';
        syncClearButton(input, clearButton);
        input.focus();
        setStatus(root, 'Search cleared.');
      });
    }

    if (form) {
      root.__wfSearchSubmit = function (event) {
        event.preventDefault();

        if (!input || !input.value.trim()) {
          if (input) input.reportValidity();
          setStatus(root, 'Enter a search query.');
          return;
        }

        setStatus(root, 'Reference form submitted without a backend.');
      };

      form.addEventListener('submit', root.__wfSearchSubmit);
    }

    if (typeof DESKTOP_MQ.addEventListener === 'function') {
      DESKTOP_MQ.addEventListener('change', handleViewportChange);
    } else if (typeof DESKTOP_MQ.addListener === 'function') {
      DESKTOP_MQ.addListener(handleViewportChange);
    }

    if (global.WfLifecycle && typeof global.WfLifecycle.onResize === 'function') {
      global.WfLifecycle.onResize(handleViewportChange);
    }

    handleViewportChange();
  }

  function destroy(root) {
    if (!root) return;

    var form = root.querySelector('[data-search-form]');
    var input = root.querySelector('[data-search-input]');
    var backdrop = root.querySelector('[data-search-backdrop]');
    var triggers = getTriggers(root);

    if (root.__wfSearchKeydown) {
      document.removeEventListener('keydown', root.__wfSearchKeydown);
      delete root.__wfSearchKeydown;
    }

    if (input && root.__wfSearchInput) {
      input.removeEventListener('input', root.__wfSearchInput);
      delete root.__wfSearchInput;
    }

    if (form && root.__wfSearchSubmit) {
      form.removeEventListener('submit', root.__wfSearchSubmit);
      delete root.__wfSearchSubmit;
    }

    setPanelOpen(root, backdrop, triggers, false);
    document.body.classList.remove(BODY_LOCK_CLASS);
    delete root.__wfSearchBound;
  }

  if (global.WfLifecycle) {
    global.WfLifecycle.registerModule('search', { init: init, destroy: destroy });
  }
})(typeof window !== 'undefined' ? window : global);
