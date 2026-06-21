<?php
/**
 * BZPM M8.3 Wave 2 — attribute filter visibility (STORE_ONLY).
 *
 * Authority: BZPM-M8.2-CLEANUP-SPECIFICATION-v1.md
 * Model: data remains in DB / import / 1C; hidden from PLP filter sidebar only.
 * Scope: PACKAGING + SERVICE classes — not COMMERCIAL, not REVIEW, not M9 profiles.
 */
class AttributeFilterVisibility {
	/** @var int[] Packaging cluster — M8.2 Packaging Data Audit */
	private static $packaging_attribute_ids = array(
		44, // Длина в упаковке (мм)
		45, // Ширина в упаковке (мм)
		46, // Высота в упаковке (мм)
		52, // Упаковка (Длина, мм)
		53, // Упаковка (Ширина, мм)
		54, // Упаковка (Высота, мм)
		56, // Упаковка (Объем, м. куб.)
		57, // Вес (нетто, кг)
	);

	/** @var int[] SERVICE attrs — M8.2 Hidden Attribute Set */
	private static $service_attribute_ids = array(
		43, // Дополнительные сведения
		48, // Комплект поставки
		58, // Комплект отгрузки
	);

	public function getPackagingAttributeIds() {
		return self::$packaging_attribute_ids;
	}

	public function getServiceAttributeIds() {
		return self::$service_attribute_ids;
	}

	/**
	 * Attribute IDs hidden from PLP filter (STORE_ONLY for filter layer).
	 *
	 * @return int[]
	 */
	public function getStoreOnlyAttributeIds() {
		return array_values(array_unique(array_merge(
			self::$packaging_attribute_ids,
			self::$service_attribute_ids
		)));
	}

	public function isStoreOnly($attribute_id) {
		return in_array((int)$attribute_id, $this->getStoreOnlyAttributeIds(), true);
	}
}
