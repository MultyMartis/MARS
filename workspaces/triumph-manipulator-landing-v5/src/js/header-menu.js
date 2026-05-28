const MENU_OPEN_CLASS = 'site-header-menu-open';
const MENU_TRANSITION_MS = 300;
const REDUCED_MQ = window.matchMedia('(prefers-reduced-motion: reduce)');

/**
 * @returns {boolean}
 */
function prefersReducedMotion() {
  return REDUCED_MQ.matches;
}

/**
 * @returns {number}
 */
function getMenuTransitionMs() {
  return prefersReducedMotion() ? 0 : MENU_TRANSITION_MS;
}

/**
 * @returns {string}
 */
function getCleanPath() {
  const { pathname, search } = window.location;
  return `${pathname}${search}`;
}

/**
 * @param {string} hash
 * @returns {HTMLElement | null}
 */
function resolveScrollTarget(hash) {
  if (!hash || hash === '#') {
    return null;
  }

  const id = decodeURIComponent(hash.slice(1));
  if (!id) {
    return null;
  }

  const target = document.getElementById(id);
  return target instanceof HTMLElement ? target : null;
}

function stripHashFromUrl() {
  if (!window.location.hash) {
    return;
  }

  history.replaceState(null, '', getCleanPath());
}

/**
 * @returns {number}
 */
function getScrollOffset() {
  const header = document.querySelector('.site-header');
  if (!(header instanceof HTMLElement)) {
    return 0;
  }

  const style = window.getComputedStyle(header);
  if (style.position === 'fixed' || style.position === 'sticky') {
    return header.getBoundingClientRect().height;
  }

  return 0;
}

/**
 * @param {HTMLElement} target
 */
function scrollToSectionTarget(target) {
  const top = Math.max(0, window.scrollY + target.getBoundingClientRect().top - getScrollOffset());
  const behavior = prefersReducedMotion() ? 'auto' : 'smooth';
  window.scrollTo({ top, behavior });
}

/**
 * @param {HTMLAnchorElement} anchor
 * @returns {boolean}
 */
function isInternalSectionLink(anchor) {
  if (anchor.hasAttribute('data-modal-open')) {
    return false;
  }

  const href = anchor.getAttribute('href');
  if (!href || !href.startsWith('#')) {
    return false;
  }

  return resolveScrollTarget(href) !== null;
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
  const navLinks = header.querySelectorAll('.site-header__nav-link');
  const brandLink = header.querySelector('.site-header__brand');

  if (!burger || !closeBtn) {
    return;
  }

  overlay.removeAttribute('hidden');

  let lastFocus = null;
  /** @type {number | null} */
  let closeTimer = null;
  let skipFocusRestoreOnClose = false;

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

      if (skipFocusRestoreOnClose) {
        skipFocusRestoreOnClose = false;
        lastFocus = null;
        return;
      }

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

  const closeMenuForNavigation = () => {
    skipFocusRestoreOnClose = true;
    closeMenu();
  };

  /**
   * @param {MouseEvent} event
   * @param {HTMLAnchorElement} anchor
   * @param {{ fromDrawer?: boolean }} [options]
   * @returns {boolean}
   */
  const handleSectionNavigation = (event, anchor, options = {}) => {
    if (!isInternalSectionLink(anchor)) {
      return false;
    }

    const href = anchor.getAttribute('href');
    const target = href ? resolveScrollTarget(href) : null;

    if (!target) {
      return false;
    }

    event.preventDefault();

    const navigate = () => {
      stripHashFromUrl();
      scrollToSectionTarget(target);
    };

    if (options.fromDrawer && header.classList.contains('site-header--menu-open')) {
      closeMenuForNavigation();
      window.setTimeout(navigate, getMenuTransitionMs());
      return true;
    }

    navigate();
    return true;
  };

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
    link.addEventListener('click', (event) => {
      if (link instanceof HTMLAnchorElement && handleSectionNavigation(event, link, { fromDrawer: true })) {
        return;
      }

      closeMenu();
    });
  });

  navLinks.forEach((link) => {
    link.addEventListener('click', (event) => {
      if (link instanceof HTMLAnchorElement) {
        handleSectionNavigation(event, link);
      }
    });
  });

  if (brandLink instanceof HTMLAnchorElement) {
    brandLink.addEventListener('click', (event) => {
      handleSectionNavigation(event, brandLink);
    });
  }

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

function initHashCleanup() {
  if (!window.location.hash) {
    return;
  }

  if (resolveScrollTarget(window.location.hash)) {
    stripHashFromUrl();
  }
}

initHashCleanup();
