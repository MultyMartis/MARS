/**
 * Sticky CTA — show after hero sentinel leaves viewport
 */
(function (global) {
  'use strict';

  function getSentinel(el) {
    var sel = el.getAttribute('data-sticky-hero') || '#hero-sentinel';
    return document.querySelector(sel);
  }

  function setVisible(bar, visible) {
    if (visible) {
      bar.hidden = false;
      bar.setAttribute('aria-hidden', 'false');
    } else {
      bar.hidden = true;
      bar.setAttribute('aria-hidden', 'true');
    }
  }

  function init(el) {
    if (el.__wfStickyBound) return;
    el.__wfStickyBound = true;

    var sentinel = getSentinel(el);
    if (!sentinel || !('IntersectionObserver' in global)) {
      setVisible(el, true);
      return;
    }

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          setVisible(el, !entry.isIntersecting);
        });
      },
      { root: null, threshold: 0 }
    );

    observer.observe(sentinel);
    el.__wfStickyObserver = observer;
  }

  function destroy(el) {
    if (el.__wfStickyObserver) {
      el.__wfStickyObserver.disconnect();
      delete el.__wfStickyObserver;
    }
    delete el.__wfStickyBound;
    setVisible(el, false);
  }

  if (global.WfLifecycle) {
    global.WfLifecycle.registerModule('sticky-cta', { init: init, destroy: destroy });
  }
})(typeof window !== 'undefined' ? window : global);
