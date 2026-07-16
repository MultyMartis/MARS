<?php // ==========================================  seo_url.php v.140618 opencart-russia.ru ===============================
class ControllerStartupSeoUrl extends Controller {
	public function index() {
		// Add rewrite to url class
		if ($this->config->get('config_seo_url')) {
			$this->url->addRewrite($this);
		}

		// Decode URL
		if (isset($this->request->get['_route_'])) {
			$blog_resolved = false;
			// SITE-002 blog SEO: keywords are stored as multi-segment paths
			// (e.g. blog/news, blog/news/{slug}) — not per-segment like categories.
			// Active startup is seo_url (not seo_pro); resolve full path first.
			$full_keyword = trim((string)$this->request->get['_route_'], '/');
			if ($full_keyword !== '' && strpos($full_keyword, '/') !== false) {
				$query = $this->db->query("SELECT * FROM " . DB_PREFIX . "seo_url WHERE keyword = '" . $this->db->escape($full_keyword) . "' AND store_id = '" . (int)$this->config->get('config_store_id') . "'");

				if ($query->num_rows) {
					$url = explode('=', $query->row['query'], 2);

					if ($url[0] == 'blog_post_id' && isset($url[1])) {
						$this->request->get['blog_post_id'] = $url[1];
						$this->request->get['route'] = 'blog/post';
						$blog_resolved = true;
					} elseif ($url[0] == 'blog_category_id' && isset($url[1])) {
						$this->request->get['blog_category_id'] = $url[1];
						$this->request->get['route'] = 'blog/category';
						$blog_resolved = true;
					}
				}
			}

			if (!$blog_resolved) {
			$parts = explode('/', $this->request->get['_route_']);

			// remove any empty arrays from trailing
			if (utf8_strlen(end($parts)) == 0) {
				array_pop($parts);
			}

			foreach ($parts as $part) {
				if ($part === 'payment-methods') {
					$this->request->get['route'] = 'information/payment';
					continue;
				}

				$query = $this->db->query("SELECT * FROM " . DB_PREFIX . "seo_url WHERE keyword = '" . $this->db->escape($part) . "' AND store_id = '" . (int)$this->config->get('config_store_id') . "'");

				if ($query->num_rows) {
					$url = explode('=', $query->row['query']);

					if ($url[0] == 'product_id') {
						$this->request->get['product_id'] = $url[1];
					}

					if ($url[0] == 'category_id') {
						if (!isset($this->request->get['path'])) {
							$this->request->get['path'] = $url[1];
						} else {
							$this->request->get['path'] .= '_' . $url[1];
						}
					}

					if ($url[0] == 'manufacturer_id') {
						$this->request->get['manufacturer_id'] = $url[1];
					}

					if ($url[0] == 'information_id') {
						$this->request->get['information_id'] = $url[1];
					}

					if ($query->row['query'] && $url[0] != 'information_id' && $url[0] != 'manufacturer_id' && $url[0] != 'category_id' && $url[0] != 'product_id') {
						$this->request->get['route'] = $query->row['query'];
					}
				} else {
					$this->request->get['route'] = 'error/not_found';

					break;
				}
			}
			}

			if (!isset($this->request->get['route'])) {
				if (isset($this->request->get['product_id'])) {
					$this->request->get['route'] = 'product/product';
				} elseif (isset($this->request->get['path'])) {
					$this->request->get['route'] = 'product/category';
				} elseif (isset($this->request->get['manufacturer_id'])) {
					$this->request->get['route'] = 'product/manufacturer/info';
				} elseif (isset($this->request->get['information_id'])) {
					$this->request->get['route'] = 'information/information';
				} elseif (isset($this->request->get['blog_post_id'])) {
					$this->request->get['route'] = 'blog/post';
				} elseif (isset($this->request->get['blog_category_id'])) {
					$this->request->get['route'] = 'blog/category';
				}
			}

			// SITE-002 category_path canonical v2 (SITE-002-PROD-CATEGORY-LARI-REPARENT-IMPLEMENTATION-01)
			if (!empty($this->request->get['path'])) {
				$canonical_ids = $this->site002CanonicalCategoryPath($this->request->get['path']);
				if ($canonical_ids) {
					$this->request->get['path'] = implode('_', $canonical_ids);
				}
				if (!empty($this->request->get['path']) && isset($this->request->get['route']) && $this->request->get['route'] == 'product/katalog') {
					$this->request->get['route'] = 'product/category';
				}
			}
		// Redirect 301   
		} elseif (isset($this->request->get['route']) && empty($this->request->post) && !isset($this->request->get['token']) && $this->config->get('config_seo_url')) {
			$arg = '';
			$cat_path = false;
			$route = $this->request->get['route'];

			if ($this->request->get['route'] == 'product/product' && isset($this->request->get['product_id'])) {
				$route = 'product_id=' . (int)$this->request->get['product_id'];
			} elseif ($this->request->get['route'] == 'product/category' && isset($this->request->get['path'])) {
				$canonical_ids = $this->site002CanonicalCategoryPath($this->request->get['path']);
				if ($canonical_ids) {
					$this->request->get['path'] = implode('_', $canonical_ids);
				}
				$categorys_id = $canonical_ids ? $canonical_ids : explode('_', (string)$this->request->get['path']);
				$cat_path = '';
				foreach ($categorys_id as $category_id) {
					$query = $this->db->query("SELECT * FROM `" . DB_PREFIX . "seo_url` WHERE `query` = 'category_id=" . (int)$category_id . "' AND `store_id` = '" . (int)$this->config->get('config_store_id') . "' AND `language_id` = '" . (int)$this->config->get('config_language_id') . "'");   
					if ($query->num_rows && $query->row['keyword'] /**/ ) {
						$cat_path .= '/' . $query->row['keyword'];
					} else {
						$cat_path = false;
						break;
					}
				}
				$arg = trim($cat_path, '/');
				if (isset($this->request->get['page'])) $arg = $arg . '?page=' . (int)$this->request->get['page'];
			} elseif ($this->request->get['route'] == 'product/manufacturer/info' && isset($this->request->get['manufacturer_id'])) {
				$route = 'manufacturer_id=' . (int)$this->request->get['manufacturer_id'];
				if (isset($this->request->get['page'])) $arg = $arg . '?page=' . (int)$this->request->get['page'];
			} elseif ($this->request->get['route'] == 'information/information' && isset($this->request->get['information_id'])) {
				$route = 'information_id=' . (int)$this->request->get['information_id'];
			} elseif (sizeof($this->request->get) > 1) {
				$args = '?' . str_replace("route=" . $this->request->get['route'].'&amp;', "", $this->request->server['QUERY_STRING']);
				$arg = str_replace('&amp;', '&', $args);
			}

			$query = $this->db->query("SELECT * FROM `" . DB_PREFIX . "seo_url` WHERE `query` = '" . $this->db->escape($route) . "' AND `store_id` = '" . (int)$this->config->get('config_store_id') . "' AND `language_id` = '" . (int)$this->config->get('config_language_id') . "'");

			if (!empty($query->num_rows) && !empty($query->row['keyword']) && $route) {
				$this->response->redirect($query->row['keyword'] . $arg, 301);
			} elseif ($cat_path) {
				$this->response->redirect('katalog/' . $arg, 301);
			} elseif ($this->request->get['route'] == 'common/home') {
				$this->response->redirect(HTTP_SERVER . $arg, 301);
			}
		}
	}

	public function rewrite($link) {
		$url_info = parse_url(str_replace('&amp;', '&', $link));

		$url = '';

		$data = array();

		parse_str($url_info['query'], $data);

		foreach ($data as $key => $value) {
			if (isset($data['route'])) {
				if (($data['route'] == 'product/product' && $key == 'product_id') || (($data['route'] == 'product/manufacturer/info' || $data['route'] == 'product/product') && $key == 'manufacturer_id') || ($data['route'] == 'information/information' && $key == 'information_id') || ($data['route'] == 'blog/post' && $key == 'blog_post_id') || ($data['route'] == 'blog/category' && $key == 'blog_category_id')) {
					$query = $this->db->query("SELECT * FROM " . DB_PREFIX . "seo_url WHERE `query` = '" . $this->db->escape($key . '=' . (int)$value) . "' AND store_id = '" . (int)$this->config->get('config_store_id') . "' AND language_id = '" . (int)$this->config->get('config_language_id') . "'");

					if ($query->num_rows && $query->row['keyword']) {
						$url .= '/' . $query->row['keyword'];

						unset($data[$key]);
						if ($key == 'blog_post_id' || $key == 'blog_category_id') {
							unset($data['route']);
						}
					}
				} elseif ($key == 'path') {
					$canonical_ids = $this->site002CanonicalCategoryPath($value);
					$categories = $canonical_ids ? $canonical_ids : explode('_', $value);

					foreach ($categories as $category) {
						$query = $this->db->query("SELECT * FROM " . DB_PREFIX . "seo_url WHERE `query` = 'category_id=" . (int)$category . "' AND store_id = '" . (int)$this->config->get('config_store_id') . "' AND language_id = '" . (int)$this->config->get('config_language_id') . "'");

						if ($query->num_rows && $query->row['keyword']) {
							$url .= '/' . $query->row['keyword'];
						} else {
							$url = '';

							break;
						}
					}

					unset($data[$key]);
				} elseif ($key == 'route') {
					// Blog category/post SEO keywords already include the hub prefix
					// (e.g. blog/news). Skip route→keyword when id rewrite applies,
					// otherwise /blog + /blog/news becomes /blog/blog/news.
					if (!empty($data['blog_post_id']) || !empty($data['blog_category_id'])) {
						continue;
					}
					$query = $this->db->query("SELECT * FROM " . DB_PREFIX . "seo_url WHERE `query` = '" . $this->db->escape($data['route']) . "' AND store_id = '" . (int)$this->config->get('config_store_id') . "' AND language_id = '" . (int)$this->config->get('config_language_id') . "'");
					if ($query->num_rows) /**/ {
						$url .= '/' . $query->row['keyword'];
					}
				}
			}
		}

		if ($url) {
			unset($data['route']);

			$query = '';

			if ($data) {
				foreach ($data as $key => $value) {
					$query .= '&' . rawurlencode((string)$key) . '=' . rawurlencode((is_array($value) ? http_build_query($value) : (string)$value));
				}

				if ($query) {
					$query = '?' . str_replace('&', '&amp;', trim($query, '&'));
				}
			}

			return $url_info['scheme'] . '://' . $url_info['host'] . (isset($url_info['port']) ? ':' . $url_info['port'] : '') . str_replace('/index.php', '', $url_info['path']) . $url . $query;
		} else {
			return $link;
		}
	}
	private function site002CanonicalCategoryPath($path_value) {
		$path_parts = explode('_', (string)$path_value);
		$leaf_id = (int)array_pop($path_parts);
		if ($leaf_id <= 0) {
			return array();
		}
		$query = $this->db->query("SELECT path_id FROM " . DB_PREFIX . "category_path WHERE category_id = '" . (int)$leaf_id . "' ORDER BY level ASC");
		$canonical_ids = array();
		foreach ($query->rows as $row) {
			$canonical_ids[] = (int)$row['path_id'];
		}
		return $canonical_ids;
	}

	private function site002CategorySlugTrail(array $category_ids) {
		$slug_parts = array();
		foreach ($category_ids as $category_id) {
			$keyword_query = $this->db->query("SELECT keyword FROM " . DB_PREFIX . "seo_url WHERE query = 'category_id=" . (int)$category_id . "' AND store_id = '" . (int)$this->config->get('config_store_id') . "' AND language_id = '" . (int)$this->config->get('config_language_id') . "'");
			if ($keyword_query->num_rows && $keyword_query->row['keyword']) {
				$slug_parts[] = $keyword_query->row['keyword'];
			} else {
				return array();
			}
		}
		return $slug_parts;
	}

}
