/**
 * FP-0002 V9-06E57 / PROD-P13 FIX02 — scroll-progress lifebuoy
 *
 * P12 translate3d-on-mover FAILED on physical iPhone.
 *
 * FIX02:
 * - Never put transform/contain on the fixed root (iOS containing-block freeze).
 * - Desktop/Android: mover transform (scale+rotate+translate px).
 * - iOS/iPadOS: position the mover with top/left in CSS pixels; transform only
 *   scale+rotate. visualViewport used for toolbar-safe metrics.
 *
 * PHYSICAL IPHONE QA remains operator/Olya pending.
 */
(function () {
  'use strict';

  var root = document.querySelector('[data-fp02-lifebuoy-parallax]');
  if (!root) {
    return;
  }

  var mover =
    root.querySelector('[data-fp02-lifebuoy-mover]') ||
    root.querySelector('.fp02-lifebuoy-parallax__mover') ||
    root.querySelector('.fp02-lifebuoy-parallax__img') ||
    root;

  function isIosLike() {
    var ua = navigator.userAgent || '';
    if (/iP(hone|ad|od)/i.test(ua)) {
      return true;
    }
    if (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1) {
      return true;
    }
    return false;
  }

  var iosFallback = isIosLike();
  if (iosFallback) {
    root.classList.add('is-ios-fallback');
    root.setAttribute('data-fp02-lb-ios', '1');
  }

  function isShortPage(scrollable) {
    var threshold = Math.max(2400, window.innerHeight * 4);
    return scrollable < threshold;
  }

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  var rafId = 0;
  var lastProgress = -1;
  var lastShort = null;

  function clamp(value, min, max) {
    return Math.max(min, Math.min(max, value));
  }

  function easeOutCubic(t) {
    t = clamp(t, 0, 1);
    return 1 - Math.pow(1 - t, 3);
  }

  function scaleForProgress(te, short) {
    var scaleStart = 1;
    var scaleMid = short ? 1.12 : 1.2;
    var scaleEnd = short ? 0.85 : 0.72;
    if (te <= 0.5) {
      return scaleStart + (scaleMid - scaleStart) * (te / 0.5);
    }
    return scaleMid + (scaleEnd - scaleMid) * ((te - 0.5) / 0.5);
  }

  function getScrollY() {
    var vv = window.visualViewport;
    if (vv && typeof vv.pageTop === 'number') {
      return vv.pageTop;
    }
    if (typeof window.scrollY === 'number') {
      return window.scrollY;
    }
    if (typeof window.pageYOffset === 'number') {
      return window.pageYOffset;
    }
    var doc = document.documentElement;
    var body = document.body;
    return (doc && doc.scrollTop) || (body && body.scrollTop) || 0;
  }

  function getViewportHeight() {
    var vv = window.visualViewport;
    if (vv && vv.height) {
      return vv.height;
    }
    return window.innerHeight || (document.documentElement && document.documentElement.clientHeight) || 0;
  }

  function getScrollMetrics() {
    var doc = document.documentElement;
    var viewport = getViewportHeight();
    var scrollHeight = doc ? doc.scrollHeight : 0;
    var scrollable = Math.max(0, scrollHeight - viewport);
    var y = getScrollY();
    var progress = scrollable > 0 ? clamp(y / scrollable, 0, 1) : 0;
    return {
      scrollable: scrollable,
      progress: progress,
      short: isShortPage(scrollable),
      viewport: viewport,
      y: y
    };
  }

  function applyState(metrics) {
    var tRaw = metrics.progress;
    if (reduceMotion.matches) {
      tRaw = 0.28;
    } else if (metrics.short) {
      tRaw = metrics.progress * 0.55;
    }

    var tEase = easeOutCubic(tRaw);
    var vh = metrics.viewport || window.innerHeight || 1;

    var xStart = -50;
    var xEnd = metrics.short ? -38 : -20;
    var yStartVh = -12;
    var yEndVh = metrics.short ? 28 : 52;
    var arcAmp = metrics.short ? 4 : 8;
    var arc = Math.sin(Math.PI * tEase) * arcAmp;
    var xPct = xStart + (xEnd - xStart) * tEase + arc;
    var yVh = yStartVh + (yEndVh - yStartVh) * tEase;
    var scale = scaleForProgress(tRaw, metrics.short);
    var rotStart = metrics.short ? -3.6 : -7.2;
    var rotEnd = metrics.short ? 12 : 21.6;
    var rotate = rotStart + (rotEnd - rotStart) * tEase;

    var xPx = (xPct / 100) * (mover.offsetWidth || root.clientWidth || window.innerWidth || 0);
    var yPx = (yVh / 100) * vh;
    var scaleVal = scale.toFixed(4);
    var rotateVal = rotate.toFixed(3) + 'deg';

    root.style.setProperty('--fp02-lb-x', xPct.toFixed(3) + '%');
    root.style.setProperty('--fp02-lb-y', yVh.toFixed(3) + 'vh');
    root.style.setProperty('--fp02-lb-scale', scaleVal);
    root.style.setProperty('--fp02-lb-rotate', rotateVal);
    root.setAttribute('data-fp02-lb-mode', metrics.short ? 'short' : 'long');
    root.setAttribute('data-fp02-lb-progress', tRaw.toFixed(4));
    root.setAttribute('data-fp02-lb-xpx', xPx.toFixed(1));
    root.setAttribute('data-fp02-lb-ypx', yPx.toFixed(1));

    if (iosFallback) {
      mover.style.left = xPx.toFixed(2) + 'px';
      mover.style.top = yPx.toFixed(2) + 'px';
      var iosTransform = 'scale(' + scaleVal + ') rotate(' + rotateVal + ')';
      mover.style.transform = iosTransform;
      mover.style.webkitTransform = iosTransform;
      return;
    }

    var transform =
      'translate3d(' +
      xPx.toFixed(2) +
      'px, ' +
      yPx.toFixed(2) +
      'px, 0) scale(' +
      scaleVal +
      ') rotate(' +
      rotateVal +
      ')';
    mover.style.transform = transform;
    mover.style.webkitTransform = transform;
  }

  function tick() {
    rafId = 0;
    var metrics = getScrollMetrics();
    if (
      lastProgress >= 0 &&
      Math.abs(metrics.progress - lastProgress) < 0.0004 &&
      lastShort === metrics.short &&
      !reduceMotion.matches
    ) {
      return;
    }
    lastProgress = metrics.progress;
    lastShort = metrics.short;
    applyState(metrics);
  }

  function requestTick() {
    if (!rafId) {
      rafId = window.requestAnimationFrame(tick);
    }
  }

  window.addEventListener('scroll', requestTick, { passive: true });
  window.addEventListener('resize', requestTick, { passive: true });
  window.addEventListener('orientationchange', requestTick, { passive: true });
  window.addEventListener('pageshow', requestTick, { passive: true });
  document.addEventListener('touchmove', requestTick, { passive: true });

  if (window.visualViewport) {
    window.visualViewport.addEventListener('scroll', requestTick, { passive: true });
    window.visualViewport.addEventListener('resize', requestTick, { passive: true });
  }

  if (typeof reduceMotion.addEventListener === 'function') {
    reduceMotion.addEventListener('change', requestTick);
  } else if (typeof reduceMotion.addListener === 'function') {
    reduceMotion.addListener(requestTick);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', requestTick);
  } else {
    requestTick();
  }
})();
