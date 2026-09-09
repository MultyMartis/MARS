#!/usr/bin/env python3
from playwright.sync_api import sync_playwright
import json

URL = "https://i-seo.su/services/seo/prodvizhenie-sajta-restorana.html"

with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    page = b.new_page()
    page.goto(URL, wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(7000)
    f = page.locator("#page__FORM_seo")
    f.scroll_into_view_if_needed()
    f.locator("input[name='pf_name']").fill("RestDiag")
    phone = f.locator("input[name='pf_phone']")
    phone.click()
    phone.fill("")
    phone.type("9115033303", delay=40)
    page.wait_for_timeout(400)
    f.locator("input[name='personal_data_consent']").first.check(force=True)
    detail = page.evaluate(
        """() => {
          const form = jQuery('#page__FORM_seo');
          const out = [];
          form.find('input,textarea,select').each(function(){
            const el = this;
            const $el = jQuery(el);
            out.push({
              name: el.name,
              id: el.id,
              type: el.type,
              className: el.className,
              val: String($el.val() || '').slice(0, 48),
              required: !!$el.prop('required'),
              checked: !!$el.prop('checked'),
              hasReqCb: $el.hasClass('required-checkbox')
            });
          });
          return {
            blocked: checkEmptyFields(form),
            phoneVal: form.find('input[name=\"pf_phone\"]').val(),
            fields: out
          };
        }"""
    )
    print(json.dumps(detail, ensure_ascii=False, indent=2))
    b.close()
