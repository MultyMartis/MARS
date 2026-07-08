
/* ==========================================================
   CORP CTA INFO PAGE FORMS (ZPM) — Run 4.230
   ========================================================== */
(function () {
  'use strict';

  var SELECTOR = '.zpm-corp-cta[data-corp-cta] form.zpm-form';
  var ENDPOINT = '/index.php?route=checkout/anketa';

  function initPhoneMask(scope) {
    var nodes = scope.querySelectorAll('[data-mask="phone"]');
    if (!nodes.length) return;
    if (window.Inputmask) {
      nodes.forEach(function (el) {
        if (el.dataset.maskInited === '1') return;
        window.Inputmask({
          mask: '+7 (999) 999-99-99',
          showMaskOnHover: false,
          clearIncomplete: true,
        }).mask(el);
        el.dataset.maskInited = '1';
      });
    } else if (window.jQuery && jQuery.fn.inputmask) {
      jQuery(nodes).inputmask({
        mask: '+7 (999) 999-99-99',
        showMaskOnHover: false,
        clearIncomplete: true,
      });
      nodes.forEach(function (el) { el.dataset.maskInited = '1'; });
    }
  }

  function initEmailValidation(scope) {
    var inputs = scope.querySelectorAll('[data-validate="email"]');
    var strictEmailRe = /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/;
    inputs.forEach(function (el) {
      if (el.dataset.emailInited === '1') return;
      el.dataset.emailInited = '1';
      function validate() {
        var v = (el.value || '').trim();
        if (!v) { el.setCustomValidity(''); return; }
        if (/[А-Яа-яЁё]/.test(v)) { el.setCustomValidity('Email должен быть латиницей'); return; }
        if (!strictEmailRe.test(v)) { el.setCustomValidity('Введите корректный email'); return; }
        el.setCustomValidity('');
      }
      el.addEventListener('input', validate);
      el.addEventListener('blur', validate);
    });
  }

  function showCorpCtaSuccess(formCard) {
    if (!formCard) return;
    var titleEl = formCard.querySelector('.zpm-corp-cta__form-title');
    var noteEl = formCard.querySelector('.zpm-corp-cta__form-note');
    var errEl = formCard.querySelector('.zpm-corp-cta__error');
    if (titleEl) titleEl.hidden = true;
    if (noteEl) noteEl.hidden = true;
    if (errEl) errEl.remove();
    var form = formCard.querySelector('form.zpm-form');
    if (form) form.remove();
    if (formCard.querySelector('.zpm-corp-cta__success')) return;
    var panel = document.createElement('div');
    panel.className = 'zpm-corp-cta__success zpm-fb__state';
    panel.setAttribute('role', 'status');
    panel.innerHTML = '<svg class="zpm-icon success zpm-icon--lg" aria-hidden="true" focusable="false"><use href="#zpm_ico__successful"></use></svg><div><h3 class="zpm-fb__title section-title__like-h3">Спасибо</h3><p class="zpm-fb__sub">Ваша заявка отправлена!</p></div>';
    formCard.appendChild(panel);
  }

  function showCorpCtaError(formCard, message) {
    if (!formCard) return;
    var errEl = formCard.querySelector('.zpm-corp-cta__error');
    if (!errEl) {
      errEl = document.createElement('div');
      errEl.className = 'zpm-corp-cta__error';
      errEl.setAttribute('role', 'alert');
      formCard.appendChild(errEl);
    }
    errEl.textContent = message || 'Произошла ошибка при отправке.';
    errEl.hidden = false;
  }

  function processCorpFetch(form, captchaToken, csrfToken, resolve, reject) {
    zpmFormAbortPending(form);
    var abortController = typeof AbortController !== 'undefined' ? new AbortController() : null;
    if (zpmFormPendingRequests && abortController) {
      zpmFormPendingRequests.set(form, abortController);
    }
    zpmFormSetLoading(form, true);

    var formData = new FormData(form);
    formData.append('csrf_token', csrfToken);
    if (captchaToken) {
      formData.append('g-recaptcha-response', captchaToken);
    }

    var fetchOpts = { method: 'POST', body: formData };
    if (abortController) {
      fetchOpts.signal = abortController.signal;
    }

    fetch(ENDPOINT, fetchOpts)
      .then(function (response) { return response.json(); })
      .then(function (data) {
        if (data.ok) {
          resolve(data);
        } else if (data.message && data.message.indexOf('CSRF') !== -1) {
          reject(new Error('Ошибка безопасности: истек токен CSRF. Обновите страницу.'));
        } else {
          reject(new Error(data.message || 'Ошибка обработки'));
        }
      })
      .catch(function (error) {
        if (error && error.name === 'AbortError') {
          reject(new Error(ZPM_FORM_ABORTED));
          return;
        }
        reject(error);
      })
      .finally(function () {
        if (zpmFormPendingRequests) {
          zpmFormPendingRequests.delete(form);
        }
        zpmFormSetLoading(form, false);
      });
  }

  function sendCorpForm(form) {
    return new Promise(function (resolve, reject) {
      var csrfToken = document.querySelector('meta[name="csrf-token"]')?.getAttribute('content');
      if (!csrfToken) {
        reject(new Error('Ошибка безопасности: отсутствует CSRF токен'));
        return;
      }
      var siteKey = document.querySelector('script[src*="google.com/recaptcha"]')?.getAttribute('data-sitekey');
      if (window.grecaptcha && siteKey) {
        grecaptcha.ready(function () {
          grecaptcha.execute(siteKey, { action: 'submit' }).then(function (token) {
            processCorpFetch(form, token, csrfToken, resolve, reject);
          });
        });
      } else {
        processCorpFetch(form, null, csrfToken, resolve, reject);
      }
    });
  }

  function onSubmit(e) {
    e.preventDefault();
    var form = e.target;
    var formCard = form.closest('.zpm-corp-cta__form-card');

    if (typeof form.checkValidity === 'function' && !form.checkValidity()) {
      if (typeof form.reportValidity === 'function') form.reportValidity();
      return;
    }

    var agreeCheckbox = form.querySelector('[name="agree"]');
    if (agreeCheckbox && !agreeCheckbox.checked) {
      showCorpCtaError(formCard, 'Пожалуйста, подтвердите согласие на обработку данных');
      return;
    }

    var errEl = formCard ? formCard.querySelector('.zpm-corp-cta__error') : null;
    if (errEl) errEl.hidden = true;

    sendCorpForm(form)
      .then(function () {
        showCorpCtaSuccess(formCard);
      })
      .catch(function (err) {
        if (err && err.message === ZPM_FORM_ABORTED) return;
        showCorpCtaError(formCard, err.message || 'Произошла ошибка при отправке.');
      });
  }

  function initCorpCtaForms() {
    document.querySelectorAll(SELECTOR).forEach(function (form) {
      if (form.dataset.zpmCorpCtaInited === '1') return;
      form.dataset.zpmCorpCtaInited = '1';
      initPhoneMask(form);
      initEmailValidation(form);
      form.addEventListener('submit', onSubmit);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initCorpCtaForms);
  } else {
    initCorpCtaForms();
  }
})();
