<?php
/**
 * BZPM M9 — filter profile: Стеллажи (category 86).
 *
 * Scope: branch root 86 and descendants only.
 * Built from production attribute inventory (SITE-002-PROD-M9-STELLAZHI-PROFILE-86-01).
 * Do not copy 301_stoly blindly — rack-specific axes differ (51/122/26/114).
 */
return array(
	'profile_id' => 86,
	'profile_key' => 'stellazhi',
	'label' => 'Стеллажи',
	'branch_root_id' => 86,
	'primary_attribute_ids' => array(
		51,  // Конструкция полки (перфорированная / сплошная / решётчатая)
		122, // Максимальная распределенная нагрузка на полку (кг)
		26,  // Ножки / каркас (уголок / труба, сталь)
		114, // Количество полок (шт)
	),
	'primary_sort' => array(
		51 => 10,
		122 => 20,
		26 => 30,
		114 => 40,
	),
	'secondary_attribute_ids' => array(
		112, // Материал полки
		21,  // Конструкция
		33,  // Тип опоры
		31,  // Регулируемость опоры по высоте (max мм)
		113, // Шаг регулировки полки (мм)
		115, // Усиление
	),
	'secondary_sort' => array(
		112 => 10,
		21 => 20,
		33 => 30,
		31 => 40,
		113 => 50,
		115 => 60,
	),
	'hidden_attribute_ids' => array(
		// Explicit branch notes; packaging/SERVICE/TECHNICAL also covered by global_hidden.php
		42, // Стандарт (noisy TECHNICAL)
		43, // Дополнительные сведения (SERVICE / free-text)
	),
);
