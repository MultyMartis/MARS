<?php
/**
 * BZPM Launch Mode — unified category visibility layer (M7.1).
 * M9.5 — neutral root hub branch list for category 79.
 * M9.7C — megamenu children historically filtered to categories with active products only.
 * M9.7E — homepage category section uses neutral hub branches
 * SITE-002-PROD-PARENT-CATEGORY-TILES-LARI-REMOVAL-01 — removed ID 88 from parent tiles whitelist (not launch root card).
 * SITE-002-PROD-CATALOG-TILE-BLOCKS-AUTOMATION-01 — Catalog Section Tiles / Плитки разделов каталога:
 *   peer root Технологическое оборудование (362); multi-section tile blocks; placeholder fallback.
 * SITE-002-PROD-MEGAMENU-CHILDREN-AUTOMATION-01 — mega menu children rebuilt DB-driven to match Catalog Section Tiles
 *   (neutral keeps product gate; other section hubs include empty active children).
 * SITE-002-PROD-FIRST-LEVEL-BLOCK-HYBRID-APPLY-01 — HYBRID Neutral first-level block (superseded by ALL15 correction).
 * SITE-002-PROD-FIRST-LEVEL-BLOCK-ALL15-CORRECTION-APPLY-01 — ALL-15 Neutral first-level block (home+/katalog):
 *   all 15 direct children of 79; (historical) empty copy on zero-product tiles;
 *   mega/buildHubChildCards product gate unchanged; Tech 362 unchanged.
 * SITE-002-PROD-EMPTY-CATEGORY-COPY-RELOCATE-AND-NEW-FIRSTLEVEL-IMAGES-01 — empty copy moved to category PLP only;
 *   first-level tiles keep ALL-15 without card empty-copy; images for empty 82/83/85/87/89.
 * SITE-002-CATALOG-NORMALIZATION-UI-REPAIR-01 — post-normalization public catalog UI:
 *   8 approved public roots on home + /katalog/; Neutral children no longer replace root catalog block;
 *   tmp/disabled roots hidden; mega menu roots aligned to approved model.
 *
 * Single source of truth for Launch Mode navigation and /katalog presentation.
 * Controllers must use this class; do not hardcode visibility rules in Twig.
 */
class CategoryVisibility {
	const LAUNCH_MODE = true;
	const CATALOG_PRIMARY_ENTRY = '/katalog/';
	const ACTIVE_LAUNCH_ROOT = 'nejtralnoe-oborudovanie';
	/** @deprecated use getVisibleRootCategoryIds(); kept for older call sites */
	const VISIBLE_ROOT_CATEGORY_ID = 79;
	const NEUTRAL_HUB_CATEGORY_ID = 79;
	const TECHNOLOGICAL_HUB_CATEGORY_ID = 362;
	const PLACEHOLDER_IMAGE = 'placeholder.png';
	/** Empty category PLP caption when the opened category has zero products. */
	const EMPTY_FIRST_LEVEL_COPY = 'Ожидайте, товары скоро поступят.';

	/** Approved public root categories after SITE-002 catalog normalization. */
	private static $visible_root_category_ids = array(79, 95, 90, 186, 375, 373, 364, 381);

	private static $visible_root_slugs = array(
		'nejtralnoe-oborudovanie',
		'holodilnoe-oborudovanie',
		'teplovoe-oborudovanie',
		'hlebopekarnoe-oborudovanie',
		'elektromehanicheskoe',
		'myasopererabatyvayuschee',
		'posuda-i-inventar',
		'upakovochnoe-oborudovanie',
	);

	private static $hidden_root_slugs = array(
		'tmp-tehnologicheskoe-oborudovanie',
		'tmp-inventar',
		'tmp-barnoe-oborudovanie',
		'tmp-posudomoechnye-mashiny',
		'tmp-ventilyacionnoe-oborudovanie',
		'tehnologicheskoe-oborudovanie',
		'inventar',
		'barnoe-oborudovanie',
		'posudomoechnye-mashiny',
		'ventilyacionnoe-oborudovanie',
		'elektromehanicheskoe-oborudovanie',
		'zapchasti',
	);

	/** ALL-15 Neutral first-level Catalog Section Tiles (home + /katalog/) — direct children of 79. */
	private static $neutral_hub_branch_ids = array(80, 82, 83, 85, 86, 87, 89, 207, 301, 322, 326, 331, 354, 358, 360);

	/** No Neutral first-level IDs hidden in Catalog Section Tiles after ALL15 correction. */
	private static $neutral_first_level_hide_wait_ids = array();

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

	public function getNeutralFirstLevelHideWaitIds() {
		return self::$neutral_first_level_hide_wait_ids;
	}

	public function getEmptyFirstLevelCopy() {
		return self::EMPTY_FIRST_LEVEL_COPY;
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

		if ($slug !== '' && in_array($slug, self::$hidden_root_slugs, true)) {
			return false;
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

	private function buildCardFromCategory($controller, $branch_id, $branch, $require_products, $attach_empty_copy = false) {
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

		$card = array(
			'category_id' => $branch_id,
			'name'        => $branch['name'],
			'href'        => $controller->url->link('product/katalog', 'path=' . $this->buildCategoryPathParam($controller, $branch_id)),
			'img'         => $this->resizeCategoryImage($controller, isset($branch['image']) ? $branch['image'] : ''),
			'thumb300'    => $this->resizeCategoryImage($controller, isset($branch['image']) ? $branch['image'] : ''),
			'count'       => $count,
			'empty_copy'  => '',
			'show_empty_copy' => false,
		);

		if ($attach_empty_copy && $count <= 0) {
			$card['empty_copy'] = self::EMPTY_FIRST_LEVEL_COPY;
			$card['show_empty_copy'] = true;
		}

		return $card;
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
	 * ALL-15 Neutral first-level cards for Catalog Section Tiles only (home + /katalog/).
	 * Show all 15 direct children of 79, including zero-product cards.
	 * Empty-state copy is NOT attached to tiles — it belongs on the category PLP only
	 * (SITE-002-PROD-EMPTY-CATEGORY-COPY-RELOCATE-AND-NEW-FIRSTLEVEL-IMAGES-01).
	 * Mega menu continues to use buildHubChildCards() with Neutral product gate.
	 */
	public function buildNeutralFirstLevelBlockCards($controller) {
		$controller->load->model('catalog/category');
		$controller->load->model('catalog/product');
		$controller->load->model('tool/image');

		$cards = array();
		$hide = self::$neutral_first_level_hide_wait_ids;

		foreach ($this->getNeutralHubBranchIds() as $branch_id) {
			$branch_id = (int)$branch_id;

			if (in_array($branch_id, $hide, true)) {
				continue;
			}

			$branch = $controller->model_catalog_category->getCategory($branch_id);
			$card = $this->buildCardFromCategory($controller, $branch_id, $branch, false, false);

			if ($card) {
				$cards[] = $card;
			}
		}

		return $this->sortCategoriesByRussianName($cards);
	}

	/**
	 * Catalog Section Tiles — single block with approved public root categories (home + /katalog/).
	 * Neutral first-level children are shown on the Neutral hub page / mega menu only.
	 */
	public function buildCatalogSectionTileBlocks($controller) {
		if (!$this->isLaunchMode()) {
			return array();
		}

		$controller->load->model('catalog/category');
		$controller->load->model('catalog/product');
		$controller->load->model('tool/image');

		$cards = array();

		foreach ($this->getVisibleRootCategoryIds() as $root_id) {
			$root = $controller->model_catalog_category->getCategory((int)$root_id);

			if (!$root || !isset($root['status']) || (int)$root['status'] !== 1) {
				continue;
			}

			$card = $this->buildCardFromCategory($controller, (int)$root_id, $root, false);

			if ($card) {
				$cards[] = $card;
			}
		}

		$cards = $this->sortCategoriesByRussianName($cards);

		if (empty($cards)) {
			return array();
		}

		return array(
			array(
				'category_id' => 0,
				'name'        => 'Каталог оборудования',
				'href'        => $controller->url->link('product/katalog'),
				'img'         => '',
				'cards'       => $this->markFirstActive($cards),
			),
		);
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
	 * Mega menu children — DB-driven parity with Catalog Section Tiles.
	 *
	 * SITE-002-PROD-MEGAMENU-CHILDREN-AUTOMATION-01:
	 * Rebuild direct children from DB (do not trust partial cat-list-header rows).
	 * Neutral hub (79): curated whitelist + require products (same as buildHubChildCards).
	 * Other section hubs (362+): all active direct children, including zero-product hubs.
	 * Non-hub roots: keep legacy product-count gate on cached children.
	 */
	public function prepareMegamenuCategories(array $categories, $controller) {
		$controller->load->model('catalog/category');
		$controller->load->model('catalog/product');
		$controller->load->model('tool/image');

		foreach ($categories as $key => $category) {
			if (empty($category['category_id'])) {
				continue;
			}

			$root_id = (int)$category['category_id'];
			$children = array();

			if ($this->isSectionHubCategory($root_id)) {
				$cards = $this->buildHubChildCards($controller, $root_id);

				foreach ($cards as $card) {
					$branch_id = (int)$card['category_id'];
					$image = '';

					$branch = $controller->model_catalog_category->getCategory($branch_id);

					if ($branch && !empty($branch['image'])) {
						$image = $branch['image'];
					}

					$children[] = array(
						'category_id'  => $branch_id,
						'name'         => $card['name'],
						'href'         => $card['href'],
						'thumb'        => $this->resizeCategoryImage($controller, $image, 160, 160),
						'thumb200'     => $this->resizeCategoryImage($controller, $image, 200, 200),
						'thumb300'     => !empty($card['thumb300']) ? $card['thumb300'] : $this->resizeCategoryImage($controller, $image, 300, 300),
						'count'        => isset($card['count']) ? (int)$card['count'] : 0,
						'has_children' => false,
					);
				}
			} else {
				if (empty($category['children']) || !is_array($category['children'])) {
					continue;
				}

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
			}

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
