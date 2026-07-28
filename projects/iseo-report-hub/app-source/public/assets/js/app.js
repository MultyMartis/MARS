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
      const original = button.textContent || 'Copy';
      button.textContent = 'Copied';
      window.setTimeout(() => {
        button.textContent = original;
      }, 1600);
    }
  } catch (err) {
    if (button instanceof HTMLButtonElement) {
      button.textContent = 'Select & copy';
    }
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const stamp = document.createElement('span');
  stamp.className = 'js-status';
  stamp.hidden = true;
  stamp.textContent = 'js-ok';
  document.body.appendChild(stamp);

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
});
