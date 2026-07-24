/* i-SEO Report Hub — Phase 0 optional demo JS only */

document.documentElement.dataset.scaffold = 'phase-0';

document.addEventListener('DOMContentLoaded', () => {
  const stamp = document.createElement('span');
  stamp.className = 'js-status';
  stamp.hidden = true;
  stamp.textContent = 'js-ok';
  document.body.appendChild(stamp);
});
