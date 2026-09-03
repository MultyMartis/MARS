#!/usr/bin/env python3
"""Transform contact-form markup to add personal_data_consent checkbox.

Idempotent for forms that already contain name=\"personal_data_consent\".
"""
from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path

PRIVACY_HREF = "/privacy-policy.html"
FIELD = "personal_data_consent"
ACCEPTED = "1"

AGREE_TEXT_RE = re.compile(
    r"Я(?:&nbsp;|\s)+соглашаюсь(?:&nbsp;|\s)+с(?:&nbsp;|\s)*"
    r'<a[^>]+href=["\']/?privacy-policy\.html["\'][^>]*>'
    r"политикой(?:&nbsp;|\s)*конфиденциальности</a>"
    r"(?:&nbsp;|\s)*и(?:&nbsp;|\s)+даю(?:&nbsp;|\s)+согласие(?:&nbsp;|\s)+на(?:&nbsp;|\s)*"
    r"обработку(?:&nbsp;|\s)+персональных(?:&nbsp;|\s)+данных",
    re.IGNORECASE | re.DOTALL,
)

FORM_AGREE_DIV_RE = re.compile(
    r'<div\s+class="form_agree__wrap">\s*' + AGREE_TEXT_RE.pattern + r"\s*</div>",
    re.IGNORECASE | re.DOTALL,
)

CALLBACK_AGREE_DIV_RE = re.compile(
    r'<div\s+class="callback_form__agree">\s*' + AGREE_TEXT_RE.pattern + r"\s*</div>",
    re.IGNORECASE | re.DOTALL,
)

BUTTON_THEN_CALLBACK_RE = re.compile(
    r"(<button\b[^>]*type=[\"']submit[\"'][^>]*>.*?</button>)\s*"
    + CALLBACK_AGREE_DIV_RE.pattern,
    re.IGNORECASE | re.DOTALL,
)

FORM_RE = re.compile(r"(<form\b[^>]*>)(.*?)(</form>)", re.IGNORECASE | re.DOTALL)


def consent_block(uid: str, wrap_class: str = "form_agree__wrap") -> str:
    return (
        f'<div class="{wrap_class} personal-data-consent-wrap">\n'
        f'\t\t\t\t<div class="checkbox-border">\n'
        f'\t              <input type="checkbox" class="required-checkbox personal-data-consent" '
        f'id="{uid}" name="{FIELD}" value="{ACCEPTED}" required>\n'
        f"\t\t\t\t</div>\n"
        f'              <label for="{uid}">Я&nbsp;соглашаюсь с&nbsp;'
        f'<a href="{PRIVACY_HREF}" target="_blank">политикой конфиденциальности</a> '
        f"и даю согласие на&nbsp;обработку персональных данных</label>\n"
        f"            </div>"
    )


def form_uid(form_open: str, body: str, counter: int) -> str:
    m = re.search(r'\bid=["\']([^"\']+)["\']', form_open, re.I)
    if m:
        safe = re.sub(r"[^a-zA-Z0-9_-]+", "_", m.group(1)).strip("_")
        if safe:
            return f"{FIELD}_{safe}"
    m = re.search(r'\bid=["\']([^"\']+)["\']', body, re.I)
    if m:
        safe = re.sub(r"[^a-zA-Z0-9_-]+", "_", m.group(1)).strip("_")
        if safe:
            return f"{FIELD}_{safe}_{counter}"
    digest = hashlib.sha1((form_open + body[:200]).encode("utf-8", "ignore")).hexdigest()[:8]
    return f"{FIELD}_{digest}_{counter}"


def looks_like_contact_form(form_open: str, body: str) -> bool:
    blob = (form_open + body).lower()
    markers = (
        "__form",
        "cf_name",
        "cf_phone",
        "calc_name",
        "calc_phone",
        "callback__",
        "audit__",
        "page__",
        "bonus__",
        "career__",
        "partners__",
        "review__",
        "tariff_",
        "calculator__",
    )
    if any(m in blob for m in markers):
        return True
    has_contact = ('type="tel"' in blob) or ('name="email"' in blob) or ("cf_phone" in blob)
    has_submit = ('type="submit"' in blob) or ('class="submit"' in blob) or ("class='submit'" in blob)
    return has_contact and has_submit


def transform_form(form_open: str, body: str, counter: int) -> tuple[str, bool]:
    if not looks_like_contact_form(form_open, body):
        return body, False

    changed = False
    uid = form_uid(form_open, body, counter)

    if re.search(rf'name=["\']{FIELD}["\']', body, re.I):
        body2 = re.sub(
            rf'(<input\b[^>]*name=["\']{FIELD}["\'][^>]*)\s+checked(?:\s*=\s*(["\'])checked\2)?',
            r"\1",
            body,
            flags=re.I,
        )
        if body2 != body:
            return body2, True
        return body, False

    def repl_form_agree(_m: re.Match) -> str:
        nonlocal changed
        changed = True
        return consent_block(uid, "form_agree__wrap")

    new_body, n = FORM_AGREE_DIV_RE.subn(repl_form_agree, body, count=1)
    if n:
        return new_body, True

    def repl_btn_cb(m: re.Match) -> str:
        nonlocal changed
        changed = True
        return consent_block(uid, "callback_form__agree") + "\n\t\t\t" + m.group(1)

    new_body, n = BUTTON_THEN_CALLBACK_RE.subn(repl_btn_cb, body, count=1)
    if n:
        body = new_body
        body2, n2 = CALLBACK_AGREE_DIV_RE.subn("", body)
        if n2:
            body = body2
        return body, True

    def repl_cb(_m: re.Match) -> str:
        nonlocal changed
        changed = True
        return consent_block(uid, "callback_form__agree")

    new_body, n = CALLBACK_AGREE_DIV_RE.subn(repl_cb, body, count=1)
    if n:
        return new_body, True

    inj = consent_block(uid, "form_agree__wrap")
    m = re.search(r"(<button\b[^>]*type=[\"']submit[\"'][^>]*>)", body, re.I)
    if m:
        return body[: m.start()] + inj + "\n\t\t\t" + body[m.start() :], True

    m = re.search(r'(<a\b[^>]*class=["\'][^"\']*\bsubmit\b[^"\']*["\'][^>]*>)', body, re.I)
    if m:
        m2 = re.search(r'<div\s+class="calculator_stage__btns">', body, re.I)
        if m2:
            return body[: m2.start()] + inj + "\n\n\t\t\t\t\t\t\t" + body[m2.start() :], True
        return body[: m.start()] + inj + "\n\t\t\t\t\t\t\t\t" + body[m.start() :], True

    return body, False


def transform_text(text: str) -> tuple[str, int]:
    counter = 0
    changes = 0
    used_ids: set[str] = set()

    def repl(m: re.Match) -> str:
        nonlocal counter, changes
        counter += 1
        form_open, body, form_close = m.group(1), m.group(2), m.group(3)
        new_body, changed = transform_form(form_open, body, counter)
        if changed:
            for uid_m in re.finditer(rf'id=["\']({FIELD}_[^"\']+)["\']', new_body):
                uid = uid_m.group(1)
                if uid in used_ids:
                    alt = f"{uid}_{counter}"
                    new_body = new_body.replace(f'id="{uid}"', f'id="{alt}"', 1)
                    new_body = new_body.replace(f'for="{uid}"', f'for="{alt}"', 1)
                    uid = alt
                used_ids.add(uid)
            changes += 1
        return form_open + new_body + form_close

    return FORM_RE.sub(repl, text), changes


def process_file(path: Path, dry_run: bool = False) -> dict:
    raw = path.read_bytes()
    try:
        text = raw.decode("utf-8")
        enc = "utf-8"
    except UnicodeDecodeError:
        text = raw.decode("cp1251")
        enc = "cp1251"

    new_text, form_changes = transform_text(text)
    changed = new_text != text
    info = {
        "path": str(path),
        "changed": changed,
        "form_changes": form_changes,
        "encoding": enc,
        "consent_count_before": len(re.findall(rf'name=["\']{FIELD}["\']', text, re.I)),
        "consent_count_after": len(re.findall(rf'name=["\']{FIELD}["\']', new_text, re.I)),
    }
    if changed and not dry_run:
        path.write_bytes(new_text.encode(enc))
    return info


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+", type=Path)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    total_changed = 0
    for p in args.paths:
        if not p.is_file():
            print(f"SKIP_MISSING {p}")
            continue
        info = process_file(p, dry_run=args.dry_run)
        if info["changed"]:
            total_changed += 1
        print(
            f"{'CHANGED' if info['changed'] else 'OK'} forms={info['form_changes']} "
            f"consent {info['consent_count_before']}->{info['consent_count_after']} {p}"
        )
    print(f"TOTAL_CHANGED_FILES={total_changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
