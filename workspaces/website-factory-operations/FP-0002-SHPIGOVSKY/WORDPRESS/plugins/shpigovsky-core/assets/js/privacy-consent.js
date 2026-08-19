(function () {
	'use strict';

	var CFG = window.fp02PrivacyConsent || null;
	if (!CFG || !CFG.cookieName || !CFG.states) {
		return;
	}

	var root = null;
	var notice = null;
	var settingsPanel = null;
	var analyticsToggle = null;
	var customizeButton = null;
	var closeSettingsButton = null;
	var saveButton = null;
	var acceptButton = null;
	var necessaryButton = null;
	var settingsHeading = null;
	var lastFocusedElement = null;
	var metrikaInitStarted = false;
	var metrikaInitialized = false;
	var reloadOnSettingsClose = false;

	function getCookie(name) {
		var escaped = name.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
		var match = document.cookie.match(new RegExp('(?:^|; )' + escaped + '=([^;]*)'));
		return match ? decodeURIComponent(match[1]) : '';
	}

	function setCookie(name, value, options) {
		var parts = [
			name + '=' + encodeURIComponent(value),
			'path=' + (options.path || '/'),
			'max-age=' + String(options.maxAge || 0),
			'SameSite=' + (options.sameSite || 'Lax')
		];

		if (options.secure) {
			parts.push('Secure');
		}

		document.cookie = parts.join('; ');
	}

	function stripValue(value, maxLength) {
		if (typeof value !== 'string') {
			return '';
		}

		return value.slice(0, maxLength);
	}

	function parseRecord(raw) {
		var fallback = {
			state: CFG.states.undecided,
			record: null,
			isValid: false,
			requiresRedecision: false
		};

		if (!raw || typeof raw !== 'string') {
			return fallback;
		}

		var parsed;
		try {
			parsed = JSON.parse(raw);
		} catch (err) {
			return fallback;
		}

		if (!parsed || typeof parsed !== 'object' || Array.isArray(parsed)) {
			return fallback;
		}

		var keys = Object.keys(parsed).sort();
		var allowed = ['analytics', 'decided_at', 'necessary', 'version'];
		if (keys.length !== allowed.length) {
			return fallback;
		}

		for (var i = 0; i < allowed.length; i++) {
			if (keys[i] !== allowed[i]) {
				return fallback;
			}
		}

		if (parsed.necessary !== true || typeof parsed.analytics !== 'boolean') {
			return fallback;
		}

		var version = Number(parsed.version);
		if (!Number.isInteger(version) || version < 1 || version > 50) {
			return fallback;
		}

		var decidedAt = stripValue(parsed.decided_at, 64);
		var timestamp = Date.parse(decidedAt);
		var minTimestamp = Date.parse('2020-01-01T00:00:00Z');
		var maxTimestamp = Date.now() + 86400000;
		if (!Number.isFinite(timestamp) || timestamp < minTimestamp || timestamp > maxTimestamp) {
			return fallback;
		}

		return {
			state: parsed.analytics ? CFG.states.analyticsAllowed : CFG.states.necessaryOnly,
			record: {
				version: version,
				necessary: true,
				analytics: parsed.analytics,
				decided_at: new Date(timestamp).toISOString()
			},
			isValid: true,
			requiresRedecision: version !== Number(CFG.currentVersion)
		};
	}

	function currentConsent() {
		return parseRecord(getCookie(CFG.cookieName));
	}

	function buildRecord(state) {
		if (state === CFG.states.analyticsAllowed) {
			return {
				version: Number(CFG.currentVersion),
				necessary: true,
				analytics: true,
				decided_at: new Date().toISOString()
			};
		}

		if (state === CFG.states.necessaryOnly) {
			return {
				version: Number(CFG.currentVersion),
				necessary: true,
				analytics: false,
				decided_at: new Date().toISOString()
			};
		}

		return null;
	}

	function shouldShowNotice(consent) {
		return !!CFG.systemEnabled && (!consent.isValid || consent.requiresRedecision || consent.state === CFG.states.undecided);
	}

	function analyticsAllowed(consent) {
		return !!CFG.systemEnabled
			&& !!consent.isValid
			&& !consent.requiresRedecision
			&& consent.state === CFG.states.analyticsAllowed;
	}

	function hideRoot() {
		if (!root) {
			return;
		}

		root.hidden = true;
		root.setAttribute('aria-hidden', 'true');
	}

	function showRoot() {
		if (!root) {
			return;
		}

		root.hidden = false;
		root.setAttribute('aria-hidden', 'false');
	}

	function closeSettings(restoreFocus) {
		if (!settingsPanel || !notice) {
			return;
		}

		settingsPanel.hidden = true;
		notice.hidden = false;
		if (customizeButton) {
			customizeButton.setAttribute('aria-expanded', 'false');
		}

		if (restoreFocus && lastFocusedElement && typeof lastFocusedElement.focus === 'function') {
			lastFocusedElement.focus();
		}
	}

	function openSettings() {
		if (!settingsPanel || !notice) {
			return;
		}

		lastFocusedElement = document.activeElement;
		notice.hidden = true;
		settingsPanel.hidden = false;
		if (customizeButton) {
			customizeButton.setAttribute('aria-expanded', 'true');
		}

		if (analyticsToggle) {
			analyticsToggle.focus();
		} else if (settingsHeading) {
			settingsHeading.focus();
		}
	}

	function dispatchLifecycle(name, detail) {
		try {
			document.dispatchEvent(new CustomEvent(name, { detail: detail }));
		} catch (err) {}
	}

	function trimDots(value) {
		return String(value || '').replace(/^\.+/, '');
	}

	function deleteCookieEverywhere(name) {
		var hostname = window.location.hostname || '';
		var hosts = [''];

		if (hostname) {
			hosts.push(hostname);
			hosts.push('.' + trimDots(hostname));

			var parts = hostname.split('.');
			if (parts.length > 2) {
				var parent = parts.slice(parts.length - 2).join('.');
				hosts.push(parent);
				hosts.push('.' + trimDots(parent));
			}
		}

		hosts.forEach(function (host) {
			var cookie = name + '=; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT; SameSite=Lax';
			if (host) {
				cookie += '; domain=' + host;
			}
			if (window.location.protocol === 'https:') {
				cookie += '; Secure';
			}
			document.cookie = cookie;
		});
	}

	function clearAnalyticsStorage() {
		var cookieNames = [
			'_ym_uid',
			'_ym_d',
			'_ym_isad',
			'_ym_retryReqs',
			'_ym_debug',
			'_ym_hostIndex',
			'_ym_visorc'
		];

		try {
			document.cookie.split(';').forEach(function (part) {
				var name = stripValue(part.split('=')[0] || '', 256).trim();
				if (name.indexOf('_ym_') === 0 || cookieNames.indexOf(name) !== -1) {
					deleteCookieEverywhere(name);
				}
			});
		} catch (err) {}

		['localStorage', 'sessionStorage'].forEach(function (storeName) {
			try {
				var store = window[storeName];
				if (!store) {
					return;
				}

				var keysToDelete = [];
				for (var i = 0; i < store.length; i++) {
					var key = store.key(i);
					if (key && key.indexOf('_ym') === 0) {
						keysToDelete.push(key);
					}
				}
				keysToDelete.forEach(function (key) {
					store.removeItem(key);
				});
			} catch (err2) {}
		});
	}

	function loadMetrikaOnce() {
		var counterId = stripValue(String(CFG.metrikaCounterId || ''), 32).replace(/\D+/g, '');
		if (!counterId || metrikaInitialized || metrikaInitStarted) {
			return;
		}

		metrikaInitStarted = true;

		var finishInit = function () {
			if (metrikaInitialized || typeof window.ym !== 'function') {
				return;
			}

			try {
				window.ym(Number(counterId), 'init', {
					clickmap: true,
					trackLinks: true,
					accurateTrackBounce: true,
					webvisor: true,
					referrer: document.referrer,
					url: window.location.href
				});
				metrikaInitialized = true;
			} catch (err) {}
		};

		if (typeof window.ym === 'function') {
			finishInit();
			return;
		}

		if (document.querySelector('script[data-fp02-metrika-script]')) {
			var existing = document.querySelector('script[data-fp02-metrika-script]');
			existing.addEventListener('load', finishInit, { once: true });
			return;
		}

		window.ym = window.ym || function () {
			(window.ym.a = window.ym.a || []).push(arguments);
		};
		window.ym.l = window.ym.l || Date.now();

		var script = document.createElement('script');
		script.async = true;
		script.src = 'https://mc.yandex.ru/metrika/tag.js';
		script.setAttribute('data-fp02-metrika-script', 'true');
		script.addEventListener('load', finishInit, { once: true });
		script.addEventListener('error', function () {
			metrikaInitStarted = false;
		}, { once: true });
		document.head.appendChild(script);
	}

	function applyConsentState(record, options) {
		var previous = currentConsent();
		var encoded = JSON.stringify(record);

		setCookie(CFG.cookieName, encoded, CFG.cookie || {});
		var next = parseRecord(encoded);
		hideRoot();
		closeSettings(false);

		dispatchLifecycle(CFG.events.updated, {
			state: next.state,
			record: next.record,
			requiresRedecision: next.requiresRedecision
		});

		if (next.state === CFG.states.analyticsAllowed) {
			dispatchLifecycle(CFG.events.analyticsGranted, { state: next.state, record: next.record });
			loadMetrikaOnce();
			return;
		}

		clearAnalyticsStorage();
		dispatchLifecycle(CFG.events.analyticsRevoked, { state: next.state, record: next.record });

		if (previous.state === CFG.states.analyticsAllowed && !(options && options.skipReload)) {
			window.location.reload();
		}
	}

	function syncUIFromConsent(consent) {
		if (analyticsToggle) {
			analyticsToggle.checked = consent.state === CFG.states.analyticsAllowed;
		}

		if (analyticsAllowed(consent)) {
			hideRoot();
			loadMetrikaOnce();
			return;
		}

		if (shouldShowNotice(consent)) {
			showRoot();
			closeSettings(false);
			return;
		}

		hideRoot();
	}

	function bindEvents() {
		if (acceptButton) {
			acceptButton.addEventListener('click', function () {
				applyConsentState(buildRecord(CFG.states.analyticsAllowed), { skipReload: true });
			});
		}

		if (necessaryButton) {
			necessaryButton.addEventListener('click', function () {
				applyConsentState(buildRecord(CFG.states.necessaryOnly));
			});
		}

		if (customizeButton) {
			customizeButton.addEventListener('click', function () {
				openSettings();
			});
		}

		if (closeSettingsButton) {
			closeSettingsButton.addEventListener('click', function () {
				closeSettings(true);
			});
		}

		if (saveButton) {
			saveButton.addEventListener('click', function () {
				var state = analyticsToggle && analyticsToggle.checked
					? CFG.states.analyticsAllowed
					: CFG.states.necessaryOnly;
				applyConsentState(buildRecord(state));
			});
		}

		document.addEventListener(CFG.events.openSettings, function () {
			showRoot();
			openSettings();
		});

		document.addEventListener('keydown', function (event) {
			if (event.key === 'Escape' && settingsPanel && !settingsPanel.hidden) {
				closeSettings(true);
			}
		});
	}

	function init() {
		root = document.querySelector('[data-fp02-cookie-consent]');
		if (!root) {
			return;
		}

		notice = root.querySelector('[data-fp02-consent-notice]');
		settingsPanel = root.querySelector('[data-fp02-consent-settings]');
		analyticsToggle = root.querySelector('[data-fp02-consent-analytics]');
		customizeButton = root.querySelector('[data-fp02-consent-customize]');
		closeSettingsButton = root.querySelector('[data-fp02-consent-close-settings]');
		saveButton = root.querySelector('[data-fp02-consent-save]');
		acceptButton = root.querySelector('[data-fp02-consent-accept]');
		necessaryButton = root.querySelector('[data-fp02-consent-necessary]');
		settingsHeading = root.querySelector('#fp02-cookie-consent-settings-title');

		window.FP02PrivacyConsent = {
			openSettings: function () {
				showRoot();
				openSettings();
			},
			getState: function () {
				return currentConsent();
			}
		};

		bindEvents();
		syncUIFromConsent(currentConsent());
	}

	if (document.readyState === 'loading') {
		document.addEventListener('DOMContentLoaded', init);
	} else {
		init();
	}
})();
