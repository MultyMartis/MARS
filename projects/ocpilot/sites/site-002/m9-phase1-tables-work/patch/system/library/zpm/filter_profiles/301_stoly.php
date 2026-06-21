<?php
/**
 * BZPM M9 Phase 1 — filter profile: Столы (category 301).
 *
 * Scope: branch root 301 and descendants only.
 * Future profiles (80, 322, 207) follow the same schema in sibling files.
 */
return array(
	'profile_id' => 301,
	'profile_key' => 'stoly',
	'label' => 'Столы',
	'branch_root_id' => 301,
	'primary_attribute_ids' => array(
		22, // Материал столешницы
		51, // Конструкция полки
		33, // Тип опоры
		20, // Макс. нагрузка (до, кг)
		25, // Наличие борта
	),
	'primary_sort' => array(
		22 => 10,
		51 => 20,
		33 => 30,
		20 => 40,
		25 => 50,
	),
	'secondary_attribute_ids' => array(
		21,  // Конструкция
		112, // Материал полки
		26,  // Ножки
		31,  // Регулируемость опоры по высоте (max мм)
		115, // Усиление
		18,  // Высота борта (мм)
		47,  // Конструкция борта
	),
	'secondary_sort' => array(
		21 => 10,
		112 => 20,
		26 => 30,
		31 => 40,
		115 => 50,
		18 => 60,
		47 => 70,
	),
	'hidden_attribute_ids' => array(
		23, // Мойка
		28, // Отверстие под смеситель
		29, // Размер раковины (ДхШхВ, мм)
	),
);
