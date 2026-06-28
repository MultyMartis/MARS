
/* ==========================================================================
   M9.14 — Corp FAQ accordion (delivery + future corp pages)
   ========================================================================== */
(function () {
  "use strict";

  function initCorpAccordion(root) {
    if (!root) return;

    var items = root.querySelectorAll("[data-accordion-item]");
    if (!items.length) return;

    items.forEach(function (item) {
      var btn = item.querySelector("[data-accordion-button]");
      var panel = item.querySelector("[data-accordion-panel]");
      if (!btn || !panel) return;

      btn.addEventListener("click", function () {
        var isOpen = btn.getAttribute("aria-expanded") === "true";

        items.forEach(function (other) {
          var otherBtn = other.querySelector("[data-accordion-button]");
          var otherPanel = other.querySelector("[data-accordion-panel]");
          if (!otherBtn || !otherPanel) return;
          otherBtn.setAttribute("aria-expanded", "false");
          otherPanel.hidden = true;
          other.classList.remove("is-open");
        });

        if (!isOpen) {
          btn.setAttribute("aria-expanded", "true");
          panel.hidden = false;
          item.classList.add("is-open");
        }
      });
    });
  }

  function bootCorpAccordions() {
    document.querySelectorAll("[data-delivery-faq]").forEach(initCorpAccordion);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", bootCorpAccordions);
  } else {
    bootCorpAccordions();
  }
})();
