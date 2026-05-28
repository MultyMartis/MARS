const MODAL_ROOT_INIT = 'data-modal-system';
const OPEN_CLASS = 'site-modal--open';
const BODY_LOCK_CLASS = 'site-modal-open';
const HEADER_MENU_BODY_LOCK_CLASS = 'site-header-menu-open';
const DYNAMIC_TITLE_SELECTOR = '[data-modal-dynamic-title]';
const DESKTOP_MODAL_QUERY = '(min-width: 1025px)';

/** @type {HTMLElement | null} */
let activeModal = null;

/** @type {HTMLElement | null} */
let lastFocusedElement = null;

/** @type {((event: KeyboardEvent) => void) | null} */
let keydownHandler = null;

/**
 * @param {HTMLElement} modal
 * @returns {HTMLElement[]}
 */
function getFocusableElements(modal) {
  const dialog = modal.querySelector('.site-modal__dialog');
  if (!dialog) {
    return [];
  }

  return Array.from(
    dialog.querySelectorAll(
      'a[href], button:not([disabled]), input:not([disabled]):not([type="hidden"]), textarea:not([disabled]), select:not([disabled]), [tabindex]:not([tabindex="-1"])'
    )
  ).filter((element) => element instanceof HTMLElement && !element.hasAttribute('hidden'));
}

/**
 * @param {HTMLElement} modal
 */
function trapFocus(modal, event) {
  if (event.key !== 'Tab') {
    return;
  }

  const focusable = getFocusableElements(modal);
  if (!focusable.length) {
    return;
  }

  const first = focusable[0];
  const last = focusable[focusable.length - 1];
  const active = document.activeElement;

  if (event.shiftKey && active === first) {
    event.preventDefault();
    last.focus();
    return;
  }

  if (!event.shiftKey && active === last) {
    event.preventDefault();
    first.focus();
  }
}

function lockBodyScroll() {
  document.body.classList.add(BODY_LOCK_CLASS);
}

function unlockBodyScroll() {
  document.body.classList.remove(BODY_LOCK_CLASS);
}

/**
 * @param {HTMLElement} modal
 * @param {HTMLElement} trigger
 */
function applyModalTitle(modal, trigger) {
  const titleEl = modal.querySelector(DYNAMIC_TITLE_SELECTOR);
  if (!(titleEl instanceof HTMLElement)) {
    return;
  }

  const defaultTitle = titleEl.dataset.modalTitleDefault || titleEl.textContent || '';
  const customTitle = trigger.getAttribute('data-modal-title');

  titleEl.textContent = customTitle || defaultTitle;
}

/**
 * @param {HTMLElement} modal
 */
function resetModalTitle(modal) {
  const titleEl = modal.querySelector(DYNAMIC_TITLE_SELECTOR);
  if (!(titleEl instanceof HTMLElement)) {
    return;
  }

  const defaultTitle = titleEl.dataset.modalTitleDefault;
  if (defaultTitle) {
    titleEl.textContent = defaultTitle;
  }
}

/**
 * @param {HTMLElement} modal
 */
function openModal(modal) {
  if (activeModal === modal) {
    return;
  }

  if (activeModal) {
    closeModal(activeModal, { restoreFocus: false });
  }

  lastFocusedElement = document.activeElement instanceof HTMLElement ? document.activeElement : null;

  modal.removeAttribute('hidden');
  modal.setAttribute('aria-hidden', 'false');
  modal.classList.add(OPEN_CLASS);
  activeModal = modal;
  lockBodyScroll();

  const focusable = getFocusableElements(modal);
  const preferredFocus = modal.querySelector('[data-modal-focus]');
  const focusTarget =
    preferredFocus instanceof HTMLElement
      ? preferredFocus
      : focusable.find((element) => element.matches('input, textarea, select')) || focusable[0];

  if (focusTarget instanceof HTMLElement) {
    window.requestAnimationFrame(() => {
      focusTarget.focus();
    });
  }

  document.dispatchEvent(
    new CustomEvent('site-modal:open', {
      detail: { modalId: modal.dataset.modalId || modal.id },
      bubbles: true,
    })
  );
}

/**
 * @param {HTMLElement} modal
 * @param {{ restoreFocus?: boolean }} [options]
 */
function closeModal(modal, options = {}) {
  const { restoreFocus = true } = options;

  if (!modal.classList.contains(OPEN_CLASS)) {
    return;
  }

  modal.classList.remove(OPEN_CLASS);
  modal.setAttribute('aria-hidden', 'true');

  const handleTransitionEnd = (event) => {
    if (event.target !== modal) {
      return;
    }

    modal.setAttribute('hidden', '');
    modal.removeEventListener('transitionend', handleTransitionEnd);
  };

  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (prefersReducedMotion) {
    modal.setAttribute('hidden', '');
  } else {
    modal.addEventListener('transitionend', handleTransitionEnd);
    window.setTimeout(() => {
      if (!modal.classList.contains(OPEN_CLASS)) {
        modal.setAttribute('hidden', '');
      }
    }, 350);
  }

  if (activeModal === modal) {
    activeModal = null;
    unlockBodyScroll();
    resetModalTitle(modal);
  }

  if (restoreFocus && lastFocusedElement && typeof lastFocusedElement.focus === 'function') {
    lastFocusedElement.focus();
  }

  lastFocusedElement = null;

  document.dispatchEvent(
    new CustomEvent('site-modal:close', {
      detail: { modalId: modal.dataset.modalId || modal.id },
      bubbles: true,
    })
  );
}

/**
 * @param {string} modalId
 * @returns {HTMLElement | null}
 */
function resolveModal(modalId) {
  if (!modalId) {
    return null;
  }

  return (
    document.querySelector(`[data-modal-id="${modalId}"]`) ||
    document.getElementById(modalId)
  );
}

/**
 * @param {HTMLElement} trigger
 */
function handleOpenTrigger(trigger, event) {
  const modalId = trigger.getAttribute('data-modal-open');
  const modal = resolveModal(modalId);

  if (!modal) {
    return;
  }

  event.preventDefault();

  const ctaSource = trigger.getAttribute('data-cta-source') || trigger.dataset.ctaSource || '';
  if (ctaSource) {
    modal.dataset.pendingCtaSource = ctaSource;
    document.dispatchEvent(
      new CustomEvent('site-modal:cta', {
        detail: { modalId: modal.dataset.modalId || modal.id, ctaSource },
        bubbles: true,
      })
    );
  }

  const header = document.querySelector('.site-header.site-header--menu-open');
  if (header) {
    header.classList.remove('site-header--menu-open');
    const burger = header.querySelector('.site-header__burger');
    if (burger) {
      burger.setAttribute('aria-expanded', 'false');
    }
  }

  const drawer = document.querySelector('.site-header__drawer');
  const overlay = document.querySelector('[data-header-overlay]');
  if (drawer) {
    drawer.setAttribute('aria-hidden', 'true');
  }
  if (overlay) {
    overlay.classList.remove('site-header__overlay--visible');
    overlay.setAttribute('aria-hidden', 'true');
  }

  if (document.body.classList.contains(HEADER_MENU_BODY_LOCK_CLASS)) {
    document.documentElement.classList.remove(HEADER_MENU_BODY_LOCK_CLASS);
    document.body.classList.remove(HEADER_MENU_BODY_LOCK_CLASS);
  }

  applyModalTitle(modal, trigger);
  openModal(modal);
}

/**
 * @param {HTMLElement} root
 */
function bindModalTriggers(root) {
  root.querySelectorAll('[data-modal-open]').forEach((trigger) => {
    if (!(trigger instanceof HTMLElement) || trigger.dataset.modalTriggerBound === 'true') {
      return;
    }

    trigger.dataset.modalTriggerBound = 'true';
    trigger.addEventListener('click', (event) => handleOpenTrigger(trigger, event));
  });

  root.querySelectorAll('[data-modal-close]').forEach((trigger) => {
    if (!(trigger instanceof HTMLElement) || trigger.dataset.modalCloseBound === 'true') {
      return;
    }

    trigger.dataset.modalCloseBound = 'true';
    trigger.addEventListener('click', (event) => {
      const modal = trigger.closest('[data-modal]');
      if (!modal || !(modal instanceof HTMLElement)) {
        return;
      }

      event.preventDefault();
      closeModal(modal);
    });
  });
}

/**
 * @param {HTMLElement} root
 */
function bindDesktopOnlyModalTriggers(root) {
  root.querySelectorAll('[data-desktop-modal-open]').forEach((trigger) => {
    if (!(trigger instanceof HTMLElement) || trigger.dataset.desktopModalTriggerBound === 'true') {
      return;
    }

    trigger.dataset.desktopModalTriggerBound = 'true';
    trigger.addEventListener('click', (event) => {
      if (!window.matchMedia(DESKTOP_MODAL_QUERY).matches) {
        return;
      }

      const modalId = trigger.getAttribute('data-desktop-modal-open');
      const modal = resolveModal(modalId);
      if (!modal) {
        return;
      }

      event.preventDefault();
      openModal(modal);
    });
  });
}

function bindGlobalHandlers() {
  if (keydownHandler) {
    return;
  }

  keydownHandler = (event) => {
    if (!activeModal) {
      return;
    }

    if (event.key === 'Escape') {
      event.preventDefault();
      closeModal(activeModal);
      return;
    }

    trapFocus(activeModal, event);
  };

  document.addEventListener('keydown', keydownHandler);
}

/**
 * @param {HTMLElement} [root]
 */
function initModals(root = document) {
  if (root === document && document.documentElement.getAttribute(MODAL_ROOT_INIT) === 'true') {
    bindModalTriggers(root);
    bindDesktopOnlyModalTriggers(root);
    return;
  }

  if (root === document) {
    document.documentElement.setAttribute(MODAL_ROOT_INIT, 'true');
    bindGlobalHandlers();
  }

  root.querySelectorAll('[data-modal]').forEach((modal) => {
    if (!(modal instanceof HTMLElement) || modal.dataset.modalShellInit === 'true') {
      return;
    }

    modal.dataset.modalShellInit = 'true';
    modal.setAttribute('aria-hidden', 'true');

    if (!modal.hasAttribute('hidden')) {
      modal.setAttribute('hidden', '');
    }

    const overlay = modal.querySelector('.site-modal__overlay');
    if (overlay instanceof HTMLElement) {
      overlay.addEventListener('click', (event) => {
        if (event.target === overlay) {
          closeModal(modal);
        }
      });
    }
  });

  bindModalTriggers(root);
  bindDesktopOnlyModalTriggers(root);
}

/**
 * @param {string} modalId
 */
function openModalById(modalId) {
  const modal = resolveModal(modalId);
  if (modal) {
    openModal(modal);
  }
}

/**
 * @param {string} modalId
 */
function closeModalById(modalId) {
  const modal = resolveModal(modalId);
  if (modal) {
    closeModal(modal);
  }
}

function getActiveModal() {
  return activeModal;
}

function bootstrapModalSystem() {
  initModals(document);
}

if (typeof window !== 'undefined') {
  window.initModals = initModals;
  window.openModalById = openModalById;
  window.closeModalById = closeModalById;
  window.getActiveModal = getActiveModal;

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', bootstrapModalSystem);
  } else {
    bootstrapModalSystem();
  }
}
