<?php
/**
 * BZPM M9 — filter profile: Полки (category 331).
 *
 * Scope: branch root 331 and descendants only.
 * Built from production attribute inventory (SITE-002-PROD-M9-POLKI-PROFILE-331-01).
 * Do not copy 86_stellazhi / 301_stoly blindly — shelf PLP axes differ.
 *
 * Note: DB has packaging dims (44/45/46/56) but no buyer product L/W/H attrs for this branch.
 */
return array(
	'profile_id' => 331,
	'profile_key' => 'polki',
	'label' => 'Полки',
	'branch_root_id' => 331,
	'primary_attribute_ids' => array(
		51,  // Конструкция полки (сплошная / перфорированная / закрытая / …)
		112, // Материал полки
		21,  // Конструкция (разборная / сварная)
		122, // Максимальная распределенная нагрузка на полку (кг)
	),
	'primary_sort' => array(
		51 => 10,
		112 => 20,
		21 => 30,
		122 => 40,
	),
	'secondary_attribute_ids' => array(
		123, // Двери (niche closed-shelf SKUs)
		26,  // Ножки (single distinct value — not PRIMARY)
		114, // Количество полок (шт) (low coverage / single value)
		115, // Усиление (single distinct value)
	),
	'secondary_sort' => array(
		123 => 10,
		26 => 20,
		114 => 30,
		115 => 40,
	),
	'hidden_attribute_ids' => array(
		// Explicit branch notes; packaging/SERVICE/TECHNICAL also covered by global_hidden.php
		42, // Стандарт (noisy TECHNICAL, single "Да")
		43, // Дополнительные сведения (SERVICE / free-text)
		44, // Длина в упаковке (мм)
		45, // Ширина в упаковке (мм)
		46, // Высота в упаковке (мм)
		56, // Упаковка (Объем)
	),
);
