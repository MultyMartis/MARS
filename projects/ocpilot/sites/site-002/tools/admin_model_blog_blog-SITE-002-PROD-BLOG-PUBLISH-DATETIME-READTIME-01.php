<?php
class ModelBlogBlog extends Model {

	/**
	 * Reading time: strip HTML, decode entities, normalize whitespace,
	 * count Unicode characters (mb_strlen UTF-8), divide by CHARS_PER_MINUTE.
	 * Constant: 1500 characters per minute.
	 */
	public function calculateReadingTimeMinutes($html) {
		$text = (string)$html;
		$text = preg_replace('/(?is)<script[^>]*>.*?<\/script>/', ' ', $text);
		$text = preg_replace('/(?is)<style[^>]*>.*?<\/style>/', ' ', $text);
		$text = strip_tags($text);
		$text = html_entity_decode($text, ENT_QUOTES, 'UTF-8');
		$text = preg_replace('/\s+/u', ' ', $text);
		$text = trim($text);
		$chars = mb_strlen($text, 'UTF-8');
		$chars_per_minute = 1500; // SITE-002 reading-time constant
		$minutes = (int)max(1, (int)ceil($chars / $chars_per_minute));
		return $minutes;
	}

	protected function normalizePublishDatetime($value) {
		$value = trim((string)$value);
		if ($value === '') {
			return '';
		}
		// HTML5 datetime-local: YYYY-MM-DDTHH:MM
		$value = str_replace('T', ' ', $value);
		$ts = strtotime($value);
		if ($ts === false) {
			return '';
		}
		return date('Y-m-d H:i:00', $ts);
	}


	/* --- Методы для КАТЕГОРИЙ (Themes) --- */

	public function addCategory($data) {
		$this->db->query("INSERT INTO " . DB_PREFIX . "blog_themes SET 
            name = '" . $this->db->escape($data['name']) . "', 
            active = '" . (int)$data['active'] . "'");

		$category_id = $this->db->getLastId();

		// Работа с SEO URL
		if (isset($data['keyword'])) {
			$this->db->query("INSERT INTO " . DB_PREFIX . "seo_url SET 
                store_id = '0', 
                language_id = '" . (int)$this->config->get('config_language_id') . "', 
                query = 'blog_category_id=" . (int)$category_id . "', 
                keyword = '" . $this->db->escape($data['keyword']) . "'");
		}

		return $category_id;
	}

	public function editCategory($category_id, $data) {
		$this->db->query("UPDATE " . DB_PREFIX . "blog_themes SET 
            name = '" . $this->db->escape($data['name']) . "', 
            active = '" . (int)$data['active'] . "' 
            WHERE id = '" . (int)$category_id . "'");

		// Обновляем SEO URL: сначала удаляем старый, потом пишем новый
		$this->db->query("DELETE FROM " . DB_PREFIX . "seo_url WHERE query = 'blog_category_id=" . (int)$category_id . "'");

		if (!empty($data['keyword'])) {
			$this->db->query("INSERT INTO " . DB_PREFIX . "seo_url SET 
                store_id = '0', 
                language_id = '" . (int)$this->config->get('config_language_id') . "', 
                query = 'blog_category_id=" . (int)$category_id . "', 
                keyword = '" . $this->db->escape($data['keyword']) . "'");
		}
	}

	public function deleteCategory($category_id) {
		$this->db->query("DELETE FROM " . DB_PREFIX . "blog_themes WHERE id = '" . (int)$category_id . "'");
		$this->db->query("DELETE FROM " . DB_PREFIX . "seo_url WHERE query = 'blog_category_id=" . (int)$category_id . "'");
	}

	public function getCategory($category_id) {
		$query = $this->db->query("SELECT DISTINCT *, (SELECT keyword FROM " . DB_PREFIX . "seo_url WHERE query = 'blog_category_id=" . (int)$category_id . "' LIMIT 1) AS keyword FROM " . DB_PREFIX . "blog_themes WHERE id = '" . (int)$category_id . "'");
		return $query->row;
	}

	public function getCategories() {
		$query = $this->db->query("SELECT * FROM " . DB_PREFIX . "blog_themes ORDER BY name ASC");
		return $query->rows;
	}


	/* --- Методы для ПОСТОВ (Posts) --- */
	public function addPost($data) {

		$date = 'NOW()';
		if (isset($data['modified']) && $data['modified'] != '') {
			$normalized = $this->normalizePublishDatetime($data['modified']);
			if ($normalized !== '') {
				$date = "'" . $this->db->escape($normalized) . "'";
			}
		}

		$reading_time_minutes = $this->calculateReadingTimeMinutes(isset($data['content']) ? $data['content'] : '');

		$this->db->query("INSERT INTO " . DB_PREFIX . "blog_posts SET 
            category_id = '" . (int)$data['category_id'] . "', 
            title = '" . $this->db->escape($data['title']) . "', 
            short_description = '" . $this->db->escape($data['short_description']) . "', 
            content = '" . $this->db->escape($data['content']) . "', 
            reading_time_minutes = '" . (int)$reading_time_minutes . "',
            image = '" . $this->db->escape($data['image']) . "', 
            active = '" . (int)$data['active'] . "', 
            meta_title = '" . $this->db->escape($data['meta_title']) . "', 
            meta_description = '" . $this->db->escape($data['meta_description']) . "', 
            meta_keyword = '" . $this->db->escape($data['meta_keyword']) . "', 
            date_added = ".$date);

		$post_id = $this->db->getLastId();

		if (isset($data['keyword'])) {
			$this->db->query("INSERT INTO " . DB_PREFIX . "seo_url SET 
                store_id = '0', 
                language_id = '" . (int)$this->config->get('config_language_id') . "', 
                query = 'blog_post_id=" . (int)$post_id . "', 
                keyword = '" . $this->db->escape($data['keyword']) . "'");
		}

		return $post_id;
	}

	public function editPost($post_id, $data) {
		
		$date = '';
		if (isset($data['modified']) && $data['modified'] != '') {
			$normalized = $this->normalizePublishDatetime($data['modified']);
			if ($normalized !== '') {
				$date = ", date_added = '" . $this->db->escape($normalized) . "'";
			}
		}

		$reading_time_minutes = $this->calculateReadingTimeMinutes(isset($data['content']) ? $data['content'] : '');

		$this->db->query("UPDATE " . DB_PREFIX . "blog_posts SET 
            category_id = '" . (int)$data['category_id'] . "', 
            title = '" . $this->db->escape($data['title']) . "', 
            short_description = '" . $this->db->escape($data['short_description']) . "', 
            content = '" . $this->db->escape($data['content']) . "', 
            reading_time_minutes = '" . (int)$reading_time_minutes . "',
            image = '" . $this->db->escape($data['image']) . "', 
            active = '" . (int)$data['active'] . "', 
            meta_title = '" . $this->db->escape($data['meta_title']) . "', 
            meta_description = '" . $this->db->escape($data['meta_description']) . "', 
            meta_keyword = '" . $this->db->escape($data['meta_keyword']) . "'".
			$date. 
            " WHERE id = '" . (int)$post_id . "'");

		$this->db->query("DELETE FROM " . DB_PREFIX . "seo_url WHERE query = 'blog_post_id=" . (int)$post_id . "'");

		if (!empty($data['keyword'])) {
			$this->db->query("INSERT INTO " . DB_PREFIX . "seo_url SET 
                store_id = '0', 
                language_id = '" . (int)$this->config->get('config_language_id') . "', 
                query = 'blog_post_id=" . (int)$post_id . "', 
                keyword = '" . $this->db->escape($data['keyword']) . "'");
		}
	}

	public function deletePost($post_id) {
		$this->db->query("DELETE FROM " . DB_PREFIX . "blog_posts WHERE id = '" . (int)$post_id . "'");
		$this->db->query("DELETE FROM " . DB_PREFIX . "seo_url WHERE query = 'blog_post_id=" . (int)$post_id . "'");
	}

	public function getPost($post_id) {
		$query = $this->db->query("SELECT DISTINCT *, (SELECT keyword FROM " . DB_PREFIX . "seo_url WHERE query = 'blog_post_id=" . (int)$post_id . "' LIMIT 1) AS keyword FROM " . DB_PREFIX . "blog_posts WHERE id = '" . (int)$post_id . "'");
		return $query->row;
	}

	public function getPosts($data = array()) {
		$sql = "SELECT p.*, t.name AS category_name FROM " . DB_PREFIX . "blog_posts p LEFT JOIN " . DB_PREFIX . "blog_themes t ON (p.category_id = t.id)";

		$sql .= " ORDER BY p.date_added DESC";

		if (isset($data['start']) || isset($data['limit'])) {
			if ($data['start'] < 0) $data['start'] = 0;
			if ($data['limit'] < 1) $data['limit'] = 20;
			$sql .= " LIMIT " . (int)$data['start'] . "," . (int)$data['limit'];
		}

		$query = $this->db->query($sql);
		return $query->rows;
	}

	public function getTotalPosts() {
		$query = $this->db->query("SELECT COUNT(*) AS total FROM " . DB_PREFIX . "blog_posts");
		return $query->row['total'];
	}
}