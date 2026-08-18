/**
 * Multi-recipient editor for Настройки сайта → Почта и формы.
 * Add/remove rows client-side. Does not touch the SMTP password field.
 */
(function () {
	'use strict';

	var root = document.querySelector('[data-fp02-recipients]');
	if (!root) {
		return;
	}

	var list = root.querySelector('[data-fp02-recipients-list]');
	var addBtn = root.querySelector('[data-fp02-recipient-add]');
	var tmpl = document.getElementById('fp02-recipient-row-template');
	var max = parseInt(root.getAttribute('data-fp02-max') || '20', 10);
	if (!list || !addBtn || !tmpl) {
		return;
	}

	function rows() {
		return list.querySelectorAll('[data-fp02-recipient-row]');
	}

	function nextIndex() {
		var maxI = -1;
		var inputs = list.querySelectorAll('input[name*="[email]"]');
		for (var i = 0; i < inputs.length; i++) {
			var match = String(inputs[i].name).match(/recipients\[(\d+)\]/);
			if (match) {
				maxI = Math.max(maxI, parseInt(match[1], 10));
			}
		}
		return maxI + 1;
	}

	function syncAddState() {
		addBtn.disabled = rows().length >= max;
	}

	function addRow(focus) {
		if (rows().length >= max) {
			return;
		}
		var html = tmpl.innerHTML.replace(/__i__/g, String(nextIndex()));
		list.insertAdjacentHTML('beforeend', html);
		if (focus) {
			var last = list.querySelector('[data-fp02-recipient-row]:last-child input[type="email"]');
			if (last) {
				last.focus();
			}
		}
		syncAddState();
	}

	addBtn.addEventListener('click', function (event) {
		event.preventDefault();
		addRow(true);
	});

	list.addEventListener('click', function (event) {
		var btn = event.target.closest('[data-fp02-recipient-remove]');
		if (!btn) {
			return;
		}
		event.preventDefault();
		var row = btn.closest('[data-fp02-recipient-row]');
		if (row) {
			row.remove();
		}
		if (rows().length === 0) {
			addRow(true);
		}
		syncAddState();
	});

	syncAddState();
})();
