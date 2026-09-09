#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Live contract probe: endpoints, consent, preventDefault, calculator DOM. No mail."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright

OUT = Path(r"X:\AI MARS\projects\iseo-su-site-ops\evidence\form-system-acceptance-01\_live-probe.json")
UA = "ISEO-SU-FORM-SYSTEM-ACCEPTANCE-01/1.0"
SHOT = Path(r"X:\AI MARS\projects\iseo-su-site-ops\evidence\form-system-acceptance-01\screenshots")

PAGES = [
    ("homepage", "https://i-seo.su/"),
    ("seo_hub", "https://i-seo.su/services/seo.html"),
    ("tariff_calc", "https://i-seo.su/tariff-calc"),
    ("nested_seo", "https://i-seo.su/services/seo/prodvizhenie-sajta-restorana.html"),
    ("city", "https://i-seo.su/services/seo/prodvizhenie-v-sankt-peterburge.html"),
    ("usa", "https://i-seo.su/services/seo/prodvizhenie-v-ssha.html"),
    ("webinar", "https://i-seo.su/webinar-seo-podryadchik.html"),
    ("blog_html", "https://i-seo.su/blog.html"),
    ("blog_wp", "https://i-seo.su/blog/"),
    ("cases", "https://i-seo.su/cases.html"),
    ("contacts", "https://i-seo.su/contacts.html"),
    ("career", "https://i-seo.su/career.html"),
    ("partners", "https://i-seo.su/partners.html"),
    ("reviews", "https://i-seo.su/reviews.html"),
    ("bonuses", "https://i-seo.su/bonuses.html"),
    ("adv_nested", "https://i-seo.su/services/adv/google-adwords.html"),
]


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


INSPECT_JS = r"""() => {
  const forms = [...document.querySelectorAll('form')].map(f => {
    const send = f.querySelector('button, input[type="submit"], input[type="button"]');
    const names = [...f.querySelectorAll('input,select,textarea')].map(el => el.getAttribute('name'));
    return {
      id: f.id || null,
      action: f.getAttribute('action'),
      method: f.getAttribute('method'),
      className: f.className,
      send_id: send ? send.id : null,
      send_type: send ? send.getAttribute('type') : null,
      data_root: send ? send.getAttribute('data-root') : null,
      consent: names.includes('personal_data_consent'),
      honeypot: names.includes('contact_company_url'),
      names: names.filter(Boolean),
      site_required: [...f.querySelectorAll('input[name$="_site"]')].map(el => ({
        name: el.name, required: el.hasAttribute('required')
      })),
      phone_contact: [...f.querySelectorAll('input,select')].filter(el => {
        const n = el.getAttribute('name') || '';
        return /contact|phone/i.test(n);
      }).map(el => ({name: el.getAttribute('name'), id: el.id, type: el.getAttribute('type'), tag: el.tagName}))
    };
  });
  const triggers = [...document.querySelectorAll('a[href*="FORM_popup"], a[href*="__FORM"]')].slice(0, 40).map(a => ({
    href: a.getAttribute('href'), text: (a.textContent||'').trim().slice(0,80)
  }));
  const calc = {
    tariff_wrap: !!document.querySelector('.tariff-calc-wrap'),
    tariff_submit: !!document.querySelector('.tariff-calc-submit'),
    tariff_request: !!document.querySelector('.tariff-calc-request, #callback__FORM_tariff_calc'),
    stage: !!document.querySelector('.calculator_stage')
  };
  function handlerInfo(id) {
    try {
      const $ = window.jQuery;
      const el = document.getElementById(id);
      if (!el || !$) return {id, missing: true};
      const ev = ($._data(el, 'events') || {});
      const clicks = ev.click || [];
      const src = clicks.map(h => String(h.handler)).join('\n');
      const urls = [...src.matchAll(/url:\s*(?:root\s*\?\s*'([^']+)'\s*:\s*)?'([^']+)'/g)].map(m => m[1] || m[2]);
      const urls2 = [...src.matchAll(/url:\s*'([^']+)'/g)].map(m => m[1]);
      return {
        id,
        click_count: clicks.length,
        preventDefault_call: /preventDefault\s*\(/.test(src),
        return_false: /return false/.test(src),
        urls: urls.length ? urls : urls2
      };
    } catch (e) {
      return {id, error: String(e)};
    }
  }
  const sendIds = [...document.querySelectorAll('[id*="FORM_send"]')].map(el => el.id);
  return {
    href: location.href,
    forms,
    triggers,
    calc,
    handlers: sendIds.map(handlerInfo),
    common_js: [...document.scripts].map(s => s.src).filter(s => /common\.js/i.test(s))
  };
}"""


def inspect_page(page, label: str, url: str) -> dict:
    console = []
    page.on("console", lambda m: console.append({"type": m.type, "text": m.text[:300]}))
    page.goto(url, wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(2500)
    inv = page.evaluate(INSPECT_JS)
    inv["label"] = label
    inv["console_errors"] = [c for c in console if c["type"] == "error"][:15]
    return inv


def calc_flow(page, url: str, label: str) -> dict:
    posts = []
    page.on(
        "request",
        lambda r: posts.append({"url": r.url, "method": r.method})
        if r.method == "POST"
        else None,
    )
    page.goto(url, wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(2500)
    before = page.evaluate(
        """() => {
          const f = document.getElementById('callback__FORM_tariff_calc');
          const box = document.querySelector('.tariff-calc-result, .tariff-calc-request');
          const cs = f ? getComputedStyle(f.closest('.tariff-calc-request') || f) : null;
          return {
            form: !!f,
            consent: !!(f && f.querySelector('[name="personal_data_consent"]')),
            names: f ? [...f.querySelectorAll('input,select,textarea')].map(el => el.name) : [],
            result_visible: box ? getComputedStyle(box).display !== 'none' : false,
            request_display: cs ? cs.display : null
          };
        }"""
    )
    btn = page.locator(".tariff-calc-submit")
    clicked = False
    if btn.count():
        btn.first.click(force=True)
        page.wait_for_timeout(1500)
        clicked = True
    after = page.evaluate(
        """() => {
          const f = document.getElementById('callback__FORM_tariff_calc');
          const result = document.querySelector('.tariff-calc-result');
          const req = document.querySelector('.tariff-calc-request');
          return {
            result_text: result ? (result.innerText||'').slice(0,400) : null,
            result_display: result ? getComputedStyle(result).display : null,
            request_display: req ? getComputedStyle(req).display : null,
            form_visible: !!(f && f.offsetParent !== null),
            consent: !!(f && f.querySelector('[name="personal_data_consent"]'))
          };
        }"""
    )
    SHOT.mkdir(parents=True, exist_ok=True)
    page.screenshot(path=str(SHOT / f"{label}-after-calc.png"), full_page=False)
    return {"url": url, "clicked": clicked, "before": before, "after": after, "posts": posts[:8]}


def main() -> None:
    SHOT.mkdir(parents=True, exist_ok=True)
    report = {"ts": utc_now(), "pages": [], "calculators": []}
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900}, user_agent=UA)
        for label, url in PAGES:
            try:
                rec = inspect_page(page, label, url)
                report["pages"].append(rec)
            except Exception as exc:  # noqa: BLE001
                report["pages"].append({"label": label, "url": url, "error": str(exc)})
        for label, url in (("seo_calc", "https://i-seo.su/services/seo.html"), ("tariff_calc", "https://i-seo.su/tariff-calc")):
            pg = browser.new_page(viewport={"width": 1440, "height": 900}, user_agent=UA)
            try:
                report["calculators"].append({"label": label, **calc_flow(pg, url, label)})
            except Exception as exc:  # noqa: BLE001
                report["calculators"].append({"label": label, "url": url, "error": str(exc)})
            pg.close()
        browser.close()
    # derived defects
    defects = []
    for rec in report["pages"]:
        if rec.get("error"):
            defects.append({"id": "NAV", "page": rec.get("label"), "detail": rec["error"]})
            continue
        for f in rec.get("forms") or []:
            if f.get("id") and "FORM" in (f.get("id") or "") and not f.get("consent"):
                defects.append({"id": "NO_CONSENT", "page": rec.get("label"), "form": f.get("id"), "url": rec.get("href")})
            for pc in f.get("phone_contact") or []:
                name = pc.get("name") or ""
                if name and name[0] not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_":
                    defects.append({"id": "CYRILLIC_NAME", "page": rec.get("label"), "form": f.get("id"), "name": name})
        for h in rec.get("handlers") or []:
            urls = h.get("urls") or []
            nested = rec.get("href", "").count("/") >= 4
            if nested and any(u and not u.startswith("/") for u in urls):
                defects.append({"id": "RELATIVE_URL", "page": rec.get("label"), "handler": h.get("id"), "urls": urls, "href": rec.get("href")})
            if h.get("id") and "FORM_send" in (h.get("id") or "") and not h.get("preventDefault_call") and not h.get("return_false"):
                defects.append({"id": "NO_PREVENTDEFAULT", "page": rec.get("label"), "handler": h.get("id")})
    report["derived_defects"] = defects
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print("pages", len(report["pages"]), "defects", len(defects))
    for d in defects[:40]:
        print(d)


if __name__ == "__main__":
    main()
