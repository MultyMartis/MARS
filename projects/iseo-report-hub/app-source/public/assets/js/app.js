/* i-SEO Report Hub — progressive enhancement marker */

document.documentElement.dataset.scaffold = 'auth-persistence';

document.addEventListener('DOMContentLoaded', () => {
  const stamp = document.createElement('span');
  stamp.className = 'js-status';
  stamp.hidden = true;
  stamp.textContent = 'js-ok';
  document.body.appendChild(stamp);
});
