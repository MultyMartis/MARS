<?php
/**
 * BZPM M9 Phase 3 — filter profile: Зонты вытяжные (category 207).
 *
 * Scope: branch root 207 and descendants only.
 * Authority: BZPM-M9-FILTER-PROFILE-SYSTEM-v1.md (branch 207 classification).
 */
return array(
	'profile_id' => 207,
	'profile_key' => 'zonty',
	'label' => 'Зонты вытяжные',
	'branch_root_id' => 207,
	'primary_attribute_ids' => array(
		21, // Конструкция
	),
	'primary_sort' => array(
		21 => 10,
	),
	'secondary_attribute_ids' => array(
		34, // Страна производства — branch exception (overrides global TECHNICAL hide)
	),
	'secondary_sort' => array(
		34 => 10,
	),
	'hidden_attribute_ids' => array(
		12,  // Габариты нетто — duplicates product dims (also global)
		23,  // Мойка
		28,  // Отверстие под смеситель
		29,  // Размер раковины
		51,  // Конструкция полки
		112, // Материал полки
		115, // Усиление
		20,  // Макс. нагрузка
		22,  // Материал столешницы
		25,  // Наличие борта
	),
);
