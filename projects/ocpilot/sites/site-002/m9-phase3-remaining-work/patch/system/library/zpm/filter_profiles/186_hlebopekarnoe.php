<?php
/**
 * BZPM M9 — filter profile: Хлебопекарное оборудование (category 186).
 *
 * Scope: branch root 186 and descendants only (INH-01).
 * Built from production attribute inventory (SITE-002-PROD-M9-HLEBOPEKARNOE-PROFILE-186-01).
 * Do not copy 86_stellazhi / 301_stoly / 331_polki blindly — bakery PLP axes differ.
 *
 * Current SKUs live under [188] Миксеры планетарные and [189] Тестомесы.
 * Shared buyer axes: volume / power / voltage. Child-specific capacity/speed as SECONDARY.
 * Note: PLP L/W/H sliders are a separate UX layer (not these packaging attrs).
 */
return array(
	'profile_id' => 186,
	'profile_key' => 'hlebopekarnoe',
	'label' => 'Хлебопекарное оборудование',
	'branch_root_id' => 186,
	'primary_attribute_ids' => array(
		127, // Объем (bowl/deza) — all 12 SKUs
		135, // Мощность, кВт
		134, // Напряжение (220В / 380В)
	),
	'primary_sort' => array(
		127 => 10,
		135 => 20,
		134 => 30,
	),
	'secondary_attribute_ids' => array(
		130, // Количество скоростей
		129, // Загрузка сухого продукта
		128, // Загрузка теста (dough mixers)
		132, // Скорость об/мин (dough mixers)
		137, // Реверс (single value — not PRIMARY)
	),
	'secondary_sort' => array(
		130 => 10,
		129 => 20,
		128 => 30,
		132 => 40,
		137 => 50,
	),
	'hidden_attribute_ids' => array(
		// Explicit branch notes; packaging/SERVICE also covered by global_hidden.php
		126, // Материал изготовления (single value, 3 SKUs — no discrimination)
		43,  // Дополнительные сведения (SERVICE / free-text)
		44,  // Длина в упаковке (мм)
		45,  // Ширина в упаковке (мм)
		46,  // Высота в упаковке (мм)
		56,  // Упаковка (Объем)
	),
);
