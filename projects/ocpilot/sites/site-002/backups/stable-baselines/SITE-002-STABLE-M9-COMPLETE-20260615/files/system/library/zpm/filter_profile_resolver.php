<?php
/**
 * BZPM M9 — category filter profile resolver (Phase 3: profiles 80, 207, 301, 322, 326).
 *
 * Static allowlist per branch; no dynamic visibility (M10), no subcategory overrides (ROAD-004).
 */
class FilterProfileResolver {
	const TIER_PRIMARY = 'PRIMARY';
	const TIER_SECONDARY = 'SECONDARY';
	const TIER_HIDDEN = 'HIDDEN';

	/** @var object|null */
	private $db;

	/** @var int[] */
	private $registered_branch_roots = array(80, 207, 301, 322, 326);

	/** @var array<int,string> */
	private $profile_file_map = array(
		80 => '80_moechnye_vanny.php',
		207 => '207_zonty.php',
		301 => '301_stoly.php',
		322 => '322_podtovarniki.php',
		326 => '326_telezhki.php',
	);

	/** @var array|null */
	private $global_hidden_ids;

	public function __construct($db = null) {
		$this->db = $db;
	}

	/**
	 * @return int[]
	 */
	public function getGlobalHiddenIds() {
		if ($this->global_hidden_ids === null) {
			$this->global_hidden_ids = require(DIR_SYSTEM . 'library/zpm/filter_profiles/global_hidden.php');
		}

		return $this->global_hidden_ids;
	}

	/**
	 * Resolve active branch profile for PLP category (self or ancestor match).
	 *
	 * @param int $category_id
	 * @return array|null
	 */
	public function resolveForCategory($category_id) {
		$profile_id = $this->findActiveProfileId((int)$category_id);

		if (!$profile_id) {
			return null;
		}

		return $this->loadProfile($profile_id);
	}

	/**
	 * @param int $category_id
	 * @return int|null
	 */
	public function findActiveProfileId($category_id) {
		$category_id = (int)$category_id;

		if ($category_id <= 0) {
			return null;
		}

		foreach ($this->registered_branch_roots as $root_id) {
			if ($category_id === (int)$root_id) {
				return (int)$root_id;
			}

			if ($this->db && $this->isUnderBranchRoot($category_id, (int)$root_id)) {
				return (int)$root_id;
			}
		}

		return null;
	}

	/**
	 * @param int $category_id
	 * @param int $root_id
	 * @return bool
	 */
	private function isUnderBranchRoot($category_id, $root_id) {
		$query = $this->db->query(
			"SELECT COUNT(*) AS total FROM " . DB_PREFIX . "category_path "
			. "WHERE category_id = '" . (int)$category_id . "' AND path_id = '" . (int)$root_id . "'"
		);

		return !empty($query->row['total']);
	}

	/**
	 * @param int $profile_id
	 * @return array|null
	 */
	public function loadProfile($profile_id) {
		$profile_id = (int)$profile_id;

		if (!isset($this->profile_file_map[$profile_id])) {
			return null;
		}

		$file = DIR_SYSTEM . 'library/zpm/filter_profiles/' . $this->profile_file_map[$profile_id];

		if (!is_file($file)) {
			return null;
		}

		$profile = require($file);
		$profile['hidden_global_ids'] = $this->getGlobalHiddenIds();

		return $profile;
	}

	/**
	 * @param array $profile
	 * @param int $attribute_id
	 * @return bool
	 */
	public function isHiddenAttribute($profile, $attribute_id) {
		$attribute_id = (int)$attribute_id;
		$allowed = array_merge(
			(array)$profile['primary_attribute_ids'],
			(array)$profile['secondary_attribute_ids']
		);

		// Branch allowlist wins over global hidden (INH-04 — e.g. attr 34 on zonty).
		if (in_array($attribute_id, $allowed, true)) {
			return false;
		}

		$hidden = array_merge(
			(array)$profile['hidden_global_ids'],
			(array)$profile['hidden_attribute_ids']
		);

		if (in_array($attribute_id, $hidden, true)) {
			return true;
		}

		return true;
	}

	/**
	 * @param array $profile
	 * @param int $attribute_id
	 * @return string|null PRIMARY|SECONDARY|null when hidden
	 */
	public function getAttributeTier($profile, $attribute_id) {
		$attribute_id = (int)$attribute_id;

		if ($this->isHiddenAttribute($profile, $attribute_id)) {
			return null;
		}

		if (in_array($attribute_id, (array)$profile['primary_attribute_ids'], true)) {
			return self::TIER_PRIMARY;
		}

		if (in_array($attribute_id, (array)$profile['secondary_attribute_ids'], true)) {
			return self::TIER_SECONDARY;
		}

		return null;
	}

	/**
	 * @param array $profile
	 * @param int $attribute_id
	 * @return int
	 */
	public function getAttributeSort($profile, $attribute_id, $tier) {
		$attribute_id = (int)$attribute_id;

		if ($tier === self::TIER_PRIMARY && !empty($profile['primary_sort'][$attribute_id])) {
			return (int)$profile['primary_sort'][$attribute_id];
		}

		if ($tier === self::TIER_SECONDARY && !empty($profile['secondary_sort'][$attribute_id])) {
			return (int)$profile['secondary_sort'][$attribute_id];
		}

		return 999;
	}

	/**
	 * Filter discovered attributes to profile allowlist; attach tier + sort metadata.
	 *
	 * @param array $profile
	 * @param array $attribute_data
	 * @return array
	 */
	public function applyProfileToAttributes($profile, $attribute_data) {
		$filtered = array();

		foreach ($attribute_data as $key => $attribute) {
			$attribute_id = (int)$attribute['attribute_id'];
			$tier = $this->getAttributeTier($profile, $attribute_id);

			if ($tier === null) {
				continue;
			}

			$attribute['tier'] = $tier;
			$attribute['sort_order'] = $this->getAttributeSort($profile, $attribute_id, $tier);
			$filtered[$key] = $attribute;
		}

		uasort($filtered, function ($a, $b) {
			$tier_order = array(
				self::TIER_PRIMARY => 0,
				self::TIER_SECONDARY => 1,
			);
			$a_tier = isset($tier_order[$a['tier']]) ? $tier_order[$a['tier']] : 9;
			$b_tier = isset($tier_order[$b['tier']]) ? $tier_order[$b['tier']] : 9;

			if ($a_tier !== $b_tier) {
				return $a_tier - $b_tier;
			}

			$a_sort = isset($a['sort_order']) ? (int)$a['sort_order'] : 999;
			$b_sort = isset($b['sort_order']) ? (int)$b['sort_order'] : 999;

			if ($a_sort !== $b_sort) {
				return $a_sort - $b_sort;
			}

			return strcmp((string)$a['name'], (string)$b['name']);
		});

		return $filtered;
	}
}
