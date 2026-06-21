<?php
/**
 * BZPM M9 Phase 3 — filter profile: Подтоварники и подставки (category 322).
 *
 * Scope: branch root 322 and descendants only.
 * Authority: BZPM-M9-FILTER-PROFILE-SYSTEM-v1.md (branch 322 classification).
 */
return array(
	'profile_id' => 322,
	'profile_key' => 'podtovarniki',
	'label' => 'Подтоварники и подставки',
	'branch_root_id' => 322,
	'primary_attribute_ids' => array(
		51, // Конструкция полки
		20, // Макс. нагрузка (до, кг)
	),
	'primary_sort' => array(
		51 => 10,
		20 => 20,
	),
	'secondary_attribute_ids' => array(
		22,  // Материал столешницы
		33,  // Тип опоры
		21,  // Конструкция
		38,  // Количество
		26,  // Ножки
		31,  // Регулируемость опоры по высоте (max мм)
		115, // Усиление
		30,  // Размер секции (REVIEW — 3 SKU)
		24,  // Назначение секции (REVIEW — 3 SKU)
		19,  // Количество уровней направляющих (REVIEW — 3 SKU)
	),
	'secondary_sort' => array(
		22 => 10,
		33 => 20,
		21 => 30,
		38 => 40,
		26 => 50,
		31 => 60,
		115 => 70,
		30 => 80,
		24 => 90,
		19 => 100,
	),
	'hidden_attribute_ids' => array(
		23,  // Мойка — sink cluster
		28,  // Отверстие под смеситель
		29,  // Размер раковины
		47,  // Конструкция борта
		112, // Материал полки — not used in branch
		25,  // Наличие борта — table/sink attr
		18,  // Высота борта — not branch focus
	),
);
