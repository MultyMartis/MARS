function initNavToggle() {
  const toggle = document.querySelector('[data-nav-toggle]');
  const nav = document.querySelector('[data-nav]');
  if (!toggle || !nav) return;

  toggle.addEventListener('click', () => {
    const open = nav.classList.toggle('is-open');
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
}

function initAccordion(root) {
  const buttons = root.querySelectorAll('[data-accordion-button]');
  buttons.forEach((button) => {
    button.addEventListener('click', () => {
      const panel = button.parentElement.querySelector('[data-accordion-panel]');
      const expanded = button.getAttribute('aria-expanded') === 'true';

      root.querySelectorAll('[data-accordion-button]').forEach((btn) => {
        btn.setAttribute('aria-expanded', 'false');
      });
      root.querySelectorAll('[data-accordion-panel]').forEach((p) => {
        p.hidden = true;
      });

      if (!expanded) {
        button.setAttribute('aria-expanded', 'true');
        panel.hidden = false;
      }
    });
  });
}

function initAccordions() {
  document.querySelectorAll('[data-accordion]').forEach(initAccordion);
}

function initContactForm() {
  const form = document.querySelector('[data-contact-form]');
  if (!form) return;

  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const status = form.querySelector('[data-form-status]');
    if (status) {
      status.hidden = false;
      status.textContent = 'Синтетическая форма: отправка не выполняется (локальная заглушка).';
    }
  });
}

document.addEventListener('DOMContentLoaded', () => {
  initNavToggle();
  initAccordions();
  initContactForm();
});
