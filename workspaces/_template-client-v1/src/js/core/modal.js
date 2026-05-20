/**
 * Website Factory — modal core
 * @global WfModal
 */
(function (global) {
  'use strict';

  var stack = [];
  var bodyLockCount = 0;
  var scrollbarWidth = 0;

  function getScrollbarWidth() {
    if (scrollbarWidth) return scrollbarWidth;
    var outer = document.createElement('div');
    outer.style.visibility = 'hidden';
    outer.style.overflow = 'scroll';
    document.body.appendChild(outer);
    var inner = document.createElement('div');
    outer.appendChild(inner);
    scrollbarWidth = outer.offsetWidth - inner.offsetWidth;
    outer.parentNode.removeChild(outer);
    return scrollbarWidth;
  }

  function lockBody() {
    bodyLockCount += 1;
    if (bodyLockCount === 1) {
      document.body.classList.add('is-modal-open');
      document.body.style.paddingRight = getScrollbarWidth() + 'px';
    }
  }

  function unlockBody() {
    bodyLockCount = Math.max(0, bodyLockCount - 1);
    if (bodyLockCount === 0) {
      document.body.classList.remove('is-modal-open');
      document.body.style.paddingRight = '';
    }
  }

  function getFocusable(container) {
    return Array.prototype.slice
      .call(
        container.querySelectorAll(
          'a[href], button:not([disabled]), textarea, input:not([disabled]), select:not([disabled]), [tabindex]:not([tabindex="-1"])'
        )
      )
      .filter(function (el) {
        return el.offsetParent !== null || el === document.activeElement;
      });
  }

  function trapFocus(modalEl, dialog) {
    function onKeyDown(e) {
      if (e.key !== 'Tab') return;
      var focusable = getFocusable(dialog);
      if (!focusable.length) return;
      var first = focusable[0];
      var last = focusable[focusable.length - 1];
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    }
    modalEl.__wfTrapFocus = onKeyDown;
    modalEl.addEventListener('keydown', onKeyDown);
  }

  function releaseFocusTrap(modalEl) {
    if (modalEl.__wfTrapFocus) {
      modalEl.removeEventListener('keydown', modalEl.__wfTrapFocus);
      delete modalEl.__wfTrapFocus;
    }
  }

  function open(modalId, trigger) {
    var modal = document.getElementById(modalId);
    if (!modal || modal.getAttribute('data-module') !== 'modal') return;

    var entry = stack.find(function (s) {
      return s.el === modal;
    });
    if (entry) return;

    var dialog = modal.querySelector('.wf-modal__dialog');
    if (!dialog) return;

    stack.push({ el: modal, trigger: trigger || null });
    modal.hidden = false;
    modal.setAttribute('aria-hidden', 'false');
    lockBody();
    trapFocus(modal, dialog);

    var focusable = getFocusable(dialog);
    var closeBtn = modal.querySelector('.wf-modal__close');
    (closeBtn || focusable[0] || dialog).focus();

    document.dispatchEvent(
      new CustomEvent('wf:modal:open', { detail: { id: modalId }, bubbles: true })
    );
  }

  function closeModal(modal, restoreFocus) {
    var idx = stack.findIndex(function (s) {
      return s.el === modal;
    });
    if (idx === -1) return;

    var entry = stack.splice(idx, 1)[0];
    releaseFocusTrap(modal);
    modal.hidden = true;
    modal.setAttribute('aria-hidden', 'true');
    unlockBody();

    if (restoreFocus !== false && entry.trigger && document.contains(entry.trigger)) {
      entry.trigger.focus();
    }

    document.dispatchEvent(
      new CustomEvent('wf:modal:close', {
        detail: { id: modal.id },
        bubbles: true
      })
    );
  }

  function closeTop() {
    if (!stack.length) return;
    closeModal(stack[stack.length - 1].el, true);
  }

  function initModal(root) {
    if (root.__wfModalBound) return;
    root.__wfModalBound = true;

    function onCloseClick(e) {
      if (e.target.closest('[data-modal-close]')) {
        e.preventDefault();
        closeModal(root, true);
      }
    }

    root.__wfModalCloseHandler = onCloseClick;
    root.addEventListener('click', onCloseClick);
  }

  function destroyModal(root) {
    if (!root.__wfModalBound) return;
    if (!root.hidden) closeModal(root, false);
    if (root.__wfModalCloseHandler) {
      root.removeEventListener('click', root.__wfModalCloseHandler);
      delete root.__wfModalCloseHandler;
    }
    delete root.__wfModalBound;
  }

  global.WfModal = {
    open: open,
    close: closeModal,
    closeTop: closeTop
  };

  if (global.WfLifecycle) {
    global.WfLifecycle.registerModule('modal', {
      init: initModal,
      destroy: destroyModal
    });
  }
})(typeof window !== 'undefined' ? window : global);
