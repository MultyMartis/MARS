/**
 * FP-0002 V9-06E57-FIX02 / PROD-P08 — scroll-progress lifebuoy parallax
 *
 * Motion model (normalized progress t ∈ [0, 1]):
 * - X/Y/rotate: easeOutCubic on effective progress (non-zero derivative at t=0 —
 *   removes FIX01 easeInOutCubic dead zone). Long page reveals ~50%→~80%.
 * - Scale (piecewise linear on raw effective t; same endpoints as FIX01):
 *     t 0→0.5: start → start×1.20
 *     t 0.5→1: mid → mid×0.60 (= start×0.72)
 * - Rotate: continuous map on eased progress; FIX01 amplitude × ≈1.20.
 * - Reverse scroll: same live mapping (no separate reverse engine).
 *
 * PROD-P08: write compositor transform directly on the image (WebKit-safe).
 * CSS custom properties are dual-written for debugging/inspection only.
 */
(function () {
  'use strict';

  var root = document.querySelector('[data-fp02-lifebuoy-parallax]');
  if (!root) {
    return;
  }

  var img = root.querySelector('.fp02-lifebuoy-parallax__img') || root;

  /**
   * Short-page threshold: scrollable distance under 4× viewport height
   * (and at least 2400px floor so tiny viewports still classify reasonably).
   * Contacts uses reduced travel/reveal/scale/rotation; Home/services stay long.
   */
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

  /**
   * easeOutCubic — de/dt(0) = 3 (immediate scroll response).
   * Replaces FIX01 easeInOutCubic (4t³ first half → de/dt(0) = 0 dead zone).
   */
  function easeOutCubic(t) {
    t = clamp(t, 0, 1);
    return 1 - Math.pow(1 - t, 3);
  }

  /**
   * Piecewise scale on effective progress te ∈ [0,1].
   * Linear per phase so scale reacts immediately (FIX01 smoothstep had de/dt(0)=0).
   * Long: 1.00 → 1.20 → 0.72
   * Short: 1.00 → 1.12 → 0.85 (reduced envelope)
   */
  function scaleForProgress(te, short) {
    var scaleStart = 1;
    var scaleMid = short ? 1.12 : 1.2;
    var scaleEnd = short ? 0.85 : 0.72;

    if (te <= 0.5) {
      return scaleStart + (scaleMid - scaleStart) * (te / 0.5);
    }

    return scaleMid + (scaleEnd - scaleMid) * ((te - 0.5) / 0.5);
  }

  function getScrollMetrics() {
    var doc = document.documentElement;
    var scrollable = Math.max(0, doc.scrollHeight - window.innerHeight);
    var progress = scrollable > 0 ? clamp(window.scrollY / scrollable, 0, 1) : 0;
    return {
      scrollable: scrollable,
      progress: progress,
      short: isShortPage(scrollable),
    };
  }

  /**
   * Long page: X -50%→-20% (~50%→~80% visible), Y -12vh→52vh,
   *   scale 1→1.2→0.72, rotate -7.2deg→+21.6deg (≈ FIX01 × 1.20).
   * Short page: effective t max ~0.55; X end -38%; Y end 28vh;
   *   milder scale/rotation so Contacts does not dominate.
   */
  function applyState(metrics) {
    var tRaw = metrics.progress;
    if (reduceMotion.matches) {
      tRaw = 0.28;
    } else if (metrics.short) {
      tRaw = metrics.progress * 0.55;
    }

    var tEase = easeOutCubic(tRaw);

    var xStart = -50;
    var xEnd = metrics.short ? -38 : -20;
    var yStart = -12;
    var yEnd = metrics.short ? 28 : 52;

    // Mild left-edge arc bulge (more into view mid-journey).
    var arcAmp = metrics.short ? 4 : 8;
    var arc = Math.sin(Math.PI * tEase) * arcAmp;

    var x = xStart + (xEnd - xStart) * tEase + arc;
    var y = yStart + (yEnd - yStart) * tEase;
    var scale = scaleForProgress(tRaw, metrics.short);

    var rotStart = metrics.short ? -3.6 : -7.2;
    var rotEnd = metrics.short ? 12 : 21.6;
    var rotate = rotStart + (rotEnd - rotStart) * tEase;

    var xVal = x.toFixed(3) + '%';
    var yVal = y.toFixed(3) + 'vh';
    var scaleVal = scale.toFixed(4);
    var rotateVal = rotate.toFixed(3) + 'deg';

    // Dual-write CSS vars (debug / fallback) + direct transform (WebKit-safe path).
    root.style.setProperty('--fp02-lb-x', xVal);
    root.style.setProperty('--fp02-lb-y', yVal);
    root.style.setProperty('--fp02-lb-scale', scaleVal);
    root.style.setProperty('--fp02-lb-rotate', rotateVal);
    root.setAttribute('data-fp02-lb-mode', metrics.short ? 'short' : 'long');
    root.setAttribute('data-fp02-lb-progress', tRaw.toFixed(4));

    var transform =
      'translate3d(' + xVal + ', ' + yVal + ', 0) scale(' + scaleVal + ') rotate(' + rotateVal + ')';
    img.style.transform = transform;
    img.style.webkitTransform = transform;
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
