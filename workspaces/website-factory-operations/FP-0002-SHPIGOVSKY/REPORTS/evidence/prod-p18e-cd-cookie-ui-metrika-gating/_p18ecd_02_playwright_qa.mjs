import fs from 'node:fs/promises';
import path from 'node:path';
import { chromium } from 'playwright';

const LIVE = 'https://shpigovsky.ru';
const OUT_DIR = String.raw`X:\AI MARS\worktrees\fp-0002-p18e-cd\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\REPORTS\evidence\prod-p18e-cd-cookie-ui-metrika-gating`;
const SCREEN_DIR = path.join(OUT_DIR, 'screens');
const COOKIE_NAME = 'fp02_cookie_consent';

await fs.mkdir(SCREEN_DIR, { recursive: true });

function sleep(ms) {
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
		colorScheme: 'light',
		locale: 'ru-RU'
	});

	if (options.reducedMotion) {
		await context.grantPermissions([]);
	}

	const page = await context.newPage();
	const requests = [];
	page.on('request', (request) => {
		const url = request.url();
		if (url.includes('mc.yandex.ru')) {
			requests.push({
				url,
				method: request.method(),
				resourceType: request.resourceType(),
				ts: Date.now()
			});
		}
	});

	return { context, page, requests };
}

async function getCookieValue(context) {
	const cookies = await context.cookies();
	const found = cookies.find((item) => item.name === COOKIE_NAME);
	return found ? found.value : null;
}

async function gotoHome(h) {
	await h.page.goto('/', { waitUntil: 'networkidle' });
	await sleep(1200);
}

async function isBannerVisible(page) {
	return page.locator('[data-fp02-cookie-consent]').isVisible();
}

async function capture(page, name) {
	await page.screenshot({ path: path.join(SCREEN_DIR, name), fullPage: true });
}

const browser = await chromium.launch({ headless: true });
const results = {
	undecided: {},
	accept: {},
	necessaryOnly: {},
	customOn: {},
	customOff: {},
	persistence: {},
	tampered: {},
	oldVersion: {},
	revoke: {},
	jsDisabled: {},
	accessibility: {},
	mobile: {},
	reducedMotion: {}
};

try {
	// Fresh visitor / undecided.
	{
		const h = await newHarness(browser);
		await gotoHome(h);
		results.undecided.bannerVisible = await isBannerVisible(h.page);
		results.undecided.cookieValue = await getCookieValue(h.context);
		results.undecided.metrikaRequests = h.requests.length;
		await capture(h.page, 'undecided-home.png');
		await h.context.close();
	}

	// Accept flow.
	{
		const h = await newHarness(browser);
		await gotoHome(h);
		await h.page.click('[data-fp02-consent-accept]');
		await h.page.waitForTimeout(2500);
		results.accept.bannerVisibleAfter = await isBannerVisible(h.page);
		results.accept.cookieValue = await getCookieValue(h.context);
		results.accept.metrikaRequests = h.requests.length;
		results.accept.tagJsLoaded = h.requests.some((item) => item.url.includes('/metrika/tag.js'));
		await capture(h.page, 'accept-home.png');
		await h.context.close();
	}

	// Necessary only.
	{
		const h = await newHarness(browser);
		await gotoHome(h);
		await h.page.click('[data-fp02-consent-necessary]');
		await h.page.waitForTimeout(1800);
		results.necessaryOnly.bannerVisibleAfter = await isBannerVisible(h.page);
		results.necessaryOnly.cookieValue = await getCookieValue(h.context);
		results.necessaryOnly.metrikaRequests = h.requests.length;
		await capture(h.page, 'necessary-only-home.png');
		await h.context.close();
	}

	// Custom on.
	{
		const h = await newHarness(browser);
		await gotoHome(h);
		await h.page.click('[data-fp02-consent-customize]');
		const toggle = h.page.locator('[data-fp02-consent-analytics]');
		await toggle.check();
		await h.page.click('[data-fp02-consent-save]');
		await h.page.waitForTimeout(2500);
		results.customOn.cookieValue = await getCookieValue(h.context);
		results.customOn.metrikaRequests = h.requests.length;
		await capture(h.page, 'custom-on-home.png');
		await h.context.close();
	}

	// Custom off.
	{
		const h = await newHarness(browser);
		await gotoHome(h);
		await h.page.click('[data-fp02-consent-customize]');
		const toggle = h.page.locator('[data-fp02-consent-analytics]');
		await toggle.uncheck();
		await h.page.click('[data-fp02-consent-save]');
		await h.page.waitForTimeout(1800);
		results.customOff.cookieValue = await getCookieValue(h.context);
		results.customOff.metrikaRequests = h.requests.length;
		await capture(h.page, 'custom-off-home.png');
		await h.context.close();
	}

	// Persistence across navigation.
	{
		const h = await newHarness(browser);
		await gotoHome(h);
		await h.page.click('[data-fp02-consent-accept]');
		await h.page.waitForTimeout(2000);
		const beforeNavCount = h.requests.length;
		await h.page.goto('/kontakty/', { waitUntil: 'networkidle' });
		await h.page.waitForTimeout(1500);
		results.persistence.acceptCookie = await getCookieValue(h.context);
		results.persistence.acceptBannerOnContacts = await isBannerVisible(h.page);
		results.persistence.acceptNewRequestsAfterNav = h.requests.length - beforeNavCount;
		await capture(h.page, 'persistence-accept-contacts.png');
		await h.context.close();
	}

	{
		const h = await newHarness(browser);
		await gotoHome(h);
		await h.page.click('[data-fp02-consent-necessary]');
		await h.page.waitForTimeout(1200);
		const beforeNavCount = h.requests.length;
		await h.page.goto('/kontakty/', { waitUntil: 'networkidle' });
		await h.page.waitForTimeout(1500);
		results.persistence.necessaryCookie = await getCookieValue(h.context);
		results.persistence.necessaryBannerOnContacts = await isBannerVisible(h.page);
		results.persistence.necessaryNewRequestsAfterNav = h.requests.length - beforeNavCount;
		await capture(h.page, 'persistence-necessary-contacts.png');
		await h.context.close();
	}

	// Tampered cookie.
	{
		const h = await newHarness(browser);
		await h.context.addCookies([{
			name: COOKIE_NAME,
			value: '%7Bbad-json',
			url: LIVE,
			path: '/'
		}]);
		await gotoHome(h);
		results.tampered.bannerVisible = await isBannerVisible(h.page);
		results.tampered.metrikaRequests = h.requests.length;
		await capture(h.page, 'tampered-home.png');
		await h.context.close();
	}

	// Old version cookie.
	{
		const h = await newHarness(browser);
		await h.context.addCookies([{
			name: COOKIE_NAME,
			value: encodeURIComponent(cookieRecord(true, 0)),
			url: LIVE,
			path: '/'
		}]);
		await gotoHome(h);
		results.oldVersion.bannerVisible = await isBannerVisible(h.page);
		results.oldVersion.metrikaRequests = h.requests.length;
		await capture(h.page, 'old-version-home.png');
		await h.context.close();
	}

	// Revoke.
	{
		const h = await newHarness(browser);
		await gotoHome(h);
		await h.page.click('[data-fp02-consent-accept]');
		await h.page.waitForTimeout(2000);
		const beforeRevokeCount = h.requests.length;
		await h.page.evaluate(() => {
			window.FP02PrivacyConsent.openSettings();
		});
		const toggle = h.page.locator('[data-fp02-consent-analytics]');
		await toggle.uncheck();
		await h.page.click('[data-fp02-consent-save]');
		await h.page.waitForLoadState('networkidle');
		await h.page.waitForTimeout(1500);
		results.revoke.cookieValue = await getCookieValue(h.context);
		results.revoke.newRequestsAfterRevoke = h.requests.length - beforeRevokeCount;
		results.revoke.bannerVisibleAfterReload = await isBannerVisible(h.page);
		await capture(h.page, 'revoke-home.png');
		await h.context.close();
	}

	// JS disabled.
	{
		const h = await newHarness(browser, { javaScriptEnabled: false });
		await gotoHome(h);
		results.jsDisabled.bannerVisible = await h.page.locator('[data-fp02-cookie-consent]').isVisible().catch(() => false);
		results.jsDisabled.metrikaRequests = h.requests.length;
		await capture(h.page, 'js-disabled-home.png');
		await h.context.close();
	}

	// Accessibility / keyboard.
	{
		const h = await newHarness(browser);
		await gotoHome(h);
		await h.page.keyboard.press('Tab');
		results.accessibility.firstFocusText = await h.page.evaluate(() => (document.activeElement && document.activeElement.textContent || '').trim());
		await h.page.keyboard.press('Tab');
		results.accessibility.secondFocusText = await h.page.evaluate(() => (document.activeElement && document.activeElement.textContent || '').trim());
		await h.page.click('[data-fp02-consent-customize]');
		results.accessibility.settingsVisible = await h.page.locator('[data-fp02-consent-settings]').isVisible();
		await h.page.keyboard.press('Escape');
		await h.page.waitForTimeout(300);
		results.accessibility.settingsVisibleAfterEscape = await h.page.locator('[data-fp02-consent-settings]').isVisible();
		await capture(h.page, 'accessibility-home.png');
		await h.context.close();
	}

	// Reduced motion.
	{
		const h = await newHarness(browser);
		await h.page.emulateMedia({ reducedMotion: 'reduce' });
		await gotoHome(h);
		results.reducedMotion.bannerVisible = await isBannerVisible(h.page);
		await capture(h.page, 'reduced-motion-home.png');
		await h.context.close();
	}

	// Mobile / viewport sanity.
	for (const width of [320, 360, 390, 768, 1280]) {
		const key = String(width);
		const h = await newHarness(browser, {
			viewport: { width, height: width < 768 ? 900 : 960 }
		});
		await gotoHome(h);
		results.mobile[key] = await h.page.evaluate(() => {
			const root = document.querySelector('[data-fp02-cookie-consent]');
			const rect = root ? root.getBoundingClientRect() : null;
			return {
				scrollWidth: document.documentElement.scrollWidth,
				innerWidth: window.innerWidth,
				noOverflow: document.documentElement.scrollWidth <= window.innerWidth + 1,
				cardWidth: rect ? rect.width : null
			};
		});
		await capture(h.page, `mobile-${width}.png`);
		await h.context.close();
	}
} finally {
	await browser.close();
}

await fs.writeFile(
	path.join(OUT_DIR, 'PLAYWRIGHT-QA.json'),
	JSON.stringify(results, null, 2) + '\n',
	'utf8'
);
