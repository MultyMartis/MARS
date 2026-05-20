/**
 * Section swap demo — paste into browser console after opening dist/index.html
 * Requires WfLifecycle loaded. See section-swap-demo-flow-v1.md
 */
(function () {
  'use strict';

  var hero = document.querySelector('[data-block-id="hero"]');
  if (!hero || !window.WfLifecycle) {
    console.error('[WF Demo] hero section or WfLifecycle missing');
    return;
  }

  var variantHtml =
    '<div class="wf-hero__overlay" aria-hidden="true"></div>' +
    '<div class="wf-container wf-hero__inner">' +
    '<h1 class="wf-hero__title">Swapped hero (demo)</h1>' +
    '<p class="wf-hero__lead">replaceSectionContent ran: destroy → innerHTML → init.</p>' +
    '<div class="wf-hero__actions">' +
    '<button type="button" class="wf-hero__cta" data-modal-open="modal-callback">Modal still works</button>' +
    '</div></div>' +
    '<div id="hero-sentinel" class="wf-hero-sentinel" aria-hidden="true"></div>';

  console.log('[WF Demo] swapping hero…');
  window.WfLifecycle.replaceSectionContent(hero, variantHtml);
  console.log('[WF Demo] done — open modal from new CTA; scroll to test sticky sentinel');
})();
