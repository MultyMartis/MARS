# -*- coding: utf-8 -*-
"""Live Playwright QA for P18E-C/D cookie consent and Metrika gating."""
from __future__ import annotations

import json
from pathlib import Path

from playwright.sync_api import sync_playwright

LIVE = "https://shpigovsky.ru"
OUT_DIR = Path(
    r"X:\AI MARS\worktrees\fp-0002-p18e-cd\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\REPORTS\evidence\prod-p18e-cd-cookie-ui-metrika-gating"
)
SCREEN_DIR = OUT_DIR / "screens"
COOKIE_NAME = "fp02_cookie_consent"


def cookie_record(analytics: bool, version: int = 1) -> str:
    return json.dumps(
        {
            "version": version,
            "necessary": True,
            "analytics": analytics,
            "decided_at": "2026-08-19T12:00:00Z",
        },
        ensure_ascii=False,
        separators=(",", ":"),
    )


def new_harness(browser, *, viewport=None, javascript_enabled=True):
    context = browser.new_context(
        base_url=LIVE,
        locale="ru-RU",
        viewport=viewport or {"width": 1280, "height": 900},
        java_script_enabled=javascript_enabled,
    )
    page = context.new_page()
    requests = []

    def on_request(request):
        url = request.url
        if "mc.yandex.ru" in url:
            requests.append(
                {
                    "url": url,
                    "method": request.method,
                    "resource_type": request.resource_type,
                }
            )

    page.on("request", on_request)
    return context, page, requests


def goto_home(page):
    page.goto("/", wait_until="networkidle")
    page.wait_for_timeout(1200)


def cookie_value(context):
    for cookie in context.cookies():
        if cookie.get("name") == COOKIE_NAME:
            return cookie.get("value")
    return None


def banner_visible(page):
    return page.locator("[data-fp02-cookie-consent]").is_visible()


def screenshot(page, name: str):
    SCREEN_DIR.mkdir(parents=True, exist_ok=True)
    page.screenshot(path=str(SCREEN_DIR / name), full_page=True)


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    SCREEN_DIR.mkdir(parents=True, exist_ok=True)
    results = {
        "undecided": {},
        "accept": {},
        "necessary_only": {},
        "custom_on": {},
        "custom_off": {},
        "persistence": {},
        "tampered": {},
        "old_version": {},
        "revoke": {},
        "js_disabled": {},
        "accessibility": {},
        "mobile": {},
    }

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)

        # Undecided.
        context, page, requests = new_harness(browser)
        goto_home(page)
        results["undecided"] = {
            "banner_visible": banner_visible(page),
            "cookie_value": cookie_value(context),
            "metrika_requests": len(requests),
        }
        screenshot(page, "undecided-home.png")
        context.close()

        # Accept.
        context, page, requests = new_harness(browser)
        goto_home(page)
        page.locator("[data-fp02-consent-accept]").click()
        page.wait_for_timeout(2500)
        results["accept"] = {
            "cookie_value": cookie_value(context),
            "banner_visible_after": banner_visible(page),
            "metrika_requests": len(requests),
        }
        screenshot(page, "accept-home.png")
        context.close()

        # Necessary only.
        context, page, requests = new_harness(browser)
        goto_home(page)
        page.locator("[data-fp02-consent-necessary]").click()
        page.wait_for_timeout(1800)
        results["necessary_only"] = {
            "cookie_value": cookie_value(context),
            "banner_visible_after": banner_visible(page),
            "metrika_requests": len(requests),
        }
        screenshot(page, "necessary-only-home.png")
        context.close()

        # Custom settings on.
        context, page, requests = new_harness(browser)
        goto_home(page)
        page.locator("[data-fp02-consent-customize]").click()
        page.locator("[data-fp02-consent-analytics]").evaluate("(node) => { node.checked = true; node.dispatchEvent(new Event('change', { bubbles: true })); }")
        page.locator("[data-fp02-consent-save]").click()
        page.wait_for_timeout(2200)
        results["custom_on"] = {
            "cookie_value": cookie_value(context),
            "metrika_requests": len(requests),
        }
        screenshot(page, "custom-on-home.png")
        context.close()

        # Custom settings off.
        context, page, requests = new_harness(browser)
        goto_home(page)
        page.locator("[data-fp02-consent-customize]").click()
        page.locator("[data-fp02-consent-analytics]").evaluate("(node) => { node.checked = false; node.dispatchEvent(new Event('change', { bubbles: true })); }")
        page.locator("[data-fp02-consent-save]").click()
        page.wait_for_timeout(1800)
        results["custom_off"] = {
            "cookie_value": cookie_value(context),
            "metrika_requests": len(requests),
        }
        screenshot(page, "custom-off-home.png")
        context.close()

        # Persistence.
        context, page, requests = new_harness(browser)
        goto_home(page)
        page.locator("[data-fp02-consent-accept]").click()
        page.wait_for_timeout(2000)
        before_nav_accept = len(requests)
        page.goto("/kontakty/", wait_until="networkidle")
        page.wait_for_timeout(1200)
        results["persistence"]["accept"] = {
            "cookie_value": cookie_value(context),
            "banner_visible_on_contacts": banner_visible(page),
            "new_requests_after_nav": len(requests) - before_nav_accept,
        }
        screenshot(page, "persistence-accept-contacts.png")
        context.close()

        context, page, requests = new_harness(browser)
        goto_home(page)
        page.locator("[data-fp02-consent-necessary]").click()
        page.wait_for_timeout(1500)
        before_nav_necessary = len(requests)
        page.goto("/kontakty/", wait_until="networkidle")
        page.wait_for_timeout(1200)
        results["persistence"]["necessary_only"] = {
            "cookie_value": cookie_value(context),
            "banner_visible_on_contacts": banner_visible(page),
            "new_requests_after_nav": len(requests) - before_nav_necessary,
        }
        screenshot(page, "persistence-necessary-contacts.png")
        context.close()

        # Tampered.
        context, page, requests = new_harness(browser)
        context.add_cookies(
            [
                {
                    "name": COOKIE_NAME,
                    "value": "%7Bbad-json",
                    "url": LIVE,
                }
            ]
        )
        goto_home(page)
        results["tampered"] = {
            "banner_visible": banner_visible(page),
            "metrika_requests": len(requests),
        }
        screenshot(page, "tampered-home.png")
        context.close()

        # Old version.
        context, page, requests = new_harness(browser)
        context.add_cookies(
            [
                {
                    "name": COOKIE_NAME,
                    "value": cookie_record(True, 0),
                    "url": LIVE,
                }
            ]
        )
        goto_home(page)
        results["old_version"] = {
            "banner_visible": banner_visible(page),
            "metrika_requests": len(requests),
        }
        screenshot(page, "old-version-home.png")
        context.close()

        # Revoke.
        context, page, requests = new_harness(browser)
        goto_home(page)
        page.locator("[data-fp02-consent-accept]").click()
        page.wait_for_timeout(2000)
        before_revoke = len(requests)
        page.evaluate("window.FP02PrivacyConsent.openSettings()")
        page.locator("[data-fp02-consent-analytics]").evaluate("(node) => { node.checked = false; node.dispatchEvent(new Event('change', { bubbles: true })); }")
        page.locator("[data-fp02-consent-save]").click()
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(1500)
        after_reload_count = len(requests)
        page.goto("/kontakty/", wait_until="networkidle")
        page.wait_for_timeout(1200)
        results["revoke"] = {
            "cookie_value": cookie_value(context),
            "new_requests_after_revoke": len(requests) - before_revoke,
            "new_requests_after_post_revoke_nav": len(requests) - after_reload_count,
        }
        screenshot(page, "revoke-home.png")
        context.close()

        # JS disabled.
        context, page, requests = new_harness(browser, javascript_enabled=False)
        goto_home(page)
        results["js_disabled"] = {
            "metrika_requests": len(requests),
        }
        screenshot(page, "js-disabled-home.png")
        context.close()

        # Accessibility.
        context, page, requests = new_harness(browser)
        goto_home(page)
        page.keyboard.press("Tab")
        first_focus = page.evaluate("(document.activeElement && document.activeElement.textContent || '').trim()")
        page.locator("[data-fp02-consent-customize]").click()
        settings_visible = page.locator("[data-fp02-consent-settings]").is_visible()
        page.keyboard.press("Escape")
        page.wait_for_timeout(300)
        settings_after_escape = page.locator("[data-fp02-consent-settings]").is_visible()
        results["accessibility"] = {
            "first_focus_text": first_focus,
            "settings_visible": settings_visible,
            "settings_visible_after_escape": settings_after_escape,
        }
        screenshot(page, "accessibility-home.png")
        context.close()

        # Mobile widths.
        for width in (320, 360, 390, 768, 1280):
            context, page, requests = new_harness(
                browser,
                viewport={"width": width, "height": 900 if width < 768 else 960},
            )
            goto_home(page)
            results["mobile"][str(width)] = page.evaluate(
                """() => ({
                    scrollWidth: document.documentElement.scrollWidth,
                    innerWidth: window.innerWidth,
                    noOverflow: document.documentElement.scrollWidth <= window.innerWidth + 1
                })"""
            )
            screenshot(page, f"mobile-{width}.png")
            context.close()

        browser.close()

    (OUT_DIR / "PLAYWRIGHT-QA.json").write_text(
        json.dumps(results, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
