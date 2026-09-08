<?php
/**
 * SITE-002 — PDP hero specs family resolver
 * Operations: SITE-002-PROD-PDP-HERO-SPECS-STELLAZHI-86-01; SITE-002-PROD-PDP-HERO-SPECS-HLEBOPEKARNOE-186-01; SITE-002-POLKI-PDP-HERO-SPECS-GO1-BUILD-01
 *
 * Returns ordered attribute IDs for `.product-hero__specs` (after L/W/H/weight).
 * Family map for [86] Стеллажи, [186] Хлебопекарное, and [331] Полки; otherwise SUPER_ATTS fallback.
 * Does not alter full characteristics table (attribute_groups).
 */
class ProductHeroSpecsResolver
{
	/** Shelving branch root category_id */
	const FAMILY_ROOT_STELLAZHI = 86;

	/** Bakery equipment branch root category_id */
	const FAMILY_ROOT_HLEBOPEKARNOE = 186;

	/** Shelves branch root category_id */
	const FAMILY_ROOT_POLKI = 331;

	/**
	 * Attribute IDs appended after product dimensions for [86] Стеллажи.
	 * Order: Конструкция, Количество полок, Макс. нагрузка на полку, Ножки, Тип опоры.
	 *
	 * @var int[]
	 */
	private $family_attr_map = array(
		86 => array(21, 114, 122, 26, 33),
		// Объем, Мощность кВт, Напряжение, Кол-во скоростей, Загрузка сухого, Загрузка теста, об/мин, Реверс
		186 => array(127, 135, 134, 130, 129, 128, 132, 137),
		// [331] Полки: 51, 112, Конструкция, Макс. нагрузка на полку, Ножки, 123; omit 114. Optional 115 if filled.
		331 => array(51, 112, 21, 122, 26, 123, 115),
	);

	/** @var object|null */
	private $db;

	public function __construct($db = null)
	{
		$this->db = $db;
	}

	/**
	 * Resolve ordered hero attribute IDs for a product.
	 *
	 * @param int $product_id
	 * @param int $path_category_id leaf category from request path (optional)
	 * @return int[]
	 */
	public function resolveAttributeIds($product_id, $path_category_id = 0)
	{
		$product_id = (int)$product_id;
		$path_category_id = (int)$path_category_id;

		if ($this->isShelvingProduct($product_id, $path_category_id)) {
			return $this->family_attr_map[self::FAMILY_ROOT_STELLAZHI];
		}

		if ($this->isBakeryProduct($product_id, $path_category_id)) {
			return $this->family_attr_map[self::FAMILY_ROOT_HLEBOPEKARNOE];
		}

		if ($this->isPolkiProduct($product_id, $path_category_id)) {
			return $this->family_attr_map[self::FAMILY_ROOT_POLKI];
		}

		if (defined('SUPER_ATTS') && is_array(SUPER_ATTS)) {
			$ids = array();

			foreach (SUPER_ATTS as $aid) {
				$aid = (int)$aid;

				if ($aid > 0) {
					$ids[] = $aid;
				}
			}

			return $ids;
		}

		return array();
	}

	/**
	 * @param int $product_id
	 * @param int $path_category_id
	 * @return bool
	 */
	private function isShelvingProduct($product_id, $path_category_id)
	{
		$root = self::FAMILY_ROOT_STELLAZHI;

		if ($path_category_id > 0 && $this->isUnderBranchRoot($path_category_id, $root)) {
			return true;
		}

		if ($product_id <= 0 || !$this->db) {
			return false;
		}

		$query = $this->db->query(
			"SELECT COUNT(*) AS total"
			. " FROM `" . DB_PREFIX . "product_to_category` pc"
			. " INNER JOIN `" . DB_PREFIX . "category_path` cp"
			. "   ON cp.category_id = pc.category_id"
			. " WHERE pc.product_id = '" . (int)$product_id . "'"
			. "   AND cp.path_id = '" . (int)$root . "'"
		);

		return !empty($query->row['total']);
	}

	/**
	 * @param int $category_id
	 * @param int $root_id
	 * @return bool
	 */

	/**
	 * @param int $product_id
	 * @param int $path_category_id
	 * @return bool
	 */
	private function isBakeryProduct($product_id, $path_category_id)
	{
		$root = self::FAMILY_ROOT_HLEBOPEKARNOE;

		if ($path_category_id > 0 && $this->isUnderBranchRoot($path_category_id, $root)) {
			return true;
		}

		if ($product_id <= 0 || !$this->db) {
			return false;
		}

		$query = $this->db->query(
			"SELECT COUNT(*) AS total"
			. " FROM `" . DB_PREFIX . "product_to_category` pc"
			. " INNER JOIN `" . DB_PREFIX . "category_path` cp"
			. "   ON cp.category_id = pc.category_id"
			. " WHERE pc.product_id = '" . (int)$product_id . "'"
			. "   AND cp.path_id = '" . (int)$root . "'"
		);

		return !empty($query->row['total']);
	}

	/**
	 * @param int $product_id
	 * @param int $path_category_id
	 * @return bool
	 */
	private function isPolkiProduct($product_id, $path_category_id)
	{
		$root = self::FAMILY_ROOT_POLKI;

		if ($path_category_id > 0 && $this->isUnderBranchRoot($path_category_id, $root)) {
			return true;
		}

		if ($product_id <= 0 || !$this->db) {
			return false;
		}

		$query = $this->db->query(
			"SELECT COUNT(*) AS total"
			. " FROM `" . DB_PREFIX . "product_to_category` pc"
			. " INNER JOIN `" . DB_PREFIX . "category_path` cp"
			. "   ON cp.category_id = pc.category_id"
			. " WHERE pc.product_id = '" . (int)$product_id . "'"
			. "   AND cp.path_id = '" . (int)$root . "'"
		);

		return !empty($query->row['total']);
	}

	private function isUnderBranchRoot($category_id, $root_id)
	{
		if (!$this->db || $category_id <= 0 || $root_id <= 0) {
			return false;
		}

		if ((int)$category_id === (int)$root_id) {
			return true;
		}

		$query = $this->db->query(
			"SELECT COUNT(*) AS total FROM `" . DB_PREFIX . "category_path`"
			. " WHERE category_id = '" . (int)$category_id . "'"
			. "   AND path_id = '" . (int)$root_id . "'"
		);

		return !empty($query->row['total']);
	}
}
