<?php
class ModelBlogBlog extends Model {

	/* --- Методы для КАТЕГОРИЙ (Разделов) --- */

	public function getCategory($category_id) {
		$query = $this->db->query("SELECT * FROM " . DB_PREFIX . "blog_themes WHERE id = '" . (int)$category_id . "' AND active = '1'");
		return $query->row;
	}

	public function getCategories() {
		$query = $this->db->query("SELECT * FROM " . DB_PREFIX . "blog_themes WHERE active = '1' ORDER BY name ASC");
		return $query->rows;
	}

	/* --- Методы для ПОСТОВ --- */

	public function getPost($post_id) {
		$query = $this->db->query("SELECT * FROM " . DB_PREFIX . "blog_posts WHERE id = '" . (int)$post_id . "' AND active = '1' AND date_added <= NOW()");
		return $query->row;
	}

	public function getPosts($data = array()) {
		// Добавляем выборку p.* (все поля поста) и t.name (название категории)
		$sql = "SELECT p.*, t.name AS category_name 
				FROM " . DB_PREFIX . "blog_posts p 
				LEFT JOIN " . DB_PREFIX . "blog_themes t ON (p.category_id = t.id) 
				WHERE p.active = '1' AND p.date_added <= NOW()";

		if (!empty($data['filter_category_id'])) {
			$sql .= " AND p.category_id = '" . (int)$data['filter_category_id'] . "'";
		}

		$sql .= " ORDER BY p.date_added DESC";

		if (isset($data['start']) || isset($data['limit'])) {
			if ($data['start'] < 0) $data['start'] = 0;
			if ($data['limit'] < 1) $data['limit'] = 10;
			$sql .= " LIMIT " . (int)$data['start'] . "," . (int)$data['limit'];
		}

		$query = $this->db->query($sql);
		return $query->rows;
	}

	public function getTotalPosts($data = array()) {
		$sql = "SELECT COUNT(*) AS total FROM " . DB_PREFIX . "blog_posts WHERE active = '1' AND date_added <= NOW()";

		if (!empty($data['filter_category_id'])) {
			$sql .= " AND category_id = '" . (int)$data['filter_category_id'] . "'";
		}

		$query = $this->db->query($sql);
		return $query->row['total'];
	}

	// Метод для обновления счетчика просмотров
	public function updateViews($post_id) {
		$this->db->query("UPDATE " . DB_PREFIX . "blog_posts SET views = (views + 1) WHERE id = '" . (int)$post_id . "'");
	}


 	// Выбираем случайные статьи (ORDER BY RAND()), активные, из той же категории
	public function getOtherPosts($category_id, $post_id = 0, $limit = 6) {   
    // Исключаем текущий ID поста, если он передан
    $sql = "SELECT p.*, t.name AS category_name 
            FROM " . DB_PREFIX . "blog_posts p 
            LEFT JOIN " . DB_PREFIX . "blog_themes t ON (p.category_id = t.id) 
            WHERE p.active = '1' AND p.date_added <= NOW() AND p.category_id = '" . (int)$category_id . "'";

    if ($post_id) {
        $sql .= " AND p.id <> '" . (int)$post_id . "'";
    }

    $sql .= " ORDER BY RAND() LIMIT " . (int)$limit;

    $query = $this->db->query($sql);
    return $query->rows;
	}
}
