/**
 * Website Factory — form core (AJAX placeholder — swap endpoint per project)
 */
(function (global) {
  'use strict';

  var SUBMIT_ENDPOINT = null; // set data-form-endpoint on form for real POST

  function showStatus(form, message, type) {
    var status = form.querySelector('.wf-form__status');
    if (!status) return;
    status.hidden = !message;
    status.textContent = message || '';
    form.classList.remove('is-success', 'is-error');
    if (type) form.classList.add('is-' + type);
  }

  function setFieldError(field, message) {
    var wrap = field.closest('.wf-field');
    if (!wrap) return;
    var err = wrap.querySelector('.wf-field__error');
    if (message) {
      wrap.classList.add('has-error');
      if (err) {
        err.textContent = message;
        err.hidden = false;
      }
    } else {
      wrap.classList.remove('has-error');
      if (err) {
        err.textContent = '';
        err.hidden = true;
      }
    }
  }

  function validateField(control) {
    if (!control) return true;
    if (!control.checkValidity()) {
      setFieldError(control, control.validationMessage || 'Invalid value');
      return false;
    }
    setFieldError(control, '');
    return true;
  }

  function validateForm(form) {
    var controls = form.querySelectorAll('.wf-field__control');
    var firstInvalid = null;
    var valid = true;
    controls.forEach(function (control) {
      if (!validateField(control)) {
        valid = false;
        if (!firstInvalid) firstInvalid = control;
      }
    });
    if (firstInvalid) firstInvalid.focus();
    return valid;
  }

  function setLoading(form, loading) {
    form.classList.toggle('is-loading', loading);
    var btn = form.querySelector('.wf-form__submit');
    if (btn) btn.disabled = loading;
  }

  function submitForm(form) {
    var endpoint =
      form.getAttribute('data-form-endpoint') ||
      SUBMIT_ENDPOINT ||
      form.getAttribute('action');

    if (!endpoint || endpoint === '#') {
      return mockSubmit(form);
    }

    setLoading(form, true);
    showStatus(form, '', null);

    var body = new FormData(form);
    var controller = new AbortController();
    form.__wfAbortController = controller;

    return fetch(endpoint, {
      method: form.getAttribute('method') || 'POST',
      body: body,
      signal: controller.signal
    })
      .then(function (res) {
        if (!res.ok) throw new Error('Server error');
        return res.json().catch(function () {
          return {};
        });
      })
      .then(function () {
        form.classList.add('is-success');
        showStatus(form, 'Thank you — we will contact you shortly.', 'success');
      })
      .catch(function () {
        form.classList.add('is-error');
        showStatus(form, 'Something went wrong. Please try again.', 'error');
      })
      .finally(function () {
        setLoading(form, false);
        delete form.__wfAbortController;
      });
  }

  function mockSubmit(form) {
    setLoading(form, true);
    showStatus(form, '', null);
    return new Promise(function (resolve) {
      setTimeout(resolve, 800);
    }).then(function () {
      form.classList.add('is-success');
      showStatus(form, 'Thank you — reference demo (no backend).', 'success');
    }).finally(function () {
      setLoading(form, false);
    });
  }

  function initForm(root) {
    if (root.__wfFormBound) return;
    root.__wfFormBound = true;

    function onBlur(e) {
      if (e.target.classList.contains('wf-field__control')) {
        validateField(e.target);
      }
    }

    function onSubmit(e) {
      e.preventDefault();
      if (root.classList.contains('is-loading')) return;
      if (!validateForm(root)) return;
      submitForm(root);
    }

    root.__wfFormBlur = onBlur;
    root.__wfFormSubmit = onSubmit;
    root.addEventListener('blur', onBlur, true);
    root.addEventListener('submit', onSubmit);
  }

  function destroyForm(root) {
    if (!root.__wfFormBound) return;
    if (root.__wfAbortController) {
      root.__wfAbortController.abort();
      delete root.__wfAbortController;
    }
    root.removeEventListener('blur', root.__wfFormBlur, true);
    root.removeEventListener('submit', root.__wfFormSubmit);
    delete root.__wfFormBlur;
    delete root.__wfFormSubmit;
    delete root.__wfFormBound;
    setLoading(root, false);
  }

  if (global.WfLifecycle) {
    global.WfLifecycle.registerModule('form', {
      init: initForm,
      destroy: destroyForm
    });
  }
})(typeof window !== 'undefined' ? window : global);
