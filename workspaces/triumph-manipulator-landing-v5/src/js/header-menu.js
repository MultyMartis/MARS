const MENU_OPEN_CLASS = 'site-header-menu-open';
const MENU_TRANSITION_MS = 300;

/**
 * @returns {boolean}
 */
function prefersReducedMotion() {
  return window.matchMedia('(prefers-reduced-motion: reduce)').matches;
}

/**
 * @returns {number}
 */
function getMenuTransitionMs() {
  return prefersReducedMotion() ? 0 : MENU_TRANSITION_MS;
}

/**
 * @param {HTMLElement} drawer
 * @param {HTMLElement} overlay
 */
function portalMenuLayers(drawer, overlay) {
  if (overlay.parentElement !== document.body) {
    document.body.appendChild(overlay);
  }

  if (drawer.parentElement !== document.body) {
    document.body.appendChild(drawer);
  }
}

function lockBodyForMenu() {
  document.documentElement.classList.add(MENU_OPEN_CLASS);
  document.body.classList.add(MENU_OPEN_CLASS);
}

function unlockBodyForMenu() {
  document.documentElement.classList.remove(MENU_OPEN_CLASS);
  document.body.classList.remove(MENU_OPEN_CLASS);
}

/**
 * @param {HTMLElement} header
 */
function initSiteHeaderMenu(header) {
  if (!header || header.dataset.menuInit === 'true') {
    return;
  }

  header.dataset.menuInit = 'true';

  const burger = header.querySelector('.site-header__burger');
  const drawer = header.querySelector('.site-header__drawer');
  const overlay = header.querySelector('[data-header-overlay]');

  if (!(drawer instanceof HTMLElement) || !(overlay instanceof HTMLElement)) {
    return;
  }

  portalMenuLayers(drawer, overlay);

  const closeBtn = drawer.querySelector('.site-header__drawer-close');
  const drawerLinks = drawer.querySelectorAll('.site-header__drawer-link');

  if (!burger || !closeBtn) {
    return;
  }

  overlay.removeAttribute('hidden');

  let lastFocus = null;
  /** @type {number | null} */
  let closeTimer = null;

  const clearCloseTimer = () => {
    if (closeTimer !== null) {
      window.clearTimeout(closeTimer);
      closeTimer = null;
    }
  };

  const applyMenuState = (isOpen) => {
    header.classList.toggle('site-header--menu-open', isOpen);
    burger.setAttribute('aria-expanded', String(isOpen));
    drawer.setAttribute('aria-hidden', String(!isOpen));
    overlay.setAttribute('aria-hidden', String(!isOpen));
    overlay.classList.toggle('site-header__overlay--visible', isOpen);
  };

  const setMenuOpen = (isOpen) => {
    clearCloseTimer();

    if (isOpen) {
      if (header.classList.contains('site-header--menu-open')) {
        return;
      }

      lastFocus = document.activeElement instanceof HTMLElement ? document.activeElement : null;
      lockBodyForMenu();
      applyMenuState(true);
      closeBtn.focus();
      return;
    }

    if (!header.classList.contains('site-header--menu-open')) {
      return;
    }

    applyMenuState(false);

    closeTimer = window.setTimeout(() => {
      unlockBodyForMenu();
      closeTimer = null;

      if (lastFocus && typeof lastFocus.focus === 'function') {
        lastFocus.focus();
      } else {
        burger.focus();
      }

      lastFocus = null;
    }, getMenuTransitionMs());
  };

  const openMenu = () => setMenuOpen(true);
  const closeMenu = () => setMenuOpen(false);

  burger.addEventListener('click', () => {
    if (header.classList.contains('site-header--menu-open')) {
      closeMenu();
      return;
    }

    openMenu();
  });

  closeBtn.addEventListener('click', closeMenu);
  overlay.addEventListener('click', closeMenu);

  drawerLinks.forEach((link) => {
    link.addEventListener('click', closeMenu);
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && header.classList.contains('site-header--menu-open')) {
      event.preventDefault();
      closeMenu();
    }
  });

  const desktopNavQuery = window.matchMedia('(min-width: 1241px)');

  const handleViewportChange = () => {
    if (desktopNavQuery.matches && header.classList.contains('site-header--menu-open')) {
      closeMenu();
    }
  };

  if (typeof desktopNavQuery.addEventListener === 'function') {
    desktopNavQuery.addEventListener('change', handleViewportChange);
  } else if (typeof desktopNavQuery.addListener === 'function') {
    desktopNavQuery.addListener(handleViewportChange);
  }
}
