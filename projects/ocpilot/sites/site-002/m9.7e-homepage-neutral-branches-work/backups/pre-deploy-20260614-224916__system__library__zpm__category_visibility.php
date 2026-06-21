<?php
/**
 * BZPM Launch Mode — unified category visibility layer (M7.1).
 * M9.5 — neutral root hub branch list for category 79.
 * M9.7C — megamenu children filtered to categories with active products only.
 *
 * Single source of truth for Launch Mode navigation and /katalog presentation.
 * Controllers must use this class; do not hardcode visibility rules in Twig.
 */
class CategoryVisibility {
	const LAUNCH_MODE = true;
	const CATALOG_PRIMARY_ENTRY = '/katalog/nejtralnoe-oborudovanie';
	const ACTIVE_LAUNCH_ROOT = 'nejtralnoe-oborudovanie';
	const VISIBLE_ROOT_CATEGORY_ID = 79;
	const NEUTRAL_HUB_CATEGORY_ID = 79;

	private static $visible_root_slugs = array(
		'nejtralnoe-oborudovanie',
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

	/** Commercial priority order for neutral hub branch cards (M9.5). */
	private static $neutral_hub_branch_ids = array(301, 80, 322, 207, 326);

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

	public function getHiddenRootSlugs() {
		return self::$hidden_root_slugs;
	}

	public function isNeutralHubCategory($category_id) {
		return (int)$category_id === self::NEUTRAL_HUB_CATEGORY_ID;
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

		return '';
	}

	public function isVisibleRootCategory($category) {
		if (!$this->isLaunchMode()) {
			return true;
		}

		if (!is_array($category)) {
			return false;
		}

		if (isset($category['category_id']) && (int)$category['category_id'] === self::VISIBLE_ROOT_CATEGORY_ID) {
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

				if ($branch && !empty($branch['image'])) {
					$child['thumb300'] = $controller->model_tool_image->resize($branch['image'], 300, 300);
				} else {
					$child['thumb300'] = $controller->model_tool_image->resize('placeholder.png', 300, 300);
				}

				$child['count'] = $count;
				$children[] = $child;
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
