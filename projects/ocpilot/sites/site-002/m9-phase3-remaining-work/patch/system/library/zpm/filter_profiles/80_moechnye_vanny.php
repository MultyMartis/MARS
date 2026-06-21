<?php
/**
 * BZPM M9 Phase 2 — filter profile: Моечные ванны (category 80).
 *
 * Scope: branch root 80 and descendants only.
 * Authority: BZPM-M9-FILTER-PROFILE-SYSTEM-v1.md (branch 80 classification).
 */
return array(
	'profile_id' => 80,
	'profile_key' => 'moechnye_vanny',
	'label' => 'Моечные ванны',
	'branch_root_id' => 80,
	'primary_attribute_ids' => array(
		29, // Размер раковины (ДхШхВ, мм)
		23, // Мойка
		25, // Наличие борта
	),
	'primary_sort' => array(
		29 => 10,
		23 => 20,
		25 => 30,
	),
	'secondary_attribute_ids' => array(
		28, // Отверстие под смеситель
		47, // Конструкция борта
		18, // Высота борта (мм)
		33, // Тип опоры
		26, // Ножки
		21, // Конструкция
		31, // Регулируемость опоры по высоте (max мм)
		22, // Материал столешницы
		17, // В комплекте
	),
	'secondary_sort' => array(
		28 => 10,
		47 => 20,
		18 => 30,
		33 => 40,
		26 => 50,
		21 => 60,
		31 => 70,
		22 => 80,
		17 => 90,
	),
	'hidden_attribute_ids' => array(
		51,  // Конструкция полки — table-only
		112, // Материал полки — table-only
		115, // Усиление — table-only
		20,  // Макс. нагрузка (до, кг) — table-only
	),
);
