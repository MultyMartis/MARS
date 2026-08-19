import fs from 'node:fs/promises';
import path from 'node:path';
import { chromium } from 'playwright';

const LIVE = 'https://shpigovsky.ru';
const OUT_DIR = String.raw`X:\AI MARS\worktrees\fp-0002-p18e-ef\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\REPORTS\evidence\prod-p18e-ef-form-goal-policy-integration`;
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

async function newHarness(options = {}) {
	const browser = await chromium.launch({ headless: true });
	const context = await browser.newContext({
		baseURL: LIVE,
		viewport: options.viewport || { width: 1280, height: 920 },
		javaScriptEnabled: options.javaScriptEnabled !== false,
		locale: 'ru-RU',
		colorScheme: 'light'
	});

	if (options.cookieValue) {
		await context.addCookies([{
			name: COOKIE_NAME,
			value: encodeURIComponent(options.cookieValue),
			url: LIVE
		}]);
	}

	const page = await context.newPage();
	const requests = [];
	const pageErrors = [];
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
	page.on('pageerror', (error) => {
		pageErrors.push(String(error));
	});

	if (options.abortMetrika) {
		await page.route('https://mc.yandex.ru/**', (route) => route.abort());
	}

	return { browser, context, page, requests, pageErrors };
}

async function goto(page, url = '/') {
	await page.goto(url, { waitUntil: 'networkidle' });
	await sleep(1200);
}

async function capture(page, name) {
	await page.screenshot({ path: path.join(SCREEN_DIR, name), fullPage: true });
}

async function installYmProbe(page) {
	await page.evaluate(() => {
		window.__fp02YmCalls = [];
		if (typeof window.ym === 'function' && !window.__fp02YmWrapped) {
			const original = window.ym;
			const wrapped = function (...args) {
				window.__fp02YmCalls.push(args);
				return original.apply(this, args);
			};
			wrapped.a = original.a;
			wrapped.l = original.l;
			window.ym = wrapped;
			window.__fp02YmWrapped = true;
		}
	});
}

async function getYmCalls(page) {
	return page.evaluate(() => Array.isArray(window.__fp02YmCalls) ? window.__fp02YmCalls : []);
}

async function formSubmit(page, marker) {
	let form = page.locator('.final-form__form').first();
	if (!(await form.isVisible().catch(() => false))) {
		const trigger = page.locator('[data-modal-open="consultation"]:visible').first();
		await trigger.click();
		await page.locator('.modal-consultation[data-modal-state="open"]').waitFor({ state: 'visible', timeout: 10000 });
		form = page.locator('.modal-consultation[data-modal-state="open"] [data-lead-form]').first();
	}
	await form.evaluate((node, token) => {
		const ensureHidden = (name, value) => {
			let input = node.querySelector(`input[name="${name}"]`);
			if (!input) {
				input = document.createElement('input');
				input.type = 'hidden';
				input.name = name;
				node.appendChild(input);
			}
			input.value = value;
		};
		ensureHidden('fp02_qa', '1');
	}, marker);

	await form.locator('input[name="name"]').fill(`QA P18EF ${marker}`);
	await form.locator('input[name="phone"]').fill('+7 (925) 183-64-64');
	await form.locator('textarea[name="message"]').fill(`QA marker ${marker}. Technical privacy regression check.`);
	await form.locator('input[name="consent"]').check();
	await page.waitForTimeout(3200);
	await form.locator('button[type="submit"]').click();
	await expectSuccess(form);
}

async function expectSuccess(form) {
	const status = form.locator('[data-lead-form-status]');
	await status.waitFor({ state: 'visible', timeout: 30000 });
	await status.waitFor({ state: 'attached', timeout: 30000 });
	await sleep(1200);
}

async function footerSettingsOpen(page) {
	const trigger = page.locator('[data-fp02-cookie-settings-open]').first();
	await trigger.scrollIntoViewIfNeeded();
	await trigger.click();
	await page.locator('[data-fp02-consent-settings]').waitFor({ state: 'visible', timeout: 10000 });
	return trigger;
}

async function setAnalyticsToggle(page, checked) {
	const toggle = page.locator('[data-fp02-consent-analytics]');
	const current = await toggle.isChecked();
	if (current === checked) {
		return toggle;
	}
	await toggle.evaluate((node) => {
		const label = node.closest('label');
		if (label) {
			label.click();
		} else {
			node.click();
		}
	});
	return toggle;
}

const results = {
	reopen: {},
	necessaryOnly: {},
	analyticsAllowed: {},
	noMetrikaFailure: {},
	withdrawal: {},
	regrant: {},
	accessibility: {},
	mobile: {}
};

// Reopen / state reflection.
{
	const h = await newHarness({ cookieValue: cookieRecord(false) });
	try {
		await goto(h.page, '/');
		const trigger = await footerSettingsOpen(h.page);
		results.reopen.footerTriggerText = await trigger.textContent();
		results.reopen.toggleCheckedForNecessary = await h.page.locator('[data-fp02-consent-analytics]').isChecked();
		results.reopen.visible = await h.page.locator('[data-fp02-consent-settings]').isVisible();
		await capture(h.page, 'reopen-home.png');
	} finally {
		await h.context.close();
		await h.browser.close();
	}
}

// Necessary-only form QA.
{
	const marker = `necessary-${Date.now()}`;
	const h = await newHarness({ cookieValue: cookieRecord(false) });
	try {
		await goto(h.page, '/kontakty/');
		await installYmProbe(h.page);
		await formSubmit(h.page, marker);
		results.necessaryOnly.marker = marker;
		results.necessaryOnly.ymCalls = await getYmCalls(h.page);
		results.necessaryOnly.metrikaRequests = h.requests;
		results.necessaryOnly.pageErrors = h.pageErrors;
		results.necessaryOnly.successText = await h.page.locator('[data-lead-form-status]').first().textContent();
		await capture(h.page, 'necessary-only-form-success.png');
	} finally {
		await h.context.close();
		await h.browser.close();
	}
}

// Analytics-allowed form QA.
{
	const marker = `analytics-${Date.now()}`;
	const h = await newHarness({ cookieValue: cookieRecord(true) });
	try {
		await goto(h.page, '/kontakty/');
		await installYmProbe(h.page);
		await formSubmit(h.page, marker);
		results.analyticsAllowed.marker = marker;
		results.analyticsAllowed.ymCalls = await getYmCalls(h.page);
		results.analyticsAllowed.metrikaRequests = h.requests;
		results.analyticsAllowed.pageErrors = h.pageErrors;
		results.analyticsAllowed.scriptTagCount = await h.page.locator('script[data-fp02-metrika-script]').count();
		await capture(h.page, 'analytics-allowed-form-success.png');
	} finally {
		await h.context.close();
		await h.browser.close();
	}
}

// Analytics allowed but Metrika unavailable.
{
	const marker = `blocked-${Date.now()}`;
	const h = await newHarness({ cookieValue: cookieRecord(true), abortMetrika: true });
	try {
		await goto(h.page, '/kontakty/');
		await installYmProbe(h.page);
		await formSubmit(h.page, marker);
		results.noMetrikaFailure.marker = marker;
		results.noMetrikaFailure.ymCalls = await getYmCalls(h.page);
		results.noMetrikaFailure.metrikaRequests = h.requests;
		results.noMetrikaFailure.pageErrors = h.pageErrors;
		results.noMetrikaFailure.successText = await h.page.locator('[data-lead-form-status]').first().textContent();
		await capture(h.page, 'no-metrika-failure-form-success.png');
	} finally {
		await h.context.close();
		await h.browser.close();
	}
}

// Withdrawal blocks future goals.
{
	const marker = `withdraw-${Date.now()}`;
	const h = await newHarness({ cookieValue: cookieRecord(true) });
	try {
		await goto(h.page, '/kontakty/');
		await footerSettingsOpen(h.page);
		const toggle = h.page.locator('[data-fp02-consent-analytics]');
		results.withdrawal.initialToggleChecked = await toggle.isChecked();
		await setAnalyticsToggle(h.page, false);
		await h.page.locator('[data-fp02-consent-save]').click();
		await h.page.waitForLoadState('networkidle');
		await sleep(1200);
		await installYmProbe(h.page);
		await formSubmit(h.page, marker);
		results.withdrawal.marker = marker;
		results.withdrawal.cookieValue = await h.context.cookies();
		results.withdrawal.ymCalls = await getYmCalls(h.page);
		results.withdrawal.metrikaRequests = h.requests;
		results.withdrawal.pageErrors = h.pageErrors;
		await capture(h.page, 'withdrawal-form-success.png');
	} finally {
		await h.context.close();
		await h.browser.close();
	}
}

// Re-grant loads once and reflects in UI.
{
	const h = await newHarness({ cookieValue: cookieRecord(false) });
	try {
		await goto(h.page, '/');
		await footerSettingsOpen(h.page);
		await setAnalyticsToggle(h.page, true);
		await h.page.locator('[data-fp02-consent-save]').click();
		await sleep(2500);
		results.regrant.metrikaRequests = h.requests;
		results.regrant.scriptTagCount = await h.page.locator('script[data-fp02-metrika-script]').count();
		await capture(h.page, 'regrant-home.png');
	} finally {
		await h.context.close();
		await h.browser.close();
	}
}

// Accessibility / focus return on desktop.
{
	const h = await newHarness({ cookieValue: cookieRecord(false) });
	try {
		await goto(h.page, '/');
		await h.page.keyboard.press('Tab');
		let activeText = await h.page.evaluate(() => (document.activeElement && document.activeElement.textContent || '').trim());
		if (!activeText.includes('Настройки cookie')) {
			const trigger = h.page.locator('[data-fp02-cookie-settings-open]').first();
			await trigger.focus();
		}
		await h.page.keyboard.press('Enter');
		await h.page.locator('[data-fp02-consent-settings]').waitFor({ state: 'visible' });
		await h.page.keyboard.press('Escape');
		await sleep(300);
		results.accessibility.focusAfterEscape = await h.page.evaluate(() => (document.activeElement && document.activeElement.textContent || '').trim());
		results.accessibility.settingsVisibleAfterEscape = await h.page.locator('[data-fp02-consent-settings]').isVisible();
		await capture(h.page, 'accessibility-footer-reopen.png');
	} finally {
		await h.context.close();
		await h.browser.close();
	}
}

// Mobile widths.
for (const width of [320, 360, 393, 1280]) {
	const h = await newHarness({
		cookieValue: cookieRecord(false),
		viewport: { width, height: width < 768 ? 900 : 960 }
	});
	try {
		await goto(h.page, '/');
		const trigger = await footerSettingsOpen(h.page);
		results.mobile[String(width)] = {
			triggerText: await trigger.textContent(),
			noOverflow: await h.page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth + 1),
			settingsVisible: await h.page.locator('[data-fp02-consent-settings]').isVisible()
		};
		await capture(h.page, `mobile-${width}-footer-reopen.png`);
	} finally {
		await h.context.close();
		await h.browser.close();
	}
}

await fs.writeFile(
	path.join(OUT_DIR, '03-live-qa.json'),
	JSON.stringify(results, null, 2) + '\n',
	'utf8'
);
