<?php
/**
 * BZPM M9 Phase 3 — filter profile: Тележки сервировочные (category 326).
 *
 * Scope: branch root 326 and descendants only.
 * Authority: BZPM-M9-FILTER-PROFILE-SYSTEM-v1.md (branch 326 sparse profile).
 * N=3 active SKU — dims + price + availability only; attr 42 deferred (global HIDDEN).
 */
return array(
	'profile_id' => 326,
	'profile_key' => 'telezhki_servirovochnye',
	'label' => 'Тележки сервировочные',
	'branch_root_id' => 326,
	'primary_attribute_ids' => array(),
	'primary_sort' => array(),
	'secondary_attribute_ids' => array(),
	'secondary_sort' => array(),
	'hidden_attribute_ids' => array(
		42, // Стандарт — REVIEW until N>=20 (also global TECHNICAL)
	),
);
