import fs from 'node:fs/promises';
import path from 'node:path';
import { chromium } from 'playwright';

const LIVE = 'https://shpigovsky.ru';
const OUT_DIR = path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Z]:)/, '$1'));
const COOKIE_NAME = 'fp02_cookie_consent';

function cookieRecord(analytics) {
	return JSON.stringify({
		version: 1,
		necessary: true,
		analytics,
		decided_at: new Date().toISOString(),
	});
}

async function countMetrika(page) {
	return page.evaluate(() => {
		const scripts = Array.from(document.querySelectorAll('script[src*="mc.yandex.ru"]'));
		return scripts.length;
	});
}

const browser = await chromium.launch({ headless: true });
const results = [];

async function runCase(name, fn) {
	try {
		const detail = await fn();
		results.push({ name, status: 'PASS', ...detail });
	} catch (error) {
		results.push({ name, status: 'FAIL', error: String(error?.message || error) });
	}
}

await runCase('UNDECIDED — banner visible, no Metrika', async () => {
	const context = await browser.newContext({ baseURL: LIVE });
	const page = await context.newPage();
	await page.goto('/', { waitUntil: 'domcontentloaded' });
	const banner = page.locator('[data-cookie-consent-banner]');
	await banner.waitFor({ state: 'visible', timeout: 15000 });
	const metrika = await countMetrika(page);
	await context.close();
	if (metrika > 0) throw new Error(`Metrika scripts=${metrika}`);
	return { metrika };
});

await runCase('NECESSARY_ONLY — no Metrika', async () => {
	const context = await browser.newContext({ baseURL: LIVE });
	await context.addCookies([
		{
			name: COOKIE_NAME,
			value: encodeURIComponent(cookieRecord(false)),
			domain: 'shpigovsky.ru',
			path: '/',
		},
	]);
	const page = await context.newPage();
	await page.goto('/', { waitUntil: 'networkidle' });
	const metrika = await countMetrika(page);
	await context.close();
	if (metrika > 0) throw new Error(`Metrika scripts=${metrika}`);
	return { metrika };
});

await runCase('ANALYTICS_ALLOWED — Metrika loads', async () => {
	const context = await browser.newContext({ baseURL: LIVE });
	await context.addCookies([
		{
			name: COOKIE_NAME,
			value: encodeURIComponent(cookieRecord(true)),
			domain: 'shpigovsky.ru',
			path: '/',
		},
	]);
	const page = await context.newPage();
	await page.goto('/', { waitUntil: 'networkidle' });
	const metrika = await countMetrika(page);
	await context.close();
	if (metrika === 0) throw new Error('Metrika missing');
	return { metrika };
});

await browser.close();

const summary = {
	captured_at: new Date().toISOString(),
	required: 'P18E PRIVACY RUNTIME SURVIVES FINAL LAUNCH AUDIT',
	all_pass: results.every((row) => row.status === 'PASS'),
	results,
};

await fs.writeFile(path.join(OUT_DIR, '18-privacy-regression.json'), JSON.stringify(summary, null, 2) + '\n');
console.log(JSON.stringify(summary, null, 2));
process.exit(summary.all_pass ? 0 : 1);
