/**
 * FP-0002 V9-06D7-A — global shell JS (packaged from V9 dist main.js).
 * Lead form submission disabled; Swiper/Fancybox/Inputmask vendors not enqueued in D7-A.
 */
(function initRevealAnimations() {
	'use strict';

	var root = document.documentElement;
	var prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
	var revealTargets = document.querySelectorAll('[data-reveal]');

	root.classList.add('js-reveal-ready');

	if (!revealTargets.length) {
		return;
	}

	function revealElement(element, delayMs) {
		if (element.classList.contains('is-revealed')) {
			return;
		}

		var delay = typeof delayMs === 'number' ? delayMs : 0;

		window.setTimeout(function () {
			element.classList.add('is-revealed');
		}, delay);
	}

	function revealAllImmediately() {
		revealTargets.forEach(function (element) {
			revealElement(element, 0);
		});
	}

	if (prefersReducedMotion || typeof window.IntersectionObserver !== 'function') {
		revealAllImmediately();
		return;
	}

	var staggerCapMs = 480;
	var observer = new window.IntersectionObserver(
		function (entries) {
			entries.forEach(function (entry) {
				if (!entry.isIntersecting) {
					return;
				}

				var element = entry.target;
				var group = element.closest('[data-reveal-group]');
				var delayMs = 0;

				if (group) {
					var siblings = group.querySelectorAll(':scope > [data-reveal], :scope > * > [data-reveal], :scope [data-reveal]');
					var index = 0;

					for (var i = 0; i < siblings.length; i += 1) {
						if (siblings[i] === element) {
							index = i;
							break;
						}
					}

					delayMs = Math.min(index * 80, staggerCapMs);
				}

				revealElement(element, delayMs);
				observer.unobserve(element);
			});
		},
		{
			threshold: 0.12,
			rootMargin: '0px 0px -5% 0px',
		}
	);

	revealTargets.forEach(function (element) {
		observer.observe(element);
	});

	window.setTimeout(revealAllImmediately, 8000);
})();

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
	var OFFCANVAS_BODY_LOCK_CLASS = 'is-offcanvas-scroll-locked';
	var offcanvasScrollLockY = 0;

	function getOffcanvasScrollY() {
		return window.scrollY || document.documentElement.scrollTop || 0;
	}

	function focusOffcanvasElement(element, preventScroll) {
		if (!element || typeof element.focus !== 'function') {
			return;
		}

		try {
			if (preventScroll) {
				element.focus({ preventScroll: true });
			} else {
				element.focus();
			}
		} catch (error) {
			element.focus();
		}
	}

	function lockOffcanvasBodyScroll() {
		offcanvasScrollLockY = getOffcanvasScrollY();
		var targetY = offcanvasScrollLockY;

		document.documentElement.classList.add(OFFCANVAS_BODY_LOCK_CLASS);
		document.body.classList.add(OFFCANVAS_BODY_LOCK_CLASS);

		window.requestAnimationFrame(function () {
			if (Math.abs(getOffcanvasScrollY() - targetY) > 1) {
				window.scrollTo(0, targetY);
			}
		});
	}

	function unlockOffcanvasBodyScroll() {
		var scrollY = offcanvasScrollLockY || getOffcanvasScrollY();

		document.documentElement.classList.remove(OFFCANVAS_BODY_LOCK_CLASS);
		document.body.classList.remove(OFFCANVAS_BODY_LOCK_CLASS);
		offcanvasScrollLockY = 0;

		if (scrollY > 0) {
			window.requestAnimationFrame(function () {
				window.scrollTo(0, scrollY);
			});
		}
	}

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
		if (isOpen) {
			return;
		}

		lastTrigger = trigger || lastTrigger;
		lockOffcanvasBodyScroll();
		isOpen = true;
		syncAria(true);

		var focusTarget = offcanvas.querySelector('[data-offcanvas-close]');
		var focusable = getFocusableElements(panel);

		if (focusTarget) {
			focusOffcanvasElement(focusTarget, true);
		} else if (focusable.length) {
			focusOffcanvasElement(focusable[0], true);
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
		unlockOffcanvasBodyScroll();

		document.removeEventListener('keydown', onKeydown);
		document.removeEventListener('keydown', trapFocus);

		// Clear offcanvas Smart Search suggestions on close (shared instances).
		var offcanvasForm = offcanvas.querySelector('[data-smart-search-form]');
		if (offcanvasForm && window.shpigovskySmartSearchInstances) {
			window.shpigovskySmartSearchInstances.forEach(function (instance) {
				if (instance && instance.form === offcanvasForm && typeof instance.clearSuggest === 'function') {
					instance.clearSuggest();
				}
			});
		}

		if (lastTrigger) {
			focusOffcanvasElement(lastTrigger, true);
		}
	}

	function onKeydown(event) {
		if (event.key === 'Escape') {
			event.preventDefault();
			closeMenu();
		}
	}

	function onViewportChange() {
		// Offcanvas may open on desktop via floating-header Menu (V9-06E54).
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
// V9-06E33-FIX01 — shared options also used by /uslugi/ category galleries
// PROD-P08 — attach optional non-Hero mobile prev/next when markup present
(function initHomeGallery() {
	'use strict';

	function fp02TrackpadMousewheel() {
		return {
			enabled: true,
			forceToAxis: true,
			releaseOnEdges: true,
			invert: false,
			sensitivity: 1,
			thresholdDelta: 8,
			thresholdTime: 500
		};
	}

	window.shpigovskyTrackpadMousewheel = fp02TrackpadMousewheel;

	function attachFp02SliderNav(slider, options) {
		if (!slider || !options || typeof options !== 'object') {
			return options;
		}
		if (!options.mousewheel) {
			options.mousewheel = fp02TrackpadMousewheel();
		}
		var prev = slider.querySelector('[data-fp02-slider-prev]');
		var next = slider.querySelector('[data-fp02-slider-next]');
		if (prev && next) {
			options.navigation = {
				prevEl: prev,
				nextEl: next,
				disabledClass: 'swiper-button-disabled',
			};
		}
		return options;
	}

	window.shpigovskyAttachFp02SliderNav = attachFp02SliderNav;

	function gallerySwiperOptions(slider) {
		return attachFp02SliderNav(slider, {
			slidesPerView: 1.15,
			spaceBetween: 10,
			loop: false,
			autoplay: false,
			navigation: false,
			watchOverflow: true,
			grabCursor: true,
			pagination: (function () {
				var pagination = slider.querySelector('[data-gallery-pagination]');
				return pagination
					? {
						el: pagination,
						clickable: true,
					}
					: false;
			})(),
			breakpoints: {
						431: {
							slidesPerView: 2.15,
							spaceBetween: 10,
						},
						768: {
							slidesPerView: 3.15,
							spaceBetween: 20,
						},
						1025: {
							slidesPerView: 3.5,
							spaceBetween: 30,
						},
			},
		});
	}

	// Expose for /uslugi/ category galleries (same settings as Home).
	window.shpigovskyGallerySwiperOptions = gallerySwiperOptions;

	function boot() {
		var slider = document.querySelector('[data-gallery-slider]');

		if (!slider || typeof window.Swiper !== 'function') {
			return;
		}

		if (slider.swiper) {
			return;
		}

		new window.Swiper(slider, gallerySwiperOptions(slider));
	}

	if (document.readyState === 'loading') {
		document.addEventListener('DOMContentLoaded', boot);
	} else {
		boot();
	}
})();

// FP-0002 v8 — reviews swiper (CF-007 neutral)
(function initReviews() {
	'use strict';

	function boot() {
		if (typeof window.Swiper !== 'function') {
			return;
		}

		document.querySelectorAll('[data-reviews-slider]').forEach(function (slider) {
			if (slider.swiper) {
				return;
			}

			var pagination = slider.querySelector('[data-reviews-pagination]');
			var options = {
			slidesPerView: 1.15,
			spaceBetween: 10,
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
						431: {
							slidesPerView: 1.15,
							spaceBetween: 10,
						},
						768: {
							slidesPerView: 2.15,
							spaceBetween: 20,
						},
						1025: {
							slidesPerView: 2.5,
							spaceBetween: 30,
						},
			},
		};

			if (typeof window.shpigovskyAttachFp02SliderNav === 'function') {
				options = window.shpigovskyAttachFp02SliderNav(slider, options);
			}

			new window.Swiper(slider, options);
		});
	}

	if (document.readyState === 'loading') {
		document.addEventListener('DOMContentLoaded', boot);
	} else {
		boot();
	}
})();

// FP-0002 v8 — specialists swiper (CF-005 neutral)
(function initSpecialists() {
	'use strict';

	function boot() {
		if (typeof window.Swiper !== 'function') {
			return;
		}

		document.querySelectorAll('[data-specialists-slider]').forEach(function (slider) {
			if (slider.swiper) {
				return;
			}

			var pagination = slider.querySelector('[data-specialists-pagination]');
			var options = {
			slidesPerView: 1.15,
			spaceBetween: 10,
			loop: false,
			autoplay: false,
			navigation: false,
			pagination: pagination
				? {
					el: pagination,
					clickable: true,
				}
				: false,
			watchOverflow: true,
			grabCursor: true,
			breakpoints: {
						431: {
							slidesPerView: 2.15,
							spaceBetween: 10,
						},
						768: {
							slidesPerView: 3.15,
							spaceBetween: 20,
						},
						1025: {
							slidesPerView: 3.5,
							spaceBetween: 30,
						},
			},
		};

			if (typeof window.shpigovskyAttachFp02SliderNav === 'function') {
				options = window.shpigovskyAttachFp02SliderNav(slider, options);
			}

			new window.Swiper(slider, options);
		});
	}

	if (document.readyState === 'loading') {
		document.addEventListener('DOMContentLoaded', boot);
	} else {
		boot();
	}
})();

// FP-0002 v8 — infrastructure G1–G4 swipers (O-Centre)
(function initInfrastructureSliders() {
	'use strict';

	var INF_GAP = 15;

	function boot() {
		if (typeof window.Swiper !== 'function') {
			return;
		}

		document.querySelectorAll('[data-inf-slider]').forEach(function (slider) {
			if (slider.swiper && !slider.swiper.destroyed) {
				return;
			}

			new window.Swiper(slider, {
				slidesPerView: 1.5,
				spaceBetween: INF_GAP,
				loop: false,
				autoplay: false,
				navigation: false,
				pagination: false,
				watchOverflow: true,
				grabCursor: true,
				mousewheel: typeof window.shpigovskyTrackpadMousewheel === 'function' ? window.shpigovskyTrackpadMousewheel() : { forceToAxis: true, releaseOnEdges: true },
				preventClicks: true,
				preventClicksPropagation: true,
				threshold: 8,
				breakpoints: {
						431: {
							slidesPerView: 1.5,
							spaceBetween: 10,
						},
						768: {
							slidesPerView: 2.5,
							spaceBetween: 20,
						},
						1025: {
							slidesPerView: 3,
							spaceBetween: 30,
						},
				},
			});
		});
	}

	if (document.readyState === 'loading') {
		document.addEventListener('DOMContentLoaded', boot);
	} else {
		boot();
	}
})();

// FP-0002 v8 CF-006 — comfort gallery fancybox
(function initComfortFancybox() {
	'use strict';

	var FP0002_FANCYBOX_ANIMATION = {
		animated: true,
		showClass: 'f-fadeIn',
		hideClass: 'f-fadeOut',
		Carousel: {
			infinite: false,
			transition: 'fade',
		},
		Toolbar: {
			display: {
				left: ['infobar'],
				middle: [],
				right: ['close'],
			},
		},
	};

	var booted = false;

	function boot() {
		var fancybox = window.Fancybox;

		if (typeof fancybox !== 'function' || booted) {
			return;
		}

		booted = true;

		var galleryOptions = FP0002_FANCYBOX_ANIMATION;

		// Comfort galleries (Home /uslugi/ /service stacks): real items only
		// (decor lives outside .comfort__gallery — E59-FIX01).
		fancybox.bind('.comfort__gallery [data-fancybox]', galleryOptions);
		// O-centre infrastructure galleries outside the Comfort stage.
		fancybox.bind('[data-fancybox="o-centre-infrastructure"]', galleryOptions);
		// Specialist certificates / diplomas (PROD-P09): one gallery group per page via data-fancybox.
		fancybox.bind('.specialist-profile__certs-grid [data-fancybox]', galleryOptions);
	}

	if (document.readyState === 'loading') {
		document.addEventListener('DOMContentLoaded', boot);
	} else {
		boot();
	}
})();

// FP-0002 v7 — home videos fancybox (Package #002)
(function initHomeVideosFancybox() {
	'use strict';

	function pauseVideos(container) {
		if (!container) {
			return;
		}

		container.querySelectorAll('video').forEach(function (video) {
			video.pause();
			video.currentTime = 0;
		});
	}

	function boot() {
		var fancybox = window.Fancybox;

		if (typeof fancybox !== 'function') {
			return;
		}

		fancybox.bind('[data-fancybox="home-videos"]', {
			animated: true,
			showClass: 'f-fadeIn',
			hideClass: 'f-fadeOut',
			groupAll: false,
			Html: {
				video: {
					autoplay: true,
					controls: true,
				},
			},
			Carousel: {
				transition: 'fade',
			},
			Toolbar: {
				display: {
					left: ['infobar'],
					middle: [],
					right: ['close'],
				},
			},
			on: {
				destroy: function (fancyboxInstance) {
					pauseVideos(fancyboxInstance.container);
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

// FP-0002 v6 — consultation modal + unified lead forms
// Modal lifecycle behavior adapted from the operator-approved Triumph Manipulator modal runtime.
(function initFp0002ModalAndLeadForms() {
	'use strict';

	var MODAL_ID = 'consultation';
	var MODAL_TRANSITION_MS = 300;
	var BODY_LOCK_CLASS = 'is-modal-scroll-locked';
	var prefersReducedMotionModal = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
	var PHONE_DIGITS_MIN = 10;
	var LEAD_FORM_CONFIG = Object.assign(
		{
			endpoint: '',
			action: 'fp02_lead_submit',
			nonce: '',
			nonceField: 'fp02_lead_nonce',
			siteConfigEndpoint: '',
			recaptchaAction: 'form_lead',
			phoneMask: '+7 (___) ___-__-__',
			backendBlockedMessage:
				'Отправка заявки пока недоступна. Позвоните нам по телефону 8 (925) 183-64-64.',
			validationErrorMessage: 'Проверьте поля формы и попробуйте снова.',
			recaptchaSecurityMessage:
				'Проверка безопасности не пройдена. Обновите страницу и попробуйте снова.',
			successMessage:
				'Заявка принята на локальном стенде. Отправка email здесь отключена — письмо не уходило.',
		},
		typeof window.fp02LeadForm === 'object' && window.fp02LeadForm ? window.fp02LeadForm : {}
	);

	var activeModal = null;
	var lastModalTrigger = null;
	var modalKeydownHandler = null;
	var siteConfigPromise = null;
	var recaptchaScriptPromise = null;
	var bodyScrollLockY = 0;

	function lockBodyScroll() {
		if (!bodyScrollLockY) {
			bodyScrollLockY = window.scrollY || document.documentElement.scrollTop || 0;
		}

		var targetY = bodyScrollLockY;
		document.documentElement.classList.add(BODY_LOCK_CLASS);
		document.body.classList.add(BODY_LOCK_CLASS);

		window.requestAnimationFrame(function () {
			if (Math.abs(window.scrollY - targetY) > 1) {
				window.scrollTo(0, targetY);
			}
		});
	}

	function unlockBodyScroll() {
		var scrollY = bodyScrollLockY || window.scrollY || document.documentElement.scrollTop || 0;
		document.documentElement.classList.remove(BODY_LOCK_CLASS);
		document.body.classList.remove(BODY_LOCK_CLASS);
		bodyScrollLockY = 0;

		if (scrollY > 0) {
			window.requestAnimationFrame(function () {
				window.scrollTo(0, scrollY);
			});
		}
	}

	function focusElement(element, preventScroll) {
		if (!element || typeof element.focus !== 'function') {
			return;
		}

		try {
			if (preventScroll) {
				element.focus({ preventScroll: true });
			} else {
				element.focus();
			}
		} catch (error) {
			element.focus();
		}
	}

	function getFocusableElements(root) {
		if (!root) {
			return [];
		}

		return Array.prototype.slice.call(
			root.querySelectorAll(
				'a[href], button:not([disabled]), input:not([disabled]):not([type="hidden"]), textarea:not([disabled]), select:not([disabled]), [tabindex]:not([tabindex="-1"])'
			)
		).filter(function (element) {
			return !element.hasAttribute('hidden');
		});
	}

	function resolveModal() {
		return document.querySelector('[data-modal="' + MODAL_ID + '"]');
	}

	function closeOffcanvasIfOpen() {
		var offcanvas = document.querySelector('[data-offcanvas][data-offcanvas-state="open"]');
		if (!offcanvas) {
			return;
		}

		var closeButton = offcanvas.querySelector('[data-offcanvas-close]');
		if (closeButton) {
			closeButton.click();
		}
	}

	function applyModalContext(modal, trigger) {
		var titleTarget = modal.querySelector('[data-modal-title-target]');
		var subtitleTarget = modal.querySelector('[data-modal-subtitle-target]');
		var submitTarget = modal.querySelector('[data-modal-submit-target]');
		var defaultTitle = titleTarget ? titleTarget.textContent.trim() : '';
		var title = trigger.getAttribute('data-modal-title') || defaultTitle;
		var subtitle = trigger.getAttribute('data-modal-subtitle') || '';
		var submitText = trigger.getAttribute('data-modal-submit-text') || title;
		var leadSource = trigger.getAttribute('data-modal-source') || '';

		if (titleTarget) {
			titleTarget.textContent = title;
		}

		if (subtitleTarget) {
			if (subtitle) {
				subtitleTarget.textContent = subtitle;
				subtitleTarget.hidden = false;
			} else {
				subtitleTarget.textContent = '';
				subtitleTarget.hidden = true;
			}
		}

		if (submitTarget) {
			submitTarget.textContent = submitText;
		}

		var form = modal.querySelector('[data-lead-form]');
		if (form) {
			setLeadSource(form, leadSource);
		}
	}

	function openModal(modal, trigger) {
		if (!modal || activeModal === modal) {
			return;
		}

		if (activeModal) {
			closeModal(activeModal, { restoreFocus: false });
		}

		lockBodyScroll();
		closeOffcanvasIfOpen();
		lastModalTrigger = trigger || lastModalTrigger;
		applyModalContext(modal, trigger || lastModalTrigger);
		bindPhoneMasksIn(modal);

		modal.removeAttribute('hidden');
		modal.setAttribute('aria-hidden', 'false');
		modal.removeAttribute('data-modal-state');
		activeModal = modal;

		var dialog = modal.querySelector('.modal-consultation__dialog');
		var focusable = getFocusableElements(dialog);
		var preferredFocus = modal.querySelector('[data-modal-focus]');
		var focusTarget = preferredFocus || focusable[0];

		var activateOpenState = function () {
			modal.setAttribute('data-modal-state', 'open');

			if (bodyScrollLockY && Math.abs(window.scrollY - bodyScrollLockY) > 1) {
				window.scrollTo(0, bodyScrollLockY);
			}

			if (focusTarget && typeof focusTarget.focus === 'function') {
				window.requestAnimationFrame(function () {
					focusElement(focusTarget, true);
				});
			}
		};

		if (prefersReducedMotionModal) {
			activateOpenState();
		} else {
			window.requestAnimationFrame(function () {
				window.requestAnimationFrame(activateOpenState);
			});
		}

		if (!modalKeydownHandler) {
			modalKeydownHandler = onModalKeydown;
			document.addEventListener('keydown', modalKeydownHandler);
		}
	}

	function finalizeModalClose(modal) {
		modal.setAttribute('aria-hidden', 'true');
		modal.removeAttribute('data-modal-state');
		modal.setAttribute('hidden', '');

		var form = modal.querySelector('[data-lead-form]');
		if (form) {
			resetLeadFormUi(form);
		}
	}

	function closeModal(modal, options) {
		if (!modal || modal.getAttribute('data-modal-state') !== 'open') {
			return;
		}

		var restoreFocus = !options || options.restoreFocus !== false;
		var triggerToRestore = lastModalTrigger;

		modal.setAttribute('data-modal-state', 'closing');

		if (activeModal === modal) {
			activeModal = null;
			unlockBodyScroll();
		}

		if (restoreFocus && triggerToRestore && typeof triggerToRestore.focus === 'function') {
			focusElement(triggerToRestore, true);
		}

		lastModalTrigger = null;

		if (prefersReducedMotionModal) {
			finalizeModalClose(modal);
			return;
		}

		var done = false;
		var finish = function () {
			if (done) {
				return;
			}

			done = true;
			finalizeModalClose(modal);
		};

		var dialog = modal.querySelector('.modal-consultation__dialog');

		if (dialog) {
			dialog.addEventListener(
				'transitionend',
				function onTransitionEnd(event) {
					if (event.target !== dialog) {
						return;
					}

					if (event.propertyName !== 'opacity' && event.propertyName !== 'transform') {
						return;
					}

					dialog.removeEventListener('transitionend', onTransitionEnd);
					finish();
				}
			);
		}

		window.setTimeout(finish, MODAL_TRANSITION_MS + 80);
	}

	function trapModalFocus(event) {
		if (!activeModal || event.key !== 'Tab') {
			return;
		}

		var dialog = activeModal.querySelector('.modal-consultation__dialog');
		var focusable = getFocusableElements(dialog);

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

	function onModalKeydown(event) {
		if (!activeModal) {
			return;
		}

		if (event.key === 'Escape') {
			event.preventDefault();
			closeModal(activeModal);
			return;
		}

		trapModalFocus(event);
	}

	function bindModalSystem() {
		var modal = resolveModal();
		if (!modal || modal.getAttribute('data-modal-init') === 'true') {
			return;
		}

		modal.setAttribute('data-modal-init', 'true');
		modal.setAttribute('aria-hidden', 'true');

		var overlay = modal.querySelector('.modal-consultation__overlay');
		if (overlay) {
			overlay.addEventListener('click', function (event) {
				if (event.target === overlay) {
					closeModal(modal);
				}
			});
		}

		document.querySelectorAll('[data-modal-close]').forEach(function (trigger) {
			if (trigger.getAttribute('data-modal-close-bound') === 'true') {
				return;
			}

			trigger.setAttribute('data-modal-close-bound', 'true');
			trigger.addEventListener('click', function (event) {
				var modalRoot = trigger.closest('[data-modal]');
				if (!modalRoot) {
					return;
				}

				event.preventDefault();
				closeModal(modalRoot);
			});
		});

		document.querySelectorAll('[data-modal-open="' + MODAL_ID + '"]').forEach(function (trigger) {
			if (trigger.getAttribute('data-modal-open-bound') === 'true') {
				return;
			}

			trigger.setAttribute('data-modal-open-bound', 'true');
			trigger.addEventListener('click', function (event) {
				var targetModal = resolveModal();
				if (!targetModal) {
					return;
				}

				bodyScrollLockY = window.scrollY || document.documentElement.scrollTop || 0;
				event.preventDefault();
				event.stopPropagation();
				openModal(targetModal, trigger);
			});
		});
	}

	function getFieldWrapper(field) {
		return field.closest('[data-lead-field-wrap]');
	}

	function getFieldErrorElement(field) {
		var errorId = field.getAttribute('aria-describedby');
		if (errorId) {
			var byId = document.getElementById(errorId);
			if (byId) {
				return byId;
			}
		}

		var wrapper = getFieldWrapper(field);
		return wrapper ? wrapper.querySelector('[data-lead-field-error]') : null;
	}

	function getFieldMessage(field) {
		if (field.name === 'phone' || field.type === 'tel') {
			return 'Укажите корректный номер телефона';
		}

		if (field.type === 'checkbox' && field.name === 'consent') {
			return 'Подтвердите согласие на обработку данных';
		}

		if (field.name === 'name') {
			return 'Укажите ваше имя';
		}

		if (field.name === 'message') {
			return 'Опишите ситуацию';
		}

		return 'Заполните это поле';
	}

	function getPhoneDigits(value) {
		return String(value || '').replace(/\D/g, '');
	}

	function isPhoneComplete(value) {
		var digits = getPhoneDigits(value);
		return digits.length >= PHONE_DIGITS_MIN;
	}

	function validateLeadField(field) {
		if (
			!(field instanceof HTMLInputElement || field instanceof HTMLTextAreaElement || field instanceof HTMLSelectElement)
		) {
			return true;
		}

		var wrapper = getFieldWrapper(field);
		var isRequired = field.required || field.getAttribute('data-required') === 'true';
		var value = field.value.trim();
		var isValid = true;

		if (field instanceof HTMLInputElement && field.type === 'checkbox') {
			if (isRequired && !field.checked) {
				isValid = false;
			}
		} else if (isRequired && !value) {
			isValid = false;
		}

		if (isValid && (field.name === 'phone' || field.type === 'tel') && (isRequired || value)) {
			isValid = isPhoneComplete(value);
		}

		if (isValid && field.name === 'name' && value.length > 0 && value.length < 2) {
			isValid = false;
		}

		var errorEl = getFieldErrorElement(field);
		if (wrapper) {
			wrapper.classList.toggle('final-form__field--invalid', !isValid && !!wrapper.closest('.final-form'));
			wrapper.classList.toggle('modal-consultation__field--invalid', !isValid && !!wrapper.closest('.modal-consultation'));
		}

		field.setAttribute('aria-invalid', isValid ? 'false' : 'true');

		if (errorEl) {
			errorEl.textContent = isValid ? '' : getFieldMessage(field);
			errorEl.hidden = isValid;
		}

		return isValid;
	}

	function validateLeadForm(form) {
		var fields = form.querySelectorAll('input, textarea, select');
		var isValid = true;

		Array.prototype.forEach.call(fields, function (field) {
			if (
				field instanceof HTMLInputElement &&
				(field.type === 'hidden' || field.closest('[data-lead-form-hidden]'))
			) {
				return;
			}

			if (!validateLeadField(field)) {
				isValid = false;
			}
		});

		return isValid;
	}

	function ensureStatusElement(form) {
		var status = form.querySelector('[data-lead-form-status]');
		if (!status) {
			status = document.createElement('div');
			status.setAttribute('data-lead-form-status', '');
			status.setAttribute('role', 'status');
			status.setAttribute('aria-live', 'polite');
			status.hidden = true;
			form.appendChild(status);
		}

		return status;
	}

	function showLeadFormStatus(form, type, message) {
		var status = ensureStatusElement(form);
		status.hidden = !message;
		status.className = form.classList.contains('final-form__form')
			? 'final-form__status'
			: 'modal-consultation__status';

		if (type) {
			status.classList.add(form.classList.contains('final-form__form')
				? 'final-form__status--' + type
				: 'modal-consultation__status--' + type);
		}

		status.textContent = message;
	}

	function setLeadFormState(form, state) {
		if (!state) {
			form.removeAttribute('data-lead-form-state');
			return;
		}

		form.setAttribute('data-lead-form-state', state);
	}

	function resetLeadFormUi(form) {
		setLeadFormState(form, '');
		showLeadFormStatus(form, '', '');

		form.querySelectorAll('.final-form__field--invalid, .modal-consultation__field--invalid').forEach(function (wrapper) {
			wrapper.classList.remove('final-form__field--invalid', 'modal-consultation__field--invalid');
		});

		form.querySelectorAll('[aria-invalid="true"]').forEach(function (field) {
			field.setAttribute('aria-invalid', 'false');
		});

		form.querySelectorAll('[data-lead-field-error]').forEach(function (errorEl) {
			errorEl.textContent = '';
			errorEl.hidden = true;
		});
	}

	function createRequestToken() {
		if (window.crypto && typeof window.crypto.randomUUID === 'function') {
			return window.crypto.randomUUID().replace(/-/g, '') + String(Date.now());
		}

		return (
			'fp02' +
			String(Date.now()) +
			Math.random().toString(36).slice(2) +
			Math.random().toString(36).slice(2)
		);
	}

	function ensureLeadSecurityFields(form) {
		var container = form.querySelector('[data-lead-form-hidden]');
		if (!container) {
			return;
		}

		var ensure = function (name, attrs) {
			var input = container.querySelector('[data-lead-hidden="' + name + '"]');
			if (input) {
				return input;
			}

			input = document.createElement('input');
			input.type = attrs.type || 'hidden';
			input.name = attrs.name || name;
			input.setAttribute('data-lead-hidden', name);
			if (attrs.value != null) {
				input.value = attrs.value;
			}
			if (attrs.autocomplete) {
				input.setAttribute('autocomplete', attrs.autocomplete);
			}
			if (attrs.tabIndex != null) {
				input.tabIndex = attrs.tabIndex;
			}
			container.appendChild(input);
			return input;
		};

		ensure('action', { name: 'action', value: LEAD_FORM_CONFIG.action || 'fp02_lead_submit' });
		ensure(LEAD_FORM_CONFIG.nonceField || 'fp02_lead_nonce', {
			name: LEAD_FORM_CONFIG.nonceField || 'fp02_lead_nonce',
			value: LEAD_FORM_CONFIG.nonce || '',
		}).setAttribute('data-lead-hidden', LEAD_FORM_CONFIG.nonceField || 'fp02_lead_nonce');
		ensure('form_started_at', {
			name: 'form_started_at',
			value: String(Math.floor(Date.now() / 1000)),
		});
		ensure('timestamp', { name: 'timestamp', value: '' });
		ensure('request_token', { name: 'request_token', value: createRequestToken() });
		ensure('company_url', {
			type: 'text',
			name: 'company_url',
			value: '',
			autocomplete: 'off',
			tabIndex: -1,
		});
	}

	function populateHiddenFields(form) {
		var container = form.querySelector('[data-lead-form-hidden]');
		if (!container) {
			return;
		}

		ensureLeadSecurityFields(form);

		var setValue = function (name, value) {
			var input = container.querySelector('[data-lead-hidden="' + name + '"]');
			if (input) {
				input.value = value;
			}
		};

		setValue('page_url', window.location.href);
		setValue('page_title', document.title || '');

		var context = form.getAttribute('data-form-context') || 'final';
		setValue('form_context', context);

		if (LEAD_FORM_CONFIG.nonce) {
			setValue(LEAD_FORM_CONFIG.nonceField || 'fp02_lead_nonce', LEAD_FORM_CONFIG.nonce);
		}

		if (LEAD_FORM_CONFIG.action) {
			setValue('action', LEAD_FORM_CONFIG.action);
		}

		var started = container.querySelector('[data-lead-hidden="form_started_at"]');
		if (started && !started.value) {
			started.value = String(Math.floor(Date.now() / 1000));
		}

		setValue('timestamp', String(Math.floor(Date.now() / 1000)));
		setValue('request_token', createRequestToken());
	}

	function setLeadSource(form, leadSource) {
		var container = form.querySelector('[data-lead-form-hidden]');
		if (!container) {
			return;
		}

		var input = container.querySelector('[data-lead-hidden="lead_source"]');
		if (input) {
			input.value = leadSource || '';
		}
	}

	/**
	 * Triumph Manipulator v6 proven phone mask (custom vanilla — no Inputmask / jQuery).
	 * Format: +7 (XXX) XXX-XX-XX
	 */
	function bindPhoneMask(input) {
		if (!input || input.getAttribute('data-phone-mask-bound') === 'true') {
			return;
		}

		input.setAttribute('data-phone-mask-bound', 'true');
		input.setAttribute('inputmode', 'tel');
		if (!input.getAttribute('autocomplete')) {
			input.setAttribute('autocomplete', 'tel');
		}

		input.addEventListener('input', function () {
			var digits = String(input.value || '').replace(/\D/g, '');
			var normalized = digits;

			if (normalized.indexOf('8') === 0) {
				normalized = '7' + normalized.slice(1);
			}

			if (normalized.length > 0 && normalized.indexOf('7') !== 0) {
				normalized = '7' + normalized;
			}

			normalized = normalized.slice(0, 11);

			if (!normalized) {
				input.value = '';
				return;
			}

			var local = normalized.slice(1);
			var formatted = '+7';

			if (local.length > 0) {
				formatted += ' (' + local.slice(0, 3);
			}
			if (local.length >= 3) {
				formatted += ') ' + local.slice(3, 6);
			}
			if (local.length >= 6) {
				formatted += '-' + local.slice(6, 8);
			}
			if (local.length >= 8) {
				formatted += '-' + local.slice(8, 10);
			}

			input.value = formatted;
		});
	}

	function collectPhoneInputs(root) {
		var scope = root || document;
		var nodes = scope.querySelectorAll(
			'input[type="tel"], input[name="phone"], input[data-phone-input], input[data-phone-mask]'
		);
		return Array.prototype.slice.call(nodes);
	}

	function bindPhoneMasksIn(root) {
		collectPhoneInputs(root).forEach(bindPhoneMask);
	}

	function collectPayload(form) {
		var formData = new FormData(form);
		var payload = {};

		formData.forEach(function (value, key) {
			if (typeof value === 'string') {
				payload[key] = value;
			}
		});

		return payload;
	}

	function loadSiteConfig() {
		if (!LEAD_FORM_CONFIG.siteConfigEndpoint) {
			return Promise.resolve({ recaptchaSiteKey: '' });
		}

		if (!siteConfigPromise) {
			siteConfigPromise = fetch(LEAD_FORM_CONFIG.siteConfigEndpoint, {
				method: 'GET',
				headers: { Accept: 'application/json' },
				credentials: 'same-origin',
			})
				.then(function (response) {
					if (!response.ok) {
						return { recaptchaSiteKey: '' };
					}

					return response.json().catch(function () {
						return { recaptchaSiteKey: '' };
					});
				})
				.then(function (data) {
					if (!data || typeof data !== 'object') {
						return { recaptchaSiteKey: '' };
					}

					return {
						recaptchaSiteKey:
							typeof data.recaptchaSiteKey === 'string' ? data.recaptchaSiteKey.trim() : '',
					};
				})
				.catch(function () {
					return { recaptchaSiteKey: '' };
				});
		}

		return siteConfigPromise;
	}

	function waitForGrecaptchaReadyApi() {
		if (typeof window.grecaptcha !== 'undefined' && typeof window.grecaptcha.ready === 'function') {
			return new Promise(function (resolve) {
				window.grecaptcha.ready(resolve);
			});
		}

		return Promise.reject(new Error('recaptcha_not_ready'));
	}

	function loadRecaptchaScript(siteKey) {
		if (!siteKey) {
			return Promise.resolve();
		}

		if (typeof window.grecaptcha !== 'undefined' && typeof window.grecaptcha.ready === 'function') {
			return Promise.resolve();
		}

		if (recaptchaScriptPromise) {
			return recaptchaScriptPromise;
		}

		recaptchaScriptPromise = new Promise(function (resolve, reject) {
			var script = document.createElement('script');
			script.src = 'https://www.google.com/recaptcha/api.js?render=' + encodeURIComponent(siteKey);
			script.async = true;
			script.defer = true;
			script.setAttribute('data-recaptcha-loader', 'true');
			script.onload = function () {
				waitForGrecaptchaReadyApi().then(resolve).catch(reject);
			};
			script.onerror = function () {
				reject(new Error('recaptcha_script_failed'));
			};
			document.head.appendChild(script);
		}).catch(function (error) {
			recaptchaScriptPromise = null;
			throw error;
		});

		return recaptchaScriptPromise;
	}

	function appendRecaptchaToken(form, formData) {
		return loadSiteConfig().then(function (config) {
			var siteKey = config.recaptchaSiteKey;
			if (!siteKey || siteKey === 'PASTE_SITE_KEY_HERE') {
				return;
			}

			return loadRecaptchaScript(siteKey)
				.then(function () {
					return waitForGrecaptchaReadyApi();
				})
				.then(function () {
					if (typeof window.grecaptcha.execute !== 'function') {
						throw new Error('recaptcha_execute_missing');
					}

					return window.grecaptcha.execute(siteKey, { action: LEAD_FORM_CONFIG.recaptchaAction });
				})
				.then(function (token) {
					if (!token) {
						throw new Error('recaptcha_token_empty');
					}

					formData.set('g-recaptcha-response', token);
					var hidden = form.querySelector('[data-lead-hidden="g-recaptcha-response"]');
					if (hidden) {
						hidden.value = token;
					}
				});
		});
	}

	function submitLeadForm(form, payload) {
		if (!LEAD_FORM_CONFIG.endpoint) {
			return Promise.reject({
				userMessage: LEAD_FORM_CONFIG.backendBlockedMessage,
				code: 'backend_blocked',
			});
		}

		var formData = new FormData();
		Object.keys(payload).forEach(function (key) {
			formData.append(key, payload[key]);
		});

		if (LEAD_FORM_CONFIG.action && !formData.get('action')) {
			formData.append('action', LEAD_FORM_CONFIG.action);
		}

		if (LEAD_FORM_CONFIG.nonce) {
			var nonceField = LEAD_FORM_CONFIG.nonceField || 'fp02_lead_nonce';
			if (!formData.get(nonceField)) {
				formData.append(nonceField, LEAD_FORM_CONFIG.nonce);
			}
		}

		return appendRecaptchaToken(form, formData)
			.then(function () {
				return fetch(LEAD_FORM_CONFIG.endpoint, {
					method: 'POST',
					body: formData,
					headers: { Accept: 'application/json' },
					credentials: 'same-origin',
				});
			})
			.then(function (response) {
				return response
					.json()
					.catch(function () {
						return null;
					})
					.then(function (data) {
						if (!response.ok) {
							var error = new Error('form_submit_failed');
							error.userMessage =
								(data && typeof data.message === 'string' && data.message) ||
								'Не удалось отправить заявку. Позвоните нам или попробуйте ещё раз.';
							throw error;
						}

						if (data && (data.ok === false || data.success === false)) {
							var fail = new Error('form_submit_failed');
							fail.userMessage =
								(typeof data.message === 'string' && data.message) ||
								'Не удалось отправить заявку. Позвоните нам или попробуйте ещё раз.';
							throw fail;
						}

						return { ok: true, data: data };
					});
			});
	}

	function initLeadForm(form) {
		if (!form || form.getAttribute('data-lead-form-init') === 'true') {
			return;
		}

		form.setAttribute('data-lead-form-init', 'true');
		populateHiddenFields(form);

		bindPhoneMasksIn(form);

		form.querySelectorAll('input, textarea, select').forEach(function (field) {
			if (
				field instanceof HTMLInputElement &&
				(field.type === 'hidden' || field.closest('[data-lead-form-hidden]'))
			) {
				return;
			}

			var revalidate = function () {
				var wrapper = getFieldWrapper(field);
				if (
					wrapper &&
					(wrapper.classList.contains('final-form__field--invalid') ||
						wrapper.classList.contains('modal-consultation__field--invalid'))
				) {
					validateLeadField(field);
				}
			};

			field.addEventListener('blur', function () {
				if (field instanceof HTMLInputElement && field.type === 'checkbox') {
					if (!field.checked) {
						return;
					}
				} else if (!field.value.trim()) {
					return;
				}

				validateLeadField(field);
			});

			if (field instanceof HTMLInputElement && field.type === 'checkbox') {
				field.addEventListener('change', revalidate);
			} else {
				field.addEventListener('input', revalidate);
			}
		});

		form.querySelectorAll('.final-form__consent-link, .modal-consultation__consent-link').forEach(function (link) {
			link.addEventListener('click', function (event) {
				event.stopPropagation();
			});
		});

		var submitButton = form.querySelector('[type="submit"]');
		var submitLock = false;

		form.addEventListener('submit', function (event) {
			event.preventDefault();

			if (submitLock || form.getAttribute('data-lead-form-state') === 'loading') {
				return;
			}

			populateHiddenFields(form);

			if (!validateLeadForm(form)) {
				setLeadFormState(form, 'error');
				showLeadFormStatus(form, 'error', LEAD_FORM_CONFIG.validationErrorMessage);
				var firstInvalid = form.querySelector('[aria-invalid="true"]');
				if (firstInvalid && typeof firstInvalid.focus === 'function') {
					firstInvalid.focus();
				}
				return;
			}

			submitLock = true;
			setLeadFormState(form, 'loading');
			showLeadFormStatus(form, 'loading', 'Отправляем заявку…');

			if (submitButton) {
				submitButton.disabled = true;
			}

			var payload = collectPayload(form);

			submitLeadForm(form, payload)
				.then(function (result) {
					var successMessage =
						(result.data && typeof result.data.message === 'string' && result.data.message) ||
						LEAD_FORM_CONFIG.successMessage ||
						'Заявка принята на локальном стенде. Отправка email здесь отключена — письмо не уходило.';
					setLeadFormState(form, 'success');
					showLeadFormStatus(form, 'success', successMessage);
					form.reset();
					ensureLeadSecurityFields(form);
					populateHiddenFields(form);
				})
				.catch(function (error) {
					setLeadFormState(form, 'error');
					showLeadFormStatus(
						form,
						'error',
						(error && error.userMessage) ||
							LEAD_FORM_CONFIG.backendBlockedMessage ||
							'Не удалось отправить заявку. Позвоните нам или попробуйте ещё раз.'
					);
				})
				.finally(function () {
					submitLock = false;
					if (submitButton && form.getAttribute('data-lead-form-state') !== 'success') {
						submitButton.disabled = false;
					}
				});
		});
	}

	function boot() {
		bindModalSystem();
		document.querySelectorAll('[data-lead-form]').forEach(function (form) {
			initLeadForm(form);
		});
		// Cover any tel fields outside lead-form markers (defensive; idempotent).
		bindPhoneMasksIn(document);
	}

	if (document.readyState === 'loading') {
		document.addEventListener('DOMContentLoaded', boot);
	} else {
		boot();
	}
})();

// FP-0002 V9-03G — shared scroll-to-top viewport control
(function initScrollToTop() {
	'use strict';

	var SCROLL_THRESHOLD = 500;
	var button = document.querySelector('[data-scroll-to-top]');

	if (!button) {
		return;
	}

	var reducedMotionMq = window.matchMedia('(prefers-reduced-motion: reduce)');
	var scrollTicking = false;

	function prefersReducedMotion() {
		return reducedMotionMq.matches;
	}

	function getScrollY() {
		return window.scrollY || document.documentElement.scrollTop || 0;
	}

	function setVisible(visible) {
		button.classList.toggle('scroll-to-top--visible', visible);
		button.setAttribute('aria-hidden', visible ? 'false' : 'true');

		if (!visible && document.activeElement === button) {
			button.blur();
		}
	}

	function updateVisibility() {
		scrollTicking = false;
		setVisible(getScrollY() > SCROLL_THRESHOLD);
	}

	function onScrollOrResize() {
		if (!scrollTicking) {
			scrollTicking = true;
			window.requestAnimationFrame(updateVisibility);
		}
	}

	button.addEventListener('click', function () {
		window.scrollTo({
			top: 0,
			behavior: prefersReducedMotion() ? 'auto' : 'smooth',
		});
	});

	window.addEventListener('scroll', onScrollOrResize, { passive: true });
	window.addEventListener('resize', onScrollOrResize, { passive: true });
	window.addEventListener('pageshow', updateVisibility);

	updateVisibility();
})();

// FP-0002 V9-06E33-FIX01 — /uslugi/ category galleries: same Swiper settings as Home gallery (dots, no arrows)
(function initServicesCategoryGalleries() {
	'use strict';

	function boot() {
		if (typeof window.Swiper !== 'function') {
			return;
		}

		var optionsFactory =
			typeof window.shpigovskyGallerySwiperOptions === 'function'
				? window.shpigovskyGallerySwiperOptions
				: null;

		document.querySelectorAll('[data-services-category-gallery]').forEach(function (slider) {
			if (slider.swiper) {
				return;
			}

			var options = optionsFactory
				? optionsFactory(slider)
				: {
					slidesPerView: 4,
					spaceBetween: 30,
					loop: false,
					autoplay: false,
					navigation: false,
					watchOverflow: true,
					grabCursor: true,
					pagination: (function () {
						var pagination = slider.querySelector('[data-gallery-pagination]');
						return pagination
							? {
								el: pagination,
								clickable: true,
							}
							: false;
					})(),
					breakpoints: {
						431: {
							slidesPerView: 2.15,
							spaceBetween: 10,
						},
						768: {
							slidesPerView: 3.15,
							spaceBetween: 20,
						},
						1025: {
							slidesPerView: 3.5,
							spaceBetween: 30,
						},
					},
				};

			if (!optionsFactory && typeof window.shpigovskyAttachFp02SliderNav === 'function') {
				options = window.shpigovskyAttachFp02SliderNav(slider, options);
			}

			new window.Swiper(slider, options);
		});
	}

	if (document.readyState === 'loading') {
		document.addEventListener('DOMContentLoaded', boot);
	} else {
		boot();
	}
})();

// FP-0002 V9-06E35 — home articles swiper (same options as Home gallery /uslugi/; dots, no arrows)
(function initHomeArticlesSlider() {
	'use strict';

	function boot() {
		if (typeof window.Swiper !== 'function') {
			return;
		}

		var optionsFactory =
			typeof window.shpigovskyGallerySwiperOptions === 'function'
				? window.shpigovskyGallerySwiperOptions
				: null;

		document.querySelectorAll('[data-articles-slider]').forEach(function (slider) {
			if (slider.swiper) {
				return;
			}

			var options = optionsFactory
				? optionsFactory(slider)
				: {
					slidesPerView: 1.15,
					spaceBetween: 10,
					loop: false,
					autoplay: false,
					navigation: false,
					watchOverflow: true,
					grabCursor: true,
					pagination: false,
					breakpoints: {
						431: {
							slidesPerView: 2.15,
							spaceBetween: 10,
						},
						768: {
							slidesPerView: 3.15,
							spaceBetween: 20,
						},
						1025: {
							slidesPerView: 3.5,
							spaceBetween: 30,
						},
					},
				};

			var articlesPagination = slider.querySelector('[data-articles-pagination]');
			if (articlesPagination) {
				options.pagination = {
					el: articlesPagination,
					clickable: true,
				};
			}

			if (!optionsFactory && typeof window.shpigovskyAttachFp02SliderNav === 'function') {
				options = window.shpigovskyAttachFp02SliderNav(slider, options);
			}

			new window.Swiper(slider, options);
		});
	}

	if (document.readyState === 'loading') {
		document.addEventListener('DOMContentLoaded', boot);
	} else {
		boot();
	}
})();

// FP-0002 V9-06E41 — Home hero slider (Swiper, horizontal)
(function initHomeHeroSlider() {
	'use strict';

	function boot() {
		var slider = document.querySelector('[data-hero-slider]');

		if (!slider || typeof window.Swiper !== 'function') {
			return;
		}

		if (slider.swiper) {
			return;
		}

		var slides = slider.querySelectorAll('.swiper-slide');
		if (!slides || slides.length < 2) {
			return;
		}

		var autoplayOn = slider.getAttribute('data-hero-autoplay') === '1';
		var arrowsOn = slider.getAttribute('data-hero-arrows') === '1';
		var dotsOn = slider.getAttribute('data-hero-dots') === '1';
		var delay = parseInt(slider.getAttribute('data-hero-delay') || '5000', 10);
		if (!delay || delay < 1000) {
			delay = 5000;
		}

		var paginationEl = slider.querySelector('[data-hero-pagination]');
		var prevEl = slider.querySelector('[data-hero-prev]');
		var nextEl = slider.querySelector('[data-hero-next]');

		var options = {
			slidesPerView: 1,
			spaceBetween: 0,
			loop: false,
			speed: 600,
			autoHeight: false,
			watchOverflow: true,
			grabCursor: true,
			effect: 'slide',
			direction: 'horizontal',
			autoplay: autoplayOn
				? {
					delay: delay,
					disableOnInteraction: false,
					pauseOnMouseEnter: true,
				}
				: false,
			pagination:
				dotsOn && paginationEl
					? {
						el: paginationEl,
						clickable: true,
					}
					: false,
			navigation:
				arrowsOn && prevEl && nextEl
					? {
						prevEl: prevEl,
						nextEl: nextEl,
					}
					: false,
		};

		new window.Swiper(slider, options);
	}

	if (document.readyState === 'loading') {
		document.addEventListener('DOMContentLoaded', boot);
	} else {
		boot();
	}
})();

// FP-0002 V9-06E43 — Services hub hero slider (services-inner-hero-v2, horizontal)
(function initServicesHeroSlider() {
	'use strict';

	function boot() {
		var slider = document.querySelector('[data-services-hero-slider]');

		if (!slider || typeof window.Swiper !== 'function') {
			return;
		}

		if (slider.swiper) {
			return;
		}

		var slides = slider.querySelectorAll('.swiper-slide');
		if (!slides || slides.length < 2) {
			return;
		}

		var autoplayOn = slider.getAttribute('data-services-hero-autoplay') === '1';
		var arrowsOn = slider.getAttribute('data-services-hero-arrows') === '1';
		var dotsOn = slider.getAttribute('data-services-hero-dots') === '1';
		var delay = parseInt(slider.getAttribute('data-services-hero-delay') || '5000', 10);
		if (!delay || delay < 1000) {
			delay = 5000;
		}

		var paginationEl = slider.querySelector('[data-services-hero-pagination]');
		var prevEl = slider.querySelector('[data-services-hero-prev]');
		var nextEl = slider.querySelector('[data-services-hero-next]');

		var options = {
			slidesPerView: 1,
			spaceBetween: 0,
			loop: false,
			speed: 600,
			autoHeight: false,
			watchOverflow: true,
			grabCursor: true,
			effect: 'slide',
			direction: 'horizontal',
			autoplay: autoplayOn
				? {
					delay: delay,
					disableOnInteraction: false,
					pauseOnMouseEnter: true,
				}
				: false,
			pagination:
				dotsOn && paginationEl
					? {
						el: paginationEl,
						clickable: true,
					}
					: false,
			navigation:
				arrowsOn && prevEl && nextEl
					? {
						prevEl: prevEl,
						nextEl: nextEl,
					}
					: false,
		};

		new window.Swiper(slider, options);
	}

	if (document.readyState === 'loading') {
		document.addEventListener('DOMContentLoaded', boot);
	} else {
		boot();
	}
})();

// FP-0002 V9-06E61 — reviews archive read-more toggle
(function initReviewArchiveReadMore() {
	'use strict';

	var LINE_COUNT = 6;
	var LABEL_MORE = 'Читать весь отзыв';
	var LABEL_HIDE = 'Свернуть';

	function lineHeight(element) {
		var styles = window.getComputedStyle(element);
		var value = parseFloat(styles.lineHeight);

		if (!value || Number.isNaN(value)) {
			value = (parseFloat(styles.fontSize) || 16) * 1.5;
		}

		return value;
	}

	function syncCard(card) {
		var body = card.querySelector('[data-review-body]');
		var button = card.querySelector('[data-review-toggle]');

		if (!body || !button) {
			return;
		}

		var clampHeight = lineHeight(body) * LINE_COUNT;
		var fullHeight = body.scrollHeight;
		var needsClamp = fullHeight > clampHeight + 2;

		if (!needsClamp) {
			body.classList.remove('is-clamped', 'is-expanded');
			body.style.removeProperty('--review-body-clamp-height');
			button.hidden = true;
			button.setAttribute('aria-expanded', 'false');
			button.textContent = LABEL_MORE;
			return;
		}

		body.style.setProperty('--review-body-clamp-height', clampHeight + 'px');
		button.hidden = false;

		if (!body.classList.contains('is-expanded')) {
			body.classList.add('is-clamped');
		}

		if (button._reviewReadMoreBound) {
			return;
		}

		button._reviewReadMoreBound = true;
		button.addEventListener('click', function () {
			var expanded = body.classList.toggle('is-expanded');
			body.classList.toggle('is-clamped', !expanded);
			button.setAttribute('aria-expanded', expanded ? 'true' : 'false');
			button.textContent = expanded ? LABEL_HIDE : LABEL_MORE;
		});
	}

	function syncAll() {
		document.querySelectorAll('[data-review-read-more]').forEach(syncCard);
	}

	function boot() {
		syncAll();
		window.addEventListener('load', syncAll);
		window.addEventListener('resize', syncAll);
	}

	if (document.readyState === 'loading') {
		document.addEventListener('DOMContentLoaded', boot);
	} else {
		boot();
	}
})();

// FP-0002 V9-06E47-FIX04 — service signs editorial 5-line clamp / read-more toggle
(function initServiceSignsReadMore() {
	'use strict';

	var LINE_COUNT = 5;
	var TOLERANCE_PX = 2;
	var RESIZE_DEBOUNCE_MS = 150;
	var LABEL_MORE = 'Читать больше';
	var LABEL_HIDE = 'Скрыть';
	var prefersReducedMotion =
		typeof window.matchMedia === 'function' &&
		window.matchMedia('(prefers-reduced-motion: reduce)').matches;

	function getLineHeight(element) {
		var styles = window.getComputedStyle(element);
		var lineHeight = parseFloat(styles.lineHeight);

		if (!lineHeight || Number.isNaN(lineHeight)) {
			var fontSize = parseFloat(styles.fontSize) || 16;
			lineHeight = fontSize * 1.5;
		}

		return lineHeight;
	}

	function setButtonLabel(button, expanded) {
		button.setAttribute('aria-expanded', expanded ? 'true' : 'false');
		button.textContent = expanded ? LABEL_HIDE : LABEL_MORE;
	}

	function clearTransitionTimer(editorial) {
		if (editorial._signsTransitionTimer) {
			window.clearTimeout(editorial._signsTransitionTimer);
			editorial._signsTransitionTimer = null;
		}

		if (editorial._signsTransitionEndHandler) {
			editorial.removeEventListener('transitionend', editorial._signsTransitionEndHandler);
			editorial._signsTransitionEndHandler = null;
		}
	}

	function afterMaxHeightTransition(editorial, done) {
		clearTransitionTimer(editorial);

		function finish() {
			clearTransitionTimer(editorial);
			editorial.classList.remove('is-animated');
			done();
		}

		function onTransitionEnd(event) {
			if (event.target !== editorial || event.propertyName !== 'max-height') {
				return;
			}

			finish();
		}

		if (prefersReducedMotion) {
			finish();
			return;
		}

		editorial._signsTransitionEndHandler = onTransitionEnd;
		editorial.addEventListener('transitionend', onTransitionEnd);
		editorial._signsTransitionTimer = window.setTimeout(finish, 500);
	}

	function measureNaturalHeight(editorial) {
		var prevClamp = editorial.classList.contains('is-clamped');
		var prevExpanded = editorial.classList.contains('is-expanded');
		var prevAnimated = editorial.classList.contains('is-animated');
		var prevClampVar = editorial.style.getPropertyValue('--signs-editorial-clamp-height');
		var prevFullVar = editorial.style.getPropertyValue('--signs-editorial-full-height');

		editorial.classList.remove('is-clamped', 'is-expanded', 'is-animated');
		editorial.style.removeProperty('--signs-editorial-clamp-height');
		editorial.style.removeProperty('--signs-editorial-full-height');
		editorial.style.maxHeight = 'none';

		var height = editorial.scrollHeight;

		editorial.style.maxHeight = '';

		if (prevClampVar) {
			editorial.style.setProperty('--signs-editorial-clamp-height', prevClampVar);
		}

		if (prevFullVar) {
			editorial.style.setProperty('--signs-editorial-full-height', prevFullVar);
		}

		editorial.classList.toggle('is-clamped', prevClamp);
		editorial.classList.toggle('is-expanded', prevExpanded);
		editorial.classList.toggle('is-animated', prevAnimated);

		return height;
	}

	function expandEditorial(editorial, button, state) {
		if (state.expanded || state.animating) {
			return;
		}

		state.animating = true;
		clearTransitionTimer(editorial);

		var clampHeight = getLineHeight(editorial) * LINE_COUNT;
		var fullHeight = measureNaturalHeight(editorial);

		editorial.style.setProperty('--signs-editorial-clamp-height', clampHeight + 'px');
		editorial.style.setProperty('--signs-editorial-full-height', fullHeight + 'px');
		editorial.classList.add('is-clamped');
		editorial.classList.remove('is-expanded');

		// Force layout at clamp height before expanding.
		void editorial.offsetHeight;

		editorial.classList.add('is-animated');
		editorial.classList.remove('is-clamped');
		editorial.classList.add('is-expanded');
		state.expanded = true;
		setButtonLabel(button, true);
		button.hidden = false;

		afterMaxHeightTransition(editorial, function () {
			state.animating = false;
			editorial.style.setProperty(
				'--signs-editorial-full-height',
				measureNaturalHeight(editorial) + 'px'
			);
		});
	}

	function collapseEditorial(editorial, button, state) {
		if (!state.expanded || state.animating) {
			return;
		}

		state.animating = true;
		clearTransitionTimer(editorial);

		var clampHeight = getLineHeight(editorial) * LINE_COUNT;
		var fullHeight = measureNaturalHeight(editorial);

		editorial.style.setProperty('--signs-editorial-clamp-height', clampHeight + 'px');
		editorial.style.setProperty('--signs-editorial-full-height', fullHeight + 'px');
		editorial.classList.add('is-expanded');
		editorial.classList.remove('is-clamped');

		// Force layout at full height before collapsing.
		void editorial.offsetHeight;

		editorial.classList.add('is-animated');
		editorial.classList.remove('is-expanded');
		editorial.classList.add('is-clamped');
		state.expanded = false;
		setButtonLabel(button, false);
		button.hidden = false;

		afterMaxHeightTransition(editorial, function () {
			state.animating = false;
		});
	}

	function applyOverflowState(editorial, button, state, needsClamp, clampHeight, fullHeight) {
		if (!needsClamp) {
			clearTransitionTimer(editorial);
			state.expanded = false;
			state.animating = false;
			editorial.classList.remove('is-clamped', 'is-expanded', 'is-animated');
			editorial.style.removeProperty('--signs-editorial-clamp-height');
			editorial.style.removeProperty('--signs-editorial-full-height');
			editorial.style.maxHeight = '';
			button.hidden = true;
			setButtonLabel(button, false);
			return;
		}

		editorial.style.setProperty('--signs-editorial-clamp-height', clampHeight + 'px');
		editorial.style.setProperty('--signs-editorial-full-height', fullHeight + 'px');
		button.hidden = false;

		if (state.expanded) {
			editorial.classList.remove('is-clamped', 'is-animated');
			editorial.classList.add('is-expanded');
			setButtonLabel(button, true);
			return;
		}

		editorial.classList.remove('is-expanded', 'is-animated');
		editorial.classList.add('is-clamped');
		setButtonLabel(button, false);
	}

	function syncBlock(root) {
		var editorial = root.querySelector('.service-leaf-signs-v1__editorial');
		var button = root.querySelector('.service-leaf-signs-v1__read-more');

		if (!editorial || !button) {
			return;
		}

		if (!button._signsReadMoreState) {
			button._signsReadMoreState = {
				expanded: false,
				animating: false
			};
		}

		var state = button._signsReadMoreState;

		if (state.animating) {
			return;
		}

		var clampHeight = getLineHeight(editorial) * LINE_COUNT;
		var fullHeight = measureNaturalHeight(editorial);
		var needsClamp = fullHeight > clampHeight + TOLERANCE_PX;

		applyOverflowState(editorial, button, state, needsClamp, clampHeight, fullHeight);

		if (!button._signsReadMoreBound) {
			button._signsReadMoreBound = true;
			button.addEventListener('click', function (event) {
				event.preventDefault();

				if (state.animating) {
					return;
				}

				if (state.expanded) {
					collapseEditorial(editorial, button, state);
				} else {
					expandEditorial(editorial, button, state);
				}
			});
		}
	}

	function syncAll() {
		var roots = document.querySelectorAll('.service-leaf-signs-v1');

		Array.prototype.forEach.call(roots, function (root) {
			syncBlock(root);
		});
	}

	function boot() {
		function runSync() {
			window.requestAnimationFrame(function () {
				window.requestAnimationFrame(syncAll);
			});
		}

		runSync();

		if (document.fonts && document.fonts.ready && typeof document.fonts.ready.then === 'function') {
			document.fonts.ready.then(function () {
				runSync();
			}).catch(function () {
				/* ignore font readiness failures */
			});
		}

		window.addEventListener('load', runSync);

		var resizeTimer = null;
		window.addEventListener('resize', function () {
			if (resizeTimer) {
				window.clearTimeout(resizeTimer);
			}

			resizeTimer = window.setTimeout(function () {
				runSync();
			}, RESIZE_DEBOUNCE_MS);
		});
	}

	if (document.readyState === 'loading') {
		document.addEventListener('DOMContentLoaded', boot);
	} else {
		boot();
	}
})();

// FP-0002 V9-06E62B — review slider five-line overflow → archive link (no in-place expand)
(function initReviewSliderFullLinks() {
	'use strict';

	var LINE_COUNT = 5;
	var TOLERANCE_PX = 2;
	var RESIZE_DEBOUNCE_MS = 150;
	var ATTR_BOUND = 'data-review-slider-full-bound';

	function lineHeight(element) {
		var styles = window.getComputedStyle(element);
		var value = parseFloat(styles.lineHeight);

		if (!value || Number.isNaN(value)) {
			value = (parseFloat(styles.fontSize) || 16) * 1.5;
		}

		return value;
	}

	function syncCard(card) {
		var text = card.querySelector('[data-review-slider-text]');
		var footer = card.querySelector('[data-review-slider-read-more]');

		if (!text || !footer) {
			return;
		}

		text.classList.remove('is-clamped');
		footer.hidden = true;

		var clampHeight = lineHeight(text) * LINE_COUNT;
		var needsLink = text.scrollHeight > clampHeight + TOLERANCE_PX;

		if (!needsLink) {
			return;
		}

		text.classList.add('is-clamped');
		footer.hidden = false;
	}

	function syncAll() {
		document.querySelectorAll('[data-reviews-slider] [data-review-slider-card]').forEach(syncCard);
	}

	function boot() {
		if (document.documentElement.getAttribute(ATTR_BOUND) === '1') {
			return;
		}

		document.documentElement.setAttribute(ATTR_BOUND, '1');
		syncAll();
		window.addEventListener('load', syncAll);

		var resizeTimer = null;
		window.addEventListener('resize', function () {
			if (resizeTimer) {
				window.clearTimeout(resizeTimer);
			}
			resizeTimer = window.setTimeout(syncAll, RESIZE_DEBOUNCE_MS);
		});
	}

	if (document.readyState === 'loading') {
		document.addEventListener('DOMContentLoaded', boot);
	} else {
		boot();
	}
})();

/* FP-0002 V9-06E62E / FIX01 — header site search dropdown (desktop main header only) */
(function initSmartSearchForms() {
	'use strict';

	var cfg = window.shpigovskySmartSearch || {};
	var endpoint = typeof cfg.endpoint === 'string' ? cfg.endpoint : '';
	var minChars = typeof cfg.minChars === 'number' ? cfg.minChars : 3;
	var debounceMs = typeof cfg.debounceMs === 'number' ? cfg.debounceMs : 250;
	var i18n = cfg.i18n || {};
	var groupOrder = Array.isArray(cfg.groupOrder) && cfg.groupOrder.length
		? cfg.groupOrder
		: ['services', 'articles', 'specialists', 'pages'];
	var groupLabels = {
		services: i18n.services || 'Услуги',
		articles: i18n.articles || 'Статьи',
		specialists: i18n.specialists || 'Специалисты',
		pages: i18n.pages || 'Страницы',
	};

	if (!endpoint) {
		return;
	}

	function escapeHtml(value) {
		return String(value == null ? '' : value)
			.replace(/&/g, '&amp;')
			.replace(/</g, '&lt;')
			.replace(/>/g, '&gt;')
			.replace(/"/g, '&quot;')
			.replace(/'/g, '&#39;');
	}

	/**
	 * Shared Smart Search binder — one instance per form.
	 * Desktop header panel and mobile offcanvas each keep isolated request state.
	 */
	function bindSmartSearchForm(form) {
		if (!form || form.getAttribute('data-smart-search-init') === 'true') {
			return null;
		}

		var smartInput = form.querySelector('[data-smart-search-input]');
		var suggestRoot = form.querySelector('[data-smart-search-suggest]');

		if (!smartInput || !suggestRoot) {
			return null;
		}

		form.setAttribute('data-smart-search-init', 'true');

		var debounceTimer = null;
		var requestSeq = 0;
		var abortController = null;
		var activeIndex = -1;
		var resultLinks = [];

		function clearSuggest() {
			activeIndex = -1;
			resultLinks = [];
			suggestRoot.innerHTML = '';
			suggestRoot.hidden = true;
			suggestRoot.removeAttribute('data-smart-search-state');
		}

		function setSuggestState(state) {
			suggestRoot.hidden = false;
			suggestRoot.setAttribute('data-smart-search-state', state);
		}

		function renderLoading() {
			setSuggestState('loading');
			suggestRoot.innerHTML =
				'<p class="site-search-suggest__status">' + escapeHtml(i18n.loading || 'Поиск…') + '</p>';
		}

		function renderEmpty() {
			setSuggestState('empty');
			suggestRoot.innerHTML =
				'<p class="site-search-suggest__status">' + escapeHtml(i18n.empty || 'Ничего не найдено') + '</p>';
		}

		function renderError() {
			setSuggestState('error');
			suggestRoot.innerHTML =
				'<p class="site-search-suggest__status">' +
				escapeHtml(i18n.error || 'Не удалось выполнить поиск. Попробуйте ещё раз или отправьте форму.') +
				'</p>';
		}

		function renderGroups(groups) {
			var html = '';
			var total = 0;

			groupOrder.forEach(function (key) {
				var items = groups && groups[key] ? groups[key] : [];

				if (!items.length) {
					return;
				}

				html += '<section class="site-search-suggest__group" data-smart-search-group="' + escapeHtml(key) + '">';
				html += '<h3 class="site-search-suggest__heading">' + escapeHtml(groupLabels[key] || key) + '</h3>';
				html += '<ul class="site-search-suggest__list">';

				items.forEach(function (item) {
					var title = escapeHtml(item.title || '');
					var url = escapeHtml(item.url || '#');
					var snippet = item.snippet
						? '<span class="site-search-suggest__snippet">' + escapeHtml(item.snippet) + '</span>'
						: '';
					html +=
						'<li class="site-search-suggest__item">' +
						'<a class="site-search-suggest__link" href="' +
						url +
						'" data-smart-search-result>' +
						'<span class="site-search-suggest__title">' +
						title +
						'</span>' +
						snippet +
						'</a></li>';
					total += 1;
				});

				html += '</ul></section>';
			});

			if (!total) {
				renderEmpty();
				return;
			}

			setSuggestState('results');
			suggestRoot.innerHTML = html;
			resultLinks = Array.prototype.slice.call(suggestRoot.querySelectorAll('[data-smart-search-result]'));
			activeIndex = -1;
		}

		function setActiveResult(index) {
			if (!resultLinks.length) {
				activeIndex = -1;
				return;
			}

			if (index < 0) {
				activeIndex = -1;
			} else if (index >= resultLinks.length) {
				activeIndex = resultLinks.length - 1;
			} else {
				activeIndex = index;
			}

			resultLinks.forEach(function (link, i) {
				if (i === activeIndex) {
					link.setAttribute('data-smart-search-active', 'true');
					link.classList.add('is-active');
				} else {
					link.removeAttribute('data-smart-search-active');
					link.classList.remove('is-active');
				}
			});
		}

		function fetchSuggestions(query) {
			requestSeq += 1;
			var seq = requestSeq;

			if (abortController && typeof abortController.abort === 'function') {
				try {
					abortController.abort();
				} catch (err) {
					// Ignore abort errors.
				}
			}

			abortController = typeof window.AbortController === 'function' ? new window.AbortController() : null;
			renderLoading();

			var url = endpoint + (endpoint.indexOf('?') === -1 ? '?' : '&') + 'q=' + encodeURIComponent(query);
			var fetchOpts = {
				method: 'GET',
				credentials: 'same-origin',
				headers: {
					Accept: 'application/json',
				},
			};

			if (abortController) {
				fetchOpts.signal = abortController.signal;
			}

			window
				.fetch(url, fetchOpts)
				.then(function (response) {
					if (!response.ok) {
						throw new Error('smart-search-http');
					}

					return response.json();
				})
				.then(function (data) {
					if (seq !== requestSeq) {
						return;
					}

					if (!data || data.empty) {
						renderEmpty();
						return;
					}

					renderGroups(data.groups || {});
				})
				.catch(function (err) {
					if (seq !== requestSeq) {
						return;
					}

					if (err && err.name === 'AbortError') {
						return;
					}

					renderError();
				});
		}

		function scheduleSuggest(rawValue) {
			var value = String(rawValue || '').replace(/^\s+|\s+$/g, '');

			if (debounceTimer) {
				window.clearTimeout(debounceTimer);
				debounceTimer = null;
			}

			if (value.length < minChars) {
				if (abortController && typeof abortController.abort === 'function') {
					try {
						abortController.abort();
					} catch (err) {
						// Ignore.
					}
				}
				requestSeq += 1;
				clearSuggest();
				return;
			}

			debounceTimer = window.setTimeout(function () {
				fetchSuggestions(value);
			}, debounceMs);
		}

		function isInstanceActive() {
			if (document.activeElement === smartInput) {
				return true;
			}

			if (suggestRoot.contains(document.activeElement)) {
				return true;
			}

			return !suggestRoot.hidden && form.contains(document.activeElement);
		}

		smartInput.addEventListener('input', function () {
			scheduleSuggest(smartInput.value);
		});

		smartInput.addEventListener('search', function () {
			scheduleSuggest(smartInput.value);
		});

		document.addEventListener('keydown', function (event) {
			if (!isInstanceActive()) {
				return;
			}

			if (event.key === 'Escape') {
				if (!suggestRoot.hidden) {
					event.preventDefault();
					event.stopImmediatePropagation();
					clearSuggest();
				}
				return;
			}

			if (suggestRoot.hidden || !resultLinks.length) {
				return;
			}

			if (event.key === 'ArrowDown') {
				event.preventDefault();
				setActiveResult(activeIndex + 1);
				return;
			}

			if (event.key === 'ArrowUp') {
				event.preventDefault();
				setActiveResult(activeIndex <= 0 ? -1 : activeIndex - 1);
				return;
			}

			if (event.key === 'Enter' && activeIndex >= 0 && resultLinks[activeIndex]) {
				event.preventDefault();
				window.location.href = resultLinks[activeIndex].href;
			}
		});

		return {
			form: form,
			input: smartInput,
			suggestRoot: suggestRoot,
			clearSuggest: clearSuggest,
		};
	}

	var instances = [];
	Array.prototype.forEach.call(document.querySelectorAll('[data-smart-search-form]'), function (form) {
		var instance = bindSmartSearchForm(form);
		if (instance) {
			instances.push(instance);
		}
	});

	window.shpigovskySmartSearchInstances = instances;
})();

(function initSiteSearchPanel() {
	'use strict';

	var panel = document.querySelector('[data-search-panel]');

	if (!panel || panel.getAttribute('data-search-init') === 'true') {
		return;
	}

	panel.setAttribute('data-search-init', 'true');

	// Only explicit dropdown toggles (data-search-toggle). Mobile offcanvas owns its own form.
	var toggles = document.querySelectorAll('[data-search-toggle]');
	var closeButtons = panel.querySelectorAll('[data-search-close]');
	var forms = document.querySelectorAll('[data-site-search-form]');
	var isOpen = false;
	var lastToggle = null;
	var panelSmartForm = panel.querySelector('[data-smart-search-form]');

	function getFocusInput() {
		return panel.querySelector('[data-search-focus], input[type="search"], input[name="s"]');
	}

	function clearPanelSuggest() {
		if (!panelSmartForm) {
			return;
		}

		var instances = window.shpigovskySmartSearchInstances || [];
		instances.forEach(function (instance) {
			if (instance && instance.form === panelSmartForm && typeof instance.clearSuggest === 'function') {
				instance.clearSuggest();
			}
		});
	}

	function setOpen(open, trigger) {
		if (open === isOpen) {
			if (open) {
				var input = getFocusInput();
				if (input) {
					input.focus();
				}
			}
			return;
		}

		isOpen = open;

		if (open) {
			panel.hidden = false;
			panel.setAttribute('data-search-state', 'open');
			panel.removeAttribute('hidden');

			// Close conflicting UI.
			var offcanvasClose = document.querySelector('[data-offcanvas][data-offcanvas-state="open"] [data-offcanvas-close]');
			if (offcanvasClose) {
				offcanvasClose.click();
			}

			var modal = document.querySelector('[data-modal="consultation"][data-modal-state="open"]');
			if (modal) {
				var modalClose = modal.querySelector('[data-modal-close]');
				if (modalClose) {
					modalClose.click();
				}
			}
		} else {
			panel.setAttribute('data-search-state', 'closed');
			panel.hidden = true;
			panel.setAttribute('hidden', 'hidden');
			clearPanelSuggest();
		}

		Array.prototype.forEach.call(toggles, function (btn) {
			btn.setAttribute('aria-expanded', open ? 'true' : 'false');
		});

		if (open) {
			lastToggle = trigger || lastToggle || toggles[0] || null;
			window.setTimeout(function () {
				var focusInput = getFocusInput();
				if (focusInput) {
					focusInput.focus();
				}
			}, 0);
		} else if (lastToggle && typeof lastToggle.focus === 'function') {
			lastToggle.focus();
		}
	}

	Array.prototype.forEach.call(toggles, function (btn) {
		btn.addEventListener('click', function (event) {
			event.preventDefault();
			var shouldOpen = btn.getAttribute('aria-expanded') !== 'true';
			setOpen(shouldOpen, btn);
		});
	});

	Array.prototype.forEach.call(closeButtons, function (btn) {
		btn.addEventListener('click', function (event) {
			event.preventDefault();
			setOpen(false);
		});
	});

	document.addEventListener('keydown', function (event) {
		if (!isOpen || event.key !== 'Escape') {
			return;
		}

		var suggest = panel.querySelector('[data-smart-search-suggest]');
		if (suggest && !suggest.hidden) {
			event.preventDefault();
			clearPanelSuggest();
			return;
		}

		event.preventDefault();
		setOpen(false);
	});

	document.addEventListener('click', function (event) {
		if (!isOpen) {
			return;
		}

		var target = event.target;
		if (!(target instanceof Element)) {
			return;
		}

		if (panel.contains(target) || target.closest('[data-search-toggle]')) {
			return;
		}

		setOpen(false);
	});

	// Close search when opening offcanvas or consultation modal.
	document.addEventListener('click', function (event) {
		var target = event.target;
		if (!(target instanceof Element)) {
			return;
		}

		if (target.closest('[data-offcanvas-open]') || target.closest('[data-modal-open="consultation"]')) {
			if (isOpen) {
				setOpen(false);
			}
		}
	}, true);

	Array.prototype.forEach.call(forms, function (form) {
		form.addEventListener('submit', function (event) {
			var input = form.querySelector('input[name="s"]');
			if (!input) {
				return;
			}

			var value = String(input.value || '').replace(/^\s+|\s+$/g, '');
			input.value = value;

			if (!value) {
				event.preventDefault();
				input.focus();
			}
		});
	});
})();

/* PROD-P13 — desktop submenu keyboard + offcanvas accordion */
(function initSecondLevelNav() {
	'use strict';

	function closeDesktop(item) {
		item.classList.remove('is-open');
		var link = item.querySelector(':scope > .site-header__nav-link');
		if (link) {
			link.setAttribute('aria-expanded', 'false');
		}
	}

	document.addEventListener('keydown', function (event) {
		if (event.key !== 'Escape') {
			return;
		}
		document.querySelectorAll('.site-header__nav-item--has-children.is-open').forEach(closeDesktop);
	});

	document.querySelectorAll('.site-header__nav-item--has-children').forEach(function (item) {
		var link = item.querySelector(':scope > .site-header__nav-link');
		if (link) {
			link.setAttribute('aria-expanded', 'false');
			link.addEventListener('focus', function () {
				item.classList.add('is-open');
				link.setAttribute('aria-expanded', 'true');
			});
		}
		item.addEventListener('focusout', function () {
			window.setTimeout(function () {
				if (!item.contains(document.activeElement)) {
					closeDesktop(item);
				}
			}, 0);
		});
	});

	document.querySelectorAll('[data-offcanvas-sub-toggle]').forEach(function (button) {
		button.addEventListener('click', function (event) {
			event.preventDefault();
			var expanded = button.getAttribute('aria-expanded') === 'true';
			var controls = button.getAttribute('aria-controls');
			var panel = controls ? document.getElementById(controls) : null;
			if (!panel && button.parentElement && button.parentElement.parentElement) {
				panel = button.parentElement.parentElement.querySelector('.offcanvas__sub-list');
			}
			button.setAttribute('aria-expanded', expanded ? 'false' : 'true');
			if (panel) {
				panel.hidden = expanded;
			}
		});
	});
})();
