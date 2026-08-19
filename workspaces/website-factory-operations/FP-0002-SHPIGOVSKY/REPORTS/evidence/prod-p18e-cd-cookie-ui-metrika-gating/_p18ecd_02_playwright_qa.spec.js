const fs = require('node:fs/promises');
const path = require('node:path');
const { test, expect } = require('@playwright/test');

const LIVE = 'https://shpigovsky.ru';
const OUT_DIR = String.raw`X:\AI MARS\worktrees\fp-0002-p18e-cd\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\REPORTS\evidence\prod-p18e-cd-cookie-ui-metrika-gating`;
const SCREEN_DIR = path.join(OUT_DIR, 'screens');
const COOKIE_NAME = 'fp02_cookie_consent';

async function sleep(ms) {
	return new Promise((resolve) => setTimeout(resolve, ms));
}

function cookieRecord(analytics, version = 1) {
	return JSON.stringify({
		version,
		necessary: true,
		analytics,
		decided_at: new Date().toISOString()
	});
}

async function newHarness(browser, options = {}) {
	const context = await browser.newContext({
		baseURL: LIVE,
		viewport: options.viewport || { width: 1280, height: 900 },
		javaScriptEnabled: options.javaScriptEnabled !== false,
		locale: 'ru-RU'
	});
	const page = await context.newPage();
	const requests = [];
	page.on('request', (request) => {
		if (request.url().includes('mc.yandex.ru')) {
			requests.push({
				url: request.url(),
				method: request.method(),
				resourceType: request.resourceType(),
				ts: Date.now()
			});
		}
	});
	return { context, page, requests };
}

async function gotoHome(h) {
	await h.page.goto('/', { waitUntil: 'networkidle' });
	await sleep(1200);
}

async function getCookieValue(context) {
	const cookies = await context.cookies();
	const found = cookies.find((cookie) => cookie.name === COOKIE_NAME);
	return found ? found.value : null;
}

async function bannerVisible(page) {
	return page.locator('[data-fp02-cookie-consent]').isVisible();
}

async function capture(page, name) {
	await page.screenshot({ path: path.join(SCREEN_DIR, name), fullPage: true });
}

test('collect live cookie consent QA evidence', async ({ browser }) => {
	await fs.mkdir(SCREEN_DIR, { recursive: true });

	const results = {
		undecided: {},
		accept: {},
		necessaryOnly: {},
		tampered: {},
		oldVersion: {},
		revoke: {},
		jsDisabled: {},
		accessibility: {},
		mobile: {}
	};

	{
		const h = await newHarness(browser);
		await gotoHome(h);
		results.undecided.bannerVisible = await bannerVisible(h.page);
		results.undecided.cookieValue = await getCookieValue(h.context);
		results.undecided.metrikaRequests = h.requests.length;
		await capture(h.page, 'undecided-home.png');
		expect(results.undecided.bannerVisible).toBeTruthy();
		expect(results.undecided.cookieValue).toBeNull();
		expect(results.undecided.metrikaRequests).toBe(0);
		await h.context.close();
	}

	{
		const h = await newHarness(browser);
		await gotoHome(h);
		await h.page.click('[data-fp02-consent-accept]');
		await h.page.waitForTimeout(2500);
		results.accept.cookieValue = await getCookieValue(h.context);
		results.accept.bannerVisibleAfter = await bannerVisible(h.page);
		results.accept.metrikaRequests = h.requests.length;
		await capture(h.page, 'accept-home.png');
		expect(results.accept.cookieValue).toContain('"analytics":true');
		expect(results.accept.bannerVisibleAfter).toBeFalsy();
		expect(results.accept.metrikaRequests).toBeGreaterThan(0);
		await h.context.close();
	}

	{
		const h = await newHarness(browser);
		await gotoHome(h);
		await h.page.click('[data-fp02-consent-necessary]');
		await h.page.waitForTimeout(1800);
		results.necessaryOnly.cookieValue = await getCookieValue(h.context);
		results.necessaryOnly.bannerVisibleAfter = await bannerVisible(h.page);
		results.necessaryOnly.metrikaRequests = h.requests.length;
		await capture(h.page, 'necessary-only-home.png');
		expect(results.necessaryOnly.cookieValue).toContain('"analytics":false');
		expect(results.necessaryOnly.bannerVisibleAfter).toBeFalsy();
		expect(results.necessaryOnly.metrikaRequests).toBe(0);
		await h.context.close();
	}

	{
		const h = await newHarness(browser);
		await h.context.addCookies([{
			name: COOKIE_NAME,
			value: '%7Bbad-json',
			url: LIVE,
			path: '/'
		}]);
		await gotoHome(h);
		results.tampered.bannerVisible = await bannerVisible(h.page);
		results.tampered.metrikaRequests = h.requests.length;
		await capture(h.page, 'tampered-home.png');
		expect(results.tampered.bannerVisible).toBeTruthy();
		expect(results.tampered.metrikaRequests).toBe(0);
		await h.context.close();
	}

	{
		const h = await newHarness(browser);
		await h.context.addCookies([{
			name: COOKIE_NAME,
			value: encodeURIComponent(cookieRecord(true, 0)),
			url: LIVE,
			path: '/'
		}]);
		await gotoHome(h);
		results.oldVersion.bannerVisible = await bannerVisible(h.page);
		results.oldVersion.metrikaRequests = h.requests.length;
		await capture(h.page, 'old-version-home.png');
		expect(results.oldVersion.bannerVisible).toBeTruthy();
		expect(results.oldVersion.metrikaRequests).toBe(0);
		await h.context.close();
	}

	{
		const h = await newHarness(browser);
		await gotoHome(h);
		await h.page.click('[data-fp02-consent-accept]');
		await h.page.waitForTimeout(2000);
		const beforeRevokeCount = h.requests.length;
		await h.page.evaluate(() => window.FP02PrivacyConsent.openSettings());
		await h.page.locator('[data-fp02-consent-analytics]').uncheck();
		await h.page.click('[data-fp02-consent-save]');
		await h.page.waitForLoadState('networkidle');
		await h.page.waitForTimeout(1500);
		results.revoke.cookieValue = await getCookieValue(h.context);
		results.revoke.newRequestsAfterRevoke = h.requests.length - beforeRevokeCount;
		await capture(h.page, 'revoke-home.png');
		expect(results.revoke.cookieValue).toContain('"analytics":false');
		expect(results.revoke.newRequestsAfterRevoke).toBe(0);
		await h.context.close();
	}

	{
		const h = await newHarness(browser, { javaScriptEnabled: false });
		await gotoHome(h);
		results.jsDisabled.metrikaRequests = h.requests.length;
		await capture(h.page, 'js-disabled-home.png');
		expect(results.jsDisabled.metrikaRequests).toBe(0);
		await h.context.close();
	}

	{
		const h = await newHarness(browser);
		await gotoHome(h);
		await h.page.keyboard.press('Tab');
		results.accessibility.firstFocusText = await h.page.evaluate(() => (document.activeElement && document.activeElement.textContent || '').trim());
		await h.page.click('[data-fp02-consent-customize]');
		results.accessibility.settingsVisible = await h.page.locator('[data-fp02-consent-settings]').isVisible();
		await h.page.keyboard.press('Escape');
		await h.page.waitForTimeout(300);
		results.accessibility.settingsVisibleAfterEscape = await h.page.locator('[data-fp02-consent-settings]').isVisible();
		await capture(h.page, 'accessibility-home.png');
		expect(results.accessibility.settingsVisible).toBeTruthy();
		expect(results.accessibility.settingsVisibleAfterEscape).toBeFalsy();
		await h.context.close();
	}

	for (const width of [320, 360, 390, 768, 1280]) {
		const key = String(width);
		const h = await newHarness(browser, {
			viewport: { width, height: width < 768 ? 900 : 960 }
		});
		await gotoHome(h);
		results.mobile[key] = await h.page.evaluate(() => ({
			scrollWidth: document.documentElement.scrollWidth,
			innerWidth: window.innerWidth,
			noOverflow: document.documentElement.scrollWidth <= window.innerWidth + 1
		}));
		await capture(h.page, `mobile-${width}.png`);
		expect(results.mobile[key].noOverflow).toBeTruthy();
		await h.context.close();
	}

	await fs.writeFile(path.join(OUT_DIR, 'PLAYWRIGHT-QA.json'), JSON.stringify(results, null, 2) + '\n', 'utf8');
});
