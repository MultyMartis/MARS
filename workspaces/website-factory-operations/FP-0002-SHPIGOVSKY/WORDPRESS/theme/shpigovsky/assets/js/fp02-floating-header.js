// FP-0002 V9-06E54 — floating utility header scroll behavior
(function initFp02FloatingHeader() {
	'use strict';

	var root = document.querySelector('[data-fp02-floating-header]');

	if (!root) {
		return;
	}

	var DESKTOP_MIN = 1025;
	var THRESHOLD_DESKTOP = 500;
	var THRESHOLD_MOBILE = 650;
	var SCROLL_DELTA = 10;
	var ticking = false;
	var lastScrollY = window.scrollY || document.documentElement.scrollTop || 0;
	var isVisible = false;
	var frozenByMenu = false;
	var prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

	function getThreshold() {
		return window.innerWidth >= DESKTOP_MIN ? THRESHOLD_DESKTOP : THRESHOLD_MOBILE;
	}

	function isOffcanvasOpen() {
		return document.body.getAttribute('data-offcanvas-state') === 'open';
	}

	function setVisible(visible) {
		if (isVisible === visible) {
			return;
		}

		isVisible = visible;
		root.classList.toggle('is-visible', visible);
		root.setAttribute('aria-hidden', visible ? 'false' : 'true');
	}

	function update() {
		ticking = false;

		if (frozenByMenu || isOffcanvasOpen()) {
			lastScrollY = window.scrollY || document.documentElement.scrollTop || 0;
			return;
		}

		var scrollY = window.scrollY || document.documentElement.scrollTop || 0;
		var threshold = getThreshold();

		if (scrollY <= threshold) {
			setVisible(false);
			lastScrollY = scrollY;
			return;
		}

		var delta = scrollY - lastScrollY;

		if (Math.abs(delta) < SCROLL_DELTA) {
			return;
		}

		if (delta > 0) {
			setVisible(true);
		} else {
			setVisible(false);
		}

		lastScrollY = scrollY;
	}

	function requestUpdate() {
		if (!ticking) {
			ticking = true;
			window.requestAnimationFrame(update);
		}
	}

	function onScroll() {
		requestUpdate();
	}

	function onOffcanvasStateChange() {
		if (isOffcanvasOpen()) {
			frozenByMenu = true;
			return;
		}

		frozenByMenu = false;
		lastScrollY = window.scrollY || document.documentElement.scrollTop || 0;
		requestUpdate();
	}

	window.addEventListener('scroll', onScroll, { passive: true });
	window.addEventListener('resize', requestUpdate, { passive: true });
	window.addEventListener('orientationchange', function () {
		window.setTimeout(requestUpdate, 100);
	});

	if (typeof window.MutationObserver === 'function') {
		var bodyObserver = new window.MutationObserver(function (mutations) {
			Array.prototype.forEach.call(mutations, function (mutation) {
				if (mutation.attributeName === 'data-offcanvas-state') {
					onOffcanvasStateChange();
				}
			});
		});

		bodyObserver.observe(document.body, {
			attributes: true,
			attributeFilter: ['data-offcanvas-state'],
		});
	}

	if (prefersReducedMotion) {
		root.style.transition = 'none';
	}

	update();
})();
