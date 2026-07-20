<?php
/**
 * BZPM Launch Mode — unified category visibility layer (M7.1).
 * M9.5 — neutral root hub branch list for category 79.
 * M9.7C — megamenu children filtered to categories with active products only.
 * M9.7E — homepage category section uses neutral hub branches
 * SITE-002-PROD-PARENT-CATEGORY-TILES-LARI-REMOVAL-01 — removed ID 88 from parent tiles whitelist (not launch root card).
 * SITE-002-PROD-CATALOG-TILE-BLOCKS-AUTOMATION-01 — Catalog Section Tiles / Плитки разделов каталога:
 *   peer root Технологическое оборудование (362); multi-section tile blocks; placeholder fallback.
 *
 * Single source of truth for Launch Mode navigation and /katalog presentation.
 * Controllers must use this class; do not hardcode visibility rules in Twig.
 */
class CategoryVisibility {
	const LAUNCH_MODE = true;
	const CATALOG_PRIMARY_ENTRY = '/katalog/nejtralnoe-oborudovanie';
	const ACTIVE_LAUNCH_ROOT = 'nejtralnoe-oborudovanie';
	/** @deprecated use getVisibleRootCategoryIds(); kept for older call sites */
	const VISIBLE_ROOT_CATEGORY_ID = 79;
	const NEUTRAL_HUB_CATEGORY_ID = 79;
	const TECHNOLOGICAL_HUB_CATEGORY_ID = 362;
	const PLACEHOLDER_IMAGE = 'placeholder.png';

	private static $visible_root_category_ids = array(79, 362);

	private static $visible_root_slugs = array(
		'nejtralnoe-oborudovanie',
		'tehnologicheskoe-oborudovanie',
	);

	private static $hidden_root_slugs = array(
		'teplovoe-oborudovanie',
		'holodilnoe-oborudovanie',
		'inventar',
		'elektromehanicheskoe-oborudovanie',
		'barnoe-oborudovanie',
		'hlebopekarnoe-oborudovanie',
		'posudomoechnye-mashiny',
		'ventilyacionnoe-oborudovanie',
	);

	/** Commercial curated list for neutral hub Catalog Section Tiles (M9.5+). */
	private static $neutral_hub_branch_ids = array(322, 331, 301, 326, 354, 358, 207, 80, 86, 360);

	public function isLaunchMode() {
		return self::LAUNCH_MODE;
	}

	public function getPrimaryCatalogEntry() {
		return self::CATALOG_PRIMARY_ENTRY;
	}

	public function getActiveLaunchRootSlug() {
		return self::ACTIVE_LAUNCH_ROOT;
	}

	public function getVisibleRootSlugs() {
		return self::$visible_root_slugs;
	}

	public function getVisibleRootCategoryIds() {
		return self::$visible_root_category_ids;
	}

	public function getHiddenRootSlugs() {
		return self::$hidden_root_slugs;
	}

	public function isNeutralHubCategory($category_id) {
		return (int)$category_id === self::NEUTRAL_HUB_CATEGORY_ID;
	}

	public function isTechnologicalHubCategory($category_id) {
		return (int)$category_id === self::TECHNOLOGICAL_HUB_CATEGORY_ID;
	}

	/** Section hubs that render Catalog Section Tiles (child cards) instead of product PLP. */
	public function isSectionHubCategory($category_id) {
		return in_array((int)$category_id, self::$visible_root_category_ids, true);
	}

	public function getNeutralHubBranchIds() {
		return self::$neutral_hub_branch_ids;
	}

	public function extractRootSlugFromHref($href) {
		if (!is_string($href) || $href === '') {
			return '';
		}

		$path = parse_url($href, PHP_URL_PATH);
		if (!is_string($path) || $path === '') {
			return '';
		}

		$path = trim($path, '/');
		if ($path === '') {
			return '';
		}

		$parts = explode('/', $path);
		if (count($parts) >= 2 && $parts[0] === 'katalog') {
			$slug = trim($parts[1]);
			if ($slug !== '') {
				return $slug;
			}
		}

		// Flat SEO roots (no /katalog/ prefix), e.g. /tehnologicheskoe-oborudovanie
		if (count($parts) >= 1) {
			$slug = trim($parts[0]);
			if ($slug !== '' && in_array($slug, self::$visible_root_slugs, true)) {
				return $slug;
			}
		}

		return '';
	}

	public function isVisibleRootCategory($category) {
		if (!$this->isLaunchMode()) {
			return true;
		}

		if (!is_array($category)) {
			return false;
		}

		if (isset($category['category_id']) && in_array((int)$category['category_id'], self::$visible_root_category_ids, true)) {
			return true;
		}

		$slug = '';

		if (!empty($category['keyword'])) {
			$slug = $category['keyword'];
		} elseif (!empty($category['href'])) {
			$slug = $this->extractRootSlugFromHref($category['href']);
		}

		return in_array($slug, self::$visible_root_slugs, true);
	}

	public function filterRootCategories(array $categories) {
		if (!$this->isLaunchMode()) {
			return $categories;
		}

		$filtered = array();

		foreach ($categories as $category) {
			if ($this->isVisibleRootCategory($category)) {
				$filtered[] = $category;
			}
		}

		return $this->markFirstActive($filtered);
	}

	private function markFirstActive(array $categories) {
		$first = true;

		foreach ($categories as $key => $category) {
			$categories[$key]['active'] = $first;
			$first = false;
		}

		return $categories;
	}

	/**
	 * Normalize category name for Russian A→Я sort (trim; case-insensitive; Ё→Е).
	 */
	private function normalizeCategoryNameForSort($name) {
		$name = trim((string)$name);

		if ($name === '') {
			return '';
		}

		if (function_exists('mb_strtolower')) {
			$name = mb_strtolower($name, 'UTF-8');
		} else {
			$name = strtolower($name);
		}

		return str_replace(array('ё', 'Ё'), 'е', $name);
	}

	/**
	 * Compare two visible category names for Russian A→Я ordering.
	 */
	private function compareCategoryNamesRu($left, $right) {
		$left = $this->normalizeCategoryNameForSort($left);
		$right = $this->normalizeCategoryNameForSort($right);

		static $collator = null;

		if ($collator === null && class_exists('Collator')) {
			$collator = new Collator('ru_RU');
		}

		if ($collator instanceof Collator) {
			return $collator->compare($left, $right);
		}

		return strcmp($left, $right);
	}

	/**
	 * Sort category rows by visible Russian name A→Я without changing membership.
	 */
	public function sortCategoriesByRussianName(array $categories, $name_key = 'name') {
		if (count($categories) < 2) {
			return $categories;
		}

		usort($categories, function ($left, $right) use ($name_key) {
			$left_name = (is_array($left) && isset($left[$name_key])) ? $left[$name_key] : '';
			$right_name = (is_array($right) && isset($right[$name_key])) ? $right[$name_key] : '';

			return $this->compareCategoryNamesRu($left_name, $right_name);
		});

		return $categories;
	}

	/**
	 * Build OpenCart path= chain from category_path for correct nested SEO URLs.
	 * SITE-002-PROD-CATEGORY-LARI-REPARENT-IMPLEMENTATION-01
	 */
	public function buildCategoryPathParam($controller, $category_id) {
		$category_id = (int)$category_id;

		if ($category_id <= 0) {
			return '';
		}

		$query = $controller->db->query("SELECT path_id FROM " . DB_PREFIX . "category_path WHERE category_id = '" . $category_id . "' ORDER BY level ASC");
		$parts = array();

		foreach ($query->rows as $row) {
			$parts[] = (int)$row['path_id'];
		}

		return implode('_', $parts);
	}

	private function resizeCategoryImage($controller, $image, $width = 300, $height = 300) {
		if (!empty($image)) {
			return $controller->model_tool_image->resize($image, $width, $height);
		}

		return $controller->model_tool_image->resize(self::PLACEHOLDER_IMAGE, $width, $height);
	}

	private function buildCardFromCategory($controller, $branch_id, $branch, $require_products) {
		$branch_id = (int)$branch_id;

		if (!$branch) {
			return null;
		}

		$filter_data = array(
			'filter_category_id'  => $branch_id,
			'filter_sub_category' => true
		);

		$count = (int)$controller->model_catalog_product->getTotalProducts($filter_data);

		if ($require_products && $count <= 0) {
			return null;
		}

		return array(
			'category_id' => $branch_id,
			'name'        => $branch['name'],
			'href'        => $controller->url->link('product/katalog', 'path=' . $this->buildCategoryPathParam($controller, $branch_id)),
			'img'         => $this->resizeCategoryImage($controller, isset($branch['image']) ? $branch['image'] : ''),
			'thumb300'    => $this->resizeCategoryImage($controller, isset($branch['image']) ? $branch['image'] : ''),
			'count'       => $count,
		);
	}

	/**
	 * Child cards for a section hub.
	 * Neutral (79): curated whitelist + products required (preserve commercial design).
	 * Other visible roots (362+): DB direct children, status-driven; include empty hubs so 1C growth appears without Twig edits.
	 */
	public function buildHubChildCards($controller, $root_category_id) {
		$root_category_id = (int)$root_category_id;

		$controller->load->model('catalog/category');
		$controller->load->model('catalog/product');
		$controller->load->model('tool/image');

		$cards = array();

		if ($root_category_id === self::NEUTRAL_HUB_CATEGORY_ID) {
			foreach ($this->getNeutralHubBranchIds() as $branch_id) {
				$branch = $controller->model_catalog_category->getCategory((int)$branch_id);
				$card = $this->buildCardFromCategory($controller, $branch_id, $branch, true);

				if ($card) {
					$cards[] = $card;
				}
			}
		} else {
			$results = $controller->model_catalog_category->getCategories($root_category_id);

			foreach ($results as $result) {
				$branch_id = (int)$result['category_id'];
				$branch = $controller->model_catalog_category->getCategory($branch_id);
				$card = $this->buildCardFromCategory($controller, $branch_id, $branch, false);

				if ($card) {
					$cards[] = $card;
				}
			}
		}

		return $this->sortCategoriesByRussianName($cards);
	}

	/**
	 * Catalog Section Tiles — one block per visible Launch Mode root.
	 */
	public function buildCatalogSectionTileBlocks($controller) {
		if (!$this->isLaunchMode()) {
			return array();
		}

		$controller->load->model('catalog/category');
		$controller->load->model('catalog/product');
		$controller->load->model('tool/image');

		$sections = array();

		foreach ($this->getVisibleRootCategoryIds() as $root_id) {
			$root = $controller->model_catalog_category->getCategory((int)$root_id);

			if (!$root) {
				continue;
			}

			$cards = $this->buildHubChildCards($controller, $root_id);

			if (empty($cards)) {
				continue;
			}

			$sections[] = array(
				'category_id' => (int)$root_id,
				'name'        => $root['name'],
				'href'        => $controller->url->link('product/katalog', 'path=' . $this->buildCategoryPathParam($controller, (int)$root_id)),
				'img'         => $this->resizeCategoryImage($controller, isset($root['image']) ? $root['image'] : ''),
				'cards'       => $this->markFirstActive($cards),
			);
		}

		return $sections;
	}

	/**
	 * M9.7E — homepage category section cards (flat list for BC).
	 * Prefer buildCatalogSectionTileBlocks() for multi-root Catalog Section Tiles.
	 */
	public function buildHomepageCategoryCards($controller) {
		$flat = array();

		foreach ($this->buildCatalogSectionTileBlocks($controller) as $section) {
			if (empty($section['cards']) || !is_array($section['cards'])) {
				continue;
			}

			foreach ($section['cards'] as $card) {
				$flat[] = $card;
			}
		}

		return $this->markFirstActive($flat);
	}

	/**
	 * Ensure root catlist rows used on /katalog have thumb300 + placeholder fallback.
	 */
	public function enrichRootCategoryThumbs(array $categories, $controller) {
		$controller->load->model('catalog/category');
		$controller->load->model('tool/image');

		foreach ($categories as $key => $category) {
			if (empty($category['category_id'])) {
				continue;
			}

			$branch = $controller->model_catalog_category->getCategory((int)$category['category_id']);
			$image = ($branch && !empty($branch['image'])) ? $branch['image'] : '';

			$categories[$key]['thumb300'] = $this->resizeCategoryImage($controller, $image, 300, 300);
			$categories[$key]['img'] = $categories[$key]['thumb300'];

			if (empty($categories[$key]['thumb'])) {
				$categories[$key]['thumb'] = $this->resizeCategoryImage($controller, $image, 160, 160);
			}

			if (empty($categories[$key]['thumb200'])) {
				$categories[$key]['thumb200'] = $this->resizeCategoryImage($controller, $image, 200, 200);
			}
		}

		return $categories;
	}

	/**
	 * M9.7C — enrich megamenu children with live product counts and thumb300;
	 * drop branches with zero active products (visibility only).
	 */
	public function prepareMegamenuCategories(array $categories, $controller) {
		$controller->load->model('catalog/category');
		$controller->load->model('catalog/product');
		$controller->load->model('tool/image');

		foreach ($categories as $key => $category) {
			if (empty($category['children']) || !is_array($category['children'])) {
				continue;
			}

			$children = array();

			foreach ($category['children'] as $child) {
				if (empty($child['category_id'])) {
					continue;
				}

				$filter_data = array(
					'filter_category_id'  => (int)$child['category_id'],
					'filter_sub_category' => true
				);

				$count = (int)$controller->model_catalog_product->getTotalProducts($filter_data);

				if ($count <= 0) {
					continue;
				}

				$branch = $controller->model_catalog_category->getCategory((int)$child['category_id']);
				$image = ($branch && !empty($branch['image'])) ? $branch['image'] : '';

				$child['thumb300'] = $this->resizeCategoryImage($controller, $image, 300, 300);
				$child['count'] = $count;
				$children[] = $child;
			}

			$children = $this->sortCategoriesByRussianName($children);

			$categories[$key]['children'] = $children;
			$categories[$key]['has_children'] = !empty($children);
		}

		return $categories;
	}

	public function applyCatalogNavData(array &$data) {
		$data['catalog_primary_entry'] = $this->getPrimaryCatalogEntry();
		$data['launch_mode'] = $this->isLaunchMode();

		if (!empty($data['categories']) && is_array($data['categories'])) {
			$data['categories'] = $this->filterRootCategories($data['categories']);
		}

		if (!empty($data['catlist']) && is_array($data['catlist'])) {
			$data['catlist'] = $this->filterRootCategories($data['catlist']);
		}

		if (!empty($data['catDesktop']) && is_array($data['catDesktop'])) {
			$data['catDesktop'] = $this->filterRootCategories($data['catDesktop']);
		}
	}
}
