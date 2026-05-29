const FORM_SELECTOR = '[data-form]';
const FORM_ROOT_INIT = 'data-form-system';
const PHONE_DIGITS_MIN = 10;
const DEFAULT_FORM_ENDPOINT = 'backend/send-lead.php';
const SITE_CONFIG_ENDPOINT = 'backend/site-config.php';
const METRIKA_COUNTER_ID = 109490539;
const METRIKA_GOAL_NAME = 'form-lead';

/** @type {Promise<{ recaptchaSiteKey: string }> | null} */
let siteConfigPromise = null;
/** @type {Promise<void> | null} */
let recaptchaScriptPromise = null;

/**
 * @param {HTMLFormElement} form
 */
function ensureStatusElement(form) {
  let status = form.querySelector('[data-form-status]');

  if (!(status instanceof HTMLElement)) {
    status = document.createElement('div');
    status.className = 'site-form__status';
    status.dataset.formStatus = '';
    status.setAttribute('role', 'status');
    status.setAttribute('aria-live', 'polite');
    status.hidden = true;
    form.appendChild(status);
  }

  return status;
}

/**
 * @param {HTMLFormElement} form
 */
function ensureHiddenFields(form) {
  let container = form.querySelector('[data-form-hidden]');

  if (!(container instanceof HTMLElement)) {
    container = document.createElement('div');
    container.className = 'site-form__hidden';
    container.dataset.formHidden = '';
    container.setAttribute('aria-hidden', 'true');
    form.prepend(container);
  }

  const fieldNames = [
    'page_url',
    'page_title',
    'page_referrer',
    'page_type',
    'form_id',
    'form_name',
    'cta_source',
    'timestamp',
    'form_started_at',
    'company_url',
    'g-recaptcha-response',
    'landing_id',
  ];

  fieldNames.forEach((name) => {
    let input = container.querySelector(`[data-form-field="${name}"]`);

    if (!(input instanceof HTMLInputElement)) {
      input = document.createElement('input');
      input.type = 'hidden';
      input.name = name;
      input.dataset.formField = name;
      if (name === 'company_url') {
        input.tabIndex = -1;
        input.autocomplete = 'off';
        input.setAttribute('aria-hidden', 'true');
      }
      container.appendChild(input);
    }
  });

  return container;
}

/**
 * @param {HTMLFormElement} form
 */
function populateHiddenFields(form) {
  const container = ensureHiddenFields(form);
  const setValue = (name, value) => {
    const input = container.querySelector(`[data-form-field="${name}"]`);
    if (input instanceof HTMLInputElement) {
      input.value = value;
    }
  };

  setValue('page_url', window.location.href);
  setValue('page_title', document.title || '');
  setValue('page_referrer', document.referrer || '');
  setValue('page_type', form.getAttribute('data-page-type') || document.body.dataset.pageType || 'landing');
  setValue('form_id', form.getAttribute('data-form-id') || form.id || 'form');
  setValue('form_name', form.getAttribute('data-form-name') || form.getAttribute('aria-label') || 'form');
  setValue('cta_source', form.getAttribute('data-cta-source') || '');
  setValue(
    'landing_id',
    document.body.dataset.landingId ||
      document.body.dataset.pageType ||
      form.getAttribute('data-page-type') ||
      'triumph-v5'
  );

  const startedAtInput = container.querySelector('[data-form-field="form_started_at"]');
  if (startedAtInput instanceof HTMLInputElement && !startedAtInput.value) {
    startedAtInput.value = new Date().toISOString();
  }

  setValue('timestamp', new Date().toISOString());
  setValue('company_url', '');
}

/**
 * @param {HTMLFormElement} form
 * @param {string} ctaSource
 */
function setFormCtaSource(form, ctaSource) {
  form.setAttribute('data-cta-source', ctaSource);
  populateHiddenFields(form);
}

/**
 * @param {HTMLInputElement} input
 */
function bindPhoneMask(input) {
  if (input.dataset.phoneMaskBound === 'true') {
    return;
  }

  input.dataset.phoneMaskBound = 'true';
  input.setAttribute('inputmode', 'tel');
  input.setAttribute('autocomplete', input.getAttribute('autocomplete') || 'tel');

  input.addEventListener('input', () => {
    const digits = input.value.replace(/\D/g, '');
    let normalized = digits;

    if (normalized.startsWith('8')) {
      normalized = `7${normalized.slice(1)}`;
    }

    if (!normalized.startsWith('7') && normalized.length > 0) {
      normalized = `7${normalized}`;
    }

    normalized = normalized.slice(0, 11);

    if (!normalized) {
      input.value = '';
      return;
    }

    const local = normalized.slice(1);
    let formatted = '+7';

    if (local.length > 0) {
      formatted += ` (${local.slice(0, 3)}`;
    }
    if (local.length >= 3) {
      formatted += `) ${local.slice(3, 6)}`;
    }
    if (local.length >= 6) {
      formatted += `-${local.slice(6, 8)}`;
    }
    if (local.length >= 8) {
      formatted += `-${local.slice(8, 10)}`;
    }

    input.value = formatted;
  });
}

/**
 * @param {HTMLElement} field
 * @returns {string}
 */
function getFieldMessage(field) {
  const wrapper =
    field.closest('[data-form-field-wrap]') || field.closest('label') || field.parentElement;
  const customMessage = wrapper?.querySelector('[data-form-error]')?.textContent?.trim();

  if (customMessage) {
    return customMessage;
  }

  const rules = (field.getAttribute('data-validate') || '').split(/\s+/).filter(Boolean);

  if (field.matches('[type="tel"], [name="phone"], [data-validate*="phone"]')) {
    return 'Укажите корректный номер телефона';
  }

  if (
    field instanceof HTMLInputElement &&
    field.type === 'checkbox' &&
    (field.name === 'consent' || rules.includes('consent'))
  ) {
    return 'Подтвердите согласие на обработку данных';
  }

  return 'Заполните это поле';
}

/**
 * @param {HTMLElement} field
 * @returns {boolean}
 */
function validateField(field) {
  if (
    !(field instanceof HTMLInputElement || field instanceof HTMLTextAreaElement || field instanceof HTMLSelectElement)
  ) {
    return true;
  }

  const wrapper =
    field.closest('[data-form-field-wrap]') || field.closest('label') || field.parentElement;

  let isValid = true;
  const rules = (field.getAttribute('data-validate') || '').split(/\s+/).filter(Boolean);
  const isRequired = field.required || rules.includes('required') || field.getAttribute('data-required') === 'true';
  const value = field.value.trim();

  if (field instanceof HTMLInputElement && field.type === 'checkbox') {
    if (isRequired && !field.checked) {
      isValid = false;
    }
  } else if (isRequired && !value) {
    isValid = false;
  }

  if (isValid && (field.type === 'tel' || field.name === 'phone' || rules.includes('phone'))) {
    const digits = value.replace(/\D/g, '');
    isValid = digits.length >= PHONE_DIGITS_MIN;
  }

  if (isValid && (field.name === 'name' || rules.includes('name')) && value.length > 0 && value.length < 2) {
    isValid = false;
  }

  const hasValue =
    field instanceof HTMLInputElement && field.type === 'checkbox' ? field.checked : value.length > 0;

  if (wrapper) {
    wrapper.classList.toggle('is-invalid', !isValid);
    wrapper.classList.toggle('is-valid', isValid && hasValue);
    const errorId = field.getAttribute('aria-describedby');
    const errorEl = errorId ? document.getElementById(errorId) : wrapper.querySelector('[data-form-error]');

    if (errorEl) {
      errorEl.textContent = isValid ? '' : getFieldMessage(field);
      errorEl.hidden = isValid;
    }

    field.setAttribute('aria-invalid', String(!isValid));
  }

  return isValid;
}

/**
 * @param {HTMLFormElement} form
 */
function validateForm(form) {
  const fields = form.querySelectorAll('input, textarea, select');
  let isValid = true;

  fields.forEach((field) => {
    if (
      field instanceof HTMLInputElement &&
      (field.type === 'hidden' || field.disabled || field.closest('[data-form-hidden]'))
    ) {
      return;
    }

    if (!validateField(field)) {
      isValid = false;
    }
  });

  return isValid;
}

/**
 * @param {HTMLFormElement} form
 */
function setFormState(form, state) {
  form.classList.remove('is-loading', 'is-success', 'is-error', 'is-success-locked');
  form.dataset.formState = state;

  if (state === 'idle') {
    delete form.dataset.formState;
    releaseSuccessLock(form);
    return;
  }

  form.classList.add(`is-${state}`);
}

/**
 * @param {HTMLFormElement} form
 */
function applySuccessLock(form) {
  form.classList.add('is-success-locked');

  form.querySelectorAll('input, textarea, select, button').forEach((control) => {
    if (!(control instanceof HTMLInputElement || control instanceof HTMLTextAreaElement || control instanceof HTMLSelectElement || control instanceof HTMLButtonElement)) {
      return;
    }

    if (control instanceof HTMLInputElement && (control.type === 'hidden' || control.closest('[data-form-hidden]'))) {
      return;
    }

    if (control.closest('.site-form__reach')) {
      return;
    }

    control.disabled = true;
  });
}

/**
 * @param {HTMLFormElement} form
 */
function releaseSuccessLock(form) {
  form.classList.remove('is-success-locked');

  form.querySelectorAll('input, textarea, select, button').forEach((control) => {
    if (control instanceof HTMLInputElement && control.type === 'hidden') {
      return;
    }

    control.disabled = false;
  });
}

/**
 * @param {HTMLFormElement} form
 * @param {'success' | 'error' | 'loading' | ''} type
 * @param {string} message
 */
function showFormStatus(form, type, message) {
  const status = ensureStatusElement(form);
  status.hidden = !message;
  status.className = 'site-form__status';

  if (type) {
    status.classList.add(`site-form__status--${type}`);
  }

  status.textContent = message;
}

/**
 * @param {HTMLFormElement} form
 */
function resetFormUi(form) {
  releaseSuccessLock(form);
  setFormState(form, 'idle');
  showFormStatus(form, '', '');
  form.querySelectorAll('.is-invalid, .is-valid').forEach((element) => {
    element.classList.remove('is-invalid', 'is-valid');
  });

  form.querySelectorAll('[aria-invalid="true"]').forEach((field) => {
    if (field instanceof HTMLElement) {
      field.setAttribute('aria-invalid', 'false');
    }
  });
}

/**
 * Fire Yandex Metrika lead goal after confirmed backend success only.
 */
function trackLeadGoal() {
  try {
    if (typeof window.ym === 'function') {
      window.ym(METRIKA_COUNTER_ID, 'reachGoal', METRIKA_GOAL_NAME);
    }
  } catch {
    // Metrika blocked or unavailable — must not affect form UX.
  }
}

/**
 * @returns {Promise<{ recaptchaSiteKey: string }>}
 */
async function loadSiteConfig() {
  if (isFileProtocolPreview()) {
    return { recaptchaSiteKey: '' };
  }

  if (!siteConfigPromise) {
    siteConfigPromise = fetch(SITE_CONFIG_ENDPOINT, {
      method: 'GET',
      headers: { Accept: 'application/json' },
      credentials: 'same-origin',
    })
      .then(async (response) => {
        if (!response.ok) {
          return { recaptchaSiteKey: '' };
        }

        const data = await response.json().catch(() => null);

        if (!data || typeof data !== 'object') {
          return { recaptchaSiteKey: '' };
        }

        const key = typeof data.recaptchaSiteKey === 'string' ? data.recaptchaSiteKey.trim() : '';

        return { recaptchaSiteKey: key };
      })
      .catch(() => ({ recaptchaSiteKey: '' }));
  }

  return siteConfigPromise;
}

/**
 * @param {string} siteKey
 * @returns {Promise<void>}
 */
function loadRecaptchaScript(siteKey) {
  if (!siteKey || recaptchaScriptPromise) {
    return recaptchaScriptPromise || Promise.resolve();
  }

  recaptchaScriptPromise = new Promise((resolve, reject) => {
    if (typeof window.grecaptcha !== 'undefined' && typeof window.grecaptcha.execute === 'function') {
      resolve();
      return;
    }

    const existing = document.querySelector('script[data-recaptcha-loader="true"]');
    if (existing) {
      existing.addEventListener('load', () => resolve(), { once: true });
      existing.addEventListener('error', () => reject(new Error('recaptcha_script_failed')), { once: true });
      return;
    }

    const script = document.createElement('script');
    script.src = `https://www.google.com/recaptcha/api.js?render=${encodeURIComponent(siteKey)}`;
    script.async = true;
    script.defer = true;
    script.dataset.recaptchaLoader = 'true';
    script.onload = () => resolve();
    script.onerror = () => reject(new Error('recaptcha_script_failed'));
    document.head.appendChild(script);
  });

  return recaptchaScriptPromise;
}

/**
 * @param {HTMLFormElement} form
 * @param {FormData} formData
 */
async function appendRecaptchaToken(form, formData) {
  const handler = form.getAttribute('data-form-handler');

  if (handler === 'mock' || isFileProtocolPreview()) {
    return;
  }

  const { recaptchaSiteKey } = await loadSiteConfig();

  if (!recaptchaSiteKey || recaptchaSiteKey === 'PASTE_SITE_KEY_HERE') {
    return;
  }

  try {
    await loadRecaptchaScript(recaptchaSiteKey);

    if (typeof window.grecaptcha === 'undefined' || typeof window.grecaptcha.execute !== 'function') {
      return;
    }

    await new Promise((resolve) => {
      window.grecaptcha.ready(resolve);
    });

    const token = await window.grecaptcha.execute(recaptchaSiteKey, { action: 'submit' });

    if (typeof token === 'string' && token) {
      formData.set('g-recaptcha-response', token);
      const hidden = form.querySelector('[data-form-field="g-recaptcha-response"]');
      if (hidden instanceof HTMLInputElement) {
        hidden.value = token;
      }
    }
  } catch {
    // If reCAPTCHA fails client-side, backend policy decides; do not block UI here.
  }
}

/**
 * @param {HTMLFormElement} form
 */
function collectPayload(form) {
  const formData = new FormData(form);
  /** @type {Record<string, string>} */
  const payload = {};

  formData.forEach((value, key) => {
    if (typeof value === 'string') {
      payload[key] = value;
    }
  });

  return payload;
}

/**
 * @param {HTMLFormElement} form
 * @param {Record<string, string>} payload
 */
async function mockSubmitHandler(form, payload) {
  const delay = Number(form.getAttribute('data-form-mock-delay')) || 900;
  await new Promise((resolve) => window.setTimeout(resolve, delay));

  if (form.getAttribute('data-form-mock-fail') === 'true') {
    throw new Error('mock_submit_failed');
  }

  return { ok: true, payload, mode: 'mock' };
}

/**
 * @param {HTMLFormElement} form
 * @returns {string}
 */
function resolveFormEndpoint(form) {
  return form.getAttribute('data-form-endpoint') || DEFAULT_FORM_ENDPOINT;
}

/**
 * @returns {boolean}
 */
function isFileProtocolPreview() {
  return window.location.protocol === 'file:';
}

/**
 * @param {Response} response
 * @returns {Promise<Record<string, unknown> | null>}
 */
async function parseJsonResponse(response) {
  const contentType = response.headers.get('content-type') || '';

  if (!contentType.includes('application/json')) {
    return null;
  }

  try {
    const data = await response.json();
    return data && typeof data === 'object' ? data : null;
  } catch {
    return null;
  }
}

/**
 * @param {HTMLFormElement} form
 * @param {Record<string, string>} payload
 */
async function productionSubmitHandler(form, payload) {
  if (isFileProtocolPreview()) {
    return mockSubmitHandler(form, payload);
  }

  const endpoint = resolveFormEndpoint(form);
  const formData = new FormData();

  Object.entries(payload).forEach(([key, value]) => {
    formData.append(key, value);
  });

  await appendRecaptchaToken(form, formData);

  let response;

  try {
    response = await fetch(endpoint, {
      method: 'POST',
      body: formData,
      headers: {
        Accept: 'application/json',
      },
      credentials: 'same-origin',
    });
  } catch {
    const error = new Error('form_endpoint_unavailable');
    error.userMessage =
      'Сервер формы недоступен. Откройте страницу через HTTP или позвоните нам.';
    throw error;
  }

  const data = await parseJsonResponse(response);

  if (!response.ok) {
    const error = new Error('form_submit_failed');
    error.userMessage =
      (data && typeof data.message === 'string' && data.message) ||
      'Не удалось отправить заявку. Позвоните нам или попробуйте ещё раз.';
    throw error;
  }

  if (data && (data.ok === false || data.success === false)) {
    const error = new Error('form_submit_failed');
    error.userMessage =
      (typeof data.message === 'string' && data.message) ||
      'Не удалось отправить заявку. Позвоните нам или попробуйте ещё раз.';
    throw error;
  }

  return { ok: true, payload, data, mode: 'production' };
}

/**
 * @param {HTMLFormElement} form
 * @param {Record<string, string>} payload
 */
async function runSubmitHandler(form, payload) {
  const handler = form.getAttribute('data-form-handler');

  if (handler === 'mock') {
    return mockSubmitHandler(form, payload);
  }

  return productionSubmitHandler(form, payload);
}

/**
 * @param {HTMLFormElement} form
 */
function bindConsentLinks(form) {
  form.querySelectorAll('.site-form__consent-text a[href]').forEach((link) => {
    link.addEventListener('click', (event) => {
      event.stopPropagation();
    });
  });
}

/**
 * @param {HTMLFormElement} form
 */
function bindFormFields(form) {
  form.querySelectorAll('input, textarea, select').forEach((field) => {
    if (
      field instanceof HTMLInputElement &&
      (field.type === 'hidden' || field.closest('[data-form-hidden]'))
    ) {
      return;
    }

    const wrapper =
      field.closest('[data-form-field-wrap]') || field.closest('label') || field.parentElement;

    if (wrapper && !wrapper.classList.contains('site-form__field')) {
      if (!(wrapper.classList.contains('site-form__consent') && wrapper.closest('.site-form__field--consent'))) {
        wrapper.classList.add('site-form__field');
      }
    }

    if (
      field instanceof HTMLInputElement &&
      (field.matches('[type="tel"], [name="phone"]') || field.hasAttribute('data-phone-mask'))
    ) {
      bindPhoneMask(field);
    }

    field.addEventListener('blur', () => {
      if (field.value.trim()) {
        validateField(field);
      }
    });

    const revalidateOnChange = () => {
      const wrap =
        field.closest('[data-form-field-wrap]') || field.closest('label') || field.parentElement;
      if (wrap?.classList.contains('is-invalid')) {
        validateField(field);
      }
    };

    if (field instanceof HTMLInputElement && field.type === 'checkbox') {
      field.addEventListener('change', revalidateOnChange);
    } else {
      field.addEventListener('input', revalidateOnChange);
    }
  });
}

/**
 * @param {HTMLFormElement} form
 */
function initForm(form) {
  if (form.dataset.formInit === 'true') {
    return;
  }

  form.dataset.formInit = 'true';
  form.classList.add('site-form');
  form.setAttribute('novalidate', 'novalidate');

  ensureHiddenFields(form);
  ensureStatusElement(form);
  populateHiddenFields(form);
  bindFormFields(form);
  bindConsentLinks(form);
  loadSiteConfig();

  const submitButton = form.querySelector('[type="submit"]');
  let submitLock = false;

  form.addEventListener('submit', async (event) => {
    event.preventDefault();

    if (
      submitLock ||
      form.classList.contains('is-loading') ||
      form.classList.contains('is-success') ||
      form.classList.contains('is-success-locked')
    ) {
      return;
    }

    populateHiddenFields(form);

    if (!validateForm(form)) {
      setFormState(form, 'error');
      showFormStatus(form, 'error', 'Проверьте поля формы и попробуйте снова.');
      const firstInvalid = form.querySelector('.is-invalid input, .is-invalid textarea, .is-invalid select');
      if (firstInvalid instanceof HTMLElement) {
        firstInvalid.focus();
      }
      return;
    }

    submitLock = true;
    setFormState(form, 'loading');
    showFormStatus(form, 'loading', 'Отправляем заявку…');

    if (submitButton instanceof HTMLButtonElement) {
      submitButton.disabled = true;
    }

    const payload = collectPayload(form);

    try {
      const submitResult = await runSubmitHandler(form, payload);
      setFormState(form, 'success');
      applySuccessLock(form);
      const successMessage =
        (typeof submitResult?.data?.message === 'string' && submitResult.data.message) ||
        form.getAttribute('data-form-success') ||
        'Заявка принята. Перезвоним в ближайшее время.';
      showFormStatus(form, 'success', successMessage);
      if (submitResult?.mode === 'production') {
        trackLeadGoal();
      }
      form.reset();
      populateHiddenFields(form);
      form.dispatchEvent(new CustomEvent('site-form:success', { detail: { payload }, bubbles: true }));
    } catch (error) {
      setFormState(form, 'error');
      const errorMessage =
        (error && typeof error.userMessage === 'string' && error.userMessage) ||
        form.getAttribute('data-form-error') ||
        'Не удалось отправить заявку. Позвоните нам или попробуйте ещё раз.';
      showFormStatus(form, 'error', errorMessage);
      form.dispatchEvent(
        new CustomEvent('site-form:error', { detail: { error, payload }, bubbles: true })
      );
    } finally {
      submitLock = false;
      if (submitButton instanceof HTMLButtonElement && !form.classList.contains('is-success')) {
        submitButton.disabled = false;
      }
    }
  });

  form.addEventListener('site-form:reset', () => {
    resetFormUi(form);
    if (submitButton instanceof HTMLButtonElement) {
      submitButton.disabled = false;
    }
    populateHiddenFields(form);
  });
}

function bindModalCtaBridge() {
  document.addEventListener('site-modal:cta', (event) => {
    if (!(event instanceof CustomEvent)) {
      return;
    }

    const modalId = event.detail?.modalId;
    const ctaSource = event.detail?.ctaSource;
    const modal = document.querySelector(`[data-modal-id="${modalId}"]`) || document.getElementById(modalId);

    if (!(modal instanceof HTMLElement) || !ctaSource) {
      return;
    }

    const form = modal.querySelector(FORM_SELECTOR);
    if (form instanceof HTMLFormElement) {
      setFormCtaSource(form, ctaSource);
    }
  });

  document.addEventListener('site-modal:open', (event) => {
    if (!(event instanceof CustomEvent)) {
      return;
    }

    const modalId = event.detail?.modalId;
    const modal = document.querySelector(`[data-modal-id="${modalId}"]`) || document.getElementById(modalId);

    if (!(modal instanceof HTMLElement)) {
      return;
    }

    const pendingCta = modal.dataset.pendingCtaSource || '';
    const form = modal.querySelector(FORM_SELECTOR);

    if (form instanceof HTMLFormElement) {
      populateHiddenFields(form);
      if (pendingCta) {
        setFormCtaSource(form, pendingCta);
        delete modal.dataset.pendingCtaSource;
      }
    }
  });
}

/**
 * @param {HTMLElement} [root]
 */
function initForms(root = document) {
  if (root === document && document.documentElement.getAttribute(FORM_ROOT_INIT) !== 'true') {
    document.documentElement.setAttribute(FORM_ROOT_INIT, 'true');
    bindModalCtaBridge();
  }

  root.querySelectorAll(FORM_SELECTOR).forEach((form) => {
    if (form instanceof HTMLFormElement) {
      initForm(form);
    }
  });
}
