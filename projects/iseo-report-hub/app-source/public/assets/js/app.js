/* i-SEO Report Hub — progressive enhancement marker */

document.documentElement.dataset.scaffold = 'auth-persistence';

async function copyTextValue(value, button) {
  try {
    if (navigator.clipboard && typeof navigator.clipboard.writeText === 'function') {
      await navigator.clipboard.writeText(value);
    } else {
      const tmp = document.createElement('textarea');
      tmp.value = value;
      tmp.setAttribute('readonly', '');
      tmp.style.position = 'absolute';
      tmp.style.left = '-9999px';
      document.body.appendChild(tmp);
      tmp.select();
      document.execCommand('copy');
      document.body.removeChild(tmp);
    }
    if (button instanceof HTMLButtonElement) {
      const original = button.textContent || 'Копировать';
      button.textContent = 'Скопировано';
      window.setTimeout(() => {
        button.textContent = original;
      }, 1600);
    }
  } catch (err) {
    if (button instanceof HTMLButtonElement) {
      button.textContent = 'Выделите и скопируйте';
    }
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const stamp = document.createElement('span');
  stamp.className = 'js-status';
  stamp.hidden = true;
  stamp.textContent = 'js-ok';
  document.body.appendChild(stamp);

  const toggle = document.querySelector('[data-sidebar-toggle]');
  if (toggle instanceof HTMLButtonElement) {
    let backdrop = document.querySelector('.sidebar-backdrop');
    if (!(backdrop instanceof HTMLElement)) {
      backdrop = document.createElement('div');
      backdrop.className = 'sidebar-backdrop';
      document.body.appendChild(backdrop);
    }
    const setOpen = (open) => {
      document.body.classList.toggle('sidebar-open', open);
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    };
    toggle.addEventListener('click', () => {
      setOpen(!document.body.classList.contains('sidebar-open'));
    });
    backdrop.addEventListener('click', () => setOpen(false));
  }

  const onceBox = document.querySelector('[data-share-once]');
  if (onceBox) {
    const input = onceBox.querySelector('[data-share-url]');
    const copyBtn = onceBox.querySelector('[data-share-copy]');
    if (input instanceof HTMLInputElement && copyBtn instanceof HTMLButtonElement) {
      copyBtn.addEventListener('click', () => {
        copyTextValue(input.value, copyBtn);
      });
    }
  }

  document.querySelectorAll('[data-copy-btn]').forEach((btn) => {
    if (!(btn instanceof HTMLButtonElement)) {
      return;
    }
    btn.addEventListener('click', () => {
      const block = btn.closest('.copy-pack-block');
      const target = block ? block.querySelector('[data-copy-target]') : null;
      let value = '';
      if (target instanceof HTMLTextAreaElement || target instanceof HTMLInputElement) {
        value = target.value;
      }
      if (value !== '') {
        copyTextValue(value, btn);
      }
    });
  });

  const applyForm = document.querySelector('[data-assembly-apply-form]');
  if (applyForm instanceof HTMLFormElement) {
    const submit = applyForm.querySelector('[data-assembly-apply-submit]');
    const confirm = applyForm.querySelector('[data-assembly-apply-confirm]');
    const boxes = document.querySelectorAll('[data-assembly-apply-block]');
    const syncApplySubmit = () => {
      const anyChecked = Array.from(boxes).some((box) => box instanceof HTMLInputElement && box.checked && !box.disabled);
      const confirmed = confirm instanceof HTMLInputElement && confirm.checked;
      if (submit instanceof HTMLButtonElement) {
        submit.disabled = !(anyChecked && confirmed);
      }
    };
    boxes.forEach((box) => {
      box.addEventListener('change', syncApplySubmit);
    });
    if (confirm instanceof HTMLInputElement) {
      confirm.addEventListener('change', syncApplySubmit);
    }
    applyForm.addEventListener('submit', (event) => {
      syncApplySubmit();
      if (submit instanceof HTMLButtonElement && submit.disabled) {
        event.preventDefault();
      }
    });
    syncApplySubmit();
  }

  // Field help (?): keep label clicks from focusing controls; Esc closes open panels.
  document.querySelectorAll('[data-field-help]').forEach((wrap) => {
    if (!(wrap instanceof HTMLElement)) {
      return;
    }
    wrap.addEventListener('click', (event) => {
      event.stopPropagation();
    });
    const details = wrap.querySelector('details.field-help__details');
    if (details instanceof HTMLDetailsElement) {
      details.addEventListener('toggle', () => {
        if (!details.open) {
          return;
        }
        document.querySelectorAll('details.field-help__details[open]').forEach((other) => {
          if (other !== details && other instanceof HTMLDetailsElement) {
            other.open = false;
          }
        });
      });
    }
  });

  document.addEventListener('keydown', (event) => {
    if (event.key !== 'Escape') {
      return;
    }
    document.querySelectorAll('details.field-help__details[open]').forEach((details) => {
      if (details instanceof HTMLDetailsElement) {
        details.open = false;
      }
    });
  });
});
