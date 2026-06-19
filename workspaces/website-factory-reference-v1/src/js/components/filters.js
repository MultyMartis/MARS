/**
 * FILTERS — mobile panel, ARIA sync, demo active-count (no filtering)
 */
(function (global) {
  'use strict';

  var OPEN_CLASS = 'wf-filters--panel-open';
  var BODY_LOCK_CLASS = 'wf-filters-reference--panel-open';
  var DESKTOP_MQ = global.matchMedia('(min-width: 1024px)');

  function isDesktop() {
    return DESKTOP_MQ.matches;
  }

  function getTriggers(root) {
    var panelId = root.id;
    if (!panelId) return [];
    return Array.prototype.slice.call(
      document.querySelectorAll('[data-filters-open][aria-controls="' + panelId + '"]')
    );
  }

  function setTriggerState(triggers, isOpen) {
    triggers.forEach(function (trigger) {
      trigger.setAttribute('aria-expanded', String(isOpen));
    });
  }

  function setPanelDialogState(panel, isOpen) {
    if (!panel) return;
    if (isDesktop()) {
      panel.setAttribute('aria-modal', 'false');
      return;
    }
    panel.setAttribute('aria-modal', String(isOpen));
  }

  function updateActiveCount(form, countNode) {
    if (!form || !countNode) return;

    var total = 0;
    var checkboxes = form.querySelectorAll('input[type="checkbox"]:checked');
    total += checkboxes.length;

    form.querySelectorAll('input[type="radio"]').forEach(function (radio) {
      if (radio.checked && radio.value !== 'all') {
        total += 1;
      }
    });

    form.querySelectorAll('.wf-filters__range-input').forEach(function (input) {
      if (input.value && input.value.trim() !== '') {
        total += 1;
      }
    });

    countNode.textContent = String(total);
  }

  function setPanelOpen(root, panel, backdrop, triggers, isOpen) {
    root.classList.toggle(OPEN_CLASS, isOpen);
    document.body.classList.toggle(BODY_LOCK_CLASS, isOpen && !isDesktop());

    if (backdrop) {
      backdrop.hidden = !isOpen || isDesktop();
      backdrop.setAttribute('aria-hidden', String(!isOpen || isDesktop()));
    }

    setTriggerState(triggers, isOpen);
    setPanelDialogState(panel, isOpen);
  }

  function init(root) {
    if (!root || root.__wfFiltersBound) return;
    root.__wfFiltersBound = true;

    var panel = root.querySelector('.wf-filters__panel');
    var backdrop = root.querySelector('[data-filters-backdrop]');
    var closeButtons = root.querySelectorAll('[data-filters-close]');
    var form = root.querySelector('[data-filters-form]');
    var countNode = root.querySelector('[data-filters-count]');
    var triggers = getTriggers(root);

    function closePanel() {
      if (!root.classList.contains(OPEN_CLASS)) return;
      setPanelOpen(root, panel, backdrop, triggers, false);
    }

    function openPanel() {
      if (isDesktop() || root.classList.contains(OPEN_CLASS)) return;
      setPanelOpen(root, panel, backdrop, triggers, true);
    }

    function handleViewportChange() {
      if (isDesktop()) {
        closePanel();
        document.body.classList.remove(BODY_LOCK_CLASS);
        if (backdrop) {
          backdrop.hidden = true;
          backdrop.setAttribute('aria-hidden', 'true');
        }
        setPanelDialogState(panel, false);
        setTriggerState(triggers, false);
      }
    }

    triggers.forEach(function (trigger) {
      trigger.addEventListener('click', function () {
        if (isDesktop()) return;
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

    root.__wfFiltersKeydown = function (event) {
      if (event.key !== 'Escape') return;
      if (!root.classList.contains(OPEN_CLASS)) return;
      event.preventDefault();
      closePanel();
      var firstTrigger = triggers[0];
      if (firstTrigger) firstTrigger.focus();
    };

    document.addEventListener('keydown', root.__wfFiltersKeydown);

    if (form) {
      root.__wfFiltersSubmit = function (event) {
        event.preventDefault();
        updateActiveCount(form, countNode);
      };

      root.__wfFiltersChange = function () {
        updateActiveCount(form, countNode);
      };

      root.__wfFiltersReset = function () {
        global.setTimeout(function () {
          updateActiveCount(form, countNode);
        }, 0);
      };

      form.addEventListener('submit', root.__wfFiltersSubmit);
      form.addEventListener('change', root.__wfFiltersChange);
      form.addEventListener('input', root.__wfFiltersChange);
      form.addEventListener('reset', root.__wfFiltersReset);
      updateActiveCount(form, countNode);
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

    var panel = root.querySelector('.wf-filters__panel');
    var backdrop = root.querySelector('[data-filters-backdrop]');
    var form = root.querySelector('[data-filters-form]');
    var triggers = getTriggers(root);

    if (root.__wfFiltersKeydown) {
      document.removeEventListener('keydown', root.__wfFiltersKeydown);
      delete root.__wfFiltersKeydown;
    }

    if (form) {
      if (root.__wfFiltersSubmit) form.removeEventListener('submit', root.__wfFiltersSubmit);
      if (root.__wfFiltersChange) form.removeEventListener('change', root.__wfFiltersChange);
      if (root.__wfFiltersInput) form.removeEventListener('input', root.__wfFiltersChange);
      if (root.__wfFiltersReset) form.removeEventListener('reset', root.__wfFiltersReset);
      delete root.__wfFiltersSubmit;
      delete root.__wfFiltersChange;
      delete root.__wfFiltersReset;
    }

    setPanelOpen(root, panel, backdrop, triggers, false);
    document.body.classList.remove(BODY_LOCK_CLASS);
    delete root.__wfFiltersBound;
  }

  if (global.WfLifecycle) {
    global.WfLifecycle.registerModule('filters', { init: init, destroy: destroy });
  }
})(typeof window !== 'undefined' ? window : global);
