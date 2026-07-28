/* i-SEO Report Hub — progressive enhancement marker */

document.documentElement.dataset.scaffold = 'auth-persistence';

document.addEventListener('DOMContentLoaded', () => {
  const stamp = document.createElement('span');
  stamp.className = 'js-status';
  stamp.hidden = true;
  stamp.textContent = 'js-ok';
  document.body.appendChild(stamp);

  const onceBox = document.querySelector('[data-share-once]');
  if (!onceBox) {
    return;
  }
  const input = onceBox.querySelector('[data-share-url]');
  const copyBtn = onceBox.querySelector('[data-share-copy]');
  if (!(input instanceof HTMLInputElement) || !(copyBtn instanceof HTMLButtonElement)) {
    return;
  }
  copyBtn.addEventListener('click', async () => {
    const value = input.value;
    try {
      if (navigator.clipboard && typeof navigator.clipboard.writeText === 'function') {
        await navigator.clipboard.writeText(value);
      } else {
        input.select();
        document.execCommand('copy');
      }
      copyBtn.textContent = 'Copied';
      window.setTimeout(() => {
        copyBtn.textContent = 'Copy';
      }, 1600);
    } catch (err) {
      input.select();
      copyBtn.textContent = 'Select & copy';
    }
  });
});
