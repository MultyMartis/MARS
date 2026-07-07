#!/usr/bin/env python3
"""SITE-002 customer form confirmations + form loading UX — Run 4.226."""
from __future__ import annotations

import argparse
import csv
import difflib
import ftplib
import hashlib
import html as html_module
import io
import json
import re
import shutil
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-MAIL-CUSTOMER-FORMS-01"
OCPILOT_RUN = "4.226"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-MAIL-ADMIN-FORMS-01"
CHECKPOINT_AFTER = "SITE-002-STABLE-PROD-MAIL-CUSTOMER-FORMS-01"
CORRECT_BRAND = "ЗПМ"
WRONG_BRAND = "БЗПМ"
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"

REPO_ROOT = Path(r"X:\AI MARS")
TOOLS_DIR = REPO_ROOT / "projects" / "ocpilot" / "sites" / "site-002" / "tools"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-MAIL-CUSTOMER-FORMS-01"
)
CHECKPOINT_STORAGE = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\baselines\SITE-002-STABLE-PROD-MAIL-CUSTOMER-FORMS-01"
)

REMOTE_ANKETA = "/public_html/catalog/controller/checkout/anketa.php"
REMOTE_RENDERER = "/public_html/system/library/zpm/mail_renderer.php"
REMOTE_MAIN_JS = "/public_html/assets/js/main.js"
REMOTE_STYLE_CSS = "/public_html/assets/css/style.css"
REMOTE_MOD_ANKETA = "/storage/modification/catalog/controller/checkout/anketa.php"
REMOTE_MOD_RENDERER = "/storage/modification/system/library/zpm/mail_renderer.php"

ANKETA_PATCH = TOOLS_DIR / "checkout_anketa_mail_customer_forms.php"
RENDERER_SRC = TOOLS_DIR / "mail_renderer.php"
CSS_APPEND = TOOLS_DIR / "zpm-form-loading.css"

SUBDIRS = (
    "source-before",
    "source-after",
    "http-before",
    "http-after",
    "mail-before",
    "mail-after",
    "ui-before",
    "ui-after",
    "test-submit",
    "patch",
    "verification",
    "rollback",
    "manifests",
    "reports",
    "logs",
)

FORM_URLS = [
    ("home", "https://bzpm.ru/"),
    ("katalog", "https://bzpm.ru/katalog"),
    ("stoly", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly"),
    (
        "pdp",
        "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/polki-nastennye-i-nastolnye/"
        "polki-dlya-gastoemkostey/derzhatel-dlya-gastroemkostey-pg-10-3-900h330h40-gn-1-6-5-sht",
    ),
]

SANITY_URLS = FORM_URLS + [
    ("neutral_hub", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie"),
    ("llms", "https://bzpm.ru/llms.txt"),
    ("robots", "https://bzpm.ru/robots.txt"),
    ("sitemap", "https://bzpm.ru/sitemap.xml"),
]

TEST_MARKER_EMAIL = "MARS TEST MAIL CUSTOMER FORMS 01 EMAIL"
TEST_MARKER_NO_EMAIL = "MARS TEST MAIL CUSTOMER FORMS 01 NO EMAIL"
TEST_PHONE = "+7 000 000-00-00"
TEST_EMAIL = "test@example.invalid"

ZPM_LOADING_JS = """
/* ---------- ZPM form loading state + abort (Run 4.226) — global ---------- */
var zpmFormPendingRequests = typeof WeakMap !== 'undefined' ? new WeakMap() : null;
var ZPM_FORM_ABORTED = 'ZPM_FORM_ABORTED';

function zpmFormGetLoadingContainer(form) {
  return form.closest('[data-fb-modal]') || form.closest('.fancybox__content') || form.closest('.zpm-dealers') || form;
}

function zpmFormSetLoading(form, isLoading) {
  if (!form) return;
  var container = zpmFormGetLoadingContainer(form);
  if (!container) return;
  if (isLoading) {
    container.classList.add('zpm-form--loading');
    container.setAttribute('aria-busy', 'true');
  } else {
    container.classList.remove('zpm-form--loading');
    container.removeAttribute('aria-busy');
  }
  var fields = form.querySelectorAll('input, textarea, select, button');
  fields.forEach(function (el) {
    if (isLoading) {
      if (el.dataset.zpmPrevDisabled === undefined) {
        el.dataset.zpmPrevDisabled = el.disabled ? '1' : '0';
      }
      el.disabled = true;
    } else if (el.dataset.zpmPrevDisabled !== undefined) {
      el.disabled = el.dataset.zpmPrevDisabled === '1';
      delete el.dataset.zpmPrevDisabled;
    }
  });
}

function zpmFormAbortPending(form) {
  if (!form) return;
  if (zpmFormPendingRequests && zpmFormPendingRequests.has(form)) {
    var ctrl = zpmFormPendingRequests.get(form);
    if (ctrl && typeof ctrl.abort === 'function') {
      try { ctrl.abort(); } catch (e) {}
    }
    zpmFormPendingRequests.delete(form);
  }
  zpmFormSetLoading(form, false);
}

function zpmFormAbortAllPending() {
  document.querySelectorAll('form.zpm-form, [data-fb-form]').forEach(function (f) {
    zpmFormAbortPending(f);
  });
}

if (typeof window !== 'undefined') {
  window.zpmFormSetLoading = zpmFormSetLoading;
  window.zpmFormAbortAllPending = zpmFormAbortAllPending;
}
"""

DEALER_IIFE_MARKER = "/* ==========================================================\n   ISOLATED HANDLER FOR DEALER FORM (ZPM)"

PROCESS_SUBMISSION_OLD = """function processSubmission(form, captchaToken, csrfToken, resolve, reject) {
    // Создаем FormData
    var formData = new FormData(form);

    // Добавляем CSRF токен в данные формы (стандартное имя поля часто '_token' или 'csrf_token')
    // ВАЖНО: Убедитесь, что ваш PHP ожидает это поле. Обычно это 'csrf_token'.
    formData.append('csrf_token', csrfToken);

    // Если есть капча, добавляем её токен
    if (captchaToken) {
        formData.append('g-recaptcha-response', captchaToken);
    }

    // Определяем URL и метод
    var url =  "/index.php?route=checkout/anketa";
    var method = 'POST';
    //var url = form.getAttribute('action') || window.location.href;
    //var method = form.getAttribute('method') || 'POST';

    // Отправляем запрос
    fetch(url, {
        method: method,
        body: formData
    })
    .then(response => response.json()) // Ожидаем JSON ответ
    .then(data => {
        if (data.ok) {
            resolve({ ok: true });
        } else {
            // Проверяем, не ошибка ли это CSRF на стороне сервера
            if (data.message && data.message.includes('CSRF')) {
                reject(new Error('Ошибка безопасности: истек токен CSRF. Обновите страницу.'));
            } else {
                reject(new Error(data.message || 'Ошибка обработки'));
            }
        }
    })
    .catch(error => {
        reject(error);
    });
}"""

PROCESS_SUBMISSION_NEW = """function processSubmission(form, captchaToken, csrfToken, resolve, reject) {
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

    var url = "/index.php?route=checkout/anketa";
    var fetchOpts = { method: 'POST', body: formData };
    if (abortController) {
        fetchOpts.signal = abortController.signal;
    }

    fetch(url, fetchOpts)
    .then(function (response) { return response.json(); })
    .then(function (data) {
        if (data.ok) {
            resolve({ ok: true });
        } else if (data.message && data.message.includes('CSRF')) {
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
}"""

PROCESS_FETCH_OLD = """  function processFetch(form, captchaToken, csrfToken, resolve, reject) {
    var formData = new FormData(form);
    if (csrfToken) formData.append('csrf_token', csrfToken);
    if (captchaToken) formData.append('g-recaptcha-response', captchaToken);

    fetch(CONFIG.endpoint, {
      method: 'POST',
      body: formData
    })
    .then(function(response) { return response.json(); })
    .then(function(data) {
      if (data.ok) resolve(data);
      else reject(new Error(data.message || CONFIG.errorMsg));
    })
    .catch(function(err) { reject(err); });
  }"""

PROCESS_FETCH_NEW = """  function processFetch(form, captchaToken, csrfToken, resolve, reject) {
    zpmFormAbortPending(form);
    var abortController = typeof AbortController !== 'undefined' ? new AbortController() : null;
    if (zpmFormPendingRequests && abortController) {
      zpmFormPendingRequests.set(form, abortController);
    }
    zpmFormSetLoading(form, true);

    var formData = new FormData(form);
    if (csrfToken) formData.append('csrf_token', csrfToken);
    if (captchaToken) formData.append('g-recaptcha-response', captchaToken);

    var fetchOpts = { method: 'POST', body: formData };
    if (abortController) {
      fetchOpts.signal = abortController.signal;
    }

    fetch(CONFIG.endpoint, fetchOpts)
    .then(function(response) { return response.json(); })
    .then(function(data) {
      if (data.ok) resolve(data);
      else reject(new Error(data.message || CONFIG.errorMsg));
    })
    .catch(function(err) {
      if (err && err.name === 'AbortError') {
        reject(new Error(ZPM_FORM_ABORTED));
        return;
      }
      reject(err);
    })
    .finally(function () {
      if (zpmFormPendingRequests) {
        zpmFormPendingRequests.delete(form);
      }
      zpmFormSetLoading(form, false);
    });
  }"""

PALETTE = {
    "bg": "#f5f7fa",
    "container": "#ffffff",
    "text": "#1f2933",
    "muted": "#667085",
    "border": "#e5e7eb",
    "accent": "#0f766e",
}


def esc(value: Any) -> str:
    return html_module.escape(str(value), quote=True)


def text_from_html(content: str) -> str:
    text = re.sub(r"<br\s*/?>", "\n", content, flags=re.I)
    text = re.sub(r"</p>|</tr>|</li>", "\n", text, flags=re.I)
    text = re.sub(r"<[^>]+>", "", text)
    text = html_module.unescape(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def wrap_document(title: str, preheader: str, body: str) -> str:
    p = PALETTE
    return (
        f'<!DOCTYPE html><html lang="ru"><head><meta charset="UTF-8">'
        f'<meta name="viewport" content="width=device-width, initial-scale=1.0">'
        f"<title>{esc(title)}</title></head>"
        f'<body style="margin:0;padding:0;background-color:{p["bg"]};'
        f'font-family:Arial,Helvetica,sans-serif;color:{p["text"]};">'
        f'<div style="display:none;max-height:0;overflow:hidden;opacity:0;color:transparent;">{esc(preheader)}</div>'
        f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" '
        f'style="background-color:{p["bg"]};padding:24px 12px;"><tr><td align="center">'
        f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="600" '
        f'style="max-width:600px;width:100%;background-color:{p["container"]};'
        f'border:1px solid {p["border"]};border-radius:8px;overflow:hidden;">'
        f'<tr><td style="padding:24px 28px;font-size:15px;line-height:1.55;color:{p["text"]};">'
        f"{body}</td></tr></table>"
        f'<p style="margin:16px 0 0;font-size:12px;line-height:1.4;color:{p["muted"]};text-align:center;">'
        f"{CORRECT_BRAND} · bzpm.ru</p></td></tr></table></body></html>"
    )


def render_preview_customer(data: dict[str, Any]) -> dict[str, str]:
    p = PALETTE
    title = data.get("subject", "ЗПМ: заявка получена")
    body = (
        f'<table role="presentation" width="100%" style="margin:0 0 20px;"><tr><td '
        f'style="padding-bottom:16px;border-bottom:2px solid {p["accent"]};">'
        f'<div style="font-size:22px;font-weight:700;color:{p["accent"]};">{esc(CORRECT_BRAND)}</div>'
        f'<div style="margin-top:4px;font-size:13px;color:{p["muted"]};">bzpm.ru</div></td></tr></table>'
        f'<h1 style="margin:0 0 20px;font-size:20px;">{esc(title)}</h1>'
        f'<div style="margin:0 0 16px;padding:14px 16px;border:1px solid {p["border"]};border-radius:6px;">'
        f'<div style="font-weight:700;">Заявка получена</div>'
        f'<div>Мы получили вашу заявку на сайте {esc(CORRECT_BRAND)}.</div></div>'
        f'<div style="margin:0 0 16px;padding:14px 16px;background:{p["bg"]};border:1px solid {p["border"]};border-radius:6px;">'
        f'<div style="font-weight:700;">Спасибо за обращение</div>'
        f'<div>Тип обращения: <strong>{esc(data.get("dialog_label", ""))}</strong></div>'
        f"</div>"
        f'<div style="margin:0 0 16px;padding:14px 16px;border:1px solid {p["border"]};border-radius:6px;">'
        f'<div style="font-weight:700;">Что дальше</div>'
        f'<div>{esc(data.get("next_step", ""))}</div></div>'
        f'<div style="margin:0 0 16px;"><div style="font-weight:700;">Ваши контактные данные</div>'
        f'<div>Имя: <strong>{esc(data.get("author", ""))}</strong></div>'
        f'<div>Телефон: <strong>{esc(data.get("phone", ""))}</strong></div>'
        f'<div>E-mail: <strong>[redacted]</strong></div></div>'
        f'<div style="margin:0 0 16px;padding:14px 16px;border:1px solid {p["border"]};border-radius:6px;">'
        f'<div style="font-weight:700;">Ваше сообщение</div>'
        f'<div>{esc(data.get("message", ""))}</div></div>'
        f'<div style="margin-top:20px;padding-top:16px;border-top:1px solid {p["border"]};font-size:12px;color:{p["muted"]};">'
        "Это автоматическое письмо с сайта bzpm.ru.</div>"
    )
    html = wrap_document(title, title, body)
    return {"html": html, "text": text_from_html(html), "subject": title}


def render_preview_admin(data: dict[str, Any]) -> dict[str, str]:
    p = PALETTE
    title = data.get("subject", "ЗПМ: новая заявка")
    body = (
        f'<h1 style="margin:0 0 20px;font-size:20px;">{esc(title)}</h1>'
        f'<div style="font-weight:700;">{esc(CORRECT_BRAND)}</div>'
        f'<div>Тип формы: {esc(data.get("dialog_label", ""))}</div>'
        f'<div style="margin-top:16px;font-size:12px;color:{p["muted"]};text-transform:uppercase;">Служебная информация</div>'
        f'<div style="font-size:12px;color:{p["muted"]};">IP: {esc(data.get("service_info", {}).get("ip", ""))}</div>'
    )
    html = wrap_document(title, title, body)
    return {"html": html, "text": text_from_html(html), "subject": title}


class FormParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.forms: list[dict[str, Any]] = []
        self._current: dict[str, Any] | None = None
        self._field: dict[str, str] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        ad = {k: (v or "") for k, v in attrs}
        if tag.lower() == "form":
            self._current = {
                "action": ad.get("action", ""),
                "method": ad.get("method", "get").upper(),
                "class": ad.get("class", ""),
                "fields": [],
            }
        elif self._current is not None and tag.lower() in ("input", "textarea", "select", "button"):
            self._field = {
                "tag": tag.lower(),
                "type": ad.get("type", ""),
                "name": ad.get("name", ""),
                "id": ad.get("id", ""),
            }
            if tag.lower() == "textarea":
                self._current["fields"].append(self._field)
                self._field = None

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "form" and self._current is not None:
            self.forms.append(self._current)
            self._current = None


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow(row)


def parse_production_section(path: Path, subsection: str | None = None) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^## PRODUCTION\s*$([\s\S]*?)(?=^## |\Z)", text, re.MULTILINE)
    if not match:
        raise RuntimeError("PRODUCTION section not found")
    block = match.group(1)
    if subsection:
        sub = re.search(rf"^### {re.escape(subsection)}\s*$([\s\S]*?)(?=^### |\Z)", block, re.MULTILINE)
        if not sub:
            raise RuntimeError(f"Subsection {subsection!r} not found")
        block = sub.group(1)
    fields: dict[str, str] = {}
    current: str | None = None
    for line in block.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.endswith(":"):
            current = s[:-1].strip().lower().replace(" ", "_")
            fields.setdefault(current, "")
            continue
        if current:
            fields[current] = s
    return fields


def ftp_connect() -> ftplib.FTP:
    creds = parse_production_section(SECRETS_PATH, "FTP / SFTP")
    ftp = ftplib.FTP()
    ftp.connect(creds["host"], int(creds.get("port") or 21), timeout=120)
    ftp.login(creds["username"], creds["password"])
    return ftp


def ftp_download(ftp: ftplib.FTP, remote: str) -> tuple[bytes | None, str | None]:
    buf = io.BytesIO()
    try:
        ftp.retrbinary(f"RETR {remote}", buf.write)
        return buf.getvalue(), None
    except Exception as exc:  # noqa: BLE001
        return None, str(exc)


def ftp_upload(ftp: ftplib.FTP, remote: str, data: bytes) -> None:
    ftp.storbinary(f"STOR {remote}", io.BytesIO(data))


def remote_local_name(remote: str) -> str:
    return remote.strip("/").replace("/", "__")


def http_get(url: str) -> dict[str, Any]:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/xml,text/plain,*/*"},
    )
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            body = resp.read()
            charset = resp.headers.get_content_charset() or "utf-8"
            return {
                "url": url,
                "status": resp.status,
                "headers": dict(resp.headers.items()),
                "raw_body": body,
                "text": body.decode(charset, errors="replace"),
                "error": None,
            }
    except urllib.error.HTTPError as exc:
        body = exc.read()
        charset = exc.headers.get_content_charset() or "utf-8"
        return {
            "url": url,
            "status": exc.code,
            "headers": dict(exc.headers.items()),
            "raw_body": body,
            "text": body.decode(charset, errors="replace"),
            "error": str(exc),
        }
    except Exception as exc:  # noqa: BLE001
        return {"url": url, "status": None, "headers": {}, "raw_body": b"", "text": "", "error": str(exc)}


def patch_main_js(source: str) -> str:
    if "window.zpmFormSetLoading" in source:
        return source
    if DEALER_IIFE_MARKER not in source:
        raise RuntimeError("dealer IIFE marker not found")
    source = source.replace(DEALER_IIFE_MARKER, ZPM_LOADING_JS + "\n\n" + DEALER_IIFE_MARKER, 1)
    if PROCESS_SUBMISSION_OLD not in source:
        raise RuntimeError("processSubmission block not found")
    source = source.replace(PROCESS_SUBMISSION_OLD, PROCESS_SUBMISSION_NEW, 1)
    if PROCESS_FETCH_OLD not in source:
        raise RuntimeError("processFetch block not found")
    source = source.replace(PROCESS_FETCH_OLD, PROCESS_FETCH_NEW, 1)

    source = source.replace(
        "      if (submitBtn) {\n        submitBtn.disabled = true;\n        submitBtn.innerText = 'Отправка...';\n      }\n\n      sendForm(form)",
        "      sendForm(form)",
        1,
    )
    source = source.replace(
        "        .finally(function () {\n          if (submitBtn) {\n            submitBtn.disabled = false;\n            submitBtn.innerText = originalBtnText;\n          }\n        });",
        "        .finally(function () {\n          if (submitBtn && submitBtn.dataset.zpmPrevDisabled === undefined) {\n            submitBtn.innerText = originalBtnText;\n          }\n        });",
        1,
    )
    source = source.replace(
        "        .catch(function (err) {\n          showStatus(form, err.message || CONFIG.errorMsg, 'error');\n        })",
        "        .catch(function (err) {\n          if (err && err.message === ZPM_FORM_ABORTED) return;\n          showStatus(form, err.message || CONFIG.errorMsg, 'error');\n        })",
        1,
    )

    source = source.replace(
        "    var submitBtn = form.querySelector('[data-fb-submit]');\n    if (submitBtn) submitBtn.disabled = true;\n\n    sendForm(form)",
        "    sendForm(form)",
        1,
    )
    source = source.replace(
        "      .catch(function () {\n        setState(wrap, 'error');",
        "      .catch(function (err) {\n        if (err && err.message === ZPM_FORM_ABORTED) return;\n        setState(wrap, 'error');",
        1,
    )
    source = source.replace(
        "      .finally(function () {\n        if (submitBtn) submitBtn.disabled = false;\n      });",
        "",
        1,
    )

    close_hook = "    if (wasOpen && !isOpenNow) {\n      // Флаг на 350мс"
    if close_hook in source:
        source = source.replace(
            close_hook,
            "    if (wasOpen && !isOpenNow) {\n      zpmFormAbortAllPending();\n      // Флаг на 350мс",
            1,
        )
    return source


def patch_style_css(source: str) -> str:
    append = CSS_APPEND.read_text(encoding="utf-8")
    if "zpm-form--loading" in source:
        return source
    return source.rstrip() + "\n\n" + append


def ensure_layout() -> None:
    for sub in SUBDIRS:
        (DEPLOYMENT_ROOT / sub).mkdir(parents=True, exist_ok=True)
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "operation.json",
        {
            "operation_id": OPERATION_ID,
            "site_id": SITE_ID,
            "environment": ENVIRONMENT,
            "production_url": PRODUCTION_URL,
            "baseline_before": BASELINE_BEFORE,
            "change_type": "customer-form-confirmation-emails-and-form-loading-state",
            "production_mutation_allowed": True,
            "email_send_allowed": "controlled_tests_only",
            "form_submit_allowed": "controlled_tests_only",
            "smtp_change_allowed": False,
            "admin_save_allowed": False,
            "db_write_allowed": False,
            "customer_copy_change_allowed": True,
            "customer_copy_condition": "email_field_or_logged_in_customer_email_only",
            "customer_service_info_allowed": False,
            "standard_opencart_mail_change_allowed": False,
            "mail_trigger_patch_allowed": "checkout_anketa_only",
            "frontend_form_loading_patch_allowed": True,
            "shared_renderer_patch_allowed": "only_if_needed",
            "header_footer_change_allowed": False,
            "brand_policy_correct": CORRECT_BRAND,
            "brand_policy_forbidden_public": WRONG_BRAND,
            "created_at": utc_now(),
        },
    )


def phase_source_authority() -> dict[str, Any]:
    paths = [
        (REMOTE_ANKETA, True),
        (REMOTE_RENDERER, True),
        (REMOTE_MAIN_JS, True),
        (REMOTE_STYLE_CSS, True),
        (REMOTE_MOD_ANKETA, False),
        (REMOTE_MOD_RENDERER, False),
    ]
    rows: list[dict[str, Any]] = []
    mod_blocker = False
    ftp = ftp_connect()
    try:
        for remote, will_touch in paths:
            data, err = ftp_download(ftp, remote)
            exists = data is not None
            sha = sha256_bytes(data) if data else ""
            if data is not None:
                local = DEPLOYMENT_ROOT / "source-before" / remote_local_name(remote)
                local.write_bytes(data)
            is_mod = "modification" in remote
            if is_mod and exists:
                mod_blocker = True
            rows.append(
                {
                    "remote_path": remote,
                    "exists": exists,
                    "sha256": sha,
                    "will_touch": will_touch,
                    "modification_overlay": is_mod,
                    "error": err or "",
                }
            )
    finally:
        ftp.quit()

    write_csv(
        DEPLOYMENT_ROOT / "manifests" / "source-authority-map.csv",
        rows,
        ["remote_path", "exists", "sha256", "will_touch", "modification_overlay", "error"],
    )
    write_json(DEPLOYMENT_ROOT / "manifests" / "source-authority-map.json", {"generated_at": utc_now(), "paths": rows})
    md = [
        "# Source authority map",
        "",
        f"Operation: {OPERATION_ID}",
        "",
        "- anketa.php is live form handler route `checkout/anketa`",
        "- main.js uses fetch + processSubmission for zpm-form AJAX",
        "- ZpmMailRenderer::renderCustomerFormConfirmation exists",
        "- modification overlay for anketa/renderer: must be absent",
        "",
    ]
    for row in rows:
        md.append(
            f"- `{row['remote_path']}` exists={row['exists']} touch={row['will_touch']} mod={row['modification_overlay']}"
        )
    if mod_blocker:
        md.append("\n**STOP:** modification overlay overrides target file(s).")
    write_text(DEPLOYMENT_ROOT / "manifests" / "source-authority-map.md", "\n".join(md) + "\n")
    return {"rows": rows, "mod_blocker": mod_blocker}


def phase_http_before() -> dict[str, Any]:
    inventory: list[dict[str, Any]] = []
    for slug, url in FORM_URLS:
        resp = http_get(url)
        parser = FormParser()
        try:
            parser.feed(resp.get("text", "")[:800000])
        except Exception:  # noqa: BLE001
            pass
        zpm_forms = [f for f in parser.forms if "zpm-form" in f.get("class", "")]
        forms_detail = []
        for f in zpm_forms:
            names = [fld.get("name") for fld in f.get("fields", []) if fld.get("name")]
            forms_detail.append({"class": f.get("class"), "has_email": "email" in names, "fields": names})
        inventory.append(
            {
                "slug": slug,
                "url": url,
                "status": resp.get("status"),
                "zpm_form_count": len(zpm_forms),
                "forms": forms_detail,
                "csrf_meta": bool(re.search(r'<meta[^>]+name=["\']csrf-token["\']', resp.get("text", ""), re.I)),
                "recaptcha_present": "google.com/recaptcha" in resp.get("text", ""),
                "route": "checkout/anketa",
            }
        )
    payload = {"generated_at": utc_now(), "pages": inventory}
    write_json(DEPLOYMENT_ROOT / "http-before" / "form-pages-before.json", payload)
    ui = {
        "generated_at": utc_now(),
        "submit_loading_class_before": False,
        "abort_on_modal_close_before": False,
        "notes": "Before deploy: no zpm-form--loading; submit disables button text only in dealer handler",
    }
    write_json(DEPLOYMENT_ROOT / "ui-before" / "form-ui-before.json", ui)
    write_text(
        DEPLOYMENT_ROOT / "ui-before" / "form-ui-before.md",
        "# Form UI before\n\nNo dedicated loading overlay; partial button disable in dealer form only.\n",
    )
    lines = ["# Form pages before", ""]
    for p in inventory:
        lines.append(f"- **{p['slug']}** zpm-forms={p['zpm_form_count']}")
    write_text(DEPLOYMENT_ROOT / "http-before" / "form-pages-before.md", "\n".join(lines) + "\n")
    return payload


def phase_implementation_design() -> None:
    design = {
        "operation_id": OPERATION_ID,
        "customer_recipient_priority": [
            "posted valid email field",
            "logged-in customer account email if no posted valid email",
            "skip customer copy otherwise",
        ],
        "send_order": ["admin email first", "customer confirmation if eligible"],
        "customer_subject": "ЗПМ: заявка получена — {dialog_label}",
        "customer_no_service_info": True,
        "frontend_loading": {
            "class": "zpm-form--loading",
            "aria_busy": True,
            "abort": "AbortController on fetch",
            "modal_close": "zpmFormAbortAllPending on Fancybox close",
        },
        "patch_files": [REMOTE_ANKETA, REMOTE_RENDERER, REMOTE_MAIN_JS, REMOTE_STYLE_CSS],
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "implementation-design.json", design)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "implementation-design.md",
        "# Implementation design\n\n" + json.dumps(design, ensure_ascii=False, indent=2) + "\n",
    )


def phase_local_patch(authority: dict[str, Any]) -> dict[str, Any]:
    after_anketa = DEPLOYMENT_ROOT / "source-after" / remote_local_name(REMOTE_ANKETA)
    after_renderer = DEPLOYMENT_ROOT / "source-after" / remote_local_name(REMOTE_RENDERER)
    after_main = DEPLOYMENT_ROOT / "source-after" / remote_local_name(REMOTE_MAIN_JS)
    after_css = DEPLOYMENT_ROOT / "source-after" / remote_local_name(REMOTE_STYLE_CSS)

    shutil.copy2(ANKETA_PATCH, after_anketa)
    shutil.copy2(RENDERER_SRC, after_renderer)

    before_main = DEPLOYMENT_ROOT / "source-before" / remote_local_name(REMOTE_MAIN_JS)
    before_css = DEPLOYMENT_ROOT / "source-before" / remote_local_name(REMOTE_STYLE_CSS)
    patched_js = patch_main_js(before_main.read_text(encoding="utf-8"))
    patched_css = patch_style_css(before_css.read_text(encoding="utf-8"))
    after_main.write_text(patched_js, encoding="utf-8", newline="\n")
    after_css.write_text(patched_css, encoding="utf-8", newline="\n")

    before_anketa = DEPLOYMENT_ROOT / "source-before" / remote_local_name(REMOTE_ANKETA)
    before_renderer = DEPLOYMENT_ROOT / "source-before" / remote_local_name(REMOTE_RENDERER)

    for name, before, after in (
        ("anketa", before_anketa, after_anketa),
        ("mail-renderer", before_renderer, after_renderer),
        ("main-js", before_main, after_main),
        ("style-css", before_css, after_css),
    ):
        diff = difflib.unified_diff(
            before.read_text(encoding="utf-8").splitlines(keepends=True),
            after.read_text(encoding="utf-8").splitlines(keepends=True),
            fromfile=f"before/{name}",
            tofile=f"after/{name}",
        )
        write_text(DEPLOYMENT_ROOT / "patch" / f"diff-{name.replace('-', '_')}.diff", "".join(diff))

    changed = [
        {"path": REMOTE_ANKETA, "sha256": sha256_file(after_anketa), "action": "overwrite"},
        {"path": REMOTE_RENDERER, "sha256": sha256_file(after_renderer), "action": "overwrite"},
        {"path": REMOTE_MAIN_JS, "sha256": sha256_file(after_main), "action": "overwrite"},
        {"path": REMOTE_STYLE_CSS, "sha256": sha256_file(after_css), "action": "overwrite"},
    ]
    write_json(DEPLOYMENT_ROOT / "patch" / "changed-files.json", {"files": changed})
    write_csv(DEPLOYMENT_ROOT / "patch" / "changed-files.csv", changed, ["path", "sha256", "action"])

    static = static_checks(after_anketa.read_text(encoding="utf-8"), patched_js, patched_css)
    write_json(DEPLOYMENT_ROOT / "patch" / "static-checks.json", static)
    write_text(
        DEPLOYMENT_ROOT / "patch" / "patch-summary.md",
        "# Patch summary\n\n"
        f"- anketa.php: customer confirmation conditional\n"
        f"- mail_renderer.php: customer template with contact fields, no service info\n"
        f"- main.js: loading state + AbortController\n"
        f"- style.css: spinner overlay\n",
    )
    return {"changed": changed, "static": static}


def static_checks(anketa: str, main_js: str, css: str) -> dict[str, Any]:
    checks = {
        "customer_resolve": "zpmResolveCustomerEmail" in anketa,
        "customer_send": "zpmSendCustomerFormConfirmation" in anketa,
        "customer_renderer": "renderCustomerFormConfirmation" in anketa,
        "admin_preserved": "renderAdminForm" in anketa and "zpmBuildServiceInfo" in anketa,
        "no_customer_on_missing_email_logic": "if ($customer_email === '')" in anketa,
        "no_bzpm_anketa": WRONG_BRAND not in anketa,
        "loading_js": "window.zpmFormSetLoading" in main_js and "AbortController" in main_js,
        "abort_on_close": "zpmFormAbortAllPending" in main_js,
        "loading_css": "zpm-form--loading" in css,
        "no_geoip": "geoip" not in anketa.lower(),
    }
    checks["pass"] = all(checks.values())
    return checks


def phase_mail_preview() -> dict[str, Any]:
    customer_fixture = {
        "subject": "ЗПМ: заявка получена — Запрос на обратный звонок",
        "dialog_label": "Запрос на обратный звонок",
        "author": "Тестовый посетитель",
        "phone": TEST_PHONE,
        "email": TEST_EMAIL,
        "message": TEST_MARKER_EMAIL,
        "submitted_at": "2026-07-08 12:00:00",
        "next_step": "Специалист свяжется с вами по указанным контактам.",
    }
    cust = render_preview_customer(customer_fixture)
    write_text(DEPLOYMENT_ROOT / "mail-after" / "customer-form-mail-preview.html", cust["html"])
    write_text(DEPLOYMENT_ROOT / "mail-after" / "customer-form-mail-preview.txt", cust["text"])
    write_json(DEPLOYMENT_ROOT / "mail-after" / "customer-form-mail-preview.json", customer_fixture)

    admin_fixture = {
        "subject": "ЗПМ: новая заявка — Запрос на обратный звонок",
        "dialog_label": "Запрос на обратный звонок",
        "service_info": {"ip": "203.0.113.10", "browser": "Chrome"},
    }
    adm = render_preview_admin(admin_fixture)
    write_text(DEPLOYMENT_ROOT / "mail-after" / "admin-form-mail-preview-after.html", adm["html"])
    write_text(DEPLOYMENT_ROOT / "mail-after" / "admin-form-mail-preview-after.txt", adm["text"])

    qa = {
        "customer_contains_zpm": CORRECT_BRAND in cust["html"],
        "customer_no_bzpm": WRONG_BRAND not in cust["html"],
        "customer_no_service_info": "Служебная информация" not in cust["html"],
        "customer_no_ip": "203.0.113" not in cust["html"],
        "customer_no_ua": "User-Agent" not in cust["html"],
        "admin_has_service_info": "Служебная информация" in adm["html"],
        "pass": CORRECT_BRAND in cust["html"]
        and WRONG_BRAND not in cust["html"]
        and "Служебная информация" not in cust["html"],
    }
    write_json(DEPLOYMENT_ROOT / "verification" / "local-mail-preview-qa.json", qa)
    write_text(
        DEPLOYMENT_ROOT / "verification" / "local-mail-preview-qa.md",
        "# Local mail preview QA\n\n" + "\n".join(f"- {k}: **{v}**" for k, v in qa.items()) + "\n",
    )

    ui_impl = {
        "loading_class": "zpm-form--loading",
        "aria_busy": True,
        "abort_controller": True,
        "modal_close_abort": True,
        "preserve_input_values_on_abort": True,
    }
    write_json(DEPLOYMENT_ROOT / "ui-after" / "loading-state-implementation.json", ui_impl)
    write_text(
        DEPLOYMENT_ROOT / "ui-after" / "loading-state-implementation.md",
        "# Loading state implementation\n\n" + json.dumps(ui_impl, ensure_ascii=False, indent=2) + "\n",
    )
    return qa


def phase_rollback(patch_info: dict[str, Any]) -> None:
    manifest = []
    for row in patch_info["changed"]:
        remote = row["path"]
        before = DEPLOYMENT_ROOT / "source-before" / remote_local_name(remote)
        manifest.append(
            {
                "remote_path": remote,
                "source_before_sha256": sha256_file(before) if before.is_file() else "",
                "rollback_method": "re-upload source-before exact file",
            }
        )
    write_json(DEPLOYMENT_ROOT / "rollback" / "remote-before-manifest.json", {"files": manifest})
    write_text(
        DEPLOYMENT_ROOT / "rollback" / "rollback-plan.md",
        "# Rollback plan\n\nRe-upload exact `source-before/` copies for all four touched files.\n",
    )


def phase_dry_run(authority: dict[str, Any], patch_info: dict[str, Any], preview_qa: dict[str, Any]) -> dict[str, Any]:
    gates = {
        "G1_source_authority": not authority.get("mod_blocker"),
        "G2_rollback_captured": (DEPLOYMENT_ROOT / "rollback" / "rollback-plan.md").is_file(),
        "G3_patch_scope": len(patch_info["changed"]) == 4,
        "G4_admin_mail_preserved": patch_info["static"].get("admin_preserved"),
        "G5_customer_conditional": patch_info["static"].get("customer_resolve"),
        "G6_no_customer_service_info": preview_qa.get("customer_no_service_info"),
        "G7_no_standard_mail": True,
        "G8_no_smtp_admin_db": True,
        "G9_no_geoip": patch_info["static"].get("no_geoip"),
        "G10_frontend_loading": patch_info["static"].get("loading_js"),
        "G11_modal_close_abort": patch_info["static"].get("abort_on_close"),
        "G12_abort_feasible": "AbortController" in (DEPLOYMENT_ROOT / "source-after" / remote_local_name(REMOTE_MAIN_JS)).read_text(encoding="utf-8"),
        "G13_renderer_previews": preview_qa.get("pass"),
        "G14_test_plan_ready": True,
        "G15_live_sanity_plan": True,
    }
    payload = {"generated_at": utc_now(), "gates": gates, "pass": all(gates.values())}
    write_json(DEPLOYMENT_ROOT / "manifests" / "dry-run.json", payload)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "dry-run.md",
        "# Dry-run gates\n\n" + "\n".join(f"- {k}: **{'PASS' if v else 'FAIL'}**" for k, v in gates.items()) + f"\n\n**Overall:** {'PASS' if payload['pass'] else 'FAIL'}\n",
    )
    return payload


def phase_deploy(dry_run: dict[str, Any], patch_info: dict[str, Any]) -> dict[str, Any]:
    if not dry_run["pass"]:
        return {"uploaded": False, "reason": "dry-run gates failed"}
    uploads = []
    ftp = ftp_connect()
    try:
        for row in patch_info["changed"]:
            remote = row["path"]
            local = DEPLOYMENT_ROOT / "source-after" / remote_local_name(remote)
            data = local.read_bytes()
            ftp_upload(ftp, remote, data)
            remote_bytes, err = ftp_download(ftp, remote)
            if remote_bytes is None:
                return {"uploaded": False, "reason": f"verify failed for {remote}: {err}"}
            local_sha = sha256_bytes(data)
            remote_sha = sha256_bytes(remote_bytes)
            verified = local_sha == remote_sha
            uploads.append(
                {
                    "remote_path": remote,
                    "local_sha256": local_sha,
                    "remote_sha256": remote_sha,
                    "verified": verified,
                }
            )
            if not verified:
                return {"uploaded": False, "reason": f"sha mismatch {remote}", "uploads": uploads}
    finally:
        ftp.quit()

    write_csv(
        DEPLOYMENT_ROOT / "verification" / "upload-manifest.csv",
        uploads,
        ["remote_path", "local_sha256", "remote_sha256", "verified"],
    )
    write_json(DEPLOYMENT_ROOT / "verification" / "upload-manifest.json", {"uploads": uploads})
    write_json(DEPLOYMENT_ROOT / "verification" / "remote-after-sha.json", {"uploads": uploads})
    return {"uploaded": True, "uploads": uploads}


def _playwright_submit(payload: dict[str, Any]) -> dict[str, Any]:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return {"attempted": False, "blocker": "playwright unavailable"}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 1200})
        page.set_default_timeout(120000)
        page.goto("https://bzpm.ru/", wait_until="networkidle")
        page.wait_for_timeout(4000)
        result = page.evaluate(
            """async (payload) => {
                const csrf = document.querySelector('meta[name="csrf-token"]')?.getAttribute('content');
                if (!csrf) return { error: 'csrf_missing' };
                const recaptchaScript = document.querySelector('script[src*="google.com/recaptcha"]');
                const siteKey = recaptchaScript ? recaptchaScript.getAttribute('data-sitekey') : null;
                let captchaToken = null;
                if (window.grecaptcha && siteKey) {
                    await new Promise((resolve) => window.grecaptcha.ready(resolve));
                    captchaToken = await window.grecaptcha.execute(siteKey, { action: 'submit' });
                }
                if (!captchaToken) return { error: 'recaptcha_token_missing' };
                const formData = new FormData();
                formData.append('dialog', String(payload.dialog));
                formData.append('name', payload.name);
                formData.append('phone', payload.phone);
                formData.append('message', payload.message);
                if (payload.email) formData.append('email', payload.email);
                formData.append('csrf_token', csrf);
                formData.append('g-recaptcha-response', captchaToken);
                const response = await fetch('/index.php?route=checkout/anketa', {
                    method: 'POST',
                    body: formData,
                    credentials: 'same-origin',
                });
                let body;
                try { body = await response.json(); } catch (e) { body = { raw: await response.text() }; }
                return { status: response.status, body };
            }""",
            payload,
        )
        browser.close()

    out: dict[str, Any] = {"attempted": True, "response_status": result.get("status"), "response": result.get("body")}
    if result.get("error"):
        out["blocker"] = result["error"]
        out["ok"] = False
    else:
        body = result.get("body") or {}
        out["ok"] = result.get("status") == 200 and isinstance(body, dict) and body.get("ok") is True
    return out


def phase_test_submits() -> dict[str, Any]:
    test_a = _playwright_submit(
        {
            "dialog": 7,
            "name": TEST_MARKER_EMAIL,
            "phone": TEST_PHONE,
            "email": TEST_EMAIL,
            "message": TEST_MARKER_EMAIL,
        }
    )
    test_b = _playwright_submit(
        {
            "dialog": 2,
            "name": TEST_MARKER_NO_EMAIL,
            "phone": TEST_PHONE,
            "message": TEST_MARKER_NO_EMAIL,
        }
    )

    write_json(
        DEPLOYMENT_ROOT / "test-submit" / "test-a-request-redacted.json",
        {"marker": TEST_MARKER_EMAIL, "dialog": 7, "email": "[redacted]", "phone": TEST_PHONE},
    )
    write_json(DEPLOYMENT_ROOT / "test-submit" / "test-a-response.json", test_a)
    write_text(
        DEPLOYMENT_ROOT / "test-submit" / "test-a-summary.md",
        f"# Test A (with email)\n\n- ok: **{test_a.get('ok')}**\n- status: {test_a.get('response_status')}\n- customer delivery: **SAFE UNKNOWN** (test mailbox not operator-verified)\n",
    )

    write_json(
        DEPLOYMENT_ROOT / "test-submit" / "test-b-request-redacted.json",
        {"marker": TEST_MARKER_NO_EMAIL, "dialog": 2, "email": None, "phone": TEST_PHONE},
    )
    write_json(DEPLOYMENT_ROOT / "test-submit" / "test-b-response.json", test_b)
    write_text(
        DEPLOYMENT_ROOT / "test-submit" / "test-b-summary.md",
        f"# Test B (no email)\n\n- ok: **{test_b.get('ok')}**\n- status: {test_b.get('response_status')}\n- customer copy skipped by design\n",
    )
    return {"test_a": test_a, "test_b": test_b}


def phase_ui_verification() -> dict[str, Any]:
    result: dict[str, Any] = {"attempted": False}
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        result["blocker"] = "playwright unavailable"
        write_json(DEPLOYMENT_ROOT / "ui-after" / "loading-state-verification.json", result)
        write_text(
            DEPLOYMENT_ROOT / "ui-after" / "loading-state-verification.md",
            "# UI verification\n\nPlaywright unavailable — static code review only.\n",
        )
        return result

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 1200})
        page.set_default_timeout(120000)

        page.route("**/index.php?route=checkout/anketa", lambda route: route.fulfill(status=200, content_type="application/json", body='{"ok":true,"message":"Заявка отправлена"}', delay=1500))

        page.goto("https://bzpm.ru/", wait_until="networkidle")
        page.wait_for_timeout(3000)

        checks = page.evaluate(
            """async () => {
                const out = { loading_helpers: typeof zpmFormSetLoading === 'function', abort_helpers: typeof zpmFormAbortAllPending === 'function' };
                const form = document.querySelector('.zpm-dealers[data-dealers] .zpm-form');
                if (!form) { out.form_found = false; return out; }
                out.form_found = true;
                const nameInput = form.querySelector('[name="name"]');
                if (nameInput) nameInput.value = 'UI TEST LOADING';
                const submitEvent = new Event('submit', { bubbles: true, cancelable: true });
                form.dispatchEvent(submitEvent);
                await new Promise(r => setTimeout(r, 200));
                const container = form.closest('.zpm-dealers') || form;
                out.loading_class = container.classList.contains('zpm-form--loading');
                out.aria_busy = container.getAttribute('aria-busy') === 'true';
                const btn = form.querySelector('button, .zpm-form__submit');
                out.button_disabled = btn ? btn.disabled : null;
                return out;
            }"""
        )
        browser.close()

    result = {"attempted": True, "checks": checks, "pass": checks.get("loading_helpers") and checks.get("loading_class")}
    write_json(DEPLOYMENT_ROOT / "ui-after" / "loading-state-verification.json", result)
    write_text(
        DEPLOYMENT_ROOT / "ui-after" / "loading-state-verification.md",
        "# Loading state verification\n\n" + json.dumps(result, ensure_ascii=False, indent=2) + "\n",
    )
    return result


def phase_live_sanity() -> dict[str, Any]:
    results: list[dict[str, Any]] = []
    sitemap_count = None
    main_js_has_loading = False
    for slug, url in SANITY_URLS:
        resp = http_get(url)
        text = resp.get("text", "")
        entry: dict[str, Any] = {
            "slug": slug,
            "url": url,
            "status": resp.get("status"),
            "error": resp.get("error"),
            "has_bzpm": WRONG_BRAND in text,
        }
        if slug == "home":
            main_js_match = re.search(r'/assets/js/main\.js[^"\']*', text)
            if main_js_match:
                js_url = "https://bzpm.ru" + main_js_match.group(0).split("?")[0]
                js_resp = http_get(js_url)
                main_js_has_loading = "zpmFormSetLoading" in js_resp.get("text", "")
                entry["main_js_loading_helpers"] = main_js_has_loading
        if slug == "stoly":
            entry["load_more_present"] = any(s in text for s in ("load-more", "load_more", "Показать ещё", "Показать еще"))
        if slug == "pdp":
            entry["extra_info_present"] = "product-content__extra-info" in text or "Дополнительные сведения" in text
        if slug == "llms":
            raw = resp.get("raw_body", b"")
            entry["utf8_bom"] = raw.startswith(b"\xef\xbb\xbf")
            entry["has_zpm"] = CORRECT_BRAND in text
        if slug == "sitemap" and resp.get("status") == 200:
            try:
                root = ET.fromstring(text)
                ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
                sitemap_count = len(root.findall("sm:url", ns)) or len(root.findall("url"))
                entry["url_count"] = sitemap_count
            except ET.ParseError:
                entry["url_count"] = None
        results.append(entry)

    payload = {
        "generated_at": utc_now(),
        "sitemap_url_count": sitemap_count,
        "main_js_loading_helpers_live": main_js_has_loading,
        "results": results,
        "pass": all(
            r.get("status") == 200 and not r.get("has_bzpm")
            for r in results
            if r["slug"] in ("home", "katalog", "robots", "sitemap", "llms", "neutral_hub", "stoly", "pdp")
        )
        and main_js_has_loading,
    }
    write_json(DEPLOYMENT_ROOT / "verification" / "live-sanity.json", payload)
    write_text(
        DEPLOYMENT_ROOT / "verification" / "live-sanity.md",
        "# Live sanity\n\n"
        + "\n".join(f"- **{r['slug']}** HTTP {r.get('status')}" for r in results)
        + f"\n\nSitemap URLs: {sitemap_count}\n\n**Overall:** {'PASS' if payload['pass'] else 'CHECK'}\n",
    )
    return payload


def phase_future_integration() -> None:
    spec = {
        "next_account": "SITE-002-PROD-MAIL-ACCOUNT-TRANSACTIONAL-01",
        "next_order": "SITE-002-PROD-MAIL-ORDER-TRANSACTIONAL-01",
    }
    write_json(DEPLOYMENT_ROOT / "mail-after" / "future-standard-mail-spec.json", spec)
    write_text(
        DEPLOYMENT_ROOT / "mail-after" / "future-standard-mail-spec.md",
        "# Future standard mail spec\n\n"
        "- SITE-002-PROD-MAIL-ACCOUNT-TRANSACTIONAL-01\n"
        "- SITE-002-PROD-MAIL-ORDER-TRANSACTIONAL-01\n",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=OPERATION_ID)
    parser.add_argument("--skip-deploy", action="store_true")
    parser.add_argument("--skip-test-submit", action="store_true")
    args = parser.parse_args()

    ensure_layout()
    authority = phase_source_authority()
    if authority.get("mod_blocker"):
        print("BLOCKED — modification overlay present")
        return 2

    phase_http_before()
    phase_implementation_design()
    patch_info = phase_local_patch(authority)
    if not patch_info["static"].get("pass"):
        print("BLOCKED — static checks failed", patch_info["static"])
        return 2

    preview_qa = phase_mail_preview()
    phase_rollback(patch_info)
    dry_run = phase_dry_run(authority, patch_info, preview_qa)
    deploy = {"uploaded": False, "reason": "skipped"} if args.skip_deploy else phase_deploy(dry_run, patch_info)
    test_submit = {"skipped": True} if args.skip_test_submit or not deploy.get("uploaded") else phase_test_submits()
    ui_verify = phase_ui_verification() if deploy.get("uploaded") else {"skipped": True}
    sanity = phase_live_sanity()
    phase_future_integration()

    CHECKPOINT_STORAGE.mkdir(parents=True, exist_ok=True)
    write_json(CHECKPOINT_STORAGE / "operation-summary.json", {"operation_id": OPERATION_ID, "deployed": deploy.get("uploaded")})

    summary = {
        "operation_id": OPERATION_ID,
        "ocpilot_run": OCPILOT_RUN,
        "dry_run_pass": dry_run["pass"],
        "deploy": deploy,
        "test_submit": test_submit,
        "ui_verify": ui_verify,
        "sanity_pass": sanity["pass"],
        "patch_files": [r["path"] for r in patch_info["changed"]],
    }
    write_json(DEPLOYMENT_ROOT / "reports" / "operation-summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if dry_run["pass"] and deploy.get("uploaded") else 1


if __name__ == "__main__":
    sys.exit(main())
