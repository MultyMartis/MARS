const FAQ_ITEM_SELECTOR = '.faq-item';
const FAQ_SECTION_ID = 'faq';
const MOBILE_MQ = window.matchMedia('(max-width: 860px)');
const REDUCED_MQ = window.matchMedia('(prefers-reduced-motion: reduce)');
const FAQ_TRANSITION_MS = 320;

/**
 * @param {HTMLElement} item
 * @returns {HTMLElement | null}
 */
function getFaqBody(item) {
  return item.querySelector('.faq-item__body');
}

/**
 * @param {HTMLElement} body
 * @returns {number}
 */
function measureFaqBodyHeight(body) {
  const inner = body.firstElementChild;
  if (!(inner instanceof HTMLElement)) {
    return 0;
  }

  const previousMaxHeight = body.style.maxHeight;
  body.style.maxHeight = 'none';
  const height = inner.scrollHeight;
  body.style.maxHeight = previousMaxHeight;
  return height;
}

/**
 * @param {HTMLElement} body
 * @param {() => void} onComplete
 */
function afterBodyTransition(body, onComplete) {
  if (REDUCED_MQ.matches) {
    onComplete();
    return;
  }

  let completed = false;

  const finish = () => {
    if (completed) {
      return;
    }

    completed = true;
    body.removeEventListener('transitionend', onTransitionEnd);
    onComplete();
  };

  const onTransitionEnd = (event) => {
    if (event.target !== body || event.propertyName !== 'max-height') {
      return;
    }

    finish();
  };

  body.addEventListener('transitionend', onTransitionEnd);
  window.setTimeout(finish, FAQ_TRANSITION_MS + 80);
}

/**
 * @param {HTMLElement} item
 */
function setExpandedClass(item, isExpanded) {
  item.classList.toggle('faq-item--expanded', isExpanded);
}

/**
 * @param {HTMLElement} item
 */
function initOpenFaqItem(item) {
  const body = getFaqBody(item);
  if (!body) {
    return;
  }

  setExpandedClass(item, true);
  body.style.maxHeight = 'none';
}

/**
 * @param {HTMLElement} item
 * @param {() => void} [onComplete]
 */
function openFaqItem(item, onComplete) {
  const body = getFaqBody(item);
  if (!body) {
    onComplete?.();
    return;
  }

  item.setAttribute('open', '');

  const targetHeight = measureFaqBodyHeight(body);

  if (REDUCED_MQ.matches) {
    setExpandedClass(item, true);
    body.style.maxHeight = `${targetHeight}px`;
    onComplete?.();
    return;
  }

  body.style.maxHeight = '0px';
  setExpandedClass(item, true);

  window.requestAnimationFrame(() => {
    window.requestAnimationFrame(() => {
      body.style.maxHeight = `${targetHeight}px`;
      afterBodyTransition(body, () => {
        body.style.maxHeight = 'none';
        onComplete?.();
      });
    });
  });
}

/**
 * @param {HTMLElement} item
 * @param {() => void} [onComplete]
 */
function closeFaqItem(item, onComplete) {
  const body = getFaqBody(item);

  if (!body || !item.hasAttribute('open')) {
    onComplete?.();
    return;
  }

  const currentHeight = body.style.maxHeight === 'none' ? measureFaqBodyHeight(body) : body.scrollHeight;

  if (REDUCED_MQ.matches) {
    setExpandedClass(item, false);
    body.style.maxHeight = '0px';
    item.removeAttribute('open');
    onComplete?.();
    return;
  }

  body.style.maxHeight = `${currentHeight}px`;
  setExpandedClass(item, false);

  window.requestAnimationFrame(() => {
    window.requestAnimationFrame(() => {
      body.style.maxHeight = '0px';
      afterBodyTransition(body, () => {
        item.removeAttribute('open');
        body.style.maxHeight = '';
        onComplete?.();
      });
    });
  });
}

/**
 * @param {HTMLElement} target
 */
function scrollToFaqTarget(target) {
  if (!MOBILE_MQ.matches || !(target instanceof HTMLElement)) {
    return;
  }

  const behavior = REDUCED_MQ.matches ? 'auto' : 'smooth';
  target.scrollIntoView({ behavior, block: 'nearest' });
}

/**
 * @param {HTMLElement | null} section
 */
function scrollToFaqSection(section) {
  if (!MOBILE_MQ.matches) {
    return;
  }

  const target = section || document.getElementById(FAQ_SECTION_ID);
  if (!(target instanceof HTMLElement)) {
    return;
  }

  const behavior = REDUCED_MQ.matches ? 'auto' : 'smooth';
  target.scrollIntoView({ behavior, block: 'start' });
}

function initFaqAccordion() {
  const items = Array.from(document.querySelectorAll(FAQ_ITEM_SELECTOR));

  if (!items.length) {
    return;
  }

  const section = document.getElementById(FAQ_SECTION_ID);

  items.forEach((item) => {
    if (!(item instanceof HTMLDetailsElement)) {
      return;
    }

    if (item.hasAttribute('open')) {
      initOpenFaqItem(item);
    }

    const summary = item.querySelector('summary');
    if (!(summary instanceof HTMLElement)) {
      return;
    }

    summary.addEventListener('click', (event) => {
      event.preventDefault();

      const wasOpen = item.hasAttribute('open');

      if (wasOpen) {
        closeFaqItem(item, () => {
          scrollToFaqSection(section);
        });
        return;
      }

      items.forEach((otherItem) => {
        if (otherItem !== item && otherItem.hasAttribute('open')) {
          closeFaqItem(otherItem);
        }
      });

      openFaqItem(item, () => {
        scrollToFaqTarget(item);
      });
    });
  });
}

initFaqAccordion();
