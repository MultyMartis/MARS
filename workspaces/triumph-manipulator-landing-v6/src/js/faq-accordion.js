const FAQ_ITEM_SELECTOR = '.faq-item';

/**
 * @param {HTMLDetailsElement} item
 */
function syncSummaryAriaExpanded(item) {
  const summary = item.querySelector('summary');

  if (summary instanceof HTMLElement) {
    summary.setAttribute('aria-expanded', item.open ? 'true' : 'false');
  }
}

function initFaqAccordion() {
  const items = Array.from(document.querySelectorAll(FAQ_ITEM_SELECTOR)).filter(
    (item) => item instanceof HTMLDetailsElement,
  );

  if (!items.length) {
    return;
  }

  let isClosingOthers = false;

  items.forEach((item) => {
    syncSummaryAriaExpanded(item);

    item.addEventListener('toggle', () => {
      syncSummaryAriaExpanded(item);

      if (isClosingOthers) {
        return;
      }

      if (!item.open) {
        return;
      }

      isClosingOthers = true;

      items.forEach((otherItem) => {
        if (otherItem !== item && otherItem.open) {
          otherItem.open = false;
          syncSummaryAriaExpanded(otherItem);
        }
      });

      isClosingOthers = false;
    });
  });
}

initFaqAccordion();
