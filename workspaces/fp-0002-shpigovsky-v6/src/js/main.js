// FP-0002 v6 — off-canvas mobile menu
(function initOffcanvas() {
	'use strict';

	var DESKTOP_MIN = 1025;
	var offcanvas = document.querySelector('[data-offcanvas]');

	if (!offcanvas) {
		return;
	}

	var panel = offcanvas.querySelector('[data-offcanvas-panel]');
	var overlay = offcanvas.querySelector('[data-offcanvas-overlay]');
	var openTriggers = document.querySelectorAll('[data-offcanvas-open]');
	var closeTriggers = offcanvas.querySelectorAll('[data-offcanvas-close]');
	var lastTrigger = null;
	var isOpen = false;

	function getFocusableElements(root) {
		if (!root) {
			return [];
		}

		return Array.prototype.slice.call(
			root.querySelectorAll(
				'a[href], button:not([disabled]), textarea:not([disabled]), input:not([disabled]), select:not([disabled]), [tabindex]:not([tabindex="-1"])'
			)
		).filter(function (element) {
			return element.offsetParent !== null || element === document.activeElement;
		});
	}

	function syncAria(open) {
		offcanvas.setAttribute('aria-hidden', open ? 'false' : 'true');
		offcanvas.setAttribute('data-offcanvas-state', open ? 'open' : 'closed');

		Array.prototype.forEach.call(openTriggers, function (trigger) {
			trigger.setAttribute('aria-expanded', open ? 'true' : 'false');
		});

		document.body.setAttribute('data-offcanvas-state', open ? 'open' : 'closed');
	}

	function trapFocus(event) {
		if (!isOpen || event.key !== 'Tab' || !panel) {
			return;
		}

		var focusable = getFocusableElements(panel);

		if (!focusable.length) {
			event.preventDefault();
			return;
		}

		var first = focusable[0];
		var last = focusable[focusable.length - 1];
		var active = document.activeElement;

		if (event.shiftKey && active === first) {
			event.preventDefault();
			last.focus();
			return;
		}

		if (!event.shiftKey && active === last) {
			event.preventDefault();
			first.focus();
		}
	}

	function openMenu(trigger) {
		if (isOpen || desktopQuery.matches) {
			return;
		}

		lastTrigger = trigger || lastTrigger;
		isOpen = true;
		syncAria(true);

		var focusTarget = offcanvas.querySelector('[data-offcanvas-close]');
		var focusable = getFocusableElements(panel);

		if (focusTarget) {
			focusTarget.focus();
		} else if (focusable.length) {
			focusable[0].focus();
		}

		document.addEventListener('keydown', onKeydown);
		document.addEventListener('keydown', trapFocus);
	}

	function closeMenu() {
		if (!isOpen) {
			return;
		}

		isOpen = false;
		syncAria(false);

		document.removeEventListener('keydown', onKeydown);
		document.removeEventListener('keydown', trapFocus);

		if (lastTrigger && typeof lastTrigger.focus === 'function') {
			lastTrigger.focus();
		}
	}

	function onKeydown(event) {
		if (event.key === 'Escape') {
			event.preventDefault();
			closeMenu();
		}
	}

	function onViewportChange() {
		if (desktopQuery.matches && isOpen) {
			closeMenu();
		}
	}

	var desktopQuery = window.matchMedia('(min-width: ' + DESKTOP_MIN + 'px)');

	Array.prototype.forEach.call(openTriggers, function (trigger) {
		trigger.addEventListener('click', function (event) {
			event.preventDefault();
			openMenu(trigger);
		});
	});

	Array.prototype.forEach.call(closeTriggers, function (trigger) {
		trigger.addEventListener('click', function (event) {
			event.preventDefault();
			closeMenu();
		});
	});

	if (overlay) {
		overlay.addEventListener('click', function () {
			closeMenu();
		});
	}

	window.addEventListener('resize', function () {
		window.requestAnimationFrame(onViewportChange);
	});

	if (typeof desktopQuery.addEventListener === 'function') {
		desktopQuery.addEventListener('change', onViewportChange);
	} else if (typeof desktopQuery.addListener === 'function') {
		desktopQuery.addListener(onViewportChange);
	}

	if (typeof window.ResizeObserver === 'function') {
		var viewportObserver = new window.ResizeObserver(function () {
			onViewportChange();
		});
		viewportObserver.observe(document.documentElement);
	}

	onViewportChange();
	syncAria(false);
})();

// FP-0002 v6 — home treatment prevention accordion (Section 03)
(function initTreatmentAccordion() {
	'use strict';

	var roots = document.querySelectorAll('[data-accordion]');

	Array.prototype.forEach.call(roots, function (root) {
		var items = root.querySelectorAll('[data-accordion-item]');

		Array.prototype.forEach.call(items, function (item) {
			var button = item.querySelector('[data-accordion-button]');
			var panel = item.querySelector('[data-accordion-panel]');

			if (!button || !panel) {
				return;
			}

			button.addEventListener('click', function () {
				var isOpen = button.getAttribute('aria-expanded') === 'true';

				Array.prototype.forEach.call(items, function (otherItem) {
					var otherButton = otherItem.querySelector('[data-accordion-button]');
					var otherPanel = otherItem.querySelector('[data-accordion-panel]');

					if (!otherButton || !otherPanel) {
						return;
					}

					var shouldOpen = otherItem === item && !isOpen;

					otherButton.setAttribute('aria-expanded', shouldOpen ? 'true' : 'false');
					otherPanel.hidden = !shouldOpen;
				});
			});
		});
	});
})();

// FP-0002 v6 — home gallery swiper
(function initHomeGallery() {
	'use strict';

	function boot() {
		var slider = document.querySelector('[data-gallery-slider]');

		if (!slider || typeof window.Swiper !== 'function') {
			return;
		}

		if (slider.swiper) {
			return;
		}

		new window.Swiper(slider, {
			slidesPerView: 4,
			spaceBetween: 20,
			loop: false,
			autoplay: false,
			navigation: false,
			pagination: false,
			watchOverflow: true,
			grabCursor: true,
			breakpoints: {
				320: {
					slidesPerView: 2.15,
					spaceBetween: 10,
				},
				768: {
					slidesPerView: 3.15,
					spaceBetween: 20,
				},
				1025: {
					slidesPerView: 4,
					spaceBetween: 20,
				},
			},
		});
	}

	if (document.readyState === 'loading') {
		document.addEventListener('DOMContentLoaded', boot);
	} else {
		boot();
	}
})();

// FP-0002 v6 — home reviews swiper
(function initHomeReviews() {
	'use strict';

	function boot() {
		var slider = document.querySelector('[data-reviews-slider]');

		if (!slider || typeof window.Swiper !== 'function') {
			return;
		}

		if (slider.swiper) {
			return;
		}

		var pagination = slider.querySelector('[data-reviews-pagination]');

		new window.Swiper(slider, {
			slidesPerView: 2.2,
			spaceBetween: 20,
			loop: false,
			autoplay: false,
			navigation: false,
			watchOverflow: true,
			grabCursor: true,
			pagination: pagination
				? {
					el: pagination,
					clickable: true,
				}
				: false,
			breakpoints: {
				320: {
					slidesPerView: 1.15,
					spaceBetween: 10,
				},
				768: {
					slidesPerView: 2.15,
					spaceBetween: 20,
				},
				1025: {
					slidesPerView: 2.2,
					spaceBetween: 20,
				},
			},
		});
	}

	if (document.readyState === 'loading') {
		document.addEventListener('DOMContentLoaded', boot);
	} else {
		boot();
	}
})();
