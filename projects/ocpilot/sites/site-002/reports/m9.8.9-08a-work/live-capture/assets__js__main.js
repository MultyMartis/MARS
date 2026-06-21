(function () {
  // Универсальный onReady (работает даже если DOM уже готов)
  function onReady(fn) {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', fn);
    } else {
      fn();
    }
  }

  // PHONE MASK (Inputmask preferred, jQuery fallback)
  function initPhoneMask() {
    const nodes = document.querySelectorAll('[data-mask="phone"]');
    if (!nodes.length) return;

    // 1) Pure Inputmask (не зависит от jQuery)
    if (window.Inputmask) {
      nodes.forEach(function (el) {
        window
          .Inputmask({
            mask: '+7 (999) 999-99-99',
            showMaskOnHover: false,
            clearIncomplete: true,
          })
          .mask(el);
      });
      return;
    }

    // 2) jQuery plugin fallback
    if (!window.jQuery || !jQuery.fn || !jQuery.fn.inputmask) return;

    const $inputs = jQuery(nodes);
    $inputs.inputmask({
      mask: '+7 (999) 999-99-99',
      showMaskOnHover: false,
      clearIncomplete: true,
    });
  }

  // EMAIL VALIDATION (no mask, no paste blocking)
  function initEmailValidation() {
    const inputs = document.querySelectorAll('[data-validate="email"]');
    if (!inputs.length) return;

    const strictEmailRe = /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/;

    inputs.forEach((el) => {
      function normalize() {
        const v = el.value || '';
        const cleaned = v.replace(/\s+/g, '').trim();
        if (cleaned !== v) el.value = cleaned;
      }

      function validate() {
        const v = (el.value || '').trim();

        // Если пустое и поле НЕ required — ок
        if (!v && !el.hasAttribute('required')) {
          el.setCustomValidity('');
          return;
        }

        // Если пустое и required — оставляем нативную required-валидацию
        if (!v && el.hasAttribute('required')) {
          el.setCustomValidity('');
          return;
        }

        // запрет кириллицы
        if (/[А-Яа-яЁё]/.test(v)) {
          el.setCustomValidity('Email должен быть латиницей');
          return;
        }

        // строгая проверка формата
        if (!strictEmailRe.test(v)) {
          el.setCustomValidity('Введите email в формате name@domain.ru / .com');
          return;
        }

        el.setCustomValidity('');
      }

      el.addEventListener('input', function () {
        normalize();
        validate();
      });

      el.addEventListener('blur', function () {
        normalize();
        validate();
      });

      el.addEventListener('change', function () {
        normalize();
        validate();
      });
    });
  }

  onReady(function () {
    initPhoneMask();
    initEmailValidation();
  });
})();

// Swiper
(function () {
  function initSwipers() {
    if (!window.Swiper) return;

    document.querySelectorAll('.js-slider').forEach(function (el) {
      new Swiper(el, {
        slidesPerView: 1,
        spaceBetween: 16,
        loop: false,
        pagination: {
          el: el.querySelector('.swiper-pagination'),
          clickable: true,
        },
        navigation: {
          nextEl: el.querySelector('.swiper-button-next'),
          prevEl: el.querySelector('.swiper-button-prev'),
        },
      });
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    initSwipers();
  });
})();

(function () {
  function initCertificatesSlider() {
    if (!window.Swiper) return;

    document.querySelectorAll('.js-certificates-slider').forEach(function (sliderEl) {
      const root = sliderEl.closest('.certificates');
      if (!root) return;

      new Swiper(sliderEl, {
        slidesPerView: 1.15,
        spaceBetween: 16,

        navigation: {
          nextEl: root.querySelector('.certificates__btn--next'),
          prevEl: root.querySelector('.certificates__btn--prev'),
        },

        breakpoints: {
          660: {
            slidesPerView: 2,
            spaceBetween: 15,
          },
          1025: {
            slidesPerView: 4,
            spaceBetween: 24,
          },
        },
      });
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    initCertificatesSlider();
  });
})();








// ОБНОВИТЬ НА ПРОДЕ

(function () {
  const GALLERY_SCROLL_OFFSET = 100;

  function scrollToGallery(root) {
    if (!root) return;

    const rect = root.getBoundingClientRect();
    const top = rect.top + window.pageYOffset - GALLERY_SCROLL_OFFSET;

    window.scrollTo({
      top: top < 0 ? 0 : top,
      behavior: 'smooth',
    });
  }

  function applyProductFancyboxClasses(fb) {
    if (!fb || !fb.container) return;

    fb.container.classList.add('is-product-fancybox');
    fb.container.classList.add('zpm-prod-patch');
  }

  function wrapProductFancyboxSlide(slide) {
    if (!slide || !slide.$content) return;

    var content = slide.$content;

    if (content.closest('.zpm-fb-product__stage')) return;

    var shell = document.createElement('div');
    shell.className = 'zpm-fb-product__shell';

    var container = document.createElement('div');
    container.className = 'container';

    var stage = document.createElement('div');
    stage.className = 'zpm-fb-product__stage';

    var parent = content.parentNode;
    if (!parent) return;

    parent.insertBefore(shell, content);
    shell.appendChild(container);
    container.appendChild(stage);
    stage.appendChild(content);
  }

  var GALLERY_DESKTOP_MQ = window.matchMedia('(min-width: 1025px)');
  var galleryResizeTimer = null;
  var galleryResizeBound = false;

  function isGalleryDesktop() {
    return GALLERY_DESKTOP_MQ.matches;
  }

  function getThumbSwiperOptions() {
    if (isGalleryDesktop()) {
      return {
        direction: 'vertical',
        slidesPerView: 'auto',
        spaceBetween: 8,
        watchSlidesProgress: true,
      };
    }

    return {
      direction: 'horizontal',
      slidesPerView: 3,
      spaceBetween: 10,
      watchSlidesProgress: true,
      breakpoints: {
        660: {
          slidesPerView: 3,
          spaceBetween: 10,
        },
      },
    };
  }

  function destroyProductGallerySwipers(root) {
    if (root._pgMainSwiper) {
      root._pgMainSwiper.destroy(true, true);
      root._pgMainSwiper = null;
    }
    if (root._pgThumbsSwiper) {
      root._pgThumbsSwiper.destroy(true, true);
      root._pgThumbsSwiper = null;
    }
  }

  function createProductGallerySwipers(root) {
    var thumbsEl = root.querySelector('.js-product-thumbs');
    var mainEl = root.querySelector('.js-product-gallery');

    if (!thumbsEl || !mainEl) return;

    var prevBtn = root.querySelector('.product-gallery__btn--prev');
    var nextBtn = root.querySelector('.product-gallery__btn--next');

    var thumbs = new Swiper(thumbsEl, getThumbSwiperOptions());

    root._pgThumbsSwiper = thumbs;

    root._pgMainSwiper = new Swiper(mainEl, {
      slidesPerView: 1,
      spaceBetween: 20,
      navigation: {
        nextEl: nextBtn,
        prevEl: prevBtn,
      },
      thumbs: { swiper: thumbs },
    });
  }

  function bindGalleryScrollHandlers(root) {
    if (root.dataset.pgScrollBound === '1') return;
    root.dataset.pgScrollBound = '1';

    root.querySelectorAll('.product-gallery__thumb').forEach(function (btn) {
      btn.addEventListener('click', function () {
        scrollToGallery(root);
      });
    });

    root.querySelectorAll('[data-fancybox="product"]').forEach(function (link) {
      link.addEventListener('click', function () {
        scrollToGallery(root);
      });
    });
  }

  function rebuildProductGalleries() {
    document.querySelectorAll('.product-gallery').forEach(function (root) {
      destroyProductGallerySwipers(root);
      createProductGallerySwipers(root);
    });
  }

  function scheduleGalleryRebuild() {
    if (galleryResizeTimer) {
      window.clearTimeout(galleryResizeTimer);
    }
    galleryResizeTimer = window.setTimeout(function () {
      galleryResizeTimer = null;
      rebuildProductGalleries();
    }, 150);
  }

  function initProductGallery() {
    if (!window.Swiper) return;

    document.querySelectorAll('.product-gallery').forEach(function (root) {
      bindGalleryScrollHandlers(root);
      destroyProductGallerySwipers(root);
      createProductGallerySwipers(root);
    });

    if (!galleryResizeBound) {
      galleryResizeBound = true;
      GALLERY_DESKTOP_MQ.addEventListener('change', scheduleGalleryRebuild);
    }
  }
function initProductFancybox() {
  if (!window.Fancybox) return;

  try {
    window.Fancybox.unbind('[data-fancybox="product"]');
  } catch (e) {}

  window.Fancybox.bind('[data-fancybox="product"]', {
    mainClass: 'zpm-prod-patch is-product-fancybox',
    dragToClose: false,
    groupAll: true,
    hideScrollbar: false,

    Thumbs: {
      autoStart: true,
    },

    Toolbar: {
      display: {
        left: [],
        middle: [],
        right: ['close'],
      },
    },

    Carousel: {
      infinite: false,
      Panzoom: {
        touch: true,
        wheel: false,
      },
    },

    Images: {
      zoom: false,
    },

    on: {
      init: function (fb) {
        applyProductFancyboxClasses(fb);

        const trigger = fb && fb.options ? fb.options.triggerEl : null;
        const root = trigger ? trigger.closest('.product-gallery') : document.querySelector('.product-gallery');

        scrollToGallery(root);
      },

      reveal: function (fb, slide) {
        applyProductFancyboxClasses(fb);
        wrapProductFancyboxSlide(slide);
      },

      done: function (fb, slide) {
        applyProductFancyboxClasses(fb);
        wrapProductFancyboxSlide(slide);
      },

      destroy: function (fb) {
        const trigger = fb && fb.options ? fb.options.triggerEl : null;
        const root = trigger ? trigger.closest('.product-gallery') : document.querySelector('.product-gallery');

        scrollToGallery(root);
      },
    },
  });
}
  document.addEventListener('DOMContentLoaded', function () {
    initProductGallery();
    initProductFancybox();
  });
})();

(function () {
  var DESKTOP_LIMIT = 8;
  var MOBILE_LIMIT = 5;
  var MOBILE_BREAKPOINT = 767;
  var TEXT_EXPAND = 'Смотреть все характеристики';
  var TEXT_COLLAPSE = 'Скрыть характеристики';

  function debounce(fn, ms) {
    var timer;
    return function () {
      var ctx = this;
      var args = arguments;
      clearTimeout(timer);
      timer = setTimeout(function () {
        fn.apply(ctx, args);
      }, ms);
    };
  }

  function getLimit() {
    return window.innerWidth > MOBILE_BREAKPOINT ? DESKTOP_LIMIT : MOBILE_LIMIT;
  }

  function scrollToProductContentMain() {
    var target = document.querySelector('.product-content__main');
    if (!target) return;

    var isMobile = window.innerWidth <= 1024;
    var offset = isMobile ? 100 : 140;
    var scrollTop =
      window.pageYOffset ||
      document.documentElement.scrollTop ||
      0;
    var targetTop =
      target.getBoundingClientRect().top +
      scrollTop -
      offset;

    window.scrollTo({
      top: Math.max(0, targetTop),
      behavior: 'smooth'
    });
  }

  function measureCollapsedHeight(table, rows, limit) {
    table.style.maxHeight = 'none';

    if (rows.length <= limit) return 0;

    var tableTop = table.getBoundingClientRect().top;
    var lastVisible = rows[limit - 1];
    var lastBottom = lastVisible.getBoundingClientRect().bottom;

    return Math.ceil(lastBottom - tableTop);
  }

  function SpecsCollapse(section) {
    this.section = section;
    this.table = section.querySelector('.spec-table');
    this.toggleWrap = section.querySelector('.product-content__specs-toggle-wrap');
    this.toggleBtn = section.querySelector('[data-product-specs-toggle]');
    this.toggleText = section.querySelector('[data-product-specs-toggle-text]');
    this.isExpanded = false;
    this.collapsedHeight = 0;

    if (!this.table || !this.toggleWrap || !this.toggleBtn) {
      return;
    }

    var self = this;

    this.onTransitionEnd = function (e) {
      if (e.target !== self.table || e.propertyName !== 'max-height') return;

      if (self.isExpanded) {
        self.table.style.maxHeight = 'none';
      }
    };

    this.table.addEventListener('transitionend', this.onTransitionEnd);
    this.toggleBtn.addEventListener('click', function () {
      self.toggle();
    });
  }

  SpecsCollapse.prototype.getRows = function () {
    return Array.prototype.slice.call(this.table.querySelectorAll('.spec-table__row'));
  };

  SpecsCollapse.prototype.setToggleState = function (expanded) {
    if (this.toggleBtn) {
      this.toggleBtn.setAttribute('aria-expanded', expanded ? 'true' : 'false');
    }
    if (this.toggleText) {
      this.toggleText.textContent = expanded ? TEXT_COLLAPSE : TEXT_EXPAND;
    }
  };

  SpecsCollapse.prototype.disable = function () {
    this.section.classList.remove('is-collapsible', 'is-collapsed', 'is-expanded');
    this.table.style.maxHeight = '';
    this.toggleWrap.hidden = true;
    this.isExpanded = false;
    this.setToggleState(false);
  };

  SpecsCollapse.prototype.applyCollapsed = function () {
    this.section.classList.add('is-collapsible', 'is-collapsed');
    this.section.classList.remove('is-expanded');
    this.table.style.maxHeight = this.collapsedHeight + 'px';
    this.isExpanded = false;
    this.setToggleState(false);
  };

  SpecsCollapse.prototype.applyExpanded = function (animate) {
    var self = this;

    this.section.classList.add('is-collapsible', 'is-expanded');
    this.section.classList.remove('is-collapsed');
    this.isExpanded = true;
    this.setToggleState(true);

    if (!animate) {
      this.table.style.maxHeight = 'none';
      return;
    }

    var fullHeight = this.table.scrollHeight;

    if (this.table.style.maxHeight === 'none' || !this.table.style.maxHeight) {
      this.table.style.maxHeight = this.collapsedHeight + 'px';
    }

    requestAnimationFrame(function () {
      self.table.style.maxHeight = fullHeight + 'px';
    });
  };

  SpecsCollapse.prototype.collapseWithAnimation = function () {
    var self = this;
    var fullHeight = this.table.scrollHeight;

    this.table.style.maxHeight = fullHeight + 'px';
    this.section.classList.add('is-collapsed');
    this.section.classList.remove('is-expanded');
    this.isExpanded = false;
    this.setToggleState(false);

    requestAnimationFrame(function () {
      self.table.style.maxHeight = self.collapsedHeight + 'px';
    });
  };

  SpecsCollapse.prototype.toggle = function () {
    if (this.isExpanded) {
      this.collapseWithAnimation();
    } else {
      this.applyExpanded(true);
    }

    scrollToProductContentMain();
  };

  SpecsCollapse.prototype.recalc = function () {
    var rows = this.getRows();
    var limit = getLimit();

    if (rows.length <= limit) {
      this.disable();
      return;
    }

    this.collapsedHeight = measureCollapsedHeight(this.table, rows, limit);
    this.toggleWrap.hidden = false;
    this.section.classList.add('is-collapsible');

    if (this.isExpanded) {
      this.section.classList.add('is-expanded');
      this.section.classList.remove('is-collapsed');
      this.table.style.maxHeight = 'none';
      this.setToggleState(true);
      return;
    }

    this.applyCollapsed();
  };

  SpecsCollapse.prototype.destroy = function () {
    if (this.table && this.onTransitionEnd) {
      this.table.removeEventListener('transitionend', this.onTransitionEnd);
    }
  };

  var controller = null;

  function initProductSpecsCollapse() {
    var section = document.querySelector('.product-content__specifications');
    if (!section) return;

    if (!controller) {
      controller = new SpecsCollapse(section);
    }

    if (!controller.table) return;

    controller.recalc();
  }

  document.addEventListener('DOMContentLoaded', initProductSpecsCollapse);
  window.addEventListener('resize', debounce(function () {
    if (controller) {
      controller.recalc();
    }
  }, 150));
})();








(function () {
  function initTabs() {
    document.querySelectorAll('.js-tabs').forEach(function (tabs) {
      var btns = tabs.querySelectorAll('[data-tab]');
      var panels = tabs.querySelectorAll('[data-panel]');

      btns.forEach(function (btn) {
        btn.addEventListener('click', function () {
          var key = btn.getAttribute('data-tab');

          btns.forEach(function (b) {
            b.classList.toggle('is-active', b === btn);
            b.setAttribute('aria-selected', b === btn ? 'true' : 'false');
          });

          panels.forEach(function (p) {
            p.classList.toggle('is-active', p.getAttribute('data-panel') === key);
          });
        });
      });
    });
  }

  document.addEventListener('DOMContentLoaded', initTabs);
})();
















(function () {
  function initRelProductsSliders() {
    if (!window.Swiper) return;

    document.querySelectorAll(".js-rel-products-slider").forEach(function (root) {
      const section = root.closest(".rel-products");
      if (!section) return;

      const swiperEl = root.querySelector(".swiper");
      const prevBtn = section.querySelector(".rel-products__btn--prev");
      const nextBtn = section.querySelector(".rel-products__btn--next");

      new Swiper(swiperEl, {
        slidesPerView: 2,
        spaceBetween: 15,
        loop: false,
        watchOverflow: true,

        navigation: {
          prevEl: prevBtn,
          nextEl: nextBtn,
        },

        breakpoints: {
          768: {
            slidesPerView: 3,
            spaceBetween: 15,
          },
          1025: {
            slidesPerView: 6,
            spaceBetween: 20,
          },
        },
      });
    });
  }

  document.addEventListener("DOMContentLoaded", initRelProductsSliders);
})();
















// Fancybox
(function () {
  function initFancybox() {
    if (!window.Fancybox) return;

    Fancybox.bind('[data-fancybox]', {
      // базово, без лишнего
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    initFancybox();
  });
})();

// Mobile menu toggle (DEPRECATED)
// Раньше меню открывалось отдельным скриптом (is-menu-open + hidden=true сразу).
// Сейчас мобильное меню управляется через POPUP MANAGER (overlay + анимации).
// Этот блок оставлен как заглушка, чтобы не ломать файл при мерже.
(function () {
  // Если в проекте включён наш overlay-режим — выходим.
  if (document.querySelector('[data-overlay]') && document.querySelector('[data-mobile-menu]')) return;
})();

























































































/* ================================
   POPUP MANAGER v2 (без мигания оверлея)
   FIX:
   - корректная закрывающая анимация поиска (suppress focusin reopen)
   - НЕ закрываем наши попапы (каталог/поиск) при кликах по Fancybox
   - Публичный API: window.ZpmPopupManager.closeAll()
================================ */

(function () {
  const overlay = document.querySelector('[data-overlay]');
  const ANIM_MS = 300;

  /* ================================
     HELPERS
  ================================ */

  function getPopupViewportTop() {
    return window.innerWidth <= 1024 ? 90 : 140;
  }

  function applyCatalogViewportPosition() {
    const layer = document.querySelector('[data-catalog]');
    const panel = layer ? layer.querySelector('.zpm-catalog__panel') : null;
    if (!layer || !panel) return;

    layer.style.position = 'fixed';
    layer.style.inset = '0';
    layer.style.top = '0';
    layer.style.left = '0';
    layer.style.right = '0';
    layer.style.bottom = '0';

    panel.style.position = 'fixed';
    panel.style.top = getPopupViewportTop() + 'px';
    panel.style.left = '50%';
    panel.style.right = 'auto';
    panel.style.bottom = 'auto';
    panel.style.transform = 'translateX(-50%)';
    panel.style.maxHeight = 'calc(100vh - ' + (getPopupViewportTop() + 16) + 'px)';
  }

  function syncActivePopupViewportPosition() {
    if (!activeName) return;

    if (activeName === 'catalog') {
      applyCatalogViewportPosition();
    }
  }

  // Fancybox добавляет класс html.with-fancybox, пока открыт любой инстанс
  function isFancyboxOpen() {
    return document.documentElement.classList.contains('with-fancybox');
  }

  // Флаг "Fancybox только что закрылась" (защита от провала клика)
  function isFancyboxClosing() {
    return document.documentElement.dataset.zpmFbClosing === '1';
  }

  // ---- Scroll lock (no jitter, scrollbar-gutter: stable) ----
  let scrollY = 0;

  function lockScroll() {
    if (document.body.classList.contains('is-scroll-locked')) return;
    scrollY = window.scrollY || document.documentElement.scrollTop || 0;
    document.body.style.top = -scrollY + 'px';
    document.body.classList.add('is-scroll-locked');
  }

  function unlockScroll() {
    if (!document.body.classList.contains('is-scroll-locked')) return;
    document.body.classList.remove('is-scroll-locked');

    const top = document.body.style.top;
    document.body.style.top = '';

    const y = top ? Math.abs(parseInt(top, 10)) : scrollY;
    window.scrollTo(0, y);
  }

  // ---- Focus trap (только) ----
  const FOCUSABLE =
    'a[href], area[href], input:not([disabled]):not([type="hidden"]), select:not([disabled]), textarea:not([disabled]), button:not([disabled]), iframe, object, embed, [contenteditable], [tabindex]:not([tabindex="-1"])';

  function createFocusTrap(rootEl) {
    let active = false;
    let lastActiveEl = null;

    function getFocusable() {
      return Array.from(rootEl.querySelectorAll(FOCUSABLE)).filter((el) => {
        return !!(el.offsetWidth || el.offsetHeight || el.getClientRects().length);
      });
    }

    function onKeyDown(e) {
      if (!active) return;
      if (e.key !== 'Tab') return;

      const items = getFocusable();
      if (!items.length) {
        e.preventDefault();
        rootEl.focus();
        return;
      }

      const first = items[0];
      const last = items[items.length - 1];

      if (!rootEl.contains(document.activeElement)) {
        e.preventDefault();
        first.focus();
        return;
      }

      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    }

    return {
      activate(focusEl) {
        if (active) return;
        active = true;
        lastActiveEl = document.activeElement;

        setTimeout(() => {
          if (focusEl && typeof focusEl.focus === 'function') {
            focusEl.focus();
            return;
          }
          const items = getFocusable();
          if (items.length) items[0].focus();
          else {
            rootEl.setAttribute('tabindex', '-1');
            rootEl.focus();
          }
        }, 0);

        document.addEventListener('keydown', onKeyDown);
      },
      deactivate(returnFocusEl) {
        if (!active) return;
        active = false;
        document.removeEventListener('keydown', onKeyDown);

        const target = returnFocusEl || lastActiveEl;
        if (target && typeof target.focus === 'function') {
          setTimeout(() => target.focus(), 0);
        }
      },
    };
  }

  /* ================================
     Overlay mode controls (body classes)
  ================================ */
  function overlayOn(theme) {
    document.body.classList.add('has-overlay');
    document.body.classList.remove('overlay--light', 'overlay--dark');
    document.body.classList.add(theme === 'dark' ? 'overlay--dark' : 'overlay--light');

    if (overlay) overlay.setAttribute('aria-hidden', 'false');
    lockScroll();
  }

  function overlayOff() {
    document.body.classList.remove('has-overlay', 'overlay--light', 'overlay--dark');
    if (overlay) overlay.setAttribute('aria-hidden', 'true');
    unlockScroll();
  }

  /* ================================
     Popup registry + single active popup
  ================================ */
  const registry = new Map(); // name -> popup
  let activeName = null;
  let closeTimer = null;

  function setBodyPopupClass(name, on) {
    const cls = 'popup-' + name + '-open';
    document.body.classList.toggle(cls, !!on);
  }

  function setHtmlClass(htmlClass, on) {
    document.documentElement.classList.toggle(htmlClass, !!on);
  }

  function forceReflow(el) {
    // eslint-disable-next-line no-unused-expressions
    el.offsetHeight;
    // eslint-disable-next-line no-unused-expressions
    getComputedStyle(el).opacity;
  }

  function closeActive({ keepOverlay } = { keepOverlay: false }) {
    if (!activeName) return;

    const p = registry.get(activeName);
    if (!p) {
      activeName = null;
      if (!keepOverlay) overlayOff();
      return;
    }

    // ВАЖНО: подавляем focusin-открытие после возврата фокуса
    p.suppressFocusin = true;

    // снять классы состояния
    setHtmlClass(p.htmlClass, false);
    setBodyPopupClass(p.name, false);

    // aria
    if (p.isAriaDialog && p.layer) p.layer.setAttribute('aria-hidden', 'true');

    // focus trap (вернёт фокус на trigger)
    if (p.focusTrap) p.focusTrap.deactivate(p.trigger);

    // hidden после анимации
    if (closeTimer) clearTimeout(closeTimer);
closeTimer = setTimeout(() => {
  if (p.layer && p.useHidden) p.layer.hidden = true;
  closeTimer = null;
}, ANIM_MS);

    activeName = null;

    // overlay
    if (!keepOverlay) overlayOff();
  }

  function openPopup(name) {
    const p = registry.get(name);
    if (!p) return;

    // если уже открыт этот же попап — toggle (закрыть)
    if (activeName === name) {
      closeActive({ keepOverlay: false });
      return;
    }

    // Переключение: закрыть активный, но overlay оставить
    if (activeName && activeName !== name) {
      closeActive({ keepOverlay: true });
    }

    // включить overlay с нужной темой
    overlayOn(p.overlayTheme);

// показать слой (не всем попапам можно hidden, напр. фильтры)
if (p.useHidden) p.layer.hidden = false;

    // обеспечить анимацию открытия из hidden
    forceReflow(p.layer);
    requestAnimationFrame(() => {
      requestAnimationFrame(() => {
        setHtmlClass(p.htmlClass, true);
        setBodyPopupClass(p.name, true);

        if (p.isAriaDialog) p.layer.setAttribute('aria-hidden', 'false');

        if (p.focusTrap) p.focusTrap.activate(p.focusOnOpenEl);

        activeName = name;
      });
    });
  }

  function registerPopup(cfg) {
const {
  name,
  trigger,
  extraTriggers,
  layer,
  layerRootForFocus,
  htmlClass,
  isAriaDialog,
  overlayTheme,
  focusOnOpenEl,
  closeSelectors,
  triggerMode = 'toggle',
  allowOutsideClose = true,
} = cfg;

const triggers = [trigger]
  .concat(Array.isArray(extraTriggers) ? extraTriggers : [])
  .filter(Boolean);

    if (!trigger || !layer) return;

    const focusTrap = createFocusTrap(layerRootForFocus || layer);

const popup = {
  name,
  trigger,
  triggers,
  layer,
  htmlClass,
  isAriaDialog: !!isAriaDialog,
  overlayTheme: overlayTheme === 'dark' ? 'dark' : 'light',
  focusOnOpenEl: focusOnOpenEl || null,
  focusTrap,
  suppressFocusin: false,
  useHidden: cfg.useHidden !== false, // по умолчанию true, но для фильтров будет false
};

    registry.set(name, popup);

// close buttons inside (ВАЖНО: глушим сторонние обработчики, чтобы не было мгновенного hidden)
if (closeSelectors) {
  layer.querySelectorAll(closeSelectors).forEach((b) => {
    b.addEventListener(
      'click',
      (e) => {
        e.preventDefault();
        e.stopPropagation();
        if (typeof e.stopImmediatePropagation === 'function') {
          e.stopImmediatePropagation();
        }

        if (activeName === name) closeActive({ keepOverlay: false });
      },
      true
    );
  });
}
// trigger click
triggers.forEach((tr) => {
  tr.addEventListener('click', (e) => {
    e.preventDefault();
    e.stopPropagation();

    if (triggerMode === 'open') {
      if (activeName !== name) openPopup(name);
      return;
    }

    openPopup(name);
  });

  // trigger focusin (для формы поиска)
  tr.addEventListener('focusin', () => {
    const p = registry.get(name);
    if (!p) return;

    if (p.suppressFocusin) {
      p.suppressFocusin = false;
      return;
    }

    if (triggerMode === 'open' && activeName !== name) openPopup(name);
  });
});

    // outside click close
    if (allowOutsideClose) {
      const interactiveRoot = layerRootForFocus || layer;

      // 1. Клик по самому layer вне panel/root => закрыть
      layer.addEventListener(
        'pointerdown',
        (e) => {
          if (isFancyboxOpen() || isFancyboxClosing()) return;
          if (activeName !== name) return;

          const t = e.target;
if (interactiveRoot && interactiveRoot.contains(t)) return;

const clickedOnOwnTrigger = triggers.some((tr) => tr && tr.contains(t));
if (clickedOnOwnTrigger) return;
          e.preventDefault();
          e.stopPropagation();
          closeActive({ keepOverlay: false });
        },
        true
      );

      // 2. Клик вообще вне layer
      document.addEventListener(
        'pointerdown',
        (e) => {
          if (isFancyboxOpen() || isFancyboxClosing()) return;
          if (activeName !== name) return;

          const t = e.target;
const clickedOnOwnTrigger = triggers.some((tr) => tr && tr.contains(t));
if (layer.contains(t) || clickedOnOwnTrigger) return;

const clickedAnotherTrigger = Array.from(registry.values()).some((pp) => {
  if (pp.name === name) return false;

  const ppTriggers = Array.isArray(pp.triggers)
    ? pp.triggers
    : (pp.trigger ? [pp.trigger] : []);

  return ppTriggers.some((tr) => tr && tr.contains(t));
});
          if (clickedAnotherTrigger) {
            closeActive({ keepOverlay: true });
          } else {
            closeActive({ keepOverlay: false });
          }
        },
        true
      );
    }
  }

  /* ================================
     Global close: overlay click + ESC
  ================================ */
  if (overlay) {
    overlay.addEventListener('pointerdown', (e) => {
      // FIX: если открыт/закрывается Fancybox — клики по нашему overlay игнорируем
      if (isFancyboxOpen() || isFancyboxClosing()) return;

      if (!activeName) return;
      e.preventDefault();
      closeActive({ keepOverlay: false });
    });
  }

  document.addEventListener('keydown', (e) => {
    // FIX: если открыт/закрывается Fancybox — ESC должен закрывать Fancybox, а не наш попап
    if (isFancyboxOpen() || isFancyboxClosing()) return;

    if (e.key !== 'Escape') return;
    if (!activeName) return;
    closeActive({ keepOverlay: false });
  });

  /* ================================
     PUBLIC API (для Fancybox режимов 1/3)
     closeAll(): закрыть ВСЁ ZPM (попапы + overlay + scroll-lock) без "залипаний" классов
  ================================ */
  function hardResetAll() {
    // 1) снять html/body классы состояний всех зарегистрированных попапов
    registry.forEach((p) => {
      if (p && p.htmlClass) setHtmlClass(p.htmlClass, false);
      if (p && p.name) setBodyPopupClass(p.name, false);

      // aria + hidden (без анимации)
      if (p && p.layer) {
        p.layer.setAttribute('aria-hidden', 'true');
        p.layer.hidden = true;
      }

      // focus trap (на всякий случай)
      if (p && p.focusTrap) p.focusTrap.deactivate(p.trigger);
    });

    activeName = null;

    // 2) на случай внешних/старых классов
    document.documentElement.classList.remove('is-menu-open');

    // 3) overlay + scroll-lock
    overlayOff();
  }

  function closeAll() {
    // Если что-то открыто — сначала штатно закрываем (с анимацией),
    // затем делаем hard reset, чтобы не оставалось "хвостов" классов.
    if (activeName) {
      closeActive({ keepOverlay: false });
      setTimeout(hardResetAll, ANIM_MS + 20);
      return;
    }
    hardResetAll();
  }

  window.ZpmPopupManager = {
    closeAll,
    hardResetAll,
    getActiveName: () => activeName,
  };

  /* ================================
     REGISTER POPUPS: catalog + search desktop + search mobile
  ================================ */

  // 1) Catalog
  const catalogBtn = document.querySelector('[data-catalog-open]');
  const catalogLayer = document.querySelector('[data-catalog]');
  const catalogPanel = catalogLayer ? catalogLayer.querySelector('.zpm-catalog__panel') : null;

  registerPopup({
    name: 'catalog',
    trigger: catalogBtn,
    layer: catalogLayer,
    layerRootForFocus: catalogPanel || catalogLayer,
    htmlClass: 'is-catalog-open',
    isAriaDialog: true,
    overlayTheme: 'light',
    focusOnOpenEl: catalogLayer ? catalogLayer.querySelector('[data-cat-btn].is-active') : null,
    closeSelectors: '[data-catalog-close]',
    triggerMode: 'toggle',
    allowOutsideClose: true,
  });

  if (catalogBtn) {
    catalogBtn.addEventListener(
      'click',
      function () {
        requestAnimationFrame(function () {
          requestAnimationFrame(function () {
            applyCatalogViewportPosition();
          });
        });
      },
      true
    );
  }

  window.addEventListener('resize', syncActivePopupViewportPosition);
  window.addEventListener('scroll', syncActivePopupViewportPosition, true);

  // 2) Desktop quick search
  const qForm = document.querySelector('[data-qsearch-trigger]');
  const qLayer = document.querySelector('[data-qsearch]');
  const qPanel = qLayer ? qLayer.querySelector('.zpm-qsearch__panel') : null;
  const qInput = document.querySelector('[data-qsearch-input-desktop]');
  const qHint = qLayer ? qLayer.querySelector('[data-qsearch-hint]') : null;
  const qList = qLayer ? qLayer.querySelector('[data-qsearch-list]') : null;
  const qCount = qLayer ? qLayer.querySelector('[data-qsearch-count]') : null;

  if (qInput && qHint && qList) {
    qInput.addEventListener('input', () => {
      const val = (qInput.value || '').trim();
      const hasText = val.length > 0;

      qHint.hidden = hasText;
      qList.hidden = !hasText;
      if (qCount) qCount.textContent = hasText ? '20' : '0';
    });
  }

  registerPopup({
    name: 'qsearch',
    trigger: qForm,
    layer: qLayer,
    layerRootForFocus: qPanel || qLayer,
    htmlClass: 'is-qsearch-open',
    isAriaDialog: true,
    overlayTheme: 'light',
    focusOnOpenEl: qInput,
    closeSelectors: '[data-qsearch-close]',
    triggerMode: 'open',
    allowOutsideClose: true,
  });





// 3) Mobile search panel// 3) Mobile search panel
const mOpenBtns = Array.from(document.querySelectorAll('[data-mobile-search-open]'));
const mPanelWrap = document.querySelector('[data-mobile-search-panel]');
const mRoot = mPanelWrap ? mPanelWrap.querySelector('.zpm-qsearch-mobile__panel') : null;
const mInput = mPanelWrap ? mPanelWrap.querySelector('[data-qsearch-input-mobile]') : null;
const mReset = mPanelWrap ? mPanelWrap.querySelector('[data-qsearch-reset-mobile]') : null;

if (mReset && mInput) {
  mReset.addEventListener('click', function (e) {
    e.preventDefault();
    e.stopPropagation();

    mInput.value = '';
    mInput.dispatchEvent(new Event('input', { bubbles: true }));
    mInput.focus();
  });
}

if (mOpenBtns.length && mPanelWrap) {
  registerPopup({
    name: 'qsearch-mobile',
    trigger: mOpenBtns[0],
    extraTriggers: mOpenBtns.slice(1),
    layer: mPanelWrap,
    layerRootForFocus: mRoot || mPanelWrap,
    htmlClass: 'is-qsearch-mobile-open',
    isAriaDialog: true,
    overlayTheme: 'light',
    focusOnOpenEl: mInput,
    closeSelectors: '[data-qsearch-mobile-close]',
    triggerMode: 'toggle',
    allowOutsideClose: true,
  });

  (function () {
    function syncExpanded() {
      const isOpen = document.documentElement.classList.contains('is-qsearch-mobile-open');

      mOpenBtns.forEach(function (btn) {
        btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      });

      mPanelWrap.setAttribute('aria-hidden', isOpen ? 'false' : 'true');
    }

    syncExpanded();

    const mo = new MutationObserver(function (muts) {
      for (let i = 0; i < muts.length; i++) {
        if (muts[i].attributeName === 'class') {
          syncExpanded();
          break;
        }
      }
    });

    mo.observe(document.documentElement, {
      attributes: true,
      attributeFilter: ['class'],
    });
  })();
}






/* ================================
   4) Mobile offcanvas menu (popup manager)
================================ */

const mMenuBtn = document.querySelector('[data-menu-open]');
const mMenuLayer = document.querySelector('[data-mobile-menu]');
const mMenuPanel = mMenuLayer ? mMenuLayer.querySelector('.zpm-mmenu__panel') : null;

// Регистрация как обычного попапа: наш светлый overlay + scroll-lock
registerPopup({
  name: 'mmenu',
  trigger: mMenuBtn,
  layer: mMenuLayer,
  layerRootForFocus: mMenuPanel || mMenuLayer,
  htmlClass: 'is-mmenu-open',
  isAriaDialog: true,
  overlayTheme: 'light',
  focusOnOpenEl: mMenuLayer ? mMenuLayer.querySelector('[data-menu-close]') : null,
  closeSelectors: '[data-menu-close]',
  triggerMode: 'toggle',
  allowOutsideClose: false, // закрытие по: наш overlay / кнопки data-menu-close
});

// Синхронизация aria-expanded на кнопке открытия меню (аккуратно, без вмешательства в ядро)
(function () {
  if (!mMenuBtn || !mMenuLayer) return;

  function setExpanded(isOpen) {
    mMenuBtn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    mMenuLayer.setAttribute('aria-hidden', isOpen ? 'false' : 'true');
  }

  // начальное
  setExpanded(false);

  // По клику на триггер (capture), заранее ставим флаг "попытка открыть"
  // Финальное состояние выставим по классу html (после rAF в openPopup)
  mMenuBtn.addEventListener(
    'click',
    () => {
      requestAnimationFrame(() => {
        const isOpen = document.documentElement.classList.contains('is-mmenu-open');
        setExpanded(isOpen);
      });
    },
    true
  );

  // По клику на любые закрывающие элементы
  mMenuLayer.querySelectorAll('[data-menu-close]').forEach((el) => {
    el.addEventListener(
      'click',
      () => {
        requestAnimationFrame(() => setExpanded(false));
      },
      true
    );
  });

  // По ESC через общий обработчик Popup Manager — тоже обновится на следующем кадре
  document.addEventListener(
    'keydown',
    (e) => {
      if (e.key !== 'Escape') return;
      requestAnimationFrame(() => {
        const isOpen = document.documentElement.classList.contains('is-mmenu-open');
        setExpanded(isOpen);
      });
    },
    true
  );
})();






/* ==========================================================
   GLOBAL PAGE PRELOADER
   - show only first time per day
   - starts from first frame via inline script in <head>
   - waits real page load
   - uses smooth fake progress
   - no flash after shown today
========================================================== */
(function () {
  const STORAGE_KEY = 'zpmPreloaderShownDate';
  const TODAY = new Date().toISOString().slice(0, 10);

  const MIN_SHOW_MS = 500; // для демо 5000; стандарт 500
  const HIDE_DELAY_MS = 180;
  const RESET_DELAY_MS = 360; // после fade-out, чтобы не мигал 0%

  const root = document.documentElement;
  const preloadEl = document.querySelector('[data-preloader]');
  const percentEl = document.querySelector('[data-preloader-percent]');
  const lineEl = document.querySelector('[data-preloader-line]');

  if (!preloadEl || !percentEl || !lineEl) return;

  let progress = 0;
  let timer = null;
  let startedAt = 0;

  const alreadyShownToday = (function () {
    try {
      return localStorage.getItem(STORAGE_KEY) === TODAY;
    } catch (e) {
      return false;
    }
  })();

  const shouldShow = root.classList.contains('is-preloader-active') && !alreadyShownToday;

  function renderProgress(value) {
    const v = Math.max(0, Math.min(100, value));
    progress = v;
    percentEl.textContent = Math.round(v) + '%';
    lineEl.style.width = v + '%';
  }

  function resetPreloaderSilently() {
    progress = 0;
    percentEl.textContent = '0%';
    lineEl.style.width = '0%';
  }

  function startFakeProgress() {
    clearInterval(timer);

    timer = setInterval(() => {
      if (progress < 18) {
        renderProgress(progress + 2);
      } else if (progress < 40) {
        renderProgress(progress + 1.5);
      } else if (progress < 65) {
        renderProgress(progress + 1);
      } else if (progress < 82) {
        renderProgress(progress + 0.6);
      } else if (progress < 92) {
        renderProgress(progress + 0.25);
      } else {
        clearInterval(timer);
      }
    }, 110);
  }

  function hideImmediately() {
    clearInterval(timer);
    root.classList.remove('is-preloader-active');
    preloadEl.setAttribute('aria-hidden', 'true');
    resetPreloaderSilently();
  }

  function finishPreloader() {
    clearInterval(timer);
    renderProgress(100);

    const elapsed = Date.now() - startedAt;
    const waitMore = Math.max(0, MIN_SHOW_MS - elapsed);

    setTimeout(() => {
      // запускаем fade-out
      root.classList.remove('is-preloader-active');
      preloadEl.setAttribute('aria-hidden', 'true');

      // сброс только после завершения transition
      setTimeout(() => {
        resetPreloaderSilently();
      }, HIDE_DELAY_MS + RESET_DELAY_MS);
    }, waitMore);
  }

  // Если уже показывали сегодня — сразу скрываем и выходим
  if (!shouldShow) {
    hideImmediately();
    return;
  }

  // Первый показ сегодня
  startedAt = Date.now();
  preloadEl.setAttribute('aria-hidden', 'false');
  renderProgress(0);

  // Старт fake progress не в тот же тик, чтобы убрать редкие микро-рывки
  requestAnimationFrame(() => {
    requestAnimationFrame(() => {
      startFakeProgress();
    });
  });

  window.addEventListener('load', function () {
    try {
      localStorage.setItem(STORAGE_KEY, TODAY);
    } catch (e) {}
    finishPreloader();
  });

  // Если страница пришла из BFCache
  window.addEventListener('pageshow', function (e) {
    if (e.persisted) {
      hideImmediately();
    }
  });
})();



























// В самом конце или начале файла, ВНЕ (function(){})
window.forceResetSearch = function(e) {
    if (e) {
        e.preventDefault();
        e.stopPropagation();
    }
    
    // Находим инпуты вручную, так как мы вне области видимости переменных скрипта
    const desktopInput = document.querySelector('[data-qsearch-input-desktop]');
    const mobileInput = document.querySelector('[data-qsearch-input-mobile]');
    
    if (desktopInput) desktopInput.value = '';
    if (mobileInput) mobileInput.value = '';
    
    // Инициируем поиск пустой строки, чтобы скрипт сам перешел в setStateIdle
    if (desktopInput) {
        desktopInput.dispatchEvent(new Event('input'));
    }
    
    console.log('Поиск очищен через глобальную функцию');
};



/* ================================
   QUICK SEARCH (desktop + mobile)
================================ */

(function () {
  const MIN_QUERY = 3;
  const DEBOUNCE_MS = 250;
  const MAX_VISIBLE_PRODUCTS = 10;

  const triggers = Array.from(document.querySelectorAll('[data-qsearch-trigger]'));
  const desktopLayer = document.querySelector('[data-qsearch]');
  const desktopInput = document.querySelector('[data-qsearch-input-desktop]');

  const mobileLayer = document.querySelector('[data-mobile-search-panel]');
  const mobileInput = document.querySelector('[data-qsearch-input-mobile]');

  if (!triggers.length || !desktopLayer || !desktopInput) return;

  const desktopPanel = desktopLayer.querySelector('.zpm-qsearch__panel');
  const desktopHint = desktopLayer.querySelector('[data-qsearch-hint]');
  const desktopHead = desktopLayer.querySelector('.zpm-popup_manager__head');
  const desktopHelpNav = desktopLayer.querySelector('.zpm-qsearch__help-nav');
  const desktopListWrapper = desktopLayer.querySelector('.zpm-qsearch__list-wrapper');
  const desktopCategoryList = desktopLayer.querySelector('.zpm-qsearch__list.category[data-qsearch-list]');
  const desktopProductList = desktopLayer.querySelector('.zpm-qsearch__list.products[data-qsearch-list]');
  const desktopShowAllBtn = desktopProductList ? desktopProductList.querySelector('.zpm-qsearch__go-search_page') : null;

  const desktopCategoryTitle = desktopCategoryList ? desktopCategoryList.querySelector('.zpm-qsearch__list-title') : null;
  const desktopProductTitle = desktopProductList ? desktopProductList.querySelector('.zpm-qsearch__list-title') : null;

  const closeBtnHtml = desktopHead && desktopHead.querySelector('[data-qsearch-close]')
    ? desktopHead.querySelector('[data-qsearch-close]').outerHTML
    : '';

  const mobileHint = mobileLayer ? mobileLayer.querySelector('[data-qsearch-hint-mobile]') : null;
  const mobileMeta = mobileLayer ? mobileLayer.querySelector('[data-qsearch-meta-mobile]') : null;
  const mobileCount = mobileLayer ? mobileLayer.querySelector('[data-qsearch-count-mobile]') : null;
  const mobileResults = mobileLayer ? mobileLayer.querySelector('[data-qsearch-results-mobile]') : null;
  const mobileCategoryList = mobileLayer ? mobileLayer.querySelector('[data-qsearch-list-mobile="category"]') : null;
  const mobileProductList = mobileLayer ? mobileLayer.querySelector('[data-qsearch-list-mobile="products"]') : null;
  const mobileShowAllBtn = mobileLayer ? mobileLayer.querySelector('.zpm-qsearch-mobile__go-search-page') : null;
  const mobileResetBtn = mobileLayer ? mobileLayer.querySelector('[data-qsearch-reset-mobile]') : null;

  if (!desktopPanel || !desktopHint || !desktopHead || !desktopHelpNav || !desktopListWrapper || !desktopCategoryList || !desktopProductList || !desktopCategoryTitle || !desktopProductTitle) {
    return;
  }

  let lastTrigger = triggers[0];
  let searchTimer = null;
  let requestId = 0;

  function isMobile() {
    return window.matchMedia('(max-width: 1024px)').matches;
  }

  function isDesktopLayerOpen() {
    if (desktopLayer.hasAttribute('hidden')) return false;
    return desktopLayer.getAttribute('aria-hidden') !== 'true';
  }

  function isMobileSearchPanelOpen() {
    return !!(mobileLayer && document.documentElement.classList.contains('is-qsearch-mobile-open'));
  }

  function placeQSearchByTrigger(btn) {
    if (!btn || isMobile()) return;

    const rect = btn.getBoundingClientRect();
    const top = Math.round(rect.bottom + 0);
    const left = Math.round(rect.left);

    desktopLayer.style.setProperty('--qs-top', top + 'px');
    desktopLayer.style.setProperty('--qs-left', left + 'px');
  }

  function escapeHtml(str) {
    return String(str)
      .replaceAll('&', '&amp;')
      .replaceAll('<', '&lt;')
      .replaceAll('>', '&gt;')
      .replaceAll('"', '&quot;')
      .replaceAll("'", '&#039;');
  }

  function setDesktopHeadText(text, icon) {
    desktopHead.innerHTML =
      '<div class="zpm-help_ico">' + escapeHtml(icon || '!') + '</div>' +
      escapeHtml(text) +
      closeBtnHtml;
  }

  function clearDesktopList(listEl) {
    Array.from(listEl.children).forEach(function (child) {
      const isTitle = child.classList && child.classList.contains('zpm-qsearch__list-title');
      const isShowAll = child.classList && child.classList.contains('zpm-qsearch__go-search_page');

      if (!isTitle && !isShowAll) {
        child.remove();
      }
    });
  }

  function clearMobileList(listEl) {
    if (!listEl) return;
    listEl.querySelectorAll('.zpm-qsearch-mobile__item').forEach(function (el) {
      el.remove();
    });
  }

  function renderDesktopCategories(items) {
    clearDesktopList(desktopCategoryList);

    if (!items.length) {
      desktopCategoryList.hidden = true;
      return;
    }

    desktopCategoryList.hidden = false;

    const fragment = document.createDocumentFragment();

    items.forEach(function (item) {
      const a = document.createElement('a');
      a.className = 'zpm-qsearch__item';
      a.href = item.href || '#';

      a.innerHTML =
        '<span class="zpm-qsearch__icon"><svg class="zpm-icon" aria-hidden="true" focusable="false"><use href="#zpm_ico__btn_next"></use></svg></span>' +
        '<span class="zpm-qsearch__meta">' +
          '<span class="zpm-qsearch__title">' + escapeHtml(item.title) + '</span>' +
          '<span class="zpm-qsearch__label">' + escapeHtml(item.label || '') + '</span>' +
        '</span>';

      fragment.appendChild(a);
    });

    desktopCategoryTitle.insertAdjacentElement('afterend', document.createElement('div'));
    desktopCategoryTitle.nextElementSibling.replaceWith(fragment);
  }

  function renderDesktopProducts(items, query) {
    clearDesktopList(desktopProductList);

    if (desktopShowAllBtn) {
      desktopShowAllBtn.href = '/search/?search=' + encodeURIComponent(query);
      desktopShowAllBtn.hidden = !items.length;
      desktopShowAllBtn.style.display = items.length > MAX_VISIBLE_PRODUCTS ? '' : 'none';
    }

    if (!items.length) {
      desktopProductList.hidden = true;
      if (desktopShowAllBtn) desktopShowAllBtn.hidden = true;
      return;
    }

    desktopProductList.hidden = false;

    const fragment = document.createDocumentFragment();

    items.slice(0, 30).forEach(function (item, index) {
      const count = String(index + 1).padStart(2, '0');

      const a = document.createElement('a');
      a.className = 'zpm-qsearch__item';
      a.href = item.href || '#';

      a.innerHTML =
        '<span class="zpm-qsearch__count">' + count + '</span>' +
        '<span class="zpm-qsearch__meta">' +
          '<span class="zpm-qsearch__title">' + escapeHtml(item.title) + '</span>' +
          '<span class="zpm-qsearch__label">' + escapeHtml(item.label || '') + '</span>' +
        '</span>';

      fragment.appendChild(a);
    });

    desktopProductTitle.insertAdjacentElement('afterend', document.createElement('div'));
    desktopProductTitle.nextElementSibling.replaceWith(fragment);
  }

  function renderMobileCategories(items) {
    if (!mobileCategoryList) return;

    clearMobileList(mobileCategoryList);

    if (!items.length) {
      mobileCategoryList.hidden = true;
      return;
    }

    mobileCategoryList.hidden = false;

    const fragment = document.createDocumentFragment();

    items.forEach(function (item) {
      const a = document.createElement('a');
      a.className = 'zpm-qsearch-mobile__item';
      a.href = item.href || '#';

      a.innerHTML =
        '<span class="zpm-qsearch-mobile__meta">' +
          '<span class="zpm-qsearch-mobile__title">' + escapeHtml(item.title) + '</span>' +
          '<span class="zpm-qsearch-mobile__label">' + escapeHtml(item.label || '') + '</span>' +
        '</span>';

      fragment.appendChild(a);
    });

    mobileCategoryList.appendChild(fragment);
  }

  function renderMobileProducts(items, query) {
    if (!mobileProductList) return;

    clearMobileList(mobileProductList);

    if (mobileShowAllBtn) {
      mobileShowAllBtn.href = '/search/?search=' + encodeURIComponent(query);
      mobileShowAllBtn.hidden = !items.length;
    }

    if (!items.length) {
      mobileProductList.hidden = true;
      if (mobileShowAllBtn) mobileShowAllBtn.hidden = true;
      return;
    }

    mobileProductList.hidden = false;

    const fragment = document.createDocumentFragment();

    items.slice(0, 30).forEach(function (item, index) {
      const a = document.createElement('a');
      a.className = 'zpm-qsearch-mobile__item';
      a.href = item.href || '#';

      a.innerHTML =
        '<span class="zpm-qsearch-mobile__count">' + String(index + 1).padStart(2, '0') + '</span>' +
        '<span class="zpm-qsearch-mobile__meta">' +
          '<span class="zpm-qsearch-mobile__title">' + escapeHtml(item.title) + '</span>' +
          '<span class="zpm-qsearch-mobile__label">' + escapeHtml(item.label || '') + '</span>' +
        '</span>';

      fragment.appendChild(a);
    });

    mobileProductList.appendChild(fragment);
  }

  function setStateIdle() {
    clearDesktopList(desktopCategoryList);
    clearDesktopList(desktopProductList);
    clearMobileList(mobileCategoryList);
    clearMobileList(mobileProductList);

    desktopHint.hidden = false;
    desktopHead.hidden = true;
    desktopHelpNav.hidden = true;
    desktopListWrapper.hidden = true;
    desktopCategoryList.hidden = true;
    desktopProductList.hidden = true;

    if (desktopShowAllBtn) {
      desktopShowAllBtn.hidden = true;
      desktopShowAllBtn.style.display = 'none';
    }

    if (mobileHint) mobileHint.hidden = false;
    if (mobileMeta) mobileMeta.hidden = true;
    if (mobileResults) mobileResults.hidden = true;
    if (mobileCategoryList) mobileCategoryList.hidden = true;
    if (mobileProductList) mobileProductList.hidden = true;
    if (mobileShowAllBtn) mobileShowAllBtn.hidden = true;
    if (mobileResetBtn) mobileResetBtn.hidden = true;
    if (mobileCount) mobileCount.textContent = '0';
  }

  function setStateSearching() {
    desktopHint.hidden = true;
    desktopHead.hidden = false;
    desktopHelpNav.hidden = true;
    desktopListWrapper.hidden = true;
    desktopCategoryList.hidden = true;
    desktopProductList.hidden = true;

    if (desktopShowAllBtn) {
      desktopShowAllBtn.hidden = true;
      desktopShowAllBtn.style.display = 'none';
    }

    setDesktopHeadText('Идёт поиск...', '!');

    if (mobileHint) mobileHint.hidden = true;
    if (mobileMeta) mobileMeta.hidden = true;
    if (mobileResults) mobileResults.hidden = true;
    if (mobileCategoryList) mobileCategoryList.hidden = true;
    if (mobileProductList) mobileProductList.hidden = true;
    if (mobileShowAllBtn) mobileShowAllBtn.hidden = true;
    if (mobileResetBtn) mobileResetBtn.hidden = false;
  }

  function setStateEmpty() {
    clearDesktopList(desktopCategoryList);
    clearDesktopList(desktopProductList);
    clearMobileList(mobileCategoryList);
    clearMobileList(mobileProductList);

    desktopHint.hidden = true;
    desktopHead.hidden = false;
    desktopHelpNav.hidden = false;
    desktopListWrapper.hidden = true;
    desktopCategoryList.hidden = true;
    desktopProductList.hidden = true;

    if (desktopShowAllBtn) {
      desktopShowAllBtn.hidden = true;
      desktopShowAllBtn.style.display = 'none';
    }

    setDesktopHeadText('Не найдено, попробуйте ещё', '!');

    if (mobileHint) mobileHint.hidden = true;
    if (mobileMeta) mobileMeta.hidden = false;
    if (mobileResults) mobileResults.hidden = false;
    if (mobileCategoryList) mobileCategoryList.hidden = true;
    if (mobileProductList) mobileProductList.hidden = true;
    if (mobileShowAllBtn) mobileShowAllBtn.hidden = true;
    if (mobileResetBtn) mobileResetBtn.hidden = false;
    if (mobileCount) mobileCount.textContent = '0';
  }

  function setStateFound(categories, products, query) {
    const total = (categories ? categories.length : 0) + (products ? products.length : 0);

    desktopHint.hidden = true;
    desktopHead.hidden = false;
    desktopHelpNav.hidden = false;
    desktopListWrapper.hidden = false;

    setDesktopHeadText('Результаты поиска', '!');

    renderDesktopCategories(categories || []);
    renderDesktopProducts(products || [], query);

    if (!categories.length) desktopCategoryList.hidden = true;
    if (!products.length) desktopProductList.hidden = true;

    if (mobileHint) mobileHint.hidden = true;
    if (mobileMeta) mobileMeta.hidden = false;
    if (mobileResults) mobileResults.hidden = false;
    if (mobileResetBtn) mobileResetBtn.hidden = false;
    if (mobileCount) mobileCount.textContent = String(total);

    renderMobileCategories(categories || []);
    renderMobileProducts(products || [], query);

    if (mobileCategoryList && !categories.length) mobileCategoryList.hidden = true;
    if (mobileProductList && !products.length) mobileProductList.hidden = true;
  }

  function runSearch(query) {
    const q = query.trim();

    return fetch('/search/?ajax=1&search=' + encodeURIComponent(q), {
      method: 'GET',
      headers: {
        'X-Requested-With': 'XMLHttpRequest'
      },
      credentials: 'same-origin'
    })
      .then(function (response) {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .catch(function (error) {
        console.error('Search AJAX error:', error);
        return { categories: [], products: [] };
      });
  }

  function performSearch(rawValue) {
    const query = (rawValue || '').trim();
    const currentRequest = ++requestId;

    clearTimeout(searchTimer);

    if (!query || query.length < MIN_QUERY) {
      setStateIdle();
      return;
    }

    setStateSearching();

    searchTimer = setTimeout(function () {
      runSearch(query).then(function (result) {
        if (currentRequest !== requestId) return;

        const categories = Array.isArray(result.categories) ? result.categories : [];
        const products = Array.isArray(result.products) ? result.products : [];

        if (!categories.length && !products.length) {
          setStateEmpty();
          return;
        }

        setStateFound(categories, products, query);
      });
    }, DEBOUNCE_MS);
  }

  function resetSearch() {
    requestId++;
    clearTimeout(searchTimer);

    desktopInput.value = '';
    if (mobileInput) mobileInput.value = '';

    setStateIdle();
  }

  triggers.forEach(function (btn) {
    btn.addEventListener('click', function () {
      lastTrigger = btn;
      placeQSearchByTrigger(btn);
      requestAnimationFrame(function () {
        placeQSearchByTrigger(btn);
      });
    });
  });

  desktopInput.addEventListener('focus', function () {
    performSearch(desktopInput.value);
    placeQSearchByTrigger(lastTrigger);
  });

  desktopInput.addEventListener('input', function () {
    performSearch(desktopInput.value);
    placeQSearchByTrigger(lastTrigger);
  });

  if (mobileInput) {
    mobileInput.addEventListener('focus', function () {
      performSearch(mobileInput.value);
    });

    mobileInput.addEventListener('input', function () {
      performSearch(mobileInput.value);
    });
  }

  triggers.forEach(function (form) {
    form.addEventListener('submit', function (e) {
      const query = (desktopInput.value || '').trim();

      if (query.length < MIN_QUERY) {
        e.preventDefault();
        performSearch(query);
      }
    });
  });

  document.addEventListener('click', function (e) {
    const resetLink = e.target.closest('.zpm-qsearch__reset-link');
    if (!resetLink) return;

    e.preventDefault();
    e.stopPropagation();
    resetSearch();
  }, true);

  document.addEventListener('click', function (e) {
    const closeBtn = e.target.closest('[data-qsearch-close], [data-qsearch-mobile-close]');
    if (!closeBtn) return;

    requestId++;
    clearTimeout(searchTimer);

    if (window.ZpmPopupManager && typeof window.ZpmPopupManager.closeAll === 'function') {
      window.ZpmPopupManager.closeAll();
    }

    setTimeout(function () {
      resetSearch();
    }, 0);
  });

  function onViewportChange() {
    if (isMobileSearchPanelOpen()) return;
    if (!isDesktopLayerOpen()) return;
    placeQSearchByTrigger(lastTrigger);
  }

  window.addEventListener('resize', onViewportChange);
  window.addEventListener('scroll', onViewportChange, true);

  setStateIdle();
})();


























/* ================================
   Mobile menu: accordion "Catalog"
================================ */

(function () {
  if (!mMenuLayer) return;

  const items = mMenuLayer.querySelectorAll('[data-mmenu-item]');
  const toggles = mMenuLayer.querySelectorAll('[data-mmenu-subtoggle]');

  function closeAllSubs() {
    items.forEach((it) => {
      it.classList.remove('is-sub-open');
      const tg = it.querySelector('[data-mmenu-subtoggle]');
      if (tg) tg.setAttribute('aria-expanded', 'false');
      const wrap = it.querySelector('.zpm-mmenu__subwrap');
      if (wrap) wrap.setAttribute('aria-hidden', 'true');
    });
  }

  // При каждом открытии меню — сворачиваем всё (чтобы не “залипало” состояние)
  if (mMenuBtn) {
    mMenuBtn.addEventListener(
      'click',
      () => {
        closeAllSubs();
      },
      true
    );
  }

  toggles.forEach((btn) => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();

      const item = btn.closest('[data-mmenu-item]');
      if (!item) return;

      const willOpen = !item.classList.contains('is-sub-open');

      // поведение: один открытый раздел (как “аккордеон”)
      closeAllSubs();

      item.classList.toggle('is-sub-open', willOpen);
      btn.setAttribute('aria-expanded', willOpen ? 'true' : 'false');

      const wrap = item.querySelector('.zpm-mmenu__subwrap');
      if (wrap) wrap.setAttribute('aria-hidden', willOpen ? 'false' : 'true');
    });
  });
})();








/* ================================
   5. Filters sidebar (popup manager)
   - mobile: offcanvas как mobile menu
   - desktop: обычный sidebar
   - без дублей overlay / scroll lock
================================ */

const fOpen = document.querySelector('[data-filter-open]');
const fLayer = document.querySelector('[data-filter-sidebar]');
const fPanel = fLayer ? fLayer.querySelector('.category__sidebar__panel') : null;
const fForm = document.querySelector('[data-filters-form]');

registerPopup({
  name: 'filter',
  trigger: fOpen,
  layer: fLayer,
  layerRootForFocus: fPanel || fLayer,
  htmlClass: 'is-filter-open',
  isAriaDialog: true,
  overlayTheme: 'light',
  focusOnOpenEl: fLayer ? fLayer.querySelector('[data-filter-close]') : null,
  closeSelectors: '[data-filter-close]',
  triggerMode: 'toggle',
  allowOutsideClose: false,
  useHidden: false,
});

(function () {
  if (!fOpen || !fLayer) return;

  function isDesktop() {
    return window.matchMedia && window.matchMedia('(min-width: 1025px)').matches;
  }

  function setExpanded(isOpen) {
    fOpen.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    fLayer.setAttribute('aria-hidden', isOpen ? 'false' : 'true');
  }

  function syncState() {
    if (isDesktop()) {
      fOpen.setAttribute('aria-expanded', 'false');
      fLayer.setAttribute('aria-hidden', 'false');
      return;
    }

    const isOpen = document.documentElement.classList.contains('is-filter-open');
    setExpanded(isOpen);
  }

  syncState();
  window.addEventListener('resize', syncState);

  fOpen.addEventListener(
    'click',
    () => {
      requestAnimationFrame(syncState);
    },
    true
  );

  fLayer.querySelectorAll('[data-filter-close]').forEach((el) => {
    el.addEventListener(
      'click',
      () => {
        requestAnimationFrame(syncState);
      },
      true
    );
  });

  document.addEventListener(
    'keydown',
    (e) => {
      if (e.key !== 'Escape') return;
      requestAnimationFrame(syncState);
    },
    true
  );
})();

const fReset = fLayer ? fLayer.querySelector('[data-filter-reset]') : null;
if (fReset && fForm) {
  fReset.addEventListener('click', (e) => {
    e.preventDefault();
    fForm.reset();
  });
}

if (fForm) {
  fForm.addEventListener('submit', () => {
    const isMobile = window.matchMedia && window.matchMedia('(max-width: 1024px)').matches;
    if (!isMobile) return;

    requestAnimationFrame(() => {
      const closeBtn = fLayer ? fLayer.querySelector('[data-filter-close]') : null;
      if (closeBtn) closeBtn.click();
    });
  });
}


















/* ================================
   Mini cart (global layer)
================================ */

(function () {
  const triggers = Array.from(document.querySelectorAll('[data-minicart-open]'));
  const layer = document.querySelector('[data-minicart]');
  const panel = layer ? layer.querySelector('.zpm-minicart__panel') : null;

  if (!triggers.length || !layer || !panel) return;

  const mainTrigger = triggers[0];
  let lastTrigger = mainTrigger;

  const ANIM_MS = 300;
  let hideTimer = null;

  function isMobile() {
    return !!(window.matchMedia && window.matchMedia('(max-width: 1024px)').matches);
  }

  function isOpen() {
    return document.documentElement.classList.contains('is-minicart-open');
  }

  function clearHideTimer() {
    if (hideTimer) {
      clearTimeout(hideTimer);
      hideTimer = null;
    }
  }

  function ensureLayerVisibleForAnim() {
    clearHideTimer();
    if (layer.hasAttribute('hidden')) layer.removeAttribute('hidden');
    if (layer.getAttribute('aria-hidden') === 'true') layer.setAttribute('aria-hidden', 'false');
  }

  function scheduleLayerHiddenAfterClose() {
    clearHideTimer();
    hideTimer = setTimeout(() => {
      if (isOpen()) return;
      layer.setAttribute('hidden', '');
      layer.setAttribute('aria-hidden', 'true');
    }, ANIM_MS);
  }

  function placePanelByTrigger(btn) {
    if (!btn) return;

    const rect = btn.getBoundingClientRect();
    const top = Math.round(rect.bottom + 0);

    if (isMobile()) {
      // На mobile горизонталь отдаём CSS:
      // left/right/top/transform из media rules
      panel.style.removeProperty('--mc-left');
      panel.style.removeProperty('--mc-top');
      return;
    }

    let left;

    if (window.innerWidth <= 1560) {
      // <=1560: панель смещаем по правой стороне кнопки + 90px.
      // Важно: в desktop CSS используется translateX(-50%),
      // значит в --mc-left передаём не край, а опорную точку.
      const panelWidth = panel.offsetWidth || panel.getBoundingClientRect().width || 0;
      left = Math.round(rect.right + 90 - panelWidth / 2);
    } else {
      // Стандарт: по центру кнопки
      left = Math.round(rect.left + rect.width / 2);
    }

    panel.style.setProperty('--mc-top', top + 'px');
    panel.style.setProperty('--mc-left', left + 'px');
  }

  registerPopup({
    name: 'minicart',
    trigger: mainTrigger,
    extraTriggers: triggers.slice(1),
    layer: layer,
    layerRootForFocus: panel,
    htmlClass: 'is-minicart-open',
    isAriaDialog: true,
    overlayTheme: 'light',
    focusOnOpenEl: layer.querySelector('[data-minicart-close]') || null,
    closeSelectors: '[data-minicart-close]',
    triggerMode: 'toggle',
    allowOutsideClose: true,
  });

  triggers.forEach((btn) => {
    btn.addEventListener('click', () => {
      lastTrigger = btn;

      ensureLayerVisibleForAnim();
      placePanelByTrigger(btn);
      requestAnimationFrame(() => placePanelByTrigger(btn));

      setTimeout(() => {
        if (!isOpen()) scheduleLayerHiddenAfterClose();
      }, 0);
    });
  });

  function onViewportChange() {
    if (!isOpen()) return;
    placePanelByTrigger(lastTrigger);
  }

  window.addEventListener('resize', onViewportChange);
  window.addEventListener('scroll', onViewportChange, true);

  const countElements = document.querySelectorAll('[data-cart-count]');
  function syncBadge() {
    // Если элементов вообще нет, выходим
    if (countElements.length === 0) return;

    // Берем значение из первого попавшегося (предполагаем, что они синхронны по тексту)
    const n = parseInt((countElements[0].textContent || '0').trim(), 10) || 0;

    // Переключаем класс у триггеров
    triggers.forEach((t) => t.classList.toggle('has-items', n > 0));
  }
  syncBadge();

  window.ZpmMiniCart = window.ZpmMiniCart || {};
  window.ZpmMiniCart.syncBadge = syncBadge;

  (function () {
    function syncExpanded() {
      const opened = document.documentElement.classList.contains('is-minicart-open');

      triggers.forEach((btn) => {
        btn.setAttribute('aria-expanded', opened ? 'true' : 'false');
      });

      layer.setAttribute('aria-hidden', opened ? 'false' : 'true');
    }

    syncExpanded();

    const mo = new MutationObserver(function (muts) {
      for (let i = 0; i < muts.length; i++) {
        if (muts[i].attributeName === 'class') {
          syncExpanded();
          break;
        }
      }
    });

    mo.observe(document.documentElement, {
      attributes: true,
      attributeFilter: ['class'],
    });
  })();

  if (!isOpen()) {
    layer.setAttribute('hidden', '');
    layer.setAttribute('aria-hidden', 'true');
  }
})();







  /* ================================
     7) City picker (center modal)
     Триггеры: [data-city-open]
     Слой: [data-city]
     Закрытие: [data-city-close] / overlay / ESC
  ================================ */
 const cityTriggers = document.querySelectorAll('[data-city-open]');
  const cityLayer = document.querySelector('[data-city]');
  const cityPanel = cityLayer ? cityLayer.querySelector('.zpm-city__panel') : null;

  if (cityTriggers.length && cityLayer) {
    registerPopup({
      name: 'city',
      trigger: cityTriggers[0],
      layer: cityLayer,
      layerRootForFocus: cityPanel || cityLayer,
      htmlClass: 'is-city-open',
      isAriaDialog: true,
      overlayTheme: 'light',
      focusOnOpenEl: cityLayer.querySelector('[data-city-search]') || cityLayer.querySelector('[data-city-close]') || null,
      closeSelectors: '[data-city-close]',
      triggerMode: 'toggle',
      allowOutsideClose: true,
    });

    cityTriggers.forEach((tr, idx) => {
      if (idx === 0) return;
      tr.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        openPopup('city');
      });
    });

    // 3. НОВИНКА: Обработчик клика по городу ВНУТРИ модалки
    cityLayer.addEventListener('click', (e) => {
      const cityBtn = e.target.closest('[data-set-city]');
      if (cityBtn) {
        const cityKey = cityBtn.dataset.setCity;
        updateCityUI(cityKey);

        // Если у тебя есть функция закрытия попапа, вызови её тут
        // Например, если библиотека поддерживает closePopup:
        if (typeof closePopup === 'function') {
          closePopup('city');
        } else {
      // Если штатного метода нет в глобальной видимости,
      // имитируем клик по любому элементу с атрибутом закрытия внутри этого попапа
      const closeBtn = cityLayer.querySelector('[data-city-close]');
      if (closeBtn) {  closeBtn.click();  }
      }




      }
    });
  }

  // 4. НОВИНКА: Проверка сохраненного города при загрузке
  const savedCity = localStorage.getItem('selected_city');
  if (savedCity) {
    updateCityUI(savedCity);
  }


})();









/* ==========================================================
   ISOLATED HANDLER FOR DEALER FORM (ZPM)
   ========================================================== */
(function () {
  'use strict';

  // Конфигурация
var CONFIG = {
    formSelector: '.zpm-dealers[data-dealers] .zpm-form',
    endpoint: '/index.php?route=checkout/anketa',
    successMsg: 'Спасибо! Ваша заявка успешно отправлена.',
    errorMsg: 'Произошла ошибка при отправке.',
    msgDuration: 5000
  };

  // Инициализация при загрузке DOM
  document.addEventListener('DOMContentLoaded', function () {
    var form = document.querySelector(CONFIG.formSelector);
    // ДОБАВИМ ЛОГ ДЛЯ ПРОВЕРКИ
    if (!form) {

      return;
    }

    initPhoneMask(form);
    initEmailValidation(form);
    initSubmitHandler(form);
  });

  /* ---------- Валидация и маски (адаптировано из вашего кода) ---------- */
  function initPhoneMask(scope) {
    var nodes = scope.querySelectorAll('[data-mask="phone"]');
    if (!nodes.length) return;

    if (window.Inputmask) {
      nodes.forEach(function (el) {
        window.Inputmask({
          mask: '+7 (999) 999-99-99',
          showMaskOnHover: false,
          clearIncomplete: true,
        }).mask(el);
      });
    } else if (window.jQuery && jQuery.fn.inputmask) {
      jQuery(nodes).inputmask({
        mask: '+7 (999) 999-99-99',
        showMaskOnHover: false,
        clearIncomplete: true,
      });
    }
  }

  function initEmailValidation(scope) {
    var inputs = scope.querySelectorAll('[data-validate="email"]');
    var strictEmailRe = /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/;

    inputs.forEach(function (el) {
      function validate() {
        var v = (el.value || '').trim();
        if (!v) { el.setCustomValidity(''); return; }
        if (/[А-Яа-яЁё]/.test(v)) { el.setCustomValidity('Email должен быть латиницей'); return; }
        if (!strictEmailRe.test(v)) { el.setCustomValidity('Введите корректный email'); return; }
        el.setCustomValidity('');
      }
      el.addEventListener('input', validate);
    });
  }

  /* ---------- Обработка отправки ---------- */
  function initSubmitHandler(form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();

      var submitBtn = form.querySelector('.zpm-form__submit');
      var originalBtnText = submitBtn ? submitBtn.innerText : 'Отправить';

      // 1. Проверка согласия (чекбокс)
      var agreeCheckbox = form.querySelector('[name="agree"]');
      if (agreeCheckbox && !agreeCheckbox.checked) {
        showStatus(form, 'Пожалуйста, подтвердите согласие на обработку данных', 'warning');
        return;
      }

      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerText = 'Отправка...';
      }

      sendForm(form)
        .then(function () {
          showStatus(form, CONFIG.successMsg, 'success');
          form.reset();
        })
        .catch(function (err) {
          showStatus(form, err.message || CONFIG.errorMsg, 'error');
        })
        .finally(function () {
          if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.innerText = originalBtnText;
          }
        });
    });
  }

  function sendForm(form) {
    return new Promise(function (resolve, reject) {
      var csrfToken = document.querySelector('meta[name="csrf-token"]')?.getAttribute('content');
      var siteKey = document.querySelector('script[src*="google.com/recaptcha"]')?.getAttribute('data-sitekey');

      if (window.grecaptcha && siteKey) {
        grecaptcha.ready(function() {
          grecaptcha.execute(siteKey, { action: 'dealer_form' }).then(function(token) {
            processFetch(form, token, csrfToken, resolve, reject);
          });
        });
      } else {
        processFetch(form, null, csrfToken, resolve, reject);
      }
    });
  }

  function processFetch(form, captchaToken, csrfToken, resolve, reject) {
    var formData = new FormData(form);
    if (csrfToken) formData.append('csrf_token', csrfToken);
    if (captchaToken) formData.append('g-recaptcha-response', captchaToken);

    fetch(CONFIG.endpoint, {
      method: 'POST',
      body: formData
    })
    .then(function(response) { return response.json(); })
    .then(function(data) {
      if (data.ok) resolve(data);
      else reject(new Error(data.message || CONFIG.errorMsg));
    })
    .catch(function(err) { reject(err); });
  }

  /* ---------- Уведомления (вместо Alert) ---------- */
  function showStatus(form, text, type) {
    // Удаляем старые сообщения если есть
    var oldMsg = form.querySelector('.zpm-form__status-msg');
    if (oldMsg) oldMsg.remove();

    var msg = document.createElement('div');
    msg.className = 'zpm-form__status-msg zpm-form__status-msg--' + type;

    // Стилизация для того, чтобы "хорошо смотрелось"
    Object.assign(msg.style, {
      marginTop: '15px',
      padding: '12px 15px',
      borderRadius: '4px',
      fontSize: '14px',
      lineHeight: '1.4',
      textAlign: 'center',
      transition: 'all 0.3s ease'
    });

    if (type === 'success') {
      msg.style.backgroundColor = '#d4edda';
      msg.style.color = '#155724';
      msg.style.border = '1px solid #c3e6cb';
    } else if (type === 'error') {
      msg.style.backgroundColor = '#f8d7da';
      msg.style.color = '#721c24';
      msg.style.border = '1px solid #f5c6cb';
    } else {
      msg.style.backgroundColor = '#fff3cd';
      msg.style.color = '#856404';
      msg.style.border = '1px solid #ffeeba';
    }

    msg.innerText = text;
    form.appendChild(msg);

    // Авто-удаление через 5 секунд
    setTimeout(function() {
      msg.style.opacity = '0';
      setTimeout(function() { msg.remove(); }, 300);
    }, CONFIG.msgDuration);
  }

})();























/* ==========================================================
   FANCYBOX FORMS + ZPM MODES (1/2/3) — VERSION-INDEPENDENT (patched)
   + ZPM animations for forms (open delay 0.3s, open anim 0.3s, close down+fade 0.3s)
   + Disable drag/pan for forms to not break transforms

   Режимы на кнопке:
     data-zpm-fb-mode="1" -> после закрытия Fancybox закрыть ВСЁ ZPM
     data-zpm-fb-mode="2" -> ничего не закрывать (закрывается только Fancybox)
     data-zpm-fb-mode="3" -> закрыть ВСЁ ZPM ДО открытия Fancybox
========================================================== */
(function () {
  if (typeof window.Fancybox === 'undefined') return;

  var MSG_MS = 3000;

  // Тайминги анимаций должны совпадать с CSS
  var OPEN_DELAY_MS = 300; // задержка после overlay
  var ANIM_MS = 300; // длительность анимации

  /* ---------- Phone mask ---------- */
  function initPhoneMask(root) {
    var scope = root || document;
    var nodes = scope.querySelectorAll('[data-mask="phone"]');
    if (!nodes.length) return;

    if (window.Inputmask) {
      nodes.forEach(function (el) {
        if (el.dataset.maskInited === '1') return;
        window.Inputmask({
          mask: '+7 (999) 999-99-99',
          showMaskOnHover: false,
          clearIncomplete: true,
        }).mask(el);
        el.dataset.maskInited = '1';
      });
      return;
    }

    if (!window.jQuery || !jQuery.fn || !jQuery.fn.inputmask) return;

    var fresh = Array.prototype.filter.call(nodes, function (el) {
      return el.dataset.maskInited !== '1';
    });
    if (!fresh.length) return;

    jQuery(fresh).inputmask({
      mask: '+7 (999) 999-99-99',
      showMaskOnHover: false,
      clearIncomplete: true,
    });

    fresh.forEach(function (el) { el.dataset.maskInited = '1'; });
  }

  /* ---------- Email validation ---------- */
  function initEmailValidation(root) {
    var scope = root || document;
    var inputs = scope.querySelectorAll('[data-validate="email"]');
    if (!inputs.length) return;

    var strictEmailRe = /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/;

    inputs.forEach(function (el) {
      if (el.dataset.emailInited === '1') return;
      el.dataset.emailInited = '1';

      function normalize() {
        var v = el.value || '';
        var cleaned = v.replace(/\s+/g, '').trim();
        if (cleaned !== v) el.value = cleaned;
      }

      function validate() {
        var v = (el.value || '').trim();

        if (!v && !el.hasAttribute('required')) { el.setCustomValidity(''); return; }
        if (!v && el.hasAttribute('required')) { el.setCustomValidity(''); return; }

        if (/[А-Яа-яЁё]/.test(v)) { el.setCustomValidity('Email должен быть латиницей'); return; }
        if (!strictEmailRe.test(v)) { el.setCustomValidity('Введите email в формате name@domain.ru / .com'); return; }

        el.setCustomValidity('');
      }

      el.addEventListener('input', function () { normalize(); validate(); });
      el.addEventListener('blur', function () { normalize(); validate(); });
      el.addEventListener('change', function () { normalize(); validate(); });
    });
  }

  /* ---------- FB states ---------- */
  function setState(wrap, state) {
    var blocks = wrap.querySelectorAll('[data-fb-state]');
    blocks.forEach(function (b) {
      b.hidden = b.getAttribute('data-fb-state') !== state;
    });
  }

  function getFirstField(form) {
    return form.querySelector('input:not([type="hidden"]), textarea, select, button');
  }

 /* ---------- Submit (с reCaptcha v3) ---------- */
/* ---------- Submit (с reCaptcha v3 + CSRF) ---------- */
function sendForm(form) {
    return new Promise(function (resolve, reject) {
        // --- 1. Получение CSRF токена ---
        var csrfToken = document.querySelector('meta[name="csrf-token"]')?.getAttribute('content');

        // Если токена нет (ошибка на сервере), можно либо отказать, либо пропустить (не рекомендуется для продакшена)
        if (!csrfToken) {
            console.error('❌ CSRF токен не найден! Проверьте PHP генерацию.');
            reject(new Error('Ошибка безопасности: отсутствует CSRF токен'));
            return;
        }

        // --- 2. Логика reCaptcha (если нужна) ---
        var siteKey = null;
        var recaptchaScript = document.querySelector('script[src*="google.com/recaptcha"]');
        if (recaptchaScript) {
            siteKey = recaptchaScript.getAttribute('data-sitekey');
        }

        if (!window.grecaptcha || !siteKey) {
             // Если капча не настроена, но CSRF есть — продолжаем
        } else {
            grecaptcha.ready(function() {
                grecaptcha.execute(siteKey, { action: 'submit' }).then(function(token) {
                    processSubmission(form, token, csrfToken, resolve, reject);
                });
            });
            return; // Ждем завершения рекапчи
        }

        // Если капча не используется или уже прошла, отправляем сразу
        processSubmission(form, null, csrfToken, resolve, reject);
    });
}

// Выносим основную логику отправки отдельно, чтобы не дублировать код
function processSubmission(form, captchaToken, csrfToken, resolve, reject) {
    // Создаем FormData
    var formData = new FormData(form);

    // Добавляем CSRF токен в данные формы (стандартное имя поля часто '_token' или 'csrf_token')
    // ВАЖНО: Убедитесь, что ваш PHP ожидает это поле. Обычно это 'csrf_token'.
    formData.append('csrf_token', csrfToken);

    // Если есть капча, добавляем её токен
    if (captchaToken) {
        formData.append('g-recaptcha-response', captchaToken);
    }

    // Определяем URL и метод
    var url =  "/index.php?route=checkout/anketa";
    var method = 'POST';
    //var url = form.getAttribute('action') || window.location.href;
    //var method = form.getAttribute('method') || 'POST';

    // Отправляем запрос
    fetch(url, {
        method: method,
        body: formData
    })
    .then(response => response.json()) // Ожидаем JSON ответ
    .then(data => {
        if (data.ok) {
            resolve({ ok: true });
        } else {
            // Проверяем, не ошибка ли это CSRF на стороне сервера
            if (data.message && data.message.includes('CSRF')) {
                reject(new Error('Ошибка безопасности: истек токен CSRF. Обновите страницу.'));
            } else {
                reject(new Error(data.message || 'Ошибка обработки'));
            }
        }
    })
    .catch(error => {
        reject(error);
    });
}

  /* ---------- Fancybox: убрать прыжок (страховка) ---------- */
  try {
    if (window.Fancybox && window.Fancybox.defaults) {
      window.Fancybox.defaults.hideScrollbar = false;
    }
  } catch (e) {}

  /* ==========================================================
     MODE STORE (на html.dataset)
========================================================== */
  function setMode(mode) {
    document.documentElement.dataset.zpmFbMode = mode;
  }
  function getMode() {
    return (document.documentElement.dataset.zpmFbMode || '1').trim();
  }
  function clearMode() {
    delete document.documentElement.dataset.zpmFbMode;
  }

  /* ==========================================================
     Helper: get current fancybox container (if any)
========================================================== */
  function getFbContainer() {
    return document.querySelector('.fancybox__container');
  }

  function markOpening() {
    var c = getFbContainer();
    if (!c) return;
    c.classList.add('zpm-fancybox', 'zpm-fb-anim', 'zpm-fb-opening');
    c.classList.remove('zpm-fb-closing');

    // снимаем opening после delay+anim
    setTimeout(function () {
      var cc = getFbContainer();
      if (!cc) return;
      cc.classList.remove('zpm-fb-opening');
    }, OPEN_DELAY_MS + ANIM_MS + 80);
  }

  function markClosing() {
    var c = getFbContainer();
    if (!c) return;
    c.classList.add('zpm-fancybox', 'zpm-fb-anim', 'zpm-fb-closing');
    c.classList.remove('zpm-fb-opening');
  }

  /* ==========================================================
     Trigger click: сохраняем режим + mode 3 закрываем ZPM до открытия
     + force form-friendly options (disable drag/pan) for these triggers
========================================================== */
  document.addEventListener('click', function (e) {
    var btn = e.target.closest('button[data-fancybox][data-src]');
    if (!btn) return;

    var mode = (btn.getAttribute('data-zpm-fb-mode') || '1').trim();
    setMode(mode);

    if (mode === '3') {
      if (window.ZpmPopupManager && typeof window.ZpmPopupManager.closeAll === 'function') {
        window.ZpmPopupManager.closeAll();
      }
    }

    // На всякий случай: если это наши формы, отключаем drag/pan/zoom,
    // чтобы fancy не перетирал transform и не ломал анимации
    try {
      if (window.Fancybox && window.Fancybox.defaults) {
        // Эти поля отличаются по сборкам; ставим максимально мягко
        window.Fancybox.defaults.dragToClose = false;
        window.Fancybox.defaults.placeFocusBack = true;

        if (window.Fancybox.defaults.Carousel) {
          window.Fancybox.defaults.Carousel = window.Fancybox.defaults.Carousel || {};
          window.Fancybox.defaults.Carousel.friction = 0.9;
          window.Fancybox.defaults.Carousel.Panzoom = window.Fancybox.defaults.Carousel.Panzoom || {};
          window.Fancybox.defaults.Carousel.Panzoom.panMode = 'mousemove'; // не тащить контент пальцем
          window.Fancybox.defaults.Carousel.Panzoom.touch = false;
          window.Fancybox.defaults.Carousel.Panzoom.wheel = false;
        }
      }
    } catch (err) {}
  });

  /* ==========================================================
     Перехват закрытия: запускаем нашу анимацию и закрываем Fancybox с задержкой
     (иначе Fancybox может моментально убрать DOM и анимацию не видно)
========================================================== */
  document.addEventListener('click', function (e) {
    var isCloseBtn = e.target.closest('[data-fancybox-close], .f-button.is-close-button');
    var isBackdrop = e.target.classList && e.target.classList.contains('fancybox__backdrop');

    if (!isCloseBtn && !isBackdrop) return;

    // если fancybox не открыта — нечего делать
    if (!document.documentElement.classList.contains('with-fancybox')) return;

    // не даём Fancybox закрыться мгновенно
    e.preventDefault();
    e.stopPropagation();

    markClosing();

    // Закрываем через таймер (после анимации)
    setTimeout(function () {
      try { window.Fancybox.close(); } catch (err) {}
    }, ANIM_MS);
  }, true);

  /* ==========================================================
     Observer: фиксируем открытие/закрытие Fancybox по html.with-fancybox
========================================================== */
  var wasOpen = document.documentElement.classList.contains('with-fancybox');

  var mo = new MutationObserver(function () {
    var isOpenNow = document.documentElement.classList.contains('with-fancybox');

    // Fancybox только что открылась
    if (!wasOpen && isOpenNow) {
      // Дадим Fancybox дорисовать контейнер
      setTimeout(function () {
        markOpening();
      }, 0);
    }

    // Fancybox только что закрылась
    if (wasOpen && !isOpenNow) {
      // Флаг на 350мс: защита от "провала" pointerdown в Popup Manager
      document.documentElement.dataset.zpmFbClosing = '1';
      setTimeout(function () {
        delete document.documentElement.dataset.zpmFbClosing;
      }, 350);

      var mode = getMode();

      // mode 1: закрыть ВСЁ ZPM после закрытия Fancybox
      if (mode === '1') {
        if (window.ZpmPopupManager && typeof window.ZpmPopupManager.closeAll === 'function') {
          window.ZpmPopupManager.closeAll();
        }
      }

      clearMode();
    }

    wasOpen = isOpenNow;
  });

  mo.observe(document.documentElement, { attributes: true, attributeFilter: ['class'] });

  /* ---------- Reveal: reset + init (если событие есть) ---------- */
  try {
    window.Fancybox.on('reveal', function (fb, slide) {
      if (!slide || !slide.$content) return;

      var wrap = slide.$content.querySelector('[data-fb-modal]');
      if (!wrap) return;

      setState(wrap, 'form');
      initPhoneMask(wrap);
      initEmailValidation(wrap);
    });
  } catch (e) {}

  /* ---------- Submit ---------- */
  document.addEventListener('submit', function (e) {
    var form = e.target.closest('[data-fb-form]');
    if (!form) return;

    e.preventDefault();

    if (typeof form.checkValidity === 'function' && !form.checkValidity()) {
      if (typeof form.reportValidity === 'function') form.reportValidity();
      return;
    }

    var wrap = form.closest('[data-fb-modal]');
    if (!wrap) return;

    var submitBtn = form.querySelector('[data-fb-submit]');
    if (submitBtn) submitBtn.disabled = true;

    sendForm(form)
      .then(function () {
        setState(wrap, 'success');
        setTimeout(function () { window.Fancybox.close(); }, MSG_MS);
      })
      .catch(function () {
        setState(wrap, 'error');
        setTimeout(function () {
          setState(wrap, 'form');
          var first = getFirstField(form);
          if (first && typeof first.focus === 'function') first.focus();
        }, MSG_MS);
      })
      .finally(function () {
        if (submitBtn) submitBtn.disabled = false;
      });
  });
})();





/* ================================
   Fancybox FORMS UX (ZPM)
   - Убираем grab: и вертикальный (dragToClose), и горизонтальный (Carousel swipe)
   - Открытие: overlay сразу, контент через 0.3s (zoom+fade 0.3)
   - Закрытие: сразу запускаем down+fade 0.3, Fancybox.close() после 0.3s
================================ */

(function () {
  if (!window.Fancybox) return;

  var OPEN_DELAY_MS = 300;
  var ANIM_MS = 300;

  // Перебиндить ТОЛЬКО формы (твои кнопки)
  var FORM_SELECTOR = 'button[data-fancybox][data-src]';

  function getInstance() {
    try {
      return window.Fancybox.getInstance && window.Fancybox.getInstance();
    } catch (e) {
      return null;
    }
  }

  function markOpenAnim(fb) {
    if (!fb || !fb.container) return;
    var c = fb.container;

    c.classList.add('zpm-fancybox-anim');
    c.classList.remove('zpm-fb-closing');
    c.classList.add('zpm-fb-opening');

    // через delay даём появиться контенту
    setTimeout(function () {
      if (!c.isConnected) return;
      c.classList.add('zpm-fb-open');
    }, OPEN_DELAY_MS);

    // cleanup opening
    setTimeout(function () {
      if (!c.isConnected) return;
      c.classList.remove('zpm-fb-opening');
    }, OPEN_DELAY_MS + ANIM_MS + 50);
  }

  function startCloseAnimAndClose() {
    var fb = getInstance();
    if (!fb || !fb.container) {
      try { window.Fancybox.close(); } catch (e) {}
      return;
    }

    var c = fb.container;

    // моментально начинаем анимацию (чтобы не было ощущения задержки)
    c.classList.add('zpm-fancybox-anim');
    c.classList.remove('zpm-fb-opening', 'zpm-fb-open');
    c.classList.add('zpm-fb-closing');

    // чтобы не было кликов во время анимации
    c.style.pointerEvents = 'none';

    setTimeout(function () {
      try { window.Fancybox.close(); } catch (e) {}
    }, ANIM_MS);
  }

  // Снять старые бинды и повесить наши опции на формы
  try { window.Fancybox.unbind && window.Fancybox.unbind(FORM_SELECTOR); } catch (e) {}

  try {
    window.Fancybox.bind(FORM_SELECTOR, {
      // ВАЖНО: убираем вертикальный drag-to-close
      dragToClose: false,

      // Убираем горизонтальный swipe (Carousel)
      Carousel: {
        // выключаем свайпы/перетаскивание
        Panzoom: {
          touch: false,
          wheel: false,
        },
        // доп. страховка: не нужен “слайдер” в формах
        Dots: false,
        Navigation: false,
        infinite: false,
      },

      on: {
        init: function (fb) {
          // overlay появится сразу (Fancybox сам)
          // контент — мы “задержим” стилями через классы
          markOpenAnim(fb);
        },
      },
    });
  } catch (e) {}

  // Закрытие: кнопка / backdrop / ESC — запускаем нашу анимацию и закрываем после 0.3s
  document.addEventListener(
    'click',
    function (e) {
      if (!document.documentElement.classList.contains('with-fancybox')) return;

      var closeBtn = e.target.closest('[data-fancybox-close], .f-button.is-close-button');
      var isBackdrop = e.target.classList && e.target.classList.contains('fancybox__backdrop');

      if (!closeBtn && !isBackdrop) return;

      e.preventDefault();
      e.stopPropagation();

      startCloseAnimAndClose();
    },
    true
  );

  document.addEventListener(
    'keydown',
    function (e) {
      if (e.key !== 'Escape') return;
      if (!document.documentElement.classList.contains('with-fancybox')) return;

      e.preventDefault();
      e.stopPropagation();

      startCloseAnimAndClose();
    },
    true
  );
})();

/* ================================
   ZPM trigger .open sync
   - ставим/снимаем .open на триггерах наших попапов по html-классам
   - не вмешивается в Popup Manager
================================ */

(function () {
  var html = document.documentElement;

  var rules = [
    { selector: '[data-catalog-open]', htmlClass: 'is-catalog-open' },
    { selector: '[data-qsearch-trigger]', htmlClass: 'is-qsearch-open' },
    { selector: '[data-mobile-search-open]', htmlClass: 'is-qsearch-mobile-open' },
    { selector: '[data-menu-open]', htmlClass: 'is-mmenu-open' },
    { selector: '[data-filter-open]', htmlClass: 'is-filter-open' },
  ];

  function apply() {
    rules.forEach(function (r) {
      var isOn = html.classList.contains(r.htmlClass);
      document.querySelectorAll(r.selector).forEach(function (el) {
        el.classList.toggle('open', isOn);
      });
    });

    // minicart: несколько триггеров
    var mcOn = html.classList.contains('is-minicart-open');
    document.querySelectorAll('[data-minicart-open]').forEach(function (el) {
      el.classList.toggle('open', mcOn);
    });
  }

  apply();

  var mo = new MutationObserver(function (muts) {
    for (var i = 0; i < muts.length; i++) {
      if (muts[i].attributeName === 'class') {
        apply();
        break;
      }
    }
  });

  mo.observe(html, { attributes: true, attributeFilter: ['class'] });
})();


/* ================================
   Fancybox (forms) — standard bind
   - Отключаем grab/drag/pan для форм (чтобы не мешал анимации)
   - RU локализация кнопок (Close/Next/Prev/…)
   - Классы для ZPM анимаций + отложенное закрытие
   - Не ломает ZPM popup manager (modes 1/2/3 остаются отдельным модулем)
================================ */

(function () {
  if (!window.Fancybox) return;

  var CLOSE_TEXT = 'Закрыть окно';

  // тайминги должны совпадать с CSS
  var OPEN_DELAY_MS = 300;
  var ANIM_MS = 300;

  // Ключевые опции: отключаем “граб”/перетаскивание и жесты
  function buildFormOptions() {
    return {
      // UI text
      l10n: {
        CLOSE: CLOSE_TEXT,
        NEXT: 'Вперёд',
        PREV: 'Назад',
        MODAL: 'Модальное окно',
        ERROR: 'Не удалось загрузить содержимое. Попробуйте ещё раз.',
        IMAGE_ERROR: 'Не удалось загрузить изображение.',
        IFRAME_ERROR: 'Ошибка загрузки страницы.',
        DOWNLOAD: 'Скачать',
        FULLSCREEN: 'Полный экран',
        THUMBS: 'Миниатюры',
        ZOOM: 'Увеличить',
        SLIDESHOW: 'Слайд-шоу',
      },

      // НЕ даём тащить/“грабить”
      dragToClose: false,
      closeButton: true,

      // В большинстве сборок v4 жесты живут в Carousel/Panzoom.
      // Ставим максимально “мягко”, чтобы не упасть на другой версии.
      Carousel: {
        // запрещаем свайп-слайдер и тянучку
        friction: 0.95,
        Panzoom: {
          touch: false,
          wheel: false,
          panMode: 'mousemove',
        },
      },

      // Хуки: добавляем классы и правим title/aria
      on: {
        init: function (fb) {
          try {
            if (fb && fb.container) {
              fb.container.classList.add('zpm-fancybox', 'zpm-fb-anim', 'zpm-fb-opening');
              setTimeout(function () {
                if (fb.container) fb.container.classList.remove('zpm-fb-opening');
              }, OPEN_DELAY_MS + ANIM_MS + 80);
            }
          } catch (e) {}
        },

        done: function (fb) {
          // подстрахуем подписи кнопок
          try {
            if (!fb || !fb.container) return;

            fb.container
              .querySelectorAll('.f-button.is-close-button,[data-fancybox-close]')
              .forEach(function (btn) {
                btn.setAttribute('title', CLOSE_TEXT);
                btn.setAttribute('aria-label', CLOSE_TEXT);
              });

            fb.container.querySelectorAll('.f-button.is-next').forEach(function (btn) {
              btn.setAttribute('title', 'Вперёд');
              btn.setAttribute('aria-label', 'Вперёд');
            });

            fb.container.querySelectorAll('.f-button.is-prev').forEach(function (btn) {
              btn.setAttribute('title', 'Назад');
              btn.setAttribute('aria-label', 'Назад');
            });
          } catch (e) {}
        },
      },
    };
  }

  // 1) Перебиндим все [data-fancybox] (стандартный способ для v4)
  //    Чтобы не было двойных обработчиков, сначала пытаемся unbind.
  try { Fancybox.unbind('[data-fancybox]'); } catch (e) {}

  // Общий bind — подстрахуем любые опенкартовские галереи.
  // Для галерей drag может быть полезен, поэтому тут НЕ выключаем жесты.
  try {
    Fancybox.bind('[data-fancybox]', {
      l10n: {
        CLOSE: CLOSE_TEXT,
        NEXT: 'Вперёд',
        PREV: 'Назад',
      },
    });
  } catch (e) {}

  // 2) Отдельный bind для твоих форм-кнопок (button[data-fancybox][data-src])
  //    Здесь выключаем grab/drag
  try {
    Fancybox.unbind('button[data-fancybox][data-src]');
  } catch (e) {}

  try {
    Fancybox.bind('button[data-fancybox][data-src]', buildFormOptions());
  } catch (e) {}

  // 3) Отложенное закрытие, чтобы закрывающая анимация успела сыграть
  //    Перехватываем click по close/backdrop только когда открыт Fancybox
  document.addEventListener(
    'click',
    function (e) {
      if (!document.documentElement.classList.contains('with-fancybox')) return;

      var closeBtn = e.target.closest('[data-fancybox-close], .f-button.is-close-button');
      var isBackdrop = e.target.classList && e.target.classList.contains('fancybox__backdrop');
      if (!closeBtn && !isBackdrop) return;

      // Не даём закрыться мгновенно
      e.preventDefault();
      e.stopPropagation();

      // Берём текущий instance (v4)
      var fb = null;
      try { fb = Fancybox.getInstance && Fancybox.getInstance(); } catch (err) {}

      // Ставим closing class на контейнер
      try {
        var c = fb && fb.container ? fb.container : document.querySelector('.fancybox__container');
        if (c) {
          c.classList.add('zpm-fancybox', 'zpm-fb-anim', 'zpm-fb-closing');
          c.classList.remove('zpm-fb-opening');
        }
      } catch (err) {}

      setTimeout(function () {
        try { Fancybox.close(); } catch (err) {}
      }, ANIM_MS);
    },
    true
  );

  // 4) Escape тоже закрываем с анимацией (иначе будет мгновенно)
  document.addEventListener(
    'keydown',
    function (e) {
      if (e.key !== 'Escape') return;
      if (!document.documentElement.classList.contains('with-fancybox')) return;

      e.preventDefault();
      e.stopPropagation();

      var fb = null;
      try { fb = Fancybox.getInstance && Fancybox.getInstance(); } catch (err) {}

      try {
        var c = fb && fb.container ? fb.container : document.querySelector('.fancybox__container');
        if (c) {
          c.classList.add('zpm-fancybox', 'zpm-fb-anim', 'zpm-fb-closing');
          c.classList.remove('zpm-fb-opening');
        }
      } catch (err) {}

      setTimeout(function () {
        try { Fancybox.close(); } catch (err) {}
      }, ANIM_MS);
    },
    true
  );
})();


















/* ==========================================================
   MODIFIED CART LOGIC FOR OPENCART
========================================================== */
(function () {
  const MAX_QTY = 99;
  const CART_URL = '/cart';
  const state = new Map(); // productId -> qty
  let totalCartItems = 0;

  const baseUrl =
    typeof OC_CART_CONFIG !== 'undefined'
      ? OC_CART_CONFIG.baseUrl
      : '/index.php?route=';

  function setSvgUse(svgEl, iconId) {
    if (!svgEl) return;
    const use = svgEl.querySelector('use');
    if (!use) return;
    use.setAttribute('href', iconId);
  }

  function syncBuyOk(cardEl, qty) {
    if (!cardEl) return;

    const ok = cardEl.querySelector('.p-card__buy-ok');
    if (!ok) return;

    if (qty <= 0) {
      ok.hidden = true;
      ok.style.display = 'none';
    } else {
      ok.hidden = false;
      ok.style.display = '';

      const cnt = ok.querySelector('.p-card__buy-ok--count');
      if (cnt) cnt.textContent = qty + ' шт.';
    }
  }

  function syncStepper(stepperEl, qty) {
    if (!stepperEl) return;

    const val = stepperEl.querySelector('[data-qty-value]');
    const minus = stepperEl.querySelector('[data-qty-minus]');
    const plus = stepperEl.querySelector('[data-qty-plus]');

    if (val) val.textContent = String(qty);
    if (minus) minus.disabled = qty <= 0;
    if (plus) plus.disabled = qty >= MAX_QTY;
  }

  function syncCardActions(actionsEl, qty) {
    if (!actionsEl) return;

    actionsEl.classList.toggle('is-qty', qty > 0);

    const stepper = actionsEl.querySelector('[data-cart-qty-card]');
    syncStepper(stepper, qty);

    const card = actionsEl.closest('.p-card');
    syncBuyOk(card, qty);
  }

  function syncPdpActions(pdpEl, qty) {
    if (!pdpEl) return;

    pdpEl.classList.toggle('added', qty > 0);

    const stepper = pdpEl.querySelector('[data-cart-qty]');
    syncStepper(stepper, qty);

    const btn = pdpEl.querySelector('[data-cart-add]');
    if (!btn) return;

    const textEl = btn.querySelector('.btn__text');
    const svgEl = btn.querySelector('svg.zpm-icon');

    if (qty > 0) {
      btn.classList.add('added');
      btn.setAttribute('data-cart-ready', 'true');

      if (textEl) textEl.textContent = 'Заказать';
      setSvgUse(svgEl, '#zpm_ico__successful');
    } else {
      btn.classList.remove('added');
      btn.removeAttribute('data-cart-ready');

      if (textEl) textEl.textContent = 'В корзину';
      setSvgUse(svgEl, '#zpm_ico__cart');
    }
  }

  function updateHeaderCounter(count) {
    const counter = document.getElementById('cartcounter');
    const countermobile = document.getElementById('cartcountermobile');

    if (count !== null && count !== undefined) {
      totalCartItems = count;
    }

    if (counter) {
      counter.textContent = totalCartItems;

      if (totalCartItems > 0) {
        counter.hidden = false;
        counter.removeAttribute('hidden');
      } else {
        counter.hidden = true;
        counter.setAttribute('hidden', '');
      }
    }

    if (countermobile) {
      countermobile.textContent = totalCartItems;

      if (totalCartItems > 0) {
        countermobile.hidden = false;
        countermobile.removeAttribute('hidden');
      } else {
        countermobile.hidden = true;
        countermobile.setAttribute('hidden', '');
      }
    }
  }

  function refreshCartData() {
    $.ajax({
      url: baseUrl + 'common/cart/info',
      type: 'get',
      dataType: 'html',
      success: function (html) {
        const list = document.querySelector('[data-minicart-list]');
        const cartlist = document.querySelector('[data-minicart-body]');
        const hint = document.querySelector('[data-minicart-hint]');

        if (list) {
          list.innerHTML = html;
          list.hidden = html.trim().length === 0;
        }

        const temp = document.createElement('div');
        temp.innerHTML = html;

        let totalQty = 0;
        temp.querySelectorAll('.zpm-minicart__item-calc__numb em').forEach(function (em) {
          totalQty += parseInt(em.textContent.replace(/\D/g, ''), 10) || 0;
        });

        if (totalQty === 0) {
          if (cartlist) cartlist.hidden = true;
          if (hint) hint.hidden = false;
        } else {
          if (cartlist) cartlist.hidden = false;
          if (hint) hint.hidden = true;
        }

        updateHeaderCounter(totalQty);
      }
    });
  }

  function setQty(id, qty, isManualClick) {
    const oldQty = state.get(id) || 0;
    const newQty = Math.max(0, Math.min(MAX_QTY, parseInt(qty, 10) || 0));

    state.set(id, newQty);
    syncAllUI(id);

    if (isManualClick) {
      const diff = newQty - oldQty;

      if (diff !== 0) {
        totalCartItems += diff;
        updateHeaderCounter();

        $.ajax({
          url: baseUrl + 'checkout/cart/add',
          type: 'post',
          data: { product_id: id, quantity: diff },
          dataType: 'json',
          success: function () {
            refreshCartData();
          }
        });
      }
    }
  }

  function syncAllUI(productId) {
    const qty = state.get(productId) || 0;

    document
      .querySelectorAll('.product-card__actions[data-product-id="' + productId + '"]')
      .forEach(function (el) {
        syncCardActions(el, qty);
      });

    document
      .querySelectorAll('.product-hero__actions[data-product-id="' + productId + '"]')
      .forEach(function (el) {
        syncPdpActions(el, qty);
      });
  }

  function init() {
    const counter = document.getElementById('cartcounter');

    if (counter) {
      totalCartItems = parseInt(counter.textContent, 10) || 0;
    }

    document.querySelectorAll('[data-product-id]').forEach(function (el) {
      const id = el.getAttribute('data-product-id');
      if (!id) return;

      const valEl = el.querySelector('[data-qty-value]');
      const currentQty = valEl ? parseInt(valEl.textContent, 10) || 0 : 0;

      state.set(id, currentQty);
      syncAllUI(id);
    });

    updateHeaderCounter();
    refreshCartData();
  }

  document.addEventListener('click', function (e) {
    const container = e.target.closest('[data-product-id]');

    if (container) {
      const id = container.getAttribute('data-product-id');
      const qty = state.get(id) || 0;
      const isPdp = container.hasAttribute('data-cart-pdp');

      if (e.target.closest('[data-cart-add]')) {
        e.preventDefault();

        if (isPdp && qty > 0) {
          window.location.href = CART_URL;
          return;
        }

        setQty(id, qty + 1, true);
        return;
      }

      if (e.target.closest('[data-qty-plus]')) {
        e.preventDefault();
        setQty(id, qty + 1, true);
        return;
      }

      if (e.target.closest('[data-qty-minus]')) {
        e.preventDefault();

        if (qty > 0) {
          setQty(id, qty - 1, true);
        }

        return;
      }
    }

    const deleteBtn = e.target.closest('.zpm-cart_item_delete');
    if (deleteBtn) {
      e.preventDefault();

      const cartId = deleteBtn.getAttribute('data-cart-id');

      $.ajax({
        url: baseUrl + 'checkout/cart/remove',
        type: 'post',
        data: { key: cartId },
        dataType: 'json',
        success: function () {
          location.reload();
        },
        error: function (xhr) {
          console.error('Ошибка удаления:', xhr.responseText);
        }
      });
    }
  });

  init();
})();







/* ==========================================================
   COPY TO CLIPBOARD + TOOLTIP (marketplace-style)
========================================================== */

(function () {
  const TIP_TEXT = 'Артикул скопирован!';
  const SHOW_MS = 3000;

  function showTip(el) {
    el.setAttribute('data-copy-tip', TIP_TEXT);

    // перезапуск анимации (если кликать быстро)
    el.classList.remove('is-copied');
    // eslint-disable-next-line no-unused-expressions
    el.offsetHeight;

    el.classList.add('is-copied');

    clearTimeout(el._copyT);
    el._copyT = setTimeout(() => {
      el.classList.remove('is-copied');
    }, SHOW_MS);
  }

  async function copyText(text) {
    // modern way
    if (navigator.clipboard && typeof navigator.clipboard.writeText === 'function') {
      await navigator.clipboard.writeText(text);
      return;
    }

    // fallback
    const ta = document.createElement('textarea');
    ta.value = text;
    ta.setAttribute('readonly', '');
    ta.style.position = 'fixed';
    ta.style.left = '-9999px';
    ta.style.top = '0';
    document.body.appendChild(ta);
    ta.select();
    document.execCommand('copy');
    document.body.removeChild(ta);
  }

  document.addEventListener('click', async (e) => {
    const el = e.target.closest('[data-copy]');
    if (!el) return;

    const text = (el.textContent || '').trim();
    if (!text) return;

    try {
      await copyText(text);
      showTip(el);
    } catch (err) {
      // если копирование запрещено — всё равно покажем подсказку (UX)
      showTip(el);
    }
  });
})();









/* ==========================================================
   FAVORITES / COMPARE
   tooltip + active toggle
   Real popup block version
========================================================== */
(function () {
  const SHOW_TIME = 3000;
  const TITLE_FAV_ADD = 'Добавить в избранное';
  const TITLE_FAV_REMOVE = 'Удалить из избранного';
  const TITLE_COMPARE_ADD = 'Добавить к сравнению';
  const TITLE_COMPARE_REMOVE = 'Удалить из сравнения';
  const ACTION_SELECTOR = '[data-fav-toggle], [data-compare-toggle]';

  function updateActionTitle(btn) {
    const isFav = btn.hasAttribute('data-fav-toggle');
    const isActive = btn.classList.contains('active');
    let title;

    if (isFav) {
      title = isActive ? TITLE_FAV_REMOVE : TITLE_FAV_ADD;
    } else {
      title = isActive ? TITLE_COMPARE_REMOVE : TITLE_COMPARE_ADD;
    }

    btn.setAttribute('title', title);
  }

  function initActionTitles() {
    document.querySelectorAll(ACTION_SELECTOR).forEach(updateActionTitle);
  }

  function hideAllActionTips(exceptEl) {
    document.querySelectorAll(ACTION_SELECTOR).forEach((node) => {
      if (node === exceptEl) return;
      node.classList.remove('is-tip', 'is-remove');
      clearTimeout(node._tipTimer);
    });
  }

  function showTip(el, text, isRemove) {
    hideAllActionTips(el);

    const body = el.querySelector('.zpm-tip__body');
    if (body) body.textContent = text;

    el.classList.remove('is-tip', 'is-remove');

    if (isRemove) {
      el.classList.add('is-remove');
    }

    // restart animation
    // eslint-disable-next-line no-unused-expressions
    el.offsetHeight;

    el.classList.add('is-tip');

    clearTimeout(el._tipTimer);
    el._tipTimer = setTimeout(() => {
      el.classList.remove('is-tip', 'is-remove');
    }, SHOW_TIME);
  }

  function sendRequest(url, productId) {
    return fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: 'product_id=' + productId
    }).then(r => r.json());
  }

  function updateWishlistTotal(total) {
  const el = document.getElementById('wishcounter');
  if (!el) return;

  const count = parseInt(total, 10) || 0;

  el.textContent = count;

  if (count > 0) {
    el.removeAttribute('hidden');
  } else {
    el.setAttribute('hidden', '');
  }
}

function updateCompareTotal(total) {
  const el = document.getElementById('comparecounter');
  if (!el) return;

  console.log(total)

  const count = parseInt(total, 10) || 0;

  el.textContent = count;

  if (count > 0) {
    el.removeAttribute('hidden');
  } else {
    el.setAttribute('hidden', '');
  }
}

document.addEventListener('click', function (e) {

  const btn = e.target.closest('[data-fav-toggle], [data-compare-toggle]');
  if (!btn) return;

  const productId = btn.dataset.productid;
  const isFav = btn.hasAttribute('data-fav-toggle');
  const isActive = btn.classList.contains('active');

  let url;

  if (isFav) {
    url = isActive
      ? '/index.php?route=account/wishlist/remove'
      : '/index.php?route=account/wishlist/add';
  } else {
    url = isActive
      ? '/index.php?route=product/compare/remove'
      : '/index.php?route=product/compare/add';
  }

  sendRequest(url, productId).then(json => {



    if (json.redirect) {
      location = json.redirect;
      return;
    }

    if (isFav && json.total != null) {
      updateWishlistTotal(json.total);
    }

    if (!isFav && json.total != null) {
      updateCompareTotal(json.total);
    }

  });

  const newState = btn.classList.toggle('active');
  updateActionTitle(btn);
  showTip(btn, newState ? 'Добавлено' : 'Удалено', !newState);

  });

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initActionTitles);
  } else {
    initActionTitles();
  }
})();













// Desktop catalog mega menu (toggle + tabs) — stable
(function () {
  const btn = document.querySelector('[data-catalog-open]');
  const catalog = document.querySelector('[data-catalog]');
  if (!btn || !catalog) return;

  const catBtns = catalog.querySelectorAll('[data-cat-btn]');
  const panes = catalog.querySelectorAll('[data-cat-pane]');

  // tabs
  catBtns.forEach((b) => {
    b.addEventListener('click', () => {
      const key = b.getAttribute('data-cat');

      catBtns.forEach((x) => x.classList.toggle('is-active', x === b));
      panes.forEach((p) =>
        p.classList.toggle('is-active', p.getAttribute('data-cat-pane') === key)
      );
    });
  });
})();

























(function () {
  function onReady(fn) {
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", fn);
    } else {
      fn();
    }
  }

  function debounce(func, timeout = 800) {
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => {
      func.apply(this, args);
    }, timeout);
  };
}

  const debouncedUpdate = debounce((root) => {
    updateProducts(root);
  }, 800);

  function reinitImages(container) {
  // 1. Попытка вызвать стандартный триггер скролла
  window.dispatchEvent(new Event('scroll'));

  // 2. Если используется конкретная библиотека (например, LazyLoad)
  if (typeof LazyLoad !== 'undefined') {
    const lazy = new LazyLoad();
    lazy.update();
  }
}

  function getPageScrollOffset() {
    var isMobile = window.innerWidth <= 1024;
    var stickyEl = isMobile
      ? document.querySelector('[data-header-mobilebar]')
      : document.querySelector('[data-header-sticky]');

    if (stickyEl) {
      var measured = Math.ceil(stickyEl.getBoundingClientRect().height);
      if (measured > 0) {
        return measured;
      }
    }

    var cssVal = getComputedStyle(document.documentElement)
      .getPropertyValue('--header-posotopn-and-size')
      .trim();
    var parsed = parseInt(cssVal, 10);
    if (!isNaN(parsed) && parsed > 0) {
      return parsed;
    }

    return isMobile ? 100 : 140;
  }

  function getPageScrollTop() {
    if (document.body.classList.contains('is-scroll-locked')) {
      var top = parseInt(document.body.style.top || '0', 10) || 0;
      return Math.abs(top);
    }

    return (
      window.pageYOffset ||
      document.documentElement.scrollTop ||
      0
    );
  }

  function scrollToCategorySection() {
    var target =
      document.querySelector('.page--category section.category') ||
      document.querySelector('section.category');
    if (!target) return;

    if (document.documentElement.classList.contains('is-filter-open')) {
      var closeBtn = document.querySelector('[data-filter-close]');
      if (closeBtn) closeBtn.click();
    }

    var offset = 0;
    var scrollTop = getPageScrollTop();
    var targetTop =
      target.getBoundingClientRect().top +
      scrollTop -
      offset;

    window.scrollTo({
      top: Math.max(0, targetTop),
      behavior: 'smooth'
    });
  }

  /**
 * Основная функция обновления товаров
 */
function updateProducts(root) {
  const form = root.querySelector("[data-filters-form]");
  const grid = document.querySelector(".category__grid");
  if (!form || !grid) return;
  const currentParams = new URLSearchParams(window.location.search);
  const stateText = getReadableState(form);
  //currentParams.delete("page");
  if (stateText) {
    currentParams.set("filters", stateText);
  } else {
    currentParams.delete("filters");
  }
  const queryString = currentParams.toString();
  const fetchUrl = window.location.pathname + (queryString ? "?" + queryString : "");

  grid.style.opacity = "0.5";
  grid.style.pointerEvents = "none";

  fetch(fetchUrl)
    .then(response => {
      if (!response.ok) throw new Error('Network response was not ok');
      return response.text();
    })
    .then(html => {
      const parser = new DOMParser();
      const doc = parser.parseFromString(html, "text/html");

      const newGrid = doc.querySelector(".category__grid");
      if (newGrid) {
        grid.innerHTML = newGrid.innerHTML;
        // Если у вас есть функции ленивой загрузки картинок, вызываем тут
        if (typeof reinitImages === 'function') reinitImages(grid);
      }

      // 2. Работаем с пагинацией
      const oldPagination = document.querySelector(".pagination");
      const newPagination = doc.querySelector(".pagination");

      if (newPagination) {
        // Если в новом HTML пагинация есть
        if (oldPagination) {
          // Если старая была — просто заменяем (или обновляем innerHTML)
          oldPagination.outerHTML = newPagination.outerHTML;
        } else {
          // Если старой не было — вставляем новую СРАЗУ ПОСЛЕ сетки товаров
          grid.insertAdjacentHTML('afterend', newPagination.outerHTML);
        }
      } else {
        // Если в новом HTML пагинации нет (товаров мало)
        if (oldPagination) {
          oldPagination.remove(); // Удаляем старую, если она была
        }
      }


      grid.style.opacity = "1";
      grid.style.pointerEvents = "all";

      scrollToCategorySection();

      initPaginationAJAX(root);
    })
    .catch(err => {
      console.error("Ошибка загрузки товаров:", err);
      grid.style.opacity = "1";
      grid.style.pointerEvents = "all";
    });
}

/**
 * Перехват кликов по пагинации
 */
function initPaginationAJAX(root) {
  const pagination = document.querySelector(".pagination");
  if (!pagination) return;

  pagination.querySelectorAll("a").forEach(link => {
    link.addEventListener("click", (e) => {
      e.preventDefault();

      const url = new URL(link.href);
      const page = url.searchParams.get("page");

      // Добавляем параметр страницы в текущий URL браузера
      const currentUrl = new URL(window.location.href);
      if (page) {
        currentUrl.searchParams.set("page", page);
      } else {
        currentUrl.searchParams.delete("page");
      }

      window.history.replaceState(null, "", currentUrl.toString());


      updateProducts(root);
    });
  });
}

  function onlyDigits(str) {
    return (str || "").toString().replace(/[^\d]/g, "");
  }

  function fmtInt(n) {
    const s = String(Math.max(0, Number(n) || 0));
    return s.replace(/\B(?=(\d{3})+(?!\d))/g, " ");
  }

  function clamp(v, min, max) {
    v = Number(v) || 0;
    return Math.min(max, Math.max(min, v));
  }

  function syncChoiceClasses(root) {
    root.querySelectorAll(".flt__check").forEach((label) => {
      const input = label.querySelector(".flt__check-input");
      label.classList.toggle("active", !!(input && input.checked));
    });

    root.querySelectorAll(".flt__switch").forEach((label) => {
      const input = label.querySelector(".flt__switch-input");
      label.classList.toggle("active", !!(input && input.checked));
    });

    updateGroupResetVisibility(root);
  }

  function initAccordions(root) {
    root.querySelectorAll("[data-acc]").forEach((group) => {
      const btn = group.querySelector("[data-acc-btn]");
      const panel = group.querySelector("[data-acc-panel]");
      if (!btn || !panel) return;

      btn.addEventListener("click", () => {
        const isOpen = btn.getAttribute("aria-expanded") === "true";
        btn.setAttribute("aria-expanded", String(!isOpen));

        if (isOpen) {
          panel.hidden = true;
          group.classList.remove("is-open");
        } else {
          panel.hidden = false;
          group.classList.add("is-open");
        }
      });
    });
  }

  function initShowMore(root) {
    root.querySelectorAll("[data-list]").forEach((list) => {
      const limit = Number(list.getAttribute("data-list-limit")) || 5;
      const wrap = list.parentElement;
      const toggle = wrap ? wrap.querySelector("[data-list-toggle]") : null;
      if (!toggle) return;

      const items = Array.from(list.querySelectorAll(".flt__check"));

      function getVisibleItems() {
        return items.filter((item) => item.getAttribute("data-search-hidden") !== "true");
      }

      function render() {
        const collapsed = list.getAttribute("data-list-collapsed") === "true";
        const visibleItems = getVisibleItems();

        visibleItems.forEach((item, index) => {
          item.hidden = collapsed && index >= limit;
        });

        items.forEach((item) => {
          if (item.getAttribute("data-search-hidden") === "true") {
            item.hidden = true;
          }
        });

        const needToggle = visibleItems.length > limit;
        toggle.hidden = !needToggle;

        if (needToggle) {
          toggle.textContent = collapsed ? "Показать все" : "Свернуть";
        }
      }

      list.__renderShowMore = render;

      render();

      toggle.addEventListener("click", () => {
        const collapsed = list.getAttribute("data-list-collapsed") === "true";
        list.setAttribute("data-list-collapsed", collapsed ? "false" : "true");
        render();
      });
    });
  }

  function bindOneRange(rangeRoot) {
    const fromInput = rangeRoot.querySelector("[data-range-from]");
    const toInput = rangeRoot.querySelector("[data-range-to]");
    const minRange = rangeRoot.querySelector("[data-range-min]");
    const maxRange = rangeRoot.querySelector("[data-range-max]");
    const progress = rangeRoot.querySelector("[data-range-progress]");
    const form = rangeRoot.closest("[data-filters-form]");

    if (!fromInput || !toInput || !minRange || !maxRange) return;

    const min = Number(minRange.min);
    const max = Number(maxRange.max);
    const step = Number(minRange.step) || 1;

    function updateProgress(a, b) {
      if (!progress) return;

      const left = ((a - min) / (max - min)) * 100;
      const right = ((b - min) / (max - min)) * 100;

      progress.style.left = left + "%";
      progress.style.width = Math.max(0, right - left) + "%";
    }

    function normalizePair(a, b) {
      let from = clamp(a, min, max);
      let to = clamp(b, min, max);

      if (from > to) {
        const tmp = from;
        from = to;
        to = tmp;
      }

      from = Math.round(from / step) * step;
      to = Math.round(to / step) * step;

      return { from: clamp(from, min, max), to: clamp(to, min, max) };
    }

    function syncFromRanges() {
      const pair = normalizePair(minRange.value, maxRange.value);

      minRange.value = String(pair.from);
      maxRange.value = String(pair.to);

      fromInput.value = fmtInt(pair.from);
      toInput.value = fmtInt(pair.to);

      updateProgress(pair.from, pair.to);
    }

    function syncFromInputs() {
      const pair = normalizePair(onlyDigits(fromInput.value), onlyDigits(toInput.value));

      minRange.value = String(pair.from);
      maxRange.value = String(pair.to);

      fromInput.value = fmtInt(pair.from);
      toInput.value = fmtInt(pair.to);

      updateProgress(pair.from, pair.to);
      if (form) updateBrowserUrl(form);
    }

        // А для самих ползунков (range) добавим обработчик "change" (срабатывает, когда отпустили мышку)
    minRange.addEventListener("change", () => { if (form) updateBrowserUrl(form); });
    maxRange.addEventListener("change", () => { if (form) updateBrowserUrl(form); });

    function handleInputTyping(inputEl) {
      const raw = onlyDigits(inputEl.value);
      inputEl.value = raw ? fmtInt(raw) : "";
    }

    minRange.addEventListener("input", syncFromRanges);
    maxRange.addEventListener("input", syncFromRanges);

    fromInput.addEventListener("input", function () {
      handleInputTyping(fromInput);
    });

    toInput.addEventListener("input", function () {
      handleInputTyping(toInput);
    });

    fromInput.addEventListener("blur", syncFromInputs);
    toInput.addEventListener("blur", syncFromInputs);

    fromInput.addEventListener("change", syncFromInputs);
    toInput.addEventListener("change", syncFromInputs);

    syncFromRanges();
  }

  function initRanges(root) {
    root.querySelectorAll("[data-range]").forEach(bindOneRange);
  }

  function initBrandSearch(root) {
    root.querySelectorAll("[data-filter-search]").forEach((input) => {
      const scope = input.closest("[data-acc-panel]") || input.parentElement;
      if (!scope) return;

      const list = scope.querySelector("[data-list]");
      if (!list) return;

      const items = Array.from(list.querySelectorAll(".flt__check"));

      input.addEventListener("input", () => {
        const q = (input.value || "").trim().toLowerCase();

        items.forEach((item) => {
          const text = (item.textContent || "").trim().toLowerCase();
          const isHiddenBySearch = q ? !text.includes(q) : false;
          item.setAttribute("data-search-hidden", isHiddenBySearch ? "true" : "false");
        });

        if (typeof list.__renderShowMore === "function") {
          list.__renderShowMore();
        }
      });
    });
  }

  function initSwitches(root) {
    const form = root.querySelector("[data-filters-form]");
    root.querySelectorAll(".flt__switch-input").forEach((input) => {
      input.addEventListener("change", () => {
        const groupName = input.getAttribute("data-switch-group");

        if (groupName && input.checked) {
          root
            .querySelectorAll('.flt__switch-input[data-switch-group="' + groupName + '"]')
            .forEach((other) => {
              if (other !== input) other.checked = false;
            });
        }

        syncChoiceClasses(root);
        if (form) updateBrowserUrl(form);
      });
    });
  }

  function initChecks(root) {
    const form = root.querySelector("[data-filters-form]");
    root.querySelectorAll(".flt__check-input").forEach((input) => {
      input.addEventListener("change", () => {
        syncChoiceClasses(root);
        if (form) updateBrowserUrl(form);
      });
    });
  }

  function collectFormState(form) {
    const fd = new FormData(form);
    const params = new URLSearchParams();

    for (const pair of fd.entries()) {
      const key = pair[0];
      const value = pair[1];

      if (value === "" || value == null) continue;
      params.append(key, value);
    }

    return params.toString();
  }

  function getReadableState(form) {
  const state = collectFormState(form);
  if (!state) return "";

  // Декодируем только структурные символы, чтобы URL оставался читаемым
  return decodeURIComponent(state)
    .replace(/%5B/g, "[")
    .replace(/%5D/g, "]")
    .replace(/\+/g, " ")
    .replace(/&/g, ";"); // Заменяем плюсы на пробелы для красоты цен
}


  // 1. Вспомогательная функция для формирования полного URL
function getFullFilterUrl(form) {
  const stateText = getReadableState(form);
  const path = window.location.pathname.replace(/^\//, "");
  const baseUrlClean = typeof baseurl !== 'undefined' ? baseurl : window.location.origin + "/";
  const fullPath = baseUrlClean + path;

  return stateText ? fullPath + "?filters=" + stateText : fullPath;
}

 // 2. Обновленная функция initCopyLink
function initCopyLink(root) {
  const form = root.querySelector("[data-filters-form]");
  const btn = root.querySelector("[data-filter-copy]");
  if (!form || !btn) return;

  async function copyStateLink() {
    // Используем новую логику формирования полного пути
    const url = getFullFilterUrl(form);

    try {
      if (navigator.clipboard && navigator.clipboard.writeText) {
        await navigator.clipboard.writeText(url);
      } else {
        const ta = document.createElement("textarea");
        ta.value = url;
        document.body.appendChild(ta);
        ta.select();
        document.execCommand("copy");
        ta.remove();
      }

      const oldText = btn.textContent;
      btn.textContent = "Ссылка скопирована";
      btn.classList.add("is-done");

      setTimeout(() => {
        btn.textContent = oldText;
        btn.classList.remove("is-done");
      }, 1800);
    } catch (err) {
      btn.textContent = "Не удалось скопировать";
      setTimeout(() => {
        btn.textContent = "Копировать ссылку";
      }, 1800);
    }
  }

  btn.addEventListener("click", copyStateLink);
}

function updateBrowserUrl(form) {
  const stateText = getReadableState(form);
  const newUrl = stateText
    ? window.location.pathname + "?filters=" + stateText
    : window.location.pathname;

  window.history.replaceState(null, "", newUrl);
  // Вызываем обновление товаров
  const root = form.closest("[data-filters]");
  debouncedUpdate(root);
}



  function updateGroupResetVisibility(root) {
    root.querySelectorAll("[data-filter-group-reset]").forEach((btn) => {
      const group = btn.closest("[data-acc].flt__group");
      if (!group) return;
      const panel = group.querySelector("[data-acc-panel]");
      if (!panel) return;
      const hasChecked = panel.querySelector(".flt__check-input:checked") !== null;
      btn.hidden = !hasChecked;
    });
  }

  function initGroupReset(root) {
    const form = root.querySelector("[data-filters-form]");
    if (!form) return;

    root.querySelectorAll("[data-filter-group-reset]").forEach((btn) => {
      btn.addEventListener("click", (e) => {
        e.preventDefault();
        e.stopPropagation();

        const group = btn.closest("[data-acc].flt__group");
        if (!group) return;
        const panel = group.querySelector("[data-acc-panel]");
        if (!panel) return;

        panel.querySelectorAll(".flt__check-input").forEach((input) => {
          input.checked = false;
          const label = input.closest(".flt__check");
          if (label) label.classList.remove("active");
        });

        syncChoiceClasses(root);
        updateBrowserUrl(form);
      });
    });
  }
 function initReset(root) {
  const form = root.querySelector("[data-filters-form]");
  const resetBtn = root.querySelector("[data-filter-reset]");
  if (!form || !resetBtn) return;

  resetBtn.addEventListener("click", (e) => {
    e.preventDefault();

    // 1. Сброс формы
    form.reset();

    root.querySelectorAll(".flt__check-input").forEach((input) => {
      input.checked = false; // Снимаем галочку
      const label = input.closest(".flt__check");
      if (label) label.classList.remove("active"); // Убираем подсветку
    });

    // 2. Сброс ползунков
    root.querySelectorAll("[data-range]").forEach((rangeRoot) => {
      const minRange = rangeRoot.querySelector("[data-range-min]");
      const maxRange = rangeRoot.querySelector("[data-range-max]");
      const fromInput = rangeRoot.querySelector("[data-range-from]");
      const toInput = rangeRoot.querySelector("[data-range-to]");
      const progress = rangeRoot.querySelector("[data-range-progress]");

      if (minRange && maxRange) {
        minRange.value = minRange.min;
        maxRange.value = maxRange.max;
        if (fromInput) fromInput.value = fmtInt(minRange.min);
        if (toInput) toInput.value = fmtInt(maxRange.max);
        if (progress) {
          progress.style.left = "0%";
          progress.style.width = "100%";
        }
      }
    });

    // 3. Сброс списков и поиска
    root.querySelectorAll("[data-list]").forEach((list) => {
      list.setAttribute("data-list-collapsed", "true");
      list.querySelectorAll(".flt__check").forEach((item) => {
        item.setAttribute("data-search-hidden", "false");
      });
      if (typeof list.__renderShowMore === "function") {
        list.__renderShowMore();
      }
    });

    // Сброс свитчей (переключателей)
  root.querySelectorAll("[data-switch-label]").forEach((label) => {
    const input = label.querySelector(".flt__switch-input");

    if (input) {
      // 1. Снимаем галочку (если нужно сбросить в false независимо от исходного HTML)
      input.checked = false;

      // 2. Убираем активный класс у обертки
      label.classList.remove("active");
    }
  });

    root.querySelectorAll("[data-filter-search]").forEach((input) => {
      input.value = "";
    });

    // 4. Синхронизация классов
    syncChoiceClasses(root);

    // 5. Очистка URL
    window.history.replaceState(null, "", window.location.pathname);

    // 6. Обновление товаров (ПЕРЕДАЕМ root)
    if (typeof updateProducts === 'function') {
        updateProducts(root);
    }
  });
}
  onReady(function () {
    const root = document.querySelector("[data-filters]");
    if (!root) return;

    initAccordions(root);
    initShowMore(root);
    initRanges(root);
    initBrandSearch(root);
    initSwitches(root);
    initChecks(root);
    initCopyLink(root);
    initReset(root);
    initGroupReset(root);
    syncChoiceClasses(root);
    initPaginationAJAX(root);
  });
})();





/* ==========================================================
   COPY ARTICLE
   tooltip on existing ZPM tip system
========================================================== */
(function () {
  const SHOW_TIME = 2000;

  function fallbackCopy(text) {
    const ta = document.createElement('textarea');
    ta.value = text;
    ta.setAttribute('readonly', '');
    ta.style.position = 'fixed';
    ta.style.left = '-9999px';
    ta.style.top = '0';
    document.body.appendChild(ta);
    ta.focus();
    ta.select();
    document.execCommand('copy');
    document.body.removeChild(ta);
  }

  async function copyText(text) {
    if (navigator.clipboard && typeof navigator.clipboard.writeText === 'function') {
      await navigator.clipboard.writeText(text);
      return;
    }

    fallbackCopy(text);
  }

  function showTip(el, text) {
    const body = el.querySelector('.zpm-tip__body');
    if (body) body.textContent = text;

    el.classList.remove('is-tip', 'is-remove');

    // restart animation
    // eslint-disable-next-line no-unused-expressions
    el.offsetHeight;

    el.classList.add('is-tip');

    clearTimeout(el._tipTimer);
    el._tipTimer = setTimeout(() => {
      el.classList.remove('is-tip', 'is-remove');
    }, SHOW_TIME);
  }

  function getCopyText(el) {
    const valueEl = el.querySelector('.zpm-copy__value');
    if (valueEl) return (valueEl.textContent || '').trim();
    return (el.textContent || '').trim();
  }

  document.addEventListener('click', async function (e) {
    const copy = e.target.closest('[data-copy]');
    if (!copy) return;

    e.preventDefault();

    const text = getCopyText(copy);
    if (!text) return;

    try {
      await copyText(text);
      showTip(copy, 'Артикул скопирован!');
    } catch (err) {
      showTip(copy, 'Артикул скопирован!');
    }
  });
})();








/* ==========================================================
   INTEGRATED CART PAGE LOGIC
   - Совмещает дизайн и реальную работу с OpenCart 3
========================================================== */
(function () {
  const MAX_QTY = 99;
  const MIN_QTY = 1;
  const baseUrl = (typeof OC_CART_CONFIG !== 'undefined') ? OC_CART_CONFIG.baseUrl : '/index.php?route=';

  let updateTimer; // Для задержки отправки запроса

  function clamp(n, min, max) {
    return Math.max(min, Math.min(max, n));
  }

  // Обновление на сервере (AJAX)
 function sendUpdateToServer(cartId, qty) {
    clearTimeout(updateTimer);

    updateTimer = setTimeout(() => {
      console.log('Отправка обновления...', cartId, qty);

      $.ajax({
        url: baseUrl + 'checkout/cart/edit',
        type: 'post',
        // Отправляем как строку формы, это самый стабильный вариант для OC3
        data: `quantity[${cartId}]=${qty}`,
        // dataType: 'json', <-- УДАЛЯЕМ ЭТО, так как сервер шлет редирект/html
        beforeSend: function() {
          $('body').css('opacity', '0.5'); // Даем понять пользователю, что работаем
        },
        complete: function() {
          // Нам неважно, success это или error (из-за 302).
          // Если запрос дошел и количество поменялось — просто обновляем страницу.
          location.reload();
        }
      });
    }, 600);
  }

  function setItemQty(item, qty, shouldUpdateServer = false) {
    const valEl = item.querySelector('[data-cart-item-qty-value]');
    const minusBtn = item.querySelector('[data-cart-item-qty-minus]');
    const plusBtn = item.querySelector('[data-cart-item-qty-plus]');
    const cartId = item.getAttribute('data-cart-id');

    const nextQty = clamp(qty, MIN_QTY, MAX_QTY);

    if (valEl) valEl.textContent = String(nextQty);
    if (minusBtn) minusBtn.disabled = nextQty <= MIN_QTY;
    if (plusBtn) plusBtn.disabled = nextQty >= MAX_QTY;

    item.setAttribute('data-cart-item-qty', String(nextQty));

    if (shouldUpdateServer && cartId) {
      sendUpdateToServer(cartId, nextQty);
    }
  }

  // Слушатель кликов
  document.addEventListener('click', function (e) {
    // 1. Плюс / Минус
    const btn = e.target.closest('[data-cart-item-qty-plus], [data-cart-item-qty-minus]');
    if (btn) {
      e.preventDefault();
      const item = btn.closest('[data-cart-item]');
      if (!item) return;

      const currentQty = parseInt(item.getAttribute('data-cart-item-qty'), 10) || MIN_QTY;
      const isPlus = btn.hasAttribute('data-cart-item-qty-plus');

      const newQty = isPlus ? currentQty + 1 : currentQty - 1;

      if (newQty >= MIN_QTY && newQty <= MAX_QTY) {
        setItemQty(item, newQty, true);
      }
      return;
    }

    // 2. Удаление (Крестик)
    const deleteBtn = e.target.closest('.zpm-cart_item_delete');
    if (deleteBtn) {
      e.preventDefault();
      const cartId = deleteBtn.getAttribute('data-cart-id');

      if (confirm('Удалить товар из корзины?')) {
        $.ajax({
          url: baseUrl + 'checkout/cart/remove',
          type: 'post',
          data: { key: cartId },
          dataType: 'json',
          success: function(json) {
            location.reload();
          }
        });
      }
    }
  });

  // Инициализация при загрузке
  function initCartPage() {
    document.querySelectorAll('[data-cart-item]').forEach(item => {
      const qty = parseInt(item.getAttribute('data-cart-item-qty'), 10) || MIN_QTY;
      setItemQty(item, qty, false);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initCartPage);
  } else {
    initCartPage();
  }
})();











/* ================================
   CHECKOUT AUTH SWITCHER & AJAX
================================ */
/* ================================
   CHECKOUT AUTH SWITCHER & AJAX
================================ */

(function () {
  function setPanelState(panel, isVisible) {
    if (!panel) return;
    panel.hidden = !isVisible;
    panel.classList.toggle('is-active', isVisible);
  }

  function setFieldsRequired(container, selector, isRequired) {
    if (!container) return;

    container.querySelectorAll(selector).forEach(function (field) {
      if (isRequired) {
        field.setAttribute('required', 'required');
      } else {
        field.removeAttribute('required');
      }
    });
  }

  function setPanelInputsEnabled(panel, enabled) {
    if (!panel) return;

    panel.querySelectorAll('input, select, textarea, button').forEach(function (field) {
      if (enabled) {
        if (field.hasAttribute('data-disabled-by-checkout')) {
          field.disabled = false;
          field.removeAttribute('data-disabled-by-checkout');
        }
      } else {
        if (!field.disabled) {
          field.disabled = true;
          field.setAttribute('data-disabled-by-checkout', 'true');
        }
      }
    });
  }

  function activateTab(root, type) {
    root.querySelectorAll('[data-checkout-tab]').forEach(function (btn) {
      btn.classList.toggle('is-active', btn.getAttribute('data-checkout-tab') === type);
    });

    root.querySelectorAll('[data-checkout-tab-text]').forEach(function (item) {
      var isActive = item.getAttribute('data-checkout-tab-text') === type;
      setPanelState(item, isActive);
    });
  }

  function initCheckout() {
    document.querySelectorAll('[data-checkout]').forEach(function (root) {
      var isLogged = root.getAttribute('data-is-logged') === 'true';

      var tabGuest = root.querySelector('[data-checkout-tab="guest"]');
      var tabLogin = root.querySelector('[data-checkout-tab="login"]');
      var tabRegister = root.querySelector('[data-checkout-tab="register"]');

      var guestPanel = root.querySelector('[data-checkout-panel="guest"]');
      var loginPanel = root.querySelector('[data-checkout-panel="login"]');
      var registerPanel = root.querySelector('[data-checkout-panel="register"]');

      var authSuccessPanel = root.querySelector('[data-checkout-auth-success]');
      var orderPanel = root.querySelector('[data-checkout-order-panel]');

      var loginForm = root.querySelector('[data-checkout-login-form]');
      var loginInput = root.querySelector('[data-checkout-login-input]');
      var mainCheckoutForm = root.querySelector('[data-checkout-main-form]');

      var deliveryTypeInputs = root.querySelectorAll('input[name="delivery_type"]');
      var deliveryBlock = root.querySelector('[data-delivery-block]');
      var deliveryDetailsBtn = root.querySelector('[data-delivery-details-toggle]');
      var deliveryDetailsBlock = root.querySelector('[data-delivery-details]');

      function disableAllMainVariants() {
        setPanelInputsEnabled(guestPanel, false);
        setPanelInputsEnabled(loginPanel, false);
        setPanelInputsEnabled(registerPanel, false);
        setPanelInputsEnabled(orderPanel, false);
      }

      function syncDeliveryBlock() {
        if (!deliveryBlock) return;

        var selected = root.querySelector('input[name="delivery_type"]:checked');
        var isDelivery = !!(selected && selected.value === 'delivery');

        setPanelState(deliveryBlock, isDelivery);

        if (!isDelivery) {
          setPanelState(deliveryDetailsBlock, false);
        }
      }

      function showGuestMode() {
        activateTab(root, 'guest');

        setPanelState(loginPanel, false);
        setPanelState(registerPanel, false);
        setPanelState(authSuccessPanel, false);
        setPanelState(guestPanel, true);
        setPanelState(orderPanel, true);

        disableAllMainVariants();
        setPanelInputsEnabled(guestPanel, true);
        setPanelInputsEnabled(orderPanel, true);

        setFieldsRequired(guestPanel, '[data-base-required]', true);
        setFieldsRequired(registerPanel, '[data-register-required]', false);

        syncDeliveryBlock();
      }

      function showLoginMode() {
        activateTab(root, 'login');

        setPanelState(guestPanel, false);
        setPanelState(registerPanel, false);
        setPanelState(authSuccessPanel, false);
        setPanelState(loginPanel, true);
        setPanelState(orderPanel, false);

        disableAllMainVariants();
        setPanelInputsEnabled(loginPanel, true);

        setFieldsRequired(guestPanel, '[data-base-required]', false);
        setFieldsRequired(registerPanel, '[data-register-required]', false);
      }

      function showRegisterMode() {
        activateTab(root, 'register');

        setPanelState(guestPanel, false);
        setPanelState(loginPanel, false);
        setPanelState(authSuccessPanel, false);
        setPanelState(registerPanel, true);
        setPanelState(orderPanel, true);

        disableAllMainVariants();
        setPanelInputsEnabled(registerPanel, true);
        setPanelInputsEnabled(orderPanel, true);

        setFieldsRequired(guestPanel, '[data-base-required]', false);
        setFieldsRequired(registerPanel, '[data-register-required]', true);

        syncDeliveryBlock();
      }

      if (tabGuest) {
        tabGuest.addEventListener('click', function (e) {
          e.preventDefault();
          showGuestMode();
        });
      }

      if (tabLogin) {
        tabLogin.addEventListener('click', function (e) {
          e.preventDefault();
          showLoginMode();
        });
      }

      if (tabRegister) {
        tabRegister.addEventListener('click', function (e) {
          e.preventDefault();
          showRegisterMode();
        });
      }

      if (deliveryTypeInputs.length) {
        deliveryTypeInputs.forEach(function (input) {
          input.addEventListener('change', syncDeliveryBlock);
        });
      }

      if (deliveryDetailsBtn && deliveryDetailsBlock) {
        deliveryDetailsBtn.addEventListener('click', function (e) {
          e.preventDefault();
          setPanelState(deliveryDetailsBlock, deliveryDetailsBlock.hidden);
        });
      }

if (loginForm) {
  var loginAlert = root.querySelector('[data-checkout-login-alert]');
  var loginAlertText = root.querySelector('[data-checkout-login-alert-text]');

  function clearLoginErrors() {
    loginForm.querySelectorAll('.has-error').forEach(function (el) {
      el.classList.remove('has-error');
    });

    loginForm.querySelectorAll('.zpm-form__error').forEach(function (el) {
      el.innerHTML = '';
    });

    if (loginAlert) {
      loginAlert.hidden = true;
      loginAlert.classList.remove('is-active');
    }

    if (loginAlertText) {
      loginAlertText.textContent = '';
    }
  }

  function showLoginError(message) {
    if (loginAlertText) {
      loginAlertText.textContent = message || 'Ошибка авторизации';
    }

    if (loginAlert) {
      loginAlert.hidden = false;
      loginAlert.classList.add('is-active');
    }
  }

  loginForm.addEventListener('submit', function (e) {
    e.preventDefault();

    clearLoginErrors();

    var emailInput = loginForm.querySelector('[name="email"]');
    var passwordInput = loginForm.querySelector('[name="password"]');

    if (emailInput && !emailInput.value.trim()) {
      var emailField = emailInput.closest('.zpm-form__field');
      if (emailField) {
        emailField.classList.add('has-error');
        var emailError = emailField.querySelector('.zpm-form__error');
        if (emailError) emailError.innerHTML = 'Введите e-mail или логин';
      }
    }

    if (passwordInput && !passwordInput.value.trim()) {
      var passwordField = passwordInput.closest('.zpm-form__field');
      if (passwordField) {
        passwordField.classList.add('has-error');
        var passwordError = passwordField.querySelector('.zpm-form__error');
        if (passwordError) passwordError.innerHTML = 'Введите пароль';
      }
    }

    if (
      (emailInput && !emailInput.value.trim()) ||
      (passwordInput && !passwordInput.value.trim())
    ) {
      return;
    }

    var formData = new FormData(loginForm);

    fetch('index.php?route=checkout/login/save', {
      method: 'POST',
      body: formData
    })
      .then(function (response) {
        return response.json();
      })
      .then(function (data) {
        if (data.error) {
          showLoginError(data.error.warning || 'Неверный e-mail / логин или пароль.');

          if (emailInput) {
            var emailField = emailInput.closest('.zpm-form__field');
            if (emailField) emailField.classList.add('has-error');
          }

          if (passwordInput) {
            var passwordField = passwordInput.closest('.zpm-form__field');
            if (passwordField) passwordField.classList.add('has-error');
          }
        } else if (data.redirect) {
          window.location.href = data.redirect;
        } else {
          window.location.reload();
        }
      })
      .catch(function (err) {
        console.error('Ошибка логина:', err);
        showLoginError('Не удалось выполнить вход. Попробуйте ещё раз.');
      });
  });
}

      if (mainCheckoutForm) {
        mainCheckoutForm.addEventListener('submit', function (e) {
          e.preventDefault();

          mainCheckoutForm.querySelectorAll('.text-danger').forEach(function (el) {
            el.remove();
          });

          mainCheckoutForm.querySelectorAll('.has-error').forEach(function (el) {
            el.classList.remove('has-error');
          });

          var formData = new FormData(mainCheckoutForm);

          fetch('index.php?route=checkout/checkout/save', {
            method: 'POST',
            body: formData
          })
            .then(function (response) {
              return response.json();
            })
            .then(function (data) {
              if (data.error) {
                for (var key in data.error) {
                  var input = mainCheckoutForm.querySelector('[name="' + key + '"]:not(:disabled)');

                  if (!input && key === 'privacy') {
                    input = mainCheckoutForm.querySelector('[name="privacy"]:not(:disabled)');
                  }

                  if (input) {
                    var parent = input.closest('.zpm-form__field, .zpm-form__agree') || input.parentElement;
                    parent.classList.add('has-error');

if (data.error) {
  for (var key in data.error) {
    var input = mainCheckoutForm.querySelector('[name="' + key + '"]:not(:disabled)');

    if (key === 'privacy') {
      input = mainCheckoutForm.querySelector('[name="privacy"]');
    }

    if (input) {
      var field = input.closest('.zpm-form__field, .zpm-form__agree');
      if (!field) continue;

      field.classList.add('has-error');

      var errorContainer = field.querySelector('.zpm-form__error');

      if (errorContainer) {
        errorContainer.innerHTML = data.error[key];
      }
    }
  }

  var firstError = mainCheckoutForm.querySelector('.has-error');
  if (firstError) {
    firstError.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }
}
                  }
                }

                var firstError = mainCheckoutForm.querySelector('.has-error');
                if (firstError) {
                  firstError.scrollIntoView({ behavior: 'smooth', block: 'center' });
                }
              } else if (data.redirect) {
                window.location.href = data.redirect;
              }
            })
            .catch(function (err) {
              console.error('Критическая ошибка при оформлении:', err);
              alert('Произошла ошибка при отправке данных. Попробуйте позже.');
            });
        });
      }

      if (isLogged) {
        activateTab(root, 'login');

        setPanelState(guestPanel, false);
        setPanelState(loginPanel, false);
        setPanelState(registerPanel, false);
        setPanelState(authSuccessPanel, true);
        setPanelState(orderPanel, true);

        disableAllMainVariants();
        setPanelInputsEnabled(orderPanel, true);

        setFieldsRequired(guestPanel, '[data-base-required]', false);
        setFieldsRequired(registerPanel, '[data-register-required]', false);

        syncDeliveryBlock();
      } else {
        showGuestMode();
      }
    });
  }

  document.addEventListener('DOMContentLoaded', initCheckout);
})();








  /* === СРАВНЕНИЕ ТОВАРОВ

                                                    */

document.addEventListener('DOMContentLoaded', () => {
  const compareTables = document.querySelectorAll('[data-compare-table]');

  if (!compareTables.length) return;

  compareTables.forEach((tableRoot) => {
    const section = tableRoot.closest('.compare-table');

    if (!section) return;

    const sliderEl = section.querySelector('[data-compare-slider]');
    const prevEl = section.querySelector('.compare-table__nav--prev');
    const nextEl = section.querySelector('.compare-table__nav--next');
    const scrollbarEl = section.querySelector('.compare-table__scrollbar');
    const paramsEl = section.querySelector('.compare-table__params');

    const noteEl = section.querySelector('[data-compare-note]');
    const emptyEl = section.querySelector('[data-compare-empty]');
    const clearBtn = section.querySelector('[data-compare-clear]');

    const listToggleBtn = section.querySelector('[data-compare-list-toggle]');
    const listDropdown = section.querySelector('#compare-list-dropdown');
    const listCurrentText = listToggleBtn ? listToggleBtn.querySelector('span') : null;

    const listOptions = section.querySelectorAll('[data-compare-list-option]');
    const listTabs = section.querySelectorAll('[data-compare-list-tab]');

    const manageBtn = section.querySelector('[data-compare-manage]');
    const favoritesBtn = section.querySelector('[data-compare-favorites]');

    let compareSwiper = null;

    const getSlides = () => {
      if (!sliderEl) return [];
      return Array.from(sliderEl.querySelectorAll('.compare-table__slide'));
    };

    const getSlidesCount = () => getSlides().length;

    const syncParamsScrollbarState = () => {
      if (!paramsEl) return;

      if (!compareSwiper) {
        paramsEl.classList.remove('with-scrollbar');
        return;
      }

      paramsEl.classList.toggle('with-scrollbar', !compareSwiper.isLocked);
    };

    const updateCompareState = () => {
      const slidesCount = getSlidesCount();

      if (slidesCount === 0) {
        tableRoot.hidden = true;

        if (noteEl) noteEl.hidden = true;
        if (emptyEl) emptyEl.hidden = false;

        if (paramsEl) {
          paramsEl.classList.remove('with-scrollbar');
        }

        return;
      }

      tableRoot.hidden = false;

      if (emptyEl) emptyEl.hidden = true;
      if (noteEl) noteEl.hidden = slidesCount > 1;
    };

    const updateNavState = () => {
      const slidesCount = getSlidesCount();
      const isLocked = compareSwiper ? compareSwiper.isLocked : slidesCount <= 1;

      if (prevEl) {
        prevEl.disabled = isLocked;
      }

      if (nextEl) {
        nextEl.disabled = isLocked;
      }

      syncParamsScrollbarState();
    };

    const initSwiper = () => {
      if (!sliderEl || typeof Swiper === 'undefined') return;

      if (compareSwiper) {
        compareSwiper.destroy(true, true);
      }

      compareSwiper = new Swiper(sliderEl, {
        speed: 500,
        watchOverflow: true,
        observer: true,
        observeParents: true,
        slidesPerView: 1.12,
        spaceBetween: 12,
        navigation: {
          prevEl,
          nextEl
        },
        scrollbar: scrollbarEl
          ? {
              el: scrollbarEl,
              draggable: true,
              dragSize: 'auto'
            }
          : undefined,
        breakpoints: {
          576: {
            slidesPerView: 1.4,
            spaceBetween: 16
          },
          768: {
            slidesPerView: 2.05,
            spaceBetween: 20
          },
          1025: {
            slidesPerView: 3,
            spaceBetween: 20
          },
          1360: {
            slidesPerView: 4,
            spaceBetween: 20
          }
        },
        on: {
          init() {
            updateNavState();
          },
          resize() {
            updateNavState();
          },
          observerUpdate() {
            updateNavState();
          },
          breakpoint() {
            updateNavState();
          },
          lock() {
            updateNavState();
          },
          unlock() {
            updateNavState();
          },
          update() {
            updateNavState();
          }
        }
      });
    };

    const refreshCompare = () => {
      updateCompareState();

      if (compareSwiper) {
        compareSwiper.update();
      }

      updateNavState();
    };

    const closeDropdown = () => {
      if (!listToggleBtn || !listDropdown) return;

      listToggleBtn.setAttribute('aria-expanded', 'false');
      listDropdown.hidden = true;
    };

    const openDropdown = () => {
      if (!listToggleBtn || !listDropdown) return;

      listToggleBtn.setAttribute('aria-expanded', 'true');
      listDropdown.hidden = false;
    };

    const toggleDropdown = () => {
      if (!listToggleBtn || !listDropdown) return;

      const isExpanded = listToggleBtn.getAttribute('aria-expanded') === 'true';

      if (isExpanded) {
        closeDropdown();
      } else {
        openDropdown();
      }
    };

 // 1. Улучшенная функция фильтрации
const setActiveList = (title, categoryId) => {
 // ЕСЛИ ID НЕ ОПРЕДЕЛЕН - ВЫХОДИМ И НИЧЕГО НЕ СКРЫВАЕМ
  if (!categoryId || categoryId === 'undefined') {
   // console.warn('Сработал пустой фильтр, игнорируем...');
    return; 
  }

  //console.log('Фильтруем по:', title, 'ID:', categoryId);


  if (listCurrentText) {
    listCurrentText.textContent = title;
  }

  // Обновляем активные классы для кнопок
  listOptions.forEach(opt => {
    const optId = opt.getAttribute('data-categoryid') || 'all';
    opt.classList.toggle('is-active', optId === categoryId);
  });
  
  listTabs.forEach(tab => {
    const tabId = tab.getAttribute('data-categoryid') || 'all';
    tab.classList.toggle('is-active', tabId === categoryId);
  });

  const slides = getSlides();
  let visibleCount = 0;

  slides.forEach((slide) => {
    // Используем getAttribute — это надежнее, чем dataset
    const slideCatId = slide.getAttribute('data-categoryid');
    
    // Если "Все" ИЛИ ID совпадает
    if (categoryId === 'all' || String(slideCatId) === String(categoryId)) {
      slide.style.display = ''; // Показываем
      visibleCount++;
    } else {
      slide.style.display = 'none'; // Скрываем
    }
  });

  console.log('Слайдов после фильтрации:', visibleCount);

  // Обновляем Swiper
  if (compareSwiper) {
    compareSwiper.update(); 
    compareSwiper.slideTo(0, 0);    

    if (typeof updateNavState === 'function') {
      updateNavState();
    }
  }

  closeDropdown();
};


// Слушаем клики по всей секции сравнения
section.addEventListener('click', (e) => {
  // Ищем, был ли клик по табу или опции (даже если попали в span внутри кнопки)
  const targetBtn = e.target.closest('[data-categoryid]');
  
  // Если это кнопка удаления товара — не мешаем ей (она обрабатывается ниже в вашем коде)
  if (!targetBtn || targetBtn.hasAttribute('data-compare-remove')) return;

  // Проверяем, что это именно таб или опция списка
  if (targetBtn.hasAttribute('data-compare-list-option') || targetBtn.hasAttribute('data-compare-list-tab')) {
    e.preventDefault();
    e.stopPropagation();

    const title = targetBtn.textContent.trim();
    const catId = targetBtn.getAttribute('data-categoryid');

    setActiveList(title, catId);
  }
});





    const clearCompare = () => {
      const slides = getSlides();

      slides.forEach((slide) => slide.remove());

      refreshCompare();

      section.dispatchEvent(
        new CustomEvent('compare:clear', {
          bubbles: true
        })
      );
    };

    if (listToggleBtn && listDropdown) {
      listToggleBtn.addEventListener('click', toggleDropdown);

      document.addEventListener('click', (event) => {
        const target = event.target;

        if (!section.contains(target)) return;

        const clickedInsideDropdown = target.closest('.compare-table__lists-select');

        if (!clickedInsideDropdown) {
          closeDropdown();
        }
      });

      document.addEventListener('keydown', (event) => {
        if (event.key === 'Escape') {
          closeDropdown();
        }
      });
    }

    if (listOptions.length) {
      listOptions.forEach((option) => {
        option.addEventListener('click', () => {
          setActiveList(option.textContent.trim());
        });
      });
    }

    if (listTabs.length) {
      listTabs.forEach((tab) => {
        tab.addEventListener('click', () => {
          setActiveList(tab.textContent.trim());
        });
      });
    }

    if (clearBtn) {
      clearBtn.addEventListener('click', () => {
        clearCompare();
      });
    }

    if (manageBtn) {
      manageBtn.addEventListener('click', () => {
        section.dispatchEvent(
          new CustomEvent('compare:manage', {
            bubbles: true
          })
        );
      });
    }

    if (favoritesBtn) {
      favoritesBtn.addEventListener('click', () => {
        section.dispatchEvent(
          new CustomEvent('compare:favorites', {
            bubbles: true
          })
        );
      });
    }

    section.addEventListener('click', (event) => {
      const removeBtn = event.target.closest('[data-compare-remove]');

      if (!removeBtn) return;

      const slide = removeBtn.closest('.compare-table__slide');

      if (!slide) return;

      slide.remove();
      refreshCompare();
    });

    initSwiper();
    refreshCompare();
  });
});










(function () {
  function initRelArticlesSliders() {
    if (!window.Swiper) return;

    document.querySelectorAll(".js-rel-articles-slider").forEach(function (root) {
      const section = root.closest(".rel-articles");
      if (!section) return;

      const swiperEl = root.querySelector(".swiper");
      const prevBtn = section.querySelector(".rel-articles__btn--prev");
      const nextBtn = section.querySelector(".rel-articles__btn--next");

      new Swiper(swiperEl, {
        slidesPerView: 1,
        spaceBetween: 10,
        loop: false,
        watchOverflow: true,

        navigation: {
          prevEl: prevBtn,
          nextEl: nextBtn,
        },

        breakpoints: {
          768: {
            slidesPerView: 2,
            spaceBetween: 15,
          },
          1025: {
            slidesPerView: 3,
            spaceBetween: 20,
          },
        },
      });
    });
  }

  document.addEventListener("DOMContentLoaded", initRelArticlesSliders);
})();












/* ================================
   SCROLL TO NEXT BLOCK (для блока видео на странице О компании)
================================ */

(function () {

  function initScrollNext() {

    const buttons = document.querySelectorAll('[data-scroll-next]');
    if (!buttons.length) return;

    buttons.forEach(function (btn) {

      btn.addEventListener('click', function () {

        const id = btn.getAttribute('data-scroll-next');
        const target = document.getElementById(id);

        if (!target) return;

        const top = target.getBoundingClientRect().top + window.pageYOffset;

        window.scrollTo({
          top: top,
          behavior: 'smooth'
        });

      });

    });

  }

  document.addEventListener('DOMContentLoaded', initScrollNext);

})();


























/* ================================
   HERO SLIDER
================================ */

(function () {
  var heroScrollItems = [];
  var heroScrollTicking = false;

  function initHeroSlider() {
    if (!window.Swiper) return;

    document.querySelectorAll('.js-hero-slider').forEach(function (root) {
      var heroWrap = root.closest('.hero-wrap') || root.parentElement || document;
      var contentEl = root.querySelector('[data-hero-content-slider]');
      var slides = contentEl
        ? contentEl.querySelectorAll('.swiper-wrapper > .swiper-slide')
        : [];
      var slidesCount = slides.length;
      var prevBtn = heroWrap.querySelector('.hero__btn--prev');
      var nextBtn = heroWrap.querySelector('.hero__btn--next');
      var btnWrap = heroWrap.querySelector('.hero__btn-wrap');
      var counterEl = heroWrap.querySelector('.hero-sliders-counet');

      if (!contentEl) return;

      if (btnWrap && slidesCount > 1) {
        btnWrap.style.display = 'flex';
      }

      var swiperOptions = {
        slidesPerView: 1,
        loop: false,
        speed: 1100,
        effect: 'fade',
        allowTouchMove: slidesCount > 1,
        fadeEffect: {
          crossFade: true,
        },
        on: {
          init: function (swiper) {
            root.dataset.heroDir = 'next';
            updateHeroState(swiper, root, 'next');
            updateHeroBgState(swiper, root, 'next', null);
            updateHeroNavState(swiper, prevBtn, nextBtn, slidesCount);
            updateHeroCounter(swiper, counterEl, slidesCount);
          },

          slideNextTransitionStart: function (swiper) {
            root.dataset.heroDir = 'next';
            updateHeroState(swiper, root, 'next');
            updateHeroBgState(swiper, root, 'next', swiper.previousIndex);
          },

          slidePrevTransitionStart: function (swiper) {
            root.dataset.heroDir = 'prev';
            updateHeroState(swiper, root, 'prev');
            updateHeroBgState(swiper, root, 'prev', swiper.previousIndex);
          },

          slideChange: function (swiper) {
            updateHeroNavState(swiper, prevBtn, nextBtn, slidesCount);
            updateHeroCounter(swiper, counterEl, slidesCount);
          },

          slideChangeTransitionEnd: function (swiper) {
            clearHeroBgLeaving(swiper, root);
          },

          autoplay: function () {
            root.dataset.heroDir = 'next';
          },
        },
      };

      if (slidesCount > 1) {
        swiperOptions.autoplay = {
          delay: 12000,
          disableOnInteraction: false,
          pauseOnMouseEnter: false,
        };
      }

      var contentSwiper = new Swiper(contentEl, swiperOptions);

      if (slidesCount > 1) {
        if (prevBtn) {
          prevBtn.addEventListener('click', function (e) {
            e.preventDefault();
            if (contentSwiper.activeIndex === 0) return;

            root.dataset.heroDir = 'prev';
            contentSwiper.slidePrev();
          });
        }

        if (nextBtn) {
          nextBtn.addEventListener('click', function (e) {
            e.preventDefault();

            root.dataset.heroDir = 'next';

            if (contentSwiper.activeIndex >= slidesCount - 1) {
              contentSwiper.slideTo(0);
              return;
            }

            contentSwiper.slideNext();
          });
        }
      }

      root.addEventListener('mouseenter', function () {
        if (contentSwiper.autoplay) contentSwiper.autoplay.stop();
      });

      root.addEventListener('mouseleave', function () {
        if (contentSwiper.autoplay) contentSwiper.autoplay.start();
      });
    });

    initHeroScrollEffects();
  }

  function updateHeroCounter(swiper, counterEl, total) {
    if (!counterEl) return;

    var current = swiper.activeIndex + 1;
    counterEl.textContent = current + ' / ' + total;
  }

  function updateHeroNavState(swiper, prevBtn, nextBtn, slidesCount) {
    if (prevBtn) {
      var isFirst = swiper.activeIndex === 0;
      prevBtn.disabled = isFirst;
      prevBtn.classList.toggle('is-disabled', isFirst);
    }

    if (nextBtn) {
      var hasMany = slidesCount > 1;
      nextBtn.disabled = !hasMany;
      nextBtn.classList.toggle('is-disabled', !hasMany);
    }
  }

  function updateHeroState(swiper, root, direction) {
    var contentSlides = root.querySelectorAll(
      '[data-hero-content-slider] .swiper-wrapper > .swiper-slide'
    );

    root.classList.remove('is-dir-next', 'is-dir-prev');
    root.classList.add(direction === 'prev' ? 'is-dir-prev' : 'is-dir-next');

    contentSlides.forEach(function (slide, index) {
      slide.classList.remove('is-prev', 'is-next', 'is-current');

      if (index === swiper.activeIndex) {
        slide.classList.add('is-current');
      } else if (index < swiper.activeIndex) {
        slide.classList.add('is-prev');
      } else {
        slide.classList.add('is-next');
      }
    });
  }

  function updateHeroBgState(swiper, root, direction, leavingIndex) {
    var bgSlides = root.querySelectorAll(
      '[data-hero-bg-slider] .swiper-wrapper > .swiper-slide'
    );

    root.classList.remove('is-dir-next', 'is-dir-prev');
    root.classList.add(direction === 'prev' ? 'is-dir-prev' : 'is-dir-next');

    bgSlides.forEach(function (slide, index) {
      slide.classList.remove(
        'is-prev',
        'is-next',
        'is-current',
        'is-leaving'
      );

      if (index === swiper.activeIndex) {
        slide.classList.add('is-current');
        return;
      }

      if (leavingIndex !== null && index === leavingIndex) {
        slide.classList.add('is-leaving');
        return;
      }

      if (index < swiper.activeIndex) {
        slide.classList.add('is-prev');
      } else {
        slide.classList.add('is-next');
      }
    });
  }

  function clearHeroBgLeaving(swiper, root) {
    var bgSlides = root.querySelectorAll(
      '[data-hero-bg-slider] .swiper-wrapper > .swiper-slide'
    );

    bgSlides.forEach(function (slide, index) {
      slide.classList.remove('is-leaving', 'is-prev', 'is-next', 'is-current');

      if (index === swiper.activeIndex) {
        slide.classList.add('is-current');
      } else if (index < swiper.activeIndex) {
        slide.classList.add('is-prev');
      } else {
        slide.classList.add('is-next');
      }
    });
  }

  function initHeroScrollEffects() {
    heroScrollItems = Array.from(
      document.querySelectorAll('[data-hero-parallax]')
    ).map(function (root) {
      return { root: root };
    });

    if (!heroScrollItems.length) return;

    updateHeroScrollEffects();

    window.addEventListener('scroll', requestHeroScrollUpdate, { passive: true });
    window.addEventListener('resize', requestHeroScrollUpdate);
    window.addEventListener('orientationchange', requestHeroScrollUpdate);
  }

  function requestHeroScrollUpdate() {
    if (heroScrollTicking) return;

    heroScrollTicking = true;

    window.requestAnimationFrame(function () {
      updateHeroScrollEffects();
      heroScrollTicking = false;
    });
  }

  function updateHeroScrollEffects() {
    var vh = window.innerHeight || document.documentElement.clientHeight || 0;

    heroScrollItems.forEach(function (item) {
      if (!item.root) return;

      var rect = item.root.getBoundingClientRect();
      var heroHeight = rect.height || 1;
      var centerOffset = rect.top + heroHeight / 2 - vh / 2;
      var progress = centerOffset / vh;

      var bgShift = progress * -150;

      var passed = Math.max(0, -rect.top);
      var blurStart = heroHeight * 0.5;
      var blurProgress = 0;

      if (passed > blurStart) {
        blurProgress = (passed - blurStart) / Math.max(heroHeight - blurStart, 1);
      }

      if (blurProgress > 1) blurProgress = 1;

      var blurValue = blurProgress * 6;

      item.root.style.setProperty('--hero-bg-shift', bgShift.toFixed(2) + 'px');
      item.root.style.setProperty('--hero-bg-blur', blurValue.toFixed(2) + 'px');
    });
  }

  document.addEventListener('DOMContentLoaded', initHeroSlider);
})();






















/* ================================
   HERO ONE SLIDER
================================ */

(function () {
  var heroOneScrollItems = [];
  var heroOneScrollTicking = false;

  function initHeroOneSlider() {
    if (!window.Swiper) return;

    document.querySelectorAll('.js-hero-one-slider').forEach(function (root) {
      var heroWrap = root.closest('.hero-one-wrap') || root.parentElement || document;
      var contentEl = root.querySelector('[data-hero-one-content-slider]');
      var slides = contentEl
        ? contentEl.querySelectorAll('.swiper-wrapper > .swiper-slide')
        : [];
      var slidesCount = slides.length;
      var prevBtn = heroWrap.querySelector('.hero-one__btn--prev');
      var nextBtn = heroWrap.querySelector('.hero-one__btn--next');
      var btnWrap = heroWrap.querySelector('.hero-one__btn-wrap');
      var counterEl = heroWrap.querySelector('.hero-one-sliders-count');

      if (!contentEl) return;

      if (btnWrap && slidesCount > 1) {
        btnWrap.style.display = 'flex';
      }

      var swiperOptions = {
        slidesPerView: 1,
        loop: false,
        speed: 1100,
        effect: 'fade',
        allowTouchMove: slidesCount > 1,
        fadeEffect: {
          crossFade: true,
        },
        on: {
          init: function (swiper) {
            root.dataset.heroOneDir = 'next';
            updateHeroOneState(swiper, root, 'next');
            updateHeroOneNavState(swiper, prevBtn, nextBtn, slidesCount);
            updateHeroOneCounter(swiper, counterEl, slidesCount);
          },
          slideNextTransitionStart: function (swiper) {
            root.dataset.heroOneDir = 'next';
            updateHeroOneState(swiper, root, 'next');
          },
          slidePrevTransitionStart: function (swiper) {
            root.dataset.heroOneDir = 'prev';
            updateHeroOneState(swiper, root, 'prev');
          },
          slideChange: function (swiper) {
            updateHeroOneNavState(swiper, prevBtn, nextBtn, slidesCount);
            updateHeroOneCounter(swiper, counterEl, slidesCount);
          },
          autoplay: function () {
            root.dataset.heroOneDir = 'next';
          },
        },
      };

      if (slidesCount > 1) {
        swiperOptions.autoplay = {
          delay: 12000,
          disableOnInteraction: false,
          pauseOnMouseEnter: false,
        };
      }

      var contentSwiper = new Swiper(contentEl, swiperOptions);

      if (slidesCount > 1) {
        if (prevBtn) {
          prevBtn.addEventListener('click', function (e) {
            e.preventDefault();
            if (contentSwiper.activeIndex === 0) return;
            contentSwiper.slidePrev();
          });
        }

        if (nextBtn) {
          nextBtn.addEventListener('click', function (e) {
            e.preventDefault();

            if (contentSwiper.activeIndex >= slidesCount - 1) {
              root.dataset.heroOneDir = 'next';
              contentSwiper.slideTo(0);
              return;
            }

            contentSwiper.slideNext();
          });
        }
      }

      root.addEventListener('mouseenter', function () {
        if (contentSwiper.autoplay) contentSwiper.autoplay.stop();
      });

      root.addEventListener('mouseleave', function () {
        if (contentSwiper.autoplay) contentSwiper.autoplay.start();
      });
    });

    initHeroOneScrollEffects();
  }

  function updateHeroOneCounter(swiper, counterEl, total) {
    if (!counterEl) return;

    var current = swiper.activeIndex + 1;
    counterEl.textContent = current + ' / ' + total;
  }

  function updateHeroOneNavState(swiper, prevBtn, nextBtn, slidesCount) {
    if (prevBtn) {
      var isFirst = swiper.activeIndex === 0;
      prevBtn.disabled = isFirst;
      prevBtn.classList.toggle('is-disabled', isFirst);
    }

    if (nextBtn) {
      var hasMany = slidesCount > 1;
      nextBtn.disabled = !hasMany;
      nextBtn.classList.toggle('is-disabled', !hasMany);
    }
  }

  function updateHeroOneState(swiper, root, direction) {
    var contentSlides = root.querySelectorAll(
      '[data-hero-one-content-slider] .swiper-wrapper > .swiper-slide'
    );

    root.classList.remove('is-one-dir-next', 'is-one-dir-prev');
    root.classList.add(direction === 'prev' ? 'is-one-dir-prev' : 'is-one-dir-next');

    contentSlides.forEach(function (slide, index) {
      slide.classList.remove('is-prev', 'is-next', 'is-current');

      if (index === swiper.activeIndex) {
        slide.classList.add('is-current');
      } else if (index < swiper.activeIndex) {
        slide.classList.add('is-prev');
      } else {
        slide.classList.add('is-next');
      }
    });
  }

  function initHeroOneScrollEffects() {
    heroOneScrollItems = Array.from(
      document.querySelectorAll('[data-hero-one-parallax]')
    ).map(function (root) {
      return { root: root };
    });

    if (!heroOneScrollItems.length) return;

    updateHeroOneScrollEffects();

    window.addEventListener('scroll', requestHeroOneScrollUpdate, { passive: true });
    window.addEventListener('resize', requestHeroOneScrollUpdate);
    window.addEventListener('orientationchange', requestHeroOneScrollUpdate);
  }

  function requestHeroOneScrollUpdate() {
    if (heroOneScrollTicking) return;

    heroOneScrollTicking = true;

    window.requestAnimationFrame(function () {
      updateHeroOneScrollEffects();
      heroOneScrollTicking = false;
    });
  }

  function updateHeroOneScrollEffects() {
    var vh = window.innerHeight || document.documentElement.clientHeight || 0;

    heroOneScrollItems.forEach(function (item) {
      if (!item.root) return;

      var rect = item.root.getBoundingClientRect();
      var heroHeight = rect.height || 1;
      var centerOffset = rect.top + heroHeight / 2 - vh / 2;
      var progress = centerOffset / vh;

      var bgShift = progress * -84;

      var passed = Math.max(0, -rect.top);
      var blurStart = heroHeight * 0.5;
      var blurProgress = 0;

      if (passed > blurStart) {
        blurProgress = (passed - blurStart) / Math.max(heroHeight - blurStart, 1);
      }

      if (blurProgress > 1) blurProgress = 1;

      var blurValue = blurProgress * 6;

      item.root.style.setProperty('--hero-bg-shift', bgShift.toFixed(2) + 'px');
      item.root.style.setProperty('--hero-bg-blur', blurValue.toFixed(2) + 'px');
    });
  }

  document.addEventListener('DOMContentLoaded', initHeroOneSlider);
})();


































// ШАПКА-ПРИЛИПАЛА
// header sticky all

(function () {
  const header = document.querySelector('[data-header]');
  const stickyDesktop = document.querySelector('[data-header-sticky]');
  const stickyMobile = document.querySelector('[data-header-mobilebar]');

  if (!header || (!stickyDesktop && !stickyMobile)) return;

  function getStickyOffset() {
    return window.innerWidth <= 1024 ? 500 : 400;
  }

  function getActualScrollTop() {
    if (document.body.classList.contains('is-scroll-locked')) {
      const bodyTop = parseInt(document.body.style.top || '0', 10) || 0;
      return Math.abs(bodyTop);
    }

    return window.scrollY || window.pageYOffset || document.documentElement.scrollTop || 0;
  }

  function setStickyState(el, state) {
    if (!el) return;
    el.classList.toggle('sticky', state);
  }

  function toggleStickyHeader() {
    const stickyOffset = getStickyOffset();
    const scrollTop = getActualScrollTop();
    const shouldStick = scrollTop > stickyOffset;
    const isMobile = window.innerWidth <= 1024;

    if (isMobile) {
      setStickyState(stickyDesktop, false);
      setStickyState(stickyMobile, shouldStick);
      header.classList.toggle('is-mobilebar-sticky', shouldStick);
      return;
    }

    setStickyState(stickyMobile, false);
    setStickyState(stickyDesktop, shouldStick);
    header.classList.remove('is-mobilebar-sticky');
  }

  window.addEventListener('scroll', toggleStickyHeader, { passive: true });
  window.addEventListener('resize', toggleStickyHeader);

  const mo = new MutationObserver(toggleStickyHeader);
  mo.observe(document.body, {
    attributes: true,
    attributeFilter: ['class', 'style']
  });

  toggleStickyHeader();
})();
































// Горизонтальный Скролл мини меню в шапке, десктоп

(function () {
  const wrappers = document.querySelectorAll('[data-menu-scroll]');

  wrappers.forEach(function (wrapper) {
    const area = wrapper.querySelector('[data-menu-scroll-area]');
    const btnLeft = wrapper.querySelector('[data-menu-scroll-left]');
    const btnRight = wrapper.querySelector('[data-menu-scroll-right]');

    if (!area || !btnLeft || !btnRight) return;

    function getStep() {
      return Math.max(180, Math.floor(area.clientWidth * 0.75));
    }

    function updateControls() {
      const maxScroll = area.scrollWidth - area.clientWidth;
      const hasOverflow = area.scrollWidth > area.clientWidth + 2;
      const atStart = area.scrollLeft <= 2;
      const atEnd = area.scrollLeft >= maxScroll - 2;

      btnLeft.hidden = !hasOverflow || atStart;
      btnRight.hidden = !hasOverflow || atEnd;

      wrapper.classList.toggle('is-overflow-left', hasOverflow && !atStart);
      wrapper.classList.toggle('is-overflow-right', hasOverflow && !atEnd);

      area.classList.remove('has-mask-left', 'has-mask-right', 'has-mask-both');

      if (hasOverflow && atStart && !atEnd) {
        area.classList.add('has-mask-right');
      } else if (hasOverflow && !atStart && atEnd) {
        area.classList.add('has-mask-left');
      } else if (hasOverflow && !atStart && !atEnd) {
        area.classList.add('has-mask-both');
      }
    }

    function scrollMenu(direction) {
      area.scrollBy({
        left: direction * getStep(),
        behavior: 'smooth'
      });
    }

    btnLeft.addEventListener('click', function () {
      scrollMenu(-1);
    });

    btnRight.addEventListener('click', function () {
      scrollMenu(1);
    });

    area.addEventListener('scroll', updateControls, { passive: true });
    window.addEventListener('resize', updateControls);

    updateControls();
  });
})();






















// ДОБАВЛЯЕМ КЛАСС .goto_sticky НА <body> ПРИ АКТИВНОМ STICKY
(function () {
  const body = document.body;
  const stickyDesktop = document.querySelector('[data-header-sticky]');
  const stickyMobile = document.querySelector('[data-header-mobilebar]');

  // Если нечего отслеживать — выходим
  if (!body || (!stickyDesktop && !stickyMobile)) return;

  function syncGotoStickyState() {
    const isDesktopSticky = stickyDesktop && stickyDesktop.classList.contains('sticky');
    const isMobileSticky = stickyMobile && stickyMobile.classList.contains('sticky');
    const isStickyActive = isDesktopSticky || isMobileSticky;

    // Переключаем класс на body
    body.classList.toggle('goto_sticky', isStickyActive);
  }

  // Отслеживаем скролл и ресайз (на случай, если sticky меняется там)
  window.addEventListener('scroll', syncGotoStickyState, { passive: true });
  window.addEventListener('resize', syncGotoStickyState);

  // Следим за изменением классов sticky-элементов
  const stickyObserver = new MutationObserver(syncGotoStickyState);

  if (stickyDesktop) {
    stickyObserver.observe(stickyDesktop, {
      attributes: true,
      attributeFilter: ['class']
    });
  }

  if (stickyMobile) {
    stickyObserver.observe(stickyMobile, {
      attributes: true,
      attributeFilter: ['class']
    });
  }

  // Первичная проверка при загрузке
  syncGotoStickyState();
})();






/* СОРТИРОВКА товаров */
(function () {
  const sortContainer = document.querySelector('.category__sort');
  if (!sortContainer) return;

  const toggleBtn = sortContainer.querySelector('[data-sort-open]');
  const menu = sortContainer.querySelector('[data-sort-menu]');
  const sortItems = sortContainer.querySelectorAll('[data-sort]');

  // 1. Логика открытия/закрытия меню
  toggleBtn.addEventListener('click', (e) => {
    const isExpanded = toggleBtn.getAttribute('aria-expanded') === 'true';
    toggleBtn.setAttribute('aria-expanded', !isExpanded);
    menu.hidden = isExpanded;
    e.stopPropagation();
  });

  // Закрытие меню при клике вне области (для удобства)
  document.addEventListener('click', (e) => {
    if (!sortContainer.contains(e.target)) {
      toggleBtn.setAttribute('aria-expanded', 'false');
      menu.hidden = true;
    }
  });

  // 2. Логика смены сортировки и перехода по ссылке
  sortItems.forEach(item => {
    item.addEventListener('click', () => {
      const sortData = item.getAttribute('data-sort'); // "sort=p.date_added&order=DESC"
      
      // Работаем с текущим URL
      const url = new URL(window.location.href);
      const params = new URLSearchParams(sortData);

      // Обновляем параметры в текущем URL, не затирая остальные (например, фильтры или пагинацию)
      params.forEach((value, key) => {
        url.searchParams.set(key, value);
      });

      // Переход по новому адресу
      window.location.href = url.toString();
    });
  });
})();


/* ЛИМИТ товаров на странице */
(function () {
  const limitContainer = document.querySelector('.category__limit');
  if (!limitContainer) return;

  const toggleBtn = limitContainer.querySelector('[data-limit-open]');
  const menu = limitContainer.querySelector('[data-limit-menu]');
  const sortContainer = document.querySelector('.category__sort');
  const sortToggleBtn = sortContainer ? sortContainer.querySelector('[data-sort-open]') : null;
  const sortMenu = sortContainer ? sortContainer.querySelector('[data-sort-menu]') : null;

  function closeMenu() {
    toggleBtn.setAttribute('aria-expanded', 'false');
    menu.hidden = true;
  }

  toggleBtn.addEventListener('click', (e) => {
    const isExpanded = toggleBtn.getAttribute('aria-expanded') === 'true';
    toggleBtn.setAttribute('aria-expanded', !isExpanded);
    menu.hidden = isExpanded;

    if (!isExpanded && sortToggleBtn && sortMenu) {
      sortToggleBtn.setAttribute('aria-expanded', 'false');
      sortMenu.hidden = true;
    }

    e.stopPropagation();
  });

  document.addEventListener('click', (e) => {
    if (!limitContainer.contains(e.target)) {
      closeMenu();
    }
  });
})();


/* CATEGORY V2 — view switcher (grid / list) */
(function () {
  var LS_KEY = 'zpm_category_view';
  var DESKTOP_MQ = window.matchMedia('(min-width: 1025px)');

  function getSection() {
    return document.querySelector('.page--category section.category');
  }

  function normalizeView(value) {
    return value === 'list' ? 'list' : 'grid';
  }

  function getStoredView() {
    try {
      return normalizeView(localStorage.getItem(LS_KEY));
    } catch (e) {
      return 'grid';
    }
  }

  function setStoredView(view) {
    try {
      localStorage.setItem(LS_KEY, normalizeView(view));
    } catch (e) {}
  }

  function updateButtons(activeView) {
    document.querySelectorAll('[data-category-view-mode]').forEach(function (btn) {
      var mode = btn.getAttribute('data-category-view-mode');
      var isActive = mode === activeView;
      btn.classList.toggle('is-active', isActive);
      btn.setAttribute('aria-pressed', isActive ? 'true' : 'false');
    });
  }

  function applyView(view) {
    var section = getSection();
    if (!section) return;

    var effectiveView = DESKTOP_MQ.matches ? normalizeView(view) : 'grid';
    section.classList.toggle('category--view-list', effectiveView === 'list');
    updateButtons(effectiveView);
  }

  function initCategoryViewSwitcher() {
    var section = getSection();
    if (!section) return;

    applyView(getStoredView());

    document.querySelectorAll('[data-category-view-mode]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        if (!DESKTOP_MQ.matches) return;
        var mode = btn.getAttribute('data-category-view-mode');
        setStoredView(mode);
        applyView(mode);
      });
    });

    if (typeof DESKTOP_MQ.addEventListener === 'function') {
      DESKTOP_MQ.addEventListener('change', function () {
        applyView(getStoredView());
      });
    } else if (typeof DESKTOP_MQ.addListener === 'function') {
      DESKTOP_MQ.addListener(function () {
        applyView(getStoredView());
      });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initCategoryViewSwitcher);
  } else {
    initCategoryViewSwitcher();
  }
})();


/* CATEGORY V2.3 / V2.3.1 — subcategory chips collapsed / expanded */
(function () {
  var MAX_LINES = 2;
  var LABEL_COLLAPSE = 'Свернуть';
  var resizeTimer = null;

  function isMobileViewport() {
    return window.matchMedia('(max-width: 768px)').matches;
  }

  function getExpandLabel(hiddenCount) {
    if (!hiddenCount || hiddenCount <= 0) {
      return isMobileViewport() ? 'Показать все' : 'Показать все подкатегории';
    }
    if (isMobileViewport()) {
      return 'Ещё ' + hiddenCount + ' подкатегорий';
    }
    return 'Показать ещё ' + hiddenCount + ' подкатегорий';
  }

  function countHiddenChips(list) {
    var rows = getChipRows(list);
    if (rows.length <= MAX_LINES) {
      return 0;
    }

    var visibleCount = 0;
    for (var i = 0; i < MAX_LINES; i++) {
      visibleCount += rows[i].chips.length;
    }

    return list.querySelectorAll('.zpm-sub-cat-chip').length - visibleCount;
  }

  function getBlock() {
    return document.querySelector('.page--category [data-subcat-chips]');
  }

  function getChipRows(list) {
    var listRect = list.getBoundingClientRect();
    var chips = list.querySelectorAll('.zpm-sub-cat-chip');
    var rows = [];

    chips.forEach(function (chip) {
      var top = Math.round(chip.getBoundingClientRect().top - listRect.top);
      var rowIndex = -1;

      for (var i = 0; i < rows.length; i++) {
        if (Math.abs(rows[i].top - top) <= 2) {
          rowIndex = i;
          break;
        }
      }

      if (rowIndex === -1) {
        rows.push({ top: top, chips: [chip] });
      } else {
        rows[rowIndex].chips.push(chip);
      }
    });

    rows.sort(function (a, b) {
      return a.top - b.top;
    });

    return rows;
  }

  function measureCollapsedHeight(list) {
    var rows = getChipRows(list);
    if (rows.length <= MAX_LINES) {
      return { needsToggle: false, maxHeight: 0 };
    }

    var listRect = list.getBoundingClientRect();
    var maxBottom = 0;

    for (var i = 0; i < MAX_LINES; i++) {
      rows[i].chips.forEach(function (chip) {
        maxBottom = Math.max(
          maxBottom,
          chip.getBoundingClientRect().bottom - listRect.top
        );
      });
    }

    return { needsToggle: true, maxHeight: Math.ceil(maxBottom) };
  }

  function initSubcatChips() {
    var block = getBlock();
    if (!block) return null;

    var list = block.querySelector('[data-subcat-chips-list]');
    var toggle = block.querySelector('[data-subcat-chips-toggle]');
    var label = block.querySelector('[data-subcat-chips-toggle-label]');
    var chevron = block.querySelector('[data-subcat-chips-toggle-chevron]');
    if (!list || !toggle || !label) return null;

    var expanded = false;

    function updateChevron(isExpanded) {
      if (!chevron) return;
      chevron.classList.remove('fa-chevron-down', 'fa-chevron-up');
      chevron.classList.add(isExpanded ? 'fa-chevron-up' : 'fa-chevron-down');
    }

    function setExpanded(nextExpanded) {
      expanded = !!nextExpanded;
      block.classList.toggle('is-expanded', expanded);
      block.classList.toggle('is-collapsed', !expanded);
      toggle.setAttribute('aria-expanded', expanded ? 'true' : 'false');
      label.textContent = expanded ? LABEL_COLLAPSE : getExpandLabel(countHiddenChips(list));
      updateChevron(expanded);
    }

    function applyLayout() {
      block.classList.remove('is-collapsible', 'is-collapsed', 'is-expanded');
      list.style.maxHeight = '';
      toggle.hidden = true;

      var metrics = measureCollapsedHeight(list);
      if (!metrics.needsToggle) {
        expanded = false;
        return;
      }

      block.classList.add('is-collapsible');
      block.style.setProperty('--subcat-chips-max-h', metrics.maxHeight + 'px');
      toggle.hidden = false;

      if (expanded) {
        setExpanded(true);
      } else {
        setExpanded(false);
      }
    }

    toggle.addEventListener('click', function () {
      setExpanded(!expanded);
    });

    applyLayout();

    if (window.ResizeObserver) {
      var ro = new ResizeObserver(function () {
        onResize();
      });
      ro.observe(list);
    }

    return {
      refresh: function () {
        applyLayout();
      },
    };
  }

  var controller = null;

  function onResize() {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function () {
      if (controller) {
        controller.refresh();
      } else {
        controller = initSubcatChips();
      }
    }, 150);
  }

  function boot() {
    requestAnimationFrame(function () {
      requestAnimationFrame(function () {
        controller = initSubcatChips();
        window.addEventListener('resize', onResize);
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();